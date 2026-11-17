## Design Intent
KESTREL's equivalent of a TT&C link is the aircraft datalinks, so CCSDS SDLS itself does not apply. The command uplink is authenticated, encrypted, and protected against replay, so an aircraft executes only fresh commands from a KESTREL ground control station. The telemetry and payload downlink is encrypted and integrity-protected. The links use CNSA algorithms under CNSSP 15 on FIPS 140-3 modules, protecting CCSD row 6's High integrity with row 13's key material. Stations alert operators to link anomalies and jamming indicators, and those alerts also reach the Security Team.

## External Dependencies
The aircraft and datalink manufacturers, who supply the datalink crypto modules.
