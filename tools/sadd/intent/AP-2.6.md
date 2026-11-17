## Design Intent
The package mirror scans every package and base image it fetches, and the pipeline scans every build artifact before release. Runners suppress package install scripts. Vendor software deliveries, such as the payload vendors' conversion software and COTS updates, are scanned at intake before anyone installs them. Fleet firmware intake follows Secure OT/Legacy Device Baselines (`DI-3.5`).

## External Dependencies
The payload vendors and COTS suppliers, whose deliveries are scanned at intake.
