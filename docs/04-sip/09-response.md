# RS: Response

*KESTREL Security Implementation Plan, Section 4 (Operate). Each record implements the outcome of the same ID in the [SADD](../03-sadd/09-response.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## RS-1: Incident Preparation

### RS-1.1: Incident Response Development

**Selected Tool / Product / Service:** Confluence Data Center, Jira Service Management Data Center, Splunk SOAR

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** DE-3.1, Cyber defense service provider

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

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** DE-3.1, Cyber defense service provider

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

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** DE-3.1, Cyber defense service provider

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-1.3.1: Tabletop Exercise Planning and Facilitation | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.3.2: Functional Incident Response Exercise Execution | 2 | Process | None | Level 2 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| RS-1.3.3: Exercise Findings and Plan Update Tracking | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RS-1.4: Security Contact Information

**Selected Tool / Product / Service:** Microsoft Defender for Cloud, Microsoft Entra ID

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** DE-3.1, Cyber defense service provider

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

**Selected Tool / Product / Service:** Jira Service Management Data Center, Splunk SOAR

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** DE-3.1, Cyber defense service provider, Paging service

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-1.5.1: Incident Notification Channel Configuration | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| RS-1.5.2: Monitoring Platform and Event Streaming Integration | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### RS-1.6: Incident Reporting and External Communications

**Selected Tool / Product / Service:** Jira Service Management Data Center, Confluence Data Center, the CSSP

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** DE-3.1, Cyber defense service provider

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-1.6.1: Regulatory/AO Incident Reporting Workflow and Timelines | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.6.2: External Stakeholder and Authority Notification Procedures | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.6.3: Vendor and Supply Chain Incident-Handling Coordination | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-1.6.4: Cross-Organization Correlation and Incident Information Sharing | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RS-1.7: Cyber Defense Service Provider Alignment

**Selected Tool / Product / Service:** Splunk SOAR containment playbooks under the CSSP agreement, Splunk Enterprise, Azure Virtual Desktop

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** DE-3.1

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

**Selected Tool / Product / Service:** Splunk Enterprise Security, Jira Service Management Data Center, Velociraptor

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, DI-1.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-2.1.1: Automated Incident Ticket Creation from Correlated Detection Alerts | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-2.1.2: Automated Context/Asset Enrichment | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-2.1.3: XDR/SIEM-to-ITSM Integration for Incident Record Creation | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |

### RS-2.2: Incident-Scoped Log Analysis and Investigation

**Selected Tool / Product / Service:** Splunk Enterprise Security, Jira Service Management Data Center, Velociraptor

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, DI-1.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-2.2.1: Alert-to-Incident Correlation and Deduplication | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-2.2.2: Investigative Log Query and Collection | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-2.2.3: SIEM-Based Investigation Workbench Usage | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RS-2.3: Evidence Preservation and Forensic Capabilities

**Selected Tool / Product / Service:** Velociraptor, NetApp StorageGRID with S3 Object Lock, Microsoft Defender XDR

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, DI-1.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C16](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-2.3.1: Evidence Collection Automation | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| RS-2.3.2: Forensic Analysis Tools Integration | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| RS-2.3.3: Immutable Evidence Storage | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| RS-2.3.4: Compliance and Legal Requirements | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RS-2.4: Asset Criticality and Business Impact Assessment

**Selected Tool / Product / Service:** Splunk Enterprise Security, Jira Service Management Data Center, Velociraptor

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, DI-1.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-2.4.1: Business Impact Classifications | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-2.4.2: Business Impact Scoring Integration into Incident Prioritization | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### RS-2.5: Automated Severity Scoring and Escalation

**Selected Tool / Product / Service:** Splunk Enterprise Security, Jira Service Management Data Center, Velociraptor

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, DI-1.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-2.5.1: Severity Scoring Model Definition | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-2.5.2: AI Incident Type Taxonomy and Severity Mapping | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-2.5.3: Automated Escalation Routing and Paging | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-2.5.4: Incident Response Metrics Dashboard | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## RS-3: Incident Containment, Recovery, and Lessons Learned

### RS-3.1: SOAR Capabilities

**Selected Tool / Product / Service:** Splunk SOAR, Splunk SOAR containment playbooks under the CSSP agreement

**Environment-Specific Tailoring:** Splunk SOAR runs the playbooks and updates Jira Service Management at each step. Its service identity can take only the listed actions. The CSSP runs the containment playbooks from its host pool, and each run pages the Security Team.

**Accountable Team:** Security Team

**Dependencies:** RS-1.1, RS-1.7, DE-3.1

**Funding Line:** FY28 and FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C31](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-3.1.1: SOAR Playbook Development and Automation Configuration | 4 | Technical | Automate | Level 3 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| RS-3.1.2: SOAR-to-SIEM/Ticketing Integration | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-3.1.3: Automated Response Action Approval Workflow | 2 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### RS-3.2: Automated Containment and Isolation Procedures

**Selected Tool / Product / Service:** Splunk SOAR, Panorama with the PAN-OS provider for OpenTofu, Cisco ACI and APIC, Microsoft Entra ID, Microsoft Defender XDR

**Environment-Specific Tailoring:** Panorama moves a cloud workload into a quarantine policy, and ACI moves a data center host into a quarantine endpoint group. Entra ID and Defender XDR disable accounts and revoke sessions. The Security Team approves before either touches production, except a CSSP playbook run when an incident cannot wait, which pages it.

**Accountable Team:** Security Team

**Dependencies:** RS-3.1, DI-5.5

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-3.2.1: Network Isolation Automation | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| RS-3.2.2: Account and Access Control Automation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### RS-3.3: Human-in-the-Loop Containment

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** The IRP's fleet section sets the airborne rule, the operations lead's approval, and the time limit on cutting a site's conduit. Fleet containment is manual and run by Fleet Operations.

**Accountable Team:** Fleet Operations, with the Security Team

**Dependencies:** RS-1.1

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

**Selected Tool / Product / Service:** Splunk SOAR, Azure Key Vault Premium, CyberArk Privileged Access Manager, JFrog Artifactory, Entrust nShield 5 HSMs

**Environment-Specific Tailoring:** Owning teams eradicate at the ISSM's direction, rotating every touched credential through Key Vault and CyberArk. Artifactory blocks a withdrawn model version. A compromised signing key is revoked and every package re-signed, and a lost aircraft's datalink keys are superseded fleet-wide.

**Accountable Team:** Owning teams, at the ISSM's direction

**Dependencies:** RS-3.2, DA-3.9

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references)

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

**Dependencies:** RS-1.1, DA-1.1

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

**Selected Tool / Product / Service:** Veeam Data Platform, JFrog Artifactory, Splunk Enterprise Security

**Environment-Specific Tailoring:** Restores come only from Veeam copies and Artifactory versions older than the earliest confirmed activity, each checked for the incident's indicators. Without a clean source, systems are rebuilt from OpenTofu and golden images. Splunk watches a recovered system closely for 30 days.

**Accountable Team:** Security Team

**Dependencies:** RC-1.2, RS-3.4

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C15](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

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

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** GV-5.1, RS-1.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| RS-4.1.1: IRP Development and Authoring | 2 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| RS-4.1.2: IRP Review and Approval | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| RS-4.1.3: IRP Periodic Review and Revision | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
