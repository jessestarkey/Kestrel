## Design Intent
Every pipeline job runs on a fresh containerized runner in Platform Prod, isolated from concurrent jobs and destroyed when the job ends. No build runs on a performer laptop or a long-lived host.

## External Dependencies
None outside the boundary.
