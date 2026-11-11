## Design Intent
Fleet Operations captures each ground control station's configuration, the launch and recovery equipment's logic, and each aircraft's firmware and model versions during maintenance windows, using the manufacturers' offline tools. The payload processing workstation is backed up as a full disk image, since its software cannot be reinstalled on a supported system. Restores to fleet equipment happen only in a maintenance window with Fleet Operations present.

## External Dependencies
The aircraft and ground equipment manufacturers, whose offline backup tools capture the equipment's configuration.
