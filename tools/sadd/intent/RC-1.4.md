## Design Intent
Fleet Operations captures each ground control station's configuration, the launch and recovery equipment's logic, and each aircraft's firmware and model versions during maintenance windows, using the manufacturers' offline tools. Captures exclude the datalink crypto modules' key material, which is restored only by a key loader fill under HSM and Hardware Root-of-Trust Management (`DA-3.4`). Each capture is kept with its prior versions, date, and change record in the backup and archive. Station configuration changes only in windows, which holds Tier 1's recovery point. Restores happen in a maintenance window with Fleet Operations present. Outside a window, only the operations lead may authorize an emergency restore, never to a station with an aircraft airborne under its control.

## External Dependencies
The aircraft and ground equipment manufacturers, whose offline backup tools capture the equipment's configuration.
