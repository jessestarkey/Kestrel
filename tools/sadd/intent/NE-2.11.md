## Design Intent
The ground segment firewall parses the command and control protocol the ground control stations use with the launch and recovery equipment. It allows only the commands each station is approved to send. Command and control traffic never crosses the conduit to the data center, so any seen there is blocked and alerted. Fleet Operations and the Security Team tune the rules after each maintenance window.

## External Dependencies
The ground equipment manufacturers, who document the command sets their equipment accepts.
