# DA: Data

*KESTREL Security Implementation Plan, Section 4 (Protect). Each record implements the outcome of the same ID in the [SADD](../03-sadd/07-data.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## DA-1: Data Awareness and Classification

### DA-1.1: Data Discovery, Labeling, and Classification

**Selected Tool / Product / Service:** Self-hosted OpenMetadata, Microsoft Purview Information Protection

**Environment-Specific Tailoring:** The Data Team labels every record at ingest, including prior collection over F28, and writes the labels as object metadata. Self-hosted OpenMetadata catalogs every store over F36 and classifies databases and structured files by content. Imagery and recordings are checked by their labels. Every result is checked against CCSD Section 2, and a store or type with no row is a finding.

**Accountable Team:** Data Team

**Dependencies:** ID-2.4, DA-1.9

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.1.1: Data Discovery and Classification | 1 (pinned) | Technical | Automate | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-1.1.2: Database Classification and Integration | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DA-1.1.1: Prior collection arrives over F28 for training in Phase 2, so the controls that act on it at ingest must exist first.

### DA-1.2: Attribute-Based Data and Application Access Enforcement (ABAC)

**Selected Tool / Product / Service:** Open Policy Agent policy decision service, Microsoft Entra ID, NetApp StorageGRID with S3 Object Lock, Azure AI Search

**Environment-Specific Tailoring:** An OPA policy decision service, with a replica on each side of the circuit that fails closed, decides data access from team, vendor rights, role, partner nation, and labels. Applications, the partner API, and the report index call it directly. StorageGRID enforces bucket policies generated from the same OPA policy, one set per data lake zone.

**Accountable Team:** Data Team

**Dependencies:** ID-2.4, DA-1.1

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.2.1: Attribute and Policy Schema Definition | 1 (pinned) | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.2.2: Policy Decision Point/Policy Engine Deployment | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-1.2.3: Policy Enforcement Point Integration at Data and Application Access Paths | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-1.2.4: Classification-to-Attribute Mapping and Policy Testing | 1 (pinned) | Technical | Automate | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.2.5: Clearance, Compartment, and Need-to-Know Attribute Integration | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.2.6: Compartment Separation and Flow Enforcement | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

**Pinned:** DA-1.2.1 and DA-1.2.4: Prior collection arrives over F28 for training in Phase 2, so the controls that act on it at ingest must exist first.

### DA-1.3: Data Provenance and Lineage Verification

**Selected Tool / Product / Service:** lakeFS, Azure Blob Storage with immutability policies, NetApp StorageGRID with S3 Object Lock

**Environment-Specific Tailoring:** Every feed is tagged with its origin at ingest, and ingest rejects any feed missing from the Data Team's source register. Provenance goes to an append-only ledger in immutable storage whose entries are hash-chained and signed. Training snapshots and partner releases verify provenance before using a record.

**Accountable Team:** Data Team

**Dependencies:** DA-1.1

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.3.1: Data Source/Origin Tracking | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.3.2: Provenance Metadata Capture and Immutable Logging | 1 (pinned) | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DA-1.3.3: Provenance Verification at Consumption/Use Points | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DA-1.3.1 and DA-1.3.2: Prior collection arrives over F28 for training in Phase 2, so the controls that act on it at ingest must exist first.

### DA-1.4: Database and Storage Threat Detection

**Selected Tool / Product / Service:** Defender for SQL and Defender for Storage, Splunk Enterprise Security

**Environment-Specific Tailoring:** Defender for SQL and Defender for Storage watch every cloud database and storage service. Splunk Enterprise Security analytics cover StorageGRID's audit logs and the report index's logs. The CSSP triages each alert, the zone's mission lead joins the investigation, and the IRP sets when it becomes an incident.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.4.1: Threat Detection Tool Deployment for Data Services | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DA-1.4.2: Anomalous Query/Access Pattern Alerting | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.4.3: Threat Finding Investigation Workflow | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DA-1.5: Data Loss Prevention (DLP) and Monitoring

**Selected Tool / Product / Service:** Azure API Management, Splunk Enterprise Security, GitLab Secret Detection

**Environment-Specific Tailoring:** Data leaves only by named paths, so DLP sits on each one. The partner API and the cross domain transfer gateway check every release against its markings. Pushes to GitLab are scanned for mission data and secrets before performer laptops can clone them. Splunk Enterprise Security correlations flag bulk reads across zones, and the data security dashboard serves the Security Team, the PMO ISSE, and the data owners.

**Accountable Team:** Security Team

**Dependencies:** DA-1.1, NE-2.10, NE-2.6

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references)

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

**Environment-Specific Tailoring:** Purview Information Protection in KESTREL's Microsoft 365 DoD tenant wraps each report released to a partner nation, limits it to that nation, and expires it on the foreign disclosure officer's terms. Wrapped reports travel through the partner API. Each partner's cross-cloud configuration is a term of its memorandum of agreement, set up as partners onboard in Phase 3.

**Accountable Team:** Mission teams, with the foreign disclosure officer

**Dependencies:** DA-1.1, ID-1.2

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

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

**Environment-Specific Tailoring:** The privacy officer approves the de-identification techniques AI-2.3 and AP-3.1 apply, with Presidio for identifying text and the person-detection model for people. KESTREL releases no datasets, so re-identification testing waits for a first release. The PMO ISSE is the only designated poster, and public content passes OPSEC and foreign disclosure review.

**Accountable Team:** Program Office (privacy officer)

**Dependencies:** DA-1.1

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.7.1: De-Identification Technique Application for Release Datasets | 2 | Technical | Automate | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.7.2: Motivated-Intruder Re-Identification Testing | N/A | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DA-1.7.3: Publicly Accessible Content Review | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Not applicable:** DA-1.7.2: KESTREL releases no datasets outside the program. A first dataset release reopens re-identification testing.

### DA-1.8: Media Protection Policy and Procedures

**Selected Tool / Product / Service:** Blancco Drive Eraser, Confluence Data Center, the datalink crypto modules

**Environment-Specific Tailoring:** Removable media is limited to three classes. Mission storage modules are encrypted under the aircraft's crypto module, carried by a named custodian, and stored locked, first on the spares and then across the fleet. Government media reaches the media intake station, which AP-2.6 scans. Key loaders stay under two-person custody, and retired drives, modules, and HSMs are wiped or zeroized on site.

**Accountable Team:** Fleet Operations, with IT Operations for drive sanitization

**Dependencies:** DI-2.3

**Funding Line:** FY27 and FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C30](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.8.1: Media Marking and Labeling Procedures | 1 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-1.8.2: Removable Media Handling and Transport Controls | 1 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-1.8.3: Media Sanitization and Destruction Procedures | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DA-1.8.4: Media Downgrading Procedures | N/A | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

**Pinned:** DA-1.8.1 and DA-1.8.2: Prior collection arrives over F28 for training in Phase 2, so the controls that act on it at ingest must exist first.

**Not applicable:** DA-1.8.4: KESTREL holds no classified data, so no media is downgraded. Data reaches the IL6 enclave only through the cross domain solution.

### DA-1.9: Data Management Plan (DMP)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** The Data Team authors the DMP in late Phase 1, with the retention schedule, minimization rules, and classification scheme, before prior collection arrives. Mission leads approve retention for their data, and the privacy officer approves handling of personal information. The Configuration Control Board approves it, and it is revised each year and whenever a payload vendor or data type is added.

**Accountable Team:** Data Team

**Dependencies:** The SADD's Data design decisions, GV-1.5

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-1.9.1: DMP Development and Authoring | 1 (pinned) | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.9.2: Data Retention and Disposition Schedule Definition | 1 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-1.9.3: Data Minimization Requirement Definition | 1 (pinned) | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-1.9.4: DMP Review and Approval | 1 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-1.9.5: DMP Periodic Review and Revision | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DA-1.9.1, DA-1.9.2, DA-1.9.3, and DA-1.9.4: KESTREL's design depends on it from the first build, since prior collection enters for training in Phase 2 under the DMP.

## DA-2: Data Encryption

### DA-2.1: Classification-Tied Document/Field-Level Encryption

**Selected Tool / Product / Service:** NetApp StorageGRID with S3 Object Lock, Azure Key Vault Premium, Azure SQL Database

**Environment-Specific Tailoring:** Each data lake zone encrypts under its own customer-supplied key on StorageGRID, which the record's label selects, with the ingest pipelines supplying the key on each request. Azure SQL column encryption protects personal fields in KESTREL-built databases. The service desk database uses transparent encryption under a customer-managed key, since column encryption would break its queries.

**Accountable Team:** Data Team, with the Platform Team

**Dependencies:** DA-3.3, DA-1.1

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

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

**Environment-Specific Tailoring:** Endpoints KESTREL terminates, namely Application Gateway, the Istio mesh, and the Palo Alto firewalls, accept only TLS 1.2 or later with CNSA cipher suites. Azure Policy enforces the minimum version on provider-managed endpoints, whose suites are recorded under DA-3.2. Corelight flags plaintext attempts on premises. GV-5.12 confirms the Istio add-on in Azure Government.

**Accountable Team:** Platform Team

**Dependencies:** DA-3.7, DA-3.8, GV-5.12

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

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

**Environment-Specific Tailoring:** Files move only over HTTPS or SFTP, including recordings crossing the ground segment conduit. Administrative SSH and RDP run only through CyberArk or a VDI session. Every transfer is logged to Splunk. If the payload processing workstation's replacement slips, its transfer is the one exception, once the AO re-dates CCSD tailoring action 3.

**Accountable Team:** Platform Team

**Dependencies:** ID-4.4

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C07](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-2.3.1: SFTP/FTPS/HTTPS Enforcement | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-2.3.2: SSH/RDP Hardening for Remote Management Access | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-2.3.3: File Transfer Audit Logging | 1 | Technical | Automate | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DA-2.4: Default Data at Rest Encryption

**Selected Tool / Product / Service:** Azure Policy, Azure Key Vault Premium, NetApp StorageGRID with S3 Object Lock, Veeam Data Platform

**Environment-Specific Tailoring:** At-rest encryption is on by default for every disk, storage service, database, and backup, and Azure Policy blocks any resource without it. StorageGRID and Veeam encrypt on premises under keys from the HSMs. Confidential computing is not required today, so protecting data in use relies on DA-2.1's column encryption.

**Accountable Team:** Platform Team

**Dependencies:** DA-3.3, DA-3.5

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), [C15](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-2.4.1: Encryption for VMs and Storage | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-2.4.2: Confidential Computing and Column Level Encryption | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DA-2.4.3: Encryption Compliance Monitoring and Enforcement | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-2.5: Encryption Key Ownership and Control

**Selected Tool / Product / Service:** Azure Key Vault Premium, Entrust nShield 5 HSMs

**Environment-Specific Tailoring:** Cloud keys are customer-managed in Key Vault Premium, imported from the nShield HSMs, and on-premises stores draw keys from the HSMs directly. Platform-managed keys are allowed only for synthetic or sanitized dev/test data, never in ML Dev/Test. The KMP maps each data class to its key tier.

**Accountable Team:** Platform Team

**Dependencies:** DA-3.5

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-2.5.1: Customer-Managed-Key Adoption Decision and Requirements Definition | 1 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-2.5.2: Data Classification-to-Key-Ownership-Tier Mapping | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## DA-3: Cryptographic Management

### DA-3.1: FIPS 140 / Approved Cryptographic Module Baseline

**Selected Tool / Product / Service:** Entrust nShield 5 HSMs, Azure Key Vault Premium, Keyfactor Command, Tenable Security Center (ACAS)

**Environment-Specific Tailoring:** KESTREL uses only FIPS 140-3 validated modules, at Level 3 for the HSMs and the datalink crypto modules, with CNSA algorithms under CNSSP 15. Scans of code, configuration, and traffic flag anything else. NSA-approved Type 1 cryptography sits on the IL6 side, inherited from the cross domain service provider.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C10](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.1.1: FIPS 140-Validated Module Selection and Inventory | 1 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.1.2: Approved Cryptographic Algorithm/Protocol Baseline Enforcement | 1 | Technical | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.1.3: Non-Compliant Cryptographic Usage Detection and Remediation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.1.4: NSA-Approved Cryptography for Classified Data | N/A | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |

**Not applicable:** DA-3.1.4: KESTREL protects no classified information. NSA-approved cryptography sits on the IL6 side, owned by the enclave and the cross domain service provider.

### DA-3.2: Post-Quantum Cryptography Readiness

**Selected Tool / Product / Service:** Keyfactor Command, Tenable Security Center (ACAS), Confluence Data Center

**Environment-Specific Tailoring:** CNSSP 15 requires CNSA 2.0 for new national security system acquisitions from 2027-01-01. Every contract therefore requires CNSA 2.0 support or an NSA-approved exception or AO waiver. The inventory starts in Phase 1 and the transition plan in Phase 2. Code signing must use CNSA 2.0 exclusively by 2030, which affects the Key Vault signing keys and the fleet key.

**Accountable Team:** Program Office (PMO ISSE), with the Platform Team

**Dependencies:** DA-3.3, GV-3.2

**Funding Line:** FY27 and FY28 program management

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C11](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.2.1: Cryptographic Inventory for PQC Migration | 1 (pinned) | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DA-3.2.2: CNSA 2.0 Algorithm Transition Planning | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DA-3.2.3: Crypto-Agility Design Requirements | 1 (pinned) | Documentation | None | Level 3 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |

**Pinned:** DA-3.2.1: CNSSP 15 requires CNSA 2.0 for new acquisitions from 2027-01-01, so the inventory starts with the first purchases. DA-3.2.3: The PKI, keys, signing, and datalinks are designed in Phase 1, so crypto-agility must be required from the start.

### DA-3.3: Key Management Policies and Infrastructure

**Selected Tool / Product / Service:** Entrust nShield 5 HSMs, Azure Key Vault Premium, Keyfactor Command

**Environment-Specific Tailoring:** Cloud workloads in every spoke holding mission data, ML Dev/Test included, draw keys only from Key Vault Premium, which also holds the release and dev/test signing keys. The nShield HSMs hold the roots, the PKI, the fleet signing key, and the datalink keys, with a standby at the alternate site.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C10](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.3.1: Centralized Key Management Infrastructure | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-3.3.2: Vault Service Tier Selection | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: High | Short-term (1–3 months) |

### DA-3.4: HSM and Hardware Root-of-Trust Management

**Selected Tool / Product / Service:** Entrust nShield 5 HSMs, Active Directory Certificate Services

**Environment-Specific Tailoring:** The nShield HSMs in the data center hold the root certificate authority, the fleet signing key, and the datalink keys. Backups reach the standby HSM at the alternate site only as security-world blobs over F19. Otherwise the keys leave only inside a datalink crypto module or a key loader, which is zeroized after each fill.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Keys and PKI are a Phase 1 prerequisite.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C10](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.4.1: HSM Deployment and Provisioning | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DA-3.4.2: Hardware Root-of-Trust Key Generation and Attestation | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DA-3.4.3: HSM Access Control and Audit Logging | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DA-3.4.1 and DA-3.4.2: KESTREL's design depends on it from the first build, since the HSMs hold the root, signing, and datalink keys.

### DA-3.5: Key Lifecycle Automation

**Selected Tool / Product / Service:** Azure Key Vault Premium, Entrust nShield 5 HSMs, Keyfactor Command

**Environment-Specific Tailoring:** Keys Key Vault generates rotate on the KMP's cadence. Imported keys cannot rotate in place, so a near-expiry event triggers an nShield job that generates, wraps, and imports the replacement. Keys are available in the second IL5 region. Backup keys are escrowed in the alternate site's HSM under split knowledge.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** DA-3.3, DA-3.4

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references)

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

**Selected Tool / Product / Service:** Azure Key Vault Premium, Entrust nShield 5 HSMs, Microsoft Entra Privileged Identity Management, Splunk Enterprise

**Environment-Specific Tailoring:** Tier 0 administrators manage keys, workload identities and Fleet Operations' key loading staff use them, and the Security Team audits them, with no identity holding two roles. Changing a key's access policy needs a second Tier 0 approver and alerts the Security Team.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** DA-3.3

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.6.1: Separation of Duties Enforcement | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-3.6.2: Key Access Monitoring | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-3.7: Certificate Policies and Integration

**Selected Tool / Product / Service:** Active Directory Certificate Services, Entrust nShield 5 HSMs, Keyfactor Command

**Environment-Specific Tailoring:** Active Directory Certificate Services issues device, workload, and code-signing certificates under the HSM-held root, and Keyfactor Command distributes them. User and partner certificates come from DoD PKI and External Certificate Authorities, whose trust anchors the identity provider holds.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** DA-3.4

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.7.1: Certificate Management Infrastructure | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DA-3.7.2: Certificate Authorities Integration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |

### DA-3.8: Automated Certificate Renewal

**Selected Tool / Product / Service:** Keyfactor Command, cert-manager

**Environment-Specific Tailoring:** cert-manager renews workload and service certificates through Keyfactor's external issuer for AD CS, ahead of expiry, and rebinds them without an operator. The Istio mesh's certificates come from istiod with its plug-in CA kept in Key Vault. Aircraft and station certificates renew during maintenance windows.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** DA-3.7

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C11](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.8.1: Automated Renewal Configuration | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.8.2: Automatic Certificate Binding | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-3.9: Certificate Lifecycle and Revocation

**Selected Tool / Product / Service:** Keyfactor Command, Splunk Enterprise

**Environment-Specific Tailoring:** Keyfactor's inventory tracks every certificate KESTREL issues or trusts, and Splunk alerts on approaching expiry or unrequested issuance. Revocation procedures cover every case, including an aircraft declared lost, whose device certificates are revoked at once. The datalink keys it shared are superseded fleet-wide from the nShield HSMs by key loader.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** DA-3.7

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

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

**Environment-Specific Tailoring:** Each spoke's Key Vault grants each workload identity only the secrets it needs. Humans hold no standing vault access and activate it just in time through Entra PIM inside an admin VDI session.

**Accountable Team:** Platform Team

**Dependencies:** ID-3.1, ID-4.3

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

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

**Environment-Specific Tailoring:** Every Key Vault is reached only through a private endpoint in its own spoke, with public network access disabled. Its firewall admits only that spoke's workloads, and Azure Policy denies any change.

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
| DA-3.11.1: Secrets Vault Private Endpoint and Firewall | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.11.2: Public Network Access Disablement | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DA-3.11.1: KESTREL's design depends on it from the first build, since every vault is private.

### DA-3.12: Secrets Vault Protection and Monitoring

**Selected Tool / Product / Service:** Azure Key Vault Premium, Defender for Key Vault, Splunk Enterprise

**Environment-Specific Tailoring:** Every Key Vault has soft delete and purge protection on, so no one person can purge a vault or key. Vault operations and Defender for Key Vault alerts go to Splunk.

**Accountable Team:** Platform Team

**Dependencies:** DA-3.10

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.12.1: Secrets Vault Deletion Protection | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-3.12.2: Secrets Vault Monitoring and Threat Detection | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DA-3.13: Key Management Plan (KMP)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** The Tier 0 administrators author the KMP, with Fleet Operations writing the datalink key procedures. It requires RSA-3072 or larger for customer-managed and imported keys under CNSA. The PMO ISSE adds the CNSA 2.0 transition section when DA-3.2.2 completes. The Security Team reviews it, and the Configuration Control Board approves it.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** The SADD's Data design decisions, GV-1.5

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DA-3.13.1: KMP Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DA-3.13.2: KMP Review and Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DA-3.13.3: KMP Periodic Review and Revision | 2 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DA-3.13.3: Its first review cannot fall in Phase 1, since the document it reviews is approved there.
