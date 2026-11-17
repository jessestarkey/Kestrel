## Design Intent
The security monitoring platform is the one place every telemetry source lands, and it correlates endpoint, identity, network, cloud, application, and ground segment events. Indicators from the CSSP arrive over F31, carry a confidence tier and an expiry, and age out unless renewed. Vetted indicators are pushed to the firewalls, the DNS filters, and EDR. Detection rules are written as code in the Security Team's repository and deployed through the pipeline over F35 after review.

## External Dependencies
The CSSP, which receives forwarded telemetry and adds its own detection under its service agreement. It also supplies threat intelligence and indicator feeds.
