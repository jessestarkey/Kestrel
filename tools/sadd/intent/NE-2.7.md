## Design Intent
Every remote population reaches KESTREL through a named path that offers no network tunnel. Performers use the identity-aware access proxy for developer tools and the VDI brokers for desktops. CSSP analysts use their own VDI host pool, and program office staff use the access proxy over F38 from the parent organization's managed devices. Vendors use the vendor host pool over F37. Penetration testers get time-bound accounts on the same paths. Management ports open only for a just-in-time window or to the privileged access platform's session hosts. Session keys and certificates are managed under the KMP. Sessions end after 15 idle minutes, and the Security Team can end any session at once.

## External Dependencies
The performer and the parent organization, whose devices originate these sessions under their interconnection agreements. The equipment and payload vendors, under their support agreements. The CSSP and the penetration testing provider, under their agreements.
