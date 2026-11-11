## Design Intent
Files move only over HTTPS or SFTP, including recordings crossing the ground segment conduit. Administrative SSH and RDP run only through the privileged access platform or a VDI session, never directly. Every transfer is logged to the security monitoring platform. The payload processing workstation's transfer is the one exception, under CCSD tailoring action 3.

## External Dependencies
None outside the boundary.
