## Design Intent
Administer Tier 0 and the cloud tenant-owner roles only from the physical privileged access workstations in the data center and at the alternate site. Other Tier 1 work runs from the Platform Team's VDI host pool, reached from performer laptops KESTREL does not own. That departure is compensated by CAC and posture checks at the broker, elevation only inside the session, recording, and live termination. Smart card redirection is allowed while clipboard, drive, and USB redirection are blocked. Administrators who work across tiers hold a separate account per tier. Ground segment administration comes only from the stations' maintenance consoles in a window.

## External Dependencies
The performer, whose CMMC Level 2 laptops are the origin for Tier 1 sessions. The CSSP, whose analysts use their own host pool under its service agreement.
