## Design Intent
The macro segments are the cloud's ten spokes, the data center's SDN segments, and the ground segment's OT zone. The data center's segments match the cloud's teams, with one segment per mission team's data lake zone. The DMZ, the VDI spoke, and Tier 0 are the high-risk classes, each isolated in its own segment. The data center's BMCs, SDN controller management, and HSM management sit on an out-of-band network. It is reachable only through the privileged access platform's session hosts, which Tier 0 reaches from the privileged access workstations.

## External Dependencies
None outside the boundary.
