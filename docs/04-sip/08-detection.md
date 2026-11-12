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

**Target Date / Sprint:** 2027-12-31

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

**Funding Line:** FY29 O&M, platform and security operations

**Rollout Phase:** Phase 4, Maturity

**Target Date / Sprint:** 2028-12-31

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

**Dependencies:** DE-2.1, DE-2.5, DE-2.7, DE-3.1

**Funding Line:** FY28 and FY29 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate, with activities through Phase 4

**Target Date / Sprint:** 2028-12-31

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

**Funding Line:** FY29 O&M, platform and security operations

**Rollout Phase:** Phase 4, Maturity

**Target Date / Sprint:** 2028-12-31

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

**Funding Line:** FY29 O&M, platform and security operations

**Rollout Phase:** Phase 4, Maturity

**Target Date / Sprint:** 2028-12-31

**Contracting / Procurement Reference:** [C17](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-1.5.1: Honeytoken and Canary Credential Deployment | 4 | Technical | None | Level 3 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-1.5.2: Decoy System/Honeypot Deployment | 4 | Technical | None | Level 3 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DE-1.5.3: Deception Trigger Alerting and Investigation Routing | 4 | Technical | None | Level 3 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### DE-1.6: User/Entity Behavior Analytics (UEBA) / Insider Threat Detection

**Selected Tool / Product / Service:** Splunk User Behavior Analytics, Microsoft Purview Insider Risk Management

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-2.1, DE-2.5, DE-2.7, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-06-30

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-1.6.1: Behavioral Baseline Profiling | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DE-1.6.2: Anomalous Behavior Alerting and Risk Scoring | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| DE-1.6.3: Insider Threat Indicator Correlation and Investigation | 3 | Process | None | Level 2 | Continuous | High | One-Time: Moderate; Recurring: High | Medium-term (3–6 months) |

### DE-1.7: Network/OT Intrusion and Anomaly Detection

**Selected Tool / Product / Service:** Corelight sensors, Nozomi Networks Guardian, Palo Alto Advanced Threat Prevention

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-2.7, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

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

**Target Date / Sprint:** 2027-12-31

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

### DE-1.9: User Activity Monitoring

**Selected Tool / Product / Service:** CyberArk Privileged Session Manager, Splunk Enterprise

**Environment-Specific Tailoring:** None. One configuration serves the cloud, the data center, and the alternate site.

**Accountable Team:** Security Team

**Dependencies:** DE-2.1, DE-2.5, DE-2.7, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C07](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-1.9.1: User Activity Monitoring Deployment on Classified Endpoints | 2 | Technical | None | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DE-1.9.2: Monitoring Policy, Trigger, and Reviewer Definition | 2 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-1.9.3: Review, Triage, and Insider Threat Program Referral | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

## DE-2: Comprehensive Logging

### DE-2.1: Infrastructure and Identity Logging

**Selected Tool / Product / Service:** Splunk Enterprise, Azure Monitor and VNet flow logs

**Environment-Specific Tailoring:** Azure Monitor collects cloud logs and forwards them to Splunk over the circuit. Splunk universal forwarders collect data center and alternate site logs, and the IT/OT DMZ collects fleet logs.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

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

**Selected Tool / Product / Service:** Splunk Enterprise, Azure Monitor and VNet flow logs

**Environment-Specific Tailoring:** Azure Monitor collects cloud logs and forwards them to Splunk over the circuit. Splunk universal forwarders collect data center and alternate site logs, and the IT/OT DMZ collects fleet logs.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-2.2.1: Resource Level Data Plane Logs | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Short-term (1–3 months) |
| DE-2.2.2: Log Storage Operations | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-2.2.3: Database Activity Auditing | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.2.4: Secrets Access Monitoring | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.2.5: NoSQL Operations Tracking | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.2.6: Other Data Services Coverage | 1 | Technical | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DE-2.2.7: Data Service Logging Automation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| DE-2.2.8: Consistent Logging Coverage Enforcement (data-service sources) | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DE-2.3: Container and Orchestration Platform Logging

**Selected Tool / Product / Service:** Azure Monitor and VNet flow logs, Defender for Containers, Splunk Enterprise

**Environment-Specific Tailoring:** Azure Monitor collects cloud logs and forwards them to Splunk over the circuit. Splunk universal forwarders collect data center and alternate site logs, and the IT/OT DMZ collects fleet logs.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

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

**Environment-Specific Tailoring:** Azure Monitor collects cloud logs and forwards them to Splunk over the circuit. Splunk universal forwarders collect data center and alternate site logs, and the IT/OT DMZ collects fleet logs.

**Accountable Team:** Mission teams and ML Team, with the Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY28 and FY29 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate, with activities through Phase 4

**Target Date / Sprint:** 2028-12-31

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

**Environment-Specific Tailoring:** Azure Monitor collects cloud logs and forwards them to Splunk over the circuit. Splunk universal forwarders collect data center and alternate site logs, and the IT/OT DMZ collects fleet logs.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

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

**Environment-Specific Tailoring:** Azure Monitor collects cloud logs and forwards them to Splunk over the circuit. Splunk universal forwarders collect data center and alternate site logs, and the IT/OT DMZ collects fleet logs.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-2.6.1: Web Application Attack Monitoring | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| DE-2.6.2: Layer 7 Attack Attempt Capturing | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| DE-2.6.3: API Abuse Tracking | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### DE-2.7: Network Security Logging

**Selected Tool / Product / Service:** Azure Monitor and VNet flow logs, Cisco ACI and APIC, Panorama with the Terraform PAN-OS provider, Infoblox NIOS, Splunk Enterprise

**Environment-Specific Tailoring:** Azure Monitor collects cloud logs and forwards them to Splunk over the circuit. Splunk universal forwarders collect data center and alternate site logs, and the IT/OT DMZ collects fleet logs.

**Accountable Team:** Platform Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

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

**Environment-Specific Tailoring:** Azure Monitor collects cloud logs and forwards them to Splunk over the circuit. Splunk universal forwarders collect data center and alternate site logs, and the IT/OT DMZ collects fleet logs.

**Accountable Team:** Fleet Operations

**Dependencies:** DE-3.1, NE-1.6

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-06-30

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

**Environment-Specific Tailoring:** Splunk runs in the data center, with a forwarding tier at the alternate site so collection continues if the data center is lost.

**Accountable Team:** Security Team

**Dependencies:** NE-2.1, DA-2.4

**Funding Line:** FY27 and FY28 and FY29 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 4

**Target Date / Sprint:** 2028-12-31

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

**Environment-Specific Tailoring:** Splunk runs in the data center, with a forwarding tier at the alternate site so collection continues if the data center is lost.

**Accountable Team:** Security Team

**Dependencies:** NE-2.1, DA-2.4

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

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

**Environment-Specific Tailoring:** Splunk runs in the data center, with a forwarding tier at the alternate site so collection continues if the data center is lost.

**Accountable Team:** Security Team

**Dependencies:** NE-2.1, DA-2.4

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-06-30

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C16](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-3.3.1: Write-Once/Immutable Log Storage Configuration | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| DE-3.3.2: Log Administrator and System Administrator Duty Separation | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-3.3.3: Audit Processing Failure and Silent-Source Alerting | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### DE-3.4: Time Synchronization

**Selected Tool / Product / Service:** Microchip SyncServer S650

**Environment-Specific Tailoring:** Splunk runs in the data center, with a forwarding tier at the alternate site so collection continues if the data center is lost.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.1, DA-2.4

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with activities through Phase 2

**Target Date / Sprint:** 2027-12-31

**Contracting / Procurement Reference:** [C20](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| DE-3.4.1: Windows Time Sync | 1 (pinned) | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-3.4.2: Linux Time Sync | 1 (pinned) | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-3.4.3: Custom NTP Servers | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| DE-3.4.4: Timestamp Format Validation | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| DE-3.4.5: Time Drift Monitoring | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** DE-3.4.1: Built in when the platform is created, since retrofitting it later costs far more. Logs collected before it cannot be correlated reliably. DE-3.4.2: Built in when the platform is created, since retrofitting it later costs far more. Logs collected before it cannot be correlated reliably. DE-3.4.3: Built in when the platform is created, since retrofitting it later costs far more. Logs collected before it cannot be correlated reliably.
