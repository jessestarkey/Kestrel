## Design Intent
The cloud hub's next-generation firewall sits at the center of the ten spokes, each peered only to the hub. Custom routes send every spoke's traffic, east-west and outbound, through it. The data center hub is a redundant appliance pair in front of the SDN fabric. Outbound web traffic is limited to an allow-list of update and package sources, all reached through the package mirror. Both hubs inspect outbound TLS. East-west flows already protected by mutual TLS between workload identities are exempt from decryption.

## External Dependencies
The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider supplies the cloud-native firewall service the cloud hub runs on.
