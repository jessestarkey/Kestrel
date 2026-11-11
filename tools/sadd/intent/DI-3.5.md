## Design Intent
Fleet Operations adopts each manufacturer's hardening guidance for the ground control stations, launch and recovery equipment, and aircraft. The payload processing workstation cannot be hardened to a current baseline, so its baseline is a set of compensating controls. These are isolation in the OT zone, application allow-listing, and a single firewalled conduit to Mission Team 1's data lake zone, per CCSD tailoring action 3. Approved firmware for each aircraft and station model is tracked in the inventory.

## External Dependencies
The aircraft and ground equipment manufacturers, for hardening guidance and approved firmware. Payload Vendor A, which certifies its conversion software only on the workstation's current operating system.
