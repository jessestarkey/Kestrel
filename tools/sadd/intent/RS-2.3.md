## Design Intent
Evidence collection is automated for cloud resources and on-premises hosts, capturing disk snapshots, memory, and the related logs. Evidence goes to a dedicated retention-locked evidence store in the data center, readable only by the Security Team and excluded from backup replication. Captures from fleet equipment and key-handling hosts exclude key material, and datalink crypto modules and HSMs are never imaged, so no row 13 material reaches the store. Analysts examine copies offline on an isolated forensic workstation that cannot reach production. Fleet equipment is imaged only during a maintenance window or after the aircraft has landed. Chain of custody follows the DoD reporting chain's requirements.

## External Dependencies
None outside the boundary.
