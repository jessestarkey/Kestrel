# RK: Risk

*KESTREL Security Implementation Plan, Section 4 (Manage). Each record implements the outcome of the same ID in the [SADD](../03-sadd/12-risk.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## RK-1: Risk Assessment and Treatment

### RK-1.1: Risk Assessment Methodology

**Selected Tool / Product / Service:** Jira Software Data Center, eMASS, Confluence Data Center

**Environment-Specific Tailoring:** The PMO ISSE defines one method based on NIST SP 800-30, scoring likelihood and impact on five-point scales. Impact is anchored to the CCSD's categorization, mission effects, and privacy harm. Anything that could cost an aircraft, compromise the command link, expose row 13's keys, or tamper with a certified model or signed release scores at the top.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** GV-1.2

**Funding Line:** FY27 and FY28 program management

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.1.1: Risk Assessment Methodology Definition | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.1.2: Methodology Application Guidance and Training | 2 | Process | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.1.3: Methodology Periodic Review and Update | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### RK-1.2: Risk Appetite and Tolerance Definition

**Selected Tool / Product / Service:** Jira Software Data Center, eMASS, Confluence Data Center

**Environment-Specific Tailoring:** The program manager drafts the risk appetite statement and the AO approves it. The AO accepts every risk, and a standing AO delegation recorded in the authorization decision lets the PMO ISSE accept Low and Very Low ones. Risk above Very Low to flight safety, the command link, keys, or the High-integrity models and releases goes to the AO.

**Accountable Team:** Program Office (program manager)

**Dependencies:** RK-1.1

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.2.1: Risk Appetite/Tolerance Statement Development | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.2.2: Tolerance-to-Acceptance-Authority Tier Alignment | 1 | Process | None | Level 1 | One-Time | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| RK-1.2.3: Periodic Review and Revision | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### RK-1.3: Risk Register and Tracking

**Selected Tool / Product / Service:** Jira Software Data Center, eMASS, Confluence Data Center

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.4

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.3.1: Risk Register Structure and Intake Process | 2 | Process | None | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.3.2: Risk Owner Assignment and Status Tracking | 2 | Process | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.3.3: Risk Register Periodic Review and Reporting | 2 | Process | None | Level 1 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| RK-1.3.4: Risk Register Automation/Integration with POA&M and SCTM | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| RK-1.3.5: Enterprise Risk Posture Dashboard | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### RK-1.4: Risk Acceptance Process

**Selected Tool / Product / Service:** Jira Software Data Center, eMASS, Confluence Data Center

**Environment-Specific Tailoring:** Acceptances are requested and scored in Jira and recorded in eMASS. A Very Low risk, or a Low risk outside CCSD rows 6, 8, 10, and 13, goes to the PMO ISSE under the AO's delegation. Everything else goes to the AO.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** RK-1.2

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.4.1: Risk Acceptance Request and Approval Workflow | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.4.2: Risk Acceptance Documentation and Expiration Tracking | 1 | Documentation | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| RK-1.4.3: Risk Acceptance Periodic Re-Review | 1 | Process | None | Level 1 | Periodic (Semi-Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### RK-1.5: Security Assessment Plan

**Selected Tool / Product / Service:** eMASS, Confluence Data Center

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** SCA

**Dependencies:** GV-5.4

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.5.1: Security Assessment Plan Development and Authoring | 3 | Documentation | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| RK-1.5.2: Security Assessment Plan Review and Approval | 3 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.5.3: Security Assessment Plan Periodic Review and Revision | 3 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RK-1.6: Security Assessment Report (SAR)

**Selected Tool / Product / Service:** eMASS

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** SCA

**Dependencies:** GV-5.4

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Government-furnished, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.6.1: SAR Development and Authoring | 3 | Documentation | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| RK-1.6.2: SAR Review and Validation | 3 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.6.3: SAR Delivery to AO/Stakeholders | 3 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### RK-1.7: Risk Assessment Report (RAR)

**Selected Tool / Product / Service:** eMASS

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** SCA

**Dependencies:** GV-5.4

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Government-furnished, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.7.1: RAR Development and Authoring | 3 | Documentation | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| RK-1.7.2: RAR Review and Validation | 3 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.7.3: RAR Delivery to AO/Stakeholders | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### RK-1.8: Plan of Action and Milestones (POA&M)

**Selected Tool / Product / Service:** Jira Software Data Center, eMASS, Confluence Data Center

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.4

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.8.1: POA&M Item Creation and Tracking | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.8.2: POA&M Milestone Monitoring and Status Reporting | 2 | Process | None | Level 1 | Periodic (Monthly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.8.3: POA&M Closure Verification and Evidence Collection | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RK-1.9: Emerging Technology Risk Assessment

**Selected Tool / Product / Service:** Jira Software Data Center, eMASS, Confluence Data Center

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Program Office (chief engineer)

**Dependencies:** GV-5.4

**Funding Line:** FY28 and FY29 program management, with the Phase 4 share unfunded

**Rollout Phase:** Phase 3, Mission, AI, and Fleet, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.9.1: Emerging Technology Horizon Scanning | 4 | Process | None | Level 3 | Periodic (Semi-Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.9.2: Technology Adoption Risk Assessment Process | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.9.3: Emerging Tech Risk Findings Integration into Risk Register | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

## RK-2: Threat Intelligence

### RK-2.1: Threat Intelligence Program

**Selected Tool / Product / Service:** Splunk Enterprise Security, Confluence Data Center, the CSSP

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1

**Funding Line:** FY28 and FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 3, Mission, AI, and Fleet, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-2.1.1: Threat Intelligence Program Charter and Source/Feed Strategy | 3 | Documentation | None | Level 2 | One-Time | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.1.2: Threat Intelligence Analyst Function/Roles Definition | 3 | Documentation | None | Level 2 | One-Time | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.1.3: Program Maturity Assessment and Periodic Review | 4 | Process | None | Level 3 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### RK-2.2: Threat Landscape Monitoring

**Selected Tool / Product / Service:** Splunk Enterprise Security, Confluence Data Center, the CSSP

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-2.2.1: Strategic Threat Actor/Campaign Tracking | 3 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.2.2: Emerging TTP (tactics, techniques, procedures) Monitoring | 3 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.2.3: Threat Landscape Reporting to Leadership/Risk Function | 3 | Documentation | None | Level 2 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### RK-2.3: Indicator Sharing and Enrichment

**Selected Tool / Product / Service:** Splunk Enterprise Security, the CSSP, DC3's DIB Cybersecurity program

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-2.3.1: Inter-Org/ISAC Indicator Sharing Participation | 2 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.3.2: Strategic Indicator Curation and Quality Vetting | 2 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.3.3: Indicator Hand-Off to Operate Pillar's IOC Feed Management | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## RK-3: Enterprise Risk Prioritization

### RK-3.1: Risk-Based Remediation Prioritization

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** RK-1.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-3.1.1: Enterprise Remediation Ranking Model | 2 | Documentation | None | Level 2 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-3.1.2: Cross-Team Remediation Prioritization Workflow | 2 | Process | None | Level 2 | Periodic (Monthly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-3.1.3: Prioritization Periodic Recalibration | 2 | Process | None | Level 2 | Periodic (Semi-Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### RK-3.2: Business Impact Analysis (BIA)

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Program Office (program manager)

**Dependencies:** RK-1.1

**Funding Line:** FY27 and FY28 program management

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-3.2.1: BIA Methodology Definition and Criticality Tiering | 1 (pinned) | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-3.2.2: BIA Execution per System/Mission-Critical Process | 2 | Process | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| RK-3.2.3: BIA Periodic Review and Update | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

**Pinned:** RK-3.2.1: Phase 1 backs up Tier 1 services, so the criticality tiers must exist first.
