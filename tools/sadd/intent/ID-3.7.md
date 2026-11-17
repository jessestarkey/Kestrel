## Design Intent
Remove vendor-default credentials from the aircraft, ground control stations, launch and recovery equipment, and operating site services before they field. Each aircraft and station authenticates with its device identity on the datalinks, and device credentials rotate in maintenance windows. Equipment that cannot authenticate itself, such as launch and recovery equipment with fixed controllers, is identified by its zone and conduit placement.

## External Dependencies
The aircraft and ground station vendors, whose devices must accept program-issued identities.
