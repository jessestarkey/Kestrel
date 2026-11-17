## Design Intent
Each operating site's ground segment firewall parses the command and control protocol the stations use with the launch and recovery equipment. It allows only the commands each station is approved to send. A DPI fault on that path falls back to a fixed allow-list rather than blocking, so launch and recovery are never cut off, and the fault alerts. Command and control protocol traffic never crosses the conduit to the data center, so any seen there is blocked and alerted. The signed flight plan files F34 delivers are files, not command traffic. Fleet Operations and the Security Team tune the rules after each maintenance window.

## External Dependencies
The ground equipment manufacturers, who document the command sets their equipment accepts.
