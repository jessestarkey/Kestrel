## Design Intent
KESTREL's equivalent of a TT&C link is the aircraft datalinks, so CCSDS SDLS itself does not apply. The command uplink is authenticated and encrypted, so an aircraft executes only commands from a KESTREL ground control station. The telemetry and payload downlink is encrypted and integrity-protected. The keys are CCSD row 13's key material, held in the HSMs and the datalink crypto modules. Stations alert operators to link anomalies and jamming indicators, and those alerts also reach the Security Team.

## External Dependencies
The aircraft and datalink manufacturers, who supply the datalink crypto modules.
