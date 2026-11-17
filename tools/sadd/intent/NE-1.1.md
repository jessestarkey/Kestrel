## Design Intent
The hubs, the alternate site firewall, and the SDN controller take their rules from one shared rule base. It is kept as policy as code in the Platform Team's repository and deployed by the pipeline over F35. Each operating site's ground segment firewall keeps its own rule set in Fleet Operations' repository, since the conduit stays a separate boundary. It is loaded from a maintenance console in a window. A rule change is a pull request with a second reviewer, and changes to the shared rule base go to the Configuration Control Board. The pipeline compares every firewall's running policy with its repository and alerts on any difference.

## External Dependencies
None outside the boundary.
