"""Check distributable bytes for local home paths, including native containers.

This is a bounded metadata hygiene check, not a general sensitive-data detector.
Reports contain only relative asset/member names, never the matched path.
"""
from pathlib import Path
import gzip
import io
import re
import stat
import zipfile

PREFIXES = [prefix.encode(codec) for prefix in ['/Users/', '/home/', 'file:///Users/', 'file:///home/']
            for codec in ['utf-8', 'utf-16-le', 'utf-16-be']]
WINDOWS = re.compile(rb'[A-Za-z]:[\\/]Users[\\/]', re.I)
WINDOWS_LE = re.compile(rb'[A-Za-z]\x00:\x00[\\/]\x00U\x00s\x00e\x00r\x00s\x00[\\/]\x00', re.I)
WINDOWS_BE = re.compile(rb'\x00[A-Za-z]\x00:\x00[\\/]\x00U\x00s\x00e\x00r\x00s\x00[\\/]', re.I)
MAX_EXPANDED = 64 * 1024 * 1024


def contains_home_path(data):
    return any(prefix in data for prefix in PREFIXES) or any(
        pattern.search(data) is not None for pattern in [WINDOWS, WINDOWS_LE, WINDOWS_BE])


def _audit_entries(entries):
    findings, expanded, scanned = [], 0, 0

    def inspect(data, filename, member='', depth=0):
        nonlocal expanded
        if depth > 3:
            raise RuntimeError('Native metadata nesting exceeds inspection limit')
        if contains_home_path(data):
            findings.append({'file': filename, 'member': member, 'kind': 'local authoring path'})
        if data.startswith(b'\x1f\x8b'):
            with gzip.GzipFile(fileobj=io.BytesIO(data)) as stream:
                raw = stream.read(MAX_EXPANDED + 1)
            if len(raw) > MAX_EXPANDED:
                raise RuntimeError('Native metadata exceeds inspection limit')
            expanded += 1
            inspect(raw, filename, member + '!gzip', depth + 1)
        elif depth < 2 and zipfile.is_zipfile(io.BytesIO(data)):
            with zipfile.ZipFile(io.BytesIO(data)) as archive:
                entries = archive.infolist()
                if len(entries) > 512 or sum(e.file_size for e in entries) > MAX_EXPANDED:
                    raise RuntimeError('Native metadata archive exceeds inspection limit')
                for entry in entries:
                    if entry.is_dir():
                        continue
                    expanded += 1
                    inspect(archive.read(entry), filename, member + '!' + entry.filename, depth + 1)

    for name, size, symlink, opener in entries:
        if symlink:
            raise RuntimeError('Release metadata inspection rejects symlinks')
        scanned += 1
        if Path(name).suffix.lower() in {'.prproj', '.mogrt', '.aegraphic'}:
            if size > MAX_EXPANDED:
                raise RuntimeError('Native container exceeds inspection limit')
            with opener() as stream:
                data = stream.read(MAX_EXPANDED + 1)
            if len(data) > MAX_EXPANDED:
                raise RuntimeError('Native container exceeds inspection limit')
            inspect(data, name)
        else:
            # Bound memory for the large original alpha movies. Keep overlap
            # so a path prefix straddling two reads cannot disappear.
            tail = b''
            with opener() as stream:
                while chunk := stream.read(256 * 1024):
                    data = tail + chunk
                    if contains_home_path(data):
                        findings.append({'file': name, 'member': '', 'kind': 'local authoring path'})
                        break
                    tail = data[-64:]
    return {'passed': not findings, 'filesScanned': scanned,
            'expandedContainers': expanded, 'findings': findings,
            'scope': 'local home-path metadata patterns; not a general secret scan'}


def audit(folder):
    folder = Path(folder)
    entries = ((p.relative_to(folder).as_posix(), p.stat().st_size, p.is_symlink(),
                lambda p=p: p.open('rb')) for p in sorted(folder.rglob('*'))
               if p.is_file() or p.is_symlink())
    return _audit_entries(entries)


def audit_archive(archive):
    """Stream an already path-validated CCX; never extracts files to disk."""
    entries = ((e.filename, e.file_size, stat.S_ISLNK(e.external_attr >> 16),
                lambda e=e: archive.open(e)) for e in archive.infolist() if not e.is_dir())
    return _audit_entries(entries)
