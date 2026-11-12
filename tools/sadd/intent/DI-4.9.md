## Design Intent
Any asset that cannot be patched gets its own segment, intrusion prevention at its only path, and tighter monitoring. The payload processing workstation is the only candidate, and only if its replacement slips past 2027-09-30. It would sit in its own OT zone segment under application allow-listing. A single conduit would carry its converted recordings to Mission Team 1's data lake zone and nothing else. The data center hub's intrusion prevention signatures would shield its known vulnerabilities at that conduit. The passive sensors and the security monitoring platform would watch it under tighter alert thresholds than the rest of the fleet.

## External Dependencies
Payload Vendor A, whose replacement workstation retires this asset.
