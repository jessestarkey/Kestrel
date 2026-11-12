## Design Intent
The service desk platform's configuration management database is KESTREL's one asset inventory. The cloud provider's resource inventory feeds it for every spoke. Agents feed it for the data center and the alternate site, with the SDN controller adding the data center's network devices, so nothing depends on manual entry. Every spoke is its own subscription under KESTREL's tenant, and a subscription created outside the landing zone raises an alert. License tracking covers every licensed product and model, such as each payload vendor's conversion software, the service desk platform, and each foundation model's terms of use.

## External Dependencies
The IL5 cloud provider's resource inventory and event interfaces.
