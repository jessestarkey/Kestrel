## Design Intent
The payload processing workstation is KESTREL's one unpatchable asset. It sits in its own OT zone segment, and a single conduit carries its converted recordings to Mission Team 1's data lake zone and nothing else. The data center hub's intrusion prevention signatures shield its known vulnerabilities at that conduit. The passive sensors and the security monitoring platform watch it under tighter alert thresholds than the rest of the fleet.

## External Dependencies
Payload Vendor A, whose replacement workstation retires this asset.
