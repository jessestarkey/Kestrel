## Design Intent
Fleet Operations adopts each manufacturer's hardening guidance for the ground control stations, launch and recovery equipment, aircraft, and operating site services. Windows-based stations take the DISA STIG unless the manufacturer documents a conflict, plus allow-listing and anti-malware where supported. An asset that cannot reach a current baseline gets a compensating control baseline instead. The payload processing workstation connects only if the AO re-dates CCSD tailoring action 3. It would then run isolated in its own OT zone with application allow-listing. Approved firmware for each model is tracked in the inventory.

## External Dependencies
The aircraft and ground equipment manufacturers, for hardening guidance and approved firmware. Payload Vendor A, which certifies its conversion software only on the workstation's current operating system.
