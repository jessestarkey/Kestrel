# DE: Detection

*KESTREL Security Implementation Plan, Section 4 (Operate). Each record implements the outcome of the same ID in the [SADD](../03-sadd/08-detection.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## DE-1: Intelligent Detection Systems

### DE-1.1: Platform-Native Threat Detection

**Selected Tool / Product / Service:** Microsoft Defender for Cloud, Microsoft Defender for Identity, Microsoft Defender XDR

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-2.1, DE-2.5, DE-2.7, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-1.1.1: Platform-Native Detection Service Enablement and Tuning | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-1.1.2: Detection Capability Review | 2 | Process | None | Level 2 | Periodic (Semi-Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-1.1.3: Addressing Detection Gaps | 2 | Process | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DE-1.1.4: Alert Quality Optimization | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-1.1.5: Detection Coverage/MITRE ATT&CK Mapping Visualization Dashboard | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DE-1.2: Adversary Emulation and Detection Validation

**Selected Tool / Product / Service:** AttackIQ Enterprise, Splunk Enterprise Security

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-2.1, DE-2.5, DE-2.7, DE-3.1

**Funding Line:** FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 4, Maturity

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C18](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-1.2.1: Breach and Attack Simulation Platform Deployment | 4 | Technical | Automate | Level 3 | Continuous | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DE-1.2.2: Adversary Emulation Exercise Planning and Execution | 4 | Process | None | Level 2 | Periodic (Annual) | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DE-1.2.3: Purple Team Exercise Coordination | 4 | Process | None | Level 3 | Periodic (Semi-Annual) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-1.2.4: Detection Efficacy Findings and Remediation Tracking | 4 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DE-1.3: Correlated Threat Detection and Analytics

**Selected Tool / Product / Service:** Splunk Enterprise Security, Microsoft Defender XDR, GitLab Ultimate

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-2.1, DE-2.7, DE-3.1, RK-2.3

**Funding Line:** FY28 and FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-1.3.1: Security Telemetry Centralization | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DE-1.3.2: Unified XDR Platform Deployment | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DE-1.3.3: Custom XDR/Platform-Native Detection Rule Creation | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-1.3.4: Threat Intelligence Enrichment | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Short-term (1–3 months) |
| DE-1.3.5: Indicator of Compromise (IOC) Feed Management | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Short-term (1–3 months) |
| DE-1.3.6: Detection-Rule-as-Code / Version-Controlled Rule Deployment Pipeline | 4 | Technical | Automate | Level 3 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### DE-1.4: Enterprise Threat Hunting Program

**Selected Tool / Product / Service:** Splunk Enterprise Security, Microsoft Defender XDR

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-2.1, DE-2.5, DE-2.7, DE-3.1

**Funding Line:** FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 4, Maturity

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-1.4.1: Hunt Hypothesis Development and Prioritization | 4 | Process | None | Level 3 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-1.4.2: Cross-Source Hunt Execution | 4 | Process | None | Level 3 | Periodic (Monthly) | High | One-Time: Low; Recurring: High | Medium-term (3–6 months) |
| DE-1.4.3: Hunt Finding-to-Detection-Rule Conversion | 4 | Process | None | Level 3 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DE-1.5: Deception Technology

**Selected Tool / Product / Service:** Acalvio ShadowPlus

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-2.1, DE-2.5, DE-2.7, DE-3.1

**Funding Line:** FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 4, Maturity

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C17](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-1.5.1: Honeytoken and Canary Credential Deployment | 4 | Technical | None | Level 3 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-1.5.2: Decoy System/Honeypot Deployment | 4 | Technical | None | Level 3 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DE-1.5.3: Deception Trigger Alerting and Investigation Routing | 4 | Technical | None | Level 3 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DE-1.6: User/Entity Behavior Analytics (UEBA) / Insider Threat Detection

**Selected Tool / Product / Service:** Splunk Enterprise Security

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-2.1, DE-2.5, DE-2.7, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-1.6.1: Behavioral Baseline Profiling | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DE-1.6.2: Anomalous Behavior Alerting and Risk Scoring | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DE-1.6.3: Insider Threat Indicator Correlation and Investigation | 3 | Process | None | Level 2 | Continuous | High | One-Time: Moderate; Recurring: High | Medium-term (3–6 months) |

### DE-1.7: Network/OT Intrusion and Anomaly Detection

**Selected Tool / Product / Service:** Corelight sensors, Nozomi Networks Guardian, Palo Alto Threat Prevention with on-box signatures

**Environment-Specific Tailoring:** Corelight sensors watch the data center and the alternate site, and Palo Alto threat prevention watches the hubs. Nozomi sensors watch each operating site's ground segment once the fleet integrates in Phase 3.

**Accountable Team:** Security Team

**Dependencies:** DE-2.7, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C14](index.md#6-contracting-and-procurement-cross-references), [C13](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-1.7.1: Network Intrusion Detection System (NIDS) Deployment | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DE-1.7.2: OT/ICS-Aware Anomaly Detection | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DE-1.7.3: Anomaly Alert Triage and Escalation Workflow | 2 | Process | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### DE-1.8: Identity Threat Detection

**Selected Tool / Product / Service:** Microsoft Entra ID Protection, Microsoft Defender for Identity, Splunk Enterprise Security

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-2.1, DE-2.5, DE-2.7, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-1.8.1: Identity Audit Record Coverage Confirmation and Review | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-1.8.2: Authentication Activities Monitoring | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-1.8.3: Risky Sign-In Pattern Detection | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-1.8.4: Compromised Account Identification | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-1.8.5: SIEM Platform Integration | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-1.8.6: Cloud Infrastructure Identity Threat Monitoring | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-1.8.7: Identity Security Posture Scoring | 2 | Technical | Visualize | Level 2 | Periodic (Monthly) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

## DE-2: Comprehensive Logging

### DE-2.1: Infrastructure and Identity Logging

**Selected Tool / Product / Service:** Azure Monitor and VNet flow logs, Microsoft Entra ID, Splunk Enterprise, Azure Policy

**Environment-Specific Tailoring:** Azure Monitor diagnostic settings send every subscription's and the tenant's activity logs to Splunk over the circuits. Splunk forwarders collect the directory, SDN controller, hypervisor, BMC, and CyberArk logs on premises. Azure Policy and a Splunk source check flag any source missing its logging.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-2.1.1: Control-Plane Activity Log Collection Centralization | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.1.2: Consistent Logging Coverage Enforcement (infrastructure/identity sources) | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DE-2.1.3: Authentication Events Capture | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.1.4: Identity Change Tracking | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-2.1.5: Identity Log Retention Extension | 1 | Technical | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.1.6: Audit and Accountability Procedures | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DE-2.2: Data Service Logging

**Selected Tool / Product / Service:** Azure Monitor and VNet flow logs, Azure Policy, NetApp StorageGRID with S3 Object Lock, Splunk Enterprise

**Environment-Specific Tailoring:** Diagnostic settings enable data-plane logs on every cloud database, storage service, vault, and queue as the pipeline creates it, and Azure Policy flags any that lose them. StorageGRID audit logs cover every data lake zone. Splunk's own audit events are forwarded to the CSSP.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-2.2.1: Resource Level Data Plane Logs | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Short-term (1–3 months) |
| DE-2.2.2: Log Storage Operations | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-2.2.3: Database Activity Auditing | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.2.4: Secrets Access Monitoring | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.2.5: NoSQL Operations Tracking | 2 (pinned) | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.2.6: Other Data Services Coverage | 2 (pinned) | Technical | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DE-2.2.7: Data Service Logging Automation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DE-2.2.8: Consistent Logging Coverage Enforcement (data-service sources) | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DE-2.2.5 and DE-2.2.6: Coverage follows the data services and log sources, most of which arrive in Phase 2.

### DE-2.3: Container and Orchestration Platform Logging

**Selected Tool / Product / Service:** Azure Monitor and VNet flow logs, Defender for Containers, Splunk Enterprise

**Environment-Specific Tailoring:** AKS audit logs, Defender for Containers runtime events, and Artifactory registry events go to Splunk. The landing zone modules enable them when a cluster is created, and Azure Policy flags any that lose them. Azure Machine Learning sends its compute logs through its own diagnostic settings.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-2.3.1: Kubernetes Control Plane Logging | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.3.2: Container Runtime Monitoring | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DE-2.3.3: Container Image Tracking | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-2.3.4: Container and Orchestration Logging Automation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DE-2.3.5: Consistent Logging Coverage Enforcement (container/orchestration sources) | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DE-2.4: Application/API Logging

**Selected Tool / Product / Service:** Splunk Enterprise, Azure API Management, Semantic Kernel

**Environment-Specific Tailoring:** A shared logging library in each team's code sends authorization, data access, and release events to Splunk. Semantic Kernel agents log every tool call with its parameters and approval. API Management logs every request, and COTS output is normalized at ingest.

**Accountable Team:** Mission teams and ML Team, with the Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY28 and FY29 RDT&E, mission and ML, with the Phase 4 share unfunded

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-2.4.1: Web Application Activities Logging | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DE-2.4.2: API Gateway Operations Monitoring | 2 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.4.3: Serverless Function Execution Tracking | 2 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.4.4: Business Process Workflows Logging | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DE-2.4.5: Structured Application Logging | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DE-2.4.6: APM Telemetry | 4 | Technical | None | Level 3 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Medium-term (3–6 months) |
| DE-2.4.7: Application Security Event Logging | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DE-2.4.8: Agentic AI Tool-Call and Action Logging | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DE-2.5: Host and Endpoint Logging

**Selected Tool / Product / Service:** Splunk Enterprise, Microsoft Defender for Endpoint

**Environment-Specific Tailoring:** Splunk universal forwarders and Defender for Endpoint collect host logs in the cloud, the data center, and the alternate site from Phase 1. Fleet host logs arrive through the IT/OT DMZ once it is built in Phase 2.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1, DI-5.4

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-2.5.1: VM Monitoring Agents Deployment | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.5.2: Windows Security Event Collection | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.5.3: Linux System Log Gathering | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.5.4: Endpoint Protection Monitoring | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DE-2.6: Edge-Attack-Surface Logging

**Selected Tool / Product / Service:** Azure Application Gateway WAF v2, Azure API Management, Splunk Enterprise

**Environment-Specific Tailoring:** Application Gateway WAF logs and API Management's rate-limit and schema rejection events go to Splunk. Splunk correlates them per source and per partner.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-2.6.1: Web Application Attack Monitoring | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.6.2: Layer 7 Attack Attempt Capturing | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DE-2.6.3: API Abuse Tracking | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### DE-2.7: Network Security Logging

**Selected Tool / Product / Service:** Azure Monitor and VNet flow logs, Cisco ACI and APIC, Panorama with the PAN-OS provider for OpenTofu, Infoblox NIOS, Splunk Enterprise

**Environment-Specific Tailoring:** NSG flow logs, ACI flow telemetry, and every Palo Alto firewall's traffic and configuration logs go to Splunk, including the alternate site and ground segment firewalls. Infoblox and Azure DNS query logs cover every resolver. Splunk stitches each connection across the circuits.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C09](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references), [C12](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-2.7.1: Network Flow Logs Capturing | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Short-term (1–3 months) |
| DE-2.7.2: Firewall Activity Monitoring | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.7.3: DNS Query Data Collection | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.7.4: Network Event Correlation | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DE-2.7.5: Network Traffic Flow Analytics | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### DE-2.8: OT/Legacy Telemetry Ingestion and Normalization

**Selected Tool / Product / Service:** Nozomi Networks Guardian, Splunk Enterprise

**Environment-Specific Tailoring:** Nozomi sensors at each operating site and the stations' own logs are collected in the IT/OT DMZ and normalized for Splunk. The payload processing workstation's log is translated only if the AO re-dates CCSD tailoring action 3.

**Accountable Team:** Fleet Operations

**Dependencies:** DE-3.1, NE-1.6

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C13](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-2.8.1: OT/Legacy Protocol Telemetry Collection | 3 | Technical | None | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| DE-2.8.2: Telemetry Normalization to Common Schema for SIEM Ingestion | 3 | Technical | Automate | Level 1 | Continuous | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |
| DE-2.8.3: Legacy System Log Format/Protocol Translation | 3 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |

## DE-3: SIEM Platform

### DE-3.1: SIEM Capabilities

**Selected Tool / Product / Service:** Splunk Enterprise, Splunk Enterprise Security, Splunk SOAR, Azure OpenAI Service

**Environment-Specific Tailoring:** Splunk Enterprise and Enterprise Security run in the data center, with a forwarding tier at the alternate site. SOAR automation is limited to enrichment, ticketing, notification, and isolating non-production hosts. AI-assisted triage calls the Azure OpenAI deployment over F32 and takes no action.

**Accountable Team:** Security Team

**Dependencies:** NE-2.1, DA-2.4

**Funding Line:** FY27, FY28, and FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 1, Foundation, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-3.1.1: SIEM Platform Deployment | 1 | Technical | None | Level 1 | Continuous | Extensive | One-Time: High; Recurring: Extensive | Long-term (6+ months) |
| DE-3.1.2: Data Source Connections | 1 | Technical | None | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DE-3.1.3: Detection/Correlation Rule Configuration | 1 | Technical | None | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-3.1.4: Response Action Automation | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DE-3.1.5: Dashboard Monitoring | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-3.1.6: AI-Powered Analysis Integration | 4 | Technical | Automate | Level 3 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Short-term (1–3 months) |

### DE-3.2: Log Retention Strategy

**Selected Tool / Product / Service:** Splunk Enterprise, NetApp StorageGRID with S3 Object Lock

**Environment-Specific Tailoring:** Splunk keeps security logs searchable for 12 months, then rolls them to StorageGRID for 18 more under AU-11. An archived sample is restored and searched each year. All telemetry is also forwarded to the CSSP.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-3.2.1: Tiered Storage Routing | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Short-term (1–3 months) |
| DE-3.2.2: Long-Term/Archive Retention Policy Configuration | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Short-term (1–3 months) |
| DE-3.2.3: External Forwarding | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-3.2.4: Security Alert and Detection Data Retention/Archival Policy | 2 | Documentation | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DE-3.2.3: Required for the interim authorization to test, since the CSSP monitors from the first build.

### DE-3.3: Audit Log Integrity Protection

**Selected Tool / Product / Service:** Splunk Enterprise, NetApp StorageGRID with S3 Object Lock, CyberArk Privileged Access Manager

**Environment-Specific Tailoring:** Splunk writes each record to an object-locked StorageGRID bucket in compliance mode and hashes each batch. No role holds the delete capability, and the logging administrator role sits with named Security Team members. Break-glass access through CyberArk alerts.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1, ID-4.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-3.3.1: Write-Once/Immutable Log Storage Configuration | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-3.3.2: Log Administrator and System Administrator Duty Separation | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-3.3.3: Audit Processing Failure and Silent-Source Alerting | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DE-3.4: Time Synchronization

**Selected Tool / Product / Service:** Microchip SyncServer S650, Splunk Enterprise

**Environment-Specific Tailoring:** GNSS-disciplined time servers in the data center serve every on-premises host, with a secondary at the alternate site. Ground segment devices fall back to each site's holdover reference. Cloud workloads use the provider's time service, and Splunk alerts on drift between the sides.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C20](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-3.4.1: Windows Time Sync | 1 (pinned) | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-3.4.2: Linux Time Sync | 1 (pinned) | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-3.4.3: Custom NTP Servers | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DE-3.4.4: Timestamp Format Validation | 2 (pinned) | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-3.4.5: Time Drift Monitoring | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DE-3.4.1, DE-3.4.2, and DE-3.4.3: Built in when the platform is created, since retrofitting it later costs far more. Logs collected before it cannot be correlated reliably. DE-3.4.4: Coverage follows the data services and log sources, most of which arrive in Phase 2.
