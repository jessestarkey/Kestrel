# NE: Network and Environment

*KESTREL Security Implementation Plan, Section 4 (Protect). Each record implements the outcome of the same ID in the [SADD](../03-sadd/04-network-and-environment.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## NE-1: Network Management and Segmentation

### NE-1.1: Network Centralization and Standardization

**Selected Tool / Product / Service:** Panorama with the PAN-OS provider for OpenTofu, Cisco ACI and APIC, OpenTofu, GitLab Ultimate

**Environment-Specific Tailoring:** One Panorama rule base, held as OpenTofu in GitLab, drives both hubs and the alternate site firewall. The APIC takes the data center fabric's policy from the same repository. A change is a merge request with a second reviewer, and changes to the shared rule base go to the Configuration Control Board. The ground segment firewall keeps its own rule set under Fleet Operations, since the conduit stays a separate boundary.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.1.1: Centralized Policy Enforcement | 1 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-1.1.2: Firewall Standardization and Routing Management | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.1.3: Network Resource Configuration Governance | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-1.1.4: Firewall/Routing Configuration Drift Detection and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### NE-1.2: Network Infrastructure Device Hardening

**Selected Tool / Product / Service:** DISA SCAP Compliance Checker and STIG Viewer, Panorama with the PAN-OS provider for OpenTofu, Cisco ACI and APIC, CyberArk Privileged Access Manager

**Environment-Specific Tailoring:** DISA STIGs harden the VM-Series cloud hub, the data center hub's PA-Series pair, and the alternate site firewall. They also harden the ACI switches and APIC, checked with the SCAP Compliance Checker. Ground segment switches are hardened on the spares in Phase 2 and at each operating site when the fleet integrates. Management interfaces accept only CyberArk-brokered sessions from the out-of-band network. The cloud and data center run dual-stack, and the ground segment drops IPv6 at its conduit.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.4, ID-4.4

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.2.1: Network Device Hardening Baseline Definition | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.2.2: Device Management Plane Hardening | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-1.2.3: IPv6 and Dual-Stack Disposition | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### NE-1.3: Insecure Services and Protocols

**Selected Tool / Product / Service:** Panorama with the PAN-OS provider for OpenTofu, Tenable Security Center (ACAS), Corelight sensors

**Environment-Specific Tailoring:** The hubs' traffic logs and ACAS scans find cleartext and obsolete protocols from Phase 1. Corelight sensors on the data center's span ports join in Phase 2. Each one found is disabled through the change process. If the payload processing workstation's replacement slips past 2027-09-30, the workstation connects only after the AO re-dates CCSD tailoring action 3. Its transfer to the data lake is then the one registered exception.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.4, NE-3.2

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C14](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.3.1: Insecure Protocol Discovery | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.3.2: Insecure Services and Protocols Disabling | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |
| NE-1.3.3: Compensating Controls Implementation | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

### NE-1.4: Network Macro Segmentation

**Selected Tool / Product / Service:** the Platform Team's landing zone modules derived from Mission Landing Zone, Panorama with the PAN-OS provider for OpenTofu, Cisco ACI and APIC, OpenTofu

**Environment-Specific Tailoring:** The landing zone modules create the ten spokes, and ACI endpoint groups give each mission team's data lake zone its own segment. The DMZ, the VDI spoke, and Tier 0 each sit in their own segment. The data center's out-of-band management network is cabled when it is built. The alternate site's management interfaces sit in their own firewall zone.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.4.1: Network Topology Design | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |
| NE-1.4.2: High-Risk Workload Isolation | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-1.4.3: Subnet Allocation and Segmentation Plan | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.4.4: Out-of-Band Management Network Isolation | 1 (pinned) | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |

**Pinned:** NE-1.4.4: Built in when the platform is created, since retrofitting it later costs far more. The out-of-band network is cabled when the data center is built.

### NE-1.5: Network Micro Segmentation

**Selected Tool / Product / Service:** Azure CNI Powered by Cilium network policy, Cisco ACI and APIC, Azure Monitor and VNet flow logs, Open Policy Agent (Gatekeeper and Conftest), Splunk Enterprise, the penetration testing provider

**Environment-Specific Tailoring:** Workload security groups in each spoke and ACI contracts in the data center carry each team's mapped flows, with everything else denied. AKS clusters use Cilium network policy that denies traffic between namespaces from their creation, and Gatekeeper rejects a namespace without one. Flow logs go to Splunk, which flags rules unused for 90 days. The penetration testers try the vendor split and the dev/test to prod deny in each annual test.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.4, DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C28](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.5.1: Communication Requirements Mapping | 1 (pinned) | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-1.5.2: Allow and Deny Rules | 1 (pinned) | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-1.5.3: Workload/Application-Based Security Grouping | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.5.4: Flow Logs Monitoring and Optimization | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-1.5.5: Security Group and Firewall Rule Drift Detection | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.5.6: Segmentation Enforcement Validation and Exfiltration Testing | 2 | Process | None | Level 2 | Periodic (Annual) (re-rated) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |

**Pinned:** NE-1.5.1: The first rules carry the flows the system description already maps. NE-1.5.2: Built in when the platform is created, since retrofitting it later costs far more. Default-deny namespace policy is set when each AKS cluster is created, and the first clusters run in Phase 1.

**Re-rated:** NE-1.5.6: The penetration testers test the whole system, including its internal segmentation, each year.

### NE-1.6: IT/OT Zone and Conduit Segmentation (IEC 62443)

**Selected Tool / Product / Service:** Palo Alto Networks PA-Series, Nozomi Networks Guardian

**Environment-Specific Tailoring:** The zones and conduits are designed and validated on the spare stations and the simulator in Phase 2. Device identity and maintenance windows then build on them. Each operating site's conduit allow-lists are applied when the fleet integrates. The IT/OT DMZ's staging servers are built behind the data center hub in Phase 2, giving fleet recordings and host logs their path.

**Accountable Team:** Fleet Operations, with the Platform Team for the IT/OT DMZ

**Dependencies:** NE-1.4

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C13](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.6.1: Zone and Conduit Model Definition | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |
| NE-1.6.2: Security Level Target (SL-T) Assignment | 2 | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.6.3: Conduit Access Control and Allow-Listing | 2 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-1.6.4: IT/OT Demilitarized Zone | 2 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-1.6.5: Zone-to-Zone Data Flow Monitoring | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-1.6.6: Zone Segmentation Enforcement Validation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### NE-1.7: Network Access Control (NAC/802.1X)

**Selected Tool / Product / Service:** Cisco Identity Services Engine, Active Directory Certificate Services

**Environment-Specific Tailoring:** Cisco ISE enforces 802.1X on every wired port in the data center and at the alternate site. Devices present certificates from Active Directory Certificate Services. Posture checks gate the privileged access workstations and servers. Stations and launch equipment without a supplicant are admitted by registered hardware address to their own zone. This is proven on the spares, then applied at each operating site. Each operating site runs its own ISE policy node, so admission works while the site is cut off. A failed device is quarantined, and the Security Team is alerted.

**Accountable Team:** Platform Team, with Fleet Operations at the operating sites

**Dependencies:** DA-3.7, ID-3.7, NE-1.6

**Funding Line:** FY28 O&M, platform and security operations, with the fleet slice as RDT&E fleet integration

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C09](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.7.1: 802.1X Port-Based Authentication Deployment | 2 | Technical | None | Level 1 | Continuous | Extensive | One-Time: Extensive; Recurring: Moderate | Long-term (6+ months) |
| NE-1.7.2: NAC Device Compliance/Posture Policy Definition | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.7.3: OT and Legacy Device Network Admission | 2 | Technical | None | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| NE-1.7.4: Rogue Device Detection and Quarantine | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### NE-1.8: Wireless Network Access Control

**Selected Tool / Product / Service:** Bastille Enterprise, Splunk Enterprise

**Environment-Specific Tailoring:** Bastille sensors detect rogue access points and unauthorized radios at the data center and the alternate site from Phase 2. They extend to each operating site when the fleet integrates. Alerts reach the Security Team through Splunk. No wireless LAN exists, so WPA2/3-Enterprise has nothing to authenticate, and any future one must use it.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C23](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.8.1: Wireless Access Policy and Authorization | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-1.8.2: Wireless Network Authentication (WPA2/3-Enterprise) | N/A | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.8.3: Rogue Access Point Detection | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

**Not applicable:** NE-1.8.2: KESTREL has no wireless LAN, so there is nothing for WPA2/3-Enterprise to authenticate. NE-1.8 requires it of any future one.

## NE-2: Network Boundary Security

### NE-2.1: Private Connectivity

**Selected Tool / Product / Service:** Azure Private Link, Azure ExpressRoute, ExpressRoute circuits from two carriers, Palo Alto Networks VM-Series, Palo Alto Networks PA-Series, Azure Policy

**Environment-Specific Tailoring:** Every provider-managed service gets a private endpoint in its own spoke, and Azure Policy denies public network access. The data center and alternate site circuits come from different carriers and terminate on the cloud hub and each site's firewall. ExpressRoute private peering is not encrypted, so IPsec tunnels in FIPS-CC mode run between the firewalls inside each circuit. The cloud hub terminates them on an active/passive VM-Series pair, sized for the bulk flows F4 and F20. BGP sessions are authenticated, and prefix filters accept only KESTREL's address ranges.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1, NE-3.4, DA-3.7

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C25](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.1.1: Private Network Endpoint Deployment | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-2.1.2: Public Network Access Disablement (private-only enforcement) | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.1.3: Private Network Endpoint Monitoring | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.1.4: Dedicated Private Circuit Connectivity | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: High | Long-term (6+ months) |
| NE-2.1.5: Routing Protocol and Control Plane Protection | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### NE-2.2: Platform Service Network Integration

**Selected Tool / Product / Service:** Azure API Management, Azure Kubernetes Service, Azure Machine Learning, Azure Application Gateway WAF v2

**Environment-Specific Tailoring:** AKS, Azure Machine Learning, and API Management are injected into their spokes' subnets, so their traffic follows the hub's routes. Application Gateway runs as a private deployment with no public IP, and its listeners exist only in the DMZ. GV-5.12 confirms the private deployment in Azure Government before the first gateway is built. Mission team services publish only internal listeners. The Platform Team reviews internal connections each quarter and removes any that no longer match a documented flow.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.4

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.2.1: Service Virtual Network Deployments | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-2.2.2: Service Communication Configuration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.2.3: Load Balancer and Edge Listener Configuration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.2.4: Internal Connection Review and Termination | 1 | Process | None | Level 1 | Periodic (Quarterly) (re-rated) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Re-rated:** NE-2.2.4: The SADD's NE-2.2 design intent reviews internal connections each quarter.

### NE-2.3: Service Native Firewall Configurations

**Selected Tool / Product / Service:** Azure Policy, Azure Key Vault Premium, Azure SQL Database, Azure Private Link

**Environment-Specific Tailoring:** Key Vault, Azure SQL, the feedback endpoints' queues, and each foundation model deployment have their resource firewalls on. Each admits only its own spoke's private endpoint and the workloads that need it, and Azure Policy denies any change that opens one. No platform service is public, so no public allow-list exists.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.3.1: Service Native Firewall Capability Enablement | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.3.2: Service Firewall Rules | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.3.3: Service Public Access Allow-List Configuration | N/A | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** NE-2.3.2: KESTREL's design depends on it from the first build, since provider-managed services accept traffic only from their own spoke.

**Not applicable:** NE-2.3.3: No KESTREL platform service is reachable over a public address, so no public allow-list exists.

### NE-2.4: Network Firewall

**Selected Tool / Product / Service:** Palo Alto Networks VM-Series, Palo Alto Networks PA-Series, Panorama with the PAN-OS provider for OpenTofu

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub, with every spoke peered only to it and user-defined routes sending all traffic through it. A PA-Series pair fronts the data center's ACI fabric. From Phase 1, custom URL categories limit outbound web traffic to the update and package sources the package mirror uses. Both hubs decrypt outbound TLS from Phase 2 with a program PKI certificate, exempting mutual TLS between workload identities.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.1, NE-1.4, DA-3.7

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.4.1: Hub and Spoke Cloud Network Topology | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |
| NE-2.4.2: Spoke Cloud Network Peering | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.4.3: Custom Routing Configuration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.4.4: Cloud-Native Firewall Deployment | 1 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| NE-2.4.5: On-Premises Perimeter Firewall Deployment | 1 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-2.4.6: Firewall Policies and Filtering Rules | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.4.7: HTTP/HTTPS Traffic URL Filtering | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.4.8: TLS Inspection Advanced Filtering | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |

**Pinned:** NE-2.4.7: The boundary stack the access point connection needs limits outbound web traffic to the package mirror's sources.

### NE-2.5: DDoS Protection

**Selected Tool / Product / Service:** the DISA Boundary Cloud Access Point, Azure Application Gateway WAF v2, Palo Alto Networks VM-Series, Palo Alto Networks PA-Series

**Environment-Specific Tailoring:** The DMZ holds no Azure public IP resources, so Azure DDoS Network Protection has nothing to cover. Its DoD-registered addresses are reached only through DISA's internet access points and the Boundary Cloud Access Point, which absorb network-layer floods upstream. Application Gateway rate-limits requests to each user-facing application. DoS protection policies on the cloud hub, matched to each spoke's address range, limit what any spoke can send. Flood alerts go to Splunk.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.4, NE-2.6, NE-2.13

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.5.1: Network Layer DDoS Protection | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| NE-2.5.2: Application Layer DDoS Protection | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| NE-2.5.3: DDoS Protection Monitoring and Alerts | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.5.4: Outbound and Internal Flood Containment | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### NE-2.6: Web Application Firewall

**Selected Tool / Product / Service:** Azure Application Gateway WAF v2, Azure API Management

**Environment-Specific Tailoring:** Application Gateway WAF v2 fronts the identity-aware proxy in blocking mode from Phase 1. The analyst portal, the signals workbench, and the partner API join it when they arrive in Phase 2, each with managed and custom rules. API Management checks every partner call against its published schema and rate-limits each partner. It admits only routes in AP-5.7's inventory. Nothing on premises faces users, so no on-premises WAF is built.

**Accountable Team:** Platform Team, with the mission teams

**Dependencies:** NE-2.2

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.6.1: WAF Service Selection | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.6.2: WAF Policy Configurations and Custom Rules | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.6.3: WAF Policy Mode | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.6.4: WAF Policy and Service Endpoint Associations | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.6.5: On-Premises Reverse-Proxy WAF Deployment | N/A | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-2.6.6: Bot Management and Request Rate Limiting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| NE-2.6.7: API Protection Policy and Schema Validation | 2 (pinned) | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-2.6.8: API Gateway Runtime Policy Enforcement | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |

**Pinned:** NE-2.6.7: The partner API, whose calls API Management checks against its schema, arrives in Phase 2.

**Not applicable:** NE-2.6.5: Nothing on premises faces users, so no on-premises reverse-proxy WAF is needed.

### NE-2.7: Secure Remote Access

**Selected Tool / Product / Service:** Pomerium Enterprise, Azure Virtual Desktop, Azure Private Link, Defender for Servers, CyberArk Privileged Access Manager

**Environment-Specific Tailoring:** Pomerium admits developers to GitLab, CI, and the experimentation workspaces from the first commit, behind the DMZ's WAF. Azure Virtual Desktop admits operators and CSSP analysts through private endpoints in the DMZ, with public access disabled. The performer hosts their names in its own DNS, pointing at DMZ addresses KESTREL supplies under the interconnection agreement. Neither path offers a network tunnel, so no laptop joins KESTREL's network. Defender for Servers opens cloud management ports only for a just-in-time window. On-premises management ports accept only CyberArk's session hosts. Sessions end after 15 idle minutes, and the Security Team can end any session at once.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.6, NE-2.13, ID-4.4, GV-5.6

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C22](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.7.1: Private Remote Access | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-2.7.2: JIT Network Port Access | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-2.7.3: Remote Access Key Management | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.7.4: Virtual Desktop Isolation | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Extensive; Recurring: High | Medium-term (3–6 months) |
| NE-2.7.5: Browser Based Access | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.7.6: Virtual Desktop Monitoring and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.7.7: Split Tunneling Prevention | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.7.8: Remote Session Disconnect Capability | 2 | Technical | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.7.9: Idle Network Connection Termination | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** NE-2.7.2: KESTREL's design depends on it from the first build, since management ports open only for a just-in-time window or to the session hosts. NE-2.7.5: KESTREL's design depends on it from the first build, since developers reach GitLab through the identity-aware proxy from the first commit.

### NE-2.8: Telemetry, Tracking, and Command (TT&C) Link Security

**Selected Tool / Product / Service:** the datalink crypto modules, Entrust nShield 5 HSMs

**Environment-Specific Tailoring:** The FIPS 140-3 validated datalink crypto modules provide the authenticated encryption these activities name, since CCSDS SDLS does not apply. Keys are generated in the nShield HSMs and loaded with a key loader. Authentication and encryption are tested on spare aircraft and the simulator in Phase 2, before any aircraft carries mission data. Every operational aircraft and station is keyed when the fleet integrates.

**Accountable Team:** Fleet Operations

**Dependencies:** ID-3.7, DA-3.4

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C26](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.8.1: Command Uplink Authentication and Encryption (CCSDS SDLS) | 2 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Long-term (6+ months) |
| NE-2.8.2: Telemetry Downlink Authentication and Integrity Protection (CCSDS SDLS) | 2 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Long-term (6+ months) |
| NE-2.8.3: Link-Anomaly and Jamming-Indicator Monitoring and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### NE-2.10: Cross Domain Solution (CDS) Transfer Procedures

**Selected Tool / Product / Service:** the cross domain service provider's enterprise CDS, Splunk Enterprise

**Environment-Specific Tailoring:** The cross domain service provider selects, operates, and accredits the CDS, so KESTREL confirms its Baseline List entry and tracks its reaccreditation. Onboarding starts in Phase 2, and the first transfers run in Phase 3. The transfer gateway in the DMZ stages low-to-high baselines only after Certification to Field approval. High-to-low products pass the enclave's release review and then KESTREL's own content checks. The provider's transfer logs and the gateway's logs go to Splunk.

**Accountable Team:** Platform Team

**Dependencies:** AP-4.5, GV-5.6

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.10.1: CDS Product Selection and Baseline List Compliance | 2 | Process | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Long-term (6+ months) |
| NE-2.10.2: CDS Transfer Request and Approval Workflow | 2 | Process | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| NE-2.10.3: Policy-Based Automated Transfer Release | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-2.10.4: Content Inspection/Filtering Prior to Transfer | 2 | Technical | None | Level 2 | Continuous | High | One-Time: Extensive; Recurring: Moderate | Long-term (6+ months) |
| NE-2.10.5: Transfer Audit Logging and Review | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| NE-2.10.6: CDS Accreditation and Periodic Reassessment | 2 | Process | None | Level 2 | Periodic (Annual) | High | One-Time: High; Recurring: Moderate | Long-term (6+ months) |
| NE-2.10.7: Manual Cross-Domain Media Transfer | N/A | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

**Not applicable:** NE-2.10.7: Manual media transfer across the domains is prohibited, so no manual transfer procedure is run.

### NE-2.11: Industrial Protocol Filtering (DPI)

**Selected Tool / Product / Service:** Palo Alto Networks PA-Series, Nozomi Networks Guardian, the aircraft and ground equipment manufacturer's tools

**Environment-Specific Tailoring:** Custom App-ID signatures, built from the manufacturer's protocol documentation, let the ground segment firewall allow only each station's approved commands. They are built and tested on the spares in Phase 2 and applied at each operating site when the fleet integrates. Command and control traffic never crosses the conduit to the data center, so any seen there is blocked and alerted. Fleet Operations and the Security Team tune the rules after each maintenance window.

**Accountable Team:** Fleet Operations

**Dependencies:** NE-1.6

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C13](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.11.1: Protocol-Aware DPI Deployment | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Moderate | Long-term (6+ months) |
| NE-2.11.2: Allowed Function Code/Command Allow-Listing | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-2.11.3: Unauthorized Command Blocking and Alerting | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.11.4: DPI Rule Tuning and False-Positive Management | 2 | Process | None | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |

### NE-2.12: Ports, Protocols, and Services Matrix (PPSM)

**Selected Tool / Product / Service:** the DoD PPSM registry, Panorama with the PAN-OS provider for OpenTofu

**Environment-Specific Tailoring:** The Security Team registers every port, protocol, and service crossing the boundary in the DoD PPSM registry before the access point connection is approved. These include the access point flows, the circuits, the CSSP feed, the cross domain transfers, and the partner API. The DMZ's internet-facing services are also registered for DISA's internet access points. From Phase 2 the pipeline checks the Panorama rule base against the registration on every change. The registration is recertified each year.

**Accountable Team:** Security Team

**Dependencies:** NE-1.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.12.1: PPSM Registration and CAL (category assurance list) Alignment | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| NE-2.12.2: PPS Baseline Documentation and Approval | 1 (pinned) | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.12.3: Boundary Enforcement Validation Against PPSM | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.12.4: PPSM Periodic Review and Recertification | 2 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

**Pinned:** NE-2.12.1 and NE-2.12.2: The access point connection approved in Phase 1 requires the PPSM registration first.

### NE-2.13: Authorized Cloud Access Point Integration

**Selected Tool / Product / Service:** the DISA Boundary Cloud Access Point, the Platform Team's landing zone modules derived from Mission Landing Zone, Palo Alto Networks VM-Series, Azure Policy

**Environment-Specific Tailoring:** Every user flow arrives through DISA's internet access points, the Boundary Cloud Access Point, and the cloud hub. Azure Policy denies Azure public IP resources in every spoke. From Phase 1 the mission-owner stack is the VM-Series hub with Threat Prevention and outbound URL filtering, followed by the DMZ's WAF. Administration uses its own path through the VDI brokers and the privileged access workstations. DISA approves the access point connection and the two dedicated circuits before the DMZ accepts traffic.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.4, NE-2.12, GV-5.6, GV-5.7, RS-1.7

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), plus government-furnished and open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.13.1: Designated Access Point Routing Enforcement | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.13.2: Mission-Owner Boundary Security Stack | 1 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-2.13.3: Segregated Management Path | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.13.4: Access Point Registration and Connection Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## NE-3: Network Visibility

### NE-3.1: Network Telemetry and Security Posture Visualization

**Selected Tool / Product / Service:** Splunk Enterprise, Corelight sensors, Azure Monitor and VNet flow logs, Cisco ACI and APIC

**Environment-Specific Tailoring:** VNet flow logs, the hubs' traffic and threat logs, and ACI flow telemetry reach Splunk from Phase 1. The CSSP therefore watches the network from the interim authorization to test. Corelight sensors on the data center's span ports join in Phase 2, and the ground segment's Guardian sensors when the fleet integrates. The Platform Team, the Security Team, and the CSSP share one network posture dashboard.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.4, DE-3.1, RS-1.7

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C14](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.1.1: Centralized Network Telemetry and Analytics Platform | 1 (pinned) | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-3.1.2: Network Security Posture Dashboard | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** NE-3.1.1: Required for the interim authorization to test, since the CSSP watches the hubs from the first build.

### NE-3.2: IDPS

**Selected Tool / Product / Service:** Palo Alto Threat Prevention with on-box signatures, Corelight sensors

**Environment-Specific Tailoring:** Threat Prevention runs on both hubs and the alternate site firewall from Phase 1, blocking at the DMZ's inbound paths and the circuits. The ground segment conduit is covered once the IT/OT DMZ is built in Phase 2. Signatures update through Panorama. East-west rules between spokes start in alert mode and move to blocking as the Security Team tunes them. Corelight sensors on the data center's span ports add detection behind the hub.

**Accountable Team:** Platform Team, with the Security Team for signature tuning

**Dependencies:** NE-2.4, DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C14](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.2.1: Cloud-Native Firewall Advanced Threat Protection Deployment | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| NE-3.2.2: On-Premises IDPS Sensor Deployment | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-3.2.3: IDPS Signature Rules Selection | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-3.2.4: IDPS Mode Configuration | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-3.2.5: Signature Fine-Tuning | 2 | Process | None | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |

**Pinned:** NE-3.2.1, NE-3.2.3, and NE-3.2.4: The boundary stack the access point connection needs includes intrusion prevention, and that connection is made in Phase 1.

### NE-3.3: Trusted DNS Service

**Selected Tool / Product / Service:** Infoblox NIOS, Infoblox NIOS virtual appliances in Azure, Azure DNS

**Environment-Specific Tailoring:** Infoblox NIOS appliances resolve for the data center and the alternate site, and NIOS virtual appliances in Platform Prod resolve for the cloud. Hosts may use no other resolver, outbound queries are filtered by policy, and every resolver validates DNSSEC. KESTREL's public names sit in a signed Azure DNS zone. Resolver traffic across the circuits stays inside their IPsec tunnels.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C12](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.3.1: Managed DNS Service Selection | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-3.3.2: Managed DNS Firewall Rules | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-3.3.3: Managed DNS Hosted Domains | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-3.3.4: Secure DNS Deployment Guidelines | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### NE-3.4: Private DNS Service

**Selected Tool / Product / Service:** Infoblox NIOS, Infoblox NIOS virtual appliances in Azure, Azure DNS

**Environment-Specific Tailoring:** Azure DNS private zones resolve each managed service to its private endpoint, and each spoke's names sit in its own zone. The cloud and data center resolvers forward each other's names across the circuit, so a circuit outage leaves local resolution working. Each operating site gets its own resolver pair, answering only its own names and the IT/OT DMZ. The pair is built on the spares in Phase 2 and at each operating site when the fleet integrates.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C12](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.4.1: Managed Private DNS for Private Resolution | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-3.4.2: Managed Private DNS for Private Endpoints | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-3.4.3: Custom DNS for Restricted Resolution | 2 (pinned) | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |

**Pinned:** NE-3.4.1 and NE-3.4.2: KESTREL's design depends on it from the first build, since private endpoints do not resolve without it. NE-3.4.3: Its only user is the ground segment, whose resolution is built on the spare stations and the simulator in Phase 2.

### NE-3.5: DNS Advanced Protection

**Selected Tool / Product / Service:** Infoblox Threat Defense, Splunk Enterprise

**Environment-Specific Tailoring:** Infoblox Threat Defense feeds reach every resolver as response policy zones, pulled by zone transfer through the hub. No query data is sent to Infoblox. The CSSP's indicators load as a local response policy zone. Query logs go to Splunk, where analytics look for tunneling, beaconing, and exfiltration. Records are checked continuously against the asset inventory to catch dangling records.

**Accountable Team:** Platform Team

**Dependencies:** NE-3.3, DI-1.1, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C12](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.5.1: Managed DNS Threat Protection | 2 | Technical | Automate | Level 1 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| NE-3.5.2: Malicious DNS Activity Monitoring | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-3.5.3: Dangling DNS Records Detection | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### NE-3.7: External Attack Surface Management

**Selected Tool / Product / Service:** Tenable Attack Surface Management, GitGuardian public monitoring, Jira Service Management Data Center

**Environment-Specific Tailoring:** Tenable Attack Surface Management watches KESTREL's public names and services continuously from outside. The Security Team reviews its findings against the inventory each month. GitGuardian watches public code hosting and paste sites for KESTREL's code, secrets, and credentials, since source code lives on performer laptops. Each finding opens a Jira Service Management ticket to the owning team.

**Accountable Team:** Security Team

**Dependencies:** DI-1.1, NE-2.13

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C29](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.7.1: Internet-Facing Asset and Exposure Discovery | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| NE-3.7.2: Shadow IT and Unsanctioned Cloud Resource Discovery | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-3.7.3: Leaked Credential and Exposed Secret Monitoring | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| NE-3.7.4: Exposure Finding Remediation Tracking | 2 | Process | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### NE-3.8: OT/Legacy Passive Monitoring

**Selected Tool / Product / Service:** Nozomi Networks Guardian

**Environment-Specific Tailoring:** Guardian sensors profile normal traffic in each ground segment zone once the fleet integrates, after their tuning on the spares under DI-1.2. Deviations alert Fleet Operations and the Security Team, and the sensors never act on traffic. Each maintenance window that changes equipment ends with a re-profiling.

**Accountable Team:** Fleet Operations

**Dependencies:** DI-1.2, NE-1.6

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C13](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.8.1: Passive Network Baseline Profiling | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-3.8.2: Anomaly Detection Rule/Model Tuning | 3 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| NE-3.8.3: Anomaly Alerting and Operator Notification | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-3.8.4: Baseline Re-Profiling After Authorized Change | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### NE-3.9: GNSS/PNT Spoofing and Jamming Detection

**Selected Tool / Product / Service:** the aircraft and ground equipment manufacturer's tools, Microchip SyncServer S650, Splunk Enterprise

**Environment-Specific Tailoring:** Each aircraft's GNSS signal and solution quality is profiled and compared with its inertial navigation. Each operating site has its own SyncServer as a holdover reference. Each station compares its GNSS timing with it, and with the data center's SyncServer whenever the conduit is up. Spoofing and jamming indicators alert the operator during flight and reach the Security Team through Splunk.

**Accountable Team:** Fleet Operations

**Dependencies:** NE-2.8, DE-2.8

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C26](index.md#6-contracting-and-procurement-cross-references), [C20](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.9.1: PNT Signal Profiling and Spoofing/Jamming Indicator Detection | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| NE-3.9.2: Cross-Source PNT Consistency Validation | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-3.9.3: Spoofing/Jamming Alerting and Operator Notification | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
