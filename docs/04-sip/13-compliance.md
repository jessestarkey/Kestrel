# CO: Compliance

*KESTREL Security Implementation Plan, Section 4 (Manage). Each record implements the outcome of the same ID in the [SADD](../03-sadd/13-compliance.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## CO-1: Regulatory and Framework Compliance

### CO-1.1: Regulatory Compliance Mapping

**Selected Tool / Product / Service:** Confluence Data Center, Jira Software Data Center

**Environment-Specific Tailoring:** The PMO ISSE inventories the issuances that bind KESTREL in Confluence and maps each to the outcomes that satisfy it. Gaps go to the requirement register, and the watch is checked each quarter with the AI regulatory mapping.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** GV-1.1, GV-4.5, GV-5.4, DoD and federal issuers

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| CO-1.1.1: Regulatory/Framework Requirement Inventory | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| CO-1.1.2: Requirement-to-Control Mapping and Gap Analysis | 2 | Documentation | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| CO-1.1.3: Regulatory Landscape Monitoring and Update Process | 2 | Process | None | Level 2 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### CO-1.2: Automated Technical Control Compliance Monitoring

**Selected Tool / Product / Service:** Tenable Security Center (ACAS), DISA SCAP Compliance Checker and STIG Viewer, Defender for Cloud CSPM, Splunk Enterprise

**Environment-Specific Tailoring:** The Platform Team holds the ACAS scan credentials and runs authenticated scans with DISA SCAP content. Defender for Cloud checks the cloud and containers. The Security Team reads the results in Splunk and tracks each finding. Fleet equipment is checked against its manufacturer baseline only in maintenance windows, with no automated correction.

**Accountable Team:** Platform Team, with the Security Team for results

**Dependencies:** DI-4.4, DI-4.5, DI-4.6, AP-5.11, DISA STIG and SCAP content

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| CO-1.2.1: Technical Control Compliance Status Aggregation and Scheduling | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| CO-1.2.2: Compliance Drift Detection and Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| CO-1.2.3: Non-Compliant Finding Remediation Tracking | 2 | Process | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### CO-1.3: Compliance Evidence Collection and Retention

**Selected Tool / Product / Service:** Azure Blob Storage with immutability policies, Confluence Data Center, GitLab Ultimate, Splunk Enterprise

**Environment-Specific Tailoring:** One evidence repository in immutable Blob storage exists from Phase 1, so every story can file its evidence. The Platform Team administers the storage account, and the Security Team holds only append and read roles. Fleet and OT evidence is entered by hand after each maintenance window, and a Splunk dashboard shows gaps.

**Accountable Team:** Security Team, with the Platform Team for the storage

**Dependencies:** GV-5.9

**Funding Line:** FY27 and FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| CO-1.3.1: Evidence Collection Automation (per control/assessment cycle) | 1 | Technical | Automate | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| CO-1.3.2: Evidence Repository Management and Retention Policy Enforcement | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| CO-1.3.3: Evidence Completeness/Quality Validation | 3 (pinned) | Process | None | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| CO-1.3.4: Compliance Posture Dashboard | 3 (pinned) | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** CO-1.3.3: Moved later to even out the Security Team, which carries most of Phase 2. Evidence validation is most useful just before the SCA's assessment. CO-1.3.4: Moved later to even out the Security Team, which carries most of Phase 2. The compliance dashboard is most useful just before the SCA's assessment.

## CO-2: Continuous Monitoring Program

### CO-2.1: Continuous Monitoring Plan (ConMon)

**Selected Tool / Product / Service:** Confluence Data Center, eMASS, Splunk Enterprise

**Environment-Specific Tailoring:** An interim ConMon plan is approved for the interim authorization to test in Phase 1, and the full plan in Phase 2. It watches CCSD tailoring action 3's 2027-09-30 date and action 6's annual review. Status goes to the AO monthly in summary and quarterly in full.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.9

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| CO-2.1.1: ConMon Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| CO-2.1.2: ConMon Review and Approval | 1 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| CO-2.1.3: ConMon Periodic Review and Revision | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### CO-2.2: Control Assessment Scheduling

**Selected Tool / Product / Service:** Confluence Data Center, eMASS, Jira Software Data Center

**Environment-Specific Tailoring:** A third of the control families is assessed each year, and the key, signing, and datalink controls each quarter. The SCA runs independent assessments, and the ISSOs self-assess between them in Jira. Inherited controls are accepted on each provider's current assessment.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** CO-2.1, GV-5.12, SCA

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| CO-2.2.1: Control Assessment Calendar/Cadence Definition | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| CO-2.2.2: Assessor Assignment and Coordination | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| CO-2.2.3: Assessment Completion Tracking and Reporting | 2 | Process | None | Level 1 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### CO-2.3: Annual Security Review

**Selected Tool / Product / Service:** Confluence Data Center, eMASS, Jira Software Data Center

**Environment-Specific Tailoring:** The SCA conducts the annual security review under the Security Assessment Plan. It covers the cloud, the data center, the alternate site, and the fleet through spares and the simulator. It uses the penetration test results. Determinations go in the SAR, and findings go to the POA&M in eMASS and the risk register.

**Accountable Team:** SCA, with the Security Team (ISSM) for access and evidence

**Dependencies:** RK-1.5, AP-3.5, SCA, Penetration testing provider

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-08-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| CO-2.3.1: Annual Review Scope and Methodology Definition | 3 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| CO-2.3.2: Annual Review Execution and Findings Documentation | 3 | Process | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: High | Medium-term (3–6 months) |
| CO-2.3.3: Annual Review Findings Integration into Risk Register/POA&M | 3 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## CO-3: Audit Management

### CO-3.1: Internal Audit Program

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center

**Environment-Specific Tailoring:** The parent organization's internal review office audits whether KESTREL's plans are carried out, reaching every governing plan at least once every two years. Findings are tracked in Jira until the fix is verified.

**Accountable Team:** Program Office, with the parent organization's internal review office

**Dependencies:** GV-2.1, Parent organization's internal review office

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| CO-3.1.1: Internal Audit Charter and Scope Definition | 3 | Documentation | None | Level 2 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| CO-3.1.2: Audit Schedule/Cadence and Execution | 3 | Process | None | Level 2 | Periodic (Annual) | High | One-Time: Low; Recurring: Moderate | Medium-term (3–6 months) |
| CO-3.1.3: Audit Findings Tracking and Remediation Verification | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| CO-3.1.4: Internal Audit Charter Periodic Review and Revision | 3 | Documentation | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### CO-3.2: External Audit Coordination

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center, Azure Blob Storage with immutability policies

**Environment-Specific Tailoring:** The program manager receives each audit or inspection request, and the ISSM packages evidence from the repository after a CUI and releasability review. DCMA and DIBCAC reviews cover the performer's CMMC laptops. Findings go to the POA&M.

**Accountable Team:** Program Office (program manager), with the Security Team (ISSM)

**Dependencies:** CO-1.3, Inspectors general, GAO, JFHQ-DODIN, DCMA, DIBCAC

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| CO-3.2.1: External Audit Request/Notification Intake Process | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| CO-3.2.2: Audit Evidence Packaging and Response Coordination | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| CO-3.2.3: External Audit Findings Tracking and Closure | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

## CO-4: Privacy Compliance

### CO-4.1: Privacy Program Management

**Selected Tool / Product / Service:** Confluence Data Center, Jira Service Management Data Center, Joint Knowledge Online training

**Environment-Specific Tailoring:** The privacy officer runs the program at the Privacy Overlay's Low tier. Users correct KESTREL-held attributes through Jira Service Management, while CAC and partner attributes are corrected at their source. Analysts, Data Team stewards, and service desk staff take role-based privacy training on JKO.

**Accountable Team:** Program Office (privacy officer)

**Dependencies:** CO-4.2, DoD component privacy office

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| CO-4.1.1: Privacy Program Charter and Policy Development | 2 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| CO-4.1.2: Privacy Roles and Responsibilities Definition | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| CO-4.1.3: PII Accuracy and Correction Request Handling | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| CO-4.1.4: Privacy Program Periodic Review | 2 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### CO-4.2: Privacy Impact Assessments (PIA)

**Selected Tool / Product / Service:** DD Form 2930, Confluence Data Center

**Environment-Specific Tailoring:** The PIA on DD Form 2930 is approved in Phase 1, before user and service desk records and the F28 imagery arrive. The component privacy office names the SORN for account and service desk records. A new collection, sensor, AI use case, or partner release triggers a reassessment.

**Accountable Team:** Program Office (privacy officer)

**Dependencies:** ID-1.1, DoD component privacy office

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| CO-4.2.1: PIA Trigger Criteria and Intake Process | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| CO-4.2.2: PIA Execution and Documentation | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| CO-4.2.3: PIA Periodic Review/Reassessment on System Change | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| CO-4.2.4: Privacy Notice and Privacy Act Statement Provision | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
