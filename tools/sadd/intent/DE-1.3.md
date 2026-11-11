## Design Intent
The security monitoring platform is the one place every telemetry source lands, and it correlates endpoint, identity, network, cloud, application, and ground segment events with each other. Threat intelligence and indicator feeds from the CSSP enrich every alert. Detection rules are written as code in the Security Team's repository and deployed through the pipeline after review.

## External Dependencies
The CSSP, which receives forwarded telemetry and adds its own detection under its service agreement. It also supplies threat intelligence and indicator feeds.
