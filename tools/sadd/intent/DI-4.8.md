## Design Intent
The VPMP sets KESTREL's remediation deadlines, with priority raised for the DMZ, Tier 0, and the fleet. Patches move from dev to test to stage before production. Tier 0 and on-premises patches go to the alternate site's standby first. Container images are rebuilt rather than patched. Redundant pairs are patched one node at a time. HSM and datalink crypto module firmware moves only to FIPS 140-3 validated versions. Fleet patches must be validated by the manufacturer, tried on a spare, and loaded in a maintenance window. An asset that cannot be patched follows Unpatchable/Legacy Asset Compensating Controls (`DI-4.9`).

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider patches the cloud platform beneath KESTREL. IAVM directives arrive through the CSSP, and the aircraft and ground equipment manufacturers validate fleet patches.
