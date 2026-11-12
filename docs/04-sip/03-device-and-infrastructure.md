# DI: Device and Infrastructure

*KESTREL Security Implementation Plan, Section 4 (Protect). Each record implements the outcome of the same ID in the [SADD](../03-sadd/03-device-and-infrastructure.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## DI-1: Asset Management

### DI-1.1: Asset Inventory and Discovery

**Selected Tool / Product / Service:** Jira Service Management Assets, Azure Resource Graph, Microsoft Defender for Cloud, Cisco ACI and APIC, Microsoft Configuration Manager

**Environment-Specific Tailoring:** Azure Resource Graph feeds every cloud spoke. Defender for Endpoint device inventory feeds every on-premises server and workstation, and the Cisco APIC adds the data center's network devices. The alternate site has no SDN fabric, and the fleet joins through DI-1.2's passive sensors. License tracking covers every licensed product and foundation model's terms.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-1.1.1: Asset Inventory Record | 1 | Technical | None | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-1.1.2: Asset Discovery | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-1.1.3: Unsanctioned Cloud Account and Landing-Zone Bypass Detection | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-1.1.4: Asset Inventory Dashboard | 2 | Technical | Visualize | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-1.1.5: Software License and Usage Restriction Tracking | 1 | Process | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### DI-1.2: OT/Legacy Passive Protocol-Aware Discovery

**Selected Tool / Product / Service:** Nozomi Networks Guardian, Jira Service Management Assets

**Environment-Specific Tailoring:** Guardian sensors are deployed and tuned on the spare stations and the simulator in Phase 2. They extend to each operating site when the fleet integrates. Aircraft are inventoried by tail number from Fleet Operations' records and reconciled when one connects to a station.

**Accountable Team:** Fleet Operations

**Dependencies:** DI-1.1, NE-1.6

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C13](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-1.2.1: Passive Sensor/Tap Deployment | 2 (pinned) | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |
| DI-1.2.2: Industrial Protocol-Aware Asset Fingerprinting | 2 (pinned) | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DI-1.2.3: Passive Discovery-to-Inventory Reconciliation | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-1.2.4: Discovery Coverage Validation Across OT Segments/Conduits | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DI-1.2.1 and DI-1.2.2: Sensors are deployed and tuned on the spare stations and the simulator in Phase 2, so they are proven before the SCA assessment.

### DI-1.3: Resource Tagging and Ownership Strategy

**Selected Tool / Product / Service:** Jira Service Management Assets, Azure Policy, Open Policy Agent (Gatekeeper and Conftest)

**Environment-Specific Tailoring:** Tags are required from the first build. Azure Policy and the pipeline's Conftest checks audit them in Phase 1 and block untagged cloud resources in Phase 2. On-premises servers are tagged when built, and Fleet Operations tags fleet equipment when it is received.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-1.3.1: Resource Organization | 1 (pinned) | Documentation | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-1.3.2: Tagging Framework | 1 (pinned) | Documentation | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-1.3.3: Tagging Enforcement | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Long-term (6+ months) |

**Pinned:** DI-1.3.1 and DI-1.3.2: Built in when the platform is created, since retrofitting it later costs far more. Resources created untagged must be found and tagged by hand.

### DI-1.4: Security Team Visibility

**Selected Tool / Product / Service:** Jira Service Management Assets, Splunk Enterprise Security

**Environment-Specific Tailoring:** The Security Team and the CSSP's analysts read the inventory in Jira Service Management Assets without the right to change it. A lookup in Splunk Enterprise Security adds each asset's owner, team, and criticality to every alert, for every location the inventory covers.

**Accountable Team:** Platform Team, with the Security Team

**Dependencies:** DI-1.1, DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-1.4.1: Security Organization Permissions | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-1.4.2: Operational Security Integration | 2 | Process | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

## DI-2: Asset Lifecycle

### DI-2.1: Secure Resource Provisioning

**Selected Tool / Product / Service:** OpenTofu, the Platform Team's landing zone modules derived from Mission Landing Zone, Azure Policy, GitLab Ultimate, Ansible Automation Platform

**Environment-Specific Tailoring:** Cloud resources come from the landing zone modules through OpenTofu in GitLab, and Azure Policy denies console creation outside break-glass. Data center and alternate site servers come from Ansible Automation Platform playbooks, with the alternate site's equipment placed under the facility agreement.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.1, DI-3.1, AP-2.21, AP-2.22, GV-5.6

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-2.1.1: Secure-By-Default Provisioning | 1 (pinned) | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-2.1.2: Provisioning Approval Workflows | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DI-2.1.1 and DI-2.1.2: Built in when the platform is created, since retrofitting it later costs far more. Every resource built before it would need rework.

### DI-2.2: Asset Lifecycle Change Control

**Selected Tool / Product / Service:** GitLab Ultimate, Jira Service Management Data Center, CyberArk Privileged Access Manager, CyberArk Privileged Session Manager

**Environment-Specific Tailoring:** A merged GitLab merge request is the change record for anything defined as code, and Jira Service Management holds the rest, including fleet changes. Emergency changes run through CyberArk and get a retrospective review within two business days. Changes to the shared rule base, the identity provider, or an interconnection go to the Configuration Control Board.

**Accountable Team:** Platform Team

**Dependencies:** DI-2.1, GV-1.5, ID-4.4

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-2.2.1: Change Approval Workflow | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-2.2.2: Change Risk Assessment | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-2.2.3: Pre-Implementation Change Testing and Validation | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DI-2.2.4: Post-Change Configuration Validation | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-2.2.5: Emergency Change Process | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-2.3: Resource Decommissioning Governance

**Selected Tool / Product / Service:** OpenTofu, Jira Service Management Data Center, Blancco Drive Eraser, Entrust nShield 5 HSMs, the aircraft and ground equipment manufacturer's tools, the payload vendors' software and SBOMs

**Environment-Specific Tailoring:** Cloud resources are destroyed by the OpenTofu that created them, which revokes their workload identities and deletes their vault secrets and keys. Data center and alternate site drives are wiped with Blancco on site, and HSMs are zeroized. Payload Vendor A fields the replacement payload processing workstation by 2027-09-30, when CCSD tailoring action 3 expires, so the legacy workstation retires before the fleet integrates. If it slips, the PMO ISSE asks the AO to re-date action 3.

**Accountable Team:** Platform Team, with Fleet Operations for the fleet

**Dependencies:** DI-1.1, ID-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations, with the fleet slice as RDT&E fleet integration

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C30](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references), [C27](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-2.3.1: Secure Decommissioning Procedures | 2 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DI-2.3.2: Orphaned Resource Detection | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-2.3.3: End-of-Life and End-of-Support Refresh Planning | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

**Pinned:** DI-2.3.1: Nothing is retired from KESTREL during the first build.

### DI-2.4: Controlled Maintenance and Support

**Selected Tool / Product / Service:** Jira Service Management Data Center, CyberArk Privileged Access Manager, CyberArk Privileged Session Manager, the aircraft and ground equipment manufacturer's tools

**Environment-Specific Tailoring:** Data center and alternate site hardware maintenance is scheduled in Jira Service Management, escorted, and recorded, and failed drives stay on site. The Phase 1 procedures cover the fleet too. Its maintenance then runs only in ID-4.5's weekly windows, which arrive with the fleet in Phase 3. The cloud provider maintains the cloud hardware.

**Accountable Team:** Platform Team, with Fleet Operations for the fleet

**Dependencies:** DI-1.1, ID-4.4, ID-4.7

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-2.4.1: Maintenance Procedures Documentation | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-2.4.2: Controlled Maintenance Scheduling, Approval, and Records | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DI-2.4.3: Support Agreements and Spare Parts | 1 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DI-2.4.4: Maintenance Tool Approval and Control | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## DI-3: Baseline Configuration Standards

### DI-3.1: Secure Configurations

**Selected Tool / Product / Service:** the Platform Team's landing zone modules derived from Mission Landing Zone, OpenTofu, Azure Policy, Ansible Automation Platform, DISA SCAP Compliance Checker and STIG Viewer

**Environment-Specific Tailoring:** DISA STIGs and SRGs set every baseline, with the Cloud Computing SRG's IL5 requirements in the cloud. The landing zone modules build the hub and ten spokes as subscriptions guarded by Azure Policy. Ansible roles carry the STIGs to the data center and alternate site.

**Accountable Team:** Platform Team

**Dependencies:** None. The landing zone is built first, alongside identity.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), plus government-furnished and open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-3.1.1: Architecture Frameworks | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-3.1.2: Configuration Frameworks | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-3.1.3: Cloud Landing Zones | 1 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-3.1.4: Infrastructure-as-Code (IaC) Templates | 1 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-3.1.5: Fail-Secure State Definition | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DI-3.1.5: Built in when the platform is created, since retrofitting it later costs far more. Both hubs fail closed from their first rule base.

### DI-3.2: Secure Compute Baselines

**Selected Tool / Product / Service:** Packer, Iron Bank hardened images from Platform One, Azure Kubernetes Service, kube-bench, Azure Virtual Desktop, Ansible Automation Platform

**Environment-Specific Tailoring:** Packer builds the cloud's VDI and server images and the data center's from the same STIG roles. The IT/OT DMZ's staging servers use the data center server image. Container base images come from Iron Bank, every AKS cluster shares one baseline checked by kube-bench, and Ansible hardens the physical servers' BMCs.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), plus government-furnished, open source, and source-available components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-3.2.1: Virtual Desktop Golden Image | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-3.2.2: Virtual Machine Golden Images | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-3.2.3: Container Golden Images | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-3.2.4: Container Orchestration Secure Baselines | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-3.2.5: Baseboard Management Controller (BMC) Hardening | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-3.3: Secure Storage Baselines

**Selected Tool / Product / Service:** Azure Policy, Azure SQL Database, NetApp StorageGRID with S3 Object Lock, Ansible Automation Platform, DISA SCAP Compliance Checker and STIG Viewer

**Environment-Specific Tailoring:** Azure Policy denies public access and requires private endpoints on every cloud storage and database service. On premises, each data lake zone's StorageGRID bucket policy admits only its own team's workloads, the Data Team, and the ML training zone where F18 allows. Ansible applies the database STIGs to the data center's databases.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-3.3.1: Cloud Storage Secure Baselines | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-3.3.2: Cloud Database Secure Baselines | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-3.3.3: On-Premises Storage Secure Baselines | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-3.3.4: On-Premises Database Secure Baselines | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-3.4: Secure Platform Services and Application Baselines

**Selected Tool / Product / Service:** Azure Policy, Defender for Cloud CSPM, Azure OpenAI Service

**Environment-Specific Tailoring:** Azure Policy initiatives set the baseline for every managed service, including a private endpoint and no local key authentication on each Azure OpenAI deployment. Turning off the provider's abuse monitoring is an exemption Microsoft approves, not a setting, so the approval is filed as evidence and confirmed each year. COTS products follow their vendors' guidance.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-3.4.1: Cloud Platform Services Secure Baselines | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-3.4.2: Secure Application Baselines | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### DI-3.5: Secure OT/Legacy Device Baselines

**Selected Tool / Product / Service:** the aircraft and ground equipment manufacturer's tools, Jira Service Management Assets, Palo Alto Networks PA-Series

**Environment-Specific Tailoring:** Fleet Operations adopts each manufacturer's hardening guidance and records approved firmware, proving both on the spare stations and the simulator. The fleet is built to them when it integrates, and DI-4.7 checks it against them. The compensating control baseline is the pattern for any asset that cannot be patched. It applies to the payload processing workstation only if its replacement slips.

**Accountable Team:** Fleet Operations

**Dependencies:** DI-1.2, NE-1.6

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C26](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-3.5.1: OT/ICS Vendor Hardening Guide Adoption | 2 (pinned) | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-3.5.2: Compensating Control Baseline Definition | 2 (pinned) | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-3.5.3: Firmware Version and Patch-Level Baseline Tracking | 2 (pinned) | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DI-3.5.1, DI-3.5.2, and DI-3.5.3: Fleet baselines are written and tried on the spare stations and the simulator in Phase 2, before the fleet integrates.

## DI-4: Configuration Policy Orchestration

### DI-4.2: Policy Service Restrictions

**Selected Tool / Product / Service:** Windows Defender Firewall, firewalld on Red Hat Enterprise Linux, Microsoft Configuration Manager, Ansible Automation Platform, Panorama with the PAN-OS provider for OpenTofu

**Environment-Specific Tailoring:** The CMP sets the permitted services, ports, and protocols for each asset type. Windows Defender Firewall through Configuration Manager and firewalld through Ansible enforce them on every host, and the shared Panorama rule base enforces them on the network. Fleet equipment follows its manufacturer's service list.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1, DI-3.2, DI-6.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.2.1: Service Restriction Policy Framework | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-4.2.2: Policy Scope and Enforcement | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.3: Unapproved Service Usage Monitoring and Alerting

**Selected Tool / Product / Service:** Tenable Security Center (ACAS), Defender for Cloud CSPM, Splunk Enterprise Security, Jira Service Management Data Center

**Environment-Specific Tailoring:** ACAS scans and Defender for Cloud CSPM look for services outside the CMP's list in every location. Findings alert in Splunk Enterprise Security and open a Jira Service Management ticket to the owning team. A DMZ or Tier 0 finding goes to the Security Team at once.

**Accountable Team:** Platform Team

**Dependencies:** DI-4.2, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.3.1: Unapproved Service Detection | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-4.3.2: Alert and Response Workflows | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.4: Compute Configuration Monitoring

**Selected Tool / Product / Service:** Tenable Security Center (ACAS), DISA SCAP Compliance Checker and STIG Viewer, Azure Machine Configuration, Defender for Cloud CSPM, Open Policy Agent (Gatekeeper and Conftest), Splunk Enterprise

**Environment-Specific Tailoring:** Azure Machine Configuration and Defender for Cloud CSPM check cloud machines, and ACAS STIG audits check data center and alternate site hosts. Gatekeeper rejects workloads that depart from the cluster baseline. A Splunk dashboard shows posture by team and spoke for the Platform Team, the Security Team, and the CSSP.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.2, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), plus government-furnished and open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.4.1: Compute Baseline Drift Detection and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.4.2: Compute Configuration Compliance Dashboard/Reporting | 2 | Technical | Visualize | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.5: Storage Configuration Monitoring

**Selected Tool / Product / Service:** Defender for Cloud CSPM, Azure Policy, Ansible Automation Platform, Splunk Enterprise

**Environment-Specific Tailoring:** Defender for Cloud CSPM and Azure Policy compliance watch every cloud storage and database service. An Ansible job compares each StorageGRID zone's bucket policy with its baseline, so access that crosses the vendor split is caught. Findings feed a Splunk storage dashboard.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.3, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.5.1: Storage Baseline Drift Detection and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DI-4.5.2: Storage Configuration Compliance Dashboard/Reporting | 2 | Technical | Visualize | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.6: Platform Services and Application Configuration Monitoring

**Selected Tool / Product / Service:** Defender for Cloud CSPM, Azure Policy, Splunk Enterprise

**Environment-Specific Tailoring:** Defender for Cloud CSPM and Azure Policy compliance watch every managed service, with a re-enabled public endpoint as the highest-priority finding. Findings appear on a Splunk platform and application dashboard. These checks cannot read the abuse monitoring exemption, so it is confirmed each year instead.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.4, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.6.1: Platform/Application Baseline Drift Detection and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.6.2: Platform/Application Configuration Compliance Dashboard/Reporting | 2 | Technical | Visualize | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.7: OT Baseline Configuration Drift Detection

**Selected Tool / Product / Service:** Nozomi Networks Guardian, the aircraft and ground equipment manufacturer's tools, Splunk Enterprise

**Environment-Specific Tailoring:** Guardian captures each station's and launch system's configuration from its traffic, and Fleet Operations exports what the manufacturer's tools allow during maintenance windows. Drift alerts reach Fleet Operations and the Security Team through Splunk, and nothing changes fleet equipment automatically.

**Accountable Team:** Fleet Operations, with the Security Team

**Dependencies:** DI-1.2, DI-3.5

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C13](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.7.1: Passive Configuration State Capture | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.7.2: Drift Alerting and Operator Notification | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.8: Vulnerability and Patch Management

**Selected Tool / Product / Service:** Tenable Security Center (ACAS), Microsoft Configuration Manager, Ansible Automation Platform, Jira Service Management Data Center, the aircraft and ground equipment manufacturer's tools

**Environment-Specific Tailoring:** ACAS scans every host from Phase 1, so Tier 0 runs under the VPMP's deadlines from the interim authorization to test. Configuration Manager and Ansible patch servers in every location, one node of each on-premises pair at a time. Container images are rebuilt rather than patched. Fleet patches start in Phase 3, validated by the manufacturer, tried on a spare, and loaded in a maintenance window.

**Accountable Team:** IT Operations, with the Platform Team and Fleet Operations

**Dependencies:** DI-3.2, DI-7.1, DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations, with the fleet slice as RDT&E fleet integration

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.8.1: Patch/Vulnerability Remediation SLA Policy | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-4.8.2: Risk-Based Prioritization Criteria | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-4.8.3: Patch Testing, Staged Rollout, and Rollback | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.8.4: Patching and Updates | 1 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DI-4.8.5: OT/ICS Vendor-Validated Patch Remediation | 3 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DI-4.8.6: Patch Compliance Tracking and Reporting | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.8.7: Exception and Risk Acceptance Workflow | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-4.8.8: IAVM/Security Directive Intake and Compliance Tracking | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

**Pinned:** DI-4.8.5: Fleet patching cannot start until the fleet integrates, inside the maintenance windows that arrive with it.

### DI-4.9: Unpatchable/Legacy Asset Compensating Controls

**Selected Tool / Product / Service:** Palo Alto Networks PA-Series, Palo Alto Threat Prevention with on-box signatures, Nozomi Networks Guardian, Splunk Enterprise Security, Trellix Application Control

**Environment-Specific Tailoring:** These controls are the pattern for any asset that cannot be patched. If none is fielded, they are validated on a spare station. If the payload processing workstation's replacement slips, the workstation connects only after the AO re-dates CCSD tailoring action 3. It then runs in its own OT zone segment with Threat Prevention at its single conduit. Trellix Application Control and tighter Guardian and Splunk thresholds complete the set.

**Accountable Team:** Fleet Operations, with the Platform Team and the Security Team

**Dependencies:** DI-3.5, NE-1.6, DE-2.8

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C13](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C32](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.9.1: Network Segmentation and Isolation Enforcement | 3 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.9.2: Virtual Patching | 3 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DI-4.9.3: Enhanced Monitoring for Unpatchable Assets | 3 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

## DI-5: Endpoint Security

### DI-5.1: Execution and Device Control

**Selected Tool / Product / Service:** App Control for Business, fapolicyd on Red Hat Enterprise Linux, Microsoft Configuration Manager, Microsoft Defender for Endpoint

**Environment-Specific Tailoring:** App Control for Business runs deny-by-default on the privileged access workstations, VDI desktops, and Windows servers. On Red Hat Enterprise Linux servers fapolicyd does the same, in every location including the IT/OT DMZ. Policies audit in Phase 2 and enforce by Phase 3, and fleet equipment follows DI-3.5 instead.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.2, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-5.1.1: Attack Surface Reduction | 2 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.1.2: Device Control | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.1.3: Application Control | 2 | Technical | None | Level 1 | Continuous | Extensive | One-Time: Moderate; Recurring: Moderate | Long-term (6+ months) |
| DI-5.1.4: Collaborative Computing Device Control | 2 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-5.2: Malicious Code Protection

**Selected Tool / Product / Service:** Defender for Servers, Azure Arc-enabled servers, Microsoft Defender for Endpoint, Defender for Containers

**Environment-Specific Tailoring:** Defender for Servers licenses Defender for Endpoint on every server, through Azure Arc for the data center, the alternate site, and the IT/OT DMZ. Microsoft 365 licensing covers it on the privileged access workstations and VDI desktops. Defender for Containers protects every AKS cluster, including the training cluster's GPU nodes.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.2, DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-5.2.1: Behavioral Anti-Malware | 1 (pinned) | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DI-5.2.2: Ransomware-Protected Folders | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.2.3: Network Protection | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.2.4: Web Protection | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.2.5: Container/Workload Runtime Protection (CWPP) | 2 | Technical | None | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

**Pinned:** DI-5.2.1: Required for the interim authorization to test, since Tier 0 is scanned and watched from the first build.

### DI-5.3: Host Hardening and Integrity Protection

**Selected Tool / Product / Service:** Microsoft Defender for Endpoint, Microsoft Configuration Manager, Ansible Automation Platform, Windows Defender Firewall, firewalld on Red Hat Enterprise Linux

**Environment-Specific Tailoring:** Configuration Manager and Ansible apply exploit protection and default-deny host firewalls to every privileged access workstation, VDI desktop, and server. The Security Team owns tamper protection in Defender for Endpoint, so no Platform Team administrator can switch off the agent that watches them.

**Accountable Team:** Platform Team, with the Security Team for the tamper protection policy

**Dependencies:** DI-3.2, DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-5.3.1: Exploit Protection | 2 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.3.2: Tamper Protection | 1 (pinned) | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.3.3: Host Firewalls | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| DI-5.3.4: Security Function Isolation | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DI-5.3.2: Required for the interim authorization to test, since Tier 0 is scanned and watched from the first build.

### DI-5.4: Endpoint Detection

**Selected Tool / Product / Service:** Microsoft Defender for Endpoint, Defender for Servers, Azure Arc-enabled servers, Tenable Security Center (ACAS), Azure Trusted Launch, Cisco ACI and APIC, Splunk Enterprise Security

**Environment-Specific Tailoring:** Defender for Endpoint is in every image from Phase 1, in audit mode until blocking is turned on in Phase 2. Hosts running payload vendor software stay in audit mode until that software is profiled. File integrity monitoring covers Tier 0 from Phase 1, cloud virtual machines use Trusted Launch from creation, and the Cisco APIC reports unknown data center devices.

**Accountable Team:** Platform Team, with the Security Team for threat hunting and custom indicators

**Dependencies:** DI-3.2, DE-3.1

**Funding Line:** FY27, FY28, and FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 1, Foundation, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-5.4.1: Vulnerability Scanning | 1 (pinned) | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DI-5.4.2: Endpoint File Integrity Monitoring (FIM) | 1 (pinned) | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.4.3: Advanced Threat Hunting | 4 | Process | None | Level 3 | Periodic (Event-Driven) | High | One-Time: Low; Recurring: High | Medium-term (3–6 months) |
| DI-5.4.4: Custom File Indicators | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.4.5: Custom Network Indicators | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.4.6: EDR Blocking/Enforcement Mode | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| DI-5.4.7: EDR Passive/Audit Mode | 1 (pinned) | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.4.8: EDR Sensor Deployment | 1 (pinned) | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DI-5.4.9: Unmanaged/Rogue Device Discovery | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.4.10: Boot Integrity and Device Health Attestation | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

**Pinned:** DI-5.4.1, DI-5.4.2, DI-5.4.7, and DI-5.4.8: Required for the interim authorization to test, since Tier 0 is scanned and watched from the first build. DI-5.4.10: Built in when the platform is created, since retrofitting it later costs far more. Trusted Launch is set when a virtual machine is created, and Phase 1 creates the first ones.

### DI-5.5: Endpoint Response

**Selected Tool / Product / Service:** Microsoft Defender XDR, Splunk SOAR, Splunk SOAR containment playbooks under the CSSP agreement

**Environment-Specific Tailoring:** The Security Team takes every response action in Defender XDR under the IRP, and live response sessions are recorded. The CSSP isolates a host only through a pre-approved Splunk SOAR playbook, which pages the Security Team. Automated isolation is limited to non-production hosts, and fleet equipment is never isolated this way.

**Accountable Team:** Security Team

**Dependencies:** DI-5.4, RS-1.1, RS-1.7

**Funding Line:** FY28 and FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C31](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-5.5.1: Extended Detection and Response (XDR) | 2 | Technical | None | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DI-5.5.2: Automated Investigation and Response | 4 | Technical | Automate | Level 3 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DI-5.5.3: Device Response | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.5.4: Device Isolation | 2 | Technical | Automate | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.5.5: File Response | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.5.6: Live Response | 4 | Technical | None | Level 3 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## DI-6: Configuration Management Planning

### DI-6.1: Configuration Management Plan (CMP)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** One CMP covers the cloud, the data center, the alternate site, and the fleet. Fleet Operations writes its OT and legacy sections and IT Operations its maintenance sections, and the Configuration Control Board approves it.

**Accountable Team:** Platform Team

**Dependencies:** The SADD's Device and Infrastructure design decisions, GV-1.5

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-6.1.1: CMP Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DI-6.1.2: CMP Review and Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-6.1.3: CMP Periodic Review and Revision | 2 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DI-6.1.3: Its first review cannot fall in Phase 1, since the document it reviews is approved there.

## DI-7: Vulnerability and Patch Management Planning

### DI-7.1: Vulnerability and Patch Management Plan (VPMP)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** One VPMP covers every location, with IT Operations writing the patch windows and Fleet Operations the fleet procedures. It is written in Phase 1, so Tier 0 runs under its deadlines from the interim authorization to test. It is revised whenever CCSD tailoring action 3 changes.

**Accountable Team:** Security Team

**Dependencies:** The SADD's vulnerability and patch management design decisions, GV-1.5

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-7.1.1: VPMP Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DI-7.1.2: VPMP Review and Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-7.1.3: VPMP Periodic Review and Revision | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
