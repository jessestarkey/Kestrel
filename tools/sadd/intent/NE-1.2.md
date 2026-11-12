## Design Intent
Hardening baselines come from the DISA STIGs for the SDN switches and controller, both hubs' firewalls, the alternate site firewall, and the ground segment network's switches. Management interfaces sit only on the out-of-band network and accept only administrators coming through the privileged access platform. The cloud and data center run dual-stack, with every hub rule written for both address families. The ground segment stays IPv4 only and drops IPv6 at its conduit.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider hardens the network devices beneath the cloud hub and the managed load balancers in the DMZ.
