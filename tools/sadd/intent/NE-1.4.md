## Design Intent
The macro segments are the cloud's ten spokes, the data center's SDN segments, the alternate site's zones, the IT/OT DMZ, and the ground segment's OT zone. The data center's segments match the cloud's teams, and each mission team's data lake zone is reachable only from that team's spokes and the ML training zone. The DMZ, the VDI spoke, and Tier 0 are the high-risk classes, each isolated in its own segment. Management interfaces at every site sit on an out-of-band network reached only through the privileged access platform's session hosts. Cloud control planes are reached the same way, over the circuit through a private link.

## External Dependencies
None outside the boundary.
