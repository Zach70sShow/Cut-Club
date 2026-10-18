# Cut Club

Original transitions, editable motion graphics, overlays and a personal asset library for Adobe Premiere Pro.

[Download the preview release](https://github.com/Zach70sShow/Cut-Club/releases/tag/v0.3.20) · [Installation](INSTALL.md) · [Release notes](RELEASE-NOTES.md) · [Report an issue](https://github.com/Zach70sShow/Cut-Club/issues)

## Status: prerelease

Version **0.3.20** is a review build. Intermittent long-session Premiere native insertion failures remain unresolved, and a native crash occurred during extended QA. Save your project and test on a duplicate before production work. Windows and a second clean Mac are not validated.

## Included

- 25 original cards: 12 transition profiles across five native mechanisms, nine title/counter designs, and four overlays.
- 60 genuine editable MOGRT variants and six alpha-overlay movies.
- Landscape and portrait formats at 720p, 1080p and 4K.
- Search, category filters, compact layout, preview-size slider and hover previews.
- Personal-library capture, portable export, reconnect and recovery tools.
- A Cut Club project bin for generated/imported supporting items.

Requires Adobe Creative Cloud Desktop and **Premiere Pro 26.5.1 or later**. Current validation is on Apple Silicon macOS. Fonts are not bundled: titles use Helvetica Neue; Lumen Credit also uses Didot.

## Install

Download `Cut-Club-0.3.20.ccx` from Releases. Save and close Premiere, unload any same-ID development registration in UXP Developer Tools, open the CCX and follow Adobe's installer. Then open **Window → UXP Plugins → Cut Club**. Read [INSTALL.md](INSTALL.md) for important workflow and recovery details.

The CCX belongs in GitHub Release assets rather than Git history. This repository holds public distribution documentation, release metadata and verification tools. The owner's private development/authoring archive is distributed separately; it is not part of the public repository.

## Verify

Expected CCX SHA-256:

`c2ce4b070b9808fe4689c4379d36a0b7eb9e919e2b9ad9c0103c94c0d6336616`

`SHA256SUMS` covers the original five-file release bundle. Download all five Release assets into one directory, then run:

```sh
python3 verify_bundle.py --bundle /path/to/downloaded-release --metadata release.json
```

The verifier checks hashes, archive integrity, identity, host requirements and permissions. It does not install the plugin or certify native stability. `audit_privacy.py` provides an additional bounded native-container metadata check; it is not a general secrets scanner.

## Updates

Updates will appear on the [Releases page](https://github.com/Zach70sShow/Cut-Club/releases). The current plugin has no in-panel update checker or automatic installer. Export your personal library before updating; install updates through Adobe's CCX flow. `release.json` is public release metadata prepared for future update support, not a working updater.

## Feedback

Use Issues with the plugin/Premiere/macOS versions, sequence format and frame rate, exact steps, expected result and actual result. Remove private footage, names, file paths and credentials from attachments. Do not upload client projects.

## Rights

Cut Club uses original branding, code and assets. Public availability of this distribution repository does not grant an open-source license or redistribution rights. Adobe applications and fonts are obtained separately. No third-party commercial effect packs are included.
