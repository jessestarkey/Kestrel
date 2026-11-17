## Design Intent
Removable media is prohibited except for three classes. The aircraft's mission storage modules are encrypted under keys in the aircraft's crypto module, readable only at the ground control station and the IT/OT DMZ. They are marked CUI, logged when they leave an aircraft, carried by a named custodian in controlled containers, and stored in the station's locked store. Encrypted government media carries prior collection to the media intake station. Datalink key loaders are held under two-person custody. Failed drives and retired modules are sanitized on site, retired or repaired HSMs and datalink modules are zeroized, and cloud media sanitization is inherited from the provider.

## External Dependencies
The IL5 cloud provider, which sanitizes cloud media under its provisional authorization.
