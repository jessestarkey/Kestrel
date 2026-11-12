# DI: Device and Infrastructure

*KESTREL Security Implementation Plan, Section 4 (Protect). Each record implements the outcome of the same ID in the [SADD](../03-sadd/03-device-and-infrastructure.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## DI-1: Asset Management

### DI-1.1: Asset Inventory and Discovery

**Selected Tool / Product / Service:** Jira Service Management Assets, Azure Resource Graph, Microsoft Defender for Cloud

**Environment-Specific Tailoring:** Azure Resource Graph feeds cloud assets, the Cisco APIC and agents feed the data center and alternate site, and Fleet Operations' records feed the fleet.

**Accountable Team:** Platform Team

**Dependencies:** None. The inventory is a Phase 1 prerequisite for everything that reads it.

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

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

**Environment-Specific Tailoring:** Azure Resource Graph feeds cloud assets, the Cisco APIC and agents feed the data center and alternate site, and Fleet Operations' records feed the fleet.

**Accountable Team:** Fleet Operations

**Dependencies:** None. The inventory is a Phase 1 prerequisite for everything that reads it.

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-06-30

**Contracting / Procurement Reference:** [C13](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-1.2.1: Passive Sensor/Tap Deployment | 3 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |
| DI-1.2.2: Industrial Protocol-Aware Asset Fingerprinting | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DI-1.2.3: Passive Discovery-to-Inventory Reconciliation | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-1.2.4: Discovery Coverage Validation Across OT Segments/Conduits | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-1.3: Resource Tagging and Ownership Strategy

**Selected Tool / Product / Service:** Jira Service Management Assets, Azure Resource Graph, Microsoft Defender for Cloud

**Environment-Specific Tailoring:** Azure Resource Graph feeds cloud assets, the Cisco APIC and agents feed the data center and alternate site, and Fleet Operations' records feed the fleet.

**Accountable Team:** Platform Team

**Dependencies:** None. The inventory is a Phase 1 prerequisite for everything that reads it.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-1.3.1: Resource Organization | 1 (pinned) | Documentation | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-1.3.2: Tagging Framework | 1 (pinned) | Documentation | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-1.3.3: Tagging Enforcement | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Long-term (6+ months) |

**Pinned:** DI-1.3.1: Built in when the platform is created, since retrofitting it later costs far more. Resources created untagged must be found and tagged by hand. DI-1.3.2: Built in when the platform is created, since retrofitting it later costs far more. Resources created untagged must be found and tagged by hand. DI-1.3.3: Built in when the platform is created, since retrofitting it later costs far more. Resources created untagged must be found and tagged by hand.

### DI-1.4: Security Team Visibility

**Selected Tool / Product / Service:** Jira Service Management Assets, Splunk Enterprise Security

**Environment-Specific Tailoring:** Azure Resource Graph feeds cloud assets, the Cisco APIC and agents feed the data center and alternate site, and Fleet Operations' records feed the fleet.

**Accountable Team:** Platform Team

**Dependencies:** None. The inventory is a Phase 1 prerequisite for everything that reads it.

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-1.4.1: Security Organization Permissions | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-1.4.2: Operational Security Integration | 2 | Process | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

## DI-2: Asset Lifecycle

### DI-2.1: Secure Resource Provisioning

**Selected Tool / Product / Service:** Terraform, Mission Landing Zone (Terraform) on Azure Government, Azure Policy, GitLab Ultimate, Jira Service Management Data Center, Ansible Automation Platform

**Environment-Specific Tailoring:** Cloud resources come from Terraform through GitLab. Data center and alternate site servers come from Ansible Automation Platform playbooks, and fleet changes follow Fleet Operations' maintenance windows.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.1, AP-2 pipeline foundation

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-2.1.1: Secure-By-Default Provisioning | 1 (pinned) | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-2.1.2: Provisioning Approval Workflows | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DI-2.1.1: Built in when the platform is created, since retrofitting it later costs far more. Every resource built before it would need rework. DI-2.1.2: Built in when the platform is created, since retrofitting it later costs far more. Every resource built before it would need rework.

### DI-2.2: Asset Lifecycle Change Control

**Selected Tool / Product / Service:** Terraform, Mission Landing Zone (Terraform) on Azure Government, Azure Policy, GitLab Ultimate, Jira Service Management Data Center, Ansible Automation Platform

**Environment-Specific Tailoring:** Cloud resources come from Terraform through GitLab. Data center and alternate site servers come from Ansible Automation Platform playbooks, and fleet changes follow Fleet Operations' maintenance windows.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.1, AP-2 pipeline foundation

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), plus open source components

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

**Selected Tool / Product / Service:** Terraform, Jira Service Management Data Center, Blancco Drive Eraser

**Environment-Specific Tailoring:** Cloud resources come from Terraform through GitLab. Data center and alternate site servers come from Ansible Automation Platform playbooks, and fleet changes follow Fleet Operations' maintenance windows.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.1, AP-2 pipeline foundation

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C30](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-2.3.1: Secure Decommissioning Procedures | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DI-2.3.2: Orphaned Resource Detection | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-2.3.3: End-of-Life and End-of-Support Refresh Planning | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### DI-2.4: Controlled Maintenance and Support

**Selected Tool / Product / Service:** Jira Service Management Data Center, CyberArk Privileged Access Manager, CyberArk Privileged Session Manager

**Environment-Specific Tailoring:** Cloud resources come from Terraform through GitLab. Data center and alternate site servers come from Ansible Automation Platform playbooks, and fleet changes follow Fleet Operations' maintenance windows.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.1, AP-2 pipeline foundation

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

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

**Selected Tool / Product / Service:** Mission Landing Zone (Terraform) on Azure Government, Azure Policy, Packer, Azure VM Image Builder, Iron Bank hardened images from Platform One, DISA SCAP Compliance Checker and STIG Viewer

**Environment-Specific Tailoring:** DISA STIGs set every baseline. Cloud baselines are Azure Policy initiatives, and data center baselines are Ansible roles.

**Accountable Team:** Platform Team

**Dependencies:** DI-2.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), plus government-furnished and open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-3.1.1: Architecture Frameworks | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-3.1.2: Configuration Frameworks | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-3.1.3: Cloud Landing Zones | 1 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-3.1.4: Infrastructure-as-Code (IaC) Templates | 1 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-3.1.5: Fail-Secure State Definition | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DI-3.2: Secure Compute Baselines

**Selected Tool / Product / Service:** Azure VM Image Builder, Packer, Iron Bank hardened images from Platform One, Azure Kubernetes Service, kube-bench, Azure Virtual Desktop

**Environment-Specific Tailoring:** DISA STIGs set every baseline. Cloud baselines are Azure Policy initiatives, and data center baselines are Ansible roles.

**Accountable Team:** Platform Team

**Dependencies:** DI-2.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), plus government-furnished and open source components

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

**Selected Tool / Product / Service:** Azure Policy, NetApp StorageGRID with S3 Object Lock, Azure SQL Database

**Environment-Specific Tailoring:** DISA STIGs set every baseline. Cloud baselines are Azure Policy initiatives, and data center baselines are Ansible roles.

**Accountable Team:** Platform Team

**Dependencies:** DI-2.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references)

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

**Environment-Specific Tailoring:** DISA STIGs set every baseline. Cloud baselines are Azure Policy initiatives, and data center baselines are Ansible roles.

**Accountable Team:** Platform Team

**Dependencies:** DI-2.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-3.4.1: Cloud Platform Services Secure Baselines | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-3.4.2: Secure Application Baselines | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### DI-3.5: Secure OT/Legacy Device Baselines

**Selected Tool / Product / Service:** the aircraft and ground equipment manufacturer's tools, Palo Alto Networks PA-Series

**Environment-Specific Tailoring:** DISA STIGs set every baseline. Cloud baselines are Azure Policy initiatives, and data center baselines are Ansible roles.

**Accountable Team:** Fleet Operations

**Dependencies:** DI-2.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-06-30

**Contracting / Procurement Reference:** [C26](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-3.5.1: OT/ICS Vendor Hardening Guide Adoption | 3 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-3.5.2: Compensating Control Baseline Definition | 3 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-3.5.3: Firmware Version and Patch-Level Baseline Tracking | 3 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## DI-4: Configuration Policy Orchestration

### DI-4.2: Policy Service Restrictions

**Selected Tool / Product / Service:** Tenable Security Center (ACAS), Azure Machine Configuration, Defender for Cloud CSPM, Ansible Automation Platform, Azure Update Manager, Microsoft Configuration Manager

**Environment-Specific Tailoring:** Azure Update Manager and Machine Configuration cover the cloud. Configuration Manager and Ansible cover the data center and alternate site, and fleet patches follow the manufacturer.

**Accountable Team:** Platform Team

**Dependencies:** DI-3, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.2.1: Service Restriction Policy Framework | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-4.2.2: Policy Scope and Enforcement | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.3: Unapproved Service Usage Monitoring and Alerting

**Selected Tool / Product / Service:** Tenable Security Center (ACAS), Azure Machine Configuration, Defender for Cloud CSPM, Ansible Automation Platform, Azure Update Manager, Microsoft Configuration Manager

**Environment-Specific Tailoring:** Azure Update Manager and Machine Configuration cover the cloud. Configuration Manager and Ansible cover the data center and alternate site, and fleet patches follow the manufacturer.

**Accountable Team:** Platform Team

**Dependencies:** DI-3, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.3.1: Unapproved Service Detection | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-4.3.2: Alert and Response Workflows | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.4: Compute Configuration Monitoring

**Selected Tool / Product / Service:** Tenable Security Center (ACAS), Azure Machine Configuration, Defender for Cloud CSPM, Ansible Automation Platform, Azure Update Manager, Microsoft Configuration Manager

**Environment-Specific Tailoring:** Azure Update Manager and Machine Configuration cover the cloud. Configuration Manager and Ansible cover the data center and alternate site, and fleet patches follow the manufacturer.

**Accountable Team:** Platform Team

**Dependencies:** DI-3, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.4.1: Compute Baseline Drift Detection and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.4.2: Compute Configuration Compliance Dashboard/Reporting | 2 | Technical | Visualize | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.5: Storage Configuration Monitoring

**Selected Tool / Product / Service:** Tenable Security Center (ACAS), Azure Machine Configuration, Defender for Cloud CSPM, Ansible Automation Platform, Azure Update Manager, Microsoft Configuration Manager

**Environment-Specific Tailoring:** Azure Update Manager and Machine Configuration cover the cloud. Configuration Manager and Ansible cover the data center and alternate site, and fleet patches follow the manufacturer.

**Accountable Team:** Platform Team

**Dependencies:** DI-3, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.5.1: Storage Baseline Drift Detection and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DI-4.5.2: Storage Configuration Compliance Dashboard/Reporting | 2 | Technical | Visualize | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.6: Platform Services and Application Configuration Monitoring

**Selected Tool / Product / Service:** Tenable Security Center (ACAS), Azure Machine Configuration, Defender for Cloud CSPM, Ansible Automation Platform, Azure Update Manager, Microsoft Configuration Manager

**Environment-Specific Tailoring:** Azure Update Manager and Machine Configuration cover the cloud. Configuration Manager and Ansible cover the data center and alternate site, and fleet patches follow the manufacturer.

**Accountable Team:** Platform Team

**Dependencies:** DI-3, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.6.1: Platform/Application Baseline Drift Detection and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.6.2: Platform/Application Configuration Compliance Dashboard/Reporting | 2 | Technical | Visualize | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.7: OT Baseline Configuration Drift Detection

**Selected Tool / Product / Service:** Nozomi Networks Guardian

**Environment-Specific Tailoring:** Azure Update Manager and Machine Configuration cover the cloud. Configuration Manager and Ansible cover the data center and alternate site, and fleet patches follow the manufacturer.

**Accountable Team:** Fleet Operations

**Dependencies:** DI-3, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-06-30

**Contracting / Procurement Reference:** [C13](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.7.1: Passive Configuration State Capture | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.7.2: Drift Alerting and Operator Notification | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DI-4.8: Vulnerability and Patch Management

**Selected Tool / Product / Service:** Tenable Security Center (ACAS), Azure Machine Configuration, Defender for Cloud CSPM, Ansible Automation Platform, Azure Update Manager, Microsoft Configuration Manager

**Environment-Specific Tailoring:** Azure Update Manager and Machine Configuration cover the cloud. Configuration Manager and Ansible cover the data center and alternate site, and fleet patches follow the manufacturer.

**Accountable Team:** Platform Team

**Dependencies:** DI-3, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.8.1: Patch/Vulnerability Remediation SLA Policy | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-4.8.2: Risk-Based Prioritization Criteria | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-4.8.3: Patch Testing, Staged Rollout, and Rollback | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.8.4: Patching and Updates | 2 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DI-4.8.5: OT/ICS Vendor-Validated Patch Remediation | 2 | Process | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DI-4.8.6: Patch Compliance Tracking and Reporting | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.8.7: Exception and Risk Acceptance Workflow | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-4.8.8: IAVM/Security Directive Intake and Compliance Tracking | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### DI-4.9: Unpatchable/Legacy Asset Compensating Controls

**Selected Tool / Product / Service:** Palo Alto Networks PA-Series, Palo Alto Advanced Threat Prevention, Nozomi Networks Guardian

**Environment-Specific Tailoring:** Azure Update Manager and Machine Configuration cover the cloud. Configuration Manager and Ansible cover the data center and alternate site, and fleet patches follow the manufacturer.

**Accountable Team:** Fleet Operations, with the Platform Team

**Dependencies:** DI-3, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C13](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-4.9.1: Network Segmentation and Isolation Enforcement | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DI-4.9.2: Virtual Patching | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DI-4.9.3: Enhanced Monitoring for Unpatchable Assets | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

## DI-5: Endpoint Security

### DI-5.1: Execution and Device Control

**Selected Tool / Product / Service:** App Control for Business, fapolicyd on Red Hat Enterprise Linux, Microsoft Defender for Endpoint, Microsoft Configuration Manager

**Environment-Specific Tailoring:** Defender for Endpoint runs on Windows and Linux hosts in every location. Linux allow-listing uses fapolicyd, and fleet equipment is excluded.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.2, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

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

**Selected Tool / Product / Service:** Microsoft Defender for Endpoint, Defender for Containers, Defender for Servers

**Environment-Specific Tailoring:** Defender for Endpoint runs on Windows and Linux hosts in every location. Linux allow-listing uses fapolicyd, and fleet equipment is excluded.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.2, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-5.2.1: Behavioral Anti-Malware | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DI-5.2.2: Ransomware-Protected Folders | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.2.3: Network Protection | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.2.4: Web Protection | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.2.5: Container/Workload Runtime Protection (CWPP) | 2 | Technical | None | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

### DI-5.3: Host Hardening and Integrity Protection

**Selected Tool / Product / Service:** Microsoft Defender for Endpoint, Microsoft Configuration Manager, Ansible Automation Platform

**Environment-Specific Tailoring:** Defender for Endpoint runs on Windows and Linux hosts in every location. Linux allow-listing uses fapolicyd, and fleet equipment is excluded.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.2, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-5.3.1: Exploit Protection | 2 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.3.2: Tamper Protection | 2 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.3.3: Host Firewalls | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| DI-5.3.4: Security Function Isolation | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DI-5.4: Endpoint Detection

**Selected Tool / Product / Service:** Microsoft Defender for Endpoint, Defender for Servers, Tenable Security Center (ACAS), Azure Trusted Launch, Cisco ACI and APIC

**Environment-Specific Tailoring:** Defender for Endpoint runs on Windows and Linux hosts in every location. Linux allow-listing uses fapolicyd, and fleet equipment is excluded.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.2, DE-3.1

**Funding Line:** FY28 and FY29 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate, with activities through Phase 4

**Target Date / Sprint:** 2028-12-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-5.4.1: Vulnerability Scanning | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DI-5.4.2: Endpoint File Integrity Monitoring (FIM) | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.4.3: Advanced Threat Hunting | 4 | Process | None | Level 3 | Periodic (Event-Driven) | High | One-Time: Low; Recurring: High | Medium-term (3–6 months) |
| DI-5.4.4: Custom File Indicators | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.4.5: Custom Network Indicators | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.4.6: EDR Blocking/Enforcement Mode | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| DI-5.4.7: EDR Passive/Audit Mode | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.4.8: EDR Sensor Deployment | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DI-5.4.9: Unmanaged/Rogue Device Discovery | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-5.4.10: Boot Integrity and Device Health Attestation | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### DI-5.5: Endpoint Response

**Selected Tool / Product / Service:** Microsoft Defender XDR, Splunk SOAR, Splunk SOAR containment playbooks under the CSSP agreement

**Environment-Specific Tailoring:** Defender for Endpoint runs on Windows and Linux hosts in every location. Linux allow-listing uses fapolicyd, and fleet equipment is excluded.

**Accountable Team:** Security Team

**Dependencies:** DI-3.2, DE-3.1

**Funding Line:** FY28 and FY29 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate, with activities through Phase 4

**Target Date / Sprint:** 2028-12-31

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

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Platform Team

**Dependencies:** DI-2, DI-3 design decisions

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-6.1.1: CMP Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DI-6.1.2: CMP Review and Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-6.1.3: CMP Periodic Review and Revision | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## DI-7: Vulnerability and Patch Management Planning

### DI-7.1: Vulnerability and Patch Management Plan (VPMP)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DI-4.8 design decisions

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DI-7.1.1: VPMP Development and Authoring | 2 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DI-7.1.2: VPMP Review and Approval | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DI-7.1.3: VPMP Periodic Review and Revision | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
