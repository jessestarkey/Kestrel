## Design Intent
The on-premises directory in the mission data center is KESTREL's identity system of record, and its cloud copy is the federation and access policy service for cloud sign-in. If the cloud is unreachable, directory logon, the stations' local CAC checks, and the break-glass accounts keep working. Cloud-federated sign-in waits for the circuit. Separate organizational units in the directory, mirrored as administrative units in the cloud copy, keep each team's identities apart.

## External Dependencies
The IL5 cloud provider's identity service, inherited under its provisional authorization.
