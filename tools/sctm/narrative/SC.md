# SC: System and Communications Protection

## SC-1

The program manager will issue the system and communications protection policy as part of KESTREL's system security policy. The Key Management Plan will hold the cryptographic procedures, and the CMP the network and boundary procedures. The Configuration Control Board will approve them, and each will be reviewed at least once a year.

## SC-2

Administration will be kept apart from user functions. Tier 0 is administered only from physical privileged access workstations, and Tier 1 from the Platform Team's own Azure Virtual Desktop host pool, never from a user desktop. Administrators hold separate accounts for administrative work. The VDI brokers have their own listener and subnet, apart from user-facing applications.

## SC-3

Virtualization-based security will isolate the EDR agent and the credential stores on every workstation, desktop, and Windows server. Tamper protection, owned by the Tier 0 administrators and changed only with the Security Team's approval, keeps the EDR agent itself from being switched off.

## SC-4

Information will not carry over between users of shared resources. Each training run gets its own containers, and its scratch storage is destroyed when it ends, so cached data and tensors cannot reach the next job. Pipeline jobs run on fresh runner pods that are destroyed afterward.

## SC-5

Network-layer floods will be absorbed upstream by DISA's internet access points and the Boundary Cloud Access Point, since the DMZ holds no cloud public addresses. Application Gateway limits the request rate to each user-facing application, and API Management limits each partner and each caller of the model endpoints. DoS protection policies on the cloud hub limit what any one spoke can send. Flood alerts go to Splunk.

## SC-7

KESTREL's external boundary will be the Boundary Cloud Access Point and the cloud hub, with the data center hub as the managed interface for its own external links. Internal boundaries divide the cloud's ten spokes, the data center's SDN segments, and the ground segment's IEC 62443 zones, each joined to the IT network only through its conduit. Platform services add their own resource firewalls, admitting only their spoke's private endpoint.

## SC-7(3)

External connections will be limited to a small set of managed access points. All user traffic arrives through the Boundary Cloud Access Point and the cloud hub. Outbound traffic leaves only through the hubs, and only for an allow-list of named classes: package sources, PKI revocation, the time reference, the threat feed, the Microsoft 365 DoD tenant, and the paging service.

## SC-7(4)

Each external telecommunications service will have a managed interface. The three dedicated circuits ride DISN through the Boundary Cloud Access Point and terminate on the cloud hub and each site's firewall. Their traffic runs inside IPsec tunnels between the firewalls. BGP sessions are authenticated, and prefix filters accept only KESTREL's address ranges. Every port, protocol, and service crossing them is registered in the DoD PPSM registry with its justification.

## SC-7(5)

Every boundary will deny traffic by default and allow it by exception. Workload security groups, ACI contracts, Cilium network policies, and the ground segment conduits each allow only mapped flows. Training compute reaches only the model registry, the package mirror, and the training data zone.

## SC-7(7)

KESTREL offers no network tunnel to any remote user. Remote access runs through Pomerium or Azure Virtual Desktop, and neither routes the user's device onto KESTREL's network, so split tunneling cannot occur.

## SC-7(8)

Outbound traffic will pass through the hubs' firewalls, which decrypt and inspect TLS and apply URL filtering. Remote users reach applications only through Pomerium, the identity-aware proxy, or the VDI brokers, both of which authenticate the user first.

## SC-7(18)

Boundary devices will fail to a safe state. The firewalls, the access proxy, the VDI brokers, and the cross domain transfer gateway fail closed. On the ground segment, a deep packet inspection fault falls back to a fixed allow-list of each station's approved commands, so launch and recovery keep working while nothing new is allowed.

## SC-7(21)

The components with the most risk will each sit in their own segment. The DMZ, the VDI spoke, and Tier 0 are isolated, and so is each ground segment zone. Each Key Vault is reachable only through its own spoke's private endpoint.

## SC-7(24)

Data loss prevention will watch personal information at the boundary. The partner API and the cross domain transfer gateway check every release against its markings, and the DMP's rules block personal information on each named outbound path.

## SC-8

Data in transit will be protected for confidentiality and integrity. Every connection uses TLS 1.2 or later, and services authenticate each other with mutual TLS using program PKI certificates. Traffic across the dedicated circuits runs inside IPsec tunnels. The aircraft datalinks use authenticated encryption on FIPS 140-3 validated crypto modules.

## SC-8(1)

The protection in transit will be cryptographic, using FIPS 140-3 validated modules and CNSA algorithms. The IPsec tunnels run in FIPS-CC mode, and the datalinks use CNSA algorithms under CNSSP 15.

## SC-10

Remote sessions will end after 15 idle minutes, and the Security Team can end any session at once. Cloud and VDI sessions also follow the AMP's limits under continuous access evaluation.

## SC-12

Keys will be generated, stored, and managed under the Key Management Plan. The root keys sit in the nShield HSMs in the data center, under KESTREL's own security world. Each spoke's customer-managed keys are generated in the HSMs and imported into Azure Key Vault Premium, which holds them at FIPS 140-3 Level 3. Key Vault rotates its keys on the KMP's schedule, and imported keys are replaced by an HSM job before they expire. Key administration is separated from key use.

## SC-12(1)

Keys whose loss would destroy data will stay available. Backup set keys and other such keys are escrowed in the alternate site's HSM under split knowledge. Recovering one needs two of the four administrator cards.

## SC-13

KESTREL will use only FIPS 140-3 validated cryptographic modules and CNSA algorithms. AES-256 protects data at rest. The datalink crypto modules and the HSMs are validated, and so is the cloud's Key Vault Premium.

## SC-15

Cameras and microphones will be disabled on the privileged access workstations and in the VDI image, so no collaborative device can be switched on remotely.

## SC-17

Certificates will come from approved authorities. The program PKI issues device, workload, and service certificates from issuing authorities under an offline root whose key is held in the HSMs. Keyfactor Command tracks every certificate. User-facing edge services present DoD PKI server certificates that browsers and partner systems already trust.

## SC-18

Allow-listing will block unapproved code, including scripts, on every workstation, desktop, and server. Attack surface reduction rules on Windows hosts block scripts and macros from untrusted sources.

## SC-20

KESTREL's public names will sit under the program's DoD parent zone, signed with DNSSEC. DoD publishes their delegation records, and the names point only at the access point's published addresses.

## SC-21

Every KESTREL resolver will validate DNSSEC on the answers it returns. Hosts may use no other resolver, and the hubs block outbound DNS to anywhere else.

## SC-22

Name resolution will be redundant and split by role. Infoblox appliances serve the data center and the alternate site, and virtual appliances serve the cloud from Platform Prod. Each operating site has its own resolver pair. No KESTREL resolver answers for the public names, so the authoritative and recursive roles stay separate.

## SC-23

Session authenticity will be protected by TLS on every session and by short-lived, signed tokens. Continuous access evaluation revokes a session's tokens when the account is disabled or its risk becomes severe.

## SC-24

The firewalls, the access proxy, the VDI brokers, and the cross domain transfer gateway will fail closed. Each preserves its state so it can recover to a known configuration.

## SC-28

Information at rest will be protected in every store. Each data lake zone, database, and storage service is encrypted, and backups and audit logs sit in immutable storage that no account can alter before its retention ends.

## SC-28(1)

Every store will be encrypted with AES-256 under keys KESTREL controls, as the DMP sets for each label. Each data lake zone uses its own key, personal fields use column encryption, and model artifacts are encrypted in the registry and on serving nodes. Edge models are encrypted under a key rooted in the HSMs. Reports released to partners are wrapped with Purview Information Protection.

## SC-39

Each process that handles untrusted or sensitive work will run in its own isolated environment. Every pipeline job runs on a fresh runner pod, every training run in its own containers, and every model evaluation in a disposable environment. Each AI agent tool runs in its own Container Instances group with hypervisor isolation.
