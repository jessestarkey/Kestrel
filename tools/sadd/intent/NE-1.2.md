## Design Intent
Hardening baselines come from the DISA STIGs for every network device, namely the SDN switches and controller, every firewall, and the ground segment switches. Management interfaces sit only on an out-of-band network and accept only administrators coming through the privileged access platform. IPv6 is enabled where a service supports it, with every rule written for both address families. Elsewhere it is disabled and filtered, and the ground segment drops it at its conduit.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider hardens the network devices beneath the cloud hub and the managed load balancers in the DMZ.
