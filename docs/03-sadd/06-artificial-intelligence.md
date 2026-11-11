# AI: Artificial Intelligence

*KESTREL SADD, Section 5 (Protect). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## AI-1: Scoping, Requirements, and Design

### AI-1.1: AI Use Case Intake and Onboarding

**Design Intent:** Every AI use case and every new model enters through the application intake path with an AI section added. It names the sponsoring intelligence mission lead, the data the use case needs, any action it can take, and a proposed risk tier. The AI/ML Governance Review Board (`GV-4.4`) approves the use case, with any conditions, before any corpus is assembled.

**NIST Control Mapping:**

- **SA-3 (partial):** claimed partial for the project-initiation stage of the ML pipeline's own lifecycle, a subject slice of the claim the Application focus area's Application Intake and Onboarding also holds. The base control is cited because its enhancements cover preproduction environments, live data use, and technology refresh, none of which this outcome performs.
- **Declined:** RA-2 and RA-3 are not claimed, because the team's answers are self-declared rather than a categorization or an assessment. PT-2, PT-3, and RA-8 belong to Privacy Requirements Definition. CA-6 is not claimed, since admitting a use case is not an authorization to operate, and tiering and approval stay with the Manage pillar's AI/ML Governance Review Board.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-1.1.1: Intake Request Submission and Initial Use-Case Registration**
    - **Description:** Establish a single submission path through which a data scientist or product owner proposes a new ML use case or a materially new use of a model the program already fields, record the decision the model supports, the named model owner and program sponsor accountable for its security, and the expected delivery timeline as a provisional use-case record, and document the intake form's required fields in the AISP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the roles-and-responsibilities dimension of the outcome's SA-3 (partial) mapping, since naming an owner and sponsor fills the roles the control requires. A single path matters more for ML than for software, because notebook work can reach a fielded decision path without ever looking like a project. Registering a materially new use of an already-fielded model is in scope, since repurposing moves the privacy, threat, and governance picture without new code.

- **AI-1.1.2: Self-Reported AI Risk and Data Profile Questionnaire**
    - **Description:** Have the requesting team answer a short, fixed questionnaire on the data sources and personal information the use case expects to consume, whether the model will be trained from scratch, fine-tuned, or obtained from an external publisher or hosted service, who can reach the inference interface, and whether the output is advisory or acted on automatically, then attach the answers to the intake record as self-reported, unverified input and document the questionnaire's fixed content in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** RA-2 and RA-3 are not claimed, because a team's unverified expectation is neither a categorization nor a risk assessment, and PT-2, PT-3, and RA-8 stay with Privacy Requirements Definition. Marking the answers unverified keeps an early guess from being read later as settled fact. This activity is Level 1, unlike the Application focus area's Level 2 questionnaire, because Privacy Requirement Derivation from Data Classification and Regulatory Scope and AI Threat Model Creation at Design-Review Gate both start from these answers.

- **AI-1.1.3: Governance Risk-Tier Routing and Review Board Submission**
    - **Description:** Submit each completed intake record and questionnaire into the Manage pillar's AI/ML governance process for risk tiering and review board adjudication, and hold the use case open until that review's decision is recorded against the intake record, with no data engineering or training work authorized to begin before then.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the risk-management-integration dimension of the outcome's SA-3 (partial) mapping. CA-6 is not claimed, and the approval decision itself belongs to the Manage pillar's Use-Case Review/Approval Workflow. What is built here is the submission, the routing, and the hold, so nothing proceeds to data engineering while a decision is outstanding. Keep review turnaround short, because teams route around a slow board by prototyping first.

- **AI-1.1.4: Routing and Handoff to Scoping, Requirements, and Design**
    - **Description:** On the recorded approval, have the intake tooling open linked, tracked items for the use case's Privacy Requirements Definition and AI Threat Modeling work, assign them to the named model owner, and carry the intake record, the questionnaire answers, and the assigned risk tier forward as their input.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no control claim of its own, since it is the mechanical consequence of the board's decision. It is Level 1 because a handoff that does not fire leaves the mandatory outcomes below it attached to nothing. Carry the answers and the assigned tier forward so privacy and threat work start from the existing profile and are scoped to the tier.

### AI-1.2: Privacy Requirements Definition

**Design Intent:** Incidental imagery of people is the only personal information in KESTREL's collection. Training sets keep it only where a detection task needs it, and no model is trained to identify individuals. The privacy officer approves each new training set's handling, and the AISP records that removing a record later means retraining rather than deleting from the weights.

**NIST Control Mapping:**

- **PT-2 (partial):** claimed partial for determining the authority under which the information in scope may be processed, since what a model learned from a record cannot be removed the way the record can. The base control is cited because its enhancements are tagging and enforcement mechanisms the Data focus area provides.
- **PT-3 (partial):** claimed partial for the purpose limits that authority carries, since data collected for one purpose is not automatically available to train a model for another.
- **RA-8 (partial):** claimed partial for the privacy risk assessment that sets which regimes and data categories are in scope. It has no enhancements.
- **SI-19 (partial):** claimed partial for deciding the de-identification requirement, while PII Detection and Redaction/Anonymization in Training Data holds the applying half.
- **SI-19(4) (partial):** claimed partial for requiring removal, masking, or replacement of direct identifiers, the deciding half on the same basis.
- **SI-19(6) (partial):** claimed partial for setting differential privacy parameters where the program elects that technique, again the deciding half only.
- **Declined:** data minimization is not claimed, since the Data focus area's Data Minimization Requirement Definition holds it under the DMP.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Base/Pretrained Model, Fine-Tuned Model, Object/File Storage

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-1.2.1: Privacy Requirement Derivation from Data Classification and Regulatory Scope**
    - **Description:** Determine which regulatory regimes and data categories apply to the datasets and inference inputs in scope, derive from the Data focus area's assigned classifications a numbered set of privacy requirements the ML system must satisfy, and document the requirements in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PT-2 (partial), PT-3 (partial), and RA-8 (partial) mappings. It is triggered by a new data source or a change in the model's intended use, not by a calendar. Settle purpose compatibility in writing before training, since data the program may store is not thereby authorized to train a model for a different mission.

- **AI-1.2.2: Differential Privacy/Anonymization Requirement Definition**
    - **Description:** Specify which de-identification technique, namely removal or masking of direct identifiers, generalization, or differential privacy, applies to each data category in scope, state the parameters and the utility floor the chosen technique has to meet, and document the requirement in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-19 (partial), SI-19(4) (partial), and SI-19(6) (partial) mappings. It is Level 2 as written and rises to Level 1 where the tailored baseline includes SI-19 because the system processes PII. State a utility floor alongside the privacy parameter, and set both with the Data Engineering engineers who must meet them, since a budget no achievable model meets gets relaxed under schedule pressure.

- **AI-1.2.3: Privacy Requirement Sign-Off and Baseline**
    - **Description:** Obtain approval of the completed privacy requirement set from the accountable authority and the program's privacy stakeholders, then place it under version control as the baseline that data engineering, training, and serving work is measured against.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Baselining matters more for privacy requirements because a dropped one cannot be patched, and a model trained on data it should not have seen must be retrained. Where the program has a privacy office or designated privacy official, that reviewer is a required signatory, since confirming the PT-2 authority determination is theirs.

### AI-1.3: Model Selection and Justification

**Design Intent:** Each model choice is recorded with the criteria it was assessed against, namely the publisher's security practice, licensing, the serialization format, and fitness for the mission. Foundation models come only from the cloud provider's IL5-authorized catalog. Every detection and embedding model starts from a pretrained checkpoint on the approved catalog or is trained from scratch, and each choice records the risks the program accepted.

**NIST Control Mapping:**

- **RA-3(1) (partial):** claimed partial for the supply chain risk assessment of a candidate model, its producer, and its declared corpus. Model Deployment Risk Threshold Evaluation holds the base RA-3 for the program's own releases.
- **SA-4 (partial):** claimed partial for the security criteria a candidate model must meet to be eligible, a model slice beside the Application focus area's Security Requirements Definition. The base is cited because its enhancements govern developer deliverables, not criteria.
- **SR-5(2) (partial):** claimed partial for assessing a model before selection, acceptance, or update. Dependency Review holds the software-component slice, since model weights are assessed against producer disclosures rather than a dependency graph.
- **SR-6 (partial):** claimed partial for assessing the model supplier itself. The base is cited because SR-6(1) tests delivered elements, and contractual flow-down stays with the Manage pillar's supply chain governance.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Base/Pretrained Model, Foundation Model

**External Dependencies:** The IL5 cloud provider, which hosts each foundation model deployment inside KESTREL's tenant under its provisional authorization. The publishers of any pretrained checkpoint or framework KESTREL adopts.

**Security Impact:** Moderate

**Activities:**

- **AI-1.3.1: Model Architecture/Vendor Selection Criteria Definition**
    - **Description:** Define the security criteria a model architecture, vendor, or pretrained checkpoint must satisfy to be eligible before candidates are shortlisted, covering disclosed training data, licensing terms, update and support commitments, and the evidence the producer will provide, and document the criteria in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-4 (partial) mapping. Write the criteria before candidates are on the table, since criteria drafted after prototyping tend to describe the model already chosen. Make evidence availability an explicit criterion, because many capable models ship with no disclosed corpus, signed artifacts, or support commitment.

- **AI-1.3.2: Model Risk Assessment**
    - **Description:** Assess each shortlisted model against its supply chain exposure, its license terms and the obligations those impose on derived models, and what its producer discloses about the origin and composition of the corpus it was trained on.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-3(1) (partial), SR-5(2) (partial), and SR-6 (partial) mappings. Treat licensing as a security question, since open-weight licenses can restrict what the program may field and to whom. An undisclosed corpus is the normal case, so record what the producer will attest to and treat the rest as accepted risk.

- **AI-1.3.3: Selection Justification Documentation and Approval**
    - **Description:** Record the selected model, the alternatives considered, the criteria each was measured against, and the residual risks accepted in choosing it, and route that record for the accountable authority's approval.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Record the alternatives considered, since a justification naming only the winner cannot be reassessed when the chosen model later shows a defect or a license change. Version the record with the model, because it is the input to any later replacement decision.

### AI-1.4: Approved AI Component Catalog

**Design Intent:** One approved AI component catalog lists the model families, pretrained checkpoints, frameworks, and model registries KESTREL may use. The ML team proposes additions, and the AI/ML Governance Review Board approves them. The package mirror and the model registry accept only what the catalog lists.

**NIST Control Mapping:**

- **SA-15 (partial):** claimed partial for the tool-options element, covering the AI-specific publisher, dataset, and library population that the Application focus area's Secure Coding Standards and Build Hardening does not reach. What this outcome produces is the governed catalog itself, not the mechanism that enforces it.
- **Declined:** the enforcement claims stay where they are. SR-4 and CM-8(3) remain Trusted Model Registry Source Validation's, SR-3 and SR-4(3) remain Trusted Internal Package Repository's, SI-10(5) remains Data Poisoning Prevention and Detection's, and RA-3(1), SA-4, SR-5(2), and SR-6 remain Model Selection and Justification's.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Third-Party Dependency (Embedded Library/Package), Artifact/Model Registry

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-1.4.1: AI Component Vetting Criteria and Catalog Publication**
    - **Description:** Define the vetting criteria for each component category, namely provenance, CVE history, and MITRE ATLAS results for a publisher, provenance, classification, and trust determination for a dataset, and CVE status, hash verification, and maintenance activity for a library, then publish the resulting catalog in an access-controlled, authoritative location linked from the model registry, SBOM documentation, and the intake workflow, and document the catalog in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-15 (partial) mapping. Write criteria per category, because a library, a model publisher, and a dataset each produce different evidence. Link the catalog from the model registry, the SBOM, and the intake workflow so engineers meet it at the point of decision, and deliver staff training through the Manage pillar's Role-Based Specialized Training.

- **AI-1.4.2: ISSE Ownership and Review Cadence**
    - **Description:** Assign the ISSE formal ownership of the catalog across all three component categories, define a minimum annual review cadence triggered additionally by a red team finding, a CVE disclosure, or a confirmed supply chain incident, and document each review's outcome in the program's governance decision-tracking record.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, since it assigns accountability for the catalog the sibling activity produces. One owner keeps all three categories current rather than only the one a team happens to care about. Record trigger-driven reviews in the Manage pillar's Governance Decision/Action Item Tracking so catalog changes sit with other governed decisions.

- **AI-1.4.3: Fast-Track Suspension and Removal**
    - **Description:** Suspend a currently approved component immediately on a confirmed critical or high CVE, maintainer abandonment, or supply chain compromise, with the ISSE authorized to suspend pending ISSO confirmation within 24 hours, then identify every affected deployment through an SBOM and model-registry cross-reference before finalizing removal, and update the enforcement mechanisms that read the catalog within the program's defined SLA.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, since its changes land in the registry, repository, and source lists the enforcing outcomes already cover. It closes the gap between annual reviews, and the SBOM and model-registry cross-reference scopes which deployments must be remediated. A deployment that cannot be remediated inside the window goes to the Risk focus area's Risk Acceptance Process with a remediation deadline.

- **AI-1.4.4: New Component Request Process**
    - **Description:** Define the path by which a development or ML team requests a new publisher, dataset, or library for the catalog, including the required fields of component name and category, use case, vetting evidence, and business justification, the review steps and their SLA, and the update the catalog and any dependent SBOM entries receive on approval, and document the resulting process in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, since it is the intake half of the published catalog. Publish a request path with a stated SLA, because teams route around a catalog they cannot ask to change. Track requests in the same record ISSE Ownership and Review Cadence reports from, so repeated requests for one component prompt a review of the criteria.

### AI-1.5: Model Provenance and Integrity Verification

**Design Intent:** Every pretrained checkpoint is checked against its publisher's signature or published digest when it enters the model registry, and it is refused if either fails. Each foundation model deployment records the exact version the cloud provider serves. A version KESTREL did not approve raises an alert.

**NIST Control Mapping:**

- **SI-7(15) (partial):** claimed partial because a model checkpoint is cryptographically authenticated before load, while Image Signing holds the container image slice.
- **SR-4 (partial):** claimed partial for documenting the provenance of an externally sourced model, where the corpus and training run were not the program's. Other provenance slices sit with outcomes such as Build Provenance and Attestation (SLSA) and AI-BOM Generation.
- **SR-4(3) (partial):** claimed partial for validating that a received model is genuine and unaltered against the publisher's digest or signature. Build Provenance and Attestation (SLSA) holds the slice for the program's own builds.
- **Declined:** CM-14 is not claimed, because blocking unsigned components is enforcement held by Signed/Hashed Reference Models and Training Artifact Signing.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Base/Pretrained Model, Foundation Model, Self-Hosted Model, Artifact/Model Registry

**External Dependencies:** The IL5 cloud provider, which hosts each foundation model deployment inside KESTREL's tenant under its provisional authorization. The publishers of any pretrained checkpoint or framework KESTREL adopts.

**Security Impact:** High

**Activities:**

- **AI-1.5.1: Model Source/Provenance Validation**
    - **Description:** Establish that a pretrained or foundation model originates from the publisher it claims and reached the program through an approved distribution path, and record that origin against the specific checkpoint version in use.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4 (partial) mapping, for models the program obtained rather than trained. Name the approved distribution path as well as the publisher, since the common failure is a legitimate model pulled from a mirror or a same-named re-upload.

- **AI-1.5.2: Model Artifact Hash/Signature Verification**
    - **Description:** Verify the model artifact's cryptographic hash or signature against the publisher's declared value before the checkpoint is loaded into any training, evaluation, or serving environment, and refuse the artifact on mismatch.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4(3) (partial) and SI-7(15) (partial) mappings. Verify at load, not only at download, so a substituted file in a shared store is caught. Name approved serialization formats here, since a code-executing format is dangerous even when it verifies, while Model Artifact Malware/Unsafe-Deserialization Scanning enforces them.

### AI-1.6: Robustness Requirements Definition

**Design Intent:** Each model's robustness requirements come from its threat model and how much the mission relies on it. For the detection models, that means holding detection rates under weather, sensor degradation, camouflage, and RF deception. For language model use cases, it means resisting jailbreaks and injected instructions. The AISP states each requirement as a measurable threshold that validation tests against.

**NIST Control Mapping:**

- **RA-9 (partial):** claimed partial for the criticality analysis of how much the mission depends on the model being correct. It has no enhancements.
- **SA-15(1) (partial):** claimed partial for defining measurable robustness criteria at the start of development. Robustness Threshold Validation Against Acceptance Criteria performs the testing that supplies the evidence.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-1.6.1: Robustness Requirement Derivation from Threat Model and Use Case Criticality**
    - **Description:** Derive the robustness properties the model must exhibit from the threats AI Threat Modeling identified, set the use case's assurance level from its mission criticality and its oversight mode, and document the required properties and the assurance level in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-9 (partial) mapping and consumes AI Threat Modeling's threats. Set the assurance level from two properties of the use case, namely mission criticality judged against everything it can reach and its oversight mode. Raise the level one step when output takes effect without prior human approval, but never lower it for oversight, and count approval only where the approver has time, information, and authority to reject. One model serving two use cases is held to the stricter level. The DoD Developmental Test and Evaluation of AI-Enabled Systems Guidebook frames the same question from the test side, tying model metrics to mission effect and worst-case performance.

- **AI-1.6.2: Robustness Acceptance Criteria and Testing Scope Definition**
    - **Description:** State the measurable thresholds each assurance level must meet under adversarial perturbation, distribution shift, and degraded input, decide which test classes apply from the model's origin and AI category, define the perturbation budgets, datasets, and minimum suite sizes the testing has to cover, and document the criteria and testing scope in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-15(1) (partial) mapping, and the criteria go to Validation and Continuous Delivery versioned with the requirements baseline. Choose test classes by model origin and AI category, with the deployed configuration as the target for a managed model, and record any class judged not applicable with ISSE-signed rationale and hand it to Red Teaming. Write a minimum and a target per assurance level, set by the program since NIST AI 600-1 asks for go/no-go thresholds without prescribing values, and size suites at no fewer than three divided by the allowed failure rate. Where one AISP covers many use cases, the AISP holds this methodology and each use case records its own classes, thresholds, datasets, and re-test cadence in an AI Cyber T&E Plan written under it.

### AI-1.7: AI Threat Modeling

**Design Intent:** The ML team threat-models every model and the mission teams threat-model every AI use case built on one, using MITRE ATLAS alongside the program's application methodology. The PMO ISSE reviews each model at the design gate. Models cover poisoning through feedback and federated updates, evasion by adversary camouflage and deception, prompt injection through retrieved reports, and capture of an aircraft's onboard model.

**NIST Control Mapping:**

- **SA-11(2) (partial):** claimed partial for threat modeling the ML system against classes such as poisoning and membership inference that Application Threat Modeling does not reach. Training Pipeline Misuse/Abuse Case Testing holds the vulnerability analysis dimension.
- **SA-15 (partial):** claimed partial for the documented ML threat taxonomy and the standard a completed model must meet, beside Application Threat Modeling's conventional-software slice.
- **SA-15(2) (partial):** claimed partial for the tracked path from an ML finding to an owned backlog item, split by finding class from Application Threat Modeling.
- **Declined:** SA-15(8) is not claimed, since Application Threat Modeling holds the shared repository ML models are added to.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Application/API, Storage/Database

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-1.7.1: AI-Specific Threat Taxonomy Adoption**
    - **Description:** Adopt and document a threat taxonomy covering the AI-specific attack classes, including training data poisoning, model extraction, adversarial examples, membership and attribute inference, and model supply chain compromise, define what a completed AI threat model must contain, and document the taxonomy in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-15 (partial) mapping. Adopt a published taxonomy such as MITRE ATLAS or the OWASP ML and LLM lists rather than writing one. A completed model must identify the training data sources and who can influence them, the query interface and who can reach it, the trust placed in any pretrained base, and the consequence of a wrong output.

- **AI-1.7.2: AI Threat Model Creation at Design-Review Gate**
    - **Description:** Require a completed AI threat model built on the adopted taxonomy before an AI system passes design review, and require it to be revisited whenever the training data sources, the base model, or the exposure of the inference interface changes.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(2) (partial) mapping and makes the practice non-optional. Trigger re-review on changes that move the threat picture, such as a new data source, a swapped base model, or a widened inference interface. Where the ML system is part of a larger application, review it at that application's design gate.

- **AI-1.7.3: AI Threat-Model-Finding-to-Backlog Conversion**
    - **Description:** Open a tracked backlog item for each accepted AI threat model finding, assigning it an owner, a severity, and a remediation target date before the design review is recorded as passed.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-15(2) (partial) mapping. ML findings route in more directions than application ones, to data engineering, the serving interface owner, or the selection decision. Route findings that change what the model must withstand to Robustness Requirements Definition as well.

### AI-1.8: OT and Safety-Critical AI Governance

**Design Intent:** No KESTREL model may command an aircraft, its flight controls, or its payload. Onboard detection models only cue the operator, and every AI agent output that would affect a flight, such as the mission-planning agent's drafts, takes effect only after an operator approves it. The AI/ML Governance Review Board enforces this list at intake, and agent tool scoping enforces it technically. Airworthiness certification remains a separate process.

**NIST Control Mapping:**

- **AC-3(2) (partial):** claimed partial for any AI-generated output that would actuate an OT or safety-critical process, agentic or not. The Identity focus area's AI Agent Identities holds the agent tool-call population and excludes OT/ICS.
- **Declined:** PM-11 is not claimed, since the AI/ML Governance Review Board already enforces the policy. SA-11(2), SA-15, SA-15(2), RA-9, and SA-15(1) are not reopened, because the assessment composes AI Threat Modeling and Robustness Requirements Definition findings and takes the safety determination from the program's systems-safety discipline. SC-7, SC-7(21), AC-4, and SC-7(5) remain IT/OT Zone and Conduit Segmentation's.

**Deployment Type:** On-Premises, Cyber-Physical System (OT/ICS)

**Affected Components:** Industrial Controller/SCADA, AI/ML System

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-1.8.1: OT-Adjacent AI Prohibited Use Case Policy**
    - **Description:** Define and maintain, for governance board approval, the AI use cases prohibited outright in or adjacent to an OT environment, among them autonomous safety decisions, autonomous mission-critical control, and unsupervised OT process changes, then communicate the restrictions to OT and AI program staff, route every matching use case to rejection under the AI/ML Governance Review Board's existing decision workflow, and document the policy as one of the board's standing rejection criteria in the AI/ML Governance Charter.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, since the Manage pillar's Use-Case Review/Approval Workflow enforces the policy as a standing rejection criterion. Deliver staff communication through Role-Based Specialized Training. This activity's deliverable is the list and its approval record.

- **AI-1.8.2: OT-Adjacent AI Risk Assessment Gate**
    - **Description:** Require a risk assessment before any AI capability deploys in or adjacent to an OT environment, and on a defined annual and trigger-driven cadence thereafter, that combines the focus area's existing adversarial-risk and mission-dependency findings with a current safety-impact determination from the program's systems-safety discipline, then escalate a high-risk finding to the AI/ML Governance Review Board and the ISSO, link the completed assessment to the model's registry entry, and document the gate's trigger, composition, and escalation path in the AISP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, since it composes AI Threat Modeling's adversarial findings and Robustness Requirements Definition's mission dependency, adding a safety-impact determination from the program's systems-safety discipline. Re-assess on a material OT change, a model update or redeployment, a new OT integration point, or a red team finding affecting an OT-adjacent control. Link the assessment to the Model Registration and Inventory Logging entry.

- **AI-1.8.3: AI/OT Boundary Isolation Architecture**
    - **Description:** Design and document the architecture separating AI decision-making functions from OT control paths so that no AI system's output can reach an actuator without first passing through a human-authorized mediation point, produce a diagram of the boundary, require review and sign-off by the ISSO and the OT security lead before the architecture is fielded, and document the architecture in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, since it describes the architecture the outcome's AC-3(2) (partial) mapping enforces, while IT/OT Zone and Conduit Segmentation governs the conduit. Every path must end at a mediation point rather than at the actuator. Review the diagram against the fielded system, which catches integrations added later that reopen a direct path.

- **AI-1.8.4: OT-Adjacent AI Action Human Authorization Gate**
    - **Description:** Technically enforce a human authorization requirement, at the integration layer between an AI system and any OT or safety-critical actuation path, for every consequential action the AI system's output would otherwise put into effect, in a form the AI system itself cannot bypass or override, and log each authorization with the deciding individual's identity and a timestamp.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-3(2) (partial) mapping as a technical gate at the required mediation point. The AI system must not hold the credential that authorizes its own action, and the approver identity and timestamp are captured as AI Agent Identities does. Test the gate by trying to reach the actuator without triggering it, such as through malformed requests, race conditions, or unmediated paths.

## AI-2: Data Engineering

### AI-2.1: Data Poisoning Prevention and Detection

**Design Intent:** Training data comes only from KESTREL's own collection, analyst corrections, federated updates from the aircraft, and products released from the IL6 enclave. The Data Team screens every batch before it enters the ML training zone. The screening checks provenance, flags outliers and duplicates, and checks for label shifts against the existing corpus. A new external dataset needs AI intake first.

**NIST Control Mapping:**

- **SI-7(1) (partial):** claimed for the integrity check Statistical/Anomaly-Based Poisoning Detection runs on a candidate corpus before admission. Endpoint File Integrity Monitoring holds the host file surface.
- **SI-7(5) (partial):** claimed partial for the automated quarantine and run-halt that follow a discovered integrity violation in a training corpus.
- **SI-10(5) (partial):** claimed for restricting training data ingestion to registered sources and approved serialization formats. The base SI-10 is not reopened, since bulk dataset ingestion is a separate input surface from the runtime request slices other outcomes hold.
- **Declined:** SI-4 is not claimed, because this outcome inspects a static dataset at rest, while SI-4 monitors a live system for events.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model, Object/File Storage, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-2.1.1: Training Data Source Validation and Trust Boundary Definition**
    - **Description:** Draw the trust boundary around the training data pipeline, register every approved source with its owner, ingestion path, and assigned trust tier, and reject at ingestion any dataset that does not resolve to a registered source in an approved serialization format.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-10(5) (partial) mapping and consumes the Data focus area's Data Provenance and Lineage Verification rather than duplicating it. Decide scraped and community-hosted corpora explicitly, and restrict formats that execute code on load. Assign each approved source a trust tier, hold tiers in separately access-controlled stores, and route any promotion to a higher tier through an accountable approver, since even a change in tier mix can shift what a model learns.

- **AI-2.1.2: Statistical/Anomaly-Based Poisoning Detection**
    - **Description:** Screen each candidate corpus for the distributional, nearest-neighbor, and duplication signatures that seeded or manipulated samples produce, and flag the individual samples and clusters that fall outside the expected profile for adjudication.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(1) (partial) mapping and runs on assembly of a candidate corpus. It is Level 2 because detection is probabilistic and needs a clean baseline, while the source restriction is the mandatory floor. A negative result is not proof of a clean corpus, since a backdoor trigger can hide inside the expected distribution.

- **AI-2.1.3: Poisoned Sample Quarantine and Retraining Trigger**
    - **Description:** Hold flagged samples out of the training set automatically and fail the run rather than training on a corpus pending adjudication, and open a retraining decision for any already-trained model whose corpus a later screen finds contaminated.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(5) (partial) mapping, the automated response that makes detection a control. Also act backward on models already serving that learned from the sample, using Dataset Lineage and Version Control to find them. Retain quarantined samples as evidence and to tune the screen.

### AI-2.2: Label Integrity Verification

**Design Intent:** Labels come from the Data Team's cleared annotators and from analyst corrections, and from no outside labeling service. A sample of every batch is labeled twice, and low agreement holds the batch. Each correction is bound to the analyst who made it, so one analyst's corrections can be reviewed or withdrawn together.

**NIST Control Mapping:**

- **SI-10 (partial):** claimed for checking the validity of label values entering the training pipeline, a slice beside the runtime input slices such as Web Application Firewall. The base is cited because SI-10(5) sits with Data Poisoning Prevention and Detection and no other enhancement fits semantic label validity.
- **SR-6 (partial):** claimed for assessing an external labeling supplier, alongside Model Selection and Justification's model-supplier slice. The base is cited because SR-6(1) tests delivered elements.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model, Object/File Storage

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-2.2.1: Labeling Source/Pipeline Trust Verification**
    - **Description:** Establish which labeling services, tools, and annotator populations the program accepts labels from, assess each external labeling supplier against the program's supply chain criteria, and authenticate label submissions to the source that produced them.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-6 (partial) mapping. Outsourced annotation puts an anonymous, high-turnover population in control of what a model learns, so record what the supplier attests about its annotators and access controls. Authenticate the label submission path, since otherwise an unauthorized relabeling looks like a legitimate correction.

- **AI-2.2.2: Label Consistency/Anomaly Auditing**
    - **Description:** Audit each labeled dataset for values outside the declared label schema, disagreement between annotators on the same item, and class distributions that deviate from the expected baseline, and return the failures for relabeling before the dataset is released to training.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-10 (partial) mapping as a gate on dataset release. Overlap a share of items across annotators and seed a holdout of known labels, since otherwise the audit cannot find a labeler who is consistently wrong. Watch class distribution closely, because a label-flipping attempt large enough to move a decision boundary also moves class balance.

### AI-2.3: Training Data Privacy Controls

**Design Intent:** Incidental imagery of people is blurred or cropped out of training data unless the detection task needs it. Training sets carry no analyst names or other personal fields. The Data Team applies these controls as it releases data into the ML training zone, and the provenance record notes which technique it applied.

**NIST Control Mapping:**

- **AC-3(11) (partial):** claimed partial for restricting access to raw, pre-transformation training data repositories as a designated information type, the enhancement's exact mechanism.
- **SI-19 (partial):** the applying half of the joint claim Privacy Requirements Definition holds from the deciding side, partial for the de-identification actually performed.
- **SI-19(4) (partial):** partial for removing, masking, or replacing direct identifiers as executed, on the same joint basis.
- **SI-19(6) (partial):** partial for applying differential privacy at the parameters the baseline set, tracked jointly with Privacy Requirements Definition.
- **Declined:** AC-6 is not reopened, since designating a restricted repository class is AC-3(11)'s subject. SC-28 is not claimed, since encryption at rest is the Data focus area's, which also supplies the DLP patterns and sensitivity labels used here.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model, Object/File Storage, Identity Lifecycle and Governance

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-2.3.1: PII Detection and Redaction/Anonymization in Training Data**
    - **Description:** Scan each dataset entering the training pipeline for the personal information categories the privacy baseline identified, and apply that baseline's assigned redaction, masking, generalization, or differential privacy technique to each category before the dataset is released for training.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-19 (partial), SI-19(4) (partial), and SI-19(6) (partial) mappings, applying what Differential Privacy/Anonymization Requirement Definition set. Run the transformation before the first copy into any training store, so no untransformed original sits in intermediate storage. Record the residual in free text, imagery, and audio as accepted risk rather than reporting full coverage.

- **AI-2.3.2: Access Control on Raw Training Data Stores**
    - **Description:** Restrict access to the raw, pre-transformation training data repositories to a named minimum population with a documented need for unredacted records, and re-attest that population on a defined cadence.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-3(11) (partial) mapping, designating the raw stores as restricted and deciding who may reach them, while the Identity focus area issues the entitlements. Re-attest access, because grants made for one exploratory question rarely get removed and the population drifts toward the whole program.

### AI-2.4: Dataset Lineage and Version Control

**Design Intent:** Every training run reads an immutable dataset snapshot in the ML training zone, identified by its content hash. Each snapshot's provenance record names the zones it came from, the release approvals behind it, and the payload vendor terms it falls under. A model can therefore be traced to the exact data and permissions that produced it.

**NIST Control Mapping:**

- **AU-10(1) (partial):** claimed partial for binding the producing source and pipeline run to the snapshot strongly enough to be non-repudiable. AI Agent Identities cites the base for agent actions, a different subject.
- **AU-10(2) (partial):** claimed partial for the means by which a reviewer later validates that binding.
- **Declined:** SR-4 is not claimed, since the Data focus area's Data Provenance and Lineage Verification holds the dataset slice. SI-12 is not claimed, since Registry Hygiene Report and Model Registry Hygiene Report hold retention, and snapshot retention here is part of the binding.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model, Object/File Storage

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-2.4.1: Dataset Versioning and Immutable Snapshotting**
    - **Description:** Snapshot each dataset at the state a training run consumes it, store the snapshot under a content-derived identifier in a repository that permits no in-place modification, and bind the producing pipeline run's identity to the snapshot as it is written.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-10(1) (partial) mapping. Use content-derived identifiers, so an in-place edit produces a new identifier instead of hiding under an old name. Set retention against the service life of the models trained on a snapshot rather than a flat calendar. Pair it with Reproducibility Controls, since neither delivers reproducibility alone.

- **AI-2.4.2: Lineage Tracking**
    - **Description:** Record for every training run which dataset snapshots it consumed and which upstream sources and transformations produced them, and make that record queryable in both directions, from a fielded model back to its data and from a suspect source forward to the models it reached.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-10(2) (partial) mapping. Record the edges as they are created, so the program can answer on the day which fielded models touched a source later found compromised.

## AI-3: Experimentation

### AI-3.1: Secure Experimentation Environment

**Design Intent:** Experimentation workspaces in ML Dev/Test are individual, scoped to the datasets each data scientist is approved for, and reached only through the identity-aware proxy. Downloads are disabled, and the workspaces have no route to any prod spoke. Mission data therefore never reaches a laptop or production.

**NIST Control Mapping:**

- **SA-3(1) (partial):** claimed partial for the interactive research workspace as a preproduction environment, split from the Application focus area's Ephemeral/Isolated Build Environments. A workspace is driven by a person over weeks, while a build runner executes a defined job and exits.
- **SC-39 (partial):** claimed on the same split, for a separate execution focus area per researcher workspace on shared GPU compute.
- **AC-6 (partial):** claimed for least-privilege scoping of experimentation identities, a slice alongside the Identity focus area's AC-6 claims.
- **Declined:** AC-3(11) is not re-claimed, since Training Data Privacy Controls designates the raw stores and this outcome scopes access to working copies. AC-4 is not claimed, because the Network and Environment focus area's segmentation outcomes carry the enclave flow policy.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Object/File Storage, Identity Lifecycle and Governance, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-3.1.1: Isolated/Sandboxed Experimentation Compute Provisioning**
    - **Description:** Provision each researcher's experimentation workspace on demand from an approved image into compute that is separated from fielded systems and from other researchers' workspaces, and tear the workspace and its storage down when the line of work it was opened for ends.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-3(1) (partial) and SC-39 (partial) mappings. Scope disposability to the line of work rather than the job, with a defined maximum lifetime and reclaim on expiry, since researchers cannot rebuild a week of state on every login. Recurring cost is High because the platform must have enough GPU capacity to displace laptop notebooks.

- **AI-3.1.2: Experimentation Data Access Scoping**
    - **Description:** Grant each experimentation workspace access only to the de-identified or subset working copies its current line of work requires, withhold the raw pre-transformation stores absent a documented need, and re-attest the resulting grants on a defined cadence.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-6 (partial) mapping and depends on Access Control on Raw Training Data Stores. A working copy inherits the handling requirements of its source unless Training Data Privacy Controls removed them, so a convenience subset is not lower sensitivity. Watch for full extracts left mounted long after the question they answered.

### AI-3.2: Experiment Tracking and Reproducibility

**Design Intent:** An experiment tracking service in ML Dev/Test records every run's code revision, dependencies, environment, hyperparameters, dataset snapshot, and metrics automatically. A checkpoint without a complete run record cannot be promoted.

**NIST Control Mapping:**

- **CM-2(2) (partial):** claimed for keeping each experiment run's configuration, namely code revision, dependencies, image, hyperparameters, and dataset snapshot, current through automated capture. Device and Infrastructure's Secure Configurations holds the infrastructure slice, and CM-2 and CM-2(3) are not reopened.
- **SA-15 (partial):** claimed partial for the experimentation standard defining what a run must record and the periodic check that tooling meets it. Other subject slices sit with outcomes such as Application Threat Modeling and Approved AI Component Catalog.
- **Declined:** AU-10(1) and AU-10(2) stay with Dataset Lineage and Version Control, whose binding this outcome consumes. The CM-3 family is not claimed, since experimentation is deliberately uncontrolled iteration. CM-12(1) concerns where information resides, not what a run consisted of.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Compute, Database Service, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-3.2.1: Experiment Metadata/Parameter Tracking**
    - **Description:** Record for every experiment run its code revision, dependency set, environment image, hyperparameters, dataset snapshot identifier, resulting metrics, and the identity that launched it, capturing them from the run itself rather than from anything a researcher enters afterward.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-2(2) (partial) mapping. Capture from the run itself, since a service researchers must remember to call records only the runs that went well. The dataset snapshot identifier joins the record to Dataset Lineage and Version Control. Settle the schema before AI-BOM Generation is built, since it assembles from this record.

- **AI-3.2.2: Reproducibility Validation**
    - **Description:** Re-execute a sampled or promotion-bound run from nothing but its recorded configuration, compare the resulting metrics and artifact against the original within a documented tolerance, and treat divergence as a defect in the tracking record rather than as acceptable variance.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-15 (partial) mapping by re-running sampled runs to prove the record is sufficient. Pin the seeds the program can, set a documented metric tolerance, and treat a result outside it as the finding. It is Level 3 because re-execution is costly, so the sampling rate is recorded with the experimentation standard.

### AI-3.3: Signed/Hashed Reference Models

**Design Intent:** A checkpoint the ML team intends to promote is hashed and signed at promotion, and the signature is bound to its run record. The training pipeline accepts only signed reference models as starting points.

**NIST Control Mapping:**

- **CM-14 (partial):** claimed for refusing promotion of an unsigned experiment checkpoint the program produced. Training Artifact Signing and Signed/Verified Training Pipeline Definitions hold the other ML slices.
- **SI-7(15) (partial):** claimed for checkpoints from the program's own experimentation, verified against a signature the program applied. Training Artifact Signing holds the finished weights, which it signs later and less often.
- **Declined:** SR-4(3) is not claimed, because a checkpoint the program produced does not arrive from an external supply chain.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Artifact/Model Registry, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-3.3.1: Reference Model Hashing/Signing at Experiment Checkpoint**
    - **Description:** Compute and sign a cryptographic digest of each experiment checkpoint the program intends to promote or share, bind the signature to the run record that produced it, and store both alongside the artifact in the experimentation artifact store.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Sign the checkpoints the program promotes or circulates, not every intermediate save. Bind the signature to the run record, so verification shows which experiment and configuration produced the checkpoint rather than only that it is unchanged.

- **AI-3.3.2: Reference Model Integrity Verification Before Promotion**
    - **Description:** Verify the checkpoint's signature and digest at the boundary where it is promoted into the training pipeline or shared beyond the workspace that produced it, and refuse the promotion on a missing, invalid, or unrecognized signature.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-14 (partial) and SI-7(15) (partial) mappings, since both turn on refusing an unverified component. Instrument the promotion boundary, because unaccounted checkpoints usually arrive as copies passed between researchers. Make refusal the default, and send externally obtained checkpoints through Model Provenance and Integrity Verification rather than an exception.

### AI-3.4: Training Script and Feature-Engineering IP Protection

**Design Intent:** Training scripts and feature-engineering code sit in ML team repositories that only ML team members can read. Clones on performer laptops are covered by the same performer controls as other source. Data scientists work on mission data only inside the workspaces.

**NIST Control Mapping:**

- **AC-3 (partial):** claimed partial for enforcing authorizations over the ML source artifact class of training scripts, feature pipelines, and notebooks. The base is cited because no enhancement fits read-restriction of a code class, and AC-3(11) covers raw data stores.
- **SI-4 (partial):** claimed for monitoring live access and egress events on those repositories. Training Cluster Network Segmentation and Egress Control holds the cluster's network egress.
- **Declined:** SC-28 is not claimed, because Default Data at Rest Encryption holds encryption of these repositories.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Object/File Storage, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** The performer, whose CMMC Level 2 controls protect source clones on its laptops.

**Security Impact:** Moderate

**Activities:**

- **AI-3.4.1: Access Control and Encryption for Training Scripts/Feature Pipelines**
    - **Description:** Restrict read and write access to the training script and feature-engineering repositories to the named population building on them, and require those repositories and their working copies to be encrypted at rest under the program's key management arrangements.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-3 (partial) mapping. Replace the default organization-wide read access when repositories are created, since the change is unpopular later. Keep this code in Secure Experimentation Environment workspaces, because a server restriction does not reach local clones. Configure encryption through the Data focus area's at-rest encryption and the KMP.

- **AI-3.4.2: Exfiltration Monitoring for Proprietary AI Code/IP**
    - **Description:** Monitor access to and movement of the AI source artifact repositories for bulk clone, mass download, and egress-to-unsanctioned-destination patterns, and route findings into the program's insider risk and incident response workflows.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4 (partial) mapping, running on the Data focus area's DLP and insider risk analytics. The local work is the content classification and misuse patterns for ML source artifacts. Name departure as a trigger, since cloning long-untouched repositories shortly before leaving is the highest-signal pattern.

## AI-4: Development and Continuous Integration

### AI-4.1: Ephemeral, Containerized Training Environments

**Design Intent:** Each training run gets its own containers on the training cluster's GPU nodes, built from an approved image and isolated from concurrent runs. Each run's scratch storage is destroyed when the run ends.

**NIST Control Mapping:**

- **SA-3(1) (partial):** claimed partial for the training runner as a preproduction environment. Unlike the Application focus area's build runner, a training job holds the whole corpus in accelerator memory for hours and writes weights.
- **SC-4 (partial):** claimed partial for residual information, since framework caches, dataset shards, and device-memory tensors survive a container exit and reach the next job. The base is cited because SC-4(2) addresses periods processing across domains, and MP-6 sanitization of retired resources stays with Resource Decommissioning Governance.
- **SC-39 (partial):** claimed partial for a separate execution focus area per training job on shared accelerators, where the default is often a shared device.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Container, Object/File Storage, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.1.1: Ephemeral, Containerized Training Runner Provisioning**
    - **Description:** Provision a fresh containerized runner from an approved training image for each training job, place concurrent jobs in separate execution focus areas on the shared accelerator fleet, and release the runner when the job terminates.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-3(1) (partial) and SC-39 (partial) mappings. Make per-job runners fast enough that nobody asks for a standing node, using a warmed image cache and pre-attached datasets. Where hardware cannot partition a device, assign it exclusively for the run rather than claiming isolation the platform does not provide.

- **AI-4.1.2: Environment Teardown and Residual-Data Wipe Enforcement**
    - **Description:** Destroy the runner's scratch volumes, dataset caches, and accelerator device memory as an enforced step of job termination, and confirm the wipe before the node is returned to the schedulable pool.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-4 (partial) mapping. Put the wipe in the platform's node lifecycle rather than the training code, since crashed, preempted, or cancelled runs skip job cleanup. Confirm the wipe before returning a node to the pool, because device memory clearing depends on driver behavior the program does not control.

### AI-4.2: Least-Privilege Training Infrastructure Access

**Design Intent:** Each training pipeline identity reads only the dataset snapshots its run declares and writes only to its own model registry namespace. Human access to the training cluster is eligible rather than standing, activated through the privileged access platform.

**NIST Control Mapping:**

- **AC-6 (partial):** claimed partial for least-privilege scoping of training service accounts and administrative roles. The base is cited because the enhancements do not address scoping a service identity to its targets, and dataset breadth is the entitlement most often left open.
- **CM-5 (partial):** claimed partial for restricting change access to the training control plane, accelerator fleet, and model registry, a path to fielded models that Least-Privilege CI/Build Infrastructure Access does not cover.
- **CM-5(5) (partial):** claimed partial for limiting who can push a model into the serving registry, with re-evaluation through Periodic Training Infrastructure Access Review. Least-Privilege CI/Build Infrastructure Access holds the build infrastructure slice.
- **Declined:** AC-6(7) is not claimed, since the Identity focus area's Access Reviews holds the privilege review obligation and these reviews run inside it.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application and Service Account Identity, Privileged Access Management, Compute, Object/File Storage, Artifact/Model Registry, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-4.2.1: Training Infrastructure Role/Scope Definition**
    - **Description:** Define the scope of every training service account and administrative role against the specific clusters, corpora, registries, and job queues it requires, and remove the standing entitlements that scope does not justify.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-6 (partial), CM-5 (partial), and CM-5(5) (partial) mappings. Author custom roles, because managed MLOps platforms ship coarse built-in roles that mostly grant the whole workspace. Accepting the defaults does not meet this activity.

- **AI-4.2.2: Periodic Training Infrastructure Access Review**
    - **Description:** Re-attest on a defined cadence which identities hold access to the training platform, its accelerator fleet, and its model registry, and revoke the grants their current owners can no longer justify.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it runs as a campaign within the Identity focus area's Access Reviews. Review service accounts as closely as people, since a retired pipeline's identity keeps its grants. Pair the review with platform authentication records to expose unused grants.

### AI-4.3: Training Cluster Network Segmentation and Egress Control

**Design Intent:** The training cluster sits in ML Dev/Test, which the cloud hub isolates from every prod spoke. Its only outbound paths are the package mirror, the model registry, and the ML training zone across the circuit, so neither the corpus nor the weights have another way out.

**NIST Control Mapping:**

- **SC-7(5) (partial):** claimed partial for default-deny at the training cluster boundary, permitting only the peers and destinations a run needs. Network Micro Segmentation holds the wider flow fabric.
- **SC-7(10) (partial):** claimed partial for preventing exfiltration across that boundary, beside Network Firewall's shared network path. Bulk corpus or weight movement out of a cluster that should only fetch packages is a distinguishable pattern.
- **Declined:** AC-4 is not claimed, since the Network and Environment focus area's segmentation outcomes enforce the enclave flow policy. SC-7 and SC-7(21) remain Network Macro Segmentation's and IT/OT Zone and Conduit Segmentation's. SI-4 stays with Training Script and Feature-Engineering IP Protection, which watches repositories rather than the cluster.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Segmentation Policy, Network Firewall, Compute, Storage/Database, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-4.3.1: Training Cluster Network Isolation/Segmentation**
    - **Description:** Place the training cluster in a dedicated network segment carrying no route into fielded systems, and admit inbound traffic only from the pipeline control plane and the artifact and data stores a run depends on.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the inbound and placement dimension of the outcome's SC-7(5) (partial) mapping, within the Network and Environment focus area's segments. Check for undesigned routes, such as a cluster sharing a segment with an inference endpoint so a scoring service can reach checkpoints. It is event-driven, changing when the platform topology changes.

- **AI-4.3.2: Egress Allow-Listing and Data-Exfiltration Monitoring**
    - **Description:** Restrict the cluster's outbound connections to an enumerated allow-list of package indexes, model hubs, and dataset sources, and alert on transfer volumes and destinations consistent with a corpus or a set of weights leaving the cluster.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the egress dimension of the outcome's SC-7(5) (partial) mapping and its SC-7(10) (partial) mapping. Pair each allowed destination with a direction and volume expectation, since the model hub a run pulls from is also a place to push weights. Build it after dependency and artifact paths are pinned, so thresholds reflect what a run actually fetches.

### AI-4.4: Training Code Static Analysis

**Design Intent:** Training scripts, data loaders, and feature-engineering code go through the same SAST in the shared pipeline as application code, with rules for the ML frameworks they use. That includes checks for unsafe deserialization and shell execution.

**NIST Control Mapping:**

- **SA-11(1) (partial):** claimed partial for static analysis of training scripts, data loaders, and feature-engineering modules that never enter the application build. SAST holds conventional application source. Confirm the tool actually reads notebooks rather than skipping them.
- **SA-15(7) (partial):** claimed partial for the automated analysis on each pipeline run, split by code class from SAST. The findings that matter are unsafe deserialization, dynamic execution in loaders, import-time fetches, and shell calls from notebooks, which a web ruleset buries.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Compute, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.4.1: SAST Tool Integration Into Training Pipeline**
    - **Description:** Integrate the static analyzer into the training pipeline so every commit and merge request against the training, data-loader, and feature-engineering repositories is scanned, and fail the run at the severity threshold the program sets.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(1) (partial) and SA-15(7) (partial) mappings. Define the scanned set as everything the pipeline may execute, and refuse anything outside it, since notebook servers can run files the repository scan never sees.

- **AI-4.4.2: Training Code Rule/Ruleset Tuning and False-Positive Baseline**
    - **Description:** Tune the analyzer's ruleset against the program's ML frameworks and notebook idioms, and record the baseline of accepted findings so that a scan result reflects new risk rather than accumulated noise.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the exploitation-potential judgment dimension of the outcome's SA-15(7) (partial) mapping. Tune out generic numeric and array rules that mean nothing in a tensor pipeline, while keeping deserialization, subprocess, and import-time network rules strict. Version the accepted-finding baseline with the ruleset and review it on the same cadence.

### AI-4.5: Training Code Secret Scanning

**Design Intent:** Training repositories are covered by the same four-point secret scanning as application repositories. Training jobs also have no reason to hold a static secret, since they authenticate with workload identity.

**NIST Control Mapping:**

- **IA-5(7) (partial):** claimed partial for keeping static credentials out of ML source repositories, which often sit outside the application organization and hold data store credentials. Training Credential Secrets Management removes the reason to commit them, and rotation runs through the Identity focus area's vault machinery.
- **Declined:** SA-11(1) is not re-claimed, since Training Code Static Analysis holds static analysis for this code class.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Storage/Database, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.5.1: Secret Scanning Tool Integration Into Training Pipeline**
    - **Description:** Integrate the secret scanner into the commit and merge path of the training and feature-engineering repositories so that a detected credential blocks the merge and opens a rotation request.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(7) (partial) mapping. Verify detector coverage for object store keys, feature store tokens, experiment tracking keys, and model hub tokens, since stock sets often miss them.

- **AI-4.5.2: Training Repository Historical Scan and Remediation**
    - **Description:** Sweep the full commit history of every training and feature-engineering repository for previously committed credentials, and drive each finding to rotation rather than to deletion from history.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Rotate every committed credential, since rewriting history removes the record but not the exposure. Scan notebook output cells too, because they can hold a printed token long after the source line changed.

### AI-4.6: AI Dependency Vulnerability Scanning

**Design Intent:** The resolved dependency set of every training and serving image is scanned against current vulnerability data on each build and daily afterward. Frameworks, tokenizers, and accelerator toolkits come only through the package mirror.

**NIST Control Mapping:**

- **RA-5 (partial):** claimed partial for continued scanning of the pinned ML dependency set in training environments, while Dependency Review decides adoption at proposal time. The base is cited because RA-5's enhancements address cadence and depth rather than the scanned surface.
- **Declined:** SR-5(2) and SR-3 are not claimed, since acceptance belongs to Dependency Review and Model Selection and Justification. SI-2 is not claimed, because Vulnerability and Patch Management holds flaw remediation and this policy is an input to it.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Third-Party Dependency (Embedded Library/Package), Compute, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** The public package indexes the mirror draws ML frameworks from.

**Security Impact:** Moderate

**Activities:**

- **AI-4.6.1: AI Framework/Library Dependency Scanning Integration**
    - **Description:** Scan the resolved dependency set of every training image and environment against current vulnerability data as a pipeline step, covering native and accelerator-toolkit components alongside the Python packages.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-5 (partial) mapping. Scan the resolved set, not the declared one, since a few named frameworks resolve to hundreds of transitive packages and vendored native libraries. Air-gapped programs document the advisory mirror's refresh cadence alongside the update policy.

- **AI-4.6.2: Dependency Update/Patch Policy Enforcement**
    - **Description:** Set by severity the maximum time a known-vulnerable ML framework or library version may remain pinned in a training environment, document it in the VPMP, and enforce that clock against the pins Reproducibility Controls maintains.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Write this policy as an ML-specific supplement to the VPMP's remediation service levels. Allow time for retraining and revalidation, since a framework upgrade changes numerics. It pairs with Dependency Pinning Enforcement, because pinning keeps a vulnerable version in place until this clock moves it.

### AI-4.7: Model Artifact Malware/Unsafe-Deserialization Scanning

**Design Intent:** KESTREL accepts model weights only in non-executable formats such as safetensors. Every model artifact entering the registry is scanned for embedded code, and pickle-based or code-carrying formats are refused.

**NIST Control Mapping:**

- **SI-3 (partial):** claimed partial for scanning model artifacts whose format executes code on load, split from Malware Scanning's build artifacts. The base is cited because no enhancement fits artifact scanning, and a checkpoint no engine flags can still run an attacker's constructor.
- **SI-10(5) (partial):** claimed partial for restricting model artifact ingestion to approved serialization formats, split by input class from Data Poisoning Prevention and Detection's datasets. A safe format is the durable answer, while scanning is the compensating control.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Artifact/Model Registry, Compute, Self-Hosted Model, Base/Pretrained Model

**External Dependencies:** The publishers of any pretrained checkpoint or framework KESTREL adopts.

**Security Impact:** High

**Activities:**

- **AI-4.7.1: Pretrained/Base Model Artifact Scanning**
    - **Description:** Scan every pretrained, base, and third-party model artifact for embedded malicious content and for the constructs that execute on deserialization, covering pickle-backed and HDF5 checkpoints and confirming that an artifact presented as safetensors conforms to that format.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-3 (partial) mapping. Confirm format from the bytes, since extensions and declared formats are attacker-controlled. Scan inside archives and sharded checkpoints, and admit or refuse a multi-file model as a whole.

- **AI-4.7.2: Scan-Gate Enforcement Before Training/Serving Pipeline Ingestion**
    - **Description:** Refuse any model artifact that has not passed the scan, or that arrives in a serialization format the program has not approved, at the boundary where it is admitted to a training or serving pipeline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-10(5) (partial) mapping. Gate both the training and the serving entrance, since the same artifact reaches each by a different path. Make refusal the default, and handle a needed but unapproved format through a recorded approval decision.

### AI-4.8: Training Infrastructure IaC Scanning

**Design Intent:** The infrastructure as code for the training cluster, the dataset snapshots, and the model registry is scanned in the pipeline with the same policy as all other infrastructure code.

**NIST Control Mapping:**

- **CM-6(1) (partial):** claimed partial for pre-provisioning checks of training infrastructure templates, split from IaC Scanning's application infrastructure. The rules encode Baseline Configuration Standards plus training-specific settings such as privileged accelerator pools, corpus-wide roles, and public dataset stores.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.8.1: IaC Scanning Tool Integration for Training Infrastructure**
    - **Description:** Integrate the template scanner into the change path for training infrastructure code so that every proposed change to cluster, storage, registry, and network definitions is evaluated before it is applied.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-6(1) (partial) mapping. Bring vendor-module and console-wizard provisioning under infrastructure-as-code first, since a scanner cannot read configuration it never sees.

- **AI-4.8.2: Misconfiguration Policy Baseline and Gating**
    - **Description:** Author the policy rules expressing the program's approved training-platform configuration, set the severity at which a template change is blocked rather than reported, record each accepted deviation with an expiry, and document the policy baseline in the AISP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Write first the rules with no generic equivalent, covering host-device access on accelerator pools, notebook and pipeline endpoint exposure, public dataset and checkpoint stores, and registry write bindings. Put an expiry on every accepted deviation, since exceptions taken during a capacity crunch are rarely revisited.

### AI-4.9: Training Pipeline Fuzz Testing

**Design Intent:** The data loaders that parse each payload vendor's raw formats, federated updates, and products released from the IL6 enclave are fuzzed on each change. These are the inputs the training pipeline did not produce itself.

**NIST Control Mapping:**

- **SA-11(8) (partial):** claimed partial for dynamic analysis of the training ingestion path, beside DAST and Fuzz Testing. The targets are native decoders, deserializers, tokenizers, and archive readers handed files whose content was trusted but whose parse safety was not.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Compute, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.9.1: Training Pipeline Fuzz Testing Tool Integration**
    - **Description:** Stand up coverage-guided fuzzing against the pipeline's data loaders, deserializers, and preprocessing code, seed it with a corpus representative of the dataset and checkpoint formats the program actually ingests, and run it continuously rather than as a campaign.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(8) (partial) mapping. Fuzz the harness the pipeline actually calls, since bugs sit in how a loader configures a decoder. Build sanitizer versions of the native components, which is usually most of the effort.

- **AI-4.9.2: Training Pipeline Crash/Finding Triage and Remediation Workflow**
    - **Description:** Triage each crash, hang, and sanitizer report with its reproducing input attached, assess exploitability before priority is assigned, and route the resulting defects to the owning team with a remediation date.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Dispose of most findings as an upstream report plus a local mitigation, usually a format restriction or pre-parse validation. Prioritize crashes reproducible from files an approved source could deliver, and record that reasoning.

### AI-4.10: Training Pipeline API/Interface Testing

**Design Intent:** The training platform's job, dataset, and registry interfaces are tested from their schemas for authorization flaws. One check confirms that a pipeline identity cannot mount a snapshot or write a namespace that is not its own.

**NIST Control Mapping:**

- **SA-11(6) (partial):** claimed partial for reviewing the training platform's exposed interfaces, beside API Security Testing's fielded APIs. For a managed MLOps product, scope the test to its configuration rather than dropping it.
- **Declined:** SI-10 is not claimed, since these inputs are job specifications and data validity sits with Label Integrity Verification and with Data Poisoning Prevention and Detection at SI-10(5). AC-3 and AC-6 are not claimed, because the test verifies enforcement the Identity focus area and Least-Privilege Training Infrastructure Access establish.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** API/Interface Contract, Identity Platform, Compute, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.10.1: Pipeline API/Interface Security Test Integration**
    - **Description:** Drive schema-derived security tests against every training control-plane operation as part of the platform's own release process, covering job submission, dataset mount, model registration, and run metadata retrieval.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(6) (partial) mapping. Focus on operations that take a reference to something the caller does not own, such as a dataset path, registry entry, or another team's run. Re-run on platform upgrades rather than program releases.

- **AI-4.10.2: Training Pipeline Authentication/Authorization Abuse Testing**
    - **Description:** Attempt each control-plane operation as an unauthenticated caller, as an authenticated caller outside the owning team, and with another team's job, dataset, and model identifiers substituted, and record every case the platform permits.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the object-level dimension of the outcome's SA-11(6) (partial) mapping. These platforms usually authenticate well but treat every workspace member as entitled to every artifact, so this test shows whether Least-Privilege Training Infrastructure Access holds.

### AI-4.11: Training Pipeline Misuse/Abuse Case Testing

**Design Intent:** Abuse cases from each model's threat model are run against the training pipeline in ML Dev/Test. Examples include a federated update crafted to backdoor the aggregate, a correction flood from one account, and a run that tries to mount another snapshot.

**NIST Control Mapping:**

- **SA-11(2) (partial):** claimed partial for the vulnerability analysis dimension applied to the training pipeline, while AI Threat Modeling holds threat modeling. That outcome identifies attacks and this one performs them, such as running a seeded sample through the real pipeline.
- **Declined:** SA-15(2) is not claimed, since results enter AI Threat Modeling's tracked path. CA-8 is not claimed, because this is the engineering team testing its own pipeline rather than an independent engagement, which Penetration Testing holds.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Compute, Application/API, Storage/Database, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.11.1: Misuse/Abuse Case Scenario Definition**
    - **Description:** Write, from the ML threat model's findings, the concrete abuse scenarios that apply to the program's own training pipeline, stating for each one the attacker's position, the action attempted, and the result that would count as a failure, and document the scenarios in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Write scenarios an insider with legitimate pipeline access could attempt, such as mounting another team's corpus, promoting an ungated checkpoint, or altering a run's configuration after review. Name each failure condition in advance so the scenario is testable.

- **AI-4.11.2: Abuse Case Test Execution and Findings Tracking**
    - **Description:** Execute the defined scenarios against a representative pipeline environment on the cadence the program sets, and record for each one what the pipeline permitted, what it blocked, and what it failed to detect.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(2) (partial) mapping. Record what the pipeline failed to detect, since a blocked attempt that alerted nobody invites a patient variant. Use a representative environment, because several scenarios look exactly like the attack they model.

### AI-4.12: Signed/Verified Training Pipeline Definitions

**Design Intent:** Training pipeline definitions use the Platform Team's signed templates and are verified before each run. A definition changed outside an approved merge stops the run.

**NIST Control Mapping:**

- **CM-14 (partial):** claimed partial for refusing to execute a training pipeline definition not signed with a recognized key. Unlike a CI definition, it decides which data and hyperparameters the model sees, while Signed/Verified Pipeline Definitions holds the CI slice.
- **SA-10 (partial):** claimed partial for configuration management of a definition the orchestrator reads every run, split from Signed/Verified Pipeline Definitions. The base is cited because no enhancement covers an orchestrator verifying its own configuration item.
- **Declined:** CM-3(1) is not claimed, since Pre-Merge Sensitive Repo File Change Detection governs the reviewed path, and this outcome catches changes that bypassed it.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** CI/CD Pipeline, Compute, Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-4.12.1: Training Pipeline-as-Code Signing and Verification**
    - **Description:** Sign each training pipeline definition as it is merged, and verify the signature against the program's recognized keys before the orchestrator executes it, refusing execution on a missing or invalid signature.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-14 (partial) and SA-10 (partial) mappings, using the signing identity Training Artifact Signing establishes. Settle early whether the orchestrator can verify before executing. If not, render the signed definition into the platform through a controlled deploying identity nobody else holds.

- **AI-4.12.2: Unauthorized Training Pipeline Modification Detection**
    - **Description:** Compare the definition the orchestrator is about to execute against the signed version of record, and alert on any definition altered through the platform's console, API, or a local override rather than through the reviewed path.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Watch console and API edits, since fixing a failing run in place is a common habit, and alert volume shows how far the reviewed path is bypassed. Compare runtime parameter overrides at submission as well as edits to the stored definition.

### AI-4.13: Reproducibility Controls

**Design Intent:** Every training environment pins its dependency versions and image digest, and the run record captures both. Certification to Field reproduces a sample of runs to confirm the pins hold.

**NIST Control Mapping:**

- **CM-2(2) (partial):** claimed partial for fixing each pipeline run's pinned dependency set and image digest as a condition of starting. Experiment Tracking and Reproducibility records what exploratory runs used, after the fact.
- **SI-7(1) (partial):** claimed partial for the integrity check on the environment at run start, a defined transitional state. Data Poisoning Prevention and Detection holds the corpus slice.
- **Declined:** SA-15 is not re-claimed, since Experiment Tracking and Reproducibility holds the experimentation standard.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Self-Hosted Model, Object/File Storage, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.13.1: Dependency Pinning Enforcement**
    - **Description:** Require every training environment to declare its dependencies as exact, content-addressed versions including transitive ones, and reject a pipeline run whose environment resolves any dependency at build or run time.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-2(2) (partial) mapping. Pin a content hash for every resolved package and an image digest rather than a tag, since versions can be republished. Include the accelerator toolkit and driver stack, which move numerics too. Dependency Update/Patch Policy Enforcement supplies the clock that moves these pins.

- **AI-4.13.2: Environment Hash Verification at Training Run Start**
    - **Description:** Compute the hash of the assembled training environment at the start of each run, compare it against the approved baseline recorded for that pipeline, and halt the run on mismatch rather than recording the difference and proceeding.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(1) (partial) mapping. Verify at run start, since startup scripts, overlays, or side-loaded wheels can change an approved image. Record the verified hash in the run record and the AI-BOM.

### AI-4.14: Training Artifact Signing

**Design Intent:** Every trained artifact is signed as the pipeline's last step, with keys held in the HSMs, and the signature binds the artifact to its run record and dataset snapshot. Serving platforms and aircraft load only signed artifacts.

**NIST Control Mapping:**

- **CM-14 (partial):** claimed partial for the finished artifact the training pipeline emits, the last ML slice. Signed/Hashed Reference Models holds experiment checkpoints, the pipeline's inputs.
- **SI-7(15) (partial):** claimed partial for the program's own trained weights, verified by the serving stack against a registry entry at load. Image Signing holds container images, which an admission controller verifies at deployment.
- **Declined:** SR-4(3) is not claimed, since the program's own output does not arrive from an external supply chain.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Artifact/Model Registry, Compute, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-4.14.1: Model Signing Key Management and Infrastructure**
    - **Description:** Establish the ML artifact signing identity, its key material, and its issuance, rotation, and revocation arrangements against the program's key management infrastructure, and record them in the KMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since key management belongs to the Data focus area's cryptographic outcomes and the KMP. Keep the key in hardware or a managed key service, and give the pipeline a workload identity that requests signatures. Decide the revocation path before the first signature, since a compromised identity means re-evaluating everything it signed. Signed/Hashed Reference Models uses the same identity.

- **AI-4.14.2: Automated Training Artifact Signing and Verification Enforcement**
    - **Description:** Sign each trained artifact as the terminal step of the pipeline that produced it, bind the signature to that run's record, and verify the signature before the serving stack loads the artifact, refusing an unsigned or unrecognized one.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-14 (partial) and SI-7(15) (partial) mappings, which turn on refusal. Sign at the pipeline's terminal step rather than at upload, so the signature attests to what the pipeline produced. Bind it to the run record so verification shows which run, corpus, and environment produced the weights.

### AI-4.15: AI-BOM Generation

**Design Intent:** Every model version gets an AI-BOM listing its dataset snapshots, base checkpoint, hyperparameters, frameworks, and the payload vendor terms its data falls under. It is stored in the model registry with the artifact.

**NIST Control Mapping:**

- **SR-4 (partial):** claimed partial for the provenance of models the program trains, recording the dataset snapshot, base checkpoint digest, and hyperparameters an SBOM has no field for. SBOM Generation and Enrichment holds software composition, and the AI-BOM is carried alongside the serving container's SBOM rather than merged.
- **SR-4(1) (partial):** claimed partial for uniquely identifying those components using identifiers upstream outcomes already set, such as Dataset Lineage and Version Control's snapshot identifiers. SBOM Generation and Enrichment holds the software-component slice.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, CI/CD Pipeline, Object/File Storage, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.15.1: Automated AI-BOM Generation**
    - **Description:** Emit a machine-readable bill of materials from every training run, listing the dataset snapshot identifiers consumed, the base model and its digest, the hyperparameter set, the pinned dependency and environment hashes, and the resulting artifact digest.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4 (partial) and SR-4(1) (partial) mappings. Emit the manifest from the run, since one assembled later is an assertion rather than a record. Pick an AI-BOM format now and record any added fields rather than waiting for a settled standard.

- **AI-4.15.2: AI-BOM Storage and Distribution**
    - **Description:** Store each bill of materials keyed to the artifact digest it describes, and make it retrievable by the serving, validation, and assessment consumers that need it without requiring access to the training platform itself.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Key manifests to the artifact digest, since two runs of one pipeline produce weights a version string will not distinguish. Index on components, so the program can list every model built on a compromised snapshot or vulnerable framework.

### AI-4.16: Training Job Audit Logging

**Design Intent:** Every training job's submission, configuration, data access, and output is logged to the security monitoring platform, where the ML team's administrators cannot change it.

**NIST Control Mapping:**

- **AU-9(3) (partial):** claimed partial for cryptographically protecting training records, since a platform administrator could otherwise alter them. Approver and Reviewer Audit Log holds the code review slice.
- **AU-12 (partial):** claimed partial for generating records of training job events, one event class feeding the Operate pillar's trail. AU-12(1) stays with SIEM Capabilities. Capture enough to show sequences such as unusual corpora, cancel-and-resubmit with changed configuration, and writes to unusual registry paths.
- **Declined:** AU-11 and AU-6 are not claimed, since the Operate pillar holds program-wide retention and review.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Self-Hosted Model, Storage/Database, Identity Platform

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.16.1: Training Job Event Capture and Immutable Logging**
    - **Description:** Capture every training job submission, configuration, data mount, completion, failure, and cancellation event with its initiating identity, and write it to a store the training platform's administrators can neither modify nor delete.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-12 (partial) and AU-9(3) (partial) mappings. Record the human behind each submission, not only the service account. Record scheduled retraining runs on the same terms, since attackers prefer that path.

- **AI-4.16.2: Audit Log Retention and Review Workflow**
    - **Description:** Set the retention period for training job records against the service life of the models those runs produced, and define who reviews them, on what cadence, and what a reviewer escalates.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, contributing a training-specific retention period and review scope to the Operate pillar's process. Set retention at least as long as a model's service life, since platform defaults are usually weeks. Review the named sequences rather than every record.

### AI-4.17: Privileged Config Change Alerting

**Design Intent:** Changes to the training platform's role bindings, service account grants, storage policies, admission rules, and gate thresholds alert the Security Team. A change with no matching approved request is investigated as an incident.

**NIST Control Mapping:**

- **CM-3(1) (partial):** claimed partial for detecting live control-plane changes to training configuration and notifying the approver, since role bindings and registry policies rarely pass through a commit. Asset Lifecycle Change Control holds the change process itself.
- **CM-3(4) (partial):** claimed partial for placing a security reviewer in that decision after the fact. Where the platform can hold a privileged change for approval, use that path instead.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Privileged Access Management, Application and Service Account Identity, Object/File Storage, Artifact/Model Registry, Self-Hosted Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.17.1: Privileged Training-Config Change Detection Rules**
    - **Description:** Define and deploy the rules that fire on change to the training platform's privileged configuration, covering cluster role bindings, pipeline service-account grants, artifact store and registry policies, admission rules, and the gate thresholds this capability's other outcomes set.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the detection dimension of the outcome's CM-3(1) (partial) mapping. Keep the rule set short so reviewers keep reading alerts. Include the rules' own configuration in the watched set.

- **AI-4.17.2: Privileged Config Change Alert Routing and Review Workflow**
    - **Description:** Route each detected privileged configuration change to a reviewer able to confirm it against an approved request, record the disposition, and escalate as a potential incident any change with no corresponding request.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-3(4) (partial) mapping and the notification dimension of CM-3(1). Route to a reviewer independent of the platform team that usually makes these changes. Decide escalation into incident response in advance, since an unexplained change may be an intrusion.

### AI-4.18: Hyperparameter Change Alerting

**Design Intent:** Each model's certification sets an approved envelope for retraining, including hyperparameter ranges. A run whose hyperparameters change outside that envelope alerts the ML team and the PMO ISSE, and its output needs full Certification to Field instead of passing on the pipeline's evidence.

**NIST Control Mapping:**

- **CM-6(1) (partial):** claimed partial for verifying a run's hyperparameters against the approved baseline, values that shape what a model learns. Training Infrastructure IaC Scanning holds the infrastructure half.
- **CM-6(2) (partial):** claimed partial for the alert and, for large deviations, the halt, beside Configuration Policy Orchestration's device-drift response.
- **Declined:** CM-2(2) is not claimed, since Experiment Tracking and Reproducibility and Reproducibility Controls hold the baseline this outcome compares against.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Compute, Base/Pretrained Model, Fine-Tuned Model

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-4.18.1: Hyperparameter Change Detection and Baseline Diffing**
    - **Description:** Diff the hyperparameter set of every promotion-bound and scheduled retraining run against the approved baseline for that pipeline, and record the difference as a first-class field of the run record.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-6(1) (partial) mapping. Diff the values the run actually used, since submission overrides, environment variables, and tuning sweeps bypass the file. Record the difference on the run record as well as in the alert.

- **AI-4.18.2: Unauthorized/Anomalous Hyperparameter Change Alerting**
    - **Description:** Alert on any hyperparameter deviation that no change request or tracked experiment accounts for, and halt the run where the deviation exceeds the bounds the program permits without review.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-6(2) (partial) mapping. It is Level 2 because detection is the floor and a careless halt on a multi-day job is costly. Set tighter bounds on sampling weights, class balancing, and augmentation, which an attacker would move to change what the model learns.

### AI-4.19: Training Credential Secrets Management

**Design Intent:** Training jobs authenticate to the dataset snapshots and the model registry with short-lived workload credentials. Any remaining secret comes from ML Dev/Test's vault at run time.

**NIST Control Mapping:**

- **IA-5(6) (partial):** claimed partial for vaulting training authenticators with lifetimes short enough to expire before misuse. CI Credential and Secrets Management holds the build slice, while training jobs reach more sensitive data stores, feature stores, labeling services, and registries.
- **IA-5(7) (partial):** claimed partial for keeping static credentials out of training configuration and platform settings. Training Code Secret Scanning removes committed credentials, while this outcome removes the reason to commit them.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Cloud Workload/Native Platform Identity, Compute, Self-Hosted Model, Secrets Vault

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-4.19.1: Short-Lived/Ephemeral Training Credential Issuance**
    - **Description:** Issue each training run workload-bound credentials scoped to the stores and registries that run requires, with a lifetime short enough to expire before a leaked token is useful and a refresh path that covers multi-day runs.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(6) (partial) mapping. Refresh credentials in-run against the workload identity for multi-day jobs, rather than stretching lifetimes. Scope each credential to the run so the audit record attributes access.

- **AI-4.19.2: Training Secrets Vault Integration**
    - **Description:** Retrieve every secret a training job needs from the program's vault at run time, and prohibit credentials in training code, notebooks, run configuration, and the training platform's own stored settings.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(7) (partial) mapping. Route secrets through the program's vault, since workspace-scoped platform secret features are readable by every member and visible in logs. Keep secrets out of notebook output cells.

## AI-5: Validation and Continuous Delivery

### AI-5.1: Jailbreak Testing

**Design Intent:** Every language model use case is tested against a versioned jailbreak corpus before Certification to Field, as part of the PMO ISSE's AI Cyber T&E for significant changes. The corpus adds program-specific attempts, such as requests to reveal sources and methods or to draft a plan outside approved areas.

**NIST Control Mapping:**

- **SA-11 (partial):** claimed partial for the model's resistance to instructions that defeat its safety alignment, the first of five attack-class slices this capability holds alongside DAST. The base is cited because no enhancement describes adversarial evaluation of a trained model. Model Serving's Filter Bypass/Evasion Testing checks one installed filter, while this suite tests the model's overall behavior, and neither substitutes for the other.
- **Declined:** SA-11(1) and SA-11(8) analyze code, not model behavior. SA-11(4), SA-11(6), and SA-11(9) have no subject here. SA-11(2) is not extended, since these suites use a maintained technique corpus rather than the program's threat model. SA-11(3) and SA-11(7) belong to Validation Report Review. SI-15 stays with Content Filtering, which receives findings as input.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-5.1.1: Jailbreak Prompt Corpus/Technique Testing**
    - **Description:** Assemble a versioned corpus of role-play, persona, encoding, multi-turn escalation, and system-prompt-extraction techniques drawn from published research and the program's own findings, and execute it against each candidate model version as a gate before certification.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the testing dimension of the outcome's SA-11 (partial) mapping. Define a refresh source and cadence for the corpus, since jailbreak techniques turn over in weeks. Score partial compliance with a rubric and a sampled human check behind any automated judge, and version the corpus with the model so new failures are distinguishable from new techniques.

- **AI-5.1.2: Jailbreak Finding Remediation and Guardrail Tuning**
    - **Description:** Open a tracked item for each successful jailbreak with a named owner and disposition, and route the technique to the remediation that fits it, whether system-prompt hardening, preference or fine-tuning data, or a rule added to the serving-layer content filter.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the flaw-correction dimension of the outcome's SA-11 (partial) mapping. Where a jailbreak cannot be fixed in the weights, accept it with compensating Content Filtering rules and record it as residual risk in Certification to Field's risk acceptance log. Treat system-prompt-only fixes with skepticism, and validate any fix against variants, not only the original string.

### AI-5.2: Prompt Injection Testing

**Design Intent:** Every language model use case is tested for prompt injection through each path content reaches it. For the LLM analyst assistant, that includes injected instructions planted in mission reports and in products released from the IL6 enclave. For AI agents, it includes injected instructions in tool responses.

**NIST Control Mapping:**

- **SA-11 (partial):** claimed partial as the second attack-class slice on the basis set out under Jailbreak Testing, for the model's failure to keep instructions separate from data. A model can resist jailbreaks and still accept an untrusted source as its instruction-giver.
- **Declined:** SI-10 is not reopened, since Input Validation checks structure and this outcome measures a semantic failure in valid requests. AC-3 and AC-6 are not claimed, since Retrieval-Augmented Generation (RAG) and Vector Store Security and AI Agent Identities own the entitlement fixes. SI-15 stays with Content Filtering.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Prompt/Instruction Layer, AI Agent, Retrieval-Augmented Generation (RAG), Vector Store/Embedding Index, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-5.2.1: Direct/Indirect Prompt Injection Test Suite Execution**
    - **Description:** Execute a maintained suite of direct and indirect injection cases against the model in its deployed configuration, planting indirect payloads in retrieval corpora, tool responses, and uploaded documents rather than only in the request, and record for each case whether the injected instruction actually took effect.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the testing dimension of the outcome's SA-11 (partial) mapping. Include indirect injection by standing up the retrieval path and tool integrations, and test the deployed configuration rather than the bare model. Record whether the model took the injected action, not whether it repeated the text. It is Level 1 for any model with retrieval, tool invocation, or a downstream parser, and Level 2 otherwise.

- **AI-5.2.2: Injection Finding Remediation and Guardrail Tuning**
    - **Description:** Track each successful injection to a remediation that constrains what a compromised turn can accomplish, including confirmation on tool invocation, reduced privilege on the retrieval and tool identity, and provenance marking of untrusted content, and re-execute the case to confirm closure.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the flaw-correction dimension of the outcome's SA-11 (partial) mapping. Prefer architectural fixes that bound what the model may do, since telling it to ignore injected instructions can be out-argued. The owning outcomes implement fixes, such as Agentic Tool-Call/Action Output Validation escalating untrusted-content directives to High-Risk Action Human Approval Gate (AI Agent Identities). Close a case only on a re-execution of the original path and a variant.

### AI-5.3: Adversarial Evasion Robustness Testing

**Design Intent:** Each detection model is tested against evasion attacks within the perturbation budgets its robustness requirements set. These include adversarial patches and camouflage for imagery, and spoofed or altered emitters for signals. Results are measured against the AISP thresholds.

**NIST Control Mapping:**

- **SA-11 (partial):** claimed partial as the third attack-class slice on the basis set out under Jailbreak Testing, for generating and running adversarial examples optimized against this model. Out-of-Distribution Robustness Testing covers naturally occurring novel inputs, and Input Validation cannot see well-formed adversarial examples.
- **RA-9 (partial), SA-15(1) (partial):** the verifying half of the joint claim Robustness Requirements Definition holds from the writing side. That outcome sets the criteria from mission criticality, and this one produces the evidence, so the two are tracked together.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Application/API, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-5.3.1: Adversarial Example Generation and Evasion Testing**
    - **Description:** Generate adversarial examples against the candidate model using the white-box gradient, black-box query, and transfer attack classes the robustness baseline specifies, at each perturbation budget it names, and record the accuracy retained under each attack.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11 (partial) mapping. Test white-box as well as black-box, and certify against the white-box figure, since weights can be lost. Run attacks to convergence with enough iterations and restarts, because gradient masking makes an underpowered attack overstate robustness. Keep budgets and the evaluation partition fixed so versions compare.

- **AI-5.3.2: Robustness Threshold Validation Against Acceptance Criteria**
    - **Description:** Compare each candidate's measured robustness against the thresholds Robustness Requirements Definition set for its attack classes and perturbation budgets, and fail the candidate to the certification gate rather than recording a shortfall as an observation.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-9 (partial) and SA-15(1) (partial) mappings, consuming Robustness Requirements Definition's baseline directly. A candidate that misses a threshold needs either a risk acceptance in Certification to Field's approval log or an approved criterion change, never an adjustment in the report. Report each attack class separately rather than as an average.

### AI-5.4: Data Poisoning Testing

**Design Intent:** Poisoning tests seed a controlled fraction of a training snapshot with backdoor triggers and flipped labels, and of the federated rounds with crafted updates. The real pipeline then trains in the evaluation environment. The tests measure how much contamination each model absorbs before its screens or the aggregator's defenses catch it.

**NIST Control Mapping:**

- **SA-11 (partial):** claimed partial as the fourth attack-class slice on the basis set out under Jailbreak Testing, for a simulated poisoning sweep that reports where the model becomes backdoored and where the screen goes quiet. Training Pipeline Misuse/Abuse Case Testing instead checks whether gates blocked named scenarios.
- **Declined:** SI-7(1), SI-7(5), and SI-10(5) stay with Data Poisoning Prevention and Detection, since this outcome measures the trained model and installs nothing. SA-11(2) is not extended, for the reason set out under Jailbreak Testing.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Base/Pretrained Model, Fine-Tuned Model, Object/File Storage, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-5.4.1: Simulated Poisoning Attack Testing Against Training Pipeline**
    - **Description:** Inject backdoor-trigger and label-flipped samples at a series of controlled contamination rates into a copy of the training corpus, run each copy through the program's real training pipeline inside the evaluation environment, and measure the attack success rate and clean-data accuracy of every resulting model.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11 (partial) mapping. Recurring cost is High, so use a few contamination rates annually or a stated proxy model. It is Level 3 because Data Engineering's boundary and screen are the floor. Record clean-data accuracy beside attack success, and keep seeded corpora and their models inside the Secure Model Evaluation Environment.

- **AI-5.4.2: Poisoning Detection Control Validation**
    - **Description:** Measure the sensitivity of the Data Engineering poisoning screen by running each seeded corpus from the sibling activity back through it, and record the contamination rate and trigger design below which it stops flagging as that screen's documented detection floor.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the assessment-evidence dimension of the outcome's SA-11 (partial) mapping. Measure the detection floor Statistical/Anomaly-Based Poisoning Detection cannot report about itself, and compare it with the susceptibility curve. A gap between the rate that backdoors the model and the rate the screen catches is a residual risk with a number.

### AI-5.5: Out-of-Distribution Robustness Testing

**Design Intent:** Each detection model is tested on out-of-distribution inputs, such as new weather, terrain, sensor faults, and emitter types it was not trained on. The test checks that it lowers its confidence rather than answering wrongly with high confidence.

**NIST Control Mapping:**

- **SA-11 (partial):** claimed partial as the fifth attack-class slice on the basis set out under Jailbreak Testing, for behavior on inputs outside the training distribution. Its defense is abstention and calibrated confidence, unlike adversarial robustness, and Data Drift Detection and Alerting covers production drift.
- **Declined:** SI-10 is not reopened, since Input Validation's structural checks cannot see valid but unfamiliar inputs.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-5.5.1: OOD Input Test Suite Execution**
    - **Description:** Assemble a test set of inputs outside the training distribution, covering degraded and corrupted inputs, unseen classes, and content from operational contexts the corpus did not represent, and execute it against each candidate model recording the confidence assigned to every wrong answer.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the testing dimension of the outcome's SA-11 (partial) mapping, consuming Robustness Requirements Definition's shift scope. Build inputs from known operational contexts, such as a different sensor, season, theater, or partner format, since a held-out split is in-distribution. Record confidence on each wrong answer, because abstention can handle unsure errors but not certain ones.

- **AI-5.5.2: OOD Detection/Rejection Behavior Validation**
    - **Description:** Verify that the model and its serving path abstain, return a low-confidence signal, or route to a human across the out-of-distribution test set instead of emitting a confident prediction, and record the residual rate of confident wrong answers against the acceptance criteria.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the assessment-evidence dimension of the outcome's SA-11 (partial) mapping. Calibrate scores before setting an abstention threshold. A model with no abstention path is an architectural finding routed to the design gate, and in a control system the abstention lands on the safe mode Rollback/Kill-Switch Mechanism defines.

### AI-5.6: Privacy-Attack Testing

**Design Intent:** Membership inference and inversion tests run against each detection model trained on imagery containing people, and against any model fine-tuned on reports. They show whether a specific record can be recovered.

**NIST Control Mapping:**

- **SI-19(8) (partial):** claimed partial for motivated intruder testing of the trained model, the derivative that carries de-identified data forward in its weights. Dataset De-Identification and Disclosure Review holds released datasets, and results are read with Embedding Inversion Resistance Testing.
- **Declined:** SI-19 and SI-19(4) are not joined, since this outcome measures whether applied techniques worked. SI-19(6) is not joined, though differential privacy is the usual remediation. SA-11 is not joined, since SI-19(8) names this mechanism directly. RA-8 stays with Privacy Requirements Definition, which takes these results as input.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Base/Pretrained Model, Fine-Tuned Model, Storage/Database

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-5.6.1: Membership Inference Attack Testing**
    - **Description:** Execute membership inference attacks against the candidate using shadow-model and confidence-threshold techniques over records known to be inside and outside the training set, and report the attacker's advantage over chance for each sensitive data category the privacy baseline identified.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-19(8) (partial) mapping. Report attacker advantage over chance rather than raw accuracy. Overfitting drives the result, so remediation is usually regularization, early stopping, or the differential privacy held under SI-19(6). Run it on each new model version trained on in-scope data.

- **AI-5.6.2: Model Inversion/Data Extraction Attack Testing**
    - **Description:** Attempt to reconstruct training records from the candidate through gradient inversion, class-representative reconstruction, and prompted verbatim extraction, and record every recovered fragment against the classification and personal-information category it belongs to.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-19(8) (partial) mapping. For generative models, prompt for memorized continuations of known prefixes before trying gradient-based techniques. Treat a recovered record as a disclosure event through the incident process, record it by category, and read results with Embedding Inversion Resistance Testing.

### AI-5.7: Red Teaming

**Design Intent:** An independent AI red team attacks every new AI use case and every change of foundation model in combination, such as a planted report that steers the assistant into misusing an agent's tool. The PMO ISSE scopes each exercise, and the red team works outside the performer.

**NIST Control Mapping:**

- **SA-11(5) (partial):** claimed partial for human-led testing of the trained model and its serving scaffolding, while Penetration Testing holds the fielded application.
- **Declined:** CA-8(2) is not claimed, though its language fits, because its discussion assesses the defending organization and Adversary Emulation and Detection Validation already holds it full. Unlike On-Device Extraction Resistance under SC-39(1), the reservation here named a pillar rather than a mechanism. Where the tailored baseline includes CA-8(2), its model-behavior dimension is a live gap under the Control Mapping Methodology. CA-8 is held full by Penetration Testing, CA-8(1) is not joined since independence sits under SA-11(5), and CA-2(2) belongs to Control Assessment Scheduling and Annual Security Review within the Manage pillar's CA-2 allocation.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Application/API, Compute

**External Dependencies:** The penetration testing provider, whose AI red team runs each exercise under its rules of engagement.

**Security Impact:** Moderate

**Activities:**

- **AI-5.7.1: Red Team Exercise Scoping and Scheduling**
    - **Description:** Define for each exercise the model, serving configuration, retrieval corpora, and tool integrations in scope, the rules of engagement and permitted techniques, which for an agentic deployment include scope-boundary evasion, high-risk-action approval gate bypass, session-timeout-control bypass, and unauthorized tool-call chaining, the team's independence from the model's builders, and the recurrence and the changes that re-trigger it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the scoping and independence dimensions of the outcome's SA-11(5) (partial) mapping. Name the mission harms the exercise should produce, and record the independence level achieved with its limits. Treat the annual cadence as a floor, and re-run after a base model swap, prompt or tool change, or new retrieval corpus. For agentic deployments, add techniques that validate specific mechanisms, namely scope-boundary evasion against Agent Tool/API Access Scoping and Agentic Session Timeout and Forced Termination, approval-gate bypass against High-Risk Action Human Approval Gate and Provenance-Gated Escalation to Human Approval, session-timeout bypass, and chaining of individually valid calls past Tool-Call Schema and Parameter Validation Against Action Contract.

- **AI-5.7.2: Red Team Finding Remediation Tracking and Validation**
    - **Description:** Convert each accepted red team finding into a tracked item carrying an owner, a severity, and a remediation date, and validate closure by having the team re-execute the original path and a variant of it rather than by accepting a written description of the fix.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the corrective-action dimension of the outcome's SA-11(5) (partial) mapping. Retest with variants, since a fine-tune or guardrail fix removes no code path. Send unclosable findings to Certification to Field's Red-Team Findings Sign-Off and dated ones to a POA&M item, and extend the automated corpus when a finding should have been caught there.

### AI-5.8: Model Card Generation

**Design Intent:** The pipeline generates a model card for each certified version from its validation results. The card states the model's intended use, its tested conditions and limits, its known failure modes, and the envelope approved for retraining. Operators and analysts can read the card for the model they use.

**NIST Control Mapping:**

- **SA-5 (partial):** claimed partial for a model card's intended use, evaluation conditions, unfit uses, and failure modes for operators. SA-5 has no enhancements. The card's wider transparency purpose has no SP 800-53 control and is recorded as a gap.
- **Declined:** the SA-15 family is declined, since it addresses development processes rather than per-version documentation. PT-5 is declined, since it governs notice to individuals, not operator documentation. RA-8 stays with Privacy Requirements Definition.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Artifact/Model Registry

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-5.8.1: Automated Model Card Generation from Validation/Test Artifacts**
    - **Description:** Generate each version's model card automatically from the evaluation metrics, robustness and adversarial test results, dataset lineage records, and AI-BOM the pipeline already produces, rather than transcribing them into a document by hand.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the authoring dimension of the outcome's SA-5 (partial) mapping. Generate the card on every build so it stays true. Separate generated results from reviewed prose on intended use, out-of-scope use, and ethics, sourcing from Experiment Tracking and Reproducibility, Dataset Lineage and Version Control, AI-BOM Generation, and this capability's test outputs.

- **AI-5.8.2: Model Card Review and Publication Workflow**
    - **Description:** Route each generated card through review by the model owner and the security and privacy reviewers the program designates, and publish the approved card with the registered model version so that it travels with the artifact into every environment the model is delivered to.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the review and publication dimension of the outcome's SA-5 (partial) mapping. Review limitations and out-of-scope use most closely, since they invite vagueness. The certification-gate review belongs to Model Card Review. Carry the card in the signed package Offline/Air-Gapped Model Integrity Verification assembles so disconnected deployments receive it.

## AI-6: Certification to Field (CtF)

### AI-6.1: Validation Report Review

**Design Intent:** The PMO ISSE reviews each candidate's validation report against the test classes and thresholds the AISP sets for its risk tier, before the gate decision. Missing coverage counts as a failure, not as a pass.

**NIST Control Mapping:**

- **SA-11(3) (partial):** covers independent verification of the evidence the validation suites produced. It is partial because it covers ML validation only, and the remaining development effort is recorded as a gap under the Control Mapping Methodology.
- **SA-11(7) (partial):** covers verifying that testing reached the required scope and depth, since no individual suite asks whether the full set of results was delivered. It is partial on the same ML-only basis, with the same recorded gap.
- **Declined:** the SA-11 base stays with the outcomes that run the tests. SA-11(5) belongs to Red-Team Findings Sign-Off. CA-2 is held by the Manage pillar's assessment capability.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-6.1.1: Validation Report Completeness/Accuracy Review**
    - **Description:** Check each candidate's consolidated validation report against the required test classes, evaluation partitions, and acceptance thresholds, and trace a sample of its reported figures back to the pipeline artifacts that produced them.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(7) (partial) mapping and the verification act of its SA-11(3) (partial) mapping. Check the report against the required-test-class manifest rather than its own contents, so missing classes show up. Trace a sample of figures back to source runs, and confirm the thresholds used match the requirements baseline in force when the candidate entered the gate.

- **AI-6.1.2: Validation Report Sign-Off and Gate Decision**
    - **Description:** Record the reviewer's decision to certify, certify with conditions, or reject the candidate, naming the report version examined and the reviewer's independence from the team that produced it, and hold promotion until that record exists.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the independence dimension of the outcome's SA-11(3) (partial) mapping. Record the reviewer's independence with its limits rather than asserting it. Certify with conditions when uses must be limited, carrying the conditions into the registration record. Return a rejected candidate to testing rather than opening a risk acceptance.

### AI-6.2: Model Card Review

**Design Intent:** The PMO ISSE checks each model card against the evidence behind it before certification. A card whose limits are vague or that omits a known failure mode is sent back.

**NIST Control Mapping:**

- **SA-5 (partial):** claimed partial for deciding at the certification gate whether the documentation is adequate to field the model, while Model Card Generation authors and publishes the card. SA-5 has no enhancements, and the transparency gap recorded there applies here too.
- **Declined:** SA-11(3) and SA-11(7) stay with Validation Report Review, since this outcome judges how faithfully the card represents evidence rather than the evidence itself.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Artifact/Model Registry

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-6.2.1: Model Card Certification-Gate Review**
    - **Description:** Review each candidate's card for factual agreement with the validation and red team evidence, presence of every section the program requires, and disclosure of the known failure modes, out-of-scope uses, and data characteristics an operator has to act on.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-5 (partial) mapping. Focus on the authored sections, namely intended use, out-of-scope use, and limitations, and ask whether a reader could tell when to stop trusting the model. Review against this candidate's own evidence, since a card carried forward from a prior version describes something else.

- **AI-6.2.2: Model Card Sign-Off for Deployment Gate**
    - **Description:** Bind an explicit acceptance or rejection of the reviewed card to the specific model version it describes, and block that version from certification until an accepted card is attached to it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the acceptance dimension of the outcome's SA-5 (partial) mapping. Bind acceptance to the model version so a later card edit is visible. Turn any caveat into a condition on the registration record, and flag a signed-off version whose card never reached its enclave.

### AI-6.3: Red-Team Findings Sign-Off

**Design Intent:** Every red team finding above the AISP's must-fix severity needs a validated fix, or a risk acceptance, before the use case can be certified. The PMO ISSE signs off on each closure.

**NIST Control Mapping:**

- **SA-11(5) (partial):** claimed partial for auditing, at fielding, whether red team findings are in a state certification can rest on. Red Teaming holds the exercise and its remediation, and a closure backed by description rather than a failed reproduction is rejected here.
- **Declined:** CA-8 and CA-8(2) are not reopened, for the reasons Red Teaming records. RA-7 is not claimed, since acceptances are recorded through Risk Acceptance and Approval Log.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Application/API, Compute

**External Dependencies:** The penetration testing provider, whose AI red team runs each exercise under its rules of engagement.

**Security Impact:** Moderate

**Activities:**

- **AI-6.3.1: Red-Team Finding Remediation Verification**
    - **Description:** Confirm for each finding from the current exercise that its recorded closure rests on a documented failed reproduction rather than a description of the change made, and identify every finding that is open, deferred, or past its remediation date.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(5) (partial) mapping. Require the variant retest Red Team Finding Remediation Tracking and Validation should have run, and treat its absence as an open finding. Recheck findings inherited from earlier exercises against the retrained model. For compensating-control closures, record what the control was measured to block.

- **AI-6.3.2: Red-Team Sign-Off and Residual-Risk Acceptance**
    - **Description:** Have the accepting authority decide on the population of findings still open at the gate, capturing each accepted finding, the compensating controls relied on, and the expiration of the acceptance, and route that decision into the capability's risk acceptance log.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Accept findings one at a time, by the PMO ISSE or above and never by the blocked team. Give each acceptance an expiration and re-decide it at the next certification. Findings accepted with remediation intent still open a POA&M item through the Manage pillar.

### AI-6.4: Risk Acceptance and Approval Log

**Design Intent:** Every risk acceptance made at AI certification is logged with its rationale, approver, compensating measures, and expiry. Each one also feeds the program's risk register, so the AO sees every accepted AI risk.

**NIST Control Mapping:**

- **RA-7 (partial):** claimed partial for recording and preserving per-model-version acceptances at the fielding gate, under a delegation inside the authorization. The Manage pillar's Risk Acceptance Process holds program-level residual risk and receives anything that moves it, while Model Deployment Risk Threshold Evaluation holds the automated block-or-promote response.
- **AU-12 (partial):** claimed partial for generating records of risk-acceptance decision events, one event class fed into the Operate pillar's trail. AU-12(1) stays with SIEM Capabilities.
- **Declined:** AU-9(3) is not reopened, since the events go to the log pipeline Approver and Reviewer Audit Log and Training Job Audit Logging already protect. CA-6 is not claimed, because these are delegated decisions inside an existing authorization, and the Manage pillar reconciles this log with the authorization package. CA-2 stays with the Manage pillar.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Storage/Database

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-6.4.1: Risk Acceptance Decision Capture and Approval Routing**
    - **Description:** Route every proposed acceptance arising at this capability's gates to the authority entitled to grant it under the program's delegation, and capture the granted decision as a log entry naming the model version, the specific risk, the compensating controls, the accepting authority, and the expiration.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-7 (partial) mapping. Name in the delegation the threshold at which a decision moves from the PMO ISSE to the AO. Reference the gate finding rather than restating it, and give every entry an expiration.

- **AI-6.4.2: Risk Acceptance Log Audit Trail Maintenance**
    - **Description:** Emit every creation, modification, extension, and expiry of a log entry as an audit record into the program's log pipeline, and keep the log's live state reconcilable against that record.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-12 (partial) mapping. Capture extensions as events, since a risk extended eleven times otherwise looks like one accepted for a year. Send events to the existing log pipeline, and in enclaves reconcile them on the program's transfer cadence.

### AI-6.5: Model Deployment Risk Threshold Evaluation

**Design Intent:** The pipeline combines each model's results across jailbreak, injection, evasion, poisoning, out-of-distribution, and privacy tests into one score against its risk tier's thresholds. Retraining within the approved envelope passes on that score alone. Anything outside it goes to the PMO ISSE for a decision.

**NIST Control Mapping:**

- **RA-3 (partial):** claimed partial for the risk assessment of each candidate model version, split by subject from the Application focus area's release assessment. The base is cited because the enhancements cover other questions, and RA-3(1) sits with Model Selection and Justification.
- **RA-7 (partial):** claimed partial for the gate's automated block-or-promote response, while Risk Acceptance and Approval Log holds the decisions after a block. Operations and Continuous Monitoring's dashboard view cannot serve as the gate record, since it moves as new findings arrive.
- **Declined:** CA-6 is not claimed, for the reason recorded under Risk Acceptance and Approval Log.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Application/API, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-6.5.1: Model Release Risk Scoring Definition**
    - **Description:** Specify how the results of this focus area's robustness, jailbreak, injection, poisoning, out-of-distribution, and privacy-attack suites, the open red team findings, and the disclosed model card limitations are normalized and weighted into one score for a candidate model version, and record that scheme alongside the program's other documented gate criteria in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-3 (partial) mapping. Normalize unlike inputs, such as attacker advantage, retained accuracy, jailbreak rate, and open findings, before combining them. Set weights as a mission judgment following the robustness and privacy baselines, and score a not-applicable suite differently from a passed one. Revise the scheme when suites, mission, or AO expectations change.

- **AI-6.5.2: Automated Model Promotion Go/No-Go Gate Enforcement**
    - **Description:** Compute each candidate's score at the gate and block its promotion to the registry channel serving traffic whenever the score exceeds the documented threshold or any individually disqualifying condition is present, recording the score and its inputs with the model version.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-7 (partial) mapping. Add findings that block regardless of score, such as a successful injection with tool access, a recovered training record, a sub-threshold physical-process robustness result, or an unverifiable artifact. Record the score, inputs, and threshold at promotion, and block at the registry channel so a failed candidate is unreachable.

- **AI-6.5.3: Version-over-Version Robustness Regression Block**
    - **Description:** Compare each candidate's result on every applicable suite with the result of the version it would replace, and block promotion when any result regresses beyond the tolerance documented in the AISP, even where the candidate still meets the assurance level's thresholds.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity also carries the outcome's RA-7 (partial) mapping, as a second automated response beside the score gate. Use the first certified version's results as the baseline, with a tolerance that absorbs run-to-run noise. For a managed foundation model, compare whenever the prompt, guardrails, retrieval sources, tools, or model version change, and route an accepted regression through Risk Acceptance and Approval Log as the new baseline.

### AI-6.6: Rollback/Kill-Switch Readiness Check

**Design Intent:** Before certification, each model's rollback is rehearsed in stage, and so is its kill switch: cloud endpoints fall back to the prior certified version, and AI agents are disabled. For edge models, the rehearsal runs on a spare aircraft, which falls back to its stored prior model or turns onboard detection off. The cutover times are recorded in the evidence.

**NIST Control Mapping:**

- **CP-10(4) (partial):** the verifying half of the joint claim Rollback/Kill-Switch Mechanism holds from the building side, timing the restoration of the previous validated version from controlled artifacts. Application Rollback, Progressive Delivery, and Feature Flag Governance holds the application slice.
- **CP-12 (partial):** the verifying half of the same joint claim Rollback/Kill-Switch Mechanism holds, showing the defined safe mode is actually entered with the model removed from the inference path.
- **Declined:** CP-4 is not claimed, since it tests the program's contingency plan rather than one mechanism. SI-13 is not reopened, as the building outcome already declined it.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Application/API, Compute, Edge/Embedded AI Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-6.6.1: Rollback/Kill-Switch Mechanism Validation**
    - **Description:** Exercise the version cutover and the kill switch against the candidate's own serving configuration in a representative environment, timing the restoration and the safe-mode entry and confirming that the reverted configuration is the validated set rather than the weights alone.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-10(4) (partial) and CP-12 (partial) mappings. Revert the full dependency set, including feature transformation, prompt template, and input schema, not only the weights. Exercise the manual path and the reinstatement path out of safe mode as well as the automated switch.

- **AI-6.6.2: Rollback Readiness Sign-Off**
    - **Description:** Compare the measured cutover and safe-mode times against the program's committed recovery time, sign the result as a certification condition, and withhold promotion of the candidate when either exceeds it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Reject or accept through Risk Acceptance and Approval Log any candidate that misses the committed recovery time. Report against the committed time rather than the previous result, and record any representative-environment substitution in the sign-off.

### AI-6.7: Model Registration and Inventory Logging

**Design Intent:** Every certified model version is registered in the model registry and the asset inventory. Each record lists its owner, certification record, where it serves, and which aircraft carry it.

**NIST Control Mapping:**

- **CM-8 (partial):** claimed partial for the trained model version as an inventoried component, which neither host nor application inventories contain. Application Registration and Inventory Logging holds applications, and Asset Inventory and Discovery holds compute and storage.
- **CM-8(1) (partial):** claimed partial on the same split, since the certification gate writes the record and keeps it current.
- **Declined:** CM-8(2) and CM-8(3) stay with Trusted Model Registry Source Validation and Model Registry Hygiene Report, which detect drift. CM-8(4) is held full by Resource Tagging and Ownership Strategy, whose taxonomy the record uses.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Database Service

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-6.7.1: Model Registration in Authoritative Inventory**
    - **Description:** Write the certified model version into the program's authoritative inventory as a required condition of the gate passing, capturing its registry identifier and artifact digest, the training run and dataset versions behind it, the serving configuration it was certified with, and the environments it is approved for.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-8(1) (partial) mapping. Link training run and dataset versions from Dataset Lineage and Version Control and Experiment Tracking and Reproducibility, so an incident can find every model built on a contaminated corpus. Record the certified serving configuration beside the digest, since a different prompt or tool set is a different system.

- **AI-6.7.2: Model Inventory Record Enrichment**
    - **Description:** Attach to each model record its accountable owner, the mission criticality of the decisions it informs, the classification of both its training corpus and its inference inputs, and the vendor or publisher of the architecture or pretrained checkpoint it derives from, resolving each value to the taxonomy that already defines it rather than restating it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Record classification on two axes, the training corpus and the inference data, since one field loses a fact. Name the accountable model owner, not the platform team. Resolve the vendor value to the Approved AI Component Catalog entry, set criticality from documented mission dependency, and update all four on change rather than on a schedule.

### AI-6.8: Model Optimization Governance

**Design Intent:** Edge models are quantized or pruned versions of the cloud detection models. Each optimized artifact is certified as its own version and re-tested for accuracy and robustness, rather than inheriting the cloud model's certification. The approved optimization methods are listed in the AISP.

**NIST Control Mapping:**

- **SA-15 (partial):** claimed partial for the catalog of optimization techniques permitted on a certified model, beside Approved AI Component Catalog's slice. The material-change rule and the regression checks add no citation, since they route to existing suites such as Canary Prompt Testing.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Edge/Embedded AI Device, Artifact/Model Registry

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-6.8.1: Approved Optimization Technique Catalog**
    - **Description:** List each optimization technique the program permits, including quantization, pruning, and distillation, with its use cases, known trade-offs, quality-impact risks, and security implications, require ISSO and governance board approval before an unlisted technique is applied to any candidate, review the catalog at least annually to incorporate new techniques, updated security research, and red team findings, and document the catalog in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-15 (partial) mapping. Write trade-offs per technique and architecture, since quantization and pruning costs vary. Link the catalog from the model intake SOP, review it annually and on red-team or research triggers, and communicate changes through Role-Based Specialized Training.

- **AI-6.8.2: Optimization Material-Change Classification and Re-Certification**
    - **Description:** Classify every optimization event as a material model update producing a new candidate model version, and route that version back through AI Threat Modeling's re-review, Robustness Requirements Definition's re-derivation, and the full Certification to Field gate rather than substituting it directly into a serving deployment.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, since it states a routing rule. Treat an optimized artifact as a model change, so it passes the same gates as its predecessor instead of being swapped in as a deployment tweak.

- **AI-6.8.3: Optimization Security and Behavioral Regression Assessment**
    - **Description:** Re-run Adversarial Evasion Robustness Testing against the optimized weights before the optimized version may be promoted, re-run the certified Canary Prompt Testing suite to compare the optimized artifact's output against the pre-optimization baseline, and re-scan the artifact through Model Artifact Malware/Unsafe-Deserialization Scanning, blocking promotion on any regression and recording a bias evaluation as an available condition for the AI/ML Governance Review Board to attach.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, orchestrating Adversarial Evasion Robustness Testing, Canary Prompt Testing, and Model Artifact Malware/Unsafe-Deserialization Scanning. Compare against the pre-optimization baseline, not only absolute thresholds. Route unremediable regressions to Risk Acceptance and Approval Log.

- **AI-6.8.4: Optimization Event Registry Documentation**
    - **Description:** Record each optimization event against the model's registry entry with the technique applied, the date, the operator, the rationale, the evaluation and assessment results, and the approval record, retained for the lifecycle of the model and reviewable by the ISSO and the AI/ML Governance Review Board on demand.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, extending the record Model Registration and Inventory Logging writes. Record the evaluator, rationale, and approval with each optimization, so the history shows who decided as well as what changed.

## AI-7: Continuous Training

### AI-7.1: Automated Retraining Pipeline Security Assessments and Patching

**Design Intent:** The retraining pipeline's images, cluster, and platform components are scanned on the VPMP's schedule and patched like any other production pipeline, even when no model change is pending.

**NIST Control Mapping:**

- **RA-5 (partial):** claimed partial for the operating retraining pipeline's orchestrator, runner images, scheduler, and integrations, scanned on a schedule after the model is fielded. AI Dependency Vulnerability Scanning holds the training dependency set, and Retraining Pipeline Integrity Verification detects unauthorized definition changes.
- **SI-2(5) (partial):** claimed partial for automatically installing updates to those components, which Patching and Updates declined for its staged rollouts.
- **Declined:** SI-2, SI-2(2), and SI-2(3) are not reopened, since Patching and Updates and Vulnerability and Patch Management hold them jointly.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, CI/CD Pipeline, Self-Hosted Model, Fine-Tuned Model, Storage/Database

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-7.1.1: Scheduled Retraining Pipeline Vulnerability Assessment**
    - **Description:** Assess the retraining pipeline's orchestrator, runner images, scheduler, and registry, feature-store, and feedback-ingestion integrations against current vulnerability data on a defined schedule, and record each finding against the component that carries it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-5 (partial) mapping. The schedule is the control, since a retraining pipeline has no commit or build event to trigger a scan. Enumerate components the program did not author, such as a managed orchestrator, vendor feature store, or hosted registry.

- **AI-7.1.2: Automated Patching and Remediation Workflow**
    - **Description:** Roll the retraining pipeline's images and components forward through an automated rebuild-and-redeploy workflow that closes the findings this outcome produces without a manual release step, and escalate any finding the workflow cannot close inside the remediation service levels the VPMP sets.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-2(5) (partial) mapping. Automatic installation is acceptable here because a bad update fails a retraining cycle before anything is promoted. Route framework version bumps through Dependency Update/Patch Policy Enforcement, since they require revalidation, and take service levels from the VPMP.

### AI-7.2: Retraining Data Integrity Checks

**Design Intent:** Every retraining record is validated against its schema, value ranges, and label vocabulary before it joins a snapshot. Each submitter's correction rate is checked for floods. Federated updates are bounded in size and combined by a robust aggregation method, so one aircraft's update cannot dominate a round.

**NIST Control Mapping:**

- **SI-7(1) (partial):** claimed partial for screening an accumulated retraining set before a cycle admits it, the slice Data Poisoning Prevention and Detection reserved. That set is written continuously by users and must be compared with the deployed model's training distribution.
- **SI-10 (partial):** claimed partial for checking the validity of retraining records, beside Label Integrity Verification. SI-10(5) for the ingestion path sits with Continuous Authentication of Feedback/Retraining Data.
- **Declined:** SI-7(5) stays with Data Poisoning Prevention and Detection, whose quarantine runs when these screens fire. SI-4 is not claimed, since the set is inspected at rest.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Fine-Tuned Model, Object/File Storage, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-7.2.1: Retraining Dataset Content Validation**
    - **Description:** Validate every retraining record against the feature schema, value ranges, and label vocabulary the deployed model was trained on, and reject the records that fail rather than coercing them into the set.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-10 (partial) mapping. Reject rather than silently coerce invalid records, since clipping or defaulting teaches the model something nobody chose. Version the schema with the deployed model, so a retraining set spanning a model change does not mix vocabularies.

- **AI-7.2.2: Retraining Data Poisoning Detection**
    - **Description:** Screen the accumulated retraining set against the training distribution the deployed model was fitted on for distributional movement, clustered near-duplicate contributions, and label-conditional anomalies, and hold the flagged clusters out of the cycle for adjudication.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(1) (partial) mapping and runs at the close of each retraining window. It complements Feedback Volume/Rate-Based Skewing Attack Detection, since a thinly spread campaign can still move the distribution. Adjudicate with Operations and Continuous Monitoring's drift detection, because genuine drift gives the same signal.

### AI-7.3: Secure Model Evaluation Environment

**Design Intent:** Candidates are evaluated in a disposable environment in ML Dev/Test, which has no route to any prod spoke. The held-out evaluation data is readable only by the evaluation pipeline, so no one tuning a model can see it.

**NIST Control Mapping:**

- **SA-3(1) (partial):** claimed partial for the post-training evaluation environment, the last of the enhancement's environment classes. It loads a finished checkpoint and points it at the partition that decides promotion, unlike Ephemeral, Containerized Training Environments.
- **SC-39 (partial):** claimed partial for a separate execution focus area per evaluation job, cited at the base since no enhancement covers container isolation.
- **AC-6 (partial):** claimed partial for scoping the evaluation identity to the partitions it needs, beside Experimentation Data Access Scoping. Keeping the held-out partition out of training stops promotion metrics from measuring memorization.
- **Declined:** AC-3(11) is not reopened, since evaluation partitions are derived copies, not raw stores. SC-4 stays with Ephemeral, Containerized Training Environments, covering nodes from the same fleet.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Object/File Storage, Self-Hosted Model, Fine-Tuned Model, Identity Lifecycle and Governance

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-7.3.1: Isolated Evaluation Environment Provisioning**
    - **Description:** Provision a disposable, separately scheduled execution focus area for each evaluation job from an approved image, deny it any route to fielded systems or to the training data stores, and destroy it with its scratch storage when the job ends.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-3(1) (partial) and SC-39 (partial) mappings. Reuse the Ephemeral, Containerized Training Environments runner machinery with different egress and data scope rather than building a second platform. Adversarial evaluation most needs the boundary, since its purpose is making the candidate misbehave.

- **AI-7.3.2: Evaluation Data Access Scoping**
    - **Description:** Grant the evaluation environment access only to the held-out and adversarial evaluation partitions a promotion decision requires, withhold those same partitions from every training identity, and re-attest both halves of that separation on a defined cadence.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-6 (partial) mapping. Scope in both directions, withholding training stores from evaluation and evaluation partitions from training identities. Set an explicit rule assigning each cycle's newly labeled data to one partition, or the evaluation set drifts into training.

### AI-7.4: Continuous Authentication of Feedback/Retraining Data

**Design Intent:** Retraining signal is accepted only from authenticated sources. Analyst corrections are bound to the analyst's identity and the inference session they correct. Federated updates are authenticated by each aircraft's device identity. Products released from the IL6 enclave are treated as untrusted input, so they pass the same checks as everything else.

**NIST Control Mapping:**

- **SI-10(5) (partial):** claimed partial for restricting feedback ingestion to registered, authenticated submitters and approved formats, an input class that admits single records continuously from outside the program. Submitters include end users, application signals, partner systems, and logging pipelines, each bound to its record and inference session.
- **SI-4 (partial):** claimed partial for monitoring the live submission stream for volume and rate, since a skewing campaign can use only plausible records. No enhancement is cited, because SI-4(2), SI-4(5), and SI-4(13) are held elsewhere for other collection points.
- **Declined:** IA-8 is held full by External PKI Trust and Sponsorship, and IA-9 by the Identity focus area's service authentication outcomes. AU-10(1) stays with Dataset Lineage and Version Control, whose record carries the submitter field.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, Self-Hosted Model, Fine-Tuned Model, Storage/Database, Identity Platform

**External Dependencies:** The IL6 enclave's owner, whose release review approves every product returned high to low.

**Security Impact:** Moderate

**Activities:**

- **AI-7.4.1: Feedback Submitter Identity/Provenance Authentication**
    - **Description:** Register every person, system, and automated pipeline permitted to submit feedback or retraining data, authenticate each submission against that registration, and bind the resolved identity and the originating inference session to the record before it is written to the retraining store.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-10(5) (partial) mapping. Decide anonymous feedback explicitly, by authenticating it, routing it to human adjudication, or accepting the exposure in writing. Bind each correction to the inference it corrects. Where training is federated, register each client, and clip or reject outlying updates at aggregation, or record in the AISP that the program does not train federatedly.

- **AI-7.4.2: Feedback Volume/Rate-Based Skewing Attack Detection**
    - **Description:** Baseline the feedback channel's normal submission volume, rate, and per-submitter concentration, and alert on the bursts, sustained high-rate contributors, and coordinated cohorts whose share of a retraining window is large enough to move what the next cycle learns.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4 (partial) mapping. Alert on a submitter's or cohort's share of the retraining window rather than a fixed count. Depend on the sibling's authentication to correlate low-rate identities, and set a recorded cap on any one submitter's contribution per window.

## AI-8: Model Serving

### AI-8.1: Extraction Abuse Monitoring

**Design Intent:** Model endpoints in ML Prod accept calls only from approved mission team workloads, and each caller's query pattern is baselined. Systematic sweeps that look like extraction alert the ML team and the Security Team. The partner API's query volume per partner is watched the same way, since its detections reveal model behavior.

**NIST Control Mapping:**

- **SI-4 (partial):** claimed partial for monitoring live inference traffic for extraction behavior, the read path out of the current model. API Abuse Protection sets consumption ceilings, while this detector fires on callers inside every quota, and findings escalate to Production Abuse Monitoring.
- **SI-4(7) (partial):** claimed partial for the automated throttle or suspension a detection drives at the inference gateway, beside EDR Blocking/Enforcement Mode at the host.
- **Declined:** no SI-4 enhancement naming a collection point fits. SI-4(2) stays with Identity Platform Threat Detection and Hardening, since this signal exists only across a window.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, AI Interface/Inference Endpoint, Application and Service Account Identity

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-8.1.1: Query Pattern Anomaly Detection**
    - **Description:** Baseline each caller's normal query distribution and alert on the input-space coverage, synthetic or near-duplicate perturbation sequences, and decision-boundary probing that characterize an attempt to reconstruct the model from its responses.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4 (partial) mapping. Trim confidence and probability values to what the mission consumes before building the detector, since scored outputs make extraction far cheaper. It is Level 2 because detection is probabilistic and needs a baseline, while API Abuse Protection's quota is the mandatory bound.

- **AI-8.1.2: Rate-Based Extraction Abuse Alerting and Throttling**
    - **Description:** Set the query-budget and pattern-score thresholds at which a caller is throttled, degraded to reduced response detail, or suspended, and wire those thresholds to fire automatically on the detector's output rather than through an analyst's decision.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(7) (partial) mapping. Prefer graduated responses, such as reduced response detail, over a binary block, since false positives are legitimate heavy users. Pair detection with a cumulative per-principal query budget over the model's service life, because slow campaigns still complete under a rate limit.

### AI-8.2: API Abuse Protection

**Design Intent:** Every model endpoint enforces rate limits and quotas per calling workload, and every language model use case also enforces them per user. A runaway caller therefore cannot exhaust shared GPU capacity or the foundation model's quota.

**NIST Control Mapping:**

- **SC-5 (partial):** claimed partial for bounding what an authenticated caller may consume from an inference endpoint, enforced as a per-principal budget. DDoS Protection holds anonymous floods, and Web Application Firewall holds unauthenticated bot rate limiting.
- **Declined:** SC-5(2) and SC-5(3) stay with DDoS Protection. SI-4 belongs to Extraction Abuse Monitoring, since this ceiling needs no theory of intent. AC-3 and AC-6 are not claimed, because the Identity focus area sets the caller classes this quota consumes.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, AI Interface/Inference Endpoint, Compute, Application and Service Account Identity

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-8.2.1: API Rate Limiting and Quota Enforcement**
    - **Description:** Define the request-rate, concurrency, and total-consumption limits for each class of caller the serving endpoint recognizes, and enforce them at the gateway per authenticated principal rather than per source address.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the enforcement dimension of the outcome's SC-5 (partial) mapping. Count per authenticated principal, not per address, since shared gateways and NAT collapse many callers into one. Use token or compute cost as the unit for generative endpoints, and resize limits as caller classes and capacity change.

- **AI-8.2.2: Abusive Client Detection and Blocking**
    - **Description:** Identify the callers that repeatedly exhaust their quota, retry against enforcement, or rotate credentials and endpoints to evade it, and block them automatically at the gateway under a documented reinstatement path.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the persistent-abuser dimension of the outcome's SC-5 (partial) mapping. Correlate consumption to the owning organization so workloads spread across keys or regions are visible. Write down a reinstatement path, and treat the block list as an accountable configuration item.

### AI-8.3: Third-Party/Foundation Model API Dependency Governance

**Design Intent:** Each foundation model is a CSP-hosted deployment inside KESTREL's boundary, reached by private endpoint with provider-side prompt logging disabled. Prompts may carry report excerpts at IL5 but never raw collection. Each deployment pins its model version, and a version change or deprecation notice triggers re-testing before the use case moves to it.

**NIST Control Mapping:**

- **IA-5(6) (partial), IA-5(7) (partial):** claimed partial for vaulting the vendor API credential and keeping it out of code, images, and settings. Training Credential Secrets Management holds training credentials, while this key reaches an external endpoint and is also a spending instrument.
- **SA-9 (partial):** claimed partial for ongoing monitoring of the model vendor's control compliance for as long as the API is in the serving path. Contract Security Requirements holds the general provider population, and Model Selection and Justification holds the one-time selection.
- **SA-9(5) (partial):** claimed partial for restricting where the vendor processes and stores prompts, retrieved context, and completions. External Runtime Service and Client-Side Code Governance holds conventional external services.
- **SR-6 (partial):** claimed partial for the recurring supplier review, beside Model Selection and Justification's pre-adoption assessment. The base is cited because SR-6(1) tests delivered elements, and contractual flow-down stays with the Manage pillar.
- **Declined:** SA-9(2) is a provider disclosure at acquisition, and the network permission decision is the CM-7 claim Platform Service Network Integration holds. RA-3(1) stays with Model Selection and Justification.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Third-Party API Model, Foundation Model, Application and Service Account Identity

**External Dependencies:** The IL5 cloud provider, which hosts each foundation model deployment inside KESTREL's tenant under its provisional authorization. The model's publisher, whose versions and deprecations the provider passes on.

**Security Impact:** High

**Activities:**

- **AI-8.3.1: Third-Party Model API Data Governance**
    - **Description:** Determine which data classifications, personal information categories, and mission content may be transmitted to each vendor-hosted model API, record the residency, retention, deletion, and training-use terms the vendor is contractually held to for that content, and document the governance policy in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-9(5) (partial) mapping. Settle in writing first whether the vendor trains on submitted content. State permitted data classes against everything that leaves the boundary, including retrieved context. Enforcement sits with Inference-Time PII Handling, Output Validation, and the Data focus area's DLP, and the determination is recorded against the DMP's retention schedule.

- **AI-8.3.2: Vendor Model API Credential Management and Rotation**
    - **Description:** Retrieve every vendor model API key from the program's vault at request time, prohibit it from appearing in serving code, container images, or platform settings, and rotate it on a defined cadence and immediately on any suspected exposure.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(6) (partial) and IA-5(7) (partial) mappings, using the Identity and Data focus areas' vault and rotation machinery. Where vendors issue only long-lived account-wide keys, rely on rotation cadence and per-workload key separation, and treat spend alerts as a compromise detector.

- **AI-8.3.3: Vendor Security Posture Monitoring**
    - **Description:** Review each model API vendor's current SOC 2 or equivalent attestation, published subprocessor and architecture changes, and incident-notification commitments on a defined cadence, and record any lapse as a risk item against the dependency.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-9 (partial) and SR-6 (partial) mappings. Review an attestation's exceptions and scope, and confirm it covers the model-serving product actually used. Check notification timelines against observed behavior. It is Level 2 and rises to Level 1 wherever the tailored baseline includes SA-9 for an external service in the authorization boundary.

### AI-8.4: Retrieval-Augmented Generation (RAG) and Vector Store Security

**Design Intent:** The mission report index takes documents only from the shared report zone, each tagged with its source and release markings. Retrieval enforces the requesting user's entitlements, so a partner-restricted report never reaches a context it should not. Products released from the IL6 enclave are marked as untrusted content in the prompt.

**NIST Control Mapping:**

- **AC-3 (partial):** claimed partial for enforcing authorizations over retrieval corpora and the vector index. The base is cited since no enhancement fits read-restriction of a content class.
- **AC-16(3) (partial):** claimed partial for carrying a source document's access and classification attributes onto its embeddings. Attribute-Based Data and Application Access Enforcement (ABAC) supplies the schema and enforcement this outcome consumes.
- **SI-7(1) (partial):** claimed partial for screening indexed retrieval content, since a poisoned document takes effect at retrieval without touching the weights. Prompt Injection Testing tests delivery through retrieval, and Output Validation screens what the model emits.
- **Declined:** AC-3(11) stays with Training Data Privacy Controls for raw training stores. SI-10(5) is not reopened, since the source trust boundary is not a format check on an ingestion mechanism.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Retrieval-Augmented Generation (RAG), Vector Store/Embedding Index, Embedding Model, Application/API, Identity Lifecycle and Governance

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-8.4.1: Retrieval Corpus Access Control and Source Trust Boundary Definition**
    - **Description:** Enumerate the corpora and document sources the retrieval layer is permitted to draw from, classify each as trusted or untrusted according to who can write to it, and restrict read and write access to the corpora and their vector indexes to the populations that require them.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-3 (partial) mapping. Classify sources by who can write to them, so an internally editable wiki counts as untrusted. Mark untrusted content through to the prompt so the model and guardrails treat it as data. Reclassify as sources are added.

- **AI-8.4.2: Retrieval Corpus Poisoning Detection**
    - **Description:** Screen documents entering the retrieval index for embedded instruction text, invisible or encoded content, implausible authority claims, and near-duplicate chunks crafted to dominate retrieval for a target query, and hold the flagged content out of the index for adjudication.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(1) (partial) mapping. Retrieval poisoning needs only one well-ranked document, so screen at indexing. Rescreen documents when they change, and screen the extracted text the chunker produces, since styled-hidden content reaches the model.

- **AI-8.4.3: Source-Document-to-Embedding Access Control Preservation**
    - **Description:** Carry each source document's classification and access-control attributes onto the chunks and embeddings derived from it, and filter retrieval results against the requesting principal's entitlements before any chunk reaches the model's context.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-16(3) (partial) mapping. Filter before retrieval, since discarding a chunk after the model has seen it protects nothing. Re-index on access changes so revoked entitlements leave the index, and take attributes and policy from the Data focus area's ABAC outcome.

- **AI-8.4.4: Embedding Inversion Resistance Testing**
    - **Description:** Attempt to reconstruct source text and identify contributing documents from the stored embeddings using inversion and membership-inference techniques, and record the recoverable content as a disclosure exposure of the vector store against the program's classification requirements.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since no SP 800-53 control addresses whether embeddings disclose their source, and CA-8 is held by Penetration Testing. Use the result to confirm the vector store's classification, which is often set lower than its source documents. It is Level 3, run annually or on an embedding model change, and read with Privacy-Attack Testing.

### AI-8.5: Input Validation

**Design Intent:** Every inference request is validated against its endpoint's input schema, types, and size limits before it reaches a model. That covers image dimensions and formats for the detection models, and prompt length for language model use cases.

**NIST Control Mapping:**

- **SI-10 (partial):** claimed partial for structurally validating inference requests at the serving boundary against the deployed version's contract. Retraining Data Integrity Checks validates what the model learns, while this checks what it is asked, and Content Filtering judges meaning.
- **Declined:** SI-10(5) is not reopened, since its input-class slices are already allocated.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, AI Interface/Inference Endpoint, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-8.5.1: Input Schema/Type Validation**
    - **Description:** Validate every inference request against the input schema, feature types, tensor shapes, and value ranges the deployed model version declares, and reject requests that fail rather than padding, truncating, or coercing them into acceptance.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the outcome's SI-10 (partial) mapping. Reject rather than pad or coerce malformed requests, since a padded request yields a confident answer on unseen data. Bind the schema to the model version so a rollback reverts both.

- **AI-8.5.2: Adversarial Input Filtering**
    - **Description:** Reject inference payloads whose size, encoding, nesting depth, context length, or content type is outside the bounds the serving path is engineered for, and cap the per-request compute a single caller can demand.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-10 (partial) mapping. Bound context length, nesting, compression, and media type, and set an output-token ceiling per request, since aggregate quotas do not stop one stalling request. It does not address adversarial examples, which Adversarial Evasion Robustness Testing measures.

### AI-8.6: Output Validation

**Design Intent:** Detection outputs are checked against their schema before they are stored. Language model responses are rendered as plain text with source citations required, and responses that echo system prompts or credentials are blocked.

**NIST Control Mapping:**

- **SI-15 (partial):** claimed partial for validating that responses match their contract and carry nothing that must not leave. Content Filtering holds the policy judgment, and DLP patterns and labels come from the Data focus area's Data Loss Prevention (DLP) and Monitoring.
- **Declined:** SI-19 stays with Inference-Time PII Handling, which owns personal information on the request path. AU-13 and AU-13(1) stay with External Attack Surface Management's outside-in monitoring.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, AI Interface/Inference Endpoint, Storage/Database

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-8.6.1: Output Schema/Format Validation**
    - **Description:** Validate every model response against the declared output schema, type, range, and format contract before it is returned, and fail the request to a defined safe default rather than passing a nonconforming response to the calling system.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the outcome's SI-15 (partial) mapping. Validate structured generative output before any consumer renders or executes it. Record the safe default, whether refusal, null, or a deterministic fallback, with the model's interface contract.

- **AI-8.6.2: Sensitive-Data Leakage Output Scanning**
    - **Description:** Scan model responses before release for credentials and keys, internal hostnames and infrastructure detail, classification and handling markings, and verbatim passages from controlled corpora, and block or redact the response when a pattern matches.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-15 (partial) mapping, running on the Data focus area's DLP engine. Add model-specific patterns for echoed retrieved context, recited system prompts, and long verbatim spans. Use span-similarity against indexed corpora, since models can reproduce content without its markings, and tune against the mission's own outputs.

### AI-8.7: Agentic Tool-Call/Action Output Validation

**Design Intent:** Every AI agent tool call is checked against the tools and parameters its task authorized before it runs, and tools run in a sandboxed container. The mission-planning agent is the first: its tools only read mission data and write drafts to an operator's approval queue. Plans are also checked against approved areas and airspace.

**NIST Control Mapping:**

- **SI-15 (partial):** claimed partial for checking that a tool-call directive's action and parameters match the task's declared contract before dispatch, alongside Output Validation's text slice. SI-15 has no enhancements.
- **AC-4 (partial):** claimed partial for provenance-based flow control, so a directive traced to untrusted content cannot reach dispatch without escalation. Network Micro Segmentation and Data Loss Prevention (DLP) and Monitoring hold the position- and label-based slices.
- **AC-3(2) (partial):** claimed jointly with AI Agent Identities, whose High-Risk Action Human Approval Gate is the dual-authorization mechanism. This outcome adds the provenance trigger that routes untrusted-origin directives into that gate even for actions not on its high-risk list.
- **SC-39 (partial):** claimed partial for a separate execution focus area per dispatched tool call, the same base-level isolation Ephemeral, Containerized Training Environments applies to training jobs.
- **Declined:** AC-6 stays with Agent Tool/API Access Scoping, which decides tool classes. SI-10 belongs to Input Validation. SC-7(21) is not claimed, since SC-39 names per-call isolation more precisely. AC-4 is not reopened for sandbox egress, which the segmentation outcomes enforce. AU-12 stays with the Detection focus area's Application/API Logging.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, AI Agent, AI Agent Identity, Container

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-8.7.1: Tool-Call Schema and Parameter Validation Against Action Contract**
    - **Description:** Validate each tool-call or function-call directive's action identifier and parameters against the task's declared action contract before the directive is dispatched to the tool or API layer, block dispatch to a defined safe default on any directive that fails validation, and log and alert the ISSO on each blocked directive.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-15 (partial) mapping. Check the specific action and parameters of each call against the task contract, which Agent Tool/API Access Scoping's class-level check cannot see. Fail to a safe default recorded with the tool's contract, since a bad tool call executes. Alert the ISSO and write blocked directives to Agentic AI Tool-Call and Action Logging (Application/API Logging).

- **AI-8.7.2: Provenance-Gated Escalation to Human Approval**
    - **Description:** Trace each tool-call directive back to the retrieved, tool-returned, or otherwise untrusted content it originated from, and route any directive so traced into Identity's High-Risk Action Human Approval Gate (AI Agent Identities) for human confirmation regardless of whether the action appears on that gate's static high-risk action list.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-4 (partial) and AC-3(2) (partial) mappings. Escalate on provenance, because injected actions hide in routine lookups and writes. Trace through multi-step loops, treating re-ingested tool returns as untrusted, and read the trust marking Retrieval Corpus Access Control and Source Trust Boundary Definition applies. Hold a flagged directive until the gate decides.

- **AI-8.7.3: Sandboxed Tool-Call Execution Environment**
    - **Description:** Execute every tool call that clears the first two activities inside an isolated sandbox that restricts network egress to the destinations the call's action contract requires, confines the filesystem and mounted data to the scope that call needs, and bounds process and resource consumption, so that a manipulated or malicious call cannot escalate beyond the action it was dispatched to perform.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-39 (partial) mapping. Tear down and rebuild the sandbox for every call so no state carries forward. Define network egress and filesystem scope per tool class, since an unrestricted network is often the more damaging gap. This contains a call already approved by the validation activities and Agent Tool/API Access Scoping (AI Agent Identities).

### AI-8.8: Inference-Time PII Handling

**Design Intent:** Prompts and inference logs are scanned for personal information, which is redacted from the logs. Inference logs follow the retention schedule the privacy officer approved, and the foundation model's provider keeps nothing.

**NIST Control Mapping:**

- **SI-12(1) (partial):** claimed partial for limiting personal information retained in inference logs and telemetry to what the privacy assessment identified. Output Validation holds secrets and controlled content, and Model Registry Hygiene Report holds the SI-12 base.
- **SI-19 (partial), SI-19(4) (partial):** the third partial member of the joint claim with Privacy Requirements Definition, which decides, and Training Data Privacy Controls, which applies at training. This outcome applies the same techniques to inference inputs.
- **Declined:** SI-19(6) is not joined, since differential privacy is a training-time mechanism fully covered elsewhere. AC-3(11) stays with Training Data Privacy Controls.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, AI Interface/Inference Endpoint, Storage/Database

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-8.8.1: Input-Side PII Detection and Redaction**
    - **Description:** Detect the personal information categories the privacy baseline identified in each inference input and apply that baseline's assigned redaction or masking technique before the request reaches the model or any vendor-hosted API.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-19 (partial) and SI-19(4) (partial) mappings at inference time, paired with PII Detection and Redaction/Anonymization in Training Data. Redact before the request leaves the boundary, not only before logging. Record the free-text residual as accepted risk.

- **AI-8.8.2: Inference Log PII Minimization/Retention Controls**
    - **Description:** Limit the personal information written into inference logs, traces, and telemetry to the elements the privacy risk assessment identified as necessary, and enforce the DMP's retention and disposition schedule on those records automatically.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-12(1) (partial) mapping. Decide deliberately against the full-fidelity logging default. Set retention jointly with Continuous Training, whose feedback path consumes these logs, choosing redacted records, a shorter restricted schedule, or recorded exposure. Take retention periods from the DMP.

### AI-8.9: Content Filtering

**Design Intent:** Inputs and outputs of every language model use case are filtered against KESTREL's use policy. The filter also detects classification markings above what KESTREL may hold, so a possible spill is blocked and reported at once.

**NIST Control Mapping:**

- **SI-15 (partial):** claimed partial for filtering prohibited content categories on the output channel, a judgment about meaning beside Output Validation's contract check. The taxonomy, thresholds, and disposition are program decisions recorded with the use policy, since no SP 800-53 control covers them.
- **Declined:** SA-11 and CA-8 are not claimed for bypass testing, which validates this outcome's own filter rather than assessing the system.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, AI Interface/Inference Endpoint

**External Dependencies:** The IL5 cloud provider, which hosts each foundation model deployment inside KESTREL's tenant under its provisional authorization. The provider supplies the in-tenant content filters.

**Security Impact:** Moderate

**Activities:**

- **AI-8.9.1: Harmful/Policy-Violating Content Filtering**
    - **Description:** Define the harm and policy categories prohibited for this system's mission and user population, screen both inference inputs and model responses against them, and set the action on a match to block, redact, or flag with the escalation path each implies.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-15 (partial) mapping. Define a mission-specific taxonomy, since consumer moderation services block legitimate analysis and miss mission categories. Filter input as well as output so refused requests are recorded as misuse evidence. It is Level 2 and rises to Level 1 for any open or public-facing natural-language interface.

- **AI-8.9.2: Filter Bypass/Evasion Testing**
    - **Description:** Exercise the deployed filter against encoding, transliteration, role-play framing, multi-turn decomposition, and language-switching evasions on a defined cadence, and feed every successful bypass back into the filter's rules or classifier.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it tests its sibling's filter. Unlike Jailbreak Testing's pre-certification check, it confirms the runtime filter still holds. Run it quarterly and on any filter, model version, or prompt scaffolding change, with a versioned corpus.

### AI-8.10: System Prompt Governance

**Design Intent:** Every system prompt is kept in its use case's repository and versioned with the release. Changes are reviewed like code and deployed only through the pipeline. A change that alters a prompt's role or limits triggers re-testing against jailbreak and injection.

**NIST Control Mapping:**

- **CM-3 (partial):** claimed partial for review and approval of system prompts as their own asset class, beside Asset Lifecycle Change Control, with the Configuration Control Board overseeing. The pre-deployment gate reruns Jailbreak Testing and Prompt Injection Testing on the changed prompt.
- **CM-2(2) (partial):** claimed partial for keeping system prompts current in a version-controlled repository, an artifact class neither infrastructure nor training configuration covers.
- **CM-4 (partial):** claimed partial for analyzing what a prompt change grants, removes, or could disclose, alongside Change Risk Assessment's provisioned-asset slice. Security Impact Analysis (SIA) holds the system-level analysis this feeds.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Prompt/Instruction Layer, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-8.10.1: System Prompt Inventory and Version Control**
    - **Description:** Conduct discovery outreach to every application and ML team to identify each system prompt in production use, record it in the authoritative inventory as an extension of the model record the Artificial Intelligence focus area's Model Registration and Inventory Logging already maintains, store the prompt text in a version-controlled repository with full history and a defined rollback SLA, and flag any prompt discovered outside this inventory for immediate review.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-2(2) (partial) mapping. Extend the Model Registration and Inventory Logging record with a browsable catalog of author, purpose, and history, plus a sweep for prompts fielded outside the gate. Restrict write access through Non-Privileged Access Control.

- **AI-8.10.2: System Prompt Change Control Workflow**
    - **Description:** Route every proposed creation, modification, or retirement of a production system prompt through documented review and ISSO sign-off before it reaches production, recording the requestor, the rationale, and the approver against the version-controlled record, and define an expedited emergency path for urgent changes that substitutes mandatory retrospective review for prior approval.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-3 (partial) mapping, applying Change Approval Workflow's sequence to prompts with oversight from the Configuration Control Board. The emergency path mirrors Emergency Change Process, with justification at implementation and mandatory retrospective review.

- **AI-8.10.3: System Prompt Security Review and Injection Hardening**
    - **Description:** Review every new or modified system prompt for injection vulnerability patterns, unintended capability grants, and policy violations before it is approved, block a prompt that fails review from reaching production until the finding is resolved, and require injection hardening, namely explicit instruction boundaries, context separation directives, and role-anchoring language resistant to redefinition, on every prompt whose deployment tier calls for it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-4 (partial) mapping, analyzing what a change could grant or expose and requiring hardening where findings are structural. Prompt hardening is one layer and does not replace Content Filtering or Prompt Injection Testing.

- **AI-8.10.4: System Prompt Pre-Deployment Testing and Periodic Audit**
    - **Description:** Require functional correctness testing, output policy compliance checks, and, for a material change, a re-run of the Validation and Continuous Delivery capability's adversarial suites scoped to the modified prompt before deployment, then audit at least annually and after any significant model or policy change for version-control currency, review status, hardening compliance, test currency, and acceptable-use-policy alignment, and report findings to the ISSO and the AI/ML Governance Review Board.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the audit and test-before-finalizing dimension of the outcome's CM-3 (partial) mapping. Re-run Jailbreak Testing and Prompt Injection Testing against the modified prompt. Route audit findings to the AI/ML Governance Review Board so cross-team patterns surface.

### AI-8.11: Model Artifact Encryption and Watermarking

**Design Intent:** Every model artifact is encrypted at rest under program keys, in the registry, on serving nodes, and on aircraft. Edge models carry a watermark, so a copy recovered from a lost aircraft can be traced to its version and tail number.

**NIST Control Mapping:**

- **SC-28(1) (partial):** claimed partial for the model artifact wherever it comes to rest, including serving caches, edge devices, and transfer media beyond the storage tier. Default Data at Rest Encryption holds the storage-service baseline.
- **Declined:** the SC-28 base is not reopened. Watermarking has no citation, since no SP 800-53 control covers marking an artifact for later attribution, and SR-4 concerns what arrives from a supply chain. The gap is recorded.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Artifact/Model Registry, Object/File Storage, Compute, Edge/Embedded AI Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-8.11.1: Model Artifact Encryption at Rest**
    - **Description:** Require every model artifact to be encrypted at rest under the program's key management arrangements in the registry, in object storage, in each serving node's local cache, and on any device it is delivered to, and verify that requirement wherever an artifact is stored outside the platform's default-encrypted services.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-28(1) (partial) mapping, extending Default Data at Rest Encryption past the storage tier. Inventory where each version physically exists, especially serving-node caches. Prefer customer-managed keys for this artifact class, decided through Encryption Key Ownership and Control.

- **AI-8.11.2: Model Watermarking for Provenance/Theft Attribution**
    - **Description:** Embed a recoverable, per-recipient mark in released model artifacts using weight-space or output-space watermarking, and maintain the extraction procedure and the release register needed to attribute a recovered copy to the recipient it was issued to.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no control citation. It is Level 3, worth building when a model goes to a partner, subcontractor, or uncontrolled device. Keep a release register beside the model registry, and test mark durability against fine-tuning, quantization, distillation, and paraphrase.

### AI-8.12: On-Device Extraction Resistance

**Design Intent:** Onboard models run in the aircraft's trusted execution environment, stored encrypted with keys held in its crypto module. They are zeroized if the aircraft detects tampering or is declared lost. An aircraft that might be captured therefore yields neither usable weights nor keys.

**NIST Control Mapping:**

- **SC-39(1) (partial):** claimed partial for running inference in a hardware-isolated enclave, the hardware separation earlier SC-39 claimants named. Confidential Computing and Column Level Encryption holds the cloud slice.
- **Declined:** the SC-39 base is not reopened. SC-28(1) stays with Model Artifact Encryption and Watermarking, while this outcome keeps decryption and execution inside the enclave.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Edge/Embedded AI Device, Compute, Self-Hosted Model

**External Dependencies:** The aircraft manufacturer, which supplies the onboard trusted execution environment and crypto module.

**Security Impact:** High

**Activities:**

- **AI-8.12.1: Secure Enclave/TEE Deployment for on-Device Inference**
    - **Description:** Deploy the on-device inference runtime inside the platform's trusted execution environment or secure enclave, seal the model artifact to that hardware so it decrypts only inside it, and attest the enclave's measurement before the weights are released to it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Extensive
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-39(1) (partial) mapping. Treat it as a platform decision, since limited enclave accelerator access may force a smaller or quantized model. Seal the artifact to the hardware and verify attestation before trusting the runtime. It is Level 2, required only on genuinely uncontrolled hardware, and revisited when hardware changes.

- **AI-8.12.2: Model Weight Extraction Resistance Validation**
    - **Description:** Attempt to recover the model weights from a representative fielded device through its storage, memory, debug and JTAG interfaces, and the timing and power side channels its hardware exposes, and record what proved recoverable as residual risk against the deployment decision.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent citation, since it tests its sibling's mechanism. Report what extraction cost and what fraction of the model it yielded. Where the enclave is a vendor's, cite the vendor's evaluation with its scope. Run annually and on hardware or model format changes.

### AI-8.13: Offline/Air-Gapped Model Integrity Verification

**Design Intent:** Every model leaving the cloud for a disconnected destination travels as a signed offline package. Destinations include the ground control stations and the IL6 enclave. Each package carries its weights, digest, AI-BOM, and certification record, and it is verified at the station before loading and at the transfer gateway before staging.

**NIST Control Mapping:**

- **SI-7(6) (partial):** claimed partial for cryptographically detecting changes to the offline model package between assembly and load. Artifact Bundle Integrity Verification holds release bundles, while a model package must also match weights, tokenizer, and configuration to each other.
- **Declined:** CM-14 and SI-7(15) are not reopened, since Training Artifact Signing and the other signing outcomes hold them and this package carries their signatures. Media transport belongs to Media Protection Policy and Procedures.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Object/File Storage, Compute, Edge/Embedded AI Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-8.13.1: Offline Model Package Signing**
    - **Description:** Assemble each model destined for a disconnected environment into a single package containing the weights, configuration, tokenizer and preprocessing assets, and version metadata, generate a digest manifest over the whole set, and sign that manifest at the point the package is built.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(6) (partial) mapping, using Training Artifact Signing's signing identity to sign the package rather than the weights. Produce the manifest at build time and ship it signed. Transfer public keys and revocation state through the approved import process, never inside the package they authenticate.

- **AI-8.13.2: Air-Gapped Integrity Verification at Load Time**
    - **Description:** Verify the offline package's signature and every manifest digest against the public key pinned during the approved import before the serving stack loads any member, and refuse the load rather than warning when verification fails or the pinned key is absent.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(6) (partial) mapping. Refuse on failure, verify at every load, and set the pinned key's rotation and re-pinning schedule at import so expiry does not cause an outage. Make key pinning a reviewed decision, since verification cannot show the package was correct when signed.

### AI-8.14: Rollback/Kill-Switch Mechanism

**Design Intent:** Each model endpoint can cut back to its previous certified version in minutes. Each AI agent and each language model use case has a kill switch the owning team and the Security Team can operate. Each aircraft keeps its prior certified edge model, and the operator can turn onboard detection off.

**NIST Control Mapping:**

- **CP-10(4) (partial):** claimed partial for restoring the serving path to a prior validated version from signed registry artifacts within a defined time. Rollback/Kill-Switch Readiness Check exercises it.
- **CP-12 (partial):** claimed partial for the safe mode the kill switch enters with the model removed from the path. It has no enhancements.
- **Declined:** the CP-10 base belongs to the Operate pillar's recovery focus area. CP-10(2) and CP-10(6) describe mechanisms not implemented here. SI-13 addresses component failure prediction, not a cutover or emergency stop.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, Self-Hosted Model, Compute, Edge/Embedded AI Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-8.14.1: Model Version Rollback Capability**
    - **Description:** Maintain the previously validated model version in a loadable, integrity-protected state alongside the current one, provide a single operator action that cuts serving traffic back to it within the program's stated recovery time without rerunning the deployment pipeline, and refuse any rollback target the registry has since withdrawn.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-10(4) (partial) mapping. Keep the prior version warm through blue-green or canary serving, and roll back the whole serving configuration, including feature transformation, prompt template, and input schema. Set the recovery time from mission consequence. Limit rollback targets to versions still certified in Model Registration and Inventory Logging, so a retired version cannot be reloaded.

- **AI-8.14.2: Kill-Switch Trigger Integration**
    - **Description:** Implement a kill switch that removes the model from the inference path and places the serving endpoint in its defined safe mode, and wire both an automated invocation path from the monitoring conditions the program specifies and a manual path an accountable operator can exercise without engineering assistance.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-12 (partial) mapping. Define the safe mode as a mission decision, such as refusal, a deterministic fallback, or handoff to a human. Exercise both the manual and automated paths, drawing triggers from drift alerting and canary prompt testing, and document reinstatement out of safe mode.

## AI-9: Operations and Continuous Monitoring

### AI-9.1: Model Drift Detection and Alerting

**Design Intent:** Each fielded model's output distribution and confidence are tracked, along with its accuracy against analyst corrections as they return. Drift past the model card's limits alerts the ML team and the owning mission team.

**NIST Control Mapping:**

- **SI-4 (partial):** claimed partial for monitoring a fielded model's own output behavior against its certified baseline, whoever asked. Extraction Abuse Monitoring watches caller intent on the read path.
- **CA-7 (partial):** claimed partial for monitoring program-defined model metrics and reporting their status, a subject slice beside Unified Vulnerability Dashboard. The Manage pillar's Continuous Monitoring Plan (ConMon) holds the strategy and frequencies.
- **Declined:** no SI-4 enhancement fits. SI-4(2) is per-event analysis held by Identity Platform Threat Detection and Hardening, SI-4(5) and SI-4(13) belong to OT/Legacy Passive Monitoring, and SI-4(12) belongs to Production Abuse Monitoring's security alert path. CA-7(3), CA-7(4), and CA-7(6) are held for other purposes or are the Manage pillar's evidence question.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-9.1.1: Model Performance/Output Drift Monitoring**
    - **Description:** Compute the fielded model's output distribution, prediction confidence profile, and, where ground truth returns, its measured accuracy over a rolling window, and compare each against the reference values recorded with the certified model version.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4 (partial) mapping. Do not rely on accuracy alone, since ground truth often arrives weeks late. Use output class balance, confidence distribution, and rejection rate for timely signal. Read reference values from certification artifacts rather than recent production data, and measure per segment.

- **AI-9.1.2: Drift Threshold Alerting and Retraining Trigger**
    - **Description:** Set the drift magnitude and persistence at which the monitor alerts the model owner and opens a retraining cycle, wire the threshold to fire on the monitor's output rather than on a review meeting, and record those thresholds alongside the program's other documented gate criteria.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the alerting dimension of the outcome's SI-4 (partial) mapping. Include persistence as well as magnitude in thresholds. A triggered retraining candidate re-enters Certification to Field like any other. Escalate drift that coincides with an abuse or poisoning finding as a security event, and record that routing in advance.

- **AI-9.1.3: Model Health/Performance Dashboard**
    - **Description:** Present drift trend over time, the retraining triggers that fired and what each produced, and the registry and certification status of every fielded model version in one view scoped to the model owners, the PMO ISSE, and the AO.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-7 (partial) mapping. Build one view across the capability, including registry, source-validation, and Data Drift Detection and Alerting status. Key the view to model version so a trend never spans a retraining boundary, and scope access. It is Level 2 because detection and response are the floor.

### AI-9.2: Data Drift Detection and Alerting

**Design Intent:** Each model's production inputs are compared with its training distribution, such as new terrain, season, sensor state, or emitter types. Drift alerts the ML team before accuracy visibly drops.

**NIST Control Mapping:**

- **SI-4 (partial):** claimed partial for monitoring the production input distribution over a window, while Model Drift Detection and Alerting measures outputs. Shifted inputs with plausible outputs signal a model answering questions it was never validated for.
- **Declined:** CA-7 is not extended, since findings surface through the sibling's dashboard. SI-10 stays with Input Validation, because every input here is individually valid and the property belongs to the stream.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Application/API, Storage/Database

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-9.2.1: Input Data Distribution Drift Monitoring**
    - **Description:** Measure the divergence between the production inference input distribution over a rolling window and the training and validation distributions recorded with the certified model version, per feature for structured inputs and in embedding space for text, imagery, and other unstructured inputs.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4 (partial) mapping. Version and store the reference distribution with the model. Retain distributional summaries rather than raw inputs, consistent with Inference-Time PII Handling. Declare expected seasonality in advance.

- **AI-9.2.2: Drift Threshold Alerting and Investigation Workflow**
    - **Description:** Set the divergence threshold at which an input drift finding is raised, route each finding to an adjudicator able to distinguish an environment change from a deliberate manipulation, and record the disposition against the model version it concerns.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the alerting dimension of the outcome's SI-4 (partial) mapping. Separate three dispositions, namely a genuine shift needing retraining, an upstream pipeline or sensor fault, and input manipulation that is an incident. Never clear a finding by recomputing the reference from recent data. Where feedback retrains the model, adjudicate jointly with Continuous Training's feedback monitoring.

### AI-9.3: Retraining Pipeline Integrity Verification

**Design Intent:** The fielded retraining pipeline's definition, schedule, data sources, and identities are compared each week with the certified versions. A difference stops retraining until it is explained.

**NIST Control Mapping:**

- **SI-7(1) (partial):** claimed partial for recurring integrity checks of the retraining pipeline's configuration against its version of record. Automated Retraining Pipeline Security Assessments and Patching covers known flaws in the components instead.
- **CM-6(2) (partial):** claimed partial for the alert and suspension of the next cycle, beside Hyperparameter Change Alerting's run-configuration response.
- **Declined:** CM-14 and SA-10 stay with Signed/Verified Training Pipeline Definitions, while this outcome compares the whole fielded configuration, including schedule, triggers, and bindings. CM-3(1) and CM-3(4) stay with Privileged Config Change Alerting for the control plane.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Self-Hosted Model, Fine-Tuned Model, CI/CD Pipeline, Artifact/Model Registry

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-9.3.1: Retraining Pipeline Configuration Integrity Check**
    - **Description:** Compare the fielded retraining pipeline's definition, schedule, trigger conditions, data-source and feature-store bindings, and promotion targets against the signed version of record at the start of every cycle and on a fixed cadence between cycles.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(1) (partial) mapping. Enumerate the full surface, including schedule, trigger predicate, resolved data source, and registry channel held in platform state. Check between cycles, and resolve bindings rather than names, so a repointed reference is caught.

- **AI-9.3.2: Unauthorized Retraining Pipeline Change Detection**
    - **Description:** Alert on every difference the integrity check reports that no approved change request accounts for, name the identity and interface that produced it, and suspend the next retraining cycle until the difference has been dispositioned.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-6(2) (partial) mapping. Suspend the next cycle rather than halting a running one. Record the interface a change arrived through alongside the identity, and read alert volume as a measure of how often the reviewed path is bypassed.

### AI-9.4: Production Abuse Monitoring

**Design Intent:** Extraction alerts, quota hits, content filter blocks, and rejected inputs from every model endpoint and use case are combined in the security monitoring platform. The Security Team and the CSSP can see a campaign across them.

**NIST Control Mapping:**

- **SI-4(12) (partial):** claimed partial for alerting the security organization when correlated serving-layer activity meets escalation criteria. SIEM Capabilities holds the program-wide slice.
- **SI-4(16) (partial):** claimed partial for correlating serving-layer monitoring output, while Correlated Threat Detection and Analytics holds correlation across the rest of the estate.
- **Declined:** no SI-4 base is claimed, since this outcome monitors nothing itself, as Unified Vulnerability Dashboard reasoned for RA-5. SI-4(7) stays with Extraction Abuse Monitoring. AU-6 and AU-6(3) are the Operate pillar's SIEM territory. IR-4, IR-5, and IR-6 belong to the Response focus area, which handles what this outcome hands over.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, AI Interface/Inference Endpoint, Application and Service Account Identity

**External Dependencies:** The CSSP, which watches the combined view through its host pool.

**Security Impact:** Moderate

**Activities:**

- **AI-9.4.1: Production Query/Usage Pattern Abuse Monitoring**
    - **Description:** Ingest the findings the serving layer's extraction detector, quota enforcement, content filter, and input validation emit into one store keyed to the calling principal, and correlate them into the aggregate abuse patterns that no single detector's threshold reaches.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(16) (partial) mapping. Key correlation to the principal and up to the owning organization, since a caller just under every threshold shows up only in one combined row. Ingest each detector's verdict without re-scoring it.

- **AI-9.4.2: Abuse Finding Escalation and Response Workflow**
    - **Description:** Define the aggregate patterns and severities that escalate to the security organization, alert on them from the correlation store, and hand each escalated finding to the program's incident process with the serving-layer evidence attached.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(12) (partial) mapping. Write escalation criteria in advance and record them with the program's thresholds. Hand over the evidence with the alert, including query history, filter hits, and quota events. The response belongs to the Operate pillar, so this activity ends at the handoff.

### AI-9.5: Canary Prompt Testing

**Design Intent:** A versioned set of canary inputs runs daily against every fielded model and use case, with known answers expected. These include images for the detection models and prompts for the language model use cases. A changed answer alerts the owning team, which catches a silent model or prompt change.

**NIST Control Mapping:**

- **SI-6 (partial):** claimed partial for periodically verifying that the serving path's guardrail and behavioral functions still work, with alert and rollback on failure. Coverage is the model serving portion only, with the rest of the estate recorded as a gap.
- **Declined:** SI-6(2) addresses distributed testing across systems, and SI-6(3) adds less than the base's alert element. SI-4 rests on real traffic. CA-8 and SA-11 belong to the Application focus area and pre-deployment validation. CP-10(4) and CP-12 are invoked, not rebuilt, from Rollback/Kill-Switch Mechanism.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI Interface/Inference Endpoint, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-9.5.1: Canary Prompt Suite Execution Against Production Model**
    - **Description:** Execute a versioned suite of fixed canary inputs with recorded expected behavior against the production serving endpoint on a defined cadence, sending them through the same path a real caller takes, and record each response against its expectation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-6 (partial) mapping. Send canaries through the production request path so the prompt, retrieval, filters, and routing are tested. Include known-answer, must-refuse, and marker inputs. Tag canary traffic out of drift monitors and retraining, and restrict access to the suite.

- **AI-9.5.2: Canary Test Failure Alerting and Rollback Trigger**
    - **Description:** Define which canary failures raise an alert and which trip the rollback or kill switch, and wire those conditions directly to the mechanism Model Serving built rather than to a notification somebody has to answer.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the alert-and-respond element of the outcome's SI-6 (partial) mapping. Trigger on repeated failure and write expectations as behavioral properties. Send a failed refusal canary to rollback and a slipping functional canary to retraining. Make sure the kill switch can be invoked from an automated trigger.

### AI-9.6: Trusted Model Registry Source Validation

**Design Intent:** Every serving platform's loaded models are resolved to their registry and digest each day and compared with the model registry. A model loaded from anywhere else alerts the Security Team.

**NIST Control Mapping:**

- **SR-4 (partial):** claimed partial for monitoring that the model a serving platform actually loaded still has its recorded provenance. Trusted Registry ConMon Report holds the container image slice.
- **CM-8(3) (partial):** claimed partial for detecting a model loaded from an unapproved source, the half Model Registration and Inventory Logging reserved. Host and application inventories cannot see it.
- **Declined:** CM-8(2) belongs to Model Registry Hygiene Report, and CM-8 and CM-8(1) to the certification gate. CM-14 is not claimed, since a validly signed public checkpoint is still this outcome's finding, and signature checks belong to Training Artifact Signing.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Artifact/Model Registry, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-9.6.1: Model Registry Source Validation**
    - **Description:** Resolve the registry host and artifact digest behind every model version a serving platform has loaded against the program's list of approved model registries on an ongoing basis, and record each result against the deployment it describes.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4 (partial) mapping. Resolve by digest, not by name or version label. Check what the process actually loaded rather than the manifest. Record explicit decisions for mirrors, caches, and vendor endpoints, and confirm any admission control on model source is on in every namespace.

- **AI-9.6.2: Non-Trusted Model Source Usage Detection and Alerting**
    - **Description:** Alert the security organization whenever a loaded model resolves to a source outside the approved list or to no recorded source at all, identifying the artifact digest, the serving host or namespace, and the identity that deployed it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-8(3) (partial) mapping. Treat an unresolvable source as an unknown artifact in production. Use the deploying identity to tell a broken promotion path from a person's action, route alerts to the security organization, and decide repeat suppressions in the approved list.

### AI-9.7: Model Registry Hygiene Report

**Design Intent:** Model versions with no deployment, rollback role, open evaluation, or IL6 baseline expire on the AISP's schedule. A monthly report shows what the registry holds against those rules.

**NIST Control Mapping:**

- **CM-8(2) (partial):** claimed partial for keeping the model inventory current by detecting versions nothing references, the half Model Registration and Inventory Logging reserved. Trusted Model Registry Source Validation holds CM-8(3).
- **CM-2(3) (partial), SI-12 (partial):** claimed partial as the model-artifact counterparts of Registry Hygiene Report's build-artifact slices. CM-2(3) keeps a defined rollback depth, and SI-12 manages registry retention and removal.
- **Declined:** SI-12(3) and MP-6 are not cited, since sanitization is the Data focus area's subject and removal here is ordinary deletion.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Model, Artifact/Model Registry

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **AI-9.7.1: Stale/Orphaned Model Version Detection and Cleanup**
    - **Description:** Identify the model versions that no serving deployment, rollback target, or open evaluation references and that have passed the retention window, and delete them on a scheduled basis together with the signatures, AI-BOMs, and evaluation artifacts bound to them.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-8(2) (partial) mapping and the disposal half of its SI-12 (partial) mapping. Compute reachability from what serving platforms report loaded. Mark lineage records for a removed version rather than dropping them, and remove the version with its signature, AI-BOM, evaluation report, and model card as a set.

- **AI-9.7.2: Model Registry Retention Policy Compliance Reporting**
    - **Description:** Report model registry contents against the program's documented retention rules, showing which model families exceed their window, which have fallen below the minimum rollback depth, and what was removed in the period.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-2(3) (partial) mapping. Set minimum rollback depth from the certification gate's rollback and kill-switch expectations. Set retention per model family, and report removals alongside remaining contents so a deleted dependency is visible.

### AI-9.8: Model Decommissioning and Disposal

**Design Intent:** Retiring a model deletes its weights and the embeddings derived from it, revokes its endpoint identities, and removes it from every aircraft. Its record is kept for as long as its certification evidence must be. The AISP sets the disposal method for each asset type.

**NIST Control Mapping:**

- **SR-12 (partial):** claimed partial for disposing of a whole retired model, inventorying every asset class, and verifying closure. Hardware and Firmware Provenance Verification holds physical components. For vendor-hosted models, this means contractual notice and retained deletion confirmation.
- **Declined:** SI-12(3) and MP-6 stay with Media Sanitization and Destruction Procedures, which this outcome invokes. Model Registry Hygiene Report handles scheduled cleanup, while this outcome runs on a deliberate decommission decision.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, Vector Store/Embedding Index, Artifact/Model Registry

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AI-9.8.1: Model Disposal Policy and Vendor Coordination Requirements**
    - **Description:** Define, by the classification it carries, the disposal or destruction method required for each asset class a fielded model accumulates, including weights, training data, embeddings, inference logs, cryptographic keys, and SBOM records, then define the contractual notification, deletion confirmation, and evidence-retention requirements the program holds its providers to for a vendor-hosted or third-party API model, and document the policy in the AISP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the disposal-decision element of the outcome's SR-12 (partial) mapping. Mirror Media Sanitization and Destruction Procedures' method-by-classification structure. Write deletion confirmation and evidence retention into vendor agreements through Contract Security Requirements.

- **AI-9.8.2: Per-Model Disposal Asset Inventory**
    - **Description:** Maintain, as a field on each model's record in the authoritative inventory, the specific weights, dataset versions, embedding stores, credentials, log locations, and SBOM references a decommission event for that model would have to reach, and review the field at the model's annual registry review.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, since the CM-8 (partial) inventory obligation stays with Model Registration and Inventory Logging, whose record it extends with a disposal asset list. Review the list annually so it is complete before a decommission event.

- **AI-9.8.3: Model Decommissioning Execution and Verified Completion Record**
    - **Description:** Execute the disposal inventory against the program's sanitization, key-destruction, and resource-teardown mechanisms for a self-hosted model, or obtain and retain the vendor's deletion confirmation for a vendor-hosted model, verify by storage scan and key-management review that no asset the inventory named survives, and produce a completion record signed by the model owner and the ISSO that updates the registry entry to a decommissioned status.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the verification and closure element of the outcome's SR-12 (partial) mapping. Invoke Media Sanitization and Destruction Procedures, Resource Decommissioning Governance, Key Lifecycle Automation, and Secrets and Credentials Protection against the assets Per-Model Disposal Asset Inventory named. Verify by scan, and sign the completion record, which Model Registry Hygiene Report then reads.

### AI-9.9: Operational Adversarial Re-Testing

**Design Intent:** Each fielded model and use case is re-tested against current jailbreak, injection, and evasion techniques each quarter. It is also re-tested when the cloud provider changes a foundation model underneath it. Results go to the PMO ISSE, and a failure reopens certification.

**NIST Control Mapping:**

- **CA-7 (partial):** claimed partial for continuing measurement of a fielded model's adversarial resistance against its certified thresholds. The Manage pillar's Continuous Monitoring Plan (ConMon) records this cadence among its frequencies.
- **RA-5 (partial):** claimed partial for the fielded model's susceptibility to published attack techniques, re-run when suites gain new techniques. AI Dependency Vulnerability Scanning holds training dependencies.
- **Declined:** SA-11 is pre-certification developer testing. SI-6 stays with Canary Prompt Testing's known-answer checks. CA-8 is not claimed, since these suites are automated. RA-5(2) stays with Endpoint Detection.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI Interface/Inference Endpoint, AI/ML System, Application/API

**External Dependencies:** The IL5 cloud provider, which hosts each foundation model deployment inside KESTREL's tenant under its provisional authorization.

**Security Impact:** Moderate

**Activities:**

- **AI-9.9.1: Scheduled Adversarial Suite Re-Execution Against Fielded Models**
    - **Description:** Re-run each fielded model's applicable jailbreak, prompt injection, adversarial evasion, and out-of-distribution suites on the cadence the AISP sets for its assurance level, against the production endpoint or a production-equivalent instance, and record each result against the model's certified thresholds.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-7 (partial) mapping. Use a quarterly floor for lower assurance levels and monthly for higher, recorded in each AI Cyber T&E Plan. Use a production-equivalent instance with the same version, prompt, guardrails, retrieval, and tools where live scanning would affect operations. Tag scan traffic, skip poisoning tests here, and append results as dated addenda to the validation report.

- **AI-9.9.2: Out-of-Cycle Re-Testing on Provider Model Change or Suite Update**
    - **Description:** Detect when a provider changes the foundation model behind a fielded use case or when a suite gains newly published techniques, re-run the applicable suites immediately rather than at the next scheduled cycle, and submit a provider model change to the Governance focus area's Security Impact Analysis (SIA).
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-5 (partial) mapping. Detect provider model changes from the API version identifier, provider notices reviewed by Vendor Security Posture Monitoring, and canary failures. Decide by assurance level in advance whether use continues during re-test, and re-run when suites gain new techniques.

- **AI-9.9.3: Operational Threshold Breach Re-Assessment**
    - **Description:** Route any operational result below its minimum acceptable threshold into a formal re-assessment, decide with the ISSM under the AISP's shortfall rules whether the use case continues under compensating controls in the meantime, and notify the AO for the higher assurance levels.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the response element of the outcome's CA-7 (partial) mapping. Dispose of a breach by remediation, compensating controls, or acceptance through Risk Acceptance and Approval Log, deciding continued operation before root cause is known. A breach meeting Ongoing Authorization's reauthorization criteria is also a security impact analysis input.

## AI-10: AI/ML Security Planning

### AI-10.1: AI/ML Security Plan (AISP)

**Design Intent:** The ML team authors KESTREL's AISP, with each mission team writing the sections for its use cases. The PMO ISSE writes the T&E methodology, since it runs Certification to Field and AI Cyber T&E. The AI/ML Governance Review Board reviews the AISP, and the Configuration Control Board approves it. It is revised each year and whenever a threshold, the component catalog, or a foundation model changes.

**NIST Control Mapping:**

- **SA-15 (partial):** claimed partial for the periodic-review clause, reviewing the whole AI/ML development process, standards, and tools as one package on a fixed cadence. Other outcomes such as Approved AI Component Catalog hold individual determinations, and the Application Security Plan (ASP) holds the conventional-software review.
- **Declined:** CM-9 belongs to the Configuration Management Plan (CMP), and PL-2 to the System Security Plan (SSP). SA-3 is not reopened, since AI Use Case Intake and Onboarding and the later capabilities hold its dimensions.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AI-10.1.1: AISP Development and Authoring**
    - **Description:** Author the AI/ML Security Plan, consolidating the ML-specific threat taxonomy, robustness testing scope, approved-component and approved-optimization criteria, misuse/abuse scenarios, training-infrastructure hardening baseline, certification risk-scoring model, and disposal policy produced across the focus area's capabilities into a single governing document.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent NIST Control Mapping claim, since the SA-15 (partial) claim rests on AISP Periodic Review and Revision. Author the AISP once the determinations it consolidates exist, such as AI-Specific Threat Taxonomy Adoption, Approved AI Component Catalog, Misconfiguration Policy Baseline and Gating, and Model Release Risk Scoring Definition.

- **AI-10.1.2: AISP Review and Approval**
    - **Description:** Route the drafted AISP through stakeholder review and secure formal approval from the accountable authority before it takes effect.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent NIST Control Mapping claim beyond the outcome's. Fix distribution and modification rights at approval, since the AISP gathers approved-component criteria, robustness thresholds, and disposal policy in one place.

- **AI-10.1.3: AISP Periodic Review and Revision**
    - **Description:** Review the AISP on a defined cadence and revise it to reflect changes in the program's ML threat landscape, approved-component and approved-optimization criteria, robustness testing scope, or governing requirements.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-15 (partial) periodic-review claim. Review the consolidated plan as one package on a fixed cadence, and revise it as the determinations it consolidates change.
