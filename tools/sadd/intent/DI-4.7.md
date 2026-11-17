## Design Intent
Fleet Operations exports each station's and launch system's configuration during maintenance windows and compares it against the manufacturer baseline. The passive sensors add firmware and protocol behavior between windows. Each aircraft's firmware and loaded model version are checked against Secure OT/Legacy Device Baselines (`DI-3.5`) when it connects to a station or enters maintenance. Drift alerts go to Fleet Operations and the Security Team, and nothing is changed automatically on fleet equipment.

## External Dependencies
None outside the boundary.
