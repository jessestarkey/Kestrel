## Design Intent
The VPMP sets KESTREL's remediation deadlines, with priority raised for assets in the DMZ, Tier 0, and the fleet. Patches move from dev to test to stage before production. Container images are rebuilt and redeployed rather than patched in place. Data center servers are patched one node of each redundant pair at a time. Fleet patches must be validated by the manufacturer, tried on a spare, and loaded in a maintenance window. The payload processing workstation's flaws run under CCSD tailoring action 3 until 2027-09-30.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider patches the cloud platform beneath KESTREL. IAVM directives arrive through the CSSP, and the aircraft and ground equipment manufacturers validate fleet patches.
