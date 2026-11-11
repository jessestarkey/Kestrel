## Design Intent
Both hubs and the SDN controller take their rules and routes from one rule base, defined once as policy as code in the Platform Team's repository and deployed to each side by the pipeline. A rule change is a pull request with a second reviewer, and changes to the shared rule base go to the Configuration Control Board. The pipeline compares each hub's running policy with the repository and alerts on any difference.

## External Dependencies
None outside the boundary.
