## Design Intent
Behavioral anti-malware runs on every privileged access workstation, VDI desktop, and virtual machine. Runtime protection sensors run on every Kubernetes cluster, including the notebook and serving node pools. Managed training compute runs only scanned images. Web and network protection on the VDI desktops allow only the management endpoints those desktops need. Malicious-domain filtering already happens at both sides' DNS resolvers.

## External Dependencies
KESTREL's Microsoft 365 DoD tenant, which supplies the endpoint protection service under its IL5 authorization.
