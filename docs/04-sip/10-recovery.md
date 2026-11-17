# RC: Recovery

*KESTREL Security Implementation Plan, Section 4 (Operate). Each record implements the outcome of the same ID in the [SADD](../03-sadd/10-recovery.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## RC-1: Backup Automation and Coverage

### RC-1.1: Backup Coverage Strategy

**Selected Tool / Product / Service:** Jira Service Management Assets, Confluence Data Center

**Environment-Specific Tailoring:** Each asset's tier is a criticality tag in Jira Service Management Assets, set from the business impact analysis. HSM key backups go only to the alternate site's nShield, wrapped, and never to Veeam.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.3, RK-3.2, RC-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-1.1.1: Backup Scope/Coverage Requirements Definition | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-1.1.2: Coverage Gap Analysis across Supported, Unsupported, and OT/Legacy Backup Workstreams | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-1.1.3: Backup Coverage Strategy Periodic Review and Update | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RC-1.2: Automated Backup for Supported Services

**Selected Tool / Product / Service:** Veeam Data Platform, Azure Backup, NetApp StorageGRID with S3 Object Lock, Azure Blob Storage with immutability policies

**Environment-Specific Tailoring:** Azure Backup protects cloud services in immutable vaults copied to US Gov Arizona. Veeam protects the data center, with copies to the alternate site and to immutable Blob storage in the second region. The pipeline and Ansible bind each resource to its tier's policy.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.3, DA-3.5, RC-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-1.2.1: Automated Backup Job Deployment and Scheduling | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| RC-1.2.2: Backup Schedule/Retention/Scope Parameter Configuration | 2 | Technical | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### RC-1.3: Backup Unsupported Services

**Selected Tool / Product / Service:** Veeam Data Platform, Ansible Automation Platform

**Environment-Specific Tailoring:** Ansible jobs export Jira Service Management, the ACI controller, the vault contents, and the network appliances on their tier's schedule, and Veeam protects the exports. Foundation model deployments are code, so they need no backup.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-1.3.1: Native Backups | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-1.3.2: Custom Backups | 2 | Technical | None | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

### RC-1.4: OT/Legacy Configuration and Engineering Backup

**Selected Tool / Product / Service:** the aircraft and ground equipment manufacturer's tools, Veeam Data Platform

**Environment-Specific Tailoring:** Fleet Operations captures station configuration, launch equipment logic, and aircraft firmware with the manufacturers' offline tools, in maintenance windows only. Captures go to Veeam without datalink key material. An emergency restore outside a window needs the operations lead.

**Accountable Team:** Fleet Operations

**Dependencies:** RC-1.2

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C26](index.md#6-contracting-and-procurement-cross-references), [C15](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-1.4.1: Engineering Workstation/PLC Configuration Backup | 3 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| RC-1.4.2: OT Asset Firmware and Configuration Version Archival | 3 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-1.4.3: OT Backup Restoration Coordination with Plant Operations | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RC-1.5: Backup Policy Enforcement

**Selected Tool / Product / Service:** Azure Policy, Veeam Data Platform, OpenTofu

**Environment-Specific Tailoring:** Azure Policy and the OpenTofu modules bind each resource's Azure Backup policy from its criticality tag, and the pipeline rejects an untagged resource. Veeam policies on premises follow the same tiers.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C15](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-1.5.1: Automated Backup Policy Assignment/Binding to In-Scope Resources | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RC-1.5.2: Backup Policy Definition and Scope/Retention Standards | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RC-1.6: Backup Health and Operations Monitoring

**Selected Tool / Product / Service:** Veeam Data Platform, Azure Backup, Splunk Enterprise

**Environment-Specific Tailoring:** Veeam and Azure Backup job results go to Splunk, and a failure alerts the Platform Team's backup operators. IT Operations runs the routine checks, a sample is test-restored each week, and a Splunk dashboard shows each tier's state.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-1.6.1: Backup Health Monitoring | 2 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-1.6.2: Alert Configuration | 2 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| RC-1.6.3: Backup Integrity/Restorability Verification | 2 | Technical | Automate | Level 1 | Periodic (Monthly) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RC-1.6.4: Backup/DR Posture Dashboard | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### RC-1.7: Backup Compliance and Coverage Monitoring

**Selected Tool / Product / Service:** Jira Service Management Assets, Veeam Data Platform, Azure Backup

**Environment-Specific Tailoring:** A weekly job compares Jira Service Management Assets with what Veeam and Azure Backup protect, at each tier's settings. A gap opens a ticket to the owning team, and fleet capture gaps go to Fleet Operations.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, DI-1.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C15](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-1.7.1: Backup Policy/Retention Compliance Monitoring | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-1.7.2: Backup Coverage Gap Identification and Remediation | 2 | Process | None | Level 1 | Periodic (Monthly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## RC-2: Backup Data Protection

### RC-2.1: Backup Access and Operations Security

**Selected Tool / Product / Service:** Veeam Data Platform, Azure Backup, CyberArk Privileged Access Manager

**Environment-Specific Tailoring:** Veeam operators are a named Platform Team group, and deleting backups or shortening retention needs a second approver through CyberArk. Azure Backup's multi-user authorization uses a Resource Guard held by the Tier 0 administrators. The Security Team audits every such action in Splunk.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, DA-3.5

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-2.1.1: Access Control Configuration | 2 | Technical | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-2.1.2: Destructive Backup Operation Protection | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### RC-2.2: Backup Data Encryption

**Selected Tool / Product / Service:** Veeam Data Platform, Azure Backup, Entrust nShield 5 HSMs, Azure Key Vault Premium

**Environment-Specific Tailoring:** Veeam encrypts each backup set under its own key rooted in the nShield HSMs. Azure Backup vaults use customer-managed keys in Key Vault Premium. Each mission team's zone has its own key and vault.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, DA-3.5

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-2.2.1: Encryption Configuration | 2 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-2.2.2: Backup Encryption Key Lifecycle Management | 2 | Technical | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### RC-2.3: Backup Immutability and Redundancy

**Selected Tool / Product / Service:** Veeam Data Platform, NetApp StorageGRID with S3 Object Lock, Azure Blob Storage with immutability policies, Azure Backup

**Environment-Specific Tailoring:** StorageGRID object lock and immutable Blob storage hold every copy in compliance mode until its retention expires. Copies go to the alternate site and to US Gov Arizona. A spill in a locked copy is sanitized by destroying its backup set's key.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, DA-3.5

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-2.3.1: Immutability Configuration | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RC-2.3.2: Geographic Redundancy | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Medium-term (3–6 months) |

## RC-3: Recovery Readiness

### RC-3.1: Recovery Objective Definition (RTO/RPO)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** The program manager approves each tier's objectives from the business impact analysis. Aircraft storage modules keep each recording until its backup completes. A tier that misses its objective in a test is raised to the AO.

**Accountable Team:** Program Office (program manager)

**Dependencies:** RK-3.2

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-3.1.1: RTO/RPO Determination per System/Data Criticality Tier | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-3.1.2: RTO/RPO Validation against Actual Recovery Test Results | 2 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RC-3.2: Backup Recovery Testing

**Selected Tool / Product / Service:** Veeam Data Platform, Azure Backup, JFrog Artifactory

**Environment-Specific Tailoring:** The Platform Team restores a quarterly sample from every tier using only the written procedure. Fleet capture restores to spares or the simulator join in Phase 3, once captures exist. The registry restore re-verifies every signature.

**Accountable Team:** Platform Team, with Fleet Operations for fleet captures

**Dependencies:** RC-1.2, RC-3.1

**Funding Line:** FY28 O&M, platform and security operations, with the fleet slice as RDT&E fleet integration

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-3.2.1: Recovery Testing Strategy | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-3.2.2: Recovery Procedure Validation | 2 | Process | None | Level 1 | Periodic (Quarterly) | High | One-Time: Low; Recurring: Moderate | Medium-term (3–6 months) |

### RC-3.3: Disaster Recovery Capabilities

**Selected Tool / Product / Service:** OpenTofu, Veeam Data Platform, Active Directory Domain Services, Active Directory Certificate Services, CyberArk Privileged Access Manager

**Environment-Specific Tailoring:** OpenTofu rebuilds the cloud spokes in US Gov Arizona after the repository and runners are restored there. The alternate site's standby directory, issuing authority, DNS, and CyberArk vault take over if the data center is lost. A failover exercise runs each year.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, RC-3.1, NE-2.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-3.3.1: Full-Scale Disaster Recovery/Failover Exercise | 2 | Process | None | Level 1 | Periodic (Annual) | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| RC-3.3.2: CP Tabletop Exercise Facilitation | 2 | Process | None | Level 1 | Periodic (Semi-Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-3.3.3: DR Exercise Findings Remediation and Plan Update | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RC-3.4: Alternate Site and Telecommunications Readiness

**Selected Tool / Product / Service:** ExpressRoute circuits from two carriers, Entrust nShield 5 HSMs, Veeam Data Platform

**Environment-Specific Tailoring:** The data center's two circuits come from different carriers to different meet-me points, and traffic fails between them each quarter. The alternate site holds the warm standbys, the second nShield, and the backup copies. Tier 2 services restore into recovery spokes in US Gov Arizona.

**Accountable Team:** Platform Team

**Dependencies:** RC-3.1, NE-2.1, Parent organization's alternate site

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C25](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references), [C15](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-3.4.1: Alternate Processing/Work Site Designation and Agreement | 2 | Process | None | Level 1 | Periodic (Annual) | High | One-Time: High; Recurring: High | Long-term (6+ months) |
| RC-3.4.2: Alternate Telecommunications Service Agreement and Redundancy | 2 | Technical | None | Level 1 | Periodic (Annual) | High | One-Time: High; Recurring: High | Long-term (6+ months) |

### RC-3.5: Manual/Fail-Safe Operational Fallback Readiness

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** Stations fly on local smart card sign-in, and aircraft keep recordings on their storage modules until the lake returns. The program manager authorizes entering and ending fallback. Fleet drills start when the fleet integrates in Phase 3.

**Accountable Team:** Fleet Operations, with the mission teams

**Dependencies:** RC-3.1

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-3.5.1: Manual Operational Procedure Documentation | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| RC-3.5.2: Fail-Safe/Degraded-Mode Operational Training and Drills | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RC-3.5.3: Fallback Trigger Criteria and Activation Authority Definition | 2 | Documentation | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## RC-4: Contingency Planning

### RC-4.1: Contingency Plan (CP)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Platform Team

**Dependencies:** GV-5.1, RC-3.1, RK-3.2

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-4.1.1: CP Development and Authoring | 2 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RC-4.1.2: CP Review and Approval | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-4.1.3: CP Periodic Review and Revision | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-4.1.4: Contingency Roster and Contact Information | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-4.1.5: Contingency Information Sharing and Disclosure Procedures | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
