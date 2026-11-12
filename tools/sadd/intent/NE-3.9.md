## Design Intent
Each aircraft's GNSS receiver reports signal and solution quality, which is profiled per aircraft and compared with its inertial navigation. Each station compares its GNSS timing with a local holdover reference. It also checks against the data center's time source whenever the conduit is up. Indicators of spoofing or jamming alert the operator at the station during flight and reach the Security Team through the security monitoring platform.

## External Dependencies
The aircraft manufacturer, whose receivers report the signal quality data this profiling uses.
