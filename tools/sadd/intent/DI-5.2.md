## Design Intent
Behavioral anti-malware runs on every privileged access workstation, VDI desktop, and virtual machine. Runtime protection sensors run on every Kubernetes cluster, including the training cluster's GPU nodes. Web and network protection on the VDI desktops allow only the management endpoints those desktops need. Malicious-domain filtering already happens at both sides' DNS resolvers.

## External Dependencies
None outside the boundary.
