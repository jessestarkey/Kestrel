# AC: Access Control

## AC-1

The program manager will issue the access control policy as part of KESTREL's system security policy. The Account Management Plan (AMP) will hold the procedures. The Configuration Control Board will approve both, and each will be reviewed at least once a year.

## AC-2

Accounts will be managed through one lifecycle. Active Directory in the mission data center holds every account, with Entra ID as its cloud copy. Access is granted in role bundles scoped by team. IT Operations changes group membership only through a recorded Jira Service Management request, which the requester's team lead approves. Partner and vendor accounts are tied to a sponsor and to their support cases or partner API roles. Access is recertified on the AMP's cadence.

## AC-2(1)

Account management will be automated. Entra ID Governance creates the baseline account when enrollment completes, and accounts are synchronized continuously against the authoritative source. Splunk computes dormancy each day, and Ansible disables any account dormant past the AMP's threshold.

## AC-2(2)

Temporary and emergency accounts will be controlled automatically. Maintenance access to the fleet opens only for a scheduled window. Vendor sessions end when their case closes, after eight hours at most. Break-glass sessions end after four hours, or once no aircraft under a station is airborne.

## AC-2(3)

Accounts will be disabled when they are no longer needed. A departure disables the person's Active Directory account and revokes their CAC binding, and accounts dormant past the AMP's threshold are disabled automatically. Each service account has a named owner and is removed when its service is. During an incident, a compromised account can be disabled at once.

## AC-2(4)

Every account creation, change, disable, and removal will be logged to Splunk from the directory and from Entra ID.

## AC-2(5)

Cloud and VDI sessions will end after the AMP's inactivity limit. Ground control stations are the exception while their aircraft is airborne, since a logged-out operator could endanger the flight.

## AC-2(11)

Conditional Access will set the conditions on each account's use, such as device compliance and network origin.

## AC-2(12)

Accounts will be monitored for atypical use. Splunk Enterprise Security baselines each role's behavior and flags deviations, such as bulk reads across data lake zones. Any use of a break-glass account alerts the Security Team and the CSSP.

## AC-2(13)

The account of anyone posing a significant risk will be disabled at once through Entra ID and Defender XDR, revoking their sessions, under the IRP.

## AC-3

Access will be enforced by the identity provider and by an attribute-based policy. Roles are Active Directory groups scoped by team, so an analyst cannot reach another team's payload vendor data. An OPA policy decision service decides data access from the user's attributes and each record's labels. Retrieval for the LLM analyst assistant enforces the requesting user's entitlements, and each agent's memory is scoped per repository or per user.

## AC-3(14)

Individuals will be able to request access to the personal information KESTREL holds about them, through the privacy officer.

## AC-4

Information flows will be enforced at every boundary. Workload security groups, ACI contracts, and Cilium network policies allow only each team's mapped flows, and the ground segment's conduits allow only approved traffic. Data loss prevention sits on every outbound path, and the partner API and the cross domain gateway check every release against its markings. Each agent tool call is checked against what its task authorized.

## AC-4(4)

Both hubs will decrypt outbound TLS so its content can be inspected. Mutual TLS between workload identities is exempt.

## AC-5

Duties will be separated where combining them would let one person cause harm alone. No merge is approved by its own author. Key administration, key use, and key auditing are held by different roles. IT Operations provisions access, but the requester's team lead approves it.

## AC-6

Every identity will have only the access its role needs. Role bundles are scoped by team, workload identities by spoke, and pipeline identities by team and environment. Each AI agent reaches only the tools its use case approves, and each training run reads only the snapshots it declares.

## AC-6(1)

Access to security functions will be limited to the roles that need it. The Security Team reads the asset inventory without the right to change it. Vault access is activated just in time, inside an administrative session. Deleting backups or shortening their retention needs a second approver.

## AC-6(2)

Administrators who work across tiers will hold a separate account for each tier, and they use a non-privileged account for everything else.

## AC-6(3)

Privileged commands will be reachable over the network only from two places. Tier 0 is reached from the privileged access workstations, and Tier 1 from the Platform Team's administrative VDI host pool.

## AC-6(5)

Privileged roles will be defined per administrative surface and held in Entra Privileged Identity Management for the cloud and in CyberArk for everything else. Tier 0 roles go only to the named Tier 0 administrators, and no role spans both the HSMs and the cloud tenants.

## AC-6(7)

Privileges will be reviewed on the AMP's cadence, with operator, platform administrator, and partner access reviewed more often than analyst access.

## AC-6(9)

Every use of a privileged function will be logged, including every key operation, and CyberArk records every privileged session.

## AC-6(10)

Non-privileged users will not be able to run privileged functions. Every privilege is eligible rather than standing, and it can be activated only through Entra Privileged Identity Management or CyberArk, for a bounded window.

## AC-7

Failed logon attempts will be limited as the AMP sets, and an account locks after too many. A ground control station whose aircraft is airborne delays the next prompt and alerts instead of locking.

## AC-8

Every sign-in page and console will display the DoD system use notification banner before access is granted.

## AC-10

Each account type will have a limit on concurrent sessions, tighter for privileged accounts, and going over it raises an alert.

## AC-11

Sessions will lock after 15 minutes of inactivity and stay locked until the user authenticates again. Ground control stations do not lock while their aircraft is airborne, under CCSD tailoring action 2.

## AC-11(1)

A locked screen will hide what was displayed on it.

## AC-12

Sessions will end automatically when the AMP's session limit is reached, or sooner when continuous access evaluation finds the risk severe. AI agent sessions end at a fixed limit.

## AC-14

Without signing in, a user can see only the system use banner and the sign-in pages. No other action is permitted.

## AC-17

Every remote population will reach KESTREL through a named path that offers no network tunnel. Developers and program office staff use Pomerium, the identity-aware proxy. Operators, data scientists, vendors, and CSSP analysts use their own host pools in Azure Virtual Desktop.

## AC-17(1)

Remote sessions will be monitored and controlled. Vendor and privileged sessions are brokered and recorded by CyberArk, and the Security Team can end any session at once.

## AC-17(2)

Remote sessions will be protected by TLS 1.2 or later, and administrative SSH and RDP run only through CyberArk or a VDI session.

## AC-17(3)

Remote access will arrive only through the Boundary Cloud Access Point and the cloud hub, and then through Pomerium or the VDI brokers.

## AC-17(4)

Privileged commands will be run remotely only through CyberArk-brokered sessions, which record every action.

## AC-18

The aircraft's command and payload datalinks will be KESTREL's only authorized wireless, and no wireless LAN exists. Rogue access points and unauthorized radios are detected at every site.

## AC-18(1)

The datalinks will use authenticated encryption on FIPS 140-3 validated crypto modules, with CNSA algorithms. Any future wireless LAN would have to use WPA3-Enterprise with EAP-TLS.

## AC-18(3)

Embedded wireless radios will be disabled on every server, workstation, and station, apart from the station datalink radios.

## AC-20

Devices KESTREL does not own will never join its network. Performer laptops reach it only through Pomerium and Azure Virtual Desktop after a posture check, under the interconnection agreement and the performer's CMMC Level 2 attestation. Parent organization devices use Pomerium alone, and vendor devices only the vendor host pool.

## AC-20(1)

External systems will be allowed only under terms that verify their controls. The performer's laptops must meet the posture check at each connection, and the interconnection agreements record the terms for each organization.

## AC-20(2)

Portable storage will not be usable with external systems to move KESTREL information. VDI desktops block downloads and drive redirection.

## AC-21

Information sharing will be decided by policy. The attribute-based policy decides each user's access from their partner nation and each record's releasability, and the foreign disclosure officer approves each release to a partner.

## AC-22

The PMO ISSE will be the only person who may post public content, which is limited to the vulnerability disclosure listing. Anything posted passes OPSEC and foreign disclosure review first, and is rechecked each year.
