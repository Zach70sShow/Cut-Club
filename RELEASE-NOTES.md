# Cut Club 0.3.22 — text/graphic insertion fix

Fixes a second null-ProjectItem failure: after inserting a transition, Cut Club could incorrectly check unrelated native text or graphics on the destination track as if they were Cut Club layers. These clips are now handled separately, while preservation checks for existing clips and ownership checks for the inserted transition remain active. Includes the earlier source-less snapshot and persistent error-message fixes.

## Verified

- Four Side Current insertions in a real test sequence containing native text with a null ProjectItem: Add, search-card double-click and repeated insertion without reload.
- Insertion onto the same track as the text graphic, outside its interval.
- All 144 original timeline items retained their tracks, timing, source ranges and names.
- Two placement Undo steps and Redo restored the expected timelines; animated blur controls read back correctly.
- All 30 JavaScript test files / 38 runner entries pass, including the regression that fails against published 0.3.21.
- Official Adobe CCX installed successfully; all 3,663 installed files match the package/source. Premiere restarted and the saved test sequence and installed panel reopened. No additional insertion was performed after that restart.

Native testing was on Premiere 26.5.1 / macOS 27.0.1. The reported second computer running Premiere 26.5.2 / macOS 27.0 still needs validation. This is a prerelease, not a claim that every native reliability issue is resolved.

## Install

Download **Cut-Club-0.3.22-Direct-Install.zip**, extract it, and open **START-HERE.html**. Save and close Premiere before running the included script according to the guide. It invokes Adobe's official installer and does not require UXP Developer Mode or an Apple Developer ID. Double-clicking a CCX alone is not a dependable installation flow.

The guide must be opened manually; this release does not yet provide the requested native installer window. No automatic updater ships. Windows, fresh-machine installation and extended-session reliability remain unvalidated. Back up your personal library and test on a duplicate project.
