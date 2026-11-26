# MP: Media Protection

## MP-1

The program manager will issue the media protection policy as part of KESTREL's system security policy. The media protection procedures, which Fleet Operations and IT Operations write, will carry it out. The Configuration Control Board will approve both, and each will be reviewed at least once a year.

## MP-2

Removable media will be prohibited except for three classes: each aircraft's mission storage modules, encrypted government media carrying prior collection, and the datalink key loaders. Mission storage modules can be read only at a ground control station and the IT/OT DMZ, and key loaders are held under two-person custody. Across the IT estate, removable storage is blocked by policy.

## MP-3

Mission storage modules will be marked CUI, and so will every other piece of removable media KESTREL holds.

## MP-4

Mission storage modules will be kept in each station's locked store when they are not in an aircraft. Key loaders are stored under two-person custody.

## MP-5

Mission storage modules will be encrypted under keys in the aircraft's crypto module, logged when they leave an aircraft, and carried by a named custodian in controlled containers. Encrypted government media is carried to the media intake station.

## MP-6

Media will be sanitized before it leaves KESTREL's control. Failed drives and retired storage modules are purged on site with Blancco to NIST SP 800-88 and verified. Retired or repaired HSMs and datalink crypto modules are zeroized. Cloud storage media is sanitized by the provider under its authorization.

## MP-6(1)

Each sanitization will be reviewed, approved, tracked, documented, and verified. The decommissioning record in Jira Service Management holds the method, the result, and a certificate of destruction for each item.

## MP-6(2)

Sanitization equipment and procedures will be tested so they keep achieving the intended result. Blancco verifies each wipe as it completes, and the equipment is checked on a schedule.

## MP-7

Removable storage will be blocked on every workstation, desktop, and server by device control policy. The one exception is the media intake station, which reads only encrypted government media. Mission storage modules are used only in aircraft and ground control stations.
