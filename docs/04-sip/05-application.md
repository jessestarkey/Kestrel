# AP: Application

*KESTREL Security Implementation Plan, Section 4 (Protect). Each record implements the outcome of the same ID in the [SADD](../03-sadd/05-application.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## AP-1: Planning, Requirements, and Design

### AP-1.1: Capability Gap Identification and Planning

**Selected Tool / Product / Service:** Confluence Data Center, Jira Software Data Center

**Environment-Specific Tailoring:** The PMO ISSE measures each team's practice against the SADD's Application outcomes once the mission teams are building in Phase 2. Each gap gets an owning team and a target date in this plan. The gap list is reviewed at every Certification to Field threshold review.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** AP-1.3

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-1.1.1: Current-State Security Capability Assessment | 2 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.1.2: Gap Analysis Against Control/Requirement Baseline | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.1.3: Capability Roadmap and Prioritization | 2 | Documentation | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.1.4: Resourcing and Budget Planning for Gap Closure | 2 (pinned) | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-1.1.4: Gap-closure budgeting follows the first capability gap assessment.

### AP-1.2: Application Intake and Onboarding

**Selected Tool / Product / Service:** Jira Software Data Center, Confluence Data Center

**Environment-Specific Tailoring:** Every application, service, or COTS product enters through one intake request in Jira, starting with the platform services built in Phase 1. The request names the owning team, product owner, data handled, payload vendor terms, and spoke or host. The PMO ISSE approves it before work starts. Intake opens the threat model and the security impact analysis, and nothing deploys without it.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** GV-5.1, GV-5.11

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-1.2.1: Intake Request Submission and Initial Project Registration | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.2.2: Self-Reported Data Sensitivity, Exposure, and Regulatory Scope Questionnaire | 1 (pinned) | Documentation | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.2.3: Intake Review and Onboarding Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.2.4: Routing and Handoff to Downstream Security Work | 1 | Technical | Automate | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-1.2.2: KESTREL's design depends on it from the first build, since every intake request names the data the application handles.

### AP-1.3: Security Requirements Definition

**Selected Tool / Product / Service:** Confluence Data Center, Jira Software Data Center

**Environment-Specific Tailoring:** The PMO ISSE turns the CCSD's control set into requirements kept in Confluence, such as identity provider sign-in, team-scoped authorization, and audit events. Each enters the team backlogs in Jira as an acceptance criterion with a test that proves it. Product owners accept no story until its security requirements pass.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** GV-5.1, GV-5.4

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-1.3.1: Control-to-Requirement Traceability Mapping | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.3.2: Non-Functional Security Requirements Definition | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.3.3: Requirements Validation Against Threat Model | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.3.4: Security Requirements Sign-Off and Baseline | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-1.4: Application Threat Modeling

**Selected Tool / Product / Service:** OWASP Threat Dragon with MITRE ATLAS, Confluence Data Center

**Environment-Specific Tailoring:** Each team models every application and AI use case in OWASP Threat Dragon before building, using one program methodology with MITRE ATLAS for AI. Anything partner-facing, internet-reachable, or able to act on aircraft gets the full model. The PMO ISSE reviews each at the design gate, starting with the Phase 1 platform services and their COTS integration boundaries.

**Accountable Team:** Program Office (PMO ISSE), with each owning team

**Dependencies:** AP-1.2

**Funding Line:** FY27, FY28, and FY29 program management, with the Phase 4 share unfunded

**Rollout Phase:** Phase 1, Foundation, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-1.4.1: Threat Modeling Methodology Standardization | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.4.2: Threat Modeling Tool Selection and Deployment | 1 (pinned) | Technical | None | Level 2 | One-Time | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AP-1.4.3: Risk-Based Threat Modeling Scoping and Triage | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.4.4: Threat Model Creation at Design-Review Gate | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AP-1.4.5: COTS/Third-Party Integration Boundary Threat Modeling | 1 (pinned) | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AP-1.4.6: Automated/AI-Assisted Threat Model Generation | 4 | Technical | Automate | Level 3 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-1.4.7: Threat-Model-Finding-to-Backlog Conversion | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-1.4.8: Security Champion Program for Threat Modeling | 2 | Process | None | Level 2 | Continuous | High | One-Time: Moderate; Recurring: High | Medium-term (3–6 months) |

**Pinned:** AP-1.4.2, AP-1.4.3, and AP-1.4.4: KESTREL's design depends on it from the first build, since intake opens a threat model for the first platform services. AP-1.4.5: KESTREL's design depends on it from the first build, since the Phase 1 platform services are COTS products.

## AP-2: Development and Continuous Integration

### AP-2.1: IDE Security Tools

**Selected Tool / Product / Service:** SonarQube for IDE

**Environment-Specific Tailoring:** The performer installs SonarQube for IDE in standalone mode, with telemetry disabled, on the laptops its developers use for KESTREL work. The plugins aid the developer, while the pipeline's scans stay the authoritative check. No plugin may send KESTREL code outside the boundary, so an AI assistant waits until KESTREL hosts one behind the identity-aware proxy.

**Accountable Team:** Platform Team, through the performer agreement

**Dependencies:** GV-5.6

**Funding Line:** FY28 and FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.1.1: IDE Plugin/Tool Selection and Rollout | 2 | Technical | None | Level 2 | One-Time | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-2.1.2: AI-Powered Code Security Assistant Deployment | 4 | Technical | Automate | Level 3 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.1.3: Developer Real-Time Finding Triage Workflow | 2 | Process | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-2.2: Secure Coding Standards and Build Hardening

**Selected Tool / Product / Service:** GitLab Ultimate, GitLab Runner on ephemeral AKS pods

**Environment-Specific Tailoring:** The ASP's coding standard names the approved languages and frameworks and prefers memory-safe languages for new services. The pipeline templates apply its compiler and packaging hardening settings, and a build that drops them fails. Platform services are COTS, so the standard first applies to the Platform Team's own automation.

**Accountable Team:** Platform Team

**Dependencies:** AP-6.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.2.1: Secure Coding Standard Definition | 1 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-2.2.2: Approved Component and Paved-Road Template Catalog | 2 | Technical | Automate | Level 2 | Periodic (Quarterly) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.2.3: Compiler and Linker Hardening Flag Enforcement | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-2.2.4: Error Handling and Message Disclosure | 1 | Technical | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-2.3: SAST

**Selected Tool / Product / Service:** GitLab SAST

**Environment-Specific Tailoring:** GitLab SAST runs on every merge request and merge from the first commit, with rules tuned to each team's languages. A finding at or above the ASP's threshold blocks the merge. Every exception the PMO ISSE approves is recorded against the finding.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.21, AP-6.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.3.1: SAST Tool Integration Into CI Pipeline | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AP-2.3.2: Rule/Ruleset Tuning and False-Positive Baseline | 1 | Process | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-2.3.3: Build-Gate Threshold Enforcement | 1 | Technical | Automate | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-2.3.1: Its build gate runs from the first commit, so the scan it gates must too.

### AP-2.4: Secret Scanning

**Selected Tool / Product / Service:** Gitleaks pre-commit hooks, GitLab Secret Detection

**Environment-Specific Tailoring:** Gitleaks runs as a pre-commit hook on performer laptops. A developer can skip a hook on a laptop KESTREL does not manage, so GitLab's push protection is the enforcing control. GitLab also scans every build and the full history on a schedule. A secret found in history is rotated first and removed second.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.21, GV-5.6

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.4.1: Secret Scanning Tool Integration Into CI Pipeline | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AP-2.4.2: Historical Repository Scan and Remediation | 1 | Technical | Automate | Level 1 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| AP-2.4.3: Pre-Commit Hook Enforcement | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-2.4.4: Server-Side Push Protection | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

**Pinned:** AP-2.4.1 and AP-2.4.4: KESTREL's design depends on it from the first build, since source code lives on performer laptops from the first commit. AP-2.4.3: Hooks cost little from the first commit and stop most secrets before they reach the repository.

### AP-2.5: Container Scanning

**Selected Tool / Product / Service:** GitLab Container Scanning, JFrog Xray

**Environment-Specific Tailoring:** GitLab Container Scanning checks every image before it is pushed, and Xray rescans stored images as new vulnerability data arrives. Images above the ASP's severity threshold cannot be pushed or deployed.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.7, AP-6.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.5.1: Container Image Vulnerability Scanning Integration | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AP-2.5.2: Scan-Gate Threshold Enforcement | 1 | Technical | Automate | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-2.6: Malware Scanning

**Selected Tool / Product / Service:** ClamAV, JFrog Xray

**Environment-Specific Tailoring:** ClamAV scans every package and base image the mirror fetches and every build artifact before release, with Xray flagging known malicious packages. Vendor deliveries, such as payload vendor software and COTS updates, are scanned at intake before anyone installs them, and the media intake station scans every government medium before import.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.7

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.6.1: Artifact/Dependency Malware Scanning Integration | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AP-2.6.2: Quarantine and Alerting Workflow | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-2.7: Trusted Internal Package Repository

**Selected Tool / Product / Service:** JFrog Artifactory, JFrog Xray

**Environment-Specific Tailoring:** Artifactory in Platform Prod is the only source builds resolve from, and the cloud hub blocks every other route to public package indexes. Each ecosystem's remote repository draws only from its approved upstream, including registry.gitlab.com for the scanners' images and advisory data. KESTREL's internal package names are reserved, so a public package of the same name cannot replace one.

**Accountable Team:** Platform Team

**Dependencies:** NE-2.4, DI-3.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.7.1: Internal Package Proxy Deployment and Upstream Scoping | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AP-2.7.2: Internal Namespace Reservation and Public Fallback Prohibition | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-2.7.3: Newly Published Version Quarantine Window | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-2.8: Dependency Review

**Selected Tool / Product / Service:** GitLab Dependency Scanning, JFrog Xray

**Environment-Specific Tailoring:** GitLab Dependency Scanning and Xray review every merge request that changes a dependency manifest for known vulnerabilities, license terms, and package health. A component that fails the ASP's criteria cannot merge without an approved exception.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.7, AP-6.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.8.1: Automated Dependency Review Integration | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AP-2.8.2: License Acceptance Policy Definition | 1 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-2.8.3: Component Provenance Admissibility Criteria | 1 | Process | None | Level 1 | Periodic (Semi-Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-2.9: External Runtime Service and Client-Side Code Governance

**Selected Tool / Product / Service:** Azure Application Gateway WAF v2, GitLab Ultimate

**Environment-Specific Tailoring:** The analyst portal and the signals workbench serve all their own client code, with no third-party scripts, fonts, or analytics. Content security policies set at Application Gateway block anything else. Applications call only provider services inside the boundary and Purview Information Protection in the Microsoft 365 DoD tenant, and any new one goes through intake.

**Accountable Team:** Mission teams

**Dependencies:** AP-1.2, NE-2.6

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.9.1: External Runtime Service Dependency Inventory and Governance | 2 (pinned) | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-2.9.2: Client-Side Script Integrity and Third-Party Tag Control | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-2.9.1: Mission applications, which call external runtime services, arrive in Phase 2.

### AP-2.10: Adversarial Code Review

**Selected Tool / Product / Service:** GitLab Ultimate

**Environment-Specific Tailoring:** A Security Team reviewer from outside the authoring team reads each high-risk change as an attacker would. Their approval is a required merge check. High-risk means authentication, cryptography, partner release logic, the payload vendor split, and any tool an AI agent can call. Any AI-assisted analysis runs on a model hosted in ML Prod.

**Accountable Team:** Security Team

**Dependencies:** AP-6.1

**Funding Line:** FY28 and FY29 O&M, platform and security operations, with the Phase 4 share unfunded

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.10.1: Adversarial/Red-Team Code Review Process Definition | 2 | Documentation | None | Level 2 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-2.10.2: High-Risk Change Identification Criteria | 2 | Documentation | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-2.10.3: AI-Assisted Adversarial Analysis Generation | 4 | Technical | Automate | Level 3 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.10.4: Findings Tracking and Remediation | 2 | Process | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-2.11: SBOM Generation and Enrichment

**Selected Tool / Product / Service:** Syft (CycloneDX), OWASP Dependency-Track, JFrog Artifactory

**Environment-Specific Tailoring:** Syft produces a CycloneDX SBOM for every build, stored in Artifactory beside the artifact it describes. Dependency-Track matches the SBOMs continuously against new vulnerability data, so a new flaw traces to every release that contains it.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.21

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.11.1: Automated SBOM Generation in Build Pipeline | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-2.11.2: SBOM Enrichment | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.11.3: Vulnerability Exploitability eXchange (VEX) Statement Production | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.11.4: SBOM Storage and Distribution | 1 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-2.11.1: Built in when the platform is created, since retrofitting it later costs far more. Releases built before it have no SBOM to match against new flaws.

### AP-2.12: Vendor SBOM Intake

**Selected Tool / Product / Service:** OWASP Dependency-Track, Jira Service Management Assets, the payload vendors' software and SBOMs, the aircraft and ground equipment manufacturer's tools

**Environment-Specific Tailoring:** Every software supplier's contract requires an SBOM with each delivery and update. That includes the payload vendors, the service desk vendor, and the ground equipment manufacturers. The supply chain lead checks each SBOM, loads it into Dependency-Track, and records it against its product in the inventory. A supplier that cannot provide one is recorded, and its product's monitoring is tightened.

**Accountable Team:** Program Office (supply chain lead)

**Dependencies:** AP-2.11

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C27](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.12.1: Vendor SBOM Ingestion and Validation Process | 2 | Process | Automate | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| AP-2.12.2: Vendor SBOM Vulnerability Correlation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.12.3: Vendor VEX Statement Intake and Application | 2 | Technical | Automate | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AP-2.13: Image Signing

**Selected Tool / Product / Service:** Sigstore Cosign, Azure Key Vault Premium, Entrust nShield 5 HSMs, Ratify, Gatekeeper and Conftest

**Environment-Specific Tailoring:** Cosign signs every release image and package in the pipeline with an HSM-backed Key Vault Premium key, and a separate key signs dev/test artifacts. Ratify and Gatekeeper admit to prod only images with the release signature and a Certification to Field attestation. Vendor images are re-signed once the mirror has scanned them. The fleet signing key stays in the nShield HSMs in the data center. The signing host first checks the cloud signature, the provenance, and the Certification to Field approval. A PKCS#11-enabled Cosign build then counter-signs each edge model package under the HSM card quorum. The stations and aircraft trust only that key, proven on the spares in Phase 2 and on the fleet in Phase 3.

**Accountable Team:** Platform Team, with the Tier 0 administrators for the fleet signing key

**Dependencies:** AP-2.21, DA-3.4

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.13.1: Signing Key Management and Infrastructure | 1 | Technical | None | Level 1 | One-Time | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.13.2: Automated Image Signing in Build Pipeline | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-2.13.3: Signature Verification Enforcement at Deploy | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-2.13.3: KESTREL's design depends on it from the first build, since nothing deploys without a signature.

**Exception:** AP-2.13.3: The bootstrap build of the landing zone, the hubs, GitLab, its runners, Artifactory, and the first AKS cluster runs from the privileged access workstations. It precedes the pipeline, signing, admission, and Certification to Field. Each is then rebuilt through the pipeline, with commits made only from the privileged access workstations. Each is scanned, signed, and certified before the DMZ admits developers under NE-2.7 or users under NE-2.13. Bootstrap session logs and the Azure activity log are kept and loaded into Splunk once it runs. Unsigned bootstrap releases are CCSD row 10 risk, so the AO accepts it under Risk Acceptance Process, and the CMP records it.

### AP-2.14: Base Image Lineage Report

**Selected Tool / Product / Service:** Iron Bank hardened images from Platform One, JFrog Artifactory, Syft (CycloneDX)

**Environment-Specific Tailoring:** Base images are the Platform Team's hardened images, built on Iron Bank and served from Artifactory. Every build records its base image and digest from Phase 1. The lineage report and staleness alerts follow in Phase 2, and a base past end of life fails the build.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.7

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references), plus government-furnished and open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.14.1: Base Image Provenance Tracking | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-2.14.2: Lineage Reporting and Staleness Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

**Pinned:** AP-2.14.1: Built in when the platform is created, since retrofitting it later costs far more. Images built before it have no recorded lineage.

### AP-2.15: IaC Scanning

**Selected Tool / Product / Service:** GitLab IaC Scanning, Gatekeeper and Conftest

**Environment-Specific Tailoring:** GitLab IaC Scanning and Conftest check every OpenTofu change against the same policy the landing zone's Azure Policy guardrails enforce. That covers the landing zone modules, each team's infrastructure, and the hubs' rule base. The bootstrap landing zone is rescanned and rebuilt through the pipeline once it exists.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.21

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.15.1: IaC Scanning Tool Integration Into CI Pipeline | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AP-2.15.2: Policy Rule Tuning and Misconfiguration Baseline | 1 | Process | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-2.15.1: Built in when the platform is created, since retrofitting it later costs far more. Every infrastructure change after bootstrap goes through the scan.

### AP-2.16: Container Hardening Verification

**Selected Tool / Product / Service:** Trivy misconfiguration scanning, Gatekeeper and Conftest

**Environment-Specific Tailoring:** Trivy checks every image and its Kubernetes manifest against the container hardening benchmark before release. The checks require a non-root user, a read-only filesystem, dropped capabilities, and resource limits. A failing image cannot reach the release namespace, and each waiver is tracked to its expiry.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.21

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.16.1: CIS/Benchmark Hardening Check Integration | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-2.16.2: Hardening Exception and Waiver Tracking | 1 | Documentation | None | Level 1 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-2.16.1: Its waiver tracking runs from Phase 1, so the check it waives must too.

### AP-2.17: Network Policy Verification

**Selected Tool / Product / Service:** Gatekeeper and Conftest, Azure CNI Powered by Cilium network policy

**Environment-Specific Tailoring:** Every workload ships with a deny-by-default Cilium network policy that permits only its team's mapped flows. Conftest checks the policy against the approved flow map in the pipeline, and Gatekeeper refuses a workload whose policy is missing or loosened.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.5

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.17.1: Default-Deny Network Policy Validation | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-2.17.2: Policy Drift Detection Pre-Deploy | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### AP-2.18: Pre-Merge Sensitive Repo File Change Detection

**Selected Tool / Product / Service:** GitLab Ultimate, Splunk Enterprise

**Environment-Specific Tailoring:** GitLab code owners make pipeline definitions, infrastructure as code, admission policy, dependency manifests, and the hubs' rule base sensitive paths. A change to one needs Platform Team and Security Team approval beyond the team's own reviewer. Each one raises an alert in Splunk.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.21, DE-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.18.1: Sensitive File/Path Change Detection Rules | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-2.18.2: Alert Routing and Review Workflow | 1 | Process | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

**Pinned:** AP-2.18.1: Its alert routing runs from Phase 1, so the detection it routes must too.

### AP-2.19: Policy-as-Code Evaluation

**Selected Tool / Product / Service:** Open Policy Agent policy decision service, Gatekeeper and Conftest, Ratify

**Environment-Specific Tailoring:** Open Policy Agent evaluates the pipeline's gates through Conftest and every cluster's admission through Gatekeeper, with Ratify for signatures. The AKS Azure Policy add-on stays off, so the Platform Team runs open-source Gatekeeper and a pinned Ratify release itself. Defender for Containers loses the add-on's Kubernetes posture checks, which Gatekeeper's audit reports replace. Admission runs in deny mode in every prod spoke and in stage from the first deployment after bootstrap.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.19.1: Admission/Policy-as-Code Engine Deployment | 1 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.19.2: Policy Rule Authoring and Version Control | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| AP-2.19.3: Policy Violation Blocking and Exception Workflow | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

**Pinned:** AP-2.19.3: KESTREL's design depends on it from the first build, since admission denies by default in every prod spoke after bootstrap.

### AP-2.20: Threat Model Staleness Check

**Selected Tool / Product / Service:** GitLab Ultimate, OWASP Threat Dragon with MITRE ATLAS

**Environment-Specific Tailoring:** A merge request that adds an interface, a data flow, an external connection, or an AI agent tool flags its threat model as stale. The owning team updates the model, and the PMO ISSE re-reviews it before the change reaches production. Every model is also re-reviewed each year.

**Accountable Team:** Program Office (PMO ISSE), with the Platform Team for change detection

**Dependencies:** AP-1.4

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.20.1: Architecture-Change-to-Threat-Model Diffing | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.20.2: Staleness Alerting and Re-Review Trigger | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-2.21: Ephemeral/Isolated Build Environments

**Selected Tool / Product / Service:** GitLab Ultimate, GitLab Runner on ephemeral AKS pods

**Environment-Specific Tailoring:** Every pipeline job runs on a fresh GitLab Runner pod in Platform Prod's AKS cluster, isolated from other jobs and destroyed when it ends. No build runs on a performer laptop or a long-lived host.

**Accountable Team:** Platform Team

**Dependencies:** DI-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.21.1: Ephemeral, Containerized Build Runner Provisioning | 1 (pinned) | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.21.2: Build Environment Isolation and Teardown Enforcement | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-2.21.1: KESTREL's design depends on it from the first build, since builds run only on ephemeral in-cloud runners.

**Exception:** AP-2.21.1: The bootstrap build runs from the privileged access workstations before the runners exist, under the exception recorded at AP-2.13.3.

### AP-2.22: Least-Privilege CI/Build Infrastructure Access

**Selected Tool / Product / Service:** GitLab Ultimate, Microsoft Entra Workload ID

**Environment-Specific Tailoring:** Each team's pipeline identity reaches only its own repositories, registry namespace, and dev/test spoke. Only the release identity can deploy to a release target, namely the prod spokes, the edge release path, the IL6 transfer gateway, and F35's on-premises targets. It runs on a separate protected runner, unlocked only by Certification to Field's approval.

**Accountable Team:** Platform Team

**Dependencies:** ID-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.22.1: CI Service Account Least-Privilege Scoping | 1 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| AP-2.22.2: Build Infrastructure Access Review | 1 | Process | None | Level 1 | Periodic (Semi-Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-2.23: Signed/Verified Pipeline Definitions

**Selected Tool / Product / Service:** GitLab Ultimate, Sigstore Cosign

**Environment-Specific Tailoring:** Every team's pipeline extends the Platform Team's templates. From Phase 1, an unapproved change to a pipeline definition stops the run and alerts the Platform and Security Teams. Signing the templates with Cosign, and verifying them before each job, follows in Phase 2.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.13

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.23.1: Pipeline-as-Code Signing and Verification | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.23.2: Unauthorized Pipeline Modification Detection | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AP-2.24: Build Provenance and Attestation (SLSA)

**Selected Tool / Product / Service:** GitLab Ultimate, Sigstore Cosign, Gatekeeper and Conftest

**Environment-Specific Tailoring:** Every build emits signed provenance naming its source revision, runner, pipeline definition, and inputs. Gatekeeper and Certification to Field both verify it. The ephemeral in-cloud runners put SLSA Build Level 3 within reach.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.13, AP-2.21

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.24.1: Build Provenance Attestation Generation | 1 (pinned) | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-2.24.2: Provenance Verification at Deploy Gate | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-2.24.1 and AP-2.24.2: Built in when the platform is created, since retrofitting it later costs far more. Artifacts built before it have no provenance to verify.

### AP-2.25: CI Credential and Secrets Management

**Selected Tool / Product / Service:** Microsoft Entra Workload ID, Azure Key Vault Premium

**Environment-Specific Tailoring:** Each team's jobs run under its own runner service account, federated to Entra ID through AKS workload identity, with short-lived team-scoped tokens. They fetch any remaining secret at run time from the Key Vault of the spoke the job targets. No long-lived credential sits in a pipeline variable or repository.

**Accountable Team:** Platform Team

**Dependencies:** ID-3.1, DA-3.10

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-2.25.1: Short-Lived/Ephemeral CI Credential Issuance | 1 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| AP-2.25.2: CI Secrets Vault Integration | 1 (pinned) | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-2.25.2: KESTREL's design depends on it from the first build, since the pipeline holds no stored secrets.

## AP-3: Testing and Continuous Delivery

### AP-3.1: Test Data Management and Preproduction Data Controls

**Selected Tool / Product / Service:** Microsoft Presidio

**Environment-Specific Tailoring:** Mission teams' dev, test, and stage clusters run on synthetic or sanitized data, never live mission data. Each set is sanitized inside its own team's zone, so the payload vendor split holds. It then reaches that team's dev/test spoke over F23. Presidio removes identifying text. Until AI-2.3's person-detection model is certified, a Data Team reviewer blurs or crops people by hand. After that, the model runs as a batch job in each zone's sanitizing pipeline, delivered over F26.

**Accountable Team:** Data Team, with the ML Team for the person-detection model

**Dependencies:** DA-1.1, AI-2.3

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-3.1.1: Masked and Synthetic Test Data Generation | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-3.1.2: Live Data Use Approval and Preproduction Handling Workflow | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-3.2: DAST

**Selected Tool / Product / Service:** GitLab DAST, Contrast Assess

**Environment-Specific Tailoring:** GitLab DAST scans every candidate build of the analyst portal, the signals workbench, the partner API, the LLM analyst assistant's front end, and the service desk in stage. Each scan runs unauthenticated and with a test account per role. Contrast Assess adds interactive testing in stage from Phase 4. Findings above the ASP's threshold block Certification to Field.

**Accountable Team:** Mission teams and ML Team, on Platform Team tooling

**Dependencies:** AP-2.21, AP-2.22, DI-2.1, ID-1.7

**Funding Line:** FY28 and FY29 RDT&E, mission and ML, with the Phase 4 share unfunded

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C19](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-3.2.1: DAST Tool Integration Into CD Pipeline | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AP-3.2.2: Interactive Application Security Testing (IAST) Instrumentation | 4 | Technical | Automate | Level 3 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-3.2.3: Authenticated Scan Configuration | 2 | Technical | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-3.2.4: Finding Triage and Remediation SLA | 2 | Process | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### AP-3.3: Application Security and Development (ASD) STIG Compliance

**Selected Tool / Product / Service:** DISA SCAP Compliance Checker and STIG Viewer, GitLab DAST, GitLab SAST, Confluence Data Center

**Environment-Specific Tailoring:** Every first-party application, including the Data Team's ingest code and the Platform Team's automation, is evaluated against the ASD STIG before Certification to Field. The SCAP Compliance Checker has no ASD content, so automated checks come from SAST and DAST findings mapped to ASD IDs. The rest are reviewed by hand in STIG Viewer, and open findings carry into STIG Risk Tracking.

**Accountable Team:** Mission teams and ML Team, on Platform Team tooling

**Dependencies:** AP-1.3

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-3.3.1: ASD STIG Checklist Mapping to Application Controls | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| AP-3.3.2: Automated STIG Compliance Scanning | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AP-3.3.3: STIG Finding Remediation Within CD Gate | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### AP-3.4: API Security Testing

**Selected Tool / Product / Service:** GitLab API Fuzzing

**Environment-Specific Tailoring:** GitLab API Fuzzing tests every API with a published schema from that schema in stage, including authorization tests for each role and partner. Today those are the partner API, the feedback endpoints, and the model endpoints the mission teams call.

**Accountable Team:** Mission teams and ML Team, on Platform Team tooling

**Dependencies:** AP-1.2, AP-2.21, AP-2.22, DI-2.1, ID-1.7

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-3.4.1: API Schema/Contract Security Testing | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AP-3.4.2: Authentication/Authorization Abuse Testing | 2 | Process | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-3.4.3: Rate Limiting and Injection Testing | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-3.4.4: Business Logic and Abuse Case Testing | 2 | Process | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

### AP-3.5: Penetration Testing

**Selected Tool / Product / Service:** the penetration testing provider, Jira Software Data Center

**Environment-Specific Tailoring:** The ISSM scopes each test, so the design's author does not scope its own check. The testers test all of KESTREL each year and the paths reachable from outside every six months, starting in Phase 2. They also test after a major change, such as a new spoke, interconnection, or external API. Fleet systems are tested on spares or the simulator, and each finding becomes a POA&M item retested before it closes.

**Accountable Team:** Security Team (ISSM), with the Program Office for the contract

**Dependencies:** GV-5.6, the penetration testing contract

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C28](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-3.5.1: Penetration Test Scoping and Scheduling | 2 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: High; Recurring: High | Short-term (1–3 months) |
| AP-3.5.2: Findings Remediation Tracking and Validation | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AP-3.5.3: Retest/Closure Verification | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### AP-3.6: Fuzz Testing

**Selected Tool / Product / Service:** Fuzzing harnesses (libFuzzer, AFL++, Jazzer)

**Environment-Specific Tailoring:** libFuzzer, AFL++, and Jazzer run as GitLab CI jobs against every parser of untrusted input, from Phase 3. The IL6 feedback endpoints are fuzzed before the first high-to-low transfer, then the partner API and the payload ingest code on each change. Vendor-format parsers are fuzzed in Platform Dev/Test from synthetic samples.

**Accountable Team:** Mission teams and ML Team, on Platform Team tooling

**Dependencies:** AP-2.21, AP-2.22, DI-2.1

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-3.6.1: Fuzz Testing Tool Integration | 3 (pinned) | Technical | Automate | Level 3 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-3.6.2: Crash/Finding Triage and Remediation Workflow | 3 (pinned) | Process | None | Level 3 | Periodic (Event-Driven) | High | One-Time: Low; Recurring: Moderate | Medium-term (3–6 months) |

**Pinned:** AP-3.6.1 and AP-3.6.2: The feedback endpoints parse IL6 products, so their fuzzing comes before the first high-to-low transfer in Phase 3.

## AP-4: Certification to Field (CtF)

### AP-4.1: Branch Protection Policy Report

**Selected Tool / Product / Service:** GitLab Ultimate, Splunk Enterprise

**Environment-Specific Tailoring:** Protected branches require a second reviewer, passing checks, and signed commits, with no administrator bypass, from the first commit. From Phase 1 a daily scan reports any repository that has drifted and opens a ticket to its owning team. The compliance report follows in Phase 2 and is part of Certification to Field's evidence.

**Accountable Team:** Platform Team, reporting to the PMO ISSE

**Dependencies:** AP-2.21

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-4.1.1: Branch Protection Rule Enforcement Scanning | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-4.1.2: Non-Compliant Repository Remediation Workflow | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-4.1.3: Branch Protection Compliance Reporting | 2 | Documentation | Visualize | Level 2 | Periodic (Monthly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-4.1.1: Its remediation workflow runs from Phase 1, so the scan that feeds it must too.

### AP-4.2: Artifact Bundle Integrity Verification

**Selected Tool / Product / Service:** Sigstore Cosign, JFrog Artifactory, ORAS offline bundles

**Environment-Specific Tailoring:** Each release bundle's member digests are recorded when it is assembled and checked again at deployment to a prod spoke or an F35 target, from Phase 1. The check extends to staging for the IL6 transfer in Phase 3. It is proven at a spare station in Phase 2 and runs at every station when the fleet integrates.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.13

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-4.2.1: Build-to-Deploy Artifact Hash/Signature Verification | 1 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-4.2.2: Artifact Bundle Tamper Detection and Blocking | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-4.2.1: Its blocking step runs from Phase 1, so the manifest check it acts on must too.

### AP-4.3: Approver and Reviewer Audit Log

**Selected Tool / Product / Service:** GitLab audit event streaming, Splunk Enterprise, Microsoft Entra ID Governance

**Environment-Specific Tailoring:** GitLab audit event streaming forwards every review, approval, dismissal, and override to Splunk, where Platform Team administrators cannot change it. Each approval is checked against the approver's Entra ID Governance entitlement at the time.

**Accountable Team:** Platform Team, with the Security Team

**Dependencies:** DE-3.1

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-4.3.1: Approval/Review Event Capture and Immutable Logging | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-4.3.2: Separation-of-Duties Validation | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-4.4: Runtime Security Baseline

**Selected Tool / Product / Service:** GitLab Ultimate, Gatekeeper and Conftest

**Environment-Specific Tailoring:** Each release carries a versioned runtime baseline covering its workload identity, privileges, filesystem, resource limits, and exposed interfaces. Stage runs the release against it before Certification to Field, so a release that would run differently in production is caught first.

**Accountable Team:** Platform Team, with each owning team

**Dependencies:** AP-2.19

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-4.4.1: Runtime Configuration Baseline Definition | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-4.4.2: Pre-Deployment Baseline Conformance Check | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AP-4.5: Deployment Risk Threshold Evaluation

**Selected Tool / Product / Service:** GitLab Ultimate, Jira Software Data Center, Gatekeeper and Conftest

**Environment-Specific Tailoring:** Certification to Field gates every release from the first platform services in Phase 1. The pipeline combines each release's findings into one risk score against the ASP's thresholds. A release outside them goes to the PMO ISSE, who approves it, sends it back, or routes it under RK-1.4. Releases are CCSD row 10, so residual risk above Very Low goes to the AO.

**Accountable Team:** Program Office (PMO ISSE), with the Platform Team for the pipeline gate

**Dependencies:** AP-6.1, AP-2.3, AP-2.5, AP-2.8, AP-2.13, AP-2.24, RK-1.4

**Funding Line:** FY27 program management

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-4.5.1: Risk Scoring Model Definition | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Low; Recurring: Low | Medium-term (3–6 months) |
| AP-4.5.2: Automated Go/No-Go Gate Enforcement | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-4.5.3: Risk Acceptance and Exception Workflow for Threshold Overrides | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

**Exception:** AP-4.5.2: The bootstrap build runs before Certification to Field exists, under the exception recorded at AP-2.13.3.

### AP-4.6: Application Rollback, Progressive Delivery, and Feature Flag Governance

**Selected Tool / Product / Service:** Azure Kubernetes Service, GitLab feature flags

**Environment-Specific Tailoring:** Every prod spoke keeps the previous certified release ready to roll back to. New releases reach a small share of traffic first and widen only if security and health signals stay clean. Feature flags are GitLab configuration, so changing one is a reviewed change.

**Accountable Team:** Mission teams and ML Team

**Dependencies:** AP-4.5

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-4.6.1: Verified Rollback Path to a Previously Certified Release | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-4.6.2: Progressive Delivery and Automated Abort on Security Signal | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-4.6.3: Security-Relevant Feature Flag Change Control | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-4.7: Application Registration and Inventory Logging

**Selected Tool / Product / Service:** Jira Service Management Assets, GitLab Ultimate

**Environment-Specific Tailoring:** Deployment to any release target fails unless the application is registered in Jira Service Management Assets. The record names its owning team, product owner, data handled, and version. Registration happens at intake, and the pipeline updates the version with each release.

**Accountable Team:** Platform Team, with IT Operations for the inventory

**Dependencies:** DI-1.1, AP-1.2

**Funding Line:** FY27 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation

**Target Date / Sprint:** 2027-09-30

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-4.7.1: Application Registration in Authoritative Inventory | 1 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-4.7.2: Inventory Record Enrichment | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## AP-5: Operations and Continuous Monitoring

### AP-5.1: Architecture Risk Tracking

**Selected Tool / Product / Service:** Jira Software Data Center

**Environment-Specific Tailoring:** Design risks a threat model identified and the AO accepted, or the PMO ISSE accepted under the standing delegation, go into one Jira register. Each carries its owner, rationale, compensating measures, and review date. The register feeds the program's risk register.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** AP-1.4, RK-1.4

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.1.1: Architecture Risk Register Maintenance | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AP-5.1.2: Risk Trend Reporting and Escalation | 2 | Process | Visualize | Level 2 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-5.2: STIG Risk Tracking

**Selected Tool / Product / Service:** eMASS, Jira Software Data Center

**Environment-Specific Tailoring:** Each open ASD STIG finding against a fielded application is bound to a POA&M item in eMASS with a remediation milestone. The Security Team reports the open findings with each continuous monitoring cycle.

**Accountable Team:** Security Team

**Dependencies:** AP-3.3

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.2.1: STIG Finding Register and Ongoing ConMon POA&M Linkage | 2 | Documentation | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AP-5.2.2: STIG Risk Trend Reporting and Escalation | 2 | Process | Visualize | Level 2 | Periodic (Monthly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-5.3: Trusted Registry ConMon Report

**Selected Tool / Product / Service:** Gatekeeper and Conftest, Ratify, Splunk Enterprise

**Environment-Specific Tailoring:** Gatekeeper lets a cluster pull only from Artifactory. A continuous check confirms every running workload resolves to it, and any image from elsewhere alerts the Security Team in Splunk.

**Accountable Team:** Platform Team, with the Security Team for the alerts

**Dependencies:** AP-2.19

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.3.1: Trusted Registry Source Validation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-5.3.2: Non-Trusted Registry Usage Detection and Alerting | 2 | Technical | Automate | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-5.4: Registry Hygiene Report

**Selected Tool / Product / Service:** JFrog Artifactory

**Environment-Specific Tailoring:** Artifactory retention keeps every fielded release, the certified release before it, and every release baselined to the IL6 enclave. Other images expire on the ASP's schedule, and a monthly report shows where the registry departs from those rules.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.7, AP-6.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.4.1: Stale/Orphaned Image Detection and Cleanup | 2 | Technical | Automate | Level 2 | Periodic (Monthly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-5.4.2: Registry Retention Policy Compliance Reporting | 2 | Documentation | Visualize | Level 2 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-5.5: Deployment Inventory Report

**Selected Tool / Product / Service:** Jira Service Management Assets, Splunk Enterprise, JFrog Artifactory

**Environment-Specific Tailoring:** The deployment inventory reads the versions running in every prod spoke and every F35 target, and compares them with what Certification to Field approved. The edge model versions each aircraft reports join it on the spares in Phase 2 and across the fleet when it integrates. Anything running that was never certified is flagged.

**Accountable Team:** Security Team

**Dependencies:** AP-4.5, AP-4.7

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.5.1: Deployed Version/Environment Inventory Collection | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-5.5.2: Inventory Drift Detection | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AP-5.6: Unified Vulnerability Dashboard

**Selected Tool / Product / Service:** OWASP Dependency-Track, Splunk Enterprise, JFrog Xray

**Environment-Specific Tailoring:** A Splunk dashboard combines every scanner's and tester's findings for each application, deduplicated and ranked by risk. The owning teams, the Security Team, and the PMO ISSE work from it, and the CSSP's analysts read it through their host pool.

**Accountable Team:** Platform Team, with the Security Team and the PMO ISSE as readers

**Dependencies:** AP-2.8, AP-2.11, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.6.1: Vulnerability Data Aggregation Across Scanning Tools | 2 | Technical | Automate | Level 2 | Continuous | Extensive | One-Time: High; Recurring: Moderate | Long-term (6+ months) |
| AP-5.6.2: Unified Risk Scoring and Prioritization View | 2 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-5.6.3: Dashboard Access and Stakeholder Reporting | 2 | Technical | Visualize | Level 2 | Periodic (Monthly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-5.7: Runtime API Inventory and Governance

**Selected Tool / Product / Service:** Azure API Management, Azure Application Gateway WAF v2, Palo Alto Networks VM-Series, Splunk Enterprise

**Environment-Specific Tailoring:** API Management, Application Gateway, and the cloud hub's traffic logs report every API endpoint actually answering requests to Splunk, east-west calls included. Each is compared with the schemas registered at intake. An undocumented route or a retired version still answering is flagged to its owning team.

**Accountable Team:** Security Team

**Dependencies:** NE-2.6, AP-1.2

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C08](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.7.1: Shadow/Undocumented API Discovery | 2 | Technical | Automate | Level 1 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| AP-5.7.2: API Inventory Enrichment | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-5.8: Secrets Management Audit

**Selected Tool / Product / Service:** Azure Key Vault Premium, Defender for Key Vault, Splunk Enterprise

**Environment-Specific Tailoring:** The secrets in every deployed environment are enumerated and reconciled against what each spoke's Key Vault issued. Defender for Key Vault alerts on unusual access. A secret nobody issued, or one unused since its last rotation, is flagged for removal.

**Accountable Team:** Security Team

**Dependencies:** DA-3.10

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.8.1: Runtime Secrets Inventory and Usage Audit | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-5.8.2: Audit Finding Remediation and Rotation | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### AP-5.9: Runtime Application Self-Protection (RASP)

**Selected Tool / Product / Service:** Contrast Protect

**Environment-Specific Tailoring:** Contrast Protect instruments the analyst portal, the signals workbench, the partner API, and the LLM analyst assistant's front end. It starts in monitor mode and blocks once each application's rules are tuned. Its events go to Splunk.

**Accountable Team:** Mission teams

**Dependencies:** AP-3.2

**Funding Line:** FY29 RDT&E, mission and ML, with the Phase 4 share unfunded

**Rollout Phase:** Phase 4, Maturity

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C19](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.9.1: RASP Agent Deployment and Application Instrumentation | 4 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-5.9.2: RASP Detection and Blocking Policy Definition | 4 | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-5.10: Vulnerability Disclosure Program

**Selected Tool / Product / Service:** the DoD Vulnerability Disclosure Program, Jira Software Data Center

**Environment-Specific Tailoring:** KESTREL's internet-reachable endpoints are enrolled in the DoD Vulnerability Disclosure Program. Every role needs a CAC or ECA credential, so researchers may test only the edge before sign-in. DC3 handles acknowledgment and disclosure timing, and the Security Team tracks each relayed report to closure like a penetration test finding.

**Accountable Team:** Security Team

**Dependencies:** NE-2.13

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.10.1: Vulnerability Disclosure Policy Publication and Researcher Intake Channel | 2 | Documentation | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-5.10.2: Reported Finding Triage and Disposition Workflow | 2 | Process | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AP-5.10.3: Researcher Acknowledgment and Coordinated Disclosure Timeline | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AP-5.11: Compliance Evidence Collection Automation

**Selected Tool / Product / Service:** GitLab Ultimate, Azure Blob Storage with immutability policies, Confluence Data Center

**Environment-Specific Tailoring:** The pipeline files every scan result, gate decision, approval, attestation, and conformance report in immutable Blob Storage as it is produced. Each is tagged to its outcome and control. Certification to Field and the SCA both draw from that store.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.24

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.11.1: Automated Evidence Artifact Collection and Control Tagging | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| AP-5.11.2: Evidence Freshness/Staleness Tracking | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-5.11.3: Evidence Export Pipeline | 2 | Technical | Automate | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AP-5.12: Fielded Dependency Vulnerability Monitoring

**Selected Tool / Product / Service:** OWASP Dependency-Track, Jira Service Management Data Center

**Environment-Specific Tailoring:** Dependency-Track matches every fielded release's SBOM daily against new disclosures. A newly vulnerable dependency opens a Jira Service Management ticket to the owning team with the VPMP's deadline. The fix ships as a rebuilt release through the normal pipeline.

**Accountable Team:** Platform Team, with the owning teams

**Dependencies:** AP-2.11, DI-7.1

**Funding Line:** FY27 and FY28 O&M, platform and security operations

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-5.12.1: Continuous Dependency Vulnerability Rescanning | 1 (pinned) | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AP-5.12.2: Dependency Patch Timeframe Policy | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-5.12.1: Releases fielded from Phase 1 need new vulnerabilities matched from the start.

## AP-6: Application Security Planning

### AP-6.1: Application Security Plan (ASP)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** The PMO ISSE authors the ASP in Phase 1, since its thresholds gate the first releases, and the Platform Team writes the pipeline sections. The Security Team reviews it and the Configuration Control Board approves it. It is revised each year and whenever a threshold or the coding standard changes.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** The SADD's Application design decisions, GV-1.5

**Funding Line:** FY27 and FY28 program management

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AP-6.1.1: ASP Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AP-6.1.2: ASP Review and Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AP-6.1.3: ASP Periodic Review and Revision | 2 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AP-6.1.3: Its first review cannot fall in Phase 1, since the document it reviews is approved there.
