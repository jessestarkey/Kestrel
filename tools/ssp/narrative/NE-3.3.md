Infoblox NIOS appliances will resolve names for the data center and the alternate site, and NIOS virtual appliances in Platform Prod will resolve for the cloud. Hosts may use no other resolver, and the hubs block outbound DNS to anywhere else. Every resolver validates DNSSEC, and resolver traffic across the circuits stays inside their IPsec tunnels.

KESTREL's public names sit signed under the program's DoD parent zone and point only at the access point's published addresses, with DoD publishing their delegation records. Azure DNS holds only the private zones.
