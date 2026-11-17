## Design Intent
Any asset that cannot be patched gets its own segment, virtual patching at its only path, and tighter monitoring. If no such asset is fielded, the pattern is validated on a spare station. The payload processing workstation is the one candidate, and it connects only if the AO re-dates CCSD tailoring action 3. It would then sit in its own OT zone under application allow-listing, with an inbound conduit from the station zone and an outbound one to the IT/OT DMZ. Both cross the ground segment firewall, whose threat signatures shield its known vulnerabilities. Its recordings would land in Mission Team 1's zone over F3, under tighter alert thresholds than the rest of the fleet.

## External Dependencies
Payload Vendor A, whose replacement workstation retires this asset.
