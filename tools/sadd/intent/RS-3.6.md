## Design Intent
Restoration uses only backups, images, and model versions from before the earliest confirmed adversary activity, and each source is checked for the incident's indicators before it is used. With no clean source, systems are rebuilt from infrastructure as code or golden images with a selective data restore. A recovered system stays under heightened monitoring for 30 days.

## External Dependencies
None outside the boundary.
