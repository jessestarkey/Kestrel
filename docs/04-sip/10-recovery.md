# RC: Recovery

*KESTREL Security Implementation Plan, Section 4 (Operate). Each record implements the outcome of the same ID in the [SADD](../03-sadd/10-recovery.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## RC-1: Backup Automation and Coverage

### RC-1.1: Backup Coverage Strategy

**Selected Tool / Product / Service:** Veeam Data Platform, Azure Backup, NetApp StorageGRID with S3 Object Lock

**Environment-Specific Tailoring:** Azure Backup protects cloud services, and Veeam protects the data center with copies to the alternate site and to immutable Blob storage in the second region.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.3, DA-3.5

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-1.1.1: Backup Scope/Coverage Requirements Definition | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-1.1.2: Coverage Gap Analysis across Supported, Unsupported, and OT/Legacy Backup Workstreams | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-1.1.3: Backup Coverage Strategy Periodic Review and Update | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RC-1.2: Automated Backup for Supported Services

**Selected Tool / Product / Service:** Veeam Data Platform, Azure Backup, NetApp StorageGRID with S3 Object Lock

**Environment-Specific Tailoring:** Azure Backup protects cloud services, and Veeam protects the data center with copies to the alternate site and to immutable Blob storage in the second region.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.3, DA-3.5

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

**Environment-Specific Tailoring:** Azure Backup protects cloud services, and Veeam protects the data center with copies to the alternate site and to immutable Blob storage in the second region.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.3, DA-3.5

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

**Environment-Specific Tailoring:** Azure Backup protects cloud services, and Veeam protects the data center with copies to the alternate site and to immutable Blob storage in the second region.

**Accountable Team:** Fleet Operations

**Dependencies:** DI-1.3, DA-3.5

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

**Environment-Specific Tailoring:** Azure Backup protects cloud services, and Veeam protects the data center with copies to the alternate site and to immutable Blob storage in the second region.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.3, DA-3.5

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

**Environment-Specific Tailoring:** Azure Backup protects cloud services, and Veeam protects the data center with copies to the alternate site and to immutable Blob storage in the second region.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.3, DA-3.5

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

**Environment-Specific Tailoring:** Azure Backup protects cloud services, and Veeam protects the data center with copies to the alternate site and to immutable Blob storage in the second region.

**Accountable Team:** Platform Team

**Dependencies:** DI-1.3, DA-3.5

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

**Selected Tool / Product / Service:** Veeam Data Platform, NetApp StorageGRID with S3 Object Lock, Azure Blob Storage with immutability policies, CyberArk Privileged Access Manager

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, DA-3.5

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-2.1.1: Access Control Configuration | 2 | Technical | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-2.1.2: Destructive Backup Operation Protection | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### RC-2.2: Backup Data Encryption

**Selected Tool / Product / Service:** Veeam Data Platform, NetApp StorageGRID with S3 Object Lock, Azure Blob Storage with immutability policies, CyberArk Privileged Access Manager

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, DA-3.5

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-2.2.1: Encryption Configuration | 2 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-2.2.2: Backup Encryption Key Lifecycle Management | 2 | Technical | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### RC-2.3: Backup Immutability and Redundancy

**Selected Tool / Product / Service:** Veeam Data Platform, NetApp StorageGRID with S3 Object Lock, Azure Blob Storage with immutability policies, CyberArk Privileged Access Manager

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, DA-3.5

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-2.3.1: Immutability Configuration | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RC-2.3.2: Geographic Redundancy | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Medium-term (3–6 months) |

## RC-3: Recovery Readiness

### RC-3.1: Recovery Objective Definition (RTO/RPO)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** Cloud spokes are rebuilt by OpenTofu in US Gov Arizona from US Gov Virginia. The data center's Tier 1 services fail over to the alternate site's warm standby.

**Accountable Team:** Program Office (program manager)

**Dependencies:** RC-1.2, RC-1.3, RK-3.2, the alternate site facility agreement

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

**Selected Tool / Product / Service:** OpenTofu, Veeam Data Platform, ExpressRoute circuits from two carriers

**Environment-Specific Tailoring:** Cloud spokes are rebuilt by OpenTofu in US Gov Arizona from US Gov Virginia. The data center's Tier 1 services fail over to the alternate site's warm standby.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, RC-1.3, RK-3.2, the alternate site facility agreement

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C25](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-3.2.1: Recovery Testing Strategy | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-3.2.2: Recovery Procedure Validation | 2 | Process | None | Level 1 | Periodic (Quarterly) | High | One-Time: Low; Recurring: Moderate | Medium-term (3–6 months) |

### RC-3.3: Disaster Recovery Capabilities

**Selected Tool / Product / Service:** OpenTofu, Veeam Data Platform, ExpressRoute circuits from two carriers

**Environment-Specific Tailoring:** Cloud spokes are rebuilt by OpenTofu in US Gov Arizona from US Gov Virginia. The data center's Tier 1 services fail over to the alternate site's warm standby.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, RC-1.3, RK-3.2, the alternate site facility agreement

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C25](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RC-3.3.1: Full-Scale Disaster Recovery/Failover Exercise | 2 | Process | None | Level 1 | Periodic (Annual) | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| RC-3.3.2: CP Tabletop Exercise Facilitation | 2 | Process | None | Level 1 | Periodic (Semi-Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RC-3.3.3: DR Exercise Findings Remediation and Plan Update | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RC-3.4: Alternate Site and Telecommunications Readiness

**Selected Tool / Product / Service:** ExpressRoute circuits from two carriers, Entrust nShield 5 HSMs, Veeam Data Platform

**Environment-Specific Tailoring:** Cloud spokes are rebuilt by OpenTofu in US Gov Arizona from US Gov Virginia. The data center's Tier 1 services fail over to the alternate site's warm standby.

**Accountable Team:** Platform Team

**Dependencies:** RC-1.2, RC-1.3, RK-3.2, the alternate site facility agreement

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

**Environment-Specific Tailoring:** Cloud spokes are rebuilt by OpenTofu in US Gov Arizona from US Gov Virginia. The data center's Tier 1 services fail over to the alternate site's warm standby.

**Accountable Team:** Fleet Operations, with the mission teams

**Dependencies:** RC-1.2, RC-1.3, RK-3.2, the alternate site facility agreement

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

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

**Dependencies:** The SADD's Recovery design decisions

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
