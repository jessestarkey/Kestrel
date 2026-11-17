## Design Intent
The DMZ's edge services, the API gateway, and the service mesh report every API endpoint actually answering requests, east-west calls included. Each is compared with the schemas registered at intake, so an undocumented route or a retired version still answering is flagged to its owning team.

## External Dependencies
None outside the boundary.
