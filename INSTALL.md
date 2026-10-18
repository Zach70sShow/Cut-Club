# Install Cut Club 0.3.20

1. Install Adobe Creative Cloud Desktop and Premiere Pro 26.5.1 or later. This review build was tested on Apple Silicon macOS/Premiere 26.5.1. Windows is not yet validated.
2. Save and close Premiere. If you use UXP Developer Tools, unload and remove the Cut Club development registration from its workspace (this removes the developer entry, not your source files). A same-ID development entry can conflict with the installed plugin.
3. Open `Cut-Club-0.3.20.ccx` and complete Adobe's installer. Install only a package received from the Cut Club publisher. No Developer Mode is needed for an ordinary CCX installation.
4. Start Premiere and choose **Window → UXP Plugins → Cut Club**. Adobe Creative Cloud’s plugin management shows the installed version; this panel does not yet display a build number.
5. On a saved test project, double-click a transition card twice at covered cuts, then check Undo/Redo. Try one title and overlay before using the build on a production edit.

Single-click opens controls; double-click adds defaults. Put the playhead on the intended cut. Cut Club chooses the supported sequence format and a safe track above the active video. Cut markers belong to the adjustment-layer source and follow its clip. Follow the Undo count reported after the operation; transition placement and project import/bin setup occupy distinct history stages, and title/movie workflows have their own counts.

Titles require Helvetica Neue; Lumen Credit also uses Didot. Fonts are not embedded or included. Edit wording and controls in Premiere Properties. After manually trimming the four premium motion families, match **Animation duration (seconds)** to the clip; after changing sequence frame rate, match **Timeline frame rate**. The panel sets those values on insertion.

Your custom library stays in a folder you select. Export it before updating or moving computers. Reconnect the exported folder after a move; personal Clear/Remove actions preserve original asset files. Do not delete Cut Club's generated native sources while saved projects or Undo may reference them.

If the panel is absent after an update, close Premiere and repeat Adobe's installation, then reopen. Do not copy files manually into Adobe's plugin folders or edit its registry. For managed installs Adobe provides an [official UPIA command-line installer](https://helpx.adobe.com/creative-cloud/apps/integration-with-other-apps/manage-plugins/install-plugins-using-upia-tool.html). Record the Adobe error and contact the publisher if installation still fails.

Keep the previous CCX for recovery. A downgrade should use Adobe's normal plugin management/installation, with a personal-library export first. This build does not modify other installed plugins or require access to third-party asset accounts.
