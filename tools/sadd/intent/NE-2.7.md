## Design Intent
Performers reach KESTREL only through the identity-aware access proxy for developer tools and the VDI brokers for desktops. Neither offers a network tunnel, so no laptop joins KESTREL's network and split tunneling cannot occur. The VDI desktops reach management ports only during an approved just-in-time window, or through the privileged access platform's session hosts. Sessions end after 15 idle minutes, and the Security Team can end any session at once. Recorded sessions and broker logs go to the security monitoring platform.

## External Dependencies
The performer, whose CMMC Level 2 laptops originate these sessions under the interconnection agreement.
