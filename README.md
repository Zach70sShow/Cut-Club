# Cut Club 0.3.21

Original transitions, editable motion graphics, overlays and a personal asset library for Adobe Premiere Pro.

[Download 0.3.21](https://github.com/Zach70sShow/Cut-Club/releases/tag/v0.3.21) · [Installation](INSTALL.md) · [Release notes](RELEASE-NOTES.md) · [Report an issue](https://github.com/Zach70sShow/Cut-Club/issues)

## Status: prerelease

This hotfix handles plain Premiere text/graphic clips that have no ProjectItem and keeps insertion errors visible. Automated regressions pass; native acceptance on the reported macOS 27.0 / Premiere 26.5.2 computer is pending. Other intermittent native insertion/handle failures and the previously observed extended-session crash are not declared fixed. Save and test a duplicate project first. Windows is not validated.

## Install on Mac

Download **Cut-Club-0.3.21-Direct-Install.zip**, fully extract it, and open **START-HERE.html**. The bundle includes the plugin and a guided script that calls Adobe's official installer. The guide explains the Terminal steps; double-clicking a CCX alone is not the required workflow. No Apple Developer ID or UXP Developer Mode is needed for this route. Adobe Creative Cloud Desktop, macOS 13 or later, and Premiere Pro 26.5.1 or later are required. Save and close Premiere before installing.

The standalone **Cut-Club-0.3.21.ccx** is also provided for Adobe-managed installation. Do not install both copies separately. Read INSTALL.md first.

## Included

- 25 original cards: 12 transition profiles across five native mechanisms, nine title/counter designs, and four overlays.
- 60 genuine editable MOGRT variants and six alpha-overlay movies.
- Landscape and portrait formats at 720p, 1080p and 4K.
- Search, category filters, compact layout, preview-size slider and hover previews.
- Personal-library capture, portable export, reconnect and recovery tools.
- A Cut Club project bin for generated/imported supporting items.

Fonts are not bundled: titles use Helvetica Neue; Lumen Credit also uses Didot. This hotfix changes no effect content or plugin permissions.

## Verification and updates

SHA256SUMS covers all other assets in this release. After downloading them into one directory, macOS users can run `shasum -a 256 -c SHA256SUMS`. Checksums verify the downloads; they do not certify native stability.

Updates appear on the [Releases page](https://github.com/Zach70sShow/Cut-Club/releases). No in-panel update checker or automatic updater ships. Export your personal library before updating and retain the previous installer for recovery.

This repository holds public distribution documentation and metadata. The owner's development archive is separate. Public availability does not grant an open-source license or redistribution rights. No third-party commercial effect packs are included. Do not upload client projects, private paths or credentials when reporting issues.
