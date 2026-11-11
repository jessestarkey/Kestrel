## Design Intent
Remove vendor-default credentials from the aircraft, ground control stations, and launch and recovery equipment before they field. Each aircraft and station authenticates with its device identity on the datalinks, and equipment that cannot authenticate itself is identified by its zone and conduit placement.

## External Dependencies
The aircraft and ground station vendors, whose devices must accept program-issued identities.
