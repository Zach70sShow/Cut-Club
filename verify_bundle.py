"""Offline inspection of the five reviewed Cut Club release assets; never installs."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile

VERSION = re.compile(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)')
DIGEST = re.compile(r'[0-9a-f]{64}')
MAX_CCX_BYTES = 1024 ** 3
MAX_EXPANDED_BYTES = 2 * 1024 ** 3
MAX_ENTRY_BYTES = 256 * 1024 ** 2
_privacy_spec = importlib.util.spec_from_file_location('cutclub_release_privacy', Path(__file__).with_name('audit_privacy.py'))
_privacy = importlib.util.module_from_spec(_privacy_spec)
_privacy_spec.loader.exec_module(_privacy)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(data):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'Duplicate JSON key')
            result[key] = value
        return result
    def constant(_):
        raise ValueError('Non-finite JSON number')
    return json.loads(data, object_pairs_hook=unique, parse_constant=constant)


def digest(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 ** 2), b''):
            result.update(chunk)
    return result.hexdigest()


def inspect_ccx(path, metadata):
    with zipfile.ZipFile(path) as archive:
        entries = archive.infolist()
        require(0 < len(entries) <= 10000, 'Unexpected archive entry count')
        seen = set()
        total = 0
        for entry in entries:
            name = entry.filename
            parsed = PurePosixPath(name)
            require(name and not name.startswith('/') and '\\' not in name and
                    ':' not in name and not any(ord(c) < 32 for c in name) and
                    not any(p in ('', '.', '..') for p in name.rstrip('/').split('/')) and
                    parsed.as_posix() == name.rstrip('/'), 'Unsafe archive path')
            key = name.rstrip('/').casefold()
            require(key not in seen, 'Duplicate or case-ambiguous archive path')
            seen.add(key)
            require(not stat.S_ISLNK(entry.external_attr >> 16), 'Symlink archive entry')
            require(not entry.flag_bits & 1, 'Encrypted archive entry')
            require(entry.file_size <= MAX_ENTRY_BYTES, 'Oversized archive entry')
            require(entry.file_size <= max(1, entry.compress_size) * 500,
                    'Excessive archive expansion ratio')
            total += entry.file_size
            require(total <= MAX_EXPANDED_BYTES, 'Archive expansion limit exceeded')
            require(not parsed.name.startswith('qa-'), 'Temporary QA module')
        names = {e.filename for e in entries if not e.is_dir()}
        require({'manifest.json', 'package.json', 'main.js', 'index.html'} <= names,
                'Missing required plugin files')
        require(archive.getinfo('manifest.json').file_size <= 1024 ** 2 and
                archive.getinfo('package.json').file_size <= 1024 ** 2 and
                archive.getinfo('main.js').file_size <= 2 * 1024 ** 2,
                'Oversized plugin metadata or entrypoint')
        manifest = read_json(archive.read('manifest.json'))
        package = read_json(archive.read('package.json'))
        require(manifest.get('id') == metadata['pluginId'], 'Unexpected plugin identity')
        require(manifest.get('version') == metadata['version'] == package.get('version'),
                'Plugin version differs from release metadata')
        require(manifest.get('host') == metadata['host'], 'Host compatibility differs')
        require(manifest.get('requiredPermissions') == metadata['permissions'],
                'Plugin permissions differ from reviewed release metadata')
        require(b'CUTCLUB_TEMPORARY_QA' not in archive.read('main.js'), 'Temporary QA injection')
        require(archive.testzip() is None, 'Archive CRC failure')
        privacy = _privacy.audit_archive(archive)
        require(privacy['passed'], 'Local authoring metadata in release package')
        return {'files': len(names), 'expandedBytes': total, 'localMetadataAudit': privacy}


def verify(bundle, metadata):
    version = metadata.get('version', '')
    require(isinstance(version, str) and VERSION.fullmatch(version), 'Invalid release version')
    require(metadata.get('schemaVersion') == 1, 'Unsupported release metadata')
    require(metadata.get('channel') in ('prerelease', 'stable'), 'Explicit release channel required')
    require(type(metadata.get('nativeAcceptanceApproved')) is bool, 'Native review decision required')
    require(metadata['channel'] != 'stable' or metadata['nativeAcceptanceApproved'],
            'Stable release blocked: native acceptance is incomplete')
    installer = 'Cut-Club-' + version + '.ccx'
    require(metadata.get('installer') == installer, 'Unexpected installer name')
    require(DIGEST.fullmatch(metadata.get('sha256', '')), 'Invalid reviewed installer digest')
    require(type(metadata.get('bytes')) is int and 0 < metadata['bytes'] <= MAX_CCX_BYTES,
            'Invalid reviewed installer size')
    require(not bundle.is_symlink() and bundle.is_dir(), 'Real release directory required')
    names = {installer, 'INSTALL.md', 'README.md', 'RELEASE-NOTES.md', 'SHA256SUMS'}
    require({p.name for p in bundle.iterdir()} == names, 'Release file allowlist differs')
    for name in names:
        path = bundle / name
        require(not path.is_symlink() and path.is_file(), 'Redirected or missing release asset')
        limit = MAX_CCX_BYTES if name == installer else 256 * 1024
        require(path.stat().st_size <= limit, 'Oversized release asset')
    require((bundle / installer).stat().st_size == metadata['bytes'], 'Installer byte count differs')
    sums = {}
    for line in (bundle / 'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.-]+)', line)
        require(match is not None, 'Malformed checksum line')
        hashed, name = match.groups()
        require(name not in sums, 'Duplicate checksum entry')
        sums[name] = hashed
    require(set(sums) == names - {'SHA256SUMS'}, 'Checksum file set differs')
    for name, expected in sums.items():
        require(digest(bundle / name) == expected, 'Checksum mismatch: ' + name)
    require(sums[installer] == metadata['sha256'], 'Installer differs from independently reviewed digest')
    for name in ('INSTALL.md', 'README.md', 'RELEASE-NOTES.md'):
        text = (bundle / name).read_text(encoding='utf-8')
        require(not re.search(r'file://|/Users/|/var/folders/', text), 'Local path in public documentation')
    archive = inspect_ccx(bundle / installer, metadata)
    return {'version': version, 'channel': metadata['channel'],
            'installerSha256': sums[installer], 'assets': sorted(names), **archive,
            'packageIntegrity': 'passed', 'nativeAcceptanceApproved': metadata['nativeAcceptanceApproved'],
            'nativeAcceptance': 'Publisher review assertion; cannot be established by archive inspection',
            'published': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle', required=True, type=Path)
    parser.add_argument('--metadata', required=True, type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(verify(args.bundle, read_json(args.metadata.read_bytes())), indent=2))
    except (ValueError, KeyError, TypeError, OSError, zipfile.BadZipFile, RuntimeError) as error:
        parser.exit(1, 'Release verification failed: ' + str(error) + '\n')
