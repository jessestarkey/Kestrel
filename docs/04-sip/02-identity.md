# ID: Identity

*KESTREL Security Implementation Plan, Section 4 (Protect). Each record implements the outcome of the same ID in the [SADD](../03-sadd/02-identity.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## ID-1: Identity Platform and Management

### ID-1.1: Identity Proofing and Enrollment

**Selected Tool / Product / Service:** Microsoft Entra ID Governance, Jira Service Management Data Center, Active Directory Domain Services

**Environment-Specific Tailoring:** Proofing binds each DoD user to the CAC record and each partner or vendor user to a sponsor's attestation. It happens once, at onboarding, so it does not vary by location.

**Accountable Team:** IT Operations

**Dependencies:** ID-1.3, DoD PKI CAC issuance, the PSO

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-1.1.1: Identity Assurance Level Determination | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-1.1.2: Sponsor/Nomination and Identity Verification | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| ID-1.1.3: Binding to Authoritative Source | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.1.4: Contractor and Foreign National Identifier Marking | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-1.1.5: Provisioning-on-Enrollment Automation | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.1.6: Re-Proofing Triggers | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-1.1.7: Address Confirmation | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### ID-1.2: External PKI Trust and Sponsorship

**Selected Tool / Product / Service:** Microsoft Entra certificate-based authentication, Microsoft Entra ID, Microsoft Entra ID Governance

**Environment-Specific Tailoring:** ECA trust, revocation checking, sponsorship, and review start in Phase 1, because vendor support engineers connect with ECA credentials from the first build. Partner nations' PKIs and identity providers join in Phase 3, once integration testing under the interim authorization to test is done, and they are trusted only for the partner API that Mission Team 2 runs.

**Accountable Team:** IT Operations

**Dependencies:** ID-1.3, DA-3.7, GV-5.6

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-1.2.1: External PKI Trust Chain Management | 1 (pinned) | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.2.2: External Credential Validation and Revocation Checking | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.2.3: Partner Identity Provider Federation Trust Management | 3 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.2.4: External User Sponsorship and Local Identity Binding | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| ID-1.2.5: External User Access Authorization Mapping | 1 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-1.2.6: External User Access Review and Revocation | 1 (pinned) | Process | None | Level 1 | Periodic (Quarterly) (re-rated) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

**Pinned:** ID-1.2.1: Vendor support engineers authenticate with ECA credentials from Phase 1, before partners onboard. ID-1.2.2: Vendor ECA credentials are revocation-checked at every session from the day vendors connect. ID-1.2.4: Each vendor engineer is sponsored and bound to a local identity from the day vendors connect. ID-1.2.5: Vendor access is authorized against its support case from the day vendors connect. ID-1.2.6: Vendor access is reviewed from the day vendors connect.

**Re-rated:** ID-1.2.6: AMP Section 6 reviews partner and vendor access quarterly.

### ID-1.3: Centralized Identity Platform

**Selected Tool / Product / Service:** Active Directory Domain Services, Microsoft Entra Connect Sync, Microsoft Entra ID, Microsoft Entra ID Governance

**Environment-Specific Tailoring:** Active Directory in the data center is the system of record, with a warm standby at the alternate site, so the data center and the fleet keep identity if the cloud is unreachable. Entra ID is its cloud projection through Entra Connect Sync.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** None. Identity is the first build.

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-1.3.1: Identity Platform Adoption | 1 | Technical | None | Level 1 | One-Time | Extensive | One-Time: High; Recurring: High | Long-term (6+ months) |
| ID-1.3.2: Identity Organization and Segmentation Strategy | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### ID-1.4: Identity Platform Threat Detection and Hardening

**Selected Tool / Product / Service:** Microsoft Defender for Identity, Microsoft Entra ID Protection, Splunk Enterprise Security

**Environment-Specific Tailoring:** Defender for Identity watches the domain controllers in the data center and at the alternate site, and Entra ID Protection watches cloud sign-ins. Both alert in Splunk.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** ID-1.3, DE-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-1.4.1: Identity Platform Protection Tool Deployment | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-1.4.2: Identity Platform Protection Tool Hardening | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** ID-1.4.1: KESTREL's design depends on it from the first build, since the Phase 1 risk-based access policy reads its signal.

### ID-1.5: Directory and Tier 0 Infrastructure Hardening

**Selected Tool / Product / Service:** Active Directory Domain Services, Active Directory Certificate Services, Entrust nShield 5 HSMs, Microsoft Defender for Identity, Microsoft Entra Connect Sync, Windows LAPS, group Managed Service Accounts, CyberArk Privileged Access Manager

**Environment-Specific Tailoring:** The root certificate authority's keys sit in the nShield HSMs, with a standby issuing authority and a second HSM at the alternate site. Directory synchronization runs only over the circuit, and Windows LAPS rotates local administrator passwords.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** ID-1.3, DA-3.4, DA-3.7

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-1.5.1: Directory Service Configuration Hardening | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.5.2: Certificate Authority Infrastructure Hardening | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.5.3: Hybrid Identity Synchronization Infrastructure Hardening | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-1.5.4: Tier 0 and Local Administrator Credential Rotation | 1 | Technical | Automate | Level 1 | Periodic (Monthly) (re-rated) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

**Re-rated:** ID-1.5.4: AMP Section 3 rotates local administrator and group Managed Service Account passwords every 30 days.

### ID-1.6: Third-Party Application and SaaS Access Governance

**Selected Tool / Product / Service:** Microsoft Entra ID, Microsoft Defender for Cloud Apps

**Environment-Specific Tailoring:** Consent control is an Entra tenant setting, so it applies only in the cloud. Discovery reads egress logs from both hubs and the alternate site's firewall, so it covers every location.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** ID-1.3

**Funding Line:** FY27 and FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 1, Foundation, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-1.6.1: Application Consent Control (OAuth/SaaS) | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-1.6.2: SaaS Application Discovery and Security Posture Management (CASB) | 4 | Technical | Automate | Level 3 | Continuous | Moderate | One-Time: Moderate; Recurring: High | Medium-term (3–6 months) |

**Pinned:** ID-1.6.1: Built in when the platform is created, since retrofitting it later costs far more. Blocking user consent is a tenant setting applied at creation.

### ID-1.7: Identities and Entitlements Lifecycle

**Selected Tool / Product / Service:** Active Directory Domain Services, Jira Service Management Data Center, Microsoft Entra ID Governance

**Environment-Specific Tailoring:** Active Directory groups own membership for every role, and IT Operations changes them through the Jira Service Management request that records each approval. Entra ID Governance access packages cover only cloud-only resources.

**Accountable Team:** IT Operations, with the Platform Team

**Dependencies:** ID-1.3

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-1.7.1: Entitlement Management | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.7.2: Entitlement Lifecycle Workflows | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| ID-1.7.3: Permissions Management | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

**Pinned:** ID-1.7.1: KESTREL's design depends on it from the first build, since team-scoped entitlements enforce the payload vendor split. ID-1.7.2: Provisioning starts in Phase 1, so its approval workflow must too, or one person could approve and provision the same access.

### ID-1.8: Account Lifecycle and Identity Data Quality

**Selected Tool / Product / Service:** Active Directory Domain Services, Splunk Enterprise, Ansible Automation Platform, Jira Service Management Data Center

**Environment-Specific Tailoring:** Splunk computes dormancy daily from Active Directory and Entra ID sign-ins, including station sign-ins, and Ansible disables the account in Active Directory, excluding break-glass accounts. A departure disables the Active Directory account, which flows to Entra ID, and revokes the CAC binding. Ground control stations pick up the revocation at their daily refresh and before each flight.

**Accountable Team:** IT Operations

**Dependencies:** ID-1.3, DE-3.1, the parent organization's and the performer's personnel systems

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C21](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-1.8.1: Authoritative Source Synchronization | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.8.2: Deprovisioning-on-Termination Automation | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.8.3: Orphaned and Dormant Account Remediation | 2 | Technical | Automate | Level 2 | Continuous (re-rated) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| ID-1.8.4: Duplicate Identity Detection and Reconciliation | 2 | Technical | None | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.8.5: Identity/Access Posture Dashboard | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

**Re-rated:** ID-1.8.3: AMP Section 4 checks dormancy daily.

### ID-1.9: Access Reviews

**Selected Tool / Product / Service:** Microsoft Entra ID Governance, CyberArk Privileged Access Manager, Jira Software Data Center

**Environment-Specific Tailoring:** Entra ID Governance runs the campaigns for cloud and directory access, and CyberArk's reviews cover vaulted privileged accounts. Operator access is reviewed with Fleet Operations' operations lead.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** ID-1.3, ID-1.7

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-1.9.1: Access Review Scope and Objectives | 2 (pinned) | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-1.9.2: Access Review Assignments | 2 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-1.9.3: Access Review Setup | 2 (pinned) | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| ID-1.9.4: Access Review Evaluations | 2 (pinned) | Process | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| ID-1.9.5: Access Review Outcome Actions | 2 (pinned) | Process | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| ID-1.9.6: Automated Access Review Campaign Generation and Reminders | 2 | Technical | Automate | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** ID-1.9.1, ID-1.9.2, ID-1.9.3, ID-1.9.4, and ID-1.9.5: The first access review follows a quarter of live accounts, so it starts in Phase 2.

### ID-1.10: Physical and Logical Access Convergence

**Selected Tool / Product / Service:** the PSO's physical access control system, Splunk Enterprise Security

**Environment-Specific Tailoring:** The PSO runs the physical access control systems at the data center and each operating site, and the parent organization's facility runs the one at the alternate site. KESTREL's account lifecycle events drive the PSO's badge provisioning and removal from Phase 2, and the correlation that alerts on an operator signed in at a station without a badge-in starts in Phase 3, when the fleet's logs arrive.

**Accountable Team:** Security Team, with the PSO

**Dependencies:** DE-3.1, the PSO physical access control system

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-1.10.1: PACS-to-Identity Platform Integration | 2 | Technical | None | Level 2 | One-Time | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| ID-1.10.2: Physical Access Provisioning and Deprovisioning | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-1.10.3: Physical-Logical Access Correlation | 3 (pinned) | Technical | Automate | Level 3 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-1.10.4: Physical Access Reconciliation and Audit | 2 | Process | None | Level 2 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** ID-1.10.3: The AMP alerts on an operator signed in at a station without a badge-in, so the correlation must run before the ATO decision.

## ID-2: User Identity Protection

### ID-2.1: User Authentication Controls

**Selected Tool / Product / Service:** Microsoft Entra certificate-based authentication, Active Directory Domain Services, Active Directory Certificate Services, the aircraft and ground equipment manufacturer's tools

**Environment-Specific Tailoring:** Cloud sign-in uses Entra certificate-based authentication with the CAC. Data center sign-in uses Active Directory smart card logon. Ground control stations always check the CAC locally, against a revocation list refreshed daily and before each flight.

**Accountable Team:** Platform Team, with Fleet Operations for the stations

**Dependencies:** ID-1.3, DA-3.7

**Funding Line:** FY27 and FY28 O&M, platform and security operations, with the fleet slice as RDT&E fleet integration

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-2.1.1: Phishing-Resistant Authenticator Selection (PIV/CAC/FIDO2) | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.1.2: Assurance-Level-to-Resource-Sensitivity Mapping | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.1.3: Derived/Mobile Credentials | N/A | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-2.1.4: Fallback/Step-Up Authenticator Policy | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.1.5: Password Security | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.1.6: OT/Legacy Authentication Compensating Controls | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-2.1.7: System Use Notification Banner Configuration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| ID-2.1.8: Logon Attempt Limits and Authentication Feedback | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Not applicable:** ID-2.1.3: KESTREL has no mobile devices, so no derived credentials are issued.

### ID-2.2: Credential Management

**Selected Tool / Product / Service:** Active Directory Certificate Services, Keyfactor Command, Entrust nShield 5 HSMs, Microsoft Entra certificate-based authentication, CAC PIN reset workstations

**Environment-Specific Tailoring:** DoD issues the CACs, and IT Operations runs CAC PIN reset workstations at the data center and each operating site, with no alternate credential for a lost card. The program PKI issues and revokes device and workload certificates in every location. Services accept a cached revocation response for up to 24 hours, and ground control stations check a local list refreshed daily and before each flight.

**Accountable Team:** Platform Team (Tier 0 administrators), with IT Operations for CAC PIN resets

**Dependencies:** ID-1.3, DA-3.4, DA-3.7, DA-3.8

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-2.2.1: PIV/CAC Credential Issuance | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-2.2.2: Credential Revocation and Renewal | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-2.2.3: PIV-Denied and Degraded-Connectivity Fallback | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.2.4: Credential Status Checking (OCSP/CRL) | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-2.2.5: National Security Systems PKI Hardware Token Management | N/A | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

**Pinned:** ID-2.2.3: Revocation checking starts in Phase 1, and it needs the rule for what happens when the revocation service is unreachable.

**Not applicable:** ID-2.2.5: KESTREL is an unclassified national security system whose users authenticate with DoD PKI CACs. NSS PKI tokens serve SECRET and higher networks, which at KESTREL means only the separately authorized IL6 enclave.

### ID-2.3: Single Sign on (SSO)

**Selected Tool / Product / Service:** Microsoft Entra ID, Microsoft Entra Conditional Access

**Environment-Specific Tailoring:** Every application federates with Entra ID by OIDC, or by SAML where a COTS product supports nothing else, including data center applications reached over the circuit. Administrative consoles never share the user session.

**Accountable Team:** Platform Team

**Dependencies:** ID-1.3, DA-3.7

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-2.3.1: SSO Planning | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.3.2: SSO Configuration | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-2.3.3: SSO Protocol Configuration Hardening | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** ID-2.3.1 and ID-2.3.2: Built in when the platform is created, since retrofitting it later costs far more. Every application joins single sign-on at intake, and Phase 1 deploys the first ones.

### ID-2.4: Non-Privileged Access Control

**Selected Tool / Product / Service:** Active Directory Domain Services, Microsoft Entra ID, Microsoft Entra ID Governance

**Environment-Specific Tailoring:** Roles are Active Directory groups scoped by team and synchronized to Entra ID. Partner users sit in release-by-nation groups that reach only the partner API.

**Accountable Team:** Platform Team

**Dependencies:** ID-1.3, DA-3.7

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-2.4.1: Default Permissions | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.4.2: Platform-Defined Non-Privileged Roles | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.4.3: Custom Non-Privileged Roles | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| ID-2.4.4: Non-Privileged Group Access Control (GBAC) Baseline | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| ID-2.4.5: Unauthenticated Action Inventory | 1 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** ID-2.4.4: KESTREL's design depends on it from the first build, since team membership is part of every role.

### ID-2.5: Adaptive, Risk-Based Access Control

**Selected Tool / Product / Service:** Microsoft Entra Conditional Access, Microsoft Entra ID Protection, Pomerium Enterprise

**Environment-Specific Tailoring:** Conditional Access reads the performer's device compliance signal, shared under the interconnection agreement, for every proxy and VDI session. The Boundary Cloud Access Point supplies the network origin, partner sessions from unexpected networks step up, and identity threat detection's risk feeds every decision. The badge correlation alert joins as a signal in Phase 3.

**Accountable Team:** Platform Team

**Dependencies:** ID-1.3, ID-1.4, DA-3.7, NE-2.7, the performer device compliance feed

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C22](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-2.5.1: Adaptive, Risk-Based Access Tool Deployment | 1 (pinned) | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-2.5.2: Adaptive, Risk-Based Access Policy Definition | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** ID-2.5.1 and ID-2.5.2: KESTREL's design depends on it from the first build, since performer laptops are admitted only on a device posture check.

### ID-2.6: Continuous Authentication

**Selected Tool / Product / Service:** Microsoft Entra Conditional Access, Microsoft Entra ID Protection, Azure Virtual Desktop

**Environment-Specific Tailoring:** Cloud and VDI sessions follow the AMP's timeouts under continuous access evaluation. Ground control stations lock after 15 minutes except while their aircraft is airborne, under CCSD tailoring action 2, from fleet integration in Phase 3.

**Accountable Team:** Platform Team, with Fleet Operations for the stations

**Dependencies:** ID-1.3, DA-3.7

**Funding Line:** FY27 and FY28 O&M, platform and security operations, with the fleet slice as RDT&E fleet integration

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-2.6.1: Session Risk Scoring | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-2.6.2: Step-Up Re-Authentication Triggers | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.6.3: Session/Token Revocation on Risk Change | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.6.4: Continuous Access Evaluation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-2.6.5: Session and Token Lifetime Policy | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.6.6: Token Binding and Proof-of-Possession | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-2.6.7: Device Lock | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-2.6.8: Concurrent Session Limits | 2 | Technical | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## ID-3: Non-Person Entity Identity Protection

### ID-3.1: Cloud Workload Identities

**Selected Tool / Product / Service:** Microsoft Entra Workload ID, AKS workload identity

**Environment-Specific Tailoring:** Every cloud workload, including the pipeline's runners, uses AKS workload identity federated to Entra ID, scoped to its own spoke. Data center services are covered by ID-3.2 and fleet devices by ID-3.7.

**Accountable Team:** Platform Team

**Dependencies:** ID-1.3, DA-3.3, DA-3.7

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-3.1.1: Cloud Workload Identity Selection | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-3.1.2: Cloud Workload Identity Permissions | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-3.1.3: Cloud Workload Identity Code Authentication Integration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-3.1.4: Native/Local Credential Elimination | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### ID-3.2: Application and Service Account Identities

**Selected Tool / Product / Service:** group Managed Service Accounts, Active Directory Certificate Services, Keyfactor Command, Jira Service Management Data Center

**Environment-Specific Tailoring:** Service accounts exist only in the data center and at the alternate site, as group Managed Service Accounts where possible and certificate-authenticated accounts otherwise, each requested through the service desk.

**Accountable Team:** Platform Team

**Dependencies:** ID-1.3, DA-3.3, DA-3.7

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-3.2.1: Service Account Creation | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-3.2.2: Service Account Least Privilege | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-3.2.3: Certificate-Based Credentials | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-3.2.4: Client Secret Fallback | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-3.2.5: Service Account Code Authentication Integration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-3.2.6: Non-Person Entity Account Recertification | 2 (pinned) | Process | None | Level 1 | Periodic (Semi-Annual) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

**Pinned:** ID-3.2.3: Certificate credentials are the preferred method, so they must exist before the client-secret fallback that starts in Phase 1. ID-3.2.6: The first access review follows a quarter of live accounts, so it starts in Phase 2.

### ID-3.3: AI Agent Identities

**Selected Tool / Product / Service:** Microsoft Entra Workload ID, AKS workload identity

**Environment-Specific Tailoring:** Each AI agent's identity is an Entra workload identity on AKS in its mission team's prod spoke, with no rights beyond the tools its use case approves.

**Accountable Team:** Mission Team 2, with the Platform Team

**Dependencies:** ID-3.1, ID-1.7, AI-1.1, AI-8.7

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-3.3.1: Agent Identity Registration | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-3.3.2: Task-Scoped Credential Issuance | 3 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-3.3.3: External Tool-Provider Registration and Approval | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| ID-3.3.4: Agent Tool/API Access Scoping | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-3.3.5: Tool-Provider Catalog Drift Detection | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-3.3.6: Delegated Authority Attribution | 3 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-3.3.7: High-Risk Action Human Approval Gate | 3 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-3.3.8: Agentic Session Timeout and Forced Termination | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### ID-3.4: Server and Services Authentication

**Selected Tool / Product / Service:** Istio service mesh add-on for AKS, Keyfactor Command, Active Directory Certificate Services

**Environment-Specific Tailoring:** The Istio mesh issues workload certificates in every cluster from an intermediate under the program PKI, and data center services use certificates from Keyfactor. Traffic across the circuit is mutually authenticated end to end.

**Accountable Team:** Platform Team

**Dependencies:** ID-1.3, DA-3.3, DA-3.7, DA-3.8

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C11](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-3.4.1: TLS Authentication for Services | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-3.4.2: Client Application Certificate Trust | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-3.4.3: Mutual TLS | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### ID-3.5: Secrets and Credentials Detection

**Selected Tool / Product / Service:** GitLab Secret Detection, Defender for Cloud CSPM, GitGuardian public monitoring

**Environment-Specific Tailoring:** Secret scanning covers the repositories, pipeline logs, container images, and cloud storage. A finding in a release candidate fails Certification to Field.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.4, NE-3.7

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C29](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-3.5.1: Agentless Scanning | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| ID-3.5.2: Secrets Exposure Monitoring | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### ID-3.6: Secrets and Credentials Protection

**Selected Tool / Product / Service:** Azure Key Vault Premium, GitLab Secret Detection, Entrust nShield 5 HSMs

**Environment-Specific Tailoring:** Each spoke's Key Vault holds only that spoke's secrets and rotates them automatically. Datalink and root keys stay in the nShield HSMs instead.

**Accountable Team:** Platform Team

**Dependencies:** ID-1.3, DA-3.3, DA-3.4, DA-3.10, DA-3.11

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-3.6.1: NPE Credential Vault Integration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-3.6.2: Automated Secret Rotation | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-3.6.3: Developer Workflow for Secrets | 2 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-3.6.4: Secrets Continuous Monitoring | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### ID-3.7: OT/Legacy Device Identity Controls

**Selected Tool / Product / Service:** the aircraft and ground equipment manufacturer's tools, the datalink crypto modules, Active Directory Certificate Services

**Environment-Specific Tailoring:** Each aircraft and station authenticates on the datalinks with a program PKI device identity loaded by the manufacturer's tools. Equipment that cannot hold one is identified by its zone and conduit placement.

**Accountable Team:** Fleet Operations

**Dependencies:** DA-3.7, NE-1.6

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C26](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-3.7.1: Default Credential Remediation | 3 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-3.7.2: Network-Based Device Identity Verification | 2 (pinned) | Technical | None | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-3.7.3: Gateway-Based Credential Proxying | 3 | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-3.7.4: Constrained-Device Certificate Lifecycle Management | 2 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-3.7.5: Credential Rotation via Maintenance Windows | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** ID-3.7.2: Datalink authentication is set up on spares and the simulator in Phase 2, and it needs device identity to verify against. ID-3.7.4: Datalink authentication is set up on spares and the simulator in Phase 2, and it needs device certificates to verify against.

## ID-4: Privileged Access Management

### ID-4.1: Privileged Access Control

**Selected Tool / Product / Service:** CyberArk Privileged Access Manager, CyberArk Privileged Session Manager, Microsoft Entra Privileged Identity Management, Windows 11 Enterprise, hardened to the DISA STIG

**Environment-Specific Tailoring:** Privileged roles are defined per administrative surface, namely the cloud hub, each spoke, the clusters, the data center, the alternate site, the PKI and HSMs, and the ground segment, in Entra PIM for the cloud and CyberArk for everything else.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** ID-1.3, ID-2.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C07](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-4.1.1: Platform-Defined Privileged Roles | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.1.2: Custom Privileged Roles | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| ID-4.1.3: Privileged Group Access Control (GBAC) Baseline | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |

### ID-4.2: Privileged Access Workstations and Administrative Tiering

**Selected Tool / Product / Service:** Windows 11 Enterprise, hardened to the DISA STIG, Azure Virtual Desktop, CyberArk Privileged Session Manager

**Environment-Specific Tailoring:** Tier 0 is administered only from the Windows 11 privileged access workstations in the data center and at the alternate site. Tier 1 runs from the platform Azure Virtual Desktop host pool, and the CSSP's pool reaches only the security monitoring platform and its playbooks.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** ID-1.3, ID-2.1, DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C02](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-4.2.1: Administrative Tier Model Definition | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.2.2: Privileged Access Workstation Deployment and Hardening | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| ID-4.2.3: Tiered Credential Isolation Enforcement | 1 | Technical | None | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-4.2.4: Tiering Compliance Monitoring and Violation Alerting | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

**Pinned:** ID-4.2.2: KESTREL's design depends on it from the first build, since Tier 0 is administered only from the privileged access workstations.

### ID-4.3: Just in Time Access

**Selected Tool / Product / Service:** CyberArk Privileged Access Manager, CyberArk Privileged Session Manager, Microsoft Entra Privileged Identity Management, Azure Virtual Desktop

**Environment-Specific Tailoring:** Cloud roles are activated through Entra PIM and on-premises and fleet roles through CyberArk, each for a bounded window, with a second approver for the PKI and HSMs.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** ID-1.3, ID-2.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C07](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-4.3.1: Privileged Access Management Tool Deployment | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: High | Medium-term (3–6 months) |
| ID-4.3.2: Time-Bound Role Eligibility Configuration | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.3.3: Activation Workflows | 1 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.3.4: Automatic Expiration | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** ID-4.3.3 and ID-4.3.4: KESTREL's design depends on it from the first build, since no privilege is standing.

### ID-4.4: Privileged Credential Vaulting and Session Brokering

**Selected Tool / Product / Service:** CyberArk Privileged Access Manager, CyberArk Privileged Session Manager, Entrust nShield 5 HSMs

**Environment-Specific Tailoring:** CyberArk vaults the built-in administrative accounts on the HSMs, network appliances, hypervisors, and out-of-band controllers, and brokers and records every session that uses one. Two-person actions use CyberArk dual control, and HSM key operations use the nShield card quorum.

**Accountable Team:** Platform Team (Tier 0 administrators)

**Dependencies:** ID-1.3, ID-2.1, DE-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C07](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-4.4.1: Privileged Credential Vaulting and Checkout | 1 | Technical | None | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-4.4.2: Privileged Session Brokering | 1 (pinned) | Technical | None | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-4.4.3: Privileged Session Recording and Monitoring | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| ID-4.4.4: Two-Person Integrity for Designated Privileged Actions | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** ID-4.4.2: KESTREL's design depends on it from the first build, since every privileged session is brokered. ID-4.4.3: KESTREL's design depends on it from the first build, since every privileged session is recorded. ID-4.4.4: KESTREL's design depends on it from the first build, since HSM key generation and root CA work in Phase 1 need a second person.

### ID-4.5: OT/Legacy Scheduled Maintenance-Window Access

**Selected Tool / Product / Service:** CyberArk Privileged Access Manager, CyberArk Privileged Session Manager, Jira Service Management Data Center

**Environment-Specific Tailoring:** Each operating site has a weekly maintenance window, never held while an aircraft under its stations is airborne, opened against an approved change record. Extensions need Fleet Operations' operations lead and an ISSO.

**Accountable Team:** Fleet Operations

**Dependencies:** ID-1.3, ID-2.1, ID-4.4, ID-3.7

**Funding Line:** FY28 RDT&E, fleet integration

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C07](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-4.5.1: Maintenance Window Scheduling and Change Coordination | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.5.2: Window-Bound Access Request and Approval | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.5.3: Time-Bound Account Enablement and Automatic Disablement | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.5.4: Maintenance Session Monitoring and Recording | 3 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-4.5.5: Window Extension and Escalation Process | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.5.6: Post-Maintenance Access Review and Audit | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.5.7: Maintenance Tool and Diagnostic Equipment Inspection | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### ID-4.6: Emergency Access

**Selected Tool / Product / Service:** Microsoft Entra ID, YubiKey 5 FIPS Series, Active Directory Certificate Services, Active Directory Domain Services, the aircraft and ground equipment manufacturer's tools, Splunk Enterprise, Azure Monitor and VNet flow logs

**Environment-Specific Tailoring:** The two cloud accounts use different sign-in methods, the cloud certificate comes from a dedicated break-glass CA, and cloud and alternate-site use alerts directly through Azure Monitor as well as Splunk. The directory set holds a domain account, each domain controller's DSRM password, and a local administrator per privileged access workstation, and every station has its own local account, all console-only under CCSD tailoring action 6. Cloud and directory sets are sealed in the data center and at the alternate site from Phase 1, and station accounts at each operating site when the fleet integrates in Phase 3.

**Accountable Team:** Platform Team (Tier 0 administrators), with Fleet Operations

**Dependencies:** ID-1.3, ID-2.1, DE-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations, with the fleet slice as RDT&E fleet integration

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C24](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-4.6.1: Emergency Access Account Creation | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.6.2: Emergency Account Authentication Protections | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.6.3: Emergency Session Scope and Time-Boxing | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.6.4: Emergency Account Monitoring and Alerting | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.6.5: Emergency Account Testing and Maintenance Procedures | 1 (pinned) | Process | None | Level 2 | Periodic (Quarterly) (re-rated) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** ID-4.6.4: KESTREL's design depends on it from the first build, since the break-glass runbook depends on the alert from the first use. ID-4.6.5: KESTREL's design depends on it from the first build, since the break-glass runbook is tested quarterly from the first set.

**Re-rated:** ID-4.6.5: AMP Section 11 tests each break-glass set quarterly.

**Exception:** ID-4.6.2: The directory and ground segment break-glass accounts use console-only passwords under CCSD tailoring action 6. The cloud accounts keep two phishing-resistant methods.

### ID-4.7: Access Process for Third-Party Support

**Selected Tool / Product / Service:** CyberArk Privileged Access Manager, CyberArk Privileged Session Manager, Jira Service Management Data Center

**Environment-Specific Tailoring:** Vendor engineers connect through CyberArk only for an open Jira Service Management case, for at most eight hours, with every session recorded. Fleet vendors connect only within a maintenance window.

**Accountable Team:** Platform Team, with each system-owning team lead as sponsor

**Dependencies:** ID-1.2, ID-1.3, ID-2.1, DE-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C07](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-4.7.1: Vendor Support Access Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.7.2: Vendor Support Approval Workflows | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-4.7.3: Vendor Support Access Monitoring and Audit Logging | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-4.7.4: Vendor Engagement Automatic Deactivation | 1 | Technical | Automate | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## ID-5: Account Management Planning

### ID-5.1: Account Management Plan (AMP)

**Selected Tool / Product / Service:** Confluence Data Center, Jira Software Data Center

**Environment-Specific Tailoring:** One AMP covers every identity population in the cloud, the data center, the alternate site, and the fleet, and it names the products this plan selects.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** The SADD's Identity design decisions

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-5.1.1: AMP Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| ID-5.1.2: AMP Review and Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| ID-5.1.3: AMP Periodic Review and Revision | 2 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** ID-5.1.3: Its first review cannot fall in Phase 1, since the document it reviews is approved there.

### ID-5.2: AMP Compliance Verification

**Selected Tool / Product / Service:** Microsoft Entra ID Governance, CyberArk Privileged Access Manager, Splunk Enterprise, Jira Software Data Center, eMASS

**Environment-Specific Tailoring:** The monthly reconciliation compares Entra ID, Active Directory, and CyberArk with the AMP from Phase 2, and the ground control stations' account settings join it when the fleet integrates in Phase 3.

**Accountable Team:** Security Team (ISSM)

**Dependencies:** ID-5.1, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C07](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| ID-5.2.1: AMP-to-Configuration Reconciliation | 2 | Technical | Automate | Level 2 | Periodic (Monthly) (re-rated) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| ID-5.2.2: AMP Compliance Finding Remediation and Escalation | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Re-rated:** ID-5.2.1: AMP Compliance Verification reconciles monthly.
