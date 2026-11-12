## Design Intent
The ground segment has four zones, namely aircraft and datalinks, ground control stations, launch and recovery, and the payload processing workstation. The station and aircraft zones carry security level target 3, and the others carry 2. One conduit joins the ground segment to the data center through an IT/OT DMZ. Recordings and model packages are staged there, so no session spans IT and OT. The passive sensors watch every zone-to-zone flow, and the penetration testers validate the zones on spares.

## External Dependencies
None outside the boundary.
