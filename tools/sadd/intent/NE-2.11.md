## Design Intent
The ground segment firewall parses the command and control protocol the ground control stations use with the launch and recovery equipment. It allows only the commands each station is approved to send. The conduit to the data center carries file transfer for recordings and model packages and nothing else, so any control protocol traffic there is blocked and alerted. Fleet Operations and the Security Team tune the rules after each maintenance window.

## External Dependencies
The ground equipment manufacturers, who document the command sets their equipment accepts.
