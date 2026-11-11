## Design Intent
The service desk platform's configuration management database is KESTREL's one asset inventory. The cloud provider's resource inventory feeds it for every spoke, and agents and the SDN controller feed it for the data center, so nothing depends on manual entry. Every spoke is its own subscription under KESTREL's tenant, and a subscription created outside the landing zone raises an alert. License tracking covers the payload vendors' conversion software, the service desk platform, and the foundation model's terms of use.

## External Dependencies
The IL5 cloud provider's resource inventory and event interfaces.
