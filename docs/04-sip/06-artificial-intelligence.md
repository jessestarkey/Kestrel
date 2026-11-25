# AI: Artificial Intelligence

*KESTREL Security Implementation Plan, Section 4 (Protect). Each record implements the outcome of the same ID in the [SADD](../03-sadd/06-artificial-intelligence.md), which holds its design intent and control mapping. See the [index](index.md) for the phases, issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*

## AI-1: Scoping, Requirements, and Design

### AI-1.1: AI Use Case Intake and Onboarding

**Selected Tool / Product / Service:** Jira Service Management Data Center, Confluence Data Center

**Environment-Specific Tailoring:** Every AI use case and new model enters through the application intake request with an AI section. It names the sponsor, the data needed, any action the use case can take, and a proposed risk tier. The path opens in late Phase 1, so the first use cases are approved before training starts. A platform model is recorded with its sponsor, provisional tier, and removal review date.

**Accountable Team:** ML Team

**Dependencies:** GV-4.4, AP-1.2

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-1.1.1: Intake Request Submission and Initial Use-Case Registration | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.1.2: Self-Reported AI Risk and Data Profile Questionnaire | 1 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.1.3: Governance Risk-Tier Routing and Review Board Submission | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.1.4: Routing and Handoff to Scoping, Requirements, and Design | 1 | Technical | Automate | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.1.5: Platform Model Intake and Expiry | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-1.2: Privacy Requirements Definition

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** Incidental imagery of people is the only personal information in the collection. The privacy officer approves each new training set's handling, and no model is trained to identify individuals. The AISP records that removing a record later means retraining rather than editing the weights.

**Accountable Team:** Program Office (privacy officer)

**Dependencies:** AI-1.1

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-1.2.1: Privacy Requirement Derivation from Data Classification and Regulatory Scope | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.2.2: Differential Privacy/Anonymization Requirement Definition | 2 | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.2.3: Privacy Requirement Sign-Off and Baseline | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-1.3: Model Selection and Justification

**Selected Tool / Product / Service:** Confluence Data Center, Azure OpenAI Service

**Environment-Specific Tailoring:** Each model choice is recorded in Confluence against its publisher's security practice, licensing, serialization format, and mission fit. Foundation models come only from the Azure OpenAI catalog inside the IL5 authorization. Detection and embedding models start from an approved pretrained checkpoint or are trained from scratch.

**Accountable Team:** ML Team

**Dependencies:** AI-1.1, AI-1.4

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-1.3.1: Model Architecture/Vendor Selection Criteria Definition | 2 | Documentation | None | Level 2 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.3.2: Model Risk Assessment | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.3.3: Selection Justification Documentation and Approval | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-1.4: Approved AI Component Catalog

**Selected Tool / Product / Service:** Confluence Data Center, JFrog Artifactory

**Environment-Specific Tailoring:** One approved component catalog lists the model families, checkpoints, frameworks, guardrail models, and registries KESTREL may use. The ML Team curates it and the AI/ML Governance Review Board approves additions. Artifactory's mirror and model registry accept only what it lists.

**Accountable Team:** ML Team

**Dependencies:** GV-4.4

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-1.4.1: AI Component Vetting Criteria and Catalog Publication | 1 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-1.4.2: ISSE Ownership and Review Cadence | 2 | Process | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.4.3: Fast-Track Suspension and Removal | 2 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.4.4: New Component Request Process | 2 | Documentation | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AI-1.4.1: KESTREL's design depends on it from the first build, since the Phase 2 training build draws only on the approved catalog.

### AI-1.5: Model Provenance and Integrity Verification

**Selected Tool / Product / Service:** Sigstore Cosign, JFrog Artifactory

**Environment-Specific Tailoring:** Every pretrained checkpoint is checked against its publisher's signature or published digest as it enters Artifactory, and refused if either fails. Each Azure OpenAI deployment records the exact model version it serves, and an unapproved version alerts the ML Team.

**Accountable Team:** ML Team

**Dependencies:** AI-1.4, AP-2.7

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-1.5.1: Model Source/Provenance Validation | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.5.2: Model Artifact Hash/Signature Verification | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-1.6: Robustness Requirements Definition

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** Each model's robustness requirements come from its threat model and the mission's reliance on it. Detection models must hold under weather, sensor faults, camouflage, and RF deception, and language model use cases must resist jailbreaks and injected instructions. The AISP states each as a measurable threshold.

**Accountable Team:** ML Team

**Dependencies:** AI-1.7

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-1.6.1: Robustness Requirement Derivation from Threat Model and Use Case Criticality | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.6.2: Robustness Acceptance Criteria and Testing Scope Definition | 2 | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-1.7: AI Threat Modeling

**Selected Tool / Product / Service:** Threagile (the program's custom image, with IL5 and ATLAS risk rules), Confluence Data Center

**Environment-Specific Tailoring:** The ML Team models every model and each mission team every use case in Threagile. The custom image's AI risk rules cite their MITRE ATLAS techniques. The models cover poisoning through feedback and federated updates, evasion, injection through retrieved reports, and capture of an aircraft's model. The PMO ISSE reviews each at the design gate.

**Accountable Team:** ML Team, with the mission teams for their use cases

**Dependencies:** AI-1.1, AP-1.4

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-1.7.1: AI-Specific Threat Taxonomy Adoption | 2 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.7.2: AI Threat Model Creation at Design-Review Gate | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AI-1.7.3: AI Threat-Model-Finding-to-Backlog Conversion | 2 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-1.8: OT and Safety-Critical AI Governance

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** No KESTREL model may command an aircraft, its flight controls, or its payload. Onboard models only cue the operator, and the mission-planning agent's drafts take effect only after an operator approves. Mission Team 2 builds that approval gate, and Fleet Operations keeps the AI/OT boundary at the stations.

**Accountable Team:** Program Office (chief engineer), with Mission Team 2 and Fleet Operations for the authorization gates

**Dependencies:** AI-1.1

**Funding Line:** FY28 program management

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-1.8.1: OT-Adjacent AI Prohibited Use Case Policy | 2 | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.8.2: OT-Adjacent AI Risk Assessment Gate | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-1.8.3: AI/OT Boundary Isolation Architecture | 2 | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-1.8.4: OT-Adjacent AI Action Human Authorization Gate | 2 | Technical | None | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |

## AI-2: Data Engineering

### AI-2.1: Data Poisoning Prevention and Detection

**Selected Tool / Product / Service:** Great Expectations, cleanlab, lakeFS

**Environment-Specific Tailoring:** Before the ATO, training uses government-furnished prior collection the AO admits under the interim authorization, received over F28, plus synthetic and simulator data. KESTREL's own collection, corrections, federated updates, and IL6 releases join after the ATO. Great Expectations and cleanlab screen every batch before it enters the ML training zone.

**Accountable Team:** Data Team

**Dependencies:** DA-1.1, DA-1.3, AI-1.1

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-2.1.1: Training Data Source Validation and Trust Boundary Definition | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-2.1.2: Statistical/Anomaly-Based Poisoning Detection | 2 | Technical | Automate | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-2.1.3: Poisoned Sample Quarantine and Retraining Trigger | 2 | Technical | Automate | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-2.2: Label Integrity Verification

**Selected Tool / Product / Service:** CVAT, cleanlab

**Environment-Specific Tailoring:** Labels come only from the Data Team's cleared annotators, analyst corrections, and model corrections released from the IL6 enclave. Each mission team's zone has its own CVAT instance, so the payload vendor split holds. A sample of every batch is labeled twice, and each correction is bound to its analyst or IL6 release record.

**Accountable Team:** Data Team

**Dependencies:** DA-1.1

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-2.2.1: Labeling Source/Pipeline Trust Verification | 2 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AI-2.2.2: Label Consistency/Anomaly Auditing | 2 | Technical | Automate | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-2.3: Training Data Privacy Controls

**Selected Tool / Product / Service:** Microsoft Presidio, Azure Machine Learning

**Environment-Specific Tailoring:** Presidio removes personal fields from training records. The ML Team builds a person-detection model in Phase 2 and certifies it in Phase 3, then delivers it to each zone over F26. Until then, a Data Team reviewer blurs or crops people before frames enter the training zone. The provenance record notes the technique applied.

**Accountable Team:** Data Team, with the ML Team for the person-detection model

**Dependencies:** DA-1.1, DA-1.7, AI-1.2, AI-1.4

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-2.3.1: PII Detection and Redaction/Anonymization in Training Data | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-2.3.2: Access Control on Raw Training Data Stores | 2 | Technical | None | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-2.4: Dataset Lineage and Version Control

**Selected Tool / Product / Service:** lakeFS, NetApp StorageGRID with S3 Object Lock

**Environment-Specific Tailoring:** Every training run reads an immutable lakeFS snapshot on StorageGRID in the ML training zone, identified by its content hash. Each snapshot's provenance names its source zones, release approvals, and payload vendor terms, so a model traces to its exact data and permissions.

**Accountable Team:** Data Team

**Dependencies:** DA-1.3

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C16](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-2.4.1: Dataset Versioning and Immutable Snapshotting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AI-2.4.2: Lineage Tracking | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

## AI-3: Experimentation

### AI-3.1: Secure Experimentation Environment

**Selected Tool / Product / Service:** JupyterHub on AKS, Azure Kubernetes Service, Azure Virtual Desktop

**Environment-Specific Tailoring:** JupyterHub spawns an individual notebook server per data scientist on an isolated-size node pool in ML Dev/Test. It is reached only from the ML host pool in Azure Virtual Desktop, so notebook output stays in the session. Each server sees only its user's approved datasets, and downloads are disabled.

**Accountable Team:** ML Team

**Dependencies:** ID-2.5, NE-2.7

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-3.1.1: Isolated/Sandboxed Experimentation Compute Provisioning | 2 | Technical | Automate | Level 1 | Continuous | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| AI-3.1.2: Experimentation Data Access Scoping | 2 | Technical | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-3.2: Experiment Tracking and Reproducibility

**Selected Tool / Product / Service:** Azure Machine Learning

**Environment-Specific Tailoring:** Azure Machine Learning's MLflow-compatible tracking records every run's code revision, dependencies, environment, hyperparameters, dataset snapshot, and metrics. A checkpoint without a complete run record cannot be promoted.

**Accountable Team:** ML Team

**Dependencies:** AI-3.1

**Funding Line:** FY28 and FY29 RDT&E, mission and ML, with the Phase 4 share unfunded

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-3.2.1: Experiment Metadata/Parameter Tracking | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-3.2.2: Reproducibility Validation | 4 | Technical | Automate | Level 3 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### AI-3.3: Signed/Hashed Reference Models

**Selected Tool / Product / Service:** Sigstore Cosign, Azure Key Vault Premium, JFrog Artifactory

**Environment-Specific Tailoring:** A checkpoint chosen as a reference model is signed with AP-2.13's dev/test key, bound to its run record. The training pipeline accepts only signed reference models as starting points.

**Accountable Team:** ML Team

**Dependencies:** AI-3.2, AP-2.13

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-3.3.1: Reference Model Hashing/Signing at Experiment Checkpoint | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-3.3.2: Reference Model Integrity Verification Before Promotion | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-3.4: Training Script and Feature-Engineering IP Protection

**Selected Tool / Product / Service:** GitLab Ultimate, Microsoft Entra ID

**Environment-Specific Tailoring:** Training scripts and feature-engineering code live in ML Team repositories only its members can read. Clones on performer laptops fall under the same performer controls as other source. Mission data is worked on only inside the workspaces.

**Accountable Team:** Platform Team

**Dependencies:** AP-2.22

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-3.4.1: Access Control and Encryption for Training Scripts/Feature Pipelines | 2 | Technical | None | Level 1 | Periodic (Semi-Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-3.4.2: Exfiltration Monitoring for Proprietary AI Code/IP | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

## AI-4: Development and Continuous Integration

### AI-4.1: Ephemeral, Containerized Training Environments

**Selected Tool / Product / Service:** Azure Machine Learning, JFrog Artifactory

**Environment-Specific Tailoring:** Training runs on Azure Machine Learning compute clusters of an isolated GPU size, injected into ML Dev/Test, with customer-managed keys. GV-5.12 confirms the size and its quota in both US Gov regions before Phase 2. If either falls short, a security impact analysis and the Configuration Control Board move training to on-premises GPU servers. Each run gets its own containers, and its scratch storage is destroyed when it ends.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AP-2.21, AI-2.4, GV-5.12

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.1.1: Ephemeral, Containerized Training Runner Provisioning | 2 | Technical | Automate | Level 1 | Continuous | High | One-Time: High; Recurring: High | Medium-term (3–6 months) |
| AI-4.1.2: Environment Teardown and Residual-Data Wipe Enforcement | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AI-4.2: Least-Privilege Training Infrastructure Access

**Selected Tool / Product / Service:** Azure Machine Learning, Microsoft Entra Workload ID

**Environment-Specific Tailoring:** Each training identity reads only the snapshots its run declares and writes only to its run's output, which the release runners collect. ML engineers hold no privileged roles on the training cluster. The Platform Team performs privileged operations for them from its admin VDI host pool under ID-4.3, reviewed twice a year.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AI-2.4, ID-4.3

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.2.1: Training Infrastructure Role/Scope Definition | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-4.2.2: Periodic Training Infrastructure Access Review | 2 | Process | None | Level 1 | Periodic (Semi-Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.3: Training Cluster Network Segmentation and Egress Control

**Selected Tool / Product / Service:** Palo Alto Networks VM-Series, Azure Policy

**Environment-Specific Tailoring:** The cloud hub keeps ML Dev/Test from every prod spoke except F25's shared services. Training pulls images and approved checkpoints from the registry and mirror, and reads the ML training zone across the circuit. Trained artifacts leave only when Platform Prod's runners collect them over F24.

**Accountable Team:** Platform Team

**Dependencies:** NE-1.5, NE-2.4

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C08](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.3.1: Training Cluster Network Isolation/Segmentation | 2 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-4.3.2: Egress Allow-Listing and Data-Exfiltration Monitoring | 2 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

### AI-4.4: Training Code Static Analysis

**Selected Tool / Product / Service:** GitLab SAST

**Environment-Specific Tailoring:** Training scripts and data loaders go through the shared pipeline's SAST, with rules for the ML frameworks used. The rules include checks for unsafe deserialization and shell execution.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AP-2.3

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.4.1: SAST Tool Integration Into Training Pipeline | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-4.4.2: Training Code Rule/Ruleset Tuning and False-Positive Baseline | 2 | Process | None | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.5: Training Code Secret Scanning

**Selected Tool / Product / Service:** Gitleaks pre-commit hooks, GitLab Secret Detection

**Environment-Specific Tailoring:** Training repositories get AP-2.4's secret scanning. Training jobs hold no static secret, since they authenticate with workload identity.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AP-2.4

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.5.1: Secret Scanning Tool Integration Into Training Pipeline | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-4.5.2: Training Repository Historical Scan and Remediation | 2 | Technical | Automate | Level 1 | One-Time | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.6: AI Dependency Vulnerability Scanning

**Selected Tool / Product / Service:** GitLab Dependency Scanning, JFrog Xray

**Environment-Specific Tailoring:** Every training and serving image's dependencies are scanned on each build and daily afterward. Frameworks, tokenizers, and accelerator toolkits come only through Artifactory.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AP-2.8

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.6.1: AI Framework/Library Dependency Scanning Integration | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-4.6.2: Dependency Update/Patch Policy Enforcement | 2 | Process | None | Level 1 | Periodic (Monthly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.7: Model Artifact Malware/Unsafe-Deserialization Scanning

**Selected Tool / Product / Service:** ModelScan, JFrog Artifactory

**Environment-Specific Tailoring:** ModelScan checks every artifact entering the model registry for embedded code. KESTREL accepts weights only in non-executable formats such as safetensors, and pickle-based formats are refused.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AI-1.4

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.7.1: Pretrained/Base Model Artifact Scanning | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-4.7.2: Scan-Gate Enforcement Before Training/Serving Pipeline Ingestion | 2 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.8: Training Infrastructure IaC Scanning

**Selected Tool / Product / Service:** GitLab IaC Scanning, Gatekeeper and Conftest

**Environment-Specific Tailoring:** The infrastructure as code for the training cluster, snapshots, and model registry is scanned with the same policy as all other infrastructure code.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AP-2.15

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.8.1: IaC Scanning Tool Integration for Training Infrastructure | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-4.8.2: Misconfiguration Policy Baseline and Gating | 2 | Process | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.9: Training Pipeline Fuzz Testing

**Selected Tool / Product / Service:** Fuzzing harnesses (libFuzzer, AFL++, Jazzer)

**Environment-Specific Tailoring:** libFuzzer, AFL++, and Jazzer fuzz the data loaders for each payload vendor's raw formats, federated updates, and IL6 releases on each change. These are the inputs the pipeline did not produce itself.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AP-2.21

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.9.1: Training Pipeline Fuzz Testing Tool Integration | 2 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-4.9.2: Training Pipeline Crash/Finding Triage and Remediation Workflow | 2 | Process | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.10: Training Pipeline API/Interface Testing

**Selected Tool / Product / Service:** GitLab API Fuzzing

**Environment-Specific Tailoring:** GitLab API Fuzzing tests the training platform's job, dataset, and registry interfaces for authorization flaws. One check confirms a training identity cannot mount another run's snapshot or write another run's output.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AI-4.2

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.10.1: Pipeline API/Interface Security Test Integration | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-4.10.2: Training Pipeline Authentication/Authorization Abuse Testing | 2 | Process | None | Level 2 | Periodic (Event-Driven) | High | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.11: Training Pipeline Misuse/Abuse Case Testing

**Selected Tool / Product / Service:** Azure Machine Learning, PyRIT

**Environment-Specific Tailoring:** Abuse cases from each threat model run against the training pipeline in ML Dev/Test. Examples include a crafted federated update, a correction flood from one account, and a run that tries another snapshot.

**Accountable Team:** ML Team, with the Security Team

**Dependencies:** AI-1.7

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.11.1: Misuse/Abuse Case Scenario Definition | 2 | Documentation | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-4.11.2: Abuse Case Test Execution and Findings Tracking | 2 | Process | None | Level 2 | Periodic (Semi-Annual) | High | One-Time: Low; Recurring: Moderate | Medium-term (3–6 months) |

### AI-4.12: Signed/Verified Training Pipeline Definitions

**Selected Tool / Product / Service:** GitLab Ultimate, Sigstore Cosign

**Environment-Specific Tailoring:** Training pipeline definitions extend the Platform Team's signed templates and are verified before each run. A definition changed outside an approved merge stops the run.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AP-2.23

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.12.1: Training Pipeline-as-Code Signing and Verification | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-4.12.2: Unauthorized Training Pipeline Modification Detection | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.13: Reproducibility Controls

**Selected Tool / Product / Service:** GitLab Ultimate, JFrog Artifactory, Azure Machine Learning

**Environment-Specific Tailoring:** Every training environment pins its dependency versions and image digest. Each run hashes its assembled environment at start, compares it with the approved baseline, and halts on a mismatch. The verified hash goes in the run record and the AI-BOM. Sampled reproduction of runs starts in Phase 4, with AI-3.2.2.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AI-3.2

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.13.1: Dependency Pinning Enforcement | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-4.13.2: Environment Hash Verification at Training Run Start | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.14: Training Artifact Signing

**Selected Tool / Product / Service:** Sigstore Cosign, Azure Key Vault Premium, GitLab Ultimate, JFrog Artifactory

**Environment-Specific Tailoring:** Platform Prod's runners collect each trained artifact, sign it with AP-2.13's dev/test key, and publish it to the model registry. The signature binds it to its run record and snapshot. AP-2.13 builds the keys, so AI-4.14.1 covers only the training pipeline's use of them.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AP-2.13, AI-4.3

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.14.1: Model Signing Key Management and Infrastructure | 2 | Technical | None | Level 1 | One-Time | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| AI-4.14.2: Automated Training Artifact Signing and Verification Enforcement | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AI-4.15: AI-BOM Generation

**Selected Tool / Product / Service:** Syft (CycloneDX), JFrog Artifactory

**Environment-Specific Tailoring:** Every model version gets a CycloneDX AI-BOM listing its snapshots, base checkpoint, hyperparameters, frameworks, and payload vendor terms. It is stored in the model registry beside the artifact.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AP-2.11

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.15.1: Automated AI-BOM Generation | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-4.15.2: AI-BOM Storage and Distribution | 2 | Technical | None | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.16: Training Job Audit Logging

**Selected Tool / Product / Service:** Azure Monitor and VNet flow logs, Splunk Enterprise

**Environment-Specific Tailoring:** Every training job's submission, configuration, data access, and output is logged to Splunk, where the training platform's administrators cannot change it. The ISSO reviews the logs each week.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** DE-3.1

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.16.1: Training Job Event Capture and Immutable Logging | 2 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AI-4.16.2: Audit Log Retention and Review Workflow | 2 | Process | None | Level 1 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### AI-4.17: Privileged Config Change Alerting

**Selected Tool / Product / Service:** Azure Monitor and VNet flow logs, Splunk Enterprise Security

**Environment-Specific Tailoring:** Changes to the training platform's role assignments, managed identities, storage policies, compute policies, and gate thresholds alert the Security Team. A change with no approved request is investigated as an incident.

**Accountable Team:** Security Team

**Dependencies:** DE-3.1

**Funding Line:** FY28 O&M, platform and security operations

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.17.1: Privileged Training-Config Change Detection Rules | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-4.17.2: Privileged Config Change Alert Routing and Review Workflow | 2 | Process | None | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.18: Hyperparameter Change Alerting

**Selected Tool / Product / Service:** Azure Machine Learning, GitLab Ultimate

**Environment-Specific Tailoring:** Run tracking compares each run's hyperparameters with the envelope its certification approved. A run outside it alerts the ML Team and the PMO ISSE and needs full Certification to Field. Envelopes exist once the first models are certified in Phase 3.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** AI-3.2

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.18.1: Hyperparameter Change Detection and Baseline Diffing | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-4.18.2: Unauthorized/Anomalous Hyperparameter Change Alerting | 2 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-4.19: Training Credential Secrets Management

**Selected Tool / Product / Service:** Microsoft Entra Workload ID, Azure Key Vault Premium

**Environment-Specific Tailoring:** Training jobs reach the snapshots and the model registry with short-lived workload identity tokens. Any remaining secret comes from ML Dev/Test's Key Vault at run time.

**Accountable Team:** ML Team, on Platform Team tooling

**Dependencies:** ID-3.1, DA-3.10

**Funding Line:** FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 2, Protect and Operate

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-4.19.1: Short-Lived/Ephemeral Training Credential Issuance | 2 | Technical | Automate | Level 1 | Continuous | High | One-Time: High; Recurring: Low | Medium-term (3–6 months) |
| AI-4.19.2: Training Secrets Vault Integration | 2 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## AI-5: Validation and Continuous Delivery

### AI-5.1: Jailbreak Testing

**Selected Tool / Product / Service:** PyRIT, garak

**Environment-Specific Tailoring:** The mission teams test every language model use case against a versioned jailbreak corpus before Certification to Field, and fix what it finds. The PMO ISSE sets the corpus and thresholds as AI Cyber T&E director. The corpus adds program-specific attempts, such as asking for sources and methods.

**Accountable Team:** ML Team and mission teams, directed by the PMO ISSE

**Dependencies:** AI-1.6, AI-8.10

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-5.1.1: Jailbreak Prompt Corpus/Technique Testing | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-5.1.2: Jailbreak Finding Remediation and Guardrail Tuning | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### AI-5.2: Prompt Injection Testing

**Selected Tool / Product / Service:** PyRIT, garak

**Environment-Specific Tailoring:** PyRIT and garak test every path content takes into a language model use case, and the owning mission team fixes what they find. For the analyst assistant, that includes reports and IL6 releases. For the mission-planning agent, it includes injected tool responses.

**Accountable Team:** ML Team and mission teams, directed by the PMO ISSE

**Dependencies:** AI-1.6, AI-8.4

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-5.2.1: Direct/Indirect Prompt Injection Test Suite Execution | 3 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-5.2.2: Injection Finding Remediation and Guardrail Tuning | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### AI-5.3: Adversarial Evasion Robustness Testing

**Selected Tool / Product / Service:** Adversarial Robustness Toolbox

**Environment-Specific Tailoring:** The ML Team tests each detection model against evasion within its robustness budget, using the Adversarial Robustness Toolbox. Tests include adversarial patches and camouflage for imagery and spoofed emitters for signals. Results are measured against the AISP thresholds.

**Accountable Team:** ML Team and mission teams, directed by the PMO ISSE

**Dependencies:** AI-1.6, AI-4.14

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-5.3.1: Adversarial Example Generation and Evasion Testing | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-5.3.2: Robustness Threshold Validation Against Acceptance Criteria | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-5.4: Data Poisoning Testing

**Selected Tool / Product / Service:** Adversarial Robustness Toolbox, Flower federated learning

**Environment-Specific Tailoring:** Poisoning tests seed a controlled fraction of a snapshot with triggers and flipped labels, and of replayed federated rounds with crafted updates. The real pipeline trains in the evaluation environment, measuring what the screens and aggregator catch.

**Accountable Team:** ML Team and mission teams, directed by the PMO ISSE

**Dependencies:** AI-2.1, AI-4.14, AI-7.2

**Funding Line:** FY28 and FY29 RDT&E, mission and ML, with the Phase 3 share pending approval, with the Phase 4 share unfunded

**Rollout Phase:** Phase 3, Mission, AI, and Fleet, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-5.4.1: Simulated Poisoning Attack Testing Against Training Pipeline | 4 | Technical | Automate | Level 3 | Periodic (Annual) | High | One-Time: Moderate; Recurring: High | Medium-term (3–6 months) |
| AI-5.4.2: Poisoning Detection Control Validation | 3 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-5.5: Out-of-Distribution Robustness Testing

**Selected Tool / Product / Service:** Adversarial Robustness Toolbox, Azure Machine Learning

**Environment-Specific Tailoring:** Each detection model is tested on out-of-distribution inputs, such as new weather, terrain, sensor faults, and emitters. The test checks that it lowers its confidence rather than answering wrongly with high confidence.

**Accountable Team:** ML Team and mission teams, directed by the PMO ISSE

**Dependencies:** AI-1.6, AI-4.14

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-5.5.1: OOD Input Test Suite Execution | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-5.5.2: OOD Detection/Rejection Behavior Validation | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-5.6: Privacy-Attack Testing

**Selected Tool / Product / Service:** Adversarial Robustness Toolbox

**Environment-Specific Tailoring:** Membership inference and inversion tests run against each model trained on imagery with people and any model fine-tuned on reports. They show whether a specific record can be recovered.

**Accountable Team:** ML Team and mission teams, directed by the PMO ISSE

**Dependencies:** AI-1.2, AI-4.14

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-5.6.1: Membership Inference Attack Testing | 3 | Technical | Automate | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| AI-5.6.2: Model Inversion/Data Extraction Attack Testing | 3 | Technical | Automate | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### AI-5.7: Red Teaming

**Selected Tool / Product / Service:** the penetration testing provider, PyRIT

**Environment-Specific Tailoring:** The penetration testing contract includes an AI red team, independent of the performer, scoped by the PMO ISSE. It attacks each new use case and each foundation model change in combination. One example is a planted report that steers the assistant into misusing an agent's tool.

**Accountable Team:** Program Office (PMO ISSE), with the penetration testing provider

**Dependencies:** AI-1.7, Penetration testing provider

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C28](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-5.7.1: Red Team Exercise Scoping and Scheduling | 3 | Process | None | Level 2 | Periodic (Annual) | Moderate | One-Time: High; Recurring: High | Short-term (1–3 months) |
| AI-5.7.2: Red Team Finding Remediation Tracking and Validation | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |

### AI-5.8: Model Card Generation

**Selected Tool / Product / Service:** Azure Machine Learning, Confluence Data Center

**Environment-Specific Tailoring:** The pipeline generates a model card for each certified version from its validation results, published in Confluence. It states the model's intended use, tested limits, known failure modes, and retraining envelope.

**Accountable Team:** ML Team

**Dependencies:** AI-1.6

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-5.8.1: Automated Model Card Generation from Validation/Test Artifacts | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-5.8.2: Model Card Review and Publication Workflow | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## AI-6: Certification to Field (CtF)

### AI-6.1: Validation Report Review

**Selected Tool / Product / Service:** GitLab Ultimate, Jira Software Data Center

**Environment-Specific Tailoring:** The PMO ISSE reviews each candidate's validation report against the test classes and thresholds the AISP sets for its risk tier. Missing coverage counts as a failure, not a pass.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** AI-5.1, AI-5.3, AI-10.1

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-6.1.1: Validation Report Completeness/Accuracy Review | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AI-6.1.2: Validation Report Sign-Off and Gate Decision | 3 | Documentation | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### AI-6.2: Model Card Review

**Selected Tool / Product / Service:** Confluence Data Center, Jira Software Data Center

**Environment-Specific Tailoring:** The PMO ISSE checks each model card against its evidence before certification. A card with vague limits or a missing known failure mode is sent back.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** AI-5.8

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-6.2.1: Model Card Certification-Gate Review | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-6.2.2: Model Card Sign-Off for Deployment Gate | 3 | Documentation | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### AI-6.3: Red-Team Findings Sign-Off

**Selected Tool / Product / Service:** Jira Software Data Center

**Environment-Specific Tailoring:** Every red team finding above the AISP's must-fix severity needs a validated fix or a risk acceptance before certification. The PMO ISSE signs off on each closure, and any acceptance above Very Low goes to the AO under RK-1.4.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** AI-5.7

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-6.3.1: Red-Team Finding Remediation Verification | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AI-6.3.2: Red-Team Sign-Off and Residual-Risk Acceptance | 3 | Documentation | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Moderate | Immediate (less than one sprint) |

### AI-6.4: Risk Acceptance and Approval Log

**Selected Tool / Product / Service:** Jira Software Data Center, eMASS

**Environment-Specific Tailoring:** Every AI risk acceptance is routed under RK-1.4, and anything above Very Low goes to the AO, since every gate acceptance touches CCSD row 8 or 10. Each is logged with its rationale, approver, compensating measures, and expiry in eMASS.

**Accountable Team:** Program Office (PMO ISSE)

**Dependencies:** AI-6.1, RK-1.4

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-6.4.1: Risk Acceptance Decision Capture and Approval Routing | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AI-6.4.2: Risk Acceptance Log Audit Trail Maintenance | 3 | Technical | Automate | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-6.5: Model Deployment Risk Threshold Evaluation

**Selected Tool / Product / Service:** GitLab Ultimate, Gatekeeper and Conftest, JFrog Artifactory

**Environment-Specific Tailoring:** The pipeline combines each model's test results into one score against its risk tier's thresholds, extending AP-4.5's gate. Retraining within the approved envelope passes on that score alone, except for edge models, which always take full Certification to Field. Anything outside it goes to the PMO ISSE. A model certified on prior and synthetic data is re-certified once live collection arrives after the ATO.

**Accountable Team:** Program Office (PMO ISSE), with the Platform Team for the pipeline gate

**Dependencies:** AI-6.1, AP-4.5

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-6.5.1: Model Release Risk Scoring Definition | 3 | Documentation | None | Level 1 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| AI-6.5.2: Automated Model Promotion Go/No-Go Gate Enforcement | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-6.5.3: Version-over-Version Robustness Regression Block | 3 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-6.6: Rollback/Kill-Switch Readiness Check

**Selected Tool / Product / Service:** KServe, GitLab feature flags, the aircraft and ground equipment manufacturer's tools

**Environment-Specific Tailoring:** Each model's rollback and kill switch are rehearsed in stage before certification. Edge rollback is rehearsed on a spare aircraft, which falls back to its stored prior model or turns onboard detection off. The cutover times are recorded as evidence.

**Accountable Team:** ML Team, with Fleet Operations

**Dependencies:** AI-8.14

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-6.6.1: Rollback/Kill-Switch Mechanism Validation | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-6.6.2: Rollback Readiness Sign-Off | 3 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |

### AI-6.7: Model Registration and Inventory Logging

**Selected Tool / Product / Service:** JFrog Artifactory, Jira Service Management Assets

**Environment-Specific Tailoring:** Every certified model version is registered in Artifactory and in Jira Service Management Assets. Each record lists its owner, certification record, the use cases it is certified for, where it serves, and which aircraft carry it.

**Accountable Team:** ML Team

**Dependencies:** AP-4.7

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-6.7.1: Model Registration in Authoritative Inventory | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-6.7.2: Model Inventory Record Enrichment | 3 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-6.8: Model Optimization Governance

**Selected Tool / Product / Service:** ONNX Runtime quantization, the aircraft and ground equipment manufacturer's tools

**Environment-Specific Tailoring:** Edge models are quantized or pruned with ONNX Runtime from the cloud detection models. Each optimized artifact is certified as its own version and re-tested for accuracy and robustness. The AISP lists the approved methods.

**Accountable Team:** ML Team

**Dependencies:** AI-6.5

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C26](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-6.8.1: Approved Optimization Technique Catalog | 3 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-6.8.2: Optimization Material-Change Classification and Re-Certification | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-6.8.3: Optimization Security and Behavioral Regression Assessment | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Moderate | Short-term (1–3 months) |
| AI-6.8.4: Optimization Event Registry Documentation | 3 | Documentation | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## AI-7: Continuous Training

### AI-7.1: Automated Retraining Pipeline Security Assessments and Patching

**Selected Tool / Product / Service:** Azure Machine Learning, Tenable Security Center (ACAS), JFrog Xray

**Environment-Specific Tailoring:** The retraining pipeline's images, cluster, and platform components are scanned and patched on the VPMP's schedule, even when no model change is pending.

**Accountable Team:** ML Team

**Dependencies:** AI-4.1, DI-7.1

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references), plus government-furnished components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-7.1.1: Scheduled Retraining Pipeline Vulnerability Assessment | 3 | Technical | Automate | Level 1 | Periodic (Monthly) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-7.1.2: Automated Patching and Remediation Workflow | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AI-7.2: Retraining Data Integrity Checks

**Selected Tool / Product / Service:** Great Expectations, Flower federated learning

**Environment-Specific Tailoring:** Great Expectations validates every retraining record's schema, ranges, and labels, and checks each submitter's correction rate for floods. Federated updates arrive in batches over F3 and F18. Flower's robust aggregation strategies combine them as replayed rounds, so one aircraft cannot dominate.

**Accountable Team:** ML Team

**Dependencies:** AI-2.1, AI-7.4

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-7.2.1: Retraining Dataset Content Validation | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-7.2.2: Retraining Data Poisoning Detection | 3 | Technical | Automate | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

### AI-7.3: Secure Model Evaluation Environment

**Selected Tool / Product / Service:** Azure Machine Learning

**Environment-Specific Tailoring:** Candidates are evaluated in a disposable environment in ML Dev/Test with no route to any prod spoke beyond F25's shared services. The held-out evaluation data is readable only by the evaluation pipeline.

**Accountable Team:** ML Team

**Dependencies:** AI-4.3

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-7.3.1: Isolated Evaluation Environment Provisioning | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AI-7.3.2: Evaluation Data Access Scoping | 3 | Technical | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-7.4: Continuous Authentication of Feedback/Retraining Data

**Selected Tool / Product / Service:** Microsoft Entra Workload ID, Active Directory Certificate Services

**Environment-Specific Tailoring:** Analyst corrections are bound to the analyst's identity and the session they correct. Federated updates are authenticated by each aircraft's device certificate when the fleet integrates. IL6 releases are untrusted input and pass the same checks.

**Accountable Team:** ML Team

**Dependencies:** ID-3.7, AI-2.2

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C02](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-7.4.1: Feedback Submitter Identity/Provenance Authentication | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-7.4.2: Feedback Volume/Rate-Based Skewing Attack Detection | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

## AI-8: Model Serving

### AI-8.1: Extraction Abuse Monitoring

**Selected Tool / Product / Service:** Azure API Management, Splunk Enterprise

**Environment-Specific Tailoring:** API Management admits only approved mission team workloads to the model endpoints, and Splunk baselines each caller's queries. Sweeps that look like extraction alert the ML Team and the Security Team. Each partner's query volume through the partner API is watched the same way.

**Accountable Team:** ML Team

**Dependencies:** AI-8.2, DE-3.1

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.1.1: Query Pattern Anomaly Detection | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-8.1.2: Rate-Based Extraction Abuse Alerting and Throttling | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AI-8.2: API Abuse Protection

**Selected Tool / Product / Service:** Azure API Management

**Environment-Specific Tailoring:** API Management enforces rate limits and quotas per calling workload, and per user for language model use cases. A runaway caller cannot exhaust GPU capacity or the foundation model's quota.

**Accountable Team:** ML Team

**Dependencies:** NE-2.2

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.2.1: API Rate Limiting and Quota Enforcement | 3 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-8.2.2: Abusive Client Detection and Blocking | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AI-8.3: Third-Party/Foundation Model API Dependency Governance

**Selected Tool / Product / Service:** Azure OpenAI Service, Azure Private Link, Azure API Management

**Environment-Specific Tailoring:** Each foundation model is an Azure OpenAI deployment in KESTREL's tenant, with customer-managed keys, reached by private endpoint. Prompts carry report excerpts but never raw collection. Azure Government stores no prompts for abuse monitoring, which the ISSM confirms with the provider each year. A dev/test deployment in ML Dev/Test, reached from stage over F27, pins the same version, and a version change triggers re-testing first.

**Accountable Team:** ML Team

**Dependencies:** NE-2.1, AI-1.3, GV-5.12

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.3.1: Third-Party Model API Data Governance | 2 (pinned) | Documentation | None | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-8.3.2: Vendor Model API Credential Management and Rotation | 2 (pinned) | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-8.3.3: Vendor Security Posture Monitoring | 3 | Process | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AI-8.3.1 and AI-8.3.2: The dev/test foundation model deployment is built in Phase 2, so Phase 3 testing does not wait on it.

**Exception:** AI-8.3.2: Key-based authentication is disabled on every Azure OpenAI deployment, so no API key exists to vault or rotate. Managed identity tokens, which rotate themselves, are the only credential.

### AI-8.4: Retrieval-Augmented Generation (RAG) and Vector Store Security

**Selected Tool / Product / Service:** Azure AI Search, Semantic Kernel, Open Policy Agent policy decision service

**Environment-Specific Tailoring:** Azure AI Search, with customer-managed keys, indexes only the shared report zone, tagging each document by source and release markings. Retrieval enforces the requesting user's entitlements, so a partner-restricted report never reaches the wrong context. IL6 releases are marked as untrusted content in the prompt.

**Accountable Team:** Mission Team 1

**Dependencies:** AI-8.3, DA-1.2, GV-5.12

**Funding Line:** FY28 and FY29 RDT&E, mission and ML, with the Phase 3 share pending approval, with the Phase 4 share unfunded

**Rollout Phase:** Phase 3, Mission, AI, and Fleet, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.4.1: Retrieval Corpus Access Control and Source Trust Boundary Definition | 3 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-8.4.2: Retrieval Corpus Poisoning Detection | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-8.4.3: Source-Document-to-Embedding Access Control Preservation | 3 | Technical | None | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| AI-8.4.4: Embedding Inversion Resistance Testing | 4 | Technical | Automate | Level 3 | Periodic (Annual) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### AI-8.5: Input Validation

**Selected Tool / Product / Service:** Azure API Management, Self-hosted LLM Guard

**Environment-Specific Tailoring:** API Management checks every request against its endpoint's schema, types, and size limits, such as image formats and prompt length. A self-hosted LLM Guard screens prompts for injection before they reach a model. Its own models pass AI-1.4 and AI-4.7 like any other.

**Accountable Team:** ML Team

**Dependencies:** AI-8.2, AI-4.7

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.5.1: Input Schema/Type Validation | 3 | Technical | Automate | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| AI-8.5.2: Adversarial Input Filtering | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-8.6: Output Validation

**Selected Tool / Product / Service:** Semantic Kernel, Self-hosted LLM Guard

**Environment-Specific Tailoring:** Detection outputs are checked against their schema before they are stored. Language model responses render as plain text with required citations. LLM Guard blocks any response that echoes a system prompt or a credential.

**Accountable Team:** ML Team

**Dependencies:** AI-8.5

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.6.1: Output Schema/Format Validation | 3 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Immediate (less than one sprint) |
| AI-8.6.2: Sensitive-Data Leakage Output Scanning | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

### AI-8.7: Agentic Tool-Call/Action Output Validation

**Selected Tool / Product / Service:** Semantic Kernel, Azure Container Instances, Open Policy Agent policy decision service, OpenHands

**Environment-Specific Tailoring:** OPA checks every tool call the mission-planning agent makes against the tools and parameters its task authorized. Each tool runs in its own Azure Container Instances group in Mission Team 2 Prod, with hypervisor isolation and customer-managed keys. Its tools read only shared reports and collection requests, and write drafts to an operator's approval queue. The coding agent's commands and file actions reach OPA through a custom OpenHands security analyzer, and its sandbox's egress reaches only Artifactory, read-only. The OpenHands server clones, pushes, and calls Azure OpenAI. OPA is the only route from the mission-planning agent to its tools, and it denies any call it cannot evaluate. Tool responses are checked against their schemas before they return to the model.

**Accountable Team:** Mission Team 2, with the Platform Team for the coding agent

**Dependencies:** AI-1.8, AI-8.10, GV-5.12

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.7.1: Tool-Call Schema and Parameter Validation Against Action Contract | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-8.7.2: Provenance-Gated Escalation to Human Approval | 3 | Technical | Automate | Level 2 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-8.7.3: Sandboxed Tool-Call Execution Environment | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |
| AI-8.7.4: Tool Gateway Mediation and Execution Integrity | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |

### AI-8.8: Inference-Time PII Handling

**Selected Tool / Product / Service:** Microsoft Presidio, Splunk Enterprise

**Environment-Specific Tailoring:** Presidio scans prompts and inference logs for personal information and redacts it from the logs. Inference logs follow the privacy officer's retention schedule, and the provider keeps nothing.

**Accountable Team:** ML Team

**Dependencies:** AI-8.5

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.8.1: Input-Side PII Detection and Redaction | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-8.8.2: Inference Log PII Minimization/Retention Controls | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AI-8.9: Content Filtering

**Selected Tool / Product / Service:** Azure OpenAI content filters, Self-hosted LLM Guard, Microsoft Presidio

**Environment-Specific Tailoring:** Azure OpenAI's content filters and LLM Guard check every language model input and output against KESTREL's use policy. ISR content trips the default violence filter, so the program applies for modified filtering. If Microsoft declines, refused requests are queued for an analyst to review. A custom check catches classification markings above what KESTREL may hold, blocking and reporting a possible spill at once.

**Accountable Team:** ML Team

**Dependencies:** AI-8.5, Microsoft's approval of modified content filtering, GV-5.12

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.9.1: Harmful/Policy-Violating Content Filtering | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AI-8.9.2: Filter Bypass/Evasion Testing | 3 | Technical | Automate | Level 2 | Periodic (Quarterly) | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |

### AI-8.10: System Prompt Governance

**Selected Tool / Product / Service:** GitLab Ultimate

**Environment-Specific Tailoring:** Every system prompt lives in its use case's GitLab repository and is versioned with the release. Changes are reviewed like code and deployed only through the pipeline. A change to a prompt's role or limits triggers jailbreak and injection re-testing.

**Accountable Team:** Mission teams

**Dependencies:** AI-1.7

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.10.1: System Prompt Inventory and Version Control | 2 (pinned) | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-8.10.2: System Prompt Change Control Workflow | 2 (pinned) | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-8.10.3: System Prompt Security Review and Injection Hardening | 3 | Technical | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-8.10.4: System Prompt Pre-Deployment Testing and Periodic Audit | 3 | Process | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AI-8.10.1 and AI-8.10.2: System prompts are versioned from the first dev/test build, so Phase 3 testing does not wait on them.

### AI-8.11: Model Artifact Encryption and Watermarking

**Selected Tool / Product / Service:** Azure Key Vault Premium, Entrust nShield 5 HSMs, JFrog Artifactory, the aircraft's onboard trusted execution environment

**Environment-Specific Tailoring:** Model artifacts are encrypted at rest under Key Vault keys in the registry and on serving nodes. Edge models are encrypted under a key rooted in the nShield HSMs and loaded into each aircraft during maintenance. Watermarking edge models follows in Phase 4.

**Accountable Team:** ML Team

**Dependencies:** AI-6.7, DA-3.4

**Funding Line:** FY28 and FY29 RDT&E, mission and ML, with the Phase 3 share pending approval, with the Phase 4 share unfunded

**Rollout Phase:** Phase 3, Mission, AI, and Fleet, with work through Phase 4

**Target Date / Sprint:** 2029-03-31

**Contracting / Procurement Reference:** [C01](index.md#6-contracting-and-procurement-cross-references), [C10](index.md#6-contracting-and-procurement-cross-references), [C05](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.11.1: Model Artifact Encryption at Rest | 3 | Technical | None | Level 1 | Periodic (Quarterly) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-8.11.2: Model Watermarking for Provenance/Theft Attribution | 4 | Technical | None | Level 3 | Periodic (Event-Driven) | High | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### AI-8.12: On-Device Extraction Resistance

**Selected Tool / Product / Service:** the aircraft's onboard trusted execution environment

**Environment-Specific Tailoring:** Onboard models run in the aircraft's trusted execution environment, stored encrypted with keys in its crypto module. They are zeroized on tamper or loss, so a captured aircraft yields neither weights nor keys. This is built and proven on a spare aircraft in Phase 2 and applied across the fleet when it integrates in Phase 3.

**Accountable Team:** Fleet Operations, with the ML Team

**Dependencies:** ID-3.7

**Funding Line:** FY28 RDT&E, fleet integration, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C26](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.12.1: Secure Enclave/TEE Deployment for on-Device Inference | 2 (pinned) | Technical | None | Level 2 | Periodic (Event-Driven) | Extensive | One-Time: High; Recurring: Moderate | Long-term (6+ months) |
| AI-8.12.2: Model Weight Extraction Resistance Validation | 2 (pinned) | Technical | None | Level 2 | Periodic (Annual) | High | One-Time: High; Recurring: Moderate | Medium-term (3–6 months) |

**Pinned:** AI-8.12.1 and AI-8.12.2: The trusted execution environment is built and proven on a spare aircraft in Phase 2, before the fleet integrates.

### AI-8.13: Offline/Air-Gapped Model Integrity Verification

**Selected Tool / Product / Service:** ORAS offline bundles, Sigstore Cosign, Entrust nShield 5 HSMs

**Environment-Specific Tailoring:** Every model leaving for a disconnected destination travels as a signed ORAS package with its weights, digest, AI-BOM, and certification record. After Certification to Field, each edge package is counter-signed with AP-2.13's nShield fleet key. The Phase 2 spares package is a test model passed through AP-4.5's gate. From Phase 3 the transfer gateway verifies packages before IL6 staging.

**Accountable Team:** ML Team

**Dependencies:** AI-4.14, AP-2.13, AP-4.5, NE-2.10

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 2, Protect and Operate, with work through Phase 3

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C10](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.13.1: Offline Model Package Signing | 2 (pinned) | Technical | Automate | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-8.13.2: Air-Gapped Integrity Verification at Load Time | 2 (pinned) | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AI-8.13.1 and AI-8.13.2: Edge package signing and verification are proven on the spare stations in Phase 2, with AP-2.13.

### AI-8.14: Rollback/Kill-Switch Mechanism

**Selected Tool / Product / Service:** KServe, GitLab feature flags, the aircraft and ground equipment manufacturer's tools, Splunk SOAR containment playbooks under the CSSP agreement

**Environment-Specific Tailoring:** KServe serves from isolated-size node pools in ML Prod, and each endpoint can return to its previous certified version in minutes. The owning team operates each kill switch directly. The Security Team and the CSSP trigger one only through the containment playbook that suspends a workload or AI agent identity. Each aircraft keeps its prior certified edge model. An agent that misbehaves is first limited to read-only drafting, then suspended, and its session record is kept as evidence.

**Accountable Team:** ML Team

**Dependencies:** AI-6.7

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C26](index.md#6-contracting-and-procurement-cross-references), [C31](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.14.1: Model Version Rollback Capability | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Short-term (1–3 months) |
| AI-8.14.2: Kill-Switch Trigger Integration | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-8.14.3: Graduated Agent Containment | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |

### AI-8.15: Agent Memory Security

**Selected Tool / Product / Service:** Semantic Kernel, OpenHands

**Environment-Specific Tailoring:** Semantic Kernel holds the mission-planning agent's working memory in process for one session and discards it at session end. No persistent memory store is deployed, and the AISP records the one-session rule. OpenHands conversation storage is disabled, so the coding agent keeps nothing after a session ends.

**Accountable Team:** Mission Team 2, with the Platform Team for the coding agent

**Dependencies:** ID-3.3

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-8.15.1: Agent Memory Scope and Retention Definition | 3 | Technical | None | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-8.15.2: Memory Write Authorization and Provenance Labeling | N/A | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Medium-term (3–6 months) |
| AI-8.15.3: Memory Content Screening and Poisoning Detection | N/A | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |

**Not applicable:** AI-8.15.2: No KESTREL agent writes persistent memory. The first that does is approved under AI-8.15.1 and brings this activity with it. AI-8.15.3: No KESTREL agent writes persistent memory. The first that does is approved under AI-8.15.1 and brings this activity with it.

## AI-9: Operations and Continuous Monitoring

### AI-9.1: Model Drift Detection and Alerting

**Selected Tool / Product / Service:** Self-hosted Evidently, Splunk Enterprise

**Environment-Specific Tailoring:** A self-hosted Evidently job tracks each fielded model's output distribution, confidence, and accuracy against returning analyst corrections, reporting to Splunk. Drift past the model card's limits alerts the ML Team and the owning mission team.

**Accountable Team:** ML Team

**Dependencies:** AI-6.7, DE-3.1

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-9.1.1: Model Performance/Output Drift Monitoring | 3 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-9.1.2: Drift Threshold Alerting and Retraining Trigger | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-9.1.3: Model Health/Performance Dashboard | 3 | Technical | Visualize | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |

### AI-9.2: Data Drift Detection and Alerting

**Selected Tool / Product / Service:** Self-hosted Evidently, Splunk Enterprise

**Environment-Specific Tailoring:** The same Evidently job compares each model's production inputs with its training distribution, such as new terrain, season, sensor state, or emitters. Drift alerts the ML Team before accuracy visibly drops.

**Accountable Team:** ML Team

**Dependencies:** AI-6.7

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-9.2.1: Input Data Distribution Drift Monitoring | 3 | Technical | Automate | Level 1 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-9.2.2: Drift Threshold Alerting and Investigation Workflow | 3 | Process | None | Level 2 | Continuous | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-9.3: Retraining Pipeline Integrity Verification

**Selected Tool / Product / Service:** GitLab Ultimate, Splunk Enterprise

**Environment-Specific Tailoring:** Each week the fielded retraining pipeline's definition, schedule, data sources, and identities are compared with the certified versions. A difference stops retraining until it is explained.

**Accountable Team:** ML Team

**Dependencies:** AI-4.12

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-9.3.1: Retraining Pipeline Configuration Integrity Check | 3 | Technical | Automate | Level 1 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-9.3.2: Unauthorized Retraining Pipeline Change Detection | 3 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-9.4: Production Abuse Monitoring

**Selected Tool / Product / Service:** Splunk Enterprise Security

**Environment-Specific Tailoring:** Extraction alerts, quota hits, filter blocks, and rejected inputs from every endpoint are combined in Splunk Enterprise Security. The Security Team and the CSSP can see a campaign across them.

**Accountable Team:** Security Team

**Dependencies:** AI-8.1, DE-3.1

**Funding Line:** FY28 O&M, platform and security operations, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-9.4.1: Production Query/Usage Pattern Abuse Monitoring | 3 | Technical | Automate | Level 2 | Continuous | High | One-Time: Moderate; Recurring: Moderate | Medium-term (3–6 months) |
| AI-9.4.2: Abuse Finding Escalation and Response Workflow | 3 | Process | None | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-9.5: Canary Prompt Testing

**Selected Tool / Product / Service:** PyRIT, GitLab Ultimate

**Environment-Specific Tailoring:** A versioned set of canary images and prompts with known answers runs daily against every fielded model and use case. A changed answer alerts the owning team, catching a silent model or prompt change.

**Accountable Team:** ML Team

**Dependencies:** AI-6.7

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C04](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-9.5.1: Canary Prompt Suite Execution Against Production Model | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-9.5.2: Canary Test Failure Alerting and Rollback Trigger | 3 | Technical | Automate | Level 2 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-9.6: Trusted Model Registry Source Validation

**Selected Tool / Product / Service:** Ratify, Gatekeeper and Conftest, JFrog Artifactory

**Environment-Specific Tailoring:** Models are packaged as OCI artifacts through KServe's modelcar format, so Ratify can verify them. Each day every serving platform's loaded models are resolved to their digest and compared with Artifactory. A model loaded from anywhere else alerts the Security Team.

**Accountable Team:** ML Team

**Dependencies:** AP-5.3

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references), plus open source components

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-9.6.1: Model Registry Source Validation | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-9.6.2: Non-Trusted Model Source Usage Detection and Alerting | 3 | Technical | Automate | Level 1 | Continuous | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-9.7: Model Registry Hygiene Report

**Selected Tool / Product / Service:** JFrog Artifactory, Splunk Enterprise

**Environment-Specific Tailoring:** Model versions with no deployment, rollback role, open evaluation, or IL6 baseline expire on the AISP's schedule. A monthly report shows what the registry holds against those rules.

**Accountable Team:** ML Team

**Dependencies:** AI-6.7

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references), [C06](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-9.7.1: Stale/Orphaned Model Version Detection and Cleanup | 3 | Technical | Automate | Level 2 | Periodic (Monthly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-9.7.2: Model Registry Retention Policy Compliance Reporting | 3 | Documentation | Visualize | Level 2 | Periodic (Quarterly) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-9.8: Model Decommissioning and Disposal

**Selected Tool / Product / Service:** JFrog Artifactory, Azure AI Search, Jira Service Management Data Center

**Environment-Specific Tailoring:** Retiring a model deletes its weights and derived embeddings, revokes its endpoint identities, and removes it from every aircraft. The IL6 enclave's owner is told of any retired baseline, and the provider confirms deletion of any hosted copy. Its record is kept as long as its certification evidence must be.

**Accountable Team:** ML Team

**Dependencies:** AI-6.7, DI-2.3

**Funding Line:** FY28 RDT&E, mission and ML, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** [C05](index.md#6-contracting-and-procurement-cross-references), [C01](index.md#6-contracting-and-procurement-cross-references), [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-9.8.1: Model Disposal Policy and Vendor Coordination Requirements | 3 | Documentation | None | Level 1 | Periodic (Annual) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-9.8.2: Per-Model Disposal Asset Inventory | 3 | Documentation | None | Level 2 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-9.8.3: Model Decommissioning Execution and Verified Completion Record | 3 | Process | None | Level 1 | Periodic (Event-Driven) | Moderate | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

### AI-9.9: Operational Adversarial Re-Testing

**Selected Tool / Product / Service:** PyRIT, garak, Adversarial Robustness Toolbox

**Environment-Specific Tailoring:** Each fielded model and use case is re-tested each quarter against new jailbreak, injection, and evasion techniques, and the mission-planning agent each month. It is also re-tested whenever the provider changes a foundation model underneath it. Results go to the PMO ISSE, and a failure reopens certification. A change to an agent's tools, memory, or input trust also triggers a re-test.

**Accountable Team:** Program Office (PMO ISSE), with the ML Team and mission teams

**Dependencies:** AI-6.5

**Funding Line:** FY28 program management, with the Phase 3 share pending approval

**Rollout Phase:** Phase 3, Mission, AI, and Fleet

**Target Date / Sprint:** 2028-07-31

**Contracting / Procurement Reference:** None. Open source, so no new contract is needed.

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-9.9.1: Scheduled Adversarial Suite Re-Execution Against Fielded Models | 3 | Technical | Automate | Level 2 | Continuous | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-9.9.2: Out-of-Cycle Re-Testing on Model, Agent, or Suite Change | 3 | Technical | Automate | Level 2 | Periodic (Event-Driven) | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-9.9.3: Operational Threshold Breach Re-Assessment | 3 | Process | None | Level 2 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

## AI-10: AI/ML Security Planning

### AI-10.1: AI/ML Security Plan (AISP)

**Selected Tool / Product / Service:** Confluence Data Center

**Environment-Specific Tailoring:** The ML Team authors the AISP in late Phase 1, with mission team sections for their use cases and the PMO ISSE's T&E methodology. The review board reviews it and the Configuration Control Board approves it. It is revised each year and whenever a threshold, the catalog, or a foundation model changes.

**Accountable Team:** ML Team

**Dependencies:** The SADD's Artificial Intelligence design decisions, GV-1.5, GV-4.4

**Funding Line:** FY27 and FY28 RDT&E, mission and ML

**Rollout Phase:** Phase 1, Foundation, with work through Phase 2

**Target Date / Sprint:** 2028-03-31

**Contracting / Procurement Reference:** [C03](index.md#6-contracting-and-procurement-cross-references)

**Status:** Not Started

**Activity-Level Metadata:**

| Activity | Phase | Control Type | Cross-Cutting Discipline | Maturity Model | ConMon Activity | Level of Effort | Cost | Time Estimation |
|---|---|---|---|---|---|---|---|---|
| AI-10.1.1: AISP Development and Authoring | 1 | Documentation | None | Level 1 | One-Time | Moderate | One-Time: Moderate; Recurring: Low | Short-term (1–3 months) |
| AI-10.1.2: AISP Review and Approval | 1 | Process | None | Level 1 | Periodic (Event-Driven) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |
| AI-10.1.3: AISP Periodic Review and Revision | 2 (pinned) | Documentation | None | Level 1 | Periodic (Annual) | Low | One-Time: Low; Recurring: Low | Short-term (1–3 months) |

**Pinned:** AI-10.1.3: Its first review cannot fall in Phase 1, since the document it reviews is approved there.
