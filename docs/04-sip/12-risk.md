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

**Environment-Specific Tailoring:** The program manager drafts the risk appetite statement and the AO approves it. The AO accepts every risk. A standing AO delegation, recorded in the interim authorization to test, lets the PMO ISSE accept Low and Very Low ones. The ATO decision carries the delegation forward. Risk above Very Low to flight safety, the command link, keys, or the High-integrity models and releases goes to the AO.

**Accountable Team:** Program Office (program manager)

**Dependencies:** RK-1.1, GV-5.7

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

**Selected Tool / Product / Service:** Jira Software Data Center, eMASS, Splunk Enterprise

**Environment-Specific Tailoring:** The risk register is a Jira project linked to eMASS POA&M items by record ID. Each risk names an owner, a score, a treatment, and a review date. The steering committee reviews it each month, and a Splunk dashboard shows it to leadership.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** RK-1.1, RK-1.8

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.3.1: Risk Register Structure and Intake Process | 2 | Process | None | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.3.2: Risk Owner Assignment and Status Tracking | 2 | Process | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.3.3: Risk Register Periodic Review and Reporting | 2 | Process | None | Level 1 | Periodic (Monthly) (re-rated) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| RK-1.3.4: Risk Register Automation/Integration with POA&M and SCTM | 3 (pinned) | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| RK-1.3.5: Enterprise Risk Posture Dashboard | 3 (pinned) | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** RK-1.3.4: Moved later to even out the Security Team, which carries most of Phase 2. Risk register automation fits the run-up to the package, alongside the POA&M and the SCTM. RK-1.3.5: Moved later to even out the Security Team, which carries most of Phase 2. The risk posture dashboard fits the run-up to the package, alongside the POA&M and the SCTM.

**Re-rated:** RK-1.3.3: The SADD's RK-1.3 design intent has the steering committee review the register each month.

### RK-1.4: Risk Acceptance Process

**Selected Tool / Product / Service:** Jira Service Management Data Center, Jira Software Data Center, eMASS

**Environment-Specific Tailoring:** Acceptances are requested in Jira Service Management and recorded in eMASS. A Very Low risk, or a Low risk outside CCSD rows 6, 8, 10, and 13, goes to the PMO ISSE under the AO's delegation. Everything else goes to the AO. The AO's acceptances of the mission-planning agent's and the coding agent's capability combinations expire after one year like any other. Acceptances are re-reviewed each quarter.

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
| RK-1.4.3: Risk Acceptance Periodic Re-Review | 1 | Process | None | Level 1 | Periodic (Quarterly) (re-rated) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

**Re-rated:** RK-1.4.3: The SADD's RK-1.4 design intent re-reviews acceptances each quarter.

### RK-1.5: Security Assessment Plan

**Selected Tool / Product / Service:** eMASS, Confluence Data Center

**Environment-Specific Tailoring:** The SCA writes the Security Assessment Plan in eMASS from the SCTM. It covers the cloud, the data center, the alternate site, the fleet through spares and the simulator, and each model through its evidence annex. Inherited controls are assessed by reviewing their provider packages.

**Accountable Team:** SCA

**Dependencies:** GV-5.9, GV-5.12, SCA

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

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

**Environment-Specific Tailoring:** The SCA writes the SAR in eMASS after the assessment that starts on 2028-07-31. The ISSM checks it for factual accuracy without changing any determination. It is handled as CUI and goes only to the AO, the program manager, the ISSM, and the PMO ISSE.

**Accountable Team:** SCA

**Dependencies:** RK-1.5, SCA

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-08-31

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

**Environment-Specific Tailoring:** The SCA writes the RAR from the SAR, the open risk register, and the monthly threat brief. It is reviewed with the risk owners and delivered to the AO with the SAR before the ATO decision.

**Accountable Team:** SCA

**Dependencies:** RK-1.6, RK-1.3, RK-2.2, SCA

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-09-09

**Contracting / Procurement Reference:** None. Government-furnished, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.7.1: RAR Development and Authoring | 3 | Documentation | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| RK-1.7.2: RAR Review and Validation | 3 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.7.3: RAR Delivery to AO/Stakeholders | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### RK-1.8: Plan of Action and Milestones (POA&M)

**Selected Tool / Product / Service:** eMASS, Jira Software Data Center

**Environment-Specific Tailoring:** POA&M items live in eMASS from Phase 1. Conditions of the interim authorization to test and the first findings are tracked from the start. Milestones are reviewed each month and reported to the AO each quarter. An ISSO closes an item only after verifying the fix, with the evidence filed in the evidence repository.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.9, CO-1.3

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.8.1: POA&M Item Creation and Tracking | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.8.2: POA&M Milestone Monitoring and Status Reporting | 1 | Process | None | Level 1 | Periodic (Monthly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.8.3: POA&M Closure Verification and Evidence Collection | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RK-1.9: Emerging Technology Risk Assessment

**Selected Tool / Product / Service:** Confluence Data Center, Jira Software Data Center

**Environment-Specific Tailoring:** The chief engineer and the PMO ISSE scan new foundation models, agent frameworks, payload sensors, and datalinks. AI candidates go through the review board and everything else through Security Impact Analysis. The post-quantum transition belongs to DA-3.2.

**Accountable Team:** Program Office (chief engineer)

**Dependencies:** GV-4.4, GV-5.11

**Funding Line:** FY28 and FY29 program management, with the Phase 3 share pending approval, with the Phase 4 share unfunded

**Rollout Phase:** Phase 3, Mission, AI, and Fleet, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-1.9.1: Emerging Technology Horizon Scanning | 4 | Process | None | Level 3 | Periodic (Semi-Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.9.2: Technology Adoption Risk Assessment Process | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-1.9.3: Emerging Tech Risk Findings Integration into Risk Register | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

## RK-2: Threat Intelligence

### RK-2.1: Threat Intelligence Program

**Selected Tool / Product / Service:** Confluence Data Center, the CSSP

**Environment-Specific Tailoring:** The Security Team names its threat intelligence analyst in Phase 2, before indicator vetting starts. Classified products reach KESTREL only as sanitized releases through a cleared government point of contact and the CSSP.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, Cyber defense service provider, DoD intelligence producers

**Funding Line:** FY28 and FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-2.1.1: Threat Intelligence Program Charter and Source/Feed Strategy | 2 | Documentation | None | Level 2 | One-Time | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.1.2: Threat Intelligence Analyst Function/Roles Definition | 2 | Documentation | None | Level 2 | One-Time | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.1.3: Program Maturity Assessment and Periodic Review | 4 | Process | None | Level 3 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### RK-2.2: Threat Landscape Monitoring

**Selected Tool / Product / Service:** Splunk Enterprise Security, Confluence Data Center, the CSSP

**Environment-Specific Tailoring:** The analyst maps each new technique, including datalink jamming and ATLAS techniques, against the detections in Splunk Enterprise Security. A monthly threat brief goes to the steering committee and the risk register.

**Accountable Team:** Security Team

**Dependencies:** RK-2.1, Cyber defense service provider, DoD intelligence producers

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-2.2.1: Strategic Threat Actor/Campaign Tracking | 3 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.2.2: Emerging TTP (tactics, techniques, procedures) Monitoring | 3 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.2.3: Threat Landscape Reporting to Leadership/Risk Function | 3 | Documentation | None | Level 2 | Periodic (Monthly) (re-rated) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

**Re-rated:** RK-2.2.3: The SADD's RK-2.2 design intent sends a threat brief each month.

### RK-2.3: Indicator Sharing and Enrichment

**Selected Tool / Product / Service:** Splunk Enterprise Security, the CSSP, DC3's DIB Cybersecurity program

**Environment-Specific Tailoring:** Indicators arrive from the CSSP as STIX over TAXII over F31 and wait for the analyst's vetting before detection uses them. KESTREL shares outbound only through the CSSP, after the ISSM's release determination. DC3's DIB Cybersecurity indicators cover only the performer's own systems.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, RK-2.1, Cyber defense service provider, DoD intelligence producers and DC3's DIB Cybersecurity program

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-2.3.1: Inter-Org/ISAC Indicator Sharing Participation | 3 (pinned) | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.3.2: Strategic Indicator Curation and Quality Vetting | 2 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RK-2.3.3: Indicator Hand-Off to Operate Pillar's IOC Feed Management | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** RK-2.3.1: Moved later to even out the Security Team, which carries most of Phase 2. Joining outside sharing communities follows a working internal intelligence feed, while curation and hand-off start in Phase 2.

## RK-3: Enterprise Risk Prioritization

### RK-3.1: Risk-Based Remediation Prioritization

**Selected Tool / Product / Service:** Jira Software Data Center, Splunk Enterprise

**Environment-Specific Tailoring:** One ranking in Jira orders remediation across every team, putting known exploited flaws on DMZ, Tier 0, or fleet assets first. IAVM and CYBERCOM deadlines are fixed inputs, and OT maintenance windows constrain fleet work. The model is recalibrated each quarter against the deviation log.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** RK-1.1, RK-3.2, CO-1.2

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RK-3.1.1: Enterprise Remediation Ranking Model | 2 | Documentation | None | Level 2 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-3.1.2: Cross-Team Remediation Prioritization Workflow | 2 | Process | None | Level 2 | Periodic (Monthly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RK-3.1.3: Prioritization Periodic Recalibration | 2 | Process | None | Level 2 | Periodic (Quarterly) (re-rated) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

**Re-rated:** RK-3.1.3: The SADD's RK-3.1 design intent recalibrates the ranking each quarter.

### RK-3.2: Business Impact Analysis (BIA)

**Selected Tool / Product / Service:** Confluence Data Center, Jira Service Management Assets

**Environment-Specific Tailoring:** The criticality tiering method exists in Phase 1, so Tier 1 backups start on provisional objectives. The full analysis in Phase 2 confirms them with the mission leads and Fleet Operations' operations lead. Results are recorded as Assets tags that set the recovery tiers and incident severity.

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
