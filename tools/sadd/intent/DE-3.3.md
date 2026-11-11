## Design Intent
Log storage is write-once until retention expires, so no one, including the platform's own administrators, can change or delete a record early. Security Team members administer the platform's content, while the Platform Team runs its infrastructure, and neither can do the other's job. A source that goes silent or an ingestion failure alerts the Security Team.

## External Dependencies
None outside the boundary.
