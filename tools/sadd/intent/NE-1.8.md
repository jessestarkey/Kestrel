## Design Intent
The command and payload datalinks are KESTREL's only authorized wireless, and their authenticated encryption under Telemetry, Tracking, and Command (TT&C) Link Security (`NE-2.8`) meets the wireless authentication requirement. No wireless LAN exists anywhere in KESTREL. Embedded radios are disabled on every server, workstation, and station, apart from the station datalink radios. Wireless sensors at the data center, the alternate site, and each operating site look for rogue access points and alert the Security Team.

## External Dependencies
None outside the boundary.
