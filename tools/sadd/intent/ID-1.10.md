## Design Intent
Correlate badge events at the mission data center and the ground control station sites with logical sign-ins, so an operator signed in at a station but not badged into that site raises an alert. The physical access control systems belong to the PSO, and at the alternate site to the parent organization's facility, so KESTREL consumes their events and drives badge provisioning from its account lifecycle rather than running them.

## External Dependencies
The PSO's physical access control systems at the data center and each operating site, and the parent organization's facility access control system at the alternate site, under the facility agreement.
