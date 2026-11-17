## Design Intent
Scheduled scans evaluate every surface against its baseline. Authenticated scans with DISA SCAP content cover hosts, configuration checks cover the cloud, and benchmark checks cover containers. Fleet equipment is checked against its manufacturer baseline only in maintenance windows or on landed aircraft, never by active scan in flight, and its drift alerts the owner without automated correction. Results feed one compliance status view. Each finding is tracked to closure under the VPMP's deadlines, and bound to a POA&M item if it will miss one.

## External Dependencies
DISA, which publishes the STIGs and SCAP content the scans use.
