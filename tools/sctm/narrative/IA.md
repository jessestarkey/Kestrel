# IA: Identification and Authentication

## IA-1

The program manager will issue the identification and authentication policy as part of KESTREL's system security policy. The Account Management Plan (AMP) will hold the procedures that carry it out, covering authenticators, assurance levels, and sessions. The Configuration Control Board will approve both, and each will be reviewed at least once a year.

## IA-2

Every person will be uniquely identified and authenticated before reaching anything in KESTREL. Active Directory in the mission data center will hold each user's account, and Entra ID will authenticate cloud sign-in against a synchronized copy of it. Group or shared accounts will not be used for everyday access.

## IA-2(1)

Privileged accounts will authenticate with a CAC, which combines the card with its PIN. Administrators will sign in with the card first, through Entra certificate-based authentication or Active Directory smart card logon, before CyberArk or Entra Privileged Identity Management grants any privileged role. The directory and station break-glass accounts are the one exception. They use console-only passwords under a compensating control, held by two custodians and changed after every use.

## IA-2(2)

Non-privileged accounts will authenticate with a smart card as well, in every location. DoD users and performers will use their CAC, vendors an ECA credential, and partners a certificate from their own nation's PKI.

## IA-2(5)

Built-in administrative accounts on appliances, hypervisors, and the HSMs will be reachable only through CyberArk. An administrator must first authenticate to CyberArk as an individual with a CAC. CyberArk then injects the shared credential into a recorded session, so the administrator never sees it and every use is tied to a person.

## IA-2(8)

Certificate-based authentication will be used for every network sign-in, and it resists replay because each logon proves possession of the card's private key against a fresh challenge. The break-glass passwords are the only authenticators that would not resist replay. They are limited to named local consoles and never cross a network.

## IA-2(12)

KESTREL will accept DoD CACs as PIV credentials. Entra certificate-based authentication will accept them in the cloud, and Active Directory smart card logon on premises. Each card's certificate is validated against DoD PKI and checked for revocation.

## IA-3

Devices will be authenticated before they connect. In the data center and at the alternate site, Cisco ISE will require 802.1X with EAP-TLS on every wired port, using device certificates from the program PKI, and the operating sites will follow in Phase 3. Each aircraft and ground control station will authenticate on the datalinks with its own program PKI device identity. Equipment that cannot hold a certificate will be admitted by its registered hardware address, and only to its own zone.

## IA-4

Each person's identifier will be assigned at enrollment and bound to their CAC record, or to their sponsor's record for partners and vendors. IT Operations will assign identifiers through Jira Service Management and Entra ID Governance. Each new account will be checked against existing ones, so no person holds two identities and no identifier is assigned to a second person.

## IA-4(4)

Each identifier will show the user's status. CAC affiliation will mark contractors, and a nationality attribute will mark partners and other foreign nationals. Roles and access policies can then tell these populations apart.

## IA-5

KESTREL will manage every authenticator it uses through a defined lifecycle. DoD issues and revokes the CACs, while the program PKI will issue, renew, and revoke device and workload certificates, with its keys in the nShield HSMs and its certificates tracked in Keyfactor Command. Windows LAPS and group Managed Service Accounts will rotate local administrator and service passwords. Vendor-default credentials will be replaced before any server controller or fleet device is fielded. After a confirmed compromise, every affected authenticator will be reset.

## IA-5(1)

Passwords will remain only on the break-glass accounts. Each password will be split between two custodians, sealed, and changed after every use. The AMP will set its length and composition.

## IA-5(2)

Certificate validation will build a path to an approved trust anchor and check revocation at each session. DoD PKI, the External Certificate Authorities, and approved partner PKIs supply the anchors. Services will accept a cached revocation response for up to 24 hours, and the ground control stations will check a local list refreshed daily and before each flight. Private keys stay on the CAC or in the HSMs, and service accounts will authenticate with certificates wherever they can.

## IA-5(6)

Authenticators will be kept out of code, images, and settings. Each cloud spoke's Key Vault will hold that spoke's secrets, and CyberArk will vault administrative credentials and inject them only into recorded sessions. Pipeline and training jobs will receive short-lived tokens through workload identity rather than stored credentials. The foundation model is reached by workload identity with key-based access disabled, so no API key exists to protect.

## IA-6

Sign-in pages and consoles will hide what a user types and will not say which part of a failed logon was wrong. Failed attempts will be limited as the AMP sets. A ground control station whose aircraft is airborne will delay the next prompt and alert instead of locking the account.

## IA-7

Operators of the nShield HSMs will authenticate with smart cards from the HSMs' own card sets, and sensitive key operations will need a quorum of those cards. Software cryptographic modules will authenticate their callers through the identity platform.

## IA-8

People outside the organization will be identified and authenticated before reaching their part of KESTREL. Vendor support engineers will sign in with ECA Medium Hardware credentials through Entra certificate-based authentication. Partner systems will authenticate to the partner API with mutual TLS, using certificates from their own nation's PKI or an ECA.

## IA-8(1)

PIV credentials issued by other federal agencies will be accepted through the same certificate-based authentication, provided their issuers are on KESTREL's trust list.

## IA-8(2)

Only external authenticators from issuers on KESTREL's trust list will be accepted. The list names the External Certificate Authorities and each partner nation's issuing authorities, and adding a partner nation requires a CCSD revision.

## IA-8(4)

Partner connections will follow defined profiles. Partner systems will use X.509 certificates over mutual TLS. Partner identity providers, when they join in Phase 3, will federate using SAML or OIDC profiles agreed with each partner.

## IA-11

Users will be asked to authenticate again when risk or context changes. Administrative consoles will always require fresh authentication, and activating a privileged role will too. Cloud and VDI sessions will end and require sign-in again when the AMP's session limits are reached, or sooner if continuous access evaluation finds the risk severe.

## IA-12

Every person will be proofed before KESTREL issues an account, at the assurance level the AMP sets for their population. DoD users and performers are proofed through their CAC issuance, and KESTREL binds each account to that record. Partners and vendors will be proofed through a KESTREL sponsor's attestation.

## IA-12(2)

The evidence behind each enrollment will be recorded in Jira Service Management. For DoD users and performers, that is the CAC record. For partners and vendors, it is the sponsor's attestation and the documents it relies on.

## IA-12(3)

IT Operations will validate the evidence at enrollment. Each CAC will be checked against DoD PKI, and each sponsor's attestation against that sponsor's agreement with KESTREL.

## IA-12(4)

DoD validates each person's identity evidence in person when it issues their CAC. KESTREL relies on that step and does not repeat it.

## IA-12(5)

For DoD users and performers, CAC issuance confirms the address of record. For partners and vendors, a registration code or notice of proofing will be sent out of band to the address their sponsor records.
