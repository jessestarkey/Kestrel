# NE: Network and Environment

*KESTREL Security Implementation Plan, Section 4 (Protect). Each record implements the outcome of the same ID in the [SADD](../03-sadd/04-network-and-environment.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## NE-1: Network Management and Segmentation

### NE-1.1: Network Centralization and Standardization

**Selected Tool / Product / Service:** Panorama with the Terraform PAN-OS provider, Cisco ACI and APIC, Terraform

**Environment-Specific Tailoring:** Cloud segmentation is the ten spoke VNets and their NSGs. Data center and alternate site segmentation is Cisco ACI endpoint groups, and the ground segment uses its own zoned firewall.

**Accountable Team:** Platform Team

**Dependencies:** DI-2.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.1.1: Centralized Policy Enforcement | 1 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-1.1.2: Firewall Standardization and Routing Management | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.1.3: Network Resource Configuration Governance | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-1.1.4: Firewall/Routing Configuration Drift Detection and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### NE-1.2: Network Infrastructure Device Hardening

**Selected Tool / Product / Service:** DISA SCAP Compliance Checker and STIG Viewer, Cisco ACI and APIC, Panorama with the Terraform PAN-OS provider

**Environment-Specific Tailoring:** Cloud segmentation is the ten spoke VNets and their NSGs. Data center and alternate site segmentation is Cisco ACI endpoint groups, and the ground segment uses its own zoned firewall.

**Accountable Team:** Platform Team

**Dependencies:** DI-2.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C09](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.2.1: Network Device Hardening Baseline Definition | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.2.2: Device Management Plane Hardening | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-1.2.3: IPv6 and Dual-Stack Disposition | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### NE-1.3: Insecure Services and Protocols

**Selected Tool / Product / Service:** Corelight sensors, Tenable Security Center (ACAS)

**Environment-Specific Tailoring:** Cloud segmentation is the ten spoke VNets and their NSGs. Data center and alternate site segmentation is Cisco ACI endpoint groups, and the ground segment uses its own zoned firewall.

**Accountable Team:** Platform Team

**Dependencies:** DI-2.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C14](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.3.1: Insecure Protocol Discovery | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.3.2: Insecure Services and Protocols Disabling | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |
| NE-1.3.3: Compensating Controls Implementation | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

### NE-1.4: Network Macro Segmentation

**Selected Tool / Product / Service:** Panorama with the Terraform PAN-OS provider, Cisco ACI and APIC, Terraform

**Environment-Specific Tailoring:** Cloud segmentation is the ten spoke VNets and their NSGs. Data center and alternate site segmentation is Cisco ACI endpoint groups, and the ground segment uses its own zoned firewall.

**Accountable Team:** Platform Team

**Dependencies:** DI-2.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

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

**Selected Tool / Product / Service:** Azure CNI Powered by Cilium network policy, Cisco ACI and APIC, Azure Monitor and VNet flow logs, Open Policy Agent (Gatekeeper and Conftest)

**Environment-Specific Tailoring:** Cloud segmentation is the ten spoke VNets and their NSGs. Data center and alternate site segmentation is Cisco ACI endpoint groups, and the ground segment uses its own zoned firewall.

**Accountable Team:** Platform Team

**Dependencies:** DI-2.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.5.1: Communication Requirements Mapping | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-1.5.2: Allow and Deny Rules | 2 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-1.5.3: Workload/Application-Based Security Grouping | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.5.4: Flow Logs Monitoring and Optimization | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-1.5.5: Security Group and Firewall Rule Drift Detection | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.5.6: Segmentation Enforcement Validation and Exfiltration Testing | 2 | Process | None | Level 2 | Periodic (Semi-Annual) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |

### NE-1.6: IT/OT Zone and Conduit Segmentation (IEC 62443)

**Selected Tool / Product / Service:** Palo Alto Networks PA-Series, Nozomi Networks Guardian

**Environment-Specific Tailoring:** Cloud segmentation is the ten spoke VNets and their NSGs. Data center and alternate site segmentation is Cisco ACI endpoint groups, and the ground segment uses its own zoned firewall.

**Accountable Team:** Fleet Operations

**Dependencies:** DI-2.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-06-30

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C13](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.6.1: Zone and Conduit Model Definition | 3 | Documentation | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |
| NE-1.6.2: Security Level Target (SL-T) Assignment | 3 | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.6.3: Conduit Access Control and Allow-Listing | 3 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-1.6.4: IT/OT Demilitarized Zone | 3 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-1.6.5: Zone-to-Zone Data Flow Monitoring | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-1.6.6: Zone Segmentation Enforcement Validation | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### NE-1.7: Network Access Control (NAC/802.1X)

**Selected Tool / Product / Service:** Cisco Identity Services Engine, Active Directory Certificate Services

**Environment-Specific Tailoring:** Cloud segmentation is the ten spoke VNets and their NSGs. Data center and alternate site segmentation is Cisco ACI endpoint groups, and the ground segment uses its own zoned firewall.

**Accountable Team:** Platform Team

**Dependencies:** DI-2.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

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

**Selected Tool / Product / Service:** Bastille Enterprise

**Environment-Specific Tailoring:** Cloud segmentation is the ten spoke VNets and their NSGs. Data center and alternate site segmentation is Cisco ACI endpoint groups, and the ground segment uses its own zoned firewall.

**Accountable Team:** Security Team

**Dependencies:** DI-2.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C23](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-1.8.1: Wireless Access Policy and Authorization | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-1.8.2: Wireless Network Authentication (WPA2/3-Enterprise) | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-1.8.3: Rogue Access Point Detection | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

## NE-2: Network Boundary Security

### NE-2.1: Private Connectivity

**Selected Tool / Product / Service:** Azure Private Link, Azure ExpressRoute, ExpressRoute circuits from two carriers, Azure Policy

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.4, ID-1.3

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C25](index.md#6-contracting-and-procurement-cross-references)

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

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.4, ID-1.3

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.2.1: Service Virtual Network Deployments | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-2.2.2: Service Communication Configuration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.2.3: Load Balancer and Edge Listener Configuration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.2.4: Internal Connection Review and Termination | 1 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### NE-2.3: Service Native Firewall Configurations

**Selected Tool / Product / Service:** Azure Policy, Azure Key Vault Premium, Azure SQL Database, Azure Private Link

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.4, ID-1.3

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.3.1: Service Native Firewall Capability Enablement | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.3.2: Service Firewall Rules | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.3.3: Service Public Access Allow-List Configuration | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** NE-2.3.2: KESTREL's design depends on it from the first build, since provider-managed services accept traffic only from their own spoke.

### NE-2.4: Network Firewall

**Selected Tool / Product / Service:** Palo Alto Networks VM-Series, Palo Alto Networks PA-Series, Panorama with the Terraform PAN-OS provider, Palo Alto Advanced URL Filtering

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.4, ID-1.3

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

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
| NE-2.4.7: HTTP/HTTPS Traffic URL Filtering | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.4.8: TLS Inspection Advanced Filtering | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |

### NE-2.5: DDoS Protection

**Selected Tool / Product / Service:** Azure DDoS Network Protection, Azure Application Gateway WAF v2, Palo Alto Networks PA-Series, the DISA Boundary Cloud Access Point

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.4, ID-1.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

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

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Platform Team, with the mission teams

**Dependencies:** NE-1.4, ID-1.3

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.6.1: WAF Service Selection | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.6.2: WAF Policy Configurations and Custom Rules | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.6.3: WAF Policy Mode | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.6.4: WAF Policy and Service Endpoint Associations | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.6.5: On-Premises Reverse-Proxy WAF Deployment | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-2.6.6: Bot Management and Request Rate Limiting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| NE-2.6.7: API Protection Policy and Schema Validation | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-2.6.8: API Gateway Runtime Policy Enforcement | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |

### NE-2.7: Secure Remote Access

**Selected Tool / Product / Service:** Pomerium Enterprise, Azure Virtual Desktop, CyberArk Privileged Access Manager

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.4, ID-1.3

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C22](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.7.1: Private Remote Access | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-2.7.2: JIT Network Port Access | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-2.7.3: Remote Access Key Management | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.7.4: Virtual Desktop Isolation | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Extensive; Recurring: High | Medium-term (3–6 months) |
| NE-2.7.5: Browser Based Access | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.7.6: Virtual Desktop Monitoring and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.7.7: Split Tunneling Prevention | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.7.8: Remote Session Disconnect Capability | 2 | Technical | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-2.7.9: Idle Network Connection Termination | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### NE-2.8: Telemetry, Tracking, and Command (TT&C) Link Security

**Selected Tool / Product / Service:** the datalink crypto modules, Entrust nShield 5 HSMs

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Fleet Operations

**Dependencies:** NE-1.4, ID-1.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-06-30

**Contracting / Procurement Reference:** [C26](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.8.1: Command Uplink Authentication and Encryption (CCSDS SDLS) | 3 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Long-term (6+ months) |
| NE-2.8.2: Telemetry Downlink Authentication and Integrity Protection (CCSDS SDLS) | 3 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Long-term (6+ months) |
| NE-2.8.3: Link-Anomaly and Jamming-Indicator Monitoring and Alerting | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### NE-2.10: Cross Domain Solution (CDS) Transfer Procedures

**Selected Tool / Product / Service:** the cross domain service provider's enterprise CDS, Splunk Enterprise

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Platform Team

**Dependencies:** the enterprise CDS interconnection agreement, AP-4

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-06-30

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.10.1: CDS Product Selection and Baseline List Compliance | 3 | Process | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Long-term (6+ months) |
| NE-2.10.2: CDS Transfer Request and Approval Workflow | 3 | Process | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| NE-2.10.3: Policy-Based Automated Transfer Release | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-2.10.4: Content Inspection/Filtering Prior to Transfer | 3 | Technical | None | Level 2 | Continuous | High | One-Time: Extensive; Recurring: Moderate | Long-term (6+ months) |
| NE-2.10.5: Transfer Audit Logging and Review | 3 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| NE-2.10.6: CDS Accreditation and Periodic Reassessment | 3 | Process | None | Level 2 | Periodic (Annual) | High | One-Time: High; Recurring: Moderate | Long-term (6+ months) |
| NE-2.10.7: Manual Cross-Domain Media Transfer | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### NE-2.11: Industrial Protocol Filtering (DPI)

**Selected Tool / Product / Service:** Palo Alto Networks PA-Series, Nozomi Networks Guardian

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Fleet Operations

**Dependencies:** NE-1.4, ID-1.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-06-30

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C13](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.11.1: Protocol-Aware DPI Deployment | 3 | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Moderate | Long-term (6+ months) |
| NE-2.11.2: Allowed Function Code/Command Allow-Listing | 3 | Documentation | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-2.11.3: Unauthorized Command Blocking and Alerting | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.11.4: DPI Rule Tuning and False-Positive Management | 3 | Process | None | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |

### NE-2.12: Ports, Protocols, and Services Matrix (PPSM)

**Selected Tool / Product / Service:** the DoD PPSM registry, Panorama with the Terraform PAN-OS provider

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Security Team

**Dependencies:** NE-1.4, ID-1.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-2.12.1: PPSM Registration and CAL (category assurance list) Alignment | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| NE-2.12.2: PPS Baseline Documentation and Approval | 2 | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.12.3: Boundary Enforcement Validation Against PPSM | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-2.12.4: PPSM Periodic Review and Recertification | 2 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### NE-2.13: Authorized Cloud Access Point Integration

**Selected Tool / Product / Service:** the DISA Boundary Cloud Access Point, Mission Landing Zone (Terraform) on Azure Government, Palo Alto Networks VM-Series

**Environment-Specific Tailoring:** VM-Series firewalls form the cloud hub. PA-Series pairs form the data center hub and the alternate site firewall, all under one Panorama rule base deployed by Terraform.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.4, ID-1.3

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

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

**Environment-Specific Tailoring:** Azure VNet flow logs cover the cloud, and Corelight sensors on ACI span ports cover the data center.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.4, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C14](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.1.1: Centralized Network Telemetry and Analytics Platform | 2 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-3.1.2: Network Security Posture Dashboard | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### NE-3.2: IDPS

**Selected Tool / Product / Service:** Palo Alto Advanced Threat Prevention, Corelight sensors

**Environment-Specific Tailoring:** Azure VNet flow logs cover the cloud, and Corelight sensors on ACI span ports cover the data center.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.4, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C14](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.2.1: Cloud-Native Firewall Advanced Threat Protection Deployment | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| NE-3.2.2: On-Premises IDPS Sensor Deployment | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| NE-3.2.3: IDPS Signature Rules Selection | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-3.2.4: IDPS Mode Configuration | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-3.2.5: Signature Fine-Tuning | 2 | Process | None | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |

### NE-3.3: Trusted DNS Service

**Selected Tool / Product / Service:** Infoblox NIOS, Azure DNS

**Environment-Specific Tailoring:** Azure VNet flow logs cover the cloud, and Corelight sensors on ACI span ports cover the data center.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.4, DE-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

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

**Selected Tool / Product / Service:** Infoblox NIOS, Azure DNS

**Environment-Specific Tailoring:** Azure VNet flow logs cover the cloud, and Corelight sensors on ACI span ports cover the data center.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.4, DE-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C12](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.4.1: Managed Private DNS for Private Resolution | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| NE-3.4.2: Managed Private DNS for Private Endpoints | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| NE-3.4.3: Custom DNS for Restricted Resolution | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |

**Pinned:** NE-3.4.1: KESTREL's design depends on it from the first build, since private endpoints do not resolve without it. NE-3.4.2: KESTREL's design depends on it from the first build, since private endpoints do not resolve without it.

### NE-3.5: DNS Advanced Protection

**Selected Tool / Product / Service:** Infoblox Threat Defense, Splunk Enterprise

**Environment-Specific Tailoring:** Azure VNet flow logs cover the cloud, and Corelight sensors on ACI span ports cover the data center.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.4, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C12](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.5.1: Managed DNS Threat Protection | 2 | Technical | Automate | Level 1 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| NE-3.5.2: Malicious DNS Activity Monitoring | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-3.5.3: Dangling DNS Records Detection | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### NE-3.7: External Attack Surface Management

**Selected Tool / Product / Service:** Tenable Attack Surface Management, GitGuardian public monitoring

**Environment-Specific Tailoring:** Azure VNet flow logs cover the cloud, and Corelight sensors on ACI span ports cover the data center.

**Accountable Team:** Security Team

**Dependencies:** NE-2.4, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C29](index.md#6-contracting-and-procurement-cross-references)

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

**Environment-Specific Tailoring:** Azure VNet flow logs cover the cloud, and Corelight sensors on ACI span ports cover the data center.

**Accountable Team:** Fleet Operations

**Dependencies:** NE-2.4, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-06-30

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

**Environment-Specific Tailoring:** Azure VNet flow logs cover the cloud, and Corelight sensors on ACI span ports cover the data center.

**Accountable Team:** Fleet Operations

**Dependencies:** NE-2.4, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-06-30

**Contracting / Procurement Reference:** [C26](index.md#6-contracting-and-procurement-cross-references), [C20](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| NE-3.9.1: PNT Signal Profiling and Spoofing/Jamming Indicator Detection | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| NE-3.9.2: Cross-Source PNT Consistency Validation | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| NE-3.9.3: Spoofing/Jamming Alerting and Operator Notification | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
