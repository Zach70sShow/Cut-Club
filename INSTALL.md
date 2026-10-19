# Install Cut Club 0.3.22 on Mac

1. Install Adobe Creative Cloud Desktop and Premiere Pro 26.5.1 or later. This guided flow requires macOS 13 or later and 3 GB of free space. Windows is not validated.
2. Export your personal Cut Club library if you have one. Save and close Premiere. If you previously loaded Cut Club through UXP Developer Tools, unload/remove that development registration; preserve your source files.
3. Download **Cut-Club-0.3.22-Direct-Install.zip** and fully extract it. Keep all files together. Open **START-HERE.html** for the illustrated step-by-step guide.
4. Open Terminal. Type `bash` followed by a space, drag **Install-Cut-Club.command** from the extracted folder into Terminal, then press Return. The script checks the bundled CCX checksum, Adobe's installer, compatible Premiere, free space and whether Premiere is closed. It asks you to type **INSTALL** before invoking Adobe's official UPIA installer. No Developer Mode, Apple Developer ID or custom unsigned application is required.
5. Wait for the script's confirmed success. Do not start another installation at the same time. Reopen Premiere and choose **Window → UXP Plugins → Cut Club**.
6. Use a saved duplicate test project containing real footage and a plain Premiere text/graphic clip. Place the playhead on a covered cut with enough footage on both sides (20 frames each for a default 40-frame transition). Try the Add button and double-click, insert again at a second cut, and check text preservation and Undo/Redo. Follow the actual Undo count shown by the panel.

The ZIP includes exactly the same CCX as the standalone download. Choose one installation route. The script uses Adobe's existing tool; it does not copy files into Adobe's plugin directories, change Developer Mode or weaken macOS protections. Keep the previous release for rollback through Adobe's normal plugin management.

## If installation fails

Read the complete message in Terminal. The installer writes a local Cut Club installation log under your user Library/Logs folder. Share the Adobe error code and plugin/Premiere/macOS versions, with private paths removed. Do not repeatedly run concurrent installers. Missing Adobe UPIA generally requires repairing or updating Creative Cloud Desktop from Adobe's official source. Do not bypass Gatekeeper, edit Adobe's registry or manually replace installed plugin files.

For the standalone CCX, use Adobe Creative Cloud's supported installation or the [official UPIA instructions](https://helpx.adobe.com/creative-cloud/apps/integration-with-other-apps/manage-plugins/install-plugins-using-upia-tool.html). Double-clicking a CCX may not work on every setup.

## Workflow notes

Single-click opens controls; double-click inserts defaults. Fonts: Helvetica Neue; Lumen Credit also uses Didot. Fonts are not included. Edit title wording in Premiere Properties. After manually trimming premium motion titles, match Animation duration (seconds) to the clip; after a frame-rate change, match Timeline frame rate. The panel sets those values on insertion.

Reconnect your exported personal-library folder after moving computers. Do not delete generated native sources while saved projects or Undo may reference them. No automatic update checker ships.

This is a prerelease. Native acceptance on macOS 27.0 / Premiere 26.5.2 is pending; other documented intermittent insertion and crash issues remain unresolved.
