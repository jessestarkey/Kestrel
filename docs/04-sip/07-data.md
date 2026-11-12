# DA: Data

*KESTREL Security Implementation Plan, Section 4 (Protect). Each record implements the outcome of the same ID in the [SADD](../03-sadd/07-data.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## DA-1: Data Awareness and Classification

### DA-1.1: Data Discovery, Labeling, and Classification

**Selected Tool / Product / Service:** Microsoft Purview Information Protection, Microsoft Purview Data Map, Open Policy Agent (Gatekeeper and Conftest)

**Environment-Specific Tailoring:** Purview Data Map scans the cloud directly and the data center through a self-hosted integration runtime. Fleet storage modules are labeled by procedure.

**Accountable Team:** Data Team

**Dependencies:** ID-2.4, DA-3.3

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.1.1: Data Discovery and Classification | 2 | Technical | Automate | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-1.1.2: Database Classification and Integration | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-1.2: Attribute-Based Data and Application Access Enforcement (ABAC)

**Selected Tool / Product / Service:** Open Policy Agent (Gatekeeper and Conftest), Microsoft Entra ID, NetApp StorageGRID with S3 Object Lock, Azure AI Search

**Environment-Specific Tailoring:** Purview Data Map scans the cloud directly and the data center through a self-hosted integration runtime. Fleet storage modules are labeled by procedure.

**Accountable Team:** Data Team

**Dependencies:** ID-2.4, DA-3.3

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.2.1: Attribute and Policy Schema Definition | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.2.2: Policy Decision Point/Policy Engine Deployment | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-1.2.3: Policy Enforcement Point Integration at Data and Application Access Paths | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-1.2.4: Classification-to-Attribute Mapping and Policy Testing | 2 | Technical | Automate | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.2.5: Clearance, Compartment, and Need-to-Know Attribute Integration | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.2.6: Compartment Separation and Flow Enforcement | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

### DA-1.3: Data Provenance and Lineage Verification

**Selected Tool / Product / Service:** lakeFS, Azure Blob Storage with immutability policies, NetApp StorageGRID with S3 Object Lock

**Environment-Specific Tailoring:** Purview Data Map scans the cloud directly and the data center through a self-hosted integration runtime. Fleet storage modules are labeled by procedure.

**Accountable Team:** Data Team

**Dependencies:** ID-2.4, DA-3.3

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.3.1: Data Source/Origin Tracking | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.3.2: Provenance Metadata Capture and Immutable Logging | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DA-1.3.3: Provenance Verification at Consumption/Use Points | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-1.4: Database and Storage Threat Detection

**Selected Tool / Product / Service:** Defender for SQL and Defender for Storage, Splunk Enterprise Security

**Environment-Specific Tailoring:** Purview Data Map scans the cloud directly and the data center through a self-hosted integration runtime. Fleet storage modules are labeled by procedure.

**Accountable Team:** Security Team

**Dependencies:** ID-2.4, DA-3.3

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.4.1: Threat Detection Tool Deployment for Data Services | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DA-1.4.2: Anomalous Query/Access Pattern Alerting | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.4.3: Threat Finding Investigation Workflow | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DA-1.5: Data Loss Prevention (DLP) and Monitoring

**Selected Tool / Product / Service:** Microsoft Purview Data Loss Prevention, Microsoft Purview Insider Risk Management, Azure API Management, Splunk Enterprise Security

**Environment-Specific Tailoring:** Purview Data Map scans the cloud directly and the data center through a self-hosted integration runtime. Fleet storage modules are labeled by procedure.

**Accountable Team:** Security Team

**Dependencies:** ID-2.4, DA-3.3

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.5.1: DLP Policy/Rule Definition | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.5.2: Insider Risk Behavioral Analytics | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DA-1.5.3: Monitoring and Response Configuration | 2 | Technical | Automate | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-1.5.4: Data Security Posture Dashboard | 2 | Technical | Visualize | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DA-1.6: Data Rights Management (DRM)

**Selected Tool / Product / Service:** Microsoft Purview Information Protection

**Environment-Specific Tailoring:** Purview Data Map scans the cloud directly and the data center through a self-hosted integration runtime. Fleet storage modules are labeled by procedure.

**Accountable Team:** Mission teams, with the foreign disclosure officer

**Dependencies:** ID-2.4, DA-3.3

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.6.1: DRM Policy Classification Mapping | 2 | Documentation | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-1.6.2: Persistent Access Control/Encryption Binding | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-1.6.3: DRM Revocation and Expiration Enforcement | 2 | Technical | None | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DA-1.7: Dataset De-Identification and Disclosure Review

**Selected Tool / Product / Service:** Microsoft Presidio, Confluence Data Center

**Environment-Specific Tailoring:** Purview Data Map scans the cloud directly and the data center through a self-hosted integration runtime. Fleet storage modules are labeled by procedure.

**Accountable Team:** Program Office (privacy officer)

**Dependencies:** ID-2.4, DA-3.3

**Funding Line:** FY27 and FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.7.1: De-Identification Technique Application for Release Datasets | 2 | Technical | Automate | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.7.2: Motivated-Intruder Re-Identification Testing | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DA-1.7.3: Publicly Accessible Content Review | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DA-1.8: Media Protection Policy and Procedures

**Selected Tool / Product / Service:** Blancco Drive Eraser, Confluence Data Center

**Environment-Specific Tailoring:** Purview Data Map scans the cloud directly and the data center through a self-hosted integration runtime. Fleet storage modules are labeled by procedure.

**Accountable Team:** Fleet Operations

**Dependencies:** ID-2.4, DA-3.3

**Funding Line:** FY27 and FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C30](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.8.1: Media Marking and Labeling Procedures | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-1.8.2: Removable Media Handling and Transport Controls | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-1.8.3: Media Sanitization and Destruction Procedures | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DA-1.8.4: Media Downgrading Procedures | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### DA-1.9: Data Management Plan (DMP)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** Purview Data Map scans the cloud directly and the data center through a self-hosted integration runtime. Fleet storage modules are labeled by procedure.

**Accountable Team:** Data Team

**Dependencies:** ID-2.4, DA-3.3

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.9.1: DMP Development and Authoring | 2 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.9.2: Data Retention and Disposition Schedule Definition | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.9.3: Data Minimization Requirement Definition | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-1.9.4: DMP Review and Approval | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-1.9.5: DMP Periodic Review and Revision | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## DA-2: Data Encryption

### DA-2.1: Classification-Tied Document/Field-Level Encryption

**Selected Tool / Product / Service:** NetApp StorageGRID with S3 Object Lock, Azure Key Vault Managed HSM, Azure SQL Database

**Environment-Specific Tailoring:** Cloud encryption uses customer-managed keys in Managed HSM. Data center and alternate site encryption uses StorageGRID and Veeam keys rooted in the nShield HSMs.

**Accountable Team:** Data Team, with the Platform Team

**Dependencies:** DA-3.3, DA-3.4

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C16](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-2.1.1: Classification-Label-to-Encryption-Policy Mapping | 2 | Documentation | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-2.1.2: Document/Field-Level Encryption Enforcement at Creation/Ingestion | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DA-2.1.3: Encryption Compliance Scanning | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-2.2: TLS Encryption Enforcement

**Selected Tool / Product / Service:** Istio service mesh add-on for AKS, Azure Policy, Corelight sensors

**Environment-Specific Tailoring:** Cloud encryption uses customer-managed keys in Managed HSM. Data center and alternate site encryption uses StorageGRID and Veeam keys rooted in the nShield HSMs.

**Accountable Team:** Platform Team

**Dependencies:** DA-3.3, DA-3.4

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C14](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-2.2.1: Minimum TLS Version/Cipher Suite Enforcement Policy | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-2.2.2: TLS Certificate Deployment Across Data Services | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-2.2.3: Non-TLS Connection Detection and Blocking | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-2.3: Secure File Transfer and Management Protocols

**Selected Tool / Product / Service:** CyberArk Privileged Session Manager, Azure Virtual Desktop, Splunk Enterprise

**Environment-Specific Tailoring:** Cloud encryption uses customer-managed keys in Managed HSM. Data center and alternate site encryption uses StorageGRID and Veeam keys rooted in the nShield HSMs.

**Accountable Team:** Platform Team

**Dependencies:** DA-3.3, DA-3.4

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C07](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-2.3.1: SFTP/FTPS/HTTPS Enforcement | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-2.3.2: SSH/RDP Hardening for Remote Management Access | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-2.3.3: File Transfer Audit Logging | 1 | Technical | Automate | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DA-2.4: Default Data at Rest Encryption

**Selected Tool / Product / Service:** Azure Policy, Azure Key Vault Managed HSM, NetApp StorageGRID with S3 Object Lock, Veeam Data Platform

**Environment-Specific Tailoring:** Cloud encryption uses customer-managed keys in Managed HSM. Data center and alternate site encryption uses StorageGRID and Veeam keys rooted in the nShield HSMs.

**Accountable Team:** Platform Team

**Dependencies:** DA-3.3, DA-3.4

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), [C15](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-2.4.1: Encryption for VMs and Storage | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-2.4.2: Confidential Computing and Column Level Encryption | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DA-2.4.3: Encryption Compliance Monitoring and Enforcement | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-2.5: Encryption Key Ownership and Control

**Selected Tool / Product / Service:** Azure Key Vault Managed HSM, Entrust nShield 5 HSMs

**Environment-Specific Tailoring:** Cloud encryption uses customer-managed keys in Managed HSM. Data center and alternate site encryption uses StorageGRID and Veeam keys rooted in the nShield HSMs.

**Accountable Team:** Platform Team

**Dependencies:** DA-3.3, DA-3.4

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-2.5.1: Customer-Managed-Key Adoption Decision and Requirements Definition | 1 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-2.5.2: Data Classification-to-Key-Ownership-Tier Mapping | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## DA-3: Cryptographic Management

### DA-3.1: FIPS 140 / Approved Cryptographic Module Baseline

**Selected Tool / Product / Service:** Entrust nShield 5 HSMs, Azure Key Vault Managed HSM, Azure Key Vault Premium, Keyfactor Command, Active Directory Certificate Services

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C10](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.1.1: FIPS 140-Validated Module Selection and Inventory | 1 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.1.2: Approved Cryptographic Algorithm/Protocol Baseline Enforcement | 1 | Technical | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.1.3: Non-Compliant Cryptographic Usage Detection and Remediation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.1.4: NSA-Approved Cryptography for Classified Data | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |

### DA-3.2: Post-Quantum Cryptography Readiness

**Selected Tool / Product / Service:** Keyfactor Command, Tenable Security Center (ACAS), Confluence Data Center

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY28 and FY29 program management

**Rollout Phase:** Phase 4, Maturity

**Target Date / Sprint:** 2028-12-31

**Contracting / Procurement Reference:** [C11](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.2.1: Cryptographic Inventory for PQC Migration | 4 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DA-3.2.2: CNSA 2.0 Algorithm Transition Planning | 4 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DA-3.2.3: Crypto-Agility Design Requirements | 4 | Documentation | None | Level 3 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |

### DA-3.3: Key Management Policies and Infrastructure

**Selected Tool / Product / Service:** Entrust nShield 5 HSMs, Azure Key Vault Managed HSM, Azure Key Vault Premium, Keyfactor Command, Active Directory Certificate Services

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C10](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.3.1: Centralized Key Management Infrastructure | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-3.3.2: Vault Service Tier Selection | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: High | Short-term (1–3 months) |

### DA-3.4: HSM and Hardware Root-of-Trust Management

**Selected Tool / Product / Service:** Entrust nShield 5 HSMs, Azure Key Vault Managed HSM, Azure Key Vault Premium, Keyfactor Command, Active Directory Certificate Services

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C10](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.4.1: HSM Deployment and Provisioning | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DA-3.4.2: Hardware Root-of-Trust Key Generation and Attestation | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DA-3.4.3: HSM Access Control and Audit Logging | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DA-3.4.1: KESTREL's design depends on it from the first build, since the HSMs hold the root, signing, and datalink keys. DA-3.4.2: KESTREL's design depends on it from the first build, since the HSMs hold the root, signing, and datalink keys.

### DA-3.5: Key Lifecycle Automation

**Selected Tool / Product / Service:** Entrust nShield 5 HSMs, Azure Key Vault Managed HSM, Azure Key Vault Premium, Keyfactor Command, Active Directory Certificate Services

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C10](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.5.1: Automated Key Rotation | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.5.2: Key Hierarchy and BYOK | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DA-3.5.3: CMK Provisioning and Configuration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DA-3.5.4: Key Escrow and Recovery Procedures | 2 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DA-3.5.2: KESTREL's design depends on it from the first build, since every cloud key is rooted in the HSMs.

### DA-3.6: Key Access Separation of Duties

**Selected Tool / Product / Service:** Azure Key Vault Managed HSM, Entrust nShield 5 HSMs, CyberArk Privileged Access Manager, Splunk Enterprise

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.6.1: Separation of Duties Enforcement | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-3.6.2: Key Access Monitoring | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-3.7: Certificate Policies and Integration

**Selected Tool / Product / Service:** Active Directory Certificate Services, Entrust nShield 5 HSMs, Keyfactor Command

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.7.1: Certificate Management Infrastructure | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-3.7.2: Certificate Authorities Integration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |

### DA-3.8: Automated Certificate Renewal

**Selected Tool / Product / Service:** Keyfactor Command, cert-manager

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C11](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.8.1: Automated Renewal Configuration | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.8.2: Automatic Certificate Binding | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-3.9: Certificate Lifecycle and Revocation

**Selected Tool / Product / Service:** Keyfactor Command, Splunk Enterprise

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C11](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.9.1: Certificate Monitoring and Alerting | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-3.9.2: Certificate Inventory and Dashboard Maintenance | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.9.3: Revocation Procedures | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-3.10: Secrets Vault Access Controls

**Selected Tool / Product / Service:** Azure Key Vault Premium, Microsoft Entra Workload ID, Microsoft Entra Privileged Identity Management

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.10.1: Secrets Vault Access Policy Configuration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-3.10.2: Secrets Vault Workload Identity and JIT Access | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

**Pinned:** DA-3.10.2: KESTREL's design depends on it from the first build, since workloads read secrets by identity, never by stored credential.

### DA-3.11: Secrets Vault Network Security Hardening

**Selected Tool / Product / Service:** Azure Key Vault Premium, Azure Private Link, Azure Policy

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.11.1: Secrets Vault Private Endpoint and Firewall | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.11.2: Public Network Access Disablement | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DA-3.11.1: KESTREL's design depends on it from the first build, since every vault is private.

### DA-3.12: Secrets Vault Protection and Monitoring

**Selected Tool / Product / Service:** Azure Key Vault Premium, Defender for Key Vault, Splunk Enterprise

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.12.1: Secrets Vault Deletion Protection | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-3.12.2: Secrets Vault Monitoring and Threat Detection | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-3.13: Key Management Plan (KMP)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** nShield HSMs in the data center hold the root keys, with a second nShield at the alternate site. Managed HSM holds the cloud keys under the HSM-rooted hierarchy.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.13.1: KMP Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.13.2: KMP Review and Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-3.13.3: KMP Periodic Review and Revision | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
