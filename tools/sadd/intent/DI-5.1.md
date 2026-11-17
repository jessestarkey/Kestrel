## Design Intent
Application allow-listing runs deny-by-default on the privileged access workstations, the VDI desktops, and every on-premises and cloud virtual machine, with attack surface reduction rules on Windows hosts. Across the IT estate, removable media is blocked except at the media intake station, which reads only encrypted government media. The ground segment's mission storage modules and key loaders follow Secure OT/Legacy Device Baselines (`DI-3.5`) instead. Cameras and microphones are disabled on the privileged access workstations and in the VDI image.

## External Dependencies
KESTREL's Microsoft 365 DoD tenant, which supplies the endpoint protection service under its IL5 authorization.
