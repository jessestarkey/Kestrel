## Design Intent
The service desk platform's configuration management database is KESTREL's one asset inventory. The cloud provider's resource inventory feeds it for every spoke. Agents feed it for every on-premises host, and the SDN controller adds the data center's network devices. Every spoke is its own subscription under KESTREL's tenant, and a subscription created outside the landing zone alerts. License tracking covers every licensed product and model, and peer-to-peer file sharing software is prohibited. An inventory dashboard shows coverage and unmanaged assets.

## External Dependencies
The IL5 cloud provider's resource inventory and event interfaces.
