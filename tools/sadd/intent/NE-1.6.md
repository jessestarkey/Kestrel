## Design Intent
The ground segment at each operating site has five zones, namely aircraft and datalinks, ground control stations, launch and recovery, the operating site services, and the payload processing workstation's reserved zone. The station, aircraft, and launch zones carry security level target 3, and the others carry 2. The IT/OT DMZ carries 3. Each site has its own conduit, terminating on its ground segment firewall and carried to the IT/OT DMZ in an encrypted tunnel over DISN (F33). Recordings and model packages are staged in the DMZ, so no session spans IT and OT. The workstation's zone stays empty unless the AO re-dates CCSD tailoring action 3.

## External Dependencies
DISA, which provides each operating site's DISN transport.
