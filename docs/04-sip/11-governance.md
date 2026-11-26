# GV: Governance

*KESTREL Security Implementation Plan, Section 4 (Manage). Each record implements the outcome of the same ID in the [SADD](../03-sadd/11-governance.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## GV-1: Security Governance Structure

### GV-1.1: Security Policy Framework

**Selected Tool / Product / Service:** Confluence Data Center, Jira Software Data Center

**Environment-Specific Tailoring:** The program manager issues one system security policy beneath DoD issuances and the parent organization's policy. It names every governing plan as a standard and maps each statement to its control families. Its scope names the fleet and ground segment, the alternate site, and the performer laptops that hold source code.

**Accountable Team:** Program Office (program manager)

**Dependencies:** GV-1.2, Parent organization's enterprise policy

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-1.1.1: Policy Framework Structure Definition | 1 | Documentation | None | Level 1 | One-Time | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-1.1.2: Policy-to-Control Mapping | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| GV-1.1.3: Policy Taxonomy and Scope/Applicability Definition | 1 | Documentation | None | Level 1 | One-Time | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### GV-1.2: Security Roles and Responsibilities

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** The responsibility matrix lives in the SSP. It names the program manager, the PMO ISSE, the ISSM, the ISSOs, the SCA, the PSO, and each team lead. It records that the Security Team and the CSSP hold no administrative roles beyond ID-4.1's exceptions. It is reviewed each year and on any change of role holder.

**Accountable Team:** Program Office (program manager)

**Dependencies:** None. Roles are the first governance decision.

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-1.2.1: Role Definition for Security Functions | 1 | Documentation | None | Level 1 | One-Time | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-1.2.2: Role Assignment and RACI/Responsibility-Matrix Documentation | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-1.2.3: Roles and Responsibilities Periodic Review | 1 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### GV-1.3: ISSO/ISSM Appointment Letters

**Selected Tool / Product / Service:** Confluence Data Center, Jira Software Data Center

**Environment-Specific Tailoring:** The program manager signs the ISSM's appointment letter, and the ISSM signs each ISSO's. Each letter names the KESTREL boundary and the authority it confers. Letters are tracked in Jira and reissued whenever a role holder or the boundary changes.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-1.2

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-1.3.1: Appointment Letter Template Development | 1 | Documentation | None | Level 1 | One-Time | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| GV-1.3.2: Appointment Letter Issuance and Tracking | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-1.3.3: Appointment Letter Renewal/Update on Personnel Change | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### GV-1.4: Security Governance and Steering Committee

**Selected Tool / Product / Service:** Jira Service Management Data Center, Confluence Data Center, Splunk Enterprise

**Environment-Specific Tailoring:** The steering committee meets monthly, with the program manager in the chair. Its decisions and actions are tracked in Jira Service Management. A Splunk dashboard shows the security posture each month.

**Accountable Team:** Program Office (program manager)

**Dependencies:** GV-1.2

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-1.4.1: Committee Charter and Membership Definition | 2 | Documentation | None | Level 2 | One-Time | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-1.4.2: Meeting Cadence and Decision-Authority Definition | 2 | Process | None | Level 2 | One-Time | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-1.4.3: Governance Decision/Action Item Tracking | 2 | Process | None | Level 2 | Periodic (Monthly) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| GV-1.4.4: Security Program Metrics/Posture Dashboard for Leadership Reporting | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

### GV-1.5: Configuration Control Board

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center

**Environment-Specific Tailoring:** The chief engineer chairs the Configuration Control Board weekly, with Fleet Operations' operations lead as a standing member. It approves the hubs' rule base, the identity provider, interconnections, and the governing plans the AO does not approve. Its decision log runs from Phase 1, since it approves the first rule base and plans.

**Accountable Team:** Program Office (chief engineer)

**Dependencies:** GV-1.2

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-1.5.1: Board Charter and Membership Definition | 1 | Documentation | None | Level 1 | One-Time | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-1.5.2: Meeting Cadence and Coordination Scope Definition | 1 | Process | None | Level 1 | One-Time | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-1.5.3: Board Decision and Escalation Log | 1 (pinned) | Documentation | None | Level 2 | Periodic (Monthly) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

**Pinned:** GV-1.5.3: The Configuration Control Board approves the first rule base and plans in Phase 1, so its decision log starts then.

### GV-1.6: Zero Trust Maturity Assessment and Roadmap

**Selected Tool / Product / Service:** Confluence Data Center, Jira Software Data Center

**Environment-Specific Tailoring:** The PMO ISSE scores KESTREL against the DoW zero trust pillars each year. The score covers the cloud, the data center, the alternate site, and the ground segment. The gaps become SIP records, and progress goes to the steering committee each quarter.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** GV-1.2, DoW zero trust reference architecture

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-1.6.1: Zero Trust Maturity Self-Assessment | 2 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| GV-1.6.2: Target-Level Gap Identification and Roadmap Development | 2 | Documentation | None | Level 2 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| GV-1.6.3: Roadmap Progress Tracking and Reassessment | 2 | Process | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

## GV-2: Policy and Awareness

### GV-2.1: Policy Lifecycle Management

**Selected Tool / Product / Service:** Confluence Data Center, GitLab Ultimate

**Environment-Specific Tailoring:** Policies and plans are versioned in Confluence. The CCB approves standards and governing plans, except those the AO approves, and the ISSM approves runbooks. Machine-enforceable policy is written as code in GitLab, such as the admission and OPA policies.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-1.1, GV-1.5

**Funding Line:** FY27 and FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-2.1.1: Policy Drafting/Authoring Workflow | 1 | Process | None | Level 1 | One-Time | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-2.1.2: Policy Review and Approval Cadence | 1 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-2.1.3: Policy Retirement/Supersession Process | 2 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| GV-2.1.4: Policy Publication and Version Control | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-2.1.5: Policy-as-Code Implementation for Machine-Enforceable Policies Where Applicable | 3 (pinned) | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

**Pinned:** GV-2.1.3: Nothing is retired from KESTREL during the first build. GV-2.1.5: Moved later to even out the Security Team, which carries most of Phase 2. Policy as code follows the Phase 2 policies it encodes.

### GV-2.2: Policy Exception Management

**Selected Tool / Product / Service:** Jira Service Management Data Center, Jira Software Data Center, Confluence Data Center

**Environment-Specific Tailoring:** Exceptions are requested in Jira Service Management with an end date. Approval follows RK-1.4, so the PMO ISSE may approve Very Low ones, and Low ones outside CCSD rows 6, 8, 10, and 13. Expired exceptions become open findings.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-1.1, RK-1.4

**Funding Line:** FY27 and FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-2.2.1: Exception Request and Risk-Based Approval Workflow | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-2.2.2: Exception Tracking and Expiration Enforcement | 1 | Process | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-2.2.3: Exception Trend Reporting | 3 (pinned) | Process | None | Level 2 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

**Pinned:** GV-2.2.3: Moved later to even out the Security Team, which carries most of Phase 2. Exception trends need exceptions on record first.

### GV-2.3: Security Awareness and Training Program

**Selected Tool / Product / Service:** Joint Knowledge Online training, Active Directory Domain Services, Ansible Automation Platform, Jira Service Management Data Center

**Environment-Specific Tailoring:** Users complete DoD cyber awareness and CUI training on JKO before their account is created and each year after. Role-based courses cover operators, OT maintainers, and receiving staff. A lapsed course disables the account in Active Directory through Ansible, and the station accounts follow on their next sync. Phishing exercises are inherited from the parent organization's and performer's email.

**Accountable Team:** Security Team (ISSM), with IT Operations

**Dependencies:** GV-1.1, ID-1.8, Parent organization's and performer's enterprise email

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-2.3.1: Baseline Security Awareness Training | 1 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| GV-2.3.2: Simulated Social Engineering Exercise | 2 | Process | None | Level 2 | Periodic (Semi-Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-2.3.3: Role-Based Specialized Training | 1 | Process | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| GV-2.3.4: Training Completion Tracking and Enforcement | 1 | Process | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### GV-2.4: Rules of Behavior and Acceptable Use Policy

**Selected Tool / Product / Service:** Confluence Data Center, Jira Service Management Data Center, Active Directory Domain Services, Ansible Automation Platform

**Environment-Specific Tailoring:** Users sign the rules of behavior through a Jira Service Management form before their account is created and each year after. A lapsed acknowledgment disables the account in Active Directory through Ansible. Violations go to the PSO.

**Accountable Team:** Security Team (ISSM), with IT Operations

**Dependencies:** GV-1.1, ID-1.8

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-2.4.1: Rules of Behavior Drafting and Publication | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-2.4.2: User Acknowledgment Collection and Tracking | 1 | Process | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-2.4.3: Non-Acknowledgment/Violation Escalation Workflow | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

## GV-3: Third-Party and Supply Chain Governance

### GV-3.1: Vendor Security Risk Assessment

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center, the Supplier Performance Risk System, Jira Service Management Assets

**Environment-Specific Tailoring:** Suppliers answer the questionnaire before award, including the Phase 1 awards, and their SPRS scores are checked. Tier 1 covers anyone touching the fleet, mission data, or keys. Each self-hosted product is registered in Jira Service Management Assets once it passes.

**Accountable Team:** Program Office (supply chain lead)

**Dependencies:** GV-1.2, Commercial suppliers

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-3.1.1: Vendor Security Questionnaire/Assessment Process | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| GV-3.1.2: Vendor Risk Tiering and Periodic Reassessment | 1 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-3.1.3: Vendor Assessment Findings Remediation Tracking | 1 | Process | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-3.1.4: Third-Party Application Registration in Authoritative Inventory | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### GV-3.2: Contract Security Requirements

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center, the Supplier Performance Risk System

**Environment-Specific Tailoring:** The clause library holds every clause the contracting table marks as new, such as path diversity and the CSSP containment role, before the Phase 1 awards. Flow-down is verified at award, and compliance is checked each year. The performer laptops holding source code fall under DFARS 252.204-7012 from Phase 1.

**Accountable Team:** Program Office (supply chain lead)

**Dependencies:** GV-3.1, Performer and subcontractors

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-3.2.1: Standard Security Clause Library | 1 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| GV-3.2.2: Contract Security Requirement Flow-Down Verification | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-3.2.3: Contract Security Compliance Monitoring | 1 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| GV-3.2.4: CUI Protection Requirements for External Systems | 1 (pinned) | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** GV-3.2.1: Every clause the contracting table marks as new, such as path diversity and the CSSP containment role, must exist before the Phase 1 awards. GV-3.2.4: The performer laptops hold source code from Phase 1, so CUI protection on external systems is required then.

### GV-3.3: Supply Chain Risk Assessment and Dependency Mapping

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center

**Environment-Specific Tailoring:** The annual assessment maps the aircraft manufacturer, both payload vendors, the cloud provider, the foundation model's publisher, and the HSM vendor. Single points of supply and countries of origin are recorded in Confluence, and findings are tracked in Jira.

**Accountable Team:** Program Office (supply chain lead)

**Dependencies:** GV-3.1, Aircraft and ground equipment manufacturers, Payload vendors, IL5 cloud provider

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-3.3.1: Software/Hardware Supply Chain Risk Assessment | 2 | Process | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| GV-3.3.2: Critical Component/Vendor Dependency Mapping | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| GV-3.3.3: Supply Chain Risk Finding Remediation Tracking | 2 | Process | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### GV-3.4: Hardware and Firmware Provenance Verification

**Selected Tool / Product / Service:** Jira Software Data Center, Blancco Drive Eraser, the aircraft and ground equipment manufacturer's tools, Jira Service Management Assets

**Environment-Specific Tailoring:** Data center hardware and HSMs are inspected at receipt from Phase 1. Aircraft and stations are inspected at receipt and rescanned for counterfeit avionics under CCSD tailoring action 4 from Phase 3, when the fleet arrives. Suspect parts are quarantined and reported to GIDEP. Each verified firmware version is recorded in Assets, and Blancco sanitizes retired drives.

**Accountable Team:** Platform Team, with Fleet Operations

**Dependencies:** GV-3.1, DI-1.1, Aircraft and ground equipment manufacturers

**Funding Line:** FY27 and FY28 O&M, platform and security operations, with the fleet slice as RDT&E fleet integration, with the Phase 3 share pending approval

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C30](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-3.4.1: Trusted Supplier and Authorized Reseller Sourcing Requirements | 1 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| GV-3.4.2: Counterfeit and Tamper Detection at Receipt | 1 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| GV-3.4.3: Periodic Counterfeit Component Rescan | 2 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| GV-3.4.4: Firmware Provenance and Integrity Verification | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| GV-3.4.5: Component Disposal and Sanitization Verification | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** GV-3.4.1 and GV-3.4.2: Phase 1 receives the HSMs, firewalls, and workstations, so receipt inspection must exist first.

### GV-3.5: Supply Chain Risk Management Plan (SCRM)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** The supply chain lead authors the SCRM plan in Confluence, and the CCB approves it. It is revised each year and whenever a Tier 1 supplier changes.

**Accountable Team:** Program Office (supply chain lead)

**Dependencies:** GV-3.1, GV-2.1

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-3.5.1: SCRM Development and Authoring | 2 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| GV-3.5.2: SCRM Review and Approval | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-3.5.3: SCRM Periodic Review and Revision | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## GV-4: AI/ML Governance

### GV-4.1: AI/ML Use Case Inventory

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center, Jira Service Management Assets

**Environment-Specific Tailoring:** The inventory is a Jira project, open from Phase 1 so the board can tier the first use cases. Each use case links to the Assets records of the model versions it runs on. Platform models are listed with their sponsor and removal review date. Vendor and platform models link from Phase 2, and certified versions as they register in Phase 3. The quarterly sweep reads Azure AI service usage and the procurement records.

**Accountable Team:** Program Office (chief engineer)

**Dependencies:** GV-1.2

**Funding Line:** FY27 and FY28 program management

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-4.1.1: AI/ML Use Case Discovery and Inventory Intake Process | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.1.2: Risk Tiering Methodology and Criteria Definition | 1 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.1.3: Inventory Periodic Review and Reassessment | 1 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.1.4: Use Case to Model Linkage | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### GV-4.2: Program-Level AI Threat Assessment

**Selected Tool / Product / Service:** Threagile (the program's custom image, with IL5 and ATLAS risk rules), Confluence Data Center

**Environment-Specific Tailoring:** The PMO ISSE maps the AI estate's trust zones in Threagile each year, including both agents and the foundation model's use cases. The ATLAS ranking goes to the review board and feeds each model's threat model.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** GV-4.1

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-4.2.1: AI Program Architecture and Trust Zone Mapping | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.2.2: MITRE ATLAS Program-Level Threat Ranking | 2 | Process | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| GV-4.2.3: Assessment Review, Distribution, and Consumption | 2 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### GV-4.3: Responsible AI Policy and Principles

**Selected Tool / Product / Service:** Confluence Data Center, Joint Knowledge Online training

**Environment-Specific Tailoring:** The responsible AI policy commits that no model commands an aircraft and that a person approves every agent action affecting a flight. Each principle maps to the AI outcomes that enforce it, and the policy joins user training.

**Accountable Team:** Program Office (chief engineer)

**Dependencies:** GV-4.4

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-4.3.1: Responsible AI Policy Development | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.3.2: Principle-to-Control Mapping | 2 | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.3.3: Policy Publication and Awareness | 2 | Process | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### GV-4.4: AI/ML Governance Review Board

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center

**Environment-Specific Tailoring:** The program office charters the AI/ML Governance Review Board in late Phase 1, so it can approve the first use cases before training starts. Until GV-4.2 and GV-4.3 arrive in Phase 2, the board judges use cases against the AISP. It admits a platform model for experimentation only. If no use case is certified on it by its recorded date, the board reviews it for removal.

**Accountable Team:** Program Office (chief engineer)

**Dependencies:** GV-1.5, GV-4.1

**Funding Line:** FY27 and FY28 program management

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-4.4.1: Review Board Charter and Membership Definition | 1 (pinned) | Documentation | None | Level 2 | One-Time | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.4.2: Use-Case Review/Approval Workflow | 1 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.4.3: Review Board Decision Tracking and Escalation | 1 (pinned) | Process | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.4.4: AI/ML Governance Posture Report | 2 | Process | None | Level 2 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** GV-4.4.1, GV-4.4.2, and GV-4.4.3: KESTREL's design depends on it from the first build, since the review board approves the first AI use cases before Phase 2.

### GV-4.5: AI/ML Regulatory Mapping (NIST AI RMF, DoD RAI)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** The PMO ISSE maps each use case against the DoD AI Cybersecurity Risk Management Tailoring Guide and the NIST AI RMF in Confluence. A new AI directive is assessed within a quarter of issue.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** GV-4.1, DoD and NIST AI guidance

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-4.5.1: Regulatory/Framework Requirement Mapping and Gap Analysis | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| GV-4.5.2: Control-to-Requirement Traceability Maintenance | 2 | Documentation | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.5.3: AI Regulatory Landscape Monitoring and Update Process | 2 | Process | None | Level 2 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### GV-4.6: AI/ML Vendor/Model Risk Assessment

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center, Jira Service Management Assets

**Environment-Specific Tailoring:** The board treats each AI supplier finding, and any accepted supplier risk routes through RK-1.4. Azure OpenAI is registered in Assets once its risk is treated. Each use case certified on it is then added, including the coding agent.

**Accountable Team:** Program Office (chief engineer)

**Dependencies:** GV-4.4, GV-3.1, RK-1.4, IL5 cloud provider

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-4.6.1: Vendor AI/ML Risk Tiering and Organizational Risk Acceptance Workflow | 2 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.6.2: Governance-Level Risk Assessment Findings Escalation and Remediation Tracking | 2 | Process | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-4.6.3: Third-Party Model Registration in Authoritative Inventory | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## GV-5: Authorization Management

### GV-5.1: Security Architecture and Design Document (SADD)

**Selected Tool / Product / Service:** GitLab Ultimate, Confluence Data Center

**Environment-Specific Tailoring:** The SADD is built from the CCSD and the SABER in GitLab, with intents written by hand. The AO approves it as the design basis, and it is rebuilt whenever the CCSD, the system description, or the SABER version changes.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** GV-5.4

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.1.1: SADD Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| GV-5.1.2: SADD Review and Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.1.3: SADD Periodic Review and Revision | 1 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### GV-5.2: Security Implementation Plan

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center, GitLab Ultimate

**Environment-Specific Tailoring:** This plan is built from the SADD in GitLab, and its records load into Jira as stories and sub-tasks. The program manager approves each revision, and it is revised each quarter from Phase 1.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** GV-5.1

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.2.1: Security Implementation Plan Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| GV-5.2.2: Security Implementation Plan Review and Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.2.3: Security Implementation Plan Periodic Review and Revision | 1 | Documentation | None | Level 1 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### GV-5.3: System Security Plan (SSP)

**Selected Tool / Product / Service:** eMASS, Confluence Data Center, compliance-trestle (OSCAL)

**Environment-Specific Tailoring:** The ISSM drafts the SSP in OSCAL with Trestle from the first version, and publishes it to eMASS. The AO approves an initial SSP before the interim authorization to test, and the full one with the package.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.1, GV-1.2

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished and open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.3.1: SSP Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | Extensive | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| GV-5.3.2: SSP Review and Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.3.3: SSP Periodic Review and Revision | 2 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.3.4: SSP Machine-Readable Authoring/Maintenance | 1 (pinned) | Technical | Automate | Level 3 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

**Pinned:** GV-5.3.3: Its first review cannot fall in Phase 1, since the document it reviews is approved there. GV-5.3.4: The SSP is kept in OSCAL from its first draft, since converting it later costs far more.

### GV-5.4: Categorization and Control Selection Document (CCSD)

**Selected Tool / Product / Service:** Confluence Data Center, eMASS

**Environment-Specific Tailoring:** The CCSD lists the 18 information types and the tailoring actions. Version 1.0 is approved, and 1.1 is in SCA review. It is revised whenever an information type, interconnection, or boundary changes, including a slip of tailoring action 3.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** GV-1.2

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.4.1: Information Type Identification and Inventory | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.4.2: Provisional Impact Value Assignment per Information Type | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.4.3: CCSD Periodic Update | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.4.4: Control Selection and Tailoring Draft | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### GV-5.5: Security Categorization

**Selected Tool / Product / Service:** eMASS

**Environment-Specific Tailoring:** The categorization is High for confidentiality and integrity and Moderate for availability, by CNSSI 1253's high-water mark over the CCSD's information types. It is reassessed with every CCSD revision.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** GV-5.4

**Funding Line:** FY27 and FY28 program management

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** None. Government-furnished, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.5.1: System-Level CIA Impact Determination | 1 | Process | None | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.5.2: Categorization Documentation and AO Concurrence | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.5.3: Categorization Periodic Reassessment | 2 (pinned) | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** GV-5.5.3: Its first review cannot fall in Phase 1, since the document it reviews is approved there.

### GV-5.6: System Interconnection Agreements (ISA/MOU/MOA)

**Selected Tool / Product / Service:** Confluence Data Center, eMASS

**Environment-Specific Tailoring:** Each signed agreement is stored in Confluence and recorded in eMASS. The CSSP and access point agreements are signed in Phase 1 for the interim authorization to test. Partner nation agreements follow before their first release. Each is reviewed each year and whenever its connection changes.

**Accountable Team:** Program Office

**Dependencies:** GV-1.2, Cyber defense service provider, Cross domain service provider and IL6 enclave AO, Partner nations, Performer, DoD PKI and External Certificate Authorities, DNS threat feed vendor, Paging service, Parent organization's managed devices

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.6.1: Interconnecting System Identification and Boundary Documentation | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.6.2: ISA/MOU/MOA Development and Signatory Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| GV-5.6.3: Interconnection Agreement Periodic Review and Renewal | 1 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### GV-5.7: Authorization to Operate (ATO) Process

**Selected Tool / Product / Service:** eMASS, Jira Software Data Center

**Environment-Specific Tailoring:** The interim authorization to test covers spare aircraft and the simulator, the access point and CSSP connections, and the prior collection admitted over F28. Its conditions are tracked to closure in the POA&M from Phase 1. The ISSM submits the full package in eMASS for the ATO decision on 2028-09-30.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.3, GV-5.4, GV-5.6, GV-5.12, RS-4.1, RK-1.8

**Funding Line:** FY27 and FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.7.1: ATO Package Submission | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.7.2: AO Risk Determination and Adjudication Tracking | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| GV-5.7.3: ATO Condition/POA&M Closure Tracking | 1 (pinned) | Process | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.7.4: Interim Authorization to Test | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** GV-5.7.3: Conditions of the interim authorization to test are tracked to closure from Phase 1. GV-5.7.4: The interim authorization to test covers Phases 1 to 3, so it is granted before Phase 1 testing starts.

### GV-5.8: Authorization Package Compilation

**Selected Tool / Product / Service:** eMASS, compliance-trestle (OSCAL), Confluence Data Center

**Environment-Specific Tailoring:** The ISSM compiles the package in eMASS once the SAR and RAR arrive, with the SSP and SCTM exported from Trestle. The model evidence annex comes from each model's AI Cyber T&E record. The PMO ISSE attests that the package matches what was built.

**Accountable Team:** Security Team (ISSM), with the PMO ISSE for the attestation

**Dependencies:** GV-5.3, GV-5.9, RK-1.6, RK-1.7, RK-1.8, AI-6.1

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-09-15

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished and open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.8.1: Authorization Package Artifact Inventory and Collection | 3 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.8.2: Authorization Package Completeness/Quality Review | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.8.3: Authorization Package Version Control and Submission Packaging | 3 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.8.4: Package Accuracy Attestation | 3 | Documentation | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.8.5: Model Assessment Evidence Annex | 3 | Documentation | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### GV-5.9: Security Controls Traceability Matrix (SCTM)

**Selected Tool / Product / Service:** compliance-trestle (OSCAL), eMASS

**Environment-Specific Tailoring:** The SCTM is kept in OSCAL with Trestle from its first version. Each row carries the control to its SADD outcome, its SSP implementation, its inheritance, and its evidence. It is validated against the SSP before each submission.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.4, GV-5.3

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** None. Government-furnished and open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.9.1: SCTM Development | 1 | Documentation | None | Level 1 | One-Time | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| GV-5.9.2: SCTM Review and Validation against SSP | 1 | Process | None | Level 1 | Periodic (Semi-Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.9.3: SCTM Periodic Update | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.9.4: SCTM Automation via Machine-Readable Format (OSCAL) for Tool-Based Control Traceability | 1 (pinned) | Technical | Automate | Level 3 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

**Pinned:** GV-5.9.4: The SCTM is kept in OSCAL from its first version, since converting it later costs far more.

### GV-5.10: Ongoing Authorization

**Selected Tool / Product / Service:** eMASS, Splunk Enterprise

**Environment-Specific Tailoring:** The reauthorization triggers are agreed for the interim authorization to test in Phase 1. They include a slip of the replacement payload processing workstation past 2027-09-30 and tailoring action 6's annual review. Splunk feeds monitoring results into the ISSM's posture view from Phase 3, and the AO receives status each quarter.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.7.3, GV-5.7.4, CO-2.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.10.1: Continuous Monitoring Data Feed into Authorization Posture | 3 | Process | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.10.2: Risk-Based Reauthorization Trigger Criteria | 1 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.10.3: Periodic Authorization Status Reporting | 1 (pinned) | Process | None | Level 1 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** GV-5.10.2 and GV-5.10.3: The interim authorization to test runs from Phase 1, so its triggers, including CCSD tailoring action 3's 2027-09-30 date, are watched from then.

### GV-5.11: Security Impact Analysis (SIA)

**Selected Tool / Product / Service:** Jira Service Management Data Center, Jira Software Data Center, GitLab Ultimate, Confluence Data Center

**Environment-Specific Tailoring:** Every change process feeds one intake in Jira Service Management, including fleet maintenance changes. Pipeline releases and retraining within the approved envelope are classified automatically from GitLab. Significant changes go to the SCA and the AO before they are made.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.9, GV-1.5

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.11.1: SIA Intake and Change Classification | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.11.2: Security and Privacy Impact Determination and SIA Record | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.11.3: Significance Determination and Authorization Routing | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.11.4: Post-Change Control Verification | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### GV-5.12: Inherited Control Validation

**Selected Tool / Product / Service:** eMASS, Confluence Data Center

**Environment-Specific Tailoring:** The ISSM confirms each provider's authorization is current before KESTREL inherits from it. Azure services, including Application Gateway private deployment and the isolated GPU size and its quota, are checked against Azure Government's IL5 audit scope in both US Gov regions. The Microsoft 365 DoD tenant, the access point, DoD PKI, the CSSP, the cross domain provider, and the alternate site's facility are checked against their own authorizations. Microsoft's approval of modified content filtering is tracked here too, and status is checked each quarter from Phase 1.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.4, IL5 cloud provider, Microsoft 365 DoD tenant, Boundary Cloud Access Point, DoD PKI, Cyber defense service provider, Cross domain service provider, Parent organization's alternate site

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| GV-5.12.1: Provider Authorization Verification | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.12.2: Customer Responsibility Matrix Integration into the SCTM | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| GV-5.12.3: Provider Authorization Status Monitoring | 1 | Process | None | Level 1 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| GV-5.12.4: Reciprocity and Joint Authorization Terms | 2 | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
