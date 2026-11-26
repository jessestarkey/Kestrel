# RS: Response

*KESTREL Security Implementation Plan, Section 4 (Operate). Each record implements the outcome of the same ID in the [SADD](../03-sadd/09-response.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## RS-1: Incident Preparation

### RS-1.1: Incident Response Development

**Selected Tool / Product / Service:** Confluence Data Center, Jira Service Management Data Center, Splunk SOAR

**Environment-Specific Tailoring:** Cloud runbooks use the provider's native response actions. Fleet runbooks are written with Fleet Operations and follow the airborne rule in RS-3.3. A lost aircraft's datalink keys are superseded fleet-wide.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** DE-3.1, Cyber defense service provider, IL5 cloud provider

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-1.1.1: Cloud Platform-Native Incident Response Runbook Development | 2 | Documentation | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| RS-1.1.2: Cloud-Native Threat Protection Platform Integration | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| RS-1.1.3: AI/ML Incident Runbook Development | 2 | Documentation | None | Level 1 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### RS-1.2: Incident Response Team Structure and Training

**Selected Tool / Product / Service:** Confluence Data Center, Jira Service Management Data Center, Splunk SOAR

**Environment-Specific Tailoring:** The ISSM leads every incident in Jira Service Management, and the CSSP contains what cannot wait through its playbooks. The Platform Team, IT Operations, the Data Team, and Fleet Operations act on their own systems at the ISSM's direction. Responders train on KESTREL's runbooks in the exercise environment each year.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** RS-4.1, Cyber defense service provider

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-1.2.1: Organize Team Structure | 2 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.2.2: Develop Team Training | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| RS-1.2.3: AI Incident Escalation Path and Model Owner Accountability | 2 | Process | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.2.4: Response Capability Resourcing and Management Support | 2 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RS-1.3: Incident Response Plan Testing and Exercises

**Selected Tool / Product / Service:** Confluence Data Center, Jira Service Management Data Center, Splunk SOAR

**Environment-Specific Tailoring:** A tabletop runs twice a year, one with an aircraft or ground segment scenario and one with an AI scenario. The yearly functional exercise uses the real tools with the CSSP and the CP's owners. Fleet systems join only by simulator or discussion.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** RS-4.1, RC-4.1, Cyber defense service provider

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-1.3.1: Tabletop Exercise Planning and Facilitation | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.3.2: Functional Incident Response Exercise Execution | 3 (pinned) | Process | None | Level 2 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| RS-1.3.3: Exercise Findings and Plan Update Tracking | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** RS-1.3.2: Moved later to even out the Security Team, which carries most of Phase 2. The functional exercise waits until the fleet and agents exist to rehearse against. The Phase 2 tabletop stays.

### RS-1.4: Security Contact Information

**Selected Tool / Product / Service:** Microsoft Defender for Cloud, Microsoft Entra ID

**Environment-Specific Tailoring:** Defender for Cloud's security contact on every subscription and the tenant is the Security Team's monitored address and the CSSP's operations center. The Security Team checks them each quarter.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** Cyber defense service provider, IL5 cloud provider

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-1.4.1: Cloud-Native Threat Protection Platform Security Contact Configuration | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| RS-1.4.2: Security Contact Information Review and Update Cadence | 2 | Process | None | Level 2 | Periodic (Semi-Annual) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### RS-1.5: Automated Notification Workflows

**Selected Tool / Product / Service:** Jira Service Management Data Center, Splunk SOAR, the paging service

**Environment-Specific Tailoring:** A declared incident pages the on-call analyst through Jira Service Management and notifies the CSSP's operations center. Severe incidents also page the ISSM and the affected team's lead. If the service desk or the circuits are down, Splunk pages directly over F29 with only an incident ID and severity.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** DE-3.1, Cyber defense service provider, Paging service

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C33](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-1.5.1: Incident Notification Channel Configuration | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RS-1.5.2: Monitoring Platform and Event Streaming Integration | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### RS-1.6: Incident Reporting and External Communications

**Selected Tool / Product / Service:** Jira Service Management Data Center, Confluence Data Center, the CSSP

**Environment-Specific Tailoring:** The ISSM notifies the AO, and the CSSP reports up the DoD chain. The foreign disclosure officer notifies partner nations, and the privacy officer reports breaches of personal information. The performer reports incidents on its laptops to DC3.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** DE-3.1, Cyber defense service provider, Partner nations, DoD component privacy office, DoD intelligence producers and DC3's DIB Cybersecurity program, Performer laptops and device management

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-1.6.1: Regulatory/AO Incident Reporting Workflow and Timelines | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.6.2: External Stakeholder and Authority Notification Procedures | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.6.3: Vendor and Supply Chain Incident-Handling Coordination | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.6.4: Cross-Organization Correlation and Incident Information Sharing | 3 (pinned) | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** RS-1.6.4: Moved later to even out the Security Team, which carries most of Phase 2. Sharing with other organizations follows a working internal intelligence feed.

### RS-1.7: Cyber Defense Service Provider Alignment

**Selected Tool / Product / Service:** Splunk SOAR containment playbooks under the CSSP agreement, Splunk Enterprise, Azure Virtual Desktop

**Environment-Specific Tailoring:** The CSSP monitors around the clock, triages, and runs the pre-approved containment playbooks from its AVD host pool. Splunk forwards all telemetry to it, and a stalled feed alerts. The ISSM tracks each CSSP directive to completion in Jira Service Management.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** DE-3.1, ID-4.1, Cyber defense service provider

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C31](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-1.7.1: Provider Service Agreement and Responsibility Division | 1 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.7.2: Telemetry and Sensor Delivery to the Provider | 1 (pinned) | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-1.7.3: Provider Incident Reporting and Directive Handling | 1 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.7.4: Automated Provider Advisory and Assistance Access | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** RS-1.7.1 and RS-1.7.2: The access point connection and the interim authorization to test need CSSP alignment in Phase 1. RS-1.7.3: A system connected under the interim authorization to test must report incidents to the CSSP and act on its directives.

## RS-2: Incident Detection, Analysis, and Investigation

### RS-2.1: Automated Incident Creation and Enrichment

**Selected Tool / Product / Service:** Splunk Enterprise Security, Jira Service Management Data Center

**Environment-Specific Tailoring:** Correlated Splunk Enterprise Security alerts above the declaration threshold open an incident in Jira Service Management automatically. Each record carries the asset's owner, team, criticality, and recent changes from Assets.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, DI-1.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-2.1.1: Automated Incident Ticket Creation from Correlated Detection Alerts | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-2.1.2: Automated Context/Asset Enrichment | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-2.1.3: XDR/SIEM-to-ITSM Integration for Incident Record Creation | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |

### RS-2.2: Incident-Scoped Log Analysis and Investigation

**Selected Tool / Product / Service:** Splunk Enterprise Security, Jira Service Management Data Center

**Environment-Specific Tailoring:** Analysts investigate in Splunk Enterprise Security and save queries and findings with the Jira Service Management record. Owning teams raise logging within an hour of a request. On fleet equipment, logging changes go only through the vendor's engineering path with Fleet Operations' concurrence.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, DI-1.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-2.2.1: Alert-to-Incident Correlation and Deduplication | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-2.2.2: Investigative Log Query and Collection | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-2.2.3: SIEM-Based Investigation Workbench Usage | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RS-2.3: Evidence Preservation and Forensic Capabilities

**Selected Tool / Product / Service:** Microsoft Defender XDR, Splunk SOAR, NetApp StorageGRID with S3 Object Lock

**Environment-Specific Tailoring:** Defender XDR live response collects memory and files under the EDR responder role, and a playbook takes cloud disk snapshots. Evidence goes to a retention-locked StorageGRID bucket only the Security Team can read, excluded from replication. Analysts examine copies on an isolated forensic workstation that cannot reach production. Fleet equipment is imaged only in maintenance windows or after landing, and crypto modules and HSMs never.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, DI-1.3, DI-5.5

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-2.3.1: Evidence Collection Automation | 3 (pinned) | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| RS-2.3.2: Forensic Analysis Tools Integration | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| RS-2.3.3: Immutable Evidence Storage | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| RS-2.3.4: Compliance and Legal Requirements | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** RS-2.3.1: Moved later to even out the Security Team, which carries most of Phase 2. Phase 2 collects evidence by hand under the IRP, and automation follows once the playbooks have run.

### RS-2.4: Asset Criticality and Business Impact Assessment

**Selected Tool / Product / Service:** Jira Service Management Assets, Splunk Enterprise Security, Jira Service Management Data Center

**Environment-Specific Tailoring:** Each asset's criticality comes from its Assets tags and the business impact analysis. The command link, the stations, the identity provider, the HSMs and PKI, and the signing and registry path rank highest. Criticality feeds incident severity in Splunk Enterprise Security.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, DI-1.3, RK-3.2

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-2.4.1: Business Impact Classifications | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-2.4.2: Business Impact Scoring Integration into Incident Prioritization | 3 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** RS-2.4.2: Moved later to even out the Security Team, which carries most of Phase 2. The business impact analysis completes in Phase 2, so its scores feed prioritization after that.

### RS-2.5: Automated Severity Scoring and Escalation

**Selected Tool / Product / Service:** Splunk Enterprise Security, Jira Service Management Data Center, the paging service

**Environment-Specific Tailoring:** Severity is computed from criticality, data sensitivity, scope, and any effect on an aircraft. The AI taxonomy covers poisoning, prompt injection, model theft, agent misuse, and a tampered edge model. Each severity has its own paging route, and a Splunk dashboard tracks time to triage, contain, and recover.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, RS-2.4, Paging service

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), [C33](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-2.5.1: Severity Scoring Model Definition | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-2.5.2: AI Incident Type Taxonomy and Severity Mapping | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-2.5.3: Automated Escalation Routing and Paging | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-2.5.4: Incident Response Metrics Dashboard | 3 (pinned) | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** RS-2.5.4: Moved later to even out the Security Team, which carries most of Phase 2. The metrics dashboard needs incident history to show anything.

## RS-3: Incident Containment, Recovery, and Lessons Learned

### RS-3.1: SOAR Capabilities

**Selected Tool / Product / Service:** Splunk SOAR, Splunk SOAR containment playbooks under the CSSP agreement, the paging service

**Environment-Specific Tailoring:** Splunk SOAR runs the playbooks and updates Jira Service Management at each step. Its service identity can take only the listed actions. The CSSP runs the containment playbooks from its host pool, and each run pages the Security Team.

**Accountable Team:** Security Team

**Dependencies:** RS-1.1, RS-1.7, DE-3.1, Paging service

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C31](index.md#6-contracting-and-procurement-cross-references), [C33](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-3.1.1: SOAR Playbook Development and Automation Configuration | 2 (pinned) | Technical | Automate | Level 3 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| RS-3.1.2: SOAR-to-SIEM/Ticketing Integration | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-3.1.3: Automated Response Action Approval Workflow | 2 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** RS-3.1.1: Containment playbooks run from Phase 2, for RS-3.2 and under the CSSP agreement, so they must be built then.

### RS-3.2: Automated Containment and Isolation Procedures

**Selected Tool / Product / Service:** Splunk SOAR, Splunk SOAR containment playbooks under the CSSP agreement, Panorama with the PAN-OS provider for OpenTofu, Cisco ACI and APIC, Microsoft Entra ID, Microsoft Defender XDR

**Environment-Specific Tailoring:** Panorama moves a cloud workload into a quarantine policy, and ACI moves a data center host into a quarantine endpoint group. Entra ID and Defender XDR disable accounts and revoke sessions. The Security Team approves before a playbook touches production, except a CSSP run when an incident cannot wait. No playbook touches fleet systems or the operating sites' admission control.

**Accountable Team:** Security Team

**Dependencies:** RS-3.1, DI-5.5

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C31](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-3.2.1: Network Isolation Automation | 3 (pinned) | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| RS-3.2.2: Account and Access Control Automation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** RS-3.2.1: Moved later to even out the Security Team, which carries most of Phase 2. Phase 2 isolates networks by hand, with device isolation and account automation in place, and network automation follows once the playbooks have run.

### RS-3.3: Human-in-the-Loop Containment

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** The IRP's fleet section sets the airborne rule, the operations lead's approval, and the time limit on cutting a site's conduit. Fleet containment is manual and run by Fleet Operations.

**Accountable Team:** Fleet Operations, with the Security Team

**Dependencies:** RS-1.1, NE-1.6

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-3.3.1: OT/Safety-Critical Asset Containment-Action Risk Classification | 2 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-3.3.2: Human Approval Workflow Routing to OT/Plant Operations Personnel | 2 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-3.3.3: Pre-Approved Manual Containment Runbook | 2 | Documentation | None | Level 2 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### RS-3.4: Eradication and Threat Removal

**Selected Tool / Product / Service:** Azure Key Vault Premium, CyberArk Privileged Access Manager, JFrog Artifactory, Entrust nShield 5 HSMs

**Environment-Specific Tailoring:** Owning teams eradicate at the ISSM's direction, rotating every touched credential through Key Vault and CyberArk. Fleet Operations eradicates only in a maintenance window or after landing. Artifactory blocks a withdrawn model version. A compromised signing key is revoked and every package re-signed, and a lost aircraft's datalink keys are superseded fleet-wide.

**Accountable Team:** Owning teams, at the ISSM's direction

**Dependencies:** RS-3.2, DA-3.9

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-3.4.1: Malware/Attacker-Artifact Removal and Persistence Eradication | 2 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-3.4.2: Post-Compromise Credential and Secret Reset/Rotation | 2 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-3.4.3: Exploited-Vulnerability Closure Verification | 2 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RS-3.5: Classified Data Spillage Response

**Selected Tool / Product / Service:** Self-hosted OpenMetadata, Splunk Enterprise Security, Confluence Data Center

**Environment-Specific Tailoring:** The ISSM traces every copy with OpenMetadata and Splunk. Owning teams sanitize their copies, and locked backups are sanitized by destroying their backup set's key. Copies stay held until the PSO and the AO release them.

**Accountable Team:** Security Team (ISSM), with the owning teams

**Dependencies:** RS-1.1, DA-1.1, RC-2.2, PSO, IL6 enclave owner, IL5 cloud provider

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-3.5.1: Spillage Identification and Scope Determination | 2 | Process | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-3.5.2: Spillage Containment and Access Suspension | 2 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| RS-3.5.3: Contaminated Media and System Sanitization | 2 | Process | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-3.5.4: Spillage Reporting and Authority Notification | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RS-3.6: Recovery and Return-to-Operations Validation

**Selected Tool / Product / Service:** Veeam Data Platform, JFrog Artifactory, OpenTofu, Packer, Splunk Enterprise Security

**Environment-Specific Tailoring:** Owning teams restore only from Veeam copies and Artifactory versions older than the earliest confirmed activity. The Security Team checks each source for the incident's indicators first. Without a clean source, systems are rebuilt from OpenTofu and Packer golden images. Splunk watches a recovered system closely for 30 days.

**Accountable Team:** Security Team

**Dependencies:** RC-1.2, RS-3.4

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), plus open source and source-available components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-3.6.1: Pre-Restoration Clean-State Verification | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-3.6.2: Post-Incident Heightened Monitoring | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RS-3.7: Systemic Lessons Learned Process

**Selected Tool / Product / Service:** Confluence Data Center, Jira Software Data Center

**Environment-Specific Tailoring:** Every incident of severity 2 or higher ends with a lessons-learned review in Confluence. Each finding becomes a Jira item, and design findings go to the PMO ISSE.

**Accountable Team:** Security Team

**Dependencies:** RS-1.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-3.7.1: Lessons Learned Framework | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-3.7.2: Improvement Implementation Tracking | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## RS-4: Incident Response Planning

### RS-4.1: Incident Response Plan (IRP)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** An interim IRP is approved in Phase 1 for the interim authorization to test. It covers declaring an incident, reporting to the CSSP, and who acts. The full IRP with its runbooks follows in Phase 2.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.1, Cyber defense service provider

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-4.1.1: IRP Development and Authoring | 1 (pinned) | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-4.1.2: IRP Review and Approval | 1 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-4.1.3: IRP Periodic Review and Revision | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** RS-4.1.1 and RS-4.1.2: The interim authorization to test needs an interim IRP, since the system reports incidents to the CSSP from Phase 1.
