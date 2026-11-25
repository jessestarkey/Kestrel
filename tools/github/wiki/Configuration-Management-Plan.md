> **Notional system.** KESTREL is fictional. This page stands in for a governing plan in KESTREL's self-hosted Confluence. Its names, thresholds, and decisions are invented to show a completed Configuration Management Plan.

# KESTREL Configuration Management Plan (CMP)

This plan sets how KESTREL's components are built, changed, hardened, protected, and retired, and how long its detection records are kept. It is the procedures half of the configuration management policy pairing. The policy half is the system security policy the program manager issues under Security Policy Framework (`GV-1.1`). It carries out the design decisions in the [Device and Infrastructure](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/03-device-and-infrastructure.md), [Network and Environment](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/04-network-and-environment.md), and [Detection](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/08-detection.md) sections of the SADD. It names the products that enforce them. The [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/03-device-and-infrastructure.md) is the record of each product selection, and a substitution there revises this plan.

**NIST Control Mapping:** CM-1 (partial) and CM-9 (full), held through DI-6.1.

> **Phasing.** This plan is approved in Phase 1 and governs every component from the day it is built. Some components arrive later. The data center's network sensors and the IT/OT DMZ arrive in Phase 2, and the fleet integrates in Phase 3. A rule marked "from Phase 2" or "from Phase 3" takes effect when its component arrives.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| CMP Version | 0.1 |
| Date | 2026-11-25 |
| Prepared By | Platform Team lead, with Fleet Operations for the OT and legacy sections and IT Operations for maintenance, reviewed by the Security Team |
| Approved By | Configuration Control Board, chaired by the chief engineer |
| Source SADD Version | 0.5 |
| Source SIP Version | 0.3 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-25 | Platform Team lead | Initial draft for Configuration Control Board review |

---

## Purpose and Scope

This CMP covers every component inside KESTREL's authorization boundary. That includes the IL5 cloud's hub and spokes, the data center, the alternate site, the IT/OT DMZ, and the fleet. It also covers the retention of KESTREL's detection records. It does not cover the performer's laptops or the parent organization's devices, though it sets the conditions they must meet to connect. Remediation deadlines for flaws belong to the Vulnerability and Patch Management Plan (VPMP).

Configuration Monitoring (DI-4.4 to DI-4.7) and Device Compliance (DI-4.1) check the running configuration against this plan. Their findings feed the compute, storage, and platform compliance dashboards in Splunk.

---

## 1. Provisioning and Secure Defaults

*Traces to DI-2.1.1 and DI-2.1.2.*

**Cloud.** Every cloud resource is created by OpenTofu through GitLab, from the Platform Team's landing zone modules. The modules apply secure settings at creation. Azure Policy and the pipeline's Conftest checks block any resource that departs from them or lacks its required tags. Azure Policy denies creation in the portal outside break-glass.

**On premises.** Every on-premises server is built from the same STIG-hardened Packer images and Ansible Automation Platform playbooks. That includes the alternate site and the IT/OT DMZ. Nobody builds a server by hand.

**Fleet.** Fleet Operations builds each station and launch system to its manufacturer's baseline under Section 4, from Phase 3.

**Approval.** Every provisioning change is a GitLab merge request. A second reviewer from the owning team approves it, checking it against the module's secure defaults and the required tags. The merged request is the provisioning record. Policy checks must pass before the merge button is available.

---

## 2. Change Management

*Traces to DI-2.2.1, DI-2.2.2, DI-2.2.5, and NE-1.1.3.*

**Standard changes.** A merged GitLab merge request is the change record for anything defined as code. Jira Service Management holds the record for everything else, including fleet changes. Each change records the components it touches, its security impact note, and its test result.

**Testing.** Cloud changes are tested in the owning team's stage cluster first. Tier 0 and data center changes go first to the alternate site's standby or a lab. A change with neither records an exception and gets extra verification after it lands. A post-change compliance scan closes the record.

**Impact analysis.** The security impact note answers four questions:

- Which components does the change touch, and what is their criticality?
- Does it change a boundary, a trust relationship, or an identity's access?
- Which controls does it affect, and does it weaken any of them?
- Could it reach an aircraft, a station, or a datalink?

The reviewer approves on that assessed risk, not on the change alone. Every change enters Security Impact Analysis (`GV-5.11`) through its note. A change the analysis finds significant goes to the SCA and the AO before it is built. Each analysis is recorded on its own SIA record, not in this plan.

**Configuration Control Board.** The chief engineer chairs the board, which meets weekly. Its members are the PMO ISSE, the ISSM, the Platform Team lead, and Fleet Operations' operations lead. The lead of any team with a change on the agenda joins them. These changes go to it:

- Any change to the shared rule base on the hubs, the alternate site firewall, and the SDN controller
- Any change to the identity provider
- A new or changed interconnection
- A change to a system prompt's roles or limits
- A change to any governing plan the AO does not approve
- A change a reviewer contests, or one the impact note rates High

**Network changes.** Every firewall, SDN, or DNS rule change is a merge request with a second reviewer. The shared rule base goes to the board. Each ground segment firewall's rule set sits in Fleet Operations' repository, reviewed the same way and loaded in a maintenance window.

**Emergency changes.** An emergency change is one that cannot wait for the weekly board without leaving an incident uncontained or a mission service down. The incident lead or the Platform Team lead declares it. It runs through CyberArk, with the justification recorded on the change record when it is made. The board reviews it within two business days and confirms it, adjusts it, or reverses it.

---

## 3. Decommissioning and End-of-Life

*Traces to DI-2.3.1, DI-2.3.2, and DI-2.3.3.*

**Retiring a resource.** The owning team opens a decommissioning record in Jira Service Management. What happens next depends on the component.

| Component | How it is retired |
|---|---|
| Cloud resource | Destroyed by the OpenTofu that created it, which revokes its workload identities and deletes its vault secrets and keys |
| Data center or alternate site server | Drives wiped on site with Blancco before the server leaves, and its certificates revoked |
| HSM | Zeroized on site |
| Aircraft or station, from Phase 3 | Keys zeroized, storage wiped, and device certificates revoked |

The Platform Team confirms the asset is gone from Assets, DNS, and the rule base before the record closes.

**Orphaned resources.** A resource is orphaned when its owning team or tag no longer resolves, or when it has been idle for 60 days. Idle means no sign-ins, no traffic, and no deployments. The Platform Team finds orphans each week from Azure Resource Graph and Assets. The owning team then has 14 days to claim the resource. An unclaimed one is decommissioned.

**End of support.** Refresh planning forecasts each asset's end of support at least 12 months ahead. An asset kept past end of support needs an exception under the exception process (`GV-2.2`). The exception states the reason, the compensating controls, and a replacement date. The PMO ISSE may approve Very Low exceptions, and Low ones outside CCSD rows 6, 8, 10, and 13. The AO approves the rest. The payload processing workstation is the known case, replaced by 2027-09-30. It connects only if the AO re-dates CCSD tailoring action 3.

---

## 4. Hardening Baselines and Frameworks

*Traces to DI-3.1.2, DI-3.5.1, DI-3.5.2, NE-1.2.1, and NE-1.2.3.*

**Frameworks.** DISA STIGs and SRGs are KESTREL's hardening basis, with the Cloud Computing SRG's IL5 requirements in the cloud. Azure Policy initiatives carry them in the cloud, and Ansible roles carry them on premises. Each deviation from a STIG is recorded with its reason in the baseline's repository and approved through Section 2.

**Fleet, from Phase 3.** Each manufacturer's hardening guide is the baseline for its ground control stations, launch and recovery equipment, aircraft, and operating site services. Windows-based stations also take the DISA STIG unless the manufacturer documents a conflict. Fleet Operations proves each baseline on the spare stations and the simulator in Phase 2.

**Assets that cannot be hardened.** An asset that cannot reach a current baseline gets a compensating control baseline. It sits in its own segment, behind virtual patching at its only path, with tighter monitoring. The payload processing workstation would be the one case, if its replacement slips. It would then run in its own OT zone under application allow-listing.

**Network devices.** DISA STIGs harden the cloud hub's VM-Series firewalls, the data center hub's PA-Series pair, and the alternate site firewall. They also harden the ACI switches and APIC, checked with the SCAP Compliance Checker. Ground segment switches are hardened on the spares in Phase 2 and at each operating site from Phase 3. Management interfaces sit only on the out-of-band network and accept only CyberArk-brokered sessions.

**IPv6.** The cloud and the data center run dual-stack, and every rule is written for both address families. Filtering, logging, and first-hop protections cover IPv6 the same as IPv4. The alternate site follows the data center. The ground segment disables IPv6 and drops it at each site's conduit.

---

## 5. Device Compliance

*Traces to DI-4.1.1, DI-4.1.3, and DI-4.1.5.*

**Devices KESTREL does not own.** No device KESTREL does not own joins its network, and no AO exception allows one. Performer laptops reach KESTREL only through Pomerium and Azure Virtual Desktop, after a posture check. Parent organization devices use Pomerium alone (F38), and vendor devices use only the vendor host pool (F37). The interconnection agreement and the performer's CMMC Level 2 attestation record those terms. A performer laptop passes the posture check only when it meets all of these:

- It is managed by the performer, and its disk is encrypted.
- Its operating system is a supported version, patched within 30 days.
- Its endpoint protection is running and current.

**Privileged access workstations.** These are KESTREL's only owned endpoints outside the VDI pools. Configuration Manager in the Tier 0 enclave enrolls each one and checks it against this compliance policy:

- BitLocker on, with Secure Boot and a healthy TPM
- Virtualization-based security and Credential Guard on
- The operating system patched within the VPMP's deadline
- Defender for Endpoint running in blocking mode, with tamper protection on
- App Control for Business enforced
- No local administrator besides the Tier 0 break-glass account

A workstation that fails any check loses Tier 0 sign-in at once. Configuration Manager tries to remediate it automatically. If that fails within 24 hours, IT Operations reimages it. KESTREL has no mobile devices, and its workstations never travel.

---

## 6. Service Restriction and Least Functionality

*Traces to DI-4.2.1, DI-4.2.2, and DI-4.3.2.*

**The policy.** Every KESTREL host and network path denies all services, ports, and protocols except those its asset type needs. The Host Firewall Rule Baseline and the PPSM record in the appendix list what is permitted. These are prohibited everywhere:

- Telnet, FTP, and TFTP
- SMBv1, and unsigned or unsealed LDAP
- SNMP v1 and v2c
- TLS below 1.2, and any cleartext management protocol
- HTTP for anything other than a redirect to HTTPS

The Security Team approves any protocol a manufacturer requires on fleet equipment, with compensating controls, confined to its conduit.

**Scope and enforcement.** The policy covers every spoke, every on-premises host, the privileged access workstations, and the VDI desktops. Windows Defender Firewall through Configuration Manager and firewalld through Ansible enforce it on each host. The shared Panorama rule base enforces it on the network. Fleet equipment follows its manufacturer's service list, from Phase 3.

**Finding a service out of policy.** ACAS scans and Defender for Cloud CSPM look for services outside the policy, and the hubs' traffic logs find prohibited protocols.

| Where it is found | Severity | What happens |
|---|---|---|
| A DMZ-facing or Tier 0 asset | High | Alerts the Security Team at once, and the owning team disables the service within 24 hours |
| Any other production asset | Medium | Opens a ticket to the owning team, fixed within 7 days |
| A dev/test asset | Low | Opens a ticket to the owning team, fixed within 30 days |

---

## 7. Endpoint Security Controls

*Traces to DI-5.1.2, DI-5.1.3, DI-5.4.6, DI-5.5.2, and DI-5.5.4.*

**Device control.** Across the IT estate, removable storage is blocked by policy. The one exception is the media intake station, which reads only encrypted government media. Bluetooth, cameras, and microphones are disabled on the privileged access workstations and in the VDI image. Permitted peripherals are keyboards, mice, displays, CAC readers, and the YubiKeys used for cloud break-glass. No other exception exists. A request for one is a change under Section 2, and the Security Team must approve it.

**Application control.** App Control for Business runs deny-by-default on the privileged access workstations, the VDI desktops, and Windows servers. Fapolicyd does the same on Red Hat Enterprise Linux servers, including the IT/OT DMZ. Policies audit in Phase 2 and enforce by Phase 3. To add a new program, a team opens a request in Jira Service Management, and the Security Team reviews it. The Platform Team then adds it to the signed policy through a merge request.

**EDR blocking.** Defender for Endpoint runs in audit mode in Phase 1 and in blocking mode from Phase 2. In blocking mode it kills, quarantines, or blocks these without waiting for an analyst:

- Known malware, and files the cloud protection service rates malicious
- Ransomware behavior, such as mass encryption or deletion of shadow copies
- Credential theft, such as reading LSASS memory
- Attack surface reduction rule violations on Windows hosts

Hosts running payload vendor software stay in audit mode until the Security Team profiles that software. Fleet equipment runs no EDR sensor.

**Automated investigation.** Defender XDR investigates every alert by itself and gathers its evidence. It remediates automatically only on non-production hosts. On production hosts it recommends a remediation, and the Security Team approves it. Tier 0 hosts sit in their own device group, which automated response and CSSP playbooks never touch.

**Isolation.** An isolated host can reach only the Defender service, so the Security Team can still investigate it. It is released when the Security Team confirms eradication and a full scan comes back clean. Automated isolation applies only to non-production hosts. The CSSP may isolate a production host only through a pre-approved playbook, which pages the Security Team.

---

## 8. Network Architecture and Segmentation

*Traces to NE-1.1.2, NE-1.6.1, NE-2.4.1, and NE-2.9.1.*

**Rule base and drift.** One Panorama rule base, held as OpenTofu in GitLab, drives both hubs and the alternate site firewall over F35. The APIC takes the data center fabric's policy from the same repository. The pipeline compares every firewall's running policy with its repository and alerts the Platform Team and the Security Team on any difference. An unapproved difference is reverted within one business day.

**Hub and spoke.** The cloud hub's VM-Series pair sits at the center of the ten spokes, and every spoke peers only with it. User-defined routes send all spoke traffic through the hub. Its rules deny traffic from any dev/test spoke to any prod spoke, apart from F25's shared services. They also deny traffic between the two mission teams' spokes. A PA-Series pair fronts the data center's ACI fabric.

**Zones and conduits, from Phase 3.** Each operating site's ground segment has five zones.

| Zone | Security level target |
|---|---|
| Aircraft and datalinks | 3 |
| Ground control stations | 3 |
| Launch and recovery | 3 |
| Operating site services | 2 |
| Payload processing workstation, reserved and empty | 2 |

The IT/OT DMZ carries security level target 3. Each site has its own conduit, ending on its ground segment firewall. An encrypted tunnel over DISN carries it to the IT/OT DMZ (F33). No session spans IT and OT. Fleet Operations designs and validates the zones on the spare stations and the simulator in Phase 2.

**Unidirectional gateways.** KESTREL uses none. The conduit carries recordings out (F3) and certified edge models in (F6), so a firewalled conduit with protocol inspection protects it instead.

---

## 9. Network Access Control

*Traces to NE-1.7.2 and NE-1.8.1.*

**Admission, from Phase 2.** Cisco ISE enforces 802.1X with EAP-TLS on every wired port in the data center and the alternate site. Each operating site follows from Phase 3. Devices present certificates from Active Directory Certificate Services. Privileged access workstations and servers must also pass a posture check:

- A valid device certificate
- Defender for Endpoint running and reporting
- The operating system patched within the VPMP's deadline

Stations and launch equipment that cannot run a supplicant are admitted by registered hardware address to their own zone only. A device that fails is quarantined, and the Security Team is alerted. Each operating site runs its own ISE policy node, so admission keeps working while the site is cut off.

**Wireless.** The command and payload datalinks are KESTREL's only authorized wireless. KESTREL has no wireless LAN. Any future one must use WPA3-Enterprise with EAP-TLS. Embedded radios are disabled on every server, workstation, and station, apart from the station datalink radios. Bastille sensors look for rogue access points at the data center and the alternate site from Phase 2. They extend to each operating site from Phase 3.

---

## 10. Boundary and API Protection

*Traces to NE-2.6.7, NE-2.7.2, and NE-2.7.7.*

**API schemas.** API Management loads each partner API's published schema as its protection policy. It rejects any call outside the schema and admits only registered partner clients. It also admits only routes in the runtime API inventory (`AP-5.7`). The schema rules catch broken object-level authorization and mass assignment by rejecting unknown fields and checking object ownership. Application Gateway WAF v2 adds managed and custom rules in front.

**Just-in-time port access.** Defender for Servers opens a cloud management port only for a just-in-time window. A request qualifies when a Tier 1 administrator names an approved change or an open incident. The window opens for one source address and closes automatically after 3 hours at most. On-premises management ports accept only CyberArk's session hosts, so they need no window.

**Remote access.** KESTREL offers no network tunnel to any remote user. Performers, program office staff, vendors, and CSSP analysts reach it through Pomerium or Azure Virtual Desktop. Neither path routes the user's device onto KESTREL's network. No split tunnel can exist, so KESTREL grants no split-tunnel exception.

---

## 11. Traffic Inspection Tuning

*Traces to NE-2.11.1, NE-2.11.4, NE-3.2.4, NE-3.2.5, and NE-3.8.2.*

The template flags NE-2.11.4, NE-3.2.5, and NE-3.8.2 as reading like logs of tuning events. KESTREL states the standing rule for each here. Each tuning change is a merge request, so the GitLab history is the log.

**Command inspection on the conduit, from Phase 3.** Each ground segment firewall parses the command and control protocol between the stations and the launch and recovery equipment. Custom App-ID signatures allow only each station's approved commands. A DPI fault falls back to a fixed allow-list of those same commands, so launch and recovery are never cut off. The fault alerts Fleet Operations and the Security Team. The operations lead and the Security Team agreed this fallback together. Command and control traffic never crosses the conduit to the data center, so any seen there is blocked.

**Tuning command rules.** Fleet Operations and the Security Team tune the command rules after each maintenance window, against the traffic seen in it. A tuning change may narrow a rule or fix a false positive. It may never add a command a station is not approved to send.

**Intrusion prevention modes.** Threat Prevention blocks at the DMZ's inbound paths, the circuits, and each operating site's conduit. East-west rule sets between spokes start in alert mode. A rule set moves to blocking after 30 days without an unexplained false positive, with the Security Team's approval. Today no rule set is held in alert mode on purpose.

**Signature tuning.** A signature that fires on known-good behavior is narrowed to exclude that source and destination. It is never disabled outright. The Security Team reviews every exclusion each quarter and removes any whose cause has gone.

**Passive monitoring, from Phase 3.** Nozomi Guardian sensors learn each ground segment zone's normal traffic, then alert on deviations. They never act on traffic. Each maintenance window that changes equipment ends with a re-profiling, which Fleet Operations and the Security Team approve. A re-profiling may not absorb a deviation the Security Team has not explained.

---

## 12. DNS and Email Authentication Architecture

*Traces to NE-3.3.1, NE-3.3.4, NE-3.4.3, NE-3.5.1, and NE-3.6.3.*

**Resolvers.** Infoblox NIOS appliances resolve for the data center and the alternate site. A pair of NIOS virtual appliances in Platform Prod, in separate availability zones, resolves for the cloud. Azure DNS holds only the private zones. Hosts may use no other resolver. The hubs block outbound DNS, DNS over HTTPS, and DNS over TLS to anywhere else.

**Authoritative names.** KESTREL's public names sit under the program's DoD parent zone, signed, and point only at the access point's published addresses. DoD publishes their delegation records. No KESTREL resolver answers for them publicly, so the authoritative and recursive roles stay separate.

**Secure DNS.** Every resolver validates DNSSEC. Resolver traffic across the circuits stays inside their IPsec tunnels, since the resolvers do not support encrypted transport between themselves.

**Operating sites, from Phase 3.** Each site runs its own resolver pair, answering only its own names and the IT/OT DMZ. It has no upstream path beyond them, so a lost conduit leaves resolution working.

**Releasing a blocked domain.** Infoblox Threat Defense blocks known-malicious, newly registered, and algorithmically generated domains. A team requests a release in Jira Service Management with the business reason. The Security Team checks the domain and adds a passthru rule that expires after 30 days. A release on a Tier 0 or DMZ asset needs the ISSM's approval. The request tickets are the record of each release.

**Email.** KESTREL runs no email service, and the AO approved removing SI-8 (CCSD tailoring action 1). So it has no DKIM, SPF, or DMARC configuration.

---

## 13. Detection and Alert Data Retention

*Traces to DE-3.2.1, DE-3.2.2, and DE-3.2.4.*

**Tiers.**

| Tier | Where | How long | Why |
|---|---|---|---|
| Hot | Splunk indexers' fast storage | 90 days | Most investigations look back no further |
| Cold | Splunk indexers' slower storage | Months 4 to 12 | Still searchable without a restore, at a slower query speed |
| Archive | StorageGRID with S3 Object Lock | Months 13 to 30 | Restored on request, taking up to one business day |

Security logs therefore stay searchable for 12 months and are kept for 30 in all. That is KESTREL's AU-11 parameter, with OMB M-21-31 as the benchmark. The Security Team measured cold search speed and archive restore time before setting the tier lines.

**Restore test.** Each year the Security Team restores an archived sample and searches it, recording the time taken. A failed test is a finding under Configuration Monitoring.

**Alert records.** Alerts, detection results, and analyst dispositions are kept for 3 years, longer than the logs. They are small, so the longer period costs little. Each alert record carries enough to stand alone after its logs age out:

- The detection rule and its version
- The asset's owner, team, and criticality
- The fields that matched, and the time window
- The analyst's disposition and its reason
- The incident record it led to, if any

Incident records follow the IRP's retention terms. Where the IRP or a POA&M item requires longer, the longer period governs. All telemetry also goes to the CSSP, which keeps its own copy under its service agreement.

---

## 14. Maintenance

*Traces to DI-2.4.1.*

**Scheduling and approval.** On-premises hardware maintenance is scheduled in Jira Service Management. The owning team's lead approves it, and Tier 0 maintenance also needs the Platform Team lead. Fleet maintenance runs only in Fleet Operations' weekly windows, from Phase 3. The cloud provider maintains the cloud hardware.

**Who may do it.** KESTREL's own staff do most maintenance. A vendor engineer is escorted on site at all times. Vendor remote sessions run only through the vendor host pool under Access Process for Third-Party Support (`ID-4.7`).

**Tools and media.** Diagnostic tools and media are approved by the Security Team and scanned at the media intake station before use.

**Repair off site.** Failed drives stay on site for sanitization. Any other component leaving the facility has its storage sanitized with Blancco first, or removed and kept. HSMs are zeroized before shipment.

**After maintenance.** A compliance scan confirms the component still meets its baseline before the record closes. A spare used for penetration testing is reimaged and re-verified before it returns to the pool.

Maintenance runs through the change workflow in Section 2, so a maintenance action and its change share one record.

---

## Appendix: Reference Data and Configuration Baselines

Each item below is living data that a system loads or checks, kept where its tool reads it.

**Firmware Version and Patch-Level Baseline** *(DI-3.5.3)*: The approved firmware for each fleet device model, recorded in Jira Service Management Assets. Fleet Operations proves each version on the spares in Phase 2.

**Host Firewall Rule Baseline** *(DI-5.3.3)*: Default-deny inbound rules per asset type, held in GitLab. Configuration Manager applies the Windows Defender Firewall rules, and Ansible applies the firewalld rules.

**Subnet Allocation and Segmentation Plan** *(NE-1.4.3)*: The address plan for every spoke, segment, and zone in every location. It is held in GitLab with the landing zone modules, and in Infoblox IPAM.

**Communication Requirements Mapping** *(NE-1.5.1)*: Each team's map of the flows its workloads need, held in GitLab. The allow rules on workload security groups, ACI contracts, and Cilium policies derive from it.

**Firewall Policies and Filtering Rules** *(NE-2.4.6)*: The shared Panorama rule base, held as OpenTofu in GitLab. Each ground segment firewall's rule set sits in Fleet Operations' repository.

**WAF Rule Set / Policy Configuration** *(NE-2.6.2)*: Application Gateway WAF v2's managed rule set and each application's custom rules, held as OpenTofu in GitLab.

**Allowed Data Flow/Protocol Definition (Diode)** *(NE-2.9.3)*: Not used. KESTREL has no unidirectional gateway, as Section 8 explains.

**Allowed Function Code/Command Allow-List** *(NE-2.11.2)*: The commands each station may send to its launch and recovery equipment, held in Fleet Operations' repository as custom App-ID signatures. It is built on the spares in Phase 2.

**Approved PPS Baseline / Ports, Protocols, and Services Matrix (PPSM)** *(NE-2.12.2)*: Every port, protocol, and service crossing the boundary, with its justification and approver. It is held in Confluence and registered in the DoD PPSM registry. The pipeline checks the rule base against it on every change from Phase 2.

---

## Approval

**Approved By:** Pending. The Configuration Control Board reviews version 0.1 in Phase 1.

**Circulated To:** the Platform Team, IT Operations, Fleet Operations, the Security Team, every team lead, and the CSSP.

**Approval Date:** Pending.

---

## Periodic Review and Revision

**Review Cadence:** Annually, as a floor.

**Revision Triggers:**
- A change to how components are provisioned, such as a new landing zone module
- A change to a hardening baseline, such as a new STIG release
- A change to the endpoint protection tools
- A new spoke, interconnection, or operating site
- The arrival of the IT/OT DMZ in Phase 2 or the fleet in Phase 3
- A change to a governing requirement
- A material finding from Configuration Monitoring or Device Compliance that cannot close without changing this plan
- A product substitution recorded in the Security Implementation Plan, for any product this document names
