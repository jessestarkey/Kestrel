# AP: Application

*KESTREL SADD, Section 5 (Protect). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## AP-1: Planning, Requirements, and Design

### AP-1.1: Capability Gap Identification and Planning

**Design Intent:** The PMO ISSE measures each team's application security practice against this SADD's Application outcomes and records the gaps in the Security Implementation Plan. Each gap gets an owning team and a target date, and the gap list is reviewed at every Certification to Field threshold review.

**NIST Control Mapping:**

- **SA-2 (partial):** claimed partial for the resource determination and the discrete application security line item in the budget submission. Security Requirements Definition holds the high-level requirements determination, and SA-2 has no enhancements to cite instead.
- **SA-3 (partial):** claimed partial for the planning and resourcing stage of the secure development lifecycle, while the Application focus area's later capabilities carry the other stages. SA-3's enhancements cover preproduction environments, live data, and technology refresh, which this outcome does not perform.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-1.1.1: Current-State Security Capability Assessment**
    - **Description:** Inventory the application security tooling, processes, and skills the program has in place today, and record the assessed state of each against the target capability the tailored Application focus area defines.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Assess what actually operates rather than what is procured or documented. A purchased scanner nobody runs looks present on paper but absent to an attacker.

- **AP-1.1.2: Gap Analysis Against Control/Requirement Baseline**
    - **Description:** Compare the assessed current state against the AO-tailored control set and the Application focus area's tailored leaf outcomes, and record each shortfall as a discrete, owned entry in the gap register.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Keep each gap discrete and separately owned. An entry reading "application security is immature" cannot be sequenced, costed, or closed, while an entry naming one missing capability can.

- **AP-1.1.3: Capability Roadmap and Prioritization**
    - **Description:** Rank the gap register by security impact and dependency order, and sequence the entries into a dated roadmap showing when each capability is expected to be in place.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Dependency order constrains the ranking as much as impact does. For example, finding triage is worthless before any scanner runs, and build-gate thresholds are worthless before a pipeline exists. This roadmap feeds the Security Implementation Plan's sequencing rather than competing with it.

- **AP-1.1.4: Resourcing and Budget Planning for Gap Closure**
    - **Description:** Determine the staffing, tooling, and licensing each roadmap item requires, and establish a discrete application security line item in the program's budget submission to fund it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the resource determination and budget line item dimensions of the outcome's SA-2 (partial) mapping. It is Level 1 because the control requires a discrete security line item rather than funding absorbed into general engineering. The annual cadence follows the budget cycle, so the roadmap has to be current before the submission window.

### AP-1.2: Application Intake and Onboarding

**Design Intent:** Every new application, service, or COTS product enters KESTREL through one intake request in the service desk, before design or purchase. The request names the owning team, its product owner, the data it handles, and the payload vendor terms it falls under. It also names the spoke it will run in. Intake opens the threat model and the significant change review, and nothing deploys without a completed intake record.

**NIST Control Mapping:**

- **SA-3 (partial):** claimed partial for the project-initiation stage of the secure development lifecycle, tracked jointly with Capability Gap Identification and Planning and the focus area's other stages. The base control is cited for the same reason given there.
- **Declined:** RA-2 and RA-3 are not claimed, because a self-reported, unverified intake answer is neither a categorization nor a risk assessment. Those stay with Security Categorization and Deployment Risk Threshold Evaluation.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Self-Hosted Third-Party Application (COTS)

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-1.2.1: Intake Request Submission and Initial Project Registration**
    - **Description:** Establish a single submission path for proposing a new application, a major addition to an existing one, or the deployment of a self-hosted third-party or COTS product, record as a provisional project record the application's purpose, whether the program builds it or acquires and deploys it as a vendor product, the named application owner and program sponsor accountable for its security, and the expected delivery timeline, and document the intake form's required fields in the ASP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the roles-and-responsibilities dimension of the outcome's SA-3 (partial) mapping, since naming an owner and sponsor fills the security roles for a specific project. A single path is the point, because a program with several informal entry points cannot know a project started. Recording build versus COTS deployment lets Routing and Handoff to Downstream Security Work pick the right path.

- **AP-1.2.2: Self-Reported Data Sensitivity, Exposure, and Regulatory Scope Questionnaire**
    - **Description:** Have the requesting team answer a short, fixed questionnaire on the kinds of data the application will handle, the networks and user populations it will be reachable from, and any regulatory or contractual scope it falls under, attach the answers to the intake record as self-reported, unverified input, and document the questionnaire's fixed content in the ASP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** RA-2 and RA-3 are not claimed, since a team's unverified expectation is neither a categorization nor a risk assessment. Mark the answers unverified so an early guess is not later read as an authoritative classification. This activity is Level 2 because the mandatory floor, a reviewed threat model at the design gate, holds whatever a team reported.

- **AP-1.2.3: Intake Review and Onboarding Approval**
    - **Description:** Review each submitted request with the PMO ISSE, confirm that the ownership and reported scope are complete and plausible enough to plan against, and record an approval, rejection, or request for more information as the decision that admits the project into the secure development lifecycle.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the risk-management-integration dimension of the outcome's SA-3 (partial) mapping. Review turnaround decides whether teams use the front door, since a decision that takes weeks gets routed around. Approval admits a project into the lifecycle and is not an authorization decision, which remains the AO's.

- **AP-1.2.4: Routing and Handoff to Downstream Security Work**
    - **Description:** On approval, have the intake tooling open linked, tracked items for the project's downstream security work and assign them to the named owner with the intake record and questionnaire answers as their input, routing a program-built application to Security Requirements Definition and Application Threat Modeling and routing a self-hosted third-party or COTS deployment instead to Governance's Vendor Security Risk Assessment, Application Threat Modeling's COTS/Third-Party Integration Boundary Threat Modeling, and Secure Application Baselines and Vulnerability and Patch Management.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no control claim of its own. It is Level 1 because a handoff that does not fire leaves the mandatory downstream outcomes attached to nothing, and it is tagged Automate for tool-driven creation of the linked items. COTS deployments route to Vendor Security Risk Assessment, COTS/Third-Party Integration Boundary Threat Modeling, and the configuration baselines rather than to requirements definition.

### AP-1.3: Security Requirements Definition

**Design Intent:** The PMO ISSE turns the CCSD's control set into application security requirements, such as authentication through the identity provider, team-scoped authorization, and audit events. Each requirement enters every team's backlog as an acceptance criterion with a test that proves it. Product owners do not accept a story until its security requirements pass.

**NIST Control Mapping:**

- **SA-2 (partial):** claimed partial for the high-level application security requirements determination, tracked jointly with the budget determination Capability Gap Identification and Planning holds.
- **SA-4 (partial):** claimed partial for the functional, strength, and assurance requirements that acquisition language later carries. Flowdown to performers belongs to the Manage pillar, and the base control is cited because SA-4's enhancements govern developer deliverables.
- **SA-8 (partial):** claimed partial for the engineering principles applied in deriving requirements, citing the base control because each enhancement names one specific principle.
- **SA-17 (partial):** claimed partial for the allocation of controls to application components. The developer's design specification is a performer deliverable measured against this baseline.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Human Authentication, Database Service, Object/File Storage

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-1.3.1: Control-to-Requirement Traceability Mapping**
    - **Description:** Trace each control in the AO-tailored baseline that an application implements to one or more numbered application requirements, and maintain the mapping so that a control with no requirement standing behind it is visible.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This mapping runs controls to numbered requirements for engineers, at a finer grain than the introduction's outcome-level mapping. It records design intent and is not the Security Controls Traceability Matrix. Changes to the tailored baseline or the application's control allocation trigger it.

- **AP-1.3.2: Non-Functional Security Requirements Definition**
    - **Description:** Specify the authentication, authorization, session management, input validation, output encoding, logging, and cryptographic behavior the application must exhibit, in terms concrete enough that a test case can be written directly from each requirement, and document the resulting requirements in the ASP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Testability is the acceptance criterion, so name the algorithm, key length, key source, and data classes rather than "encrypt data at rest." Derive the set from OWASP ASVS at the selected verification level and write it to consume the program's identity, cryptographic, and logging services. Logging requirements point at Web Application Activities Logging rather than inventing an event list per application.

- **AP-1.3.3: Requirements Validation Against Threat Model**
    - **Description:** Check the drafted requirement set against the threats and design weaknesses Application Threat Modeling produced, and add or revise requirements wherever a modeled threat has no requirement that mitigates it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity consumes Application Threat Modeling's accepted findings and turns them into requirement changes. It catches what a control-derived set misses, namely what an adversary would actually attempt against this design. It re-runs whenever a threat model is revised.

- **AP-1.3.4: Security Requirements Sign-Off and Baseline**
    - **Description:** Route the completed requirement set through PMO ISSE and stakeholder review, secure the accountable authority's approval, and place the approved set under version control as the baseline that subsequent design work is measured against.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Baselining matters more than the signature, since an unbaselined set silently loses requirements under schedule pressure. Once baselined, each change is tracked with an approver, so an assessor can confirm no control was quietly dropped.

### AP-1.4: Application Threat Modeling

**Design Intent:** Each team threat-models every application and AI use case it owns before building, using one program methodology. Rigor scales with the data handled and the exposure, so anything partner-facing, internet-reachable, or able to act on aircraft gets the full model. The PMO ISSE reviews each model at the design gate, and the models live in the program's threat model repository.

**NIST Control Mapping:**

- **SA-11(2) (partial):** held for the threat modeling dimension for conventional software, tracked jointly with Threat Model Staleness Check and AI Threat Modeling, while API Security Testing holds the vulnerability analysis dimension. COTS/Third-Party Integration Boundary Threat Modeling extends it to the assembled solution, not the vendor's internal design.
- **SA-15 (partial):** claimed for the documented methodology and completeness standard, and for how rigorously it applies per project through Risk-Based Threat Modeling Scoping and Triage. Other outcomes hold the rest of this base control by subject.
- **SA-15(2) (partial):** claimed for the modeling tooling and the tracked path from accepted finding to owned backlog item.
- **SA-15(8) (partial):** claimed for the obligation to reuse prior models, carried by the methodology standard and the model repository, leaving reuse in other focus areas to their own outcomes.
- **Declined:** SA-15(4) is withdrawn in Rev 5 and incorporated into SA-11(2), so the threat modeling claim sits there rather than in the SA-15 family.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Self-Hosted Third-Party Application (COTS)

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-1.4.1: Threat Modeling Methodology Standardization**
    - **Description:** Select one threat modeling methodology such as STRIDE or PASTA, define how it is applied and what a completed model must contain, require teams to start from the program's library of prior models rather than a blank page, and document the resulting methodology in the ASP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries both the SA-15 (partial) mapping and the SA-15(8) (partial) mapping. Choosing one methodology and applying it consistently matters more than which one, since models built differently cannot be compared. The completeness standard keeps the gate from being passed by a diagram with no analysis behind it.

- **AP-1.4.2: Threat Modeling Tool Selection and Deployment**
    - **Description:** Evaluate and deploy the threat modeling tooling that supports the chosen methodology, including a model repository that stores completed models as versioned, machine-readable artifacts in source control alongside the architecture documentation they describe, and make the tooling reachable from every environment in which design work is performed.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The model repository has the lasting consequence, since it enables reuse and portfolio-wide coverage views. Store models as versioned, structured artifacts so Architecture-Change-to-Threat-Model Diffing can diff against them. This is Level 2 because a documented template can meet the mandatory obligation, while tooling makes it scale.

- **AP-1.4.3: Risk-Based Threat Modeling Scoping and Triage**
    - **Description:** Assess each new application's data classification, external exposure, and regulatory scope at project initiation, and use that assessment to scale the required threat-modeling rigor and route the project to the appropriate review checkpoint.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-15 (partial) mapping for how rigorously the process applies to a project. Triage sizes the review, choosing between a champion-facilitated session and a security-engineering deep dive. It never lowers the floor, since every new application and trust-boundary change still needs a reviewed model.

- **AP-1.4.4: Threat Model Creation at Design-Review Gate**
    - **Description:** Make a completed, reviewed threat model a condition of passing the design review gate for every new application and for every change to an existing application's trust boundaries, authentication paths, or data flows.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the threat modeling half of the outcome's SA-11(2) (partial) mapping and is where the practice becomes non-optional. The gate is a human design review, so it carries no Automate tag. Scoping the trigger to trust boundary, authentication, and data flow changes keeps it proportionate.

- **AP-1.4.5: COTS/Third-Party Integration Boundary Threat Modeling**
    - **Description:** Model the trust boundaries, data flows, and failure modes of the connections the program builds around a self-hosted third-party or COTS deployment routed here by Application Intake and Onboarding, covering identity federation, first-party API calls into the product, data exchanged with program-owned stores, and its network path, while treating the product's own internal design as an opaque boundary this activity does not reason about.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(2) (partial) mapping for the assembled solution, not the vendor's internal design. Intake routing triggers it, since a COTS deployment has no design review to condition. It is Level 2 because Vendor Security Risk Assessment and Secure Application Baselines hold the mandatory floor, and it is the only activity here reaching Self-Hosted Third-Party Application (COTS).

- **AP-1.4.6: Automated/AI-Assisted Threat Model Generation**
    - **Description:** Generate draft threat models automatically from the program's architecture diagrams, data flow definitions, and design documents, and route each draft to a human reviewer for correction and acceptance before it is treated as the design's model.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** A generated draft saves blank-page effort but is never the reviewed model the gate requires, and it does not satisfy SA-11(2) on its own. Output quality is bounded by the architecture artifacts it reads. An air-gapped program needs an accredited in-enclave model, or this activity is deferred.

- **AP-1.4.7: Threat-Model-Finding-to-Backlog Conversion**
    - **Description:** Convert every accepted threat model finding into a tracked backlog item carrying an owner, a severity, and a remediation target date, rather than leaving it recorded only inside the model.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the tracking dimension of the outcome's SA-15(2) (partial) mapping. An unconverted finding is no better than one nobody found. Findings that change what the application must do also route through Requirements Validation Against Threat Model.

- **AP-1.4.8: Security Champion Program for Threat Modeling**
    - **Description:** Train and designate a security champion on each development team to facilitate threat modeling sessions and perform first-pass model review, escalating to security engineering only the cases the champion is not equipped to judge.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Recurring cost is High because each development team gives up a standing fraction of an engineer every year. Champions make the design-review gate survivable at scale. Their authority stops at new trust boundaries, new external interfaces, or the most sensitive data, which stay with security engineering, and training comes from the Manage pillar's program.

## AP-2: Development and Continuous Integration

### AP-2.1: IDE Security Tools

**Design Intent:** The performer agreement requires security plugins in the development environments its developers use for KESTREL work. The plugins flag vulnerable patterns and secrets as code is written. They are an aid to the developer, while the pipeline's scans remain the authoritative check.

**NIST Control Mapping:**

- **SA-11(1) (partial):** claimed partial for editor-resident analysis, with SAST holding the pipeline half that produces retained results. Editor findings are advisory, since a dismissible analysis cannot carry an assessment obligation.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code

**External Dependencies:** The performer, which under the interconnection agreement equips the laptops its developers use for KESTREL work.

**Security Impact:** Moderate

**Activities:**

- **AP-2.1.1: IDE Plugin/Tool Selection and Rollout**
    - **Description:** Evaluate the security plugins available for the program's supported development environments, select the set that covers the languages and frameworks actually in use, and distribute them through the managed workstation configuration developers already receive.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Distribute through managed configuration rather than self-installation, so coverage is measurable. Language and framework coverage outweighs every other selection criterion.

- **AP-2.1.2: AI-Powered Code Security Assistant Deployment**
    - **Description:** Deploy the AI-assisted code security assistant into the developer's editor so that vulnerable patterns are flagged inline as code is typed and a candidate remediation is offered with each flag.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** A suggested fix is a draft the developer stays accountable for. An assistant backed by a vendor-hosted model cannot reach an air-gapped enclave without an accredited in-enclave deployment. It is Level 3 because SAST meets the mandatory static analysis obligation.

- **AP-2.1.3: Developer Real-Time Finding Triage Workflow**
    - **Description:** Define how a developer confirms, fixes, or dismisses an inline finding, and require that every dismissal be recorded with a stated reason rather than silently cleared from the editor.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Recorded dismissals improve the ruleset, since a rule everyone dismisses belongs in SAST's tuning baseline. The workflow stops at disposition, because a significant finding resurfaces in the gated pipeline scan.

### AP-2.2: Secure Coding Standards and Build Hardening

**Design Intent:** The ASP's coding standard names the approved languages and frameworks, prefers memory-safe languages for new services, and lists the functions and patterns developers may not use. Every build applies the standard's compiler and packaging hardening settings, and the pipeline fails a build that drops them.

**NIST Control Mapping:**

- **SA-15 (partial):** claimed for the coding standards and the tool options and configurations the build must use, including the compiler and linker settings. It is one subject slice of a base control the framework divides by what is standardized, with Application Threat Modeling holding the modeling methodology and all slices tracked jointly.
- **SI-16 (partial):** claimed for the production side of memory protection, since a binary compiled without hardening flags cannot be protected by a host setting. Host Hardening and Integrity Protection holds the enforcement side, and SI-16 has no enhancements.
- **SI-11 (full):** carried by Error Handling and Message Disclosure, which shows users only what they need and reserves operational detail for authorized personnel.
- **Declined:** SA-4(3) governs acquisition contracts, which belong to the Manage pillar's Contract Security Requirements. SA-8 stays with Security Requirements Definition. SA-15(5) addresses exposed interfaces rather than permitted language constructs.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Third-Party Dependency (Embedded Library/Package)

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.2.1: Secure Coding Standard Definition**
    - **Description:** Publish the program's secure coding standard covering the approved languages and frameworks, the functions, interfaces, and language constructs developers are prohibited from calling, and the required patterns for the flaw classes the program's stack produces, revise it against what the scanning outcomes actually report, and document the standard in the ASP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the standards dimension of the outcome's SA-15 (partial) mapping. Select the subset of an industry guide that fits the program's languages and state each item concretely enough to judge compliance. Drive the annual review from recurring findings, since a flaw class repeating across teams is a missing standard entry.

- **AP-2.2.2: Approved Component and Paved-Road Template Catalog**
    - **Description:** Maintain the vetted library set and preconfigured project templates carrying the program's authentication, cryptography, input validation, and logging defaults already wired in, publish them as the starting point every new service is scaffolded from, and document the catalog in the ASP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the tools dimension of the outcome's SA-15 (partial) mapping. It is tagged Automate because scaffolding from a template replaces hand-built security plumbing. Review quarterly, since a stale entry passes vulnerabilities to every team that adopted it, and point cryptography at the program's approved algorithms rather than restating them.

- **AP-2.2.3: Compiler and Linker Hardening Flag Enforcement**
    - **Description:** Require the exploit-mitigation compiler and linker settings on every build that produces native code, covering stack protectors, fortified source functions, full relocation read-only, position-independent executables, and the platform's control-flow integrity instrumentation, and fail the build when a produced binary does not carry them.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-16 (partial) mapping and the tool-configuration dimension of its SA-15 (partial) mapping. Verify the produced binary rather than the build script, since vendored subprojects, release paths, and toolchain upgrades routinely drop settings. Record a target that cannot accept a setting as a deviation under Hardening Exception and Waiver Tracking discipline.

- **AP-2.2.4: Error Handling and Message Disclosure**
    - **Description:** Add error handling rules to the secure coding standard that return generic messages to users, log the diagnostic detail operators need where only authorized personnel can read it, and verify the rules in code review and testing.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-11 (full) mapping. Design out stack traces, query fragments, internal hostnames, and user-enumeration differences. Send the detail to logs under Application/API Logging instead of discarding it.

### AP-2.3: SAST

**Design Intent:** SAST runs on every merge request and every merge in the shared pipeline, with rules tuned to each team's languages and frameworks. A finding at or above the ASP's threshold blocks the merge, and every exception the PMO ISSE approves is recorded against the finding.

**NIST Control Mapping:**

- **SA-11(1) (partial):** claimed as the pipeline half of the split with IDE Security Tools, which holds the editor half. This outcome produces the reproducible, retained results the enhancement depends on.
- **SA-15(7) (partial):** claimed for the automated analysis of the program's own source at the point a flaw is introduced. The exploitation-potential judgment is shared with Rule/Ruleset Tuning and False-Positive Baseline, and the claim is not extended to later-stage scanners, which analyze what development produced.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.3.1: SAST Tool Integration Into CI Pipeline**
    - **Description:** Wire the static analysis scanner into the CI workflow so that it runs automatically against every commit and merge request, publishing its findings to the pipeline result the developer already reads.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(1) and SA-15(7) (partial) mappings. Publish findings into the pipeline result rather than a separate console, so developers see them without logging into another tool.

- **AP-2.3.2: Rule/Ruleset Tuning and False-Positive Baseline**
    - **Description:** Tune the scanner's ruleset to the program's languages, frameworks, and coding patterns, and record each confirmed false positive in a reviewed baseline so that it is suppressed with justification rather than ignored by habit.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Treat the suppression baseline like a waiver, since a suppression added to unblock a release can hide a real finding permanently. It is not tagged Automate because adjudicating false positives is human judgment. Review quarterly and whenever the scanner's rule content updates.

- **AP-2.3.3: Build-Gate Threshold Enforcement**
    - **Description:** Set the finding severity and count at which the pipeline fails the build rather than warning, and enforce that threshold automatically so a build carrying findings above it cannot produce a promotable artifact.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The threshold is a documented risk decision the PMO ISSE owns, recorded with the program's other gate criteria. Expect to tighten it over time. It is tagged Automate because the gate blocks the build without a human deciding each time.

### AP-2.4: Secret Scanning

**Design Intent:** Source code lives on performer laptops, so secret scanning runs at all four points. Pre-commit hooks run on the laptops, push protection runs at the repository, the pipeline scans every build, and scheduled scans cover full history. A secret found in history is rotated first and removed second.

**NIST Control Mapping:**

- **IA-5(7) (partial):** claimed for prevention at source, stopping unencrypted authenticators from entering the codebase and removing those already there. It joins the Identity focus area's jointly tracked group, where Secrets and Credentials Detection holds the continuous safety net while this outcome gates commits and builds.
- **Declined:** SA-11(1) is not re-claimed, because SAST owns static code analysis and this outcome's obligation is the authenticator requirement.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, CI/CD Pipeline

**External Dependencies:** The performer, which under the interconnection agreement equips the laptops its developers use for KESTREL work. Its developers run the pre-commit hooks.

**Security Impact:** Moderate

**Activities:**

- **AP-2.4.1: Secret Scanning Tool Integration Into CI Pipeline**
    - **Description:** Integrate the secret scanner into the CI workflow so that every commit and merge request is inspected for credentials, keys, tokens, and connection strings before the change can be merged.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(7) (partial) mapping where it is enforceable, since the pipeline can refuse a merge. Cover the program's own credential formats, not only vendor-recognized ones.

- **AP-2.4.2: Historical Repository Scan and Remediation**
    - **Description:** Sweep the full commit history of every program repository for secrets committed before scanning was in place, and drive each confirmed exposure to rotation and revocation rather than to deletion from history alone.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Rotation through the Identity focus area's secrets machinery is the actual remediation, since clones, forks, and backups still hold a rewritten secret. Re-run the sweep for newly onboarded repositories, force pushes, and new detector pattern releases. Effort comes from tracing and rotating each secret, not from the scan.

- **AP-2.4.3: Pre-Commit Hook Enforcement**
    - **Description:** Distribute and configure pre-commit hooks that scan staged changes on the developer's workstation and refuse the commit when a credential pattern matches, so the most common exposures never reach the server.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** A pre-commit hook is a convenience rather than a boundary, since developers can bypass it, so this activity is Level 2. Its value is preventing exposure and the rotation that follows. Server-Side Push Protection is the enforceable form.

- **AP-2.4.4: Server-Side Push Protection**
    - **Description:** Enable pre-receive scanning on the source platform so that a push carrying a matched credential pattern is rejected outright, returning the offending commit and path to the developer rather than accepting the objects and reporting on them afterward.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(7) (partial) mapping at the only point where prevention and enforcement coincide. Rejecting the push removes the rotation obligation entirely. Restrict overrides to named approvers, record each with its justification, and treat it as a disclosure unless adjudicated a false positive.

### AP-2.5: Container Scanning

**Design Intent:** Every image the pipeline builds is scanned before it is pushed to the registry, and the registry rescans stored images as new vulnerability data arrives. Images above the ASP's severity threshold cannot be pushed or deployed.

**NIST Control Mapping:**

- **RA-5 (partial):** claimed for the pre-deployment container image scanning surface, alongside Endpoint Detection's Vulnerability Scanning for live hosts. The base control is cited because RA-5's enhancements address cadence, breadth, privileged access, and trends rather than this surface.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Container, Third-Party Dependency (Embedded Library/Package), CI/CD Pipeline, Artifact/Model Registry

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.5.1: Container Image Vulnerability Scanning Integration**
    - **Description:** Integrate the container image scanner into the build so that every image and every layer it inherits is analyzed against current vulnerability data as part of producing the image, not as a separate step afterward.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-5 (partial) mapping. Scan inherited layers, not only the application layer, since most vulnerable surface comes from the base image Base Image Lineage Report tracks.

- **AP-2.5.2: Scan-Gate Threshold Enforcement**
    - **Description:** Define the vulnerability severity and count at which an image is refused, and enforce that threshold automatically so a failing image neither completes its build nor reaches the trusted registry.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Blocking the push to the trusted registry matters more than failing the build, since deployment draws from the registry. Disposition an unfixable vulnerability through the Exception and Risk Acceptance Workflow rather than lowering the threshold. That acceptance is an RA-7 risk decision, not a hardening waiver.

### AP-2.6: Malware Scanning

**Design Intent:** The package mirror scans every package and base image it fetches, and the pipeline scans every build artifact before release. Vendor deliveries, such as payload vendor software and fleet firmware, are scanned at intake before anyone installs them.

**NIST Control Mapping:**

- **SI-3 (partial):** claimed as the build-time slice of malicious code protection, alongside the runtime slices Malicious Code Protection holds. It scans artifacts and fetched packages before anything executes them, and the base control is cited because no enhancement fits better.
- **SI-3(10) (partial):** carried by Quarantine and Alerting Workflow, which preserves the sample for analysis and routes the alert to incident handling. It is partial because the analysis happens in the incident process.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Third-Party Dependency (Embedded Library/Package), CI/CD Pipeline, Artifact/Model Registry, Object/File Storage

**External Dependencies:** The aircraft, ground equipment, and payload vendors, whose deliveries are scanned at intake.

**Security Impact:** Moderate

**Activities:**

- **AP-2.6.1: Artifact/Dependency Malware Scanning Integration**
    - **Description:** Suppress dependency install-script execution on the build runner, hold newly published package versions behind a proxy-side quarantine for a defined cooldown, and behind those controls integrate anti-malware scanning of build artifacts and fetched dependencies so every artifact is scanned before publication and every dependency before it is cached for reuse.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-3 (partial) mapping. The preventive controls are install-script suppression, such as npm ci --ignore-scripts, and the quarantine window Trusted Internal Package Repository owns, since a malicious hook runs before any scan fires. Signature and behavioral scanning sits on top as detection.

- **AP-2.6.2: Quarantine and Alerting Workflow**
    - **Description:** Move any artifact or package flagged as malicious into an isolated quarantine location, fail the build that produced or consumed it and refuse its push to the trusted registry, and alert the security organization with the artifact, its source, and the build that pulled it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the response dimension of the outcome's SI-3 (partial) mapping and its SI-3(10) (partial) mapping. Block the registry push as well as the build. Quarantine rather than delete, and route the alert to the Operate pillar's incident handling, since a malicious dependency is an incident rather than a failed test.

### AP-2.7: Trusted Internal Package Repository

**Design Intent:** The package mirror in Platform Prod is the only source builds resolve from, and the hub blocks every other route to public package indexes. Each ecosystem's proxy draws only from its approved upstream indexes. KESTREL's internal package names are reserved in the mirror, so a public package with the same name cannot replace one.

**NIST Control Mapping:**

- **SR-3 (partial):** claimed for the controlled path through which language-ecosystem components enter the program. It is tracked jointly with Dependency Review and Vendor SBOM Intake, which decide whether a component is admissible rather than where it comes from.
- **SR-4(3) (partial):** claimed for validating fetched packages against the publisher's digest or signature before caching. It is tracked jointly with Build Provenance and Attestation (SLSA) and Model Provenance and Integrity Verification, split by artifact class.
- **Declined:** SR-11 stays with Hardware and Firmware Provenance Verification, since this outcome is an ingress control, and its SR-11(3) gap is not closed here. CM-7(5) belongs to Execution and Device Control, which governs execution rather than package sources.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Third-Party Dependency (Embedded Library/Package), Artifact/Model Registry, CI/CD Pipeline

**External Dependencies:** The public package indexes and image sources the mirror draws from.

**Security Impact:** High

**Activities:**

- **AP-2.7.1: Internal Package Proxy Deployment and Upstream Scoping**
    - **Description:** Deploy the internal package proxy for every language ecosystem the program builds in, configure the build environments to resolve exclusively through it, and record the explicit list of upstream indexes each ecosystem's proxy is permitted to fetch from.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-3 (partial) and SR-4(3) (partial) mappings. Supply resolver configuration from the runner image, since a proxy developers can route around is a cache rather than a control. Document the permitted upstream list and cover every ecosystem the program builds in.

- **AP-2.7.2: Internal Namespace Reservation and Public Fallback Prohibition**
    - **Description:** Reserve the program's own package names and organization scopes in the internal proxy and disable public-index fallback for those namespaces, so that a failed internal resolution returns an error rather than a package a stranger published under the same name.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Dependency confusion is a resolution-order defect that scanning cannot close. Fail closed, since a silent public fallback looks correct until malicious code runs. Treat internal package names as sensitive, because they leak through SBOMs, errors, and lockfiles.

- **AP-2.7.3: Newly Published Version Quarantine Window**
    - **Description:** Hold every upstream version published inside the program's defined cooldown interval in proxy-side quarantine until it has aged past that window, and document the interval and its exception path alongside the program's other gate criteria.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity operates the quarantine Artifact/Dependency Malware Scanning Integration relies on, using the interval Component Provenance Admissibility Criteria sets. Most typosquatted and account-takeover packages are withdrawn within days, so the cost is release latency and the benefit is never being the first consumer. Keep a recorded exception path for urgent fixes. It is Level 2 because controlled ingress and namespace protection are the mandatory obligations.

### AP-2.8: Dependency Review

**Design Intent:** Every pull request that changes a dependency manifest is reviewed automatically for known vulnerabilities, license terms, and package health. A component that fails the ASP's criteria cannot merge without an approved exception.

**NIST Control Mapping:**

- **RA-5 (partial):** claimed for identifying known-vulnerable dependency versions at review time, while Container Scanning and Endpoint Detection hold other scanning surfaces.
- **SR-3 (partial):** claimed for the acceptance policy applied to incoming components, tracked jointly with Vendor SBOM Intake and Trusted Internal Package Repository. License Acceptance Policy Definition and Component Provenance Admissibility Criteria carry it jointly as two halves of one policy under different owners.
- **SR-5(2) (partial):** claimed because pull-request review assesses a component before acceptance.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Third-Party Dependency (Embedded Library/Package)

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.8.1: Automated Dependency Review Integration**
    - **Description:** Integrate automated dependency review into the pull request workflow so that any change to a dependency manifest is analyzed and its findings posted to the review before a human approves the merge.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-5 and SR-5(2) (partial) mappings at the moment the reviewer is already looking at the change. Review the transitive graph, since the vulnerable component is rarely the one a developer added.

- **AP-2.8.2: License Acceptance Policy Definition**
    - **Description:** Settle with program counsel which software licenses the program accepts outright, which it refuses, and which require a case-by-case determination, record the resulting list as the license criterion the review gate evaluates every dependency against, and document the policy in the ASP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SR-3 (partial) mapping jointly with Component Provenance Admissibility Criteria. License acceptance is a legal judgment made with program counsel and reviewed annually. Name the cases reviewers would otherwise decide alone, such as strong copyleft in distributed artifacts and components with no license statement at all.

- **AP-2.8.3: Component Provenance Admissibility Criteria**
    - **Description:** Define the origin, publisher, and repository evidence a third-party component must carry before it may be accepted, express each criterion as a threshold the review gate can evaluate rather than a judgment call, record the criteria and their exception path with the program's other gate conditions, and document them in the ASP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the other part of the outcome's SR-3 (partial) mapping, the half the PMO ISSE owns. Set thresholds for signed releases or provenance attestations, an OpenSSF Scorecard floor, maintainer count, repository age, and a publication-to-adoption interval, each with a recorded exception path. The proxy's Newly Published Version Quarantine Window is configured to that interval, and the criteria are reviewed semi-annually.

### AP-2.9: External Runtime Service and Client-Side Code Governance

**Design Intent:** Every user-facing application serves all of its own client code from KESTREL, with no third-party scripts, fonts, or analytics. Content security policies block anything else. No application calls an external runtime service other than those the cloud provider hosts inside the boundary, and any proposal to add one goes through intake.

**NIST Control Mapping:**

- **SA-9 (partial):** claimed for oversight of conventional external services the application calls in its request path. It is one of five population slices, with Contract Security Requirements holding the general provider population, and all are tracked jointly.
- **SA-9(5) (partial):** claimed for restricting where each provider processes and stores transmitted data, shared with Third-Party/Foundation Model API Dependency Governance by population. Contractual flow-down stays with the Manage pillar.
- **SI-7 (partial):** claimed for verifying externally hosted client-side code and refusing a mismatch, tracked jointly with Host Hardening and Integrity Protection's agent self-protection slice.
- **Declined:** SI-7(1) is not claimed, because the framework's SI-7(1) claims cover checks the program runs against objects it holds, while subresource integrity is enforced by a browser the program does not operate.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Client-Side/Browser-Executed Code

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.9.1: External Runtime Service Dependency Inventory and Governance**
    - **Description:** Record each external service the application calls at runtime with its owner, the purpose of the call, the data classes sent to it, the credential it authenticates with, and the residency, retention, and incident-notification terms the provider is held to, and require an entry to exist before a new external dependency reaches a fielded release.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-9 (partial) and SA-9(5) (partial) mappings. Record the data classes transmitted, since analytics and error-reporting integrations often send far more than expected, and record each call's purpose so it can be retired. Reconcile the inventory against the Network and Environment focus area's permitted egress.

- **AP-2.9.2: Client-Side Script Integrity and Third-Party Tag Control**
    - **Description:** Pin every externally hosted script the application includes to a verified digest through subresource integrity, restrict the sources a browser may load executable content from through the content security policy the runtime baseline requires, and refuse to serve a release that references an externally hosted script carrying neither.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7 (partial) mapping against a supply chain attack no program scanner sees. Self-host scripts where possible, and pin digests as the fallback, refreshing pins under dependency-upgrade review. It is Level 2 because an application serving no external client-side code meets the outcome through the inventory alone.

### AP-2.10: Adversarial Code Review

**Design Intent:** High-risk changes get a second review by a designated security reviewer from outside the authoring team. High-risk means authentication and authorization, cryptography, partner release logic, enforcement of the payload vendor split, and any tool an AI agent can call. The reviewer reads the change as an attacker would, and their approval is a required check on the merge.

**NIST Control Mapping:**

- **SA-11(4) (full):** claimed full because this outcome supplies the documented manual review process, the techniques, and the defined body of code High-Risk Change Identification Criteria sets. The obligation rests on the three human activities, while AI-Assisted Adversarial Analysis Generation carries no citation because model output is not manual review.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.10.1: Adversarial/Red-Team Code Review Process Definition**
    - **Description:** Define how an adversarial code review is conducted, who is qualified to perform it, what the reviewer is expected to attempt against the change, and what a completed review must record, and document the resulting process in the ASP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the documented-process dimension of the outcome's SA-11(4) (full) mapping. Require reviewer independence from the change's author. Record what was attempted and found sound as well as what failed, so coverage can be shown later.

- **AP-2.10.2: High-Risk Change Identification Criteria**
    - **Description:** Establish objective, checkable criteria for which changes require adversarial review, naming the code paths, data classes, and design surfaces that qualify, and document them alongside the review process in the ASP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity defines the code the outcome's SA-11(4) (full) mapping applies to. Qualify authentication and authorization logic, cryptography, untrusted input parsing, threat-model trust-boundary crossings, and the most sensitive data classes, using criteria checkable from the change itself. Revisit annually and whenever a threat model adds a trust boundary.

- **AP-2.10.3: AI-Assisted Adversarial Analysis Generation**
    - **Description:** Run an AI agent across each change that meets the high-risk criteria to produce a written adversarial analysis of the complete change set, and deliver that analysis to the human reviewer as preparatory input rather than as the review itself.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent citation, since the SA-11(4) (full) claim rests on human review. Record what the reviewer attempted independently, because a review made entirely of agent findings was not performed. An air-gapped program needs an accredited in-enclave model, or the activity is deferred. It is Level 3 because the manual obligation is met without it.

- **AP-2.10.4: Findings Tracking and Remediation**
    - **Description:** Convert every accepted adversarial review finding into a tracked item with an owner, a severity, and a target date, and verify the fix by re-review rather than closing the item on the developer's assertion.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the flaw-tracking dimension of the outcome's SA-11(4) (full) mapping. Close findings by re-review, since an adversarial finding is usually a reasoning error a plausible fix can leave intact.

### AP-2.11: SBOM Generation and Enrichment

**Design Intent:** Every build produces an SBOM in a standard format, stored in the registry with the artifact it describes. The SBOMs are matched continuously against new vulnerability data, so a newly disclosed flaw can be traced to every release that contains it.

**NIST Control Mapping:**

- **SR-4 (partial):** claimed for documenting the provenance of software the program builds, tracked jointly with Base Image Lineage Report and Build Provenance and Attestation (SLSA).
- **SR-4(1) (partial):** claimed for uniquely identifying each component the bill of materials names, while other provenance outcomes identify their own artifact classes.
- **Declined:** enrichment carries no independent RA-5 claim, since it queries vulnerability data the scanning outcomes already claim.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** CI/CD Pipeline, Database Service

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.11.1: Automated SBOM Generation in Build Pipeline**
    - **Description:** Emit a machine-readable bill of materials in a standard format as an output of every build, capturing the resolved component set and versions the build actually used rather than the ones the manifest declared.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4 and SR-4(1) (partial) mappings. Record resolved versions rather than declared ranges, since the SBOM must describe what shipped. Choose a format the program's consumers and Government customer can ingest.

- **AP-2.11.2: SBOM Enrichment**
    - **Description:** Correlate each generated bill of materials against vulnerability and license data sources so that the record carries the known exposures and license obligations of its components rather than component names alone.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Enrichment answers whether a new vulnerability affects anything fielded. Re-correlating stored SBOMs as advisories publish carries the lasting value. It is Level 2 because generation alone satisfies the mandatory obligation.

- **AP-2.11.3: Vulnerability Exploitability eXchange (VEX) Statement Production**
    - **Description:** Record the program's exploitability determination for each vulnerability the enrichment correlation matches against a component the program ships, and publish the result as a machine-readable exploitability statement keyed to the same artifact digest the bill of materials describes.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent claim and does not reopen RA-5. Recording not-affected determinations keeps re-correlation readable instead of repeating the same assessment every cycle. Bind each statement to an artifact digest and re-decide it per release, using CSAF or the CycloneDX profile.

- **AP-2.11.4: SBOM Storage and Distribution**
    - **Description:** Store every generated bill of materials in a retrievable repository keyed to the artifact it describes, and establish how it is distributed to the Government customer, downstream consumers, and assessors on request.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Key each SBOM to the artifact digest rather than a version string, since two builds of one version can differ. Retain it beyond the artifact's deployment, because questions arrive long after fielding.

### AP-2.12: Vendor SBOM Intake

**Design Intent:** Contracts with every software supplier require an SBOM with each delivery and each update. That includes the payload vendors, the service desk vendor, and the ground equipment manufacturers. Each SBOM is checked for format and completeness and recorded against its product in the inventory. Where a supplier cannot provide one, the gap is recorded and the product's monitoring is tightened.

**NIST Control Mapping:**

- **SR-3 (partial):** claimed for the intake process that obtains and validates supplier composition data. Dependency Review and Trusted Internal Package Repository hold the other slices, and contractual authority comes from the Manage pillar.
- **SR-4(4) (partial):** claimed because validating an acquired product's composition against the supplier's declaration is the pedigree analysis the enhancement describes.
- **Declined:** correlation carries no independent RA-5 claim, since it consumes vulnerability data rather than scanning.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Third-Party Application (COTS), Database Service

**External Dependencies:** The payload vendors, the service desk vendor, and the aircraft and ground equipment manufacturers, which supply SBOMs under their contracts.

**Security Impact:** Moderate

**Activities:**

- **AP-2.12.1: Vendor SBOM Ingestion and Validation Process**
    - **Description:** Define and operate the process that receives a supplier bill of materials, validates its format and completeness against the program's acceptance criteria, and records it against the specific product version it describes.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-3 and SR-4(4) (partial) mappings. Reject an SBOM lacking transitive dependencies rather than filing it. Intake runs on each product delivery or update.

- **AP-2.12.2: Vendor SBOM Vulnerability Correlation**
    - **Description:** Correlate the components a validated vendor bill of materials declares against vulnerability data, and route each material exposure to the program's risk process rather than treating it as a supplier-side concern.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Route correlation output to the program's risk process and a supplier action, since a vulnerable integrated product is the program's risk. Re-run correlation as new vulnerability data publishes.

- **AP-2.12.3: Vendor VEX Statement Intake and Application**
    - **Description:** Request each supplier's exploitability statements alongside its bill of materials, validate that every statement resolves to a product version the program actually fields, and apply the accepted statuses to the correlation output so that a supplier-assessed non-exploitable finding is suppressed with an attributed justification rather than silently dropped.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SR-3 (partial) mapping. Attribute each suppression to the supplier's statement, since an assertion is not evidence and the program owns the risk decision. Validate that statements resolve to a fielded version, and treat supplier silence as no suppression.

### AP-2.13: Image Signing

**Design Intent:** The pipeline signs every image and release package automatically, with keys held in the HSMs. Admission control in every cluster rejects an unsigned image or one signed by any other key. The ground control stations and aircraft verify each edge model package's signature before loading it.

**NIST Control Mapping:**

- **CM-14 (partial):** claimed for container images, refusing deployment of images unsigned by a recognized key. Signed/Verified Pipeline Definitions holds the pipeline-definition scope.
- **SI-7(15) (partial):** claimed for cryptographic authentication of container images before installation, partial because it covers containers only. It is distinct from the SI-7, SI-7(1), SI-7(9), and SI-7(10) claims held for agents, files, and boot integrity.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Container, CI/CD Pipeline, Artifact/Model Registry

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AP-2.13.1: Signing Key Management and Infrastructure**
    - **Description:** Establish the signing identity, key protection, and transparency or attestation storage the image signing scheme depends on, drawing the keys and their protection from the program's key management infrastructure and documenting the arrangement in the KMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Protect the signing key independently of the pipeline, preferring short-lived or workload-bound identities over long-lived keys in CI configuration. Plan revocation and re-signing before an incident. Keyless Sigstore signing needs Fulcio and Rekor reachable, so an air-gapped program records in the KMP whether it deploys them in-enclave or falls back to local key custody.

- **AP-2.13.2: Automated Image Signing in Build Pipeline**
    - **Description:** Sign every image as an automatic step of the build that produced it, recording the signature and its attestation alongside the image in the trusted registry.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Sign inside the build, since a later signature attests only to what was handed to the signer.

- **AP-2.13.3: Signature Verification Enforcement at Deploy**
    - **Description:** Configure the deployment path to verify each image's signature against the program's recognized keys and to refuse any image whose signature is absent, invalid, or signed by an unrecognized identity.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-14 and SI-7(15) (partial) mappings, since both turn on refusing an unverified component. Enforce through the admission engine Policy-as-Code Evaluation deploys, so the rule is version controlled like every other admission policy.

### AP-2.14: Base Image Lineage Report

**Design Intent:** Every build records its base image and digest, and the lineage report shows how far each base has fallen behind its upstream. Base images are the Platform Team's hardened ones from the package mirror. A base past end of life fails the build.

**NIST Control Mapping:**

- **SR-4 (partial):** claimed for the provenance of inherited container layers, tracked jointly with SBOM Generation and Enrichment and Build Provenance and Attestation (SLSA).
- **SR-4(2) (partial):** recording each base image digest and following it through derived images is the tracking the enhancement describes.
- **Declined:** SI-2 is not claimed, since staleness alerting feeds the flaw remediation process Vulnerability and Patch Management (Configuration Policy Orchestration) holds.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Container, Third-Party Dependency (Embedded Library/Package), CI/CD Pipeline, Artifact/Model Registry, Database Service

**External Dependencies:** The public image sources the hardened base images derive from.

**Security Impact:** Moderate

**Activities:**

- **AP-2.14.1: Base Image Provenance Tracking**
    - **Description:** Record the identity, digest, and source registry of every base image each build inherits from, and store that lineage against the produced image so the chain can be resolved later without rebuilding.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4 and SR-4(2) (partial) mappings. Record the digest rather than the mutable tag, or the record cannot say which base a fielded image contains. A lineage entry pointing outside Container Golden Images is itself a finding.

- **AP-2.14.2: Lineage Reporting and Staleness Alerting**
    - **Description:** Report base image lineage across the program's image portfolio and alert the owning teams when a base image has been superseded, has passed its end-of-life date, or has exceeded the program's defined age threshold.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** The staleness age threshold is a documented program decision recorded with the other gate criteria. Alert the consuming teams, since the rebuild happens in each application's pipeline. It is tagged Automate rather than Visualize because it produces records and alerts, not a dashboard.

### AP-2.15: IaC Scanning

**Design Intent:** Every change to infrastructure as code is scanned in the pipeline against the same policy the landing zone guardrails enforce, so a misconfiguration fails before it is deployed. That includes the Platform Team's modules, each team's own infrastructure, and the hubs' rule base.

**NIST Control Mapping:**

- **CM-6(1) (partial):** claimed as an independent pre-deployment slice that verifies settings before they are applied, while the other claimants verify existing resources. The rules encode the baselines Baseline Configuration Standards defines, so any divergence is a defect here.
- **Declined:** CM-3(2) stays with Asset Lifecycle Change Control, since this outcome checks a proposed template rather than validating an implemented change.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Infrastructure-as-Code (IaC), Compute, Storage/Database, Network Infrastructure

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.15.1: IaC Scanning Tool Integration Into CI Pipeline**
    - **Description:** Integrate the infrastructure-as-code scanner into the CI workflow so that every change to a template is evaluated against the policy rule set before the change can be merged or applied.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-6(1) (partial) mapping. Scan the rendered plan as well as the template, since many misconfigurations appear only once variables, modules, and defaults resolve.

- **AP-2.15.2: Policy Rule Tuning and Misconfiguration Baseline**
    - **Description:** Tune the scanner's policy rules to the program's approved baseline configurations, and record each accepted deviation in a reviewed misconfiguration baseline so that a suppression carries a justification and an owner.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Align rules to the baselines Baseline Configuration Standards publishes rather than creating a second definition. It is not tagged Automate because tuning and deviation adjudication are judgment. Review quarterly as provider services and baselines change.

### AP-2.16: Container Hardening Verification

**Design Intent:** The pipeline checks every image and its runtime configuration against the container hardening benchmark before it ships. The checks require a non-root user, a read-only filesystem, dropped capabilities, and resource limits. A failing image cannot reach the registry's release namespace.

**NIST Control Mapping:**

- **CM-6 (partial):** the base is cited for identifying, documenting, and approving deviations, which Hardening Exception and Waiver Tracking supplies, held partial for the container benchmark only.
- **CM-6(1) (partial):** claimed for the automated benchmark check, a pre-deployment slice distinct from Secure Compute Baselines' container definitions and Configuration Policy Orchestration's runtime verification, which hold other parts.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Container, CI/CD Pipeline

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.16.1: CIS/Benchmark Hardening Check Integration**
    - **Description:** Integrate the container and orchestration benchmark checks into the pipeline so that every image and its declared runtime configuration are evaluated against the adopted benchmark as part of the build.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-6(1) (partial) mapping. Check the declared runtime configuration too, since privilege escalation, host mounts, and capability grants live there rather than in the image.

- **AP-2.16.2: Hardening Exception and Waiver Tracking**
    - **Description:** Record every accepted deviation from the hardening benchmark with its justification, approving authority, compensating control, and expiration, and re-review each waiver when it expires rather than letting it stand indefinitely.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-6 (partial) mapping. Give every waiver an expiration date, or it silently becomes the real standard. The record holds configuration deviations only, while an unfixable vulnerability is an RA-7 acceptance routed through the Exception and Risk Acceptance Workflow.

### AP-2.17: Network Policy Verification

**Design Intent:** Every workload ships with a deny-by-default network policy that permits only the flows its team mapped. The pipeline checks that policy against the approved flow map before admission, so a workload with a missing or loosened policy is refused.

**NIST Control Mapping:**

- **AC-4 (partial), SC-7(5) (partial):** each claimed as a pre-deployment slice alongside the runtime claims of Network Micro Segmentation and IT/OT Zone and Conduit Segmentation. It verifies before admission that policy denies by default and matches the baseline Communication Requirements Mapping produces.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Segmentation Policy, Container, Infrastructure-as-Code (IaC)

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **AP-2.17.1: Default-Deny Network Policy Validation**
    - **Description:** Validate that every workload ships with a network policy that denies unmatched ingress and egress by default and permits only the flows the approved communication baseline authorizes, failing the pipeline when no policy is present at all.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-4 and SC-7(5) (partial) mappings before deployment. Treat a missing policy as a failure, since most orchestration platforms allow all traffic when none is attached.

- **AP-2.17.2: Policy Drift Detection Pre-Deploy**
    - **Description:** Compare each proposed network policy against the approved communication baseline and surface every added, broadened, or removed rule in the change review so that a widened flow is an explicit decision rather than an unnoticed edit.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Present the diff to a reviewer rather than blocking, since a rule engine cannot tell a legitimate new flow from an over-permissive one. Fix uncovered flows by updating the baseline through Communication Requirements Mapping. It is Level 2 because default-deny validation meets the mandatory obligation.

### AP-2.18: Pre-Merge Sensitive Repo File Change Detection

**Design Intent:** Pipeline definitions, infrastructure as code, admission policy, dependency manifests, ownership files, and the hubs' rule base are sensitive paths. A change to any of them needs approval from the Platform Team and the Security Team in addition to the team's own reviewer, and each one raises an alert in the security monitoring platform.

**NIST Control Mapping:**

- **CM-3(1) (partial):** claimed for automatically documenting a sensitive repository change, notifying approvers, and holding it until review. Asset Lifecycle Change Control keeps the broader CM-3 (partial) claim, which this outcome feeds.
- **CM-3(4) (partial):** routing sensitive-path changes to security reviewers places a security representative in the change decision.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** CI/CD Pipeline, Infrastructure-as-Code (IaC), Third-Party Dependency (Embedded Library/Package)

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **AP-2.18.1: Sensitive File/Path Change Detection Rules**
    - **Description:** Define the repository paths whose modification requires security review, and configure the pull request checks that detect and flag any change touching them before the merge is permitted.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the detection dimension of the outcome's CM-3(1) (partial) mapping. Put the detection rules on the sensitive path list, or removing a path is the one unnoticed change. It is tagged Automate because matching runs on every pull request.

- **AP-2.18.2: Alert Routing and Review Workflow**
    - **Description:** Route each flagged change to the designated security reviewer, require that reviewer's explicit approval before the merge can complete, and record the disposition with the pull request.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-3(4) (partial) mapping and the approval-blocking dimension of CM-3(1). Make review a required merge check, since a notification alone is a log entry. Where volume is high, use designated reviewers with security context for the path, and define a broader scope and training before using threat modeling champions here.

### AP-2.19: Policy-as-Code Evaluation

**Design Intent:** One policy engine evaluates the pipeline's gates and every cluster's admission decisions. Its rules are version-controlled policy in the Platform Team's repository, changed only by reviewed pull requests. Admission runs in deny mode in every prod spoke and in stage, so stage rejects what production would.

**NIST Control Mapping:**

- **CM-3(1) (partial):** claimed for automatically blocking non-compliant deployments and recording exceptions, shared with Pre-Merge Sensitive Repo File Change Detection's repository slice.
- **SA-15 (partial):** claimed for documenting and controlling changes to tool configuration through version-controlled policy rules, one subject slice alongside Application Threat Modeling and others.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Container Orchestration Control Plane, CI/CD Pipeline, Segmentation Policy

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AP-2.19.1: Admission/Policy-as-Code Engine Deployment**
    - **Description:** Deploy the policy engine into the pipeline and into the cluster admission path so that a single evaluation point decides whether a build artifact or a workload is permitted to proceed.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Decide and document fail-closed or fail-open behavior when the engine is unreachable, since admission now depends on it. Place the engine at admission as well as in the pipeline, because workloads can reach a cluster by other paths.

- **AP-2.19.2: Policy Rule Authoring and Version Control**
    - **Description:** Author the program's admission and deployment rules as policy code held in version control, reviewed through the same pull request process as application code, and tested against known-good and known-bad inputs before release.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-15 (partial) mapping. It is tagged Automate as the named policy-as-code practice. Test each rule against inputs it should reject as well as permit, and put rule files on the sensitive path list.

- **AP-2.19.3: Policy Violation Blocking and Exception Workflow**
    - **Description:** Configure the engine to block anything that violates policy, and define the exception path by which a documented, time-limited, approved waiver permits a specific violation without weakening the rule for everyone else.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-3(1) (partial) mapping, both the prohibition and the recorded approval path. Scope each exception to a named artifact with an expiration, rather than relaxing the rule. Adjudication remains human work.

### AP-2.20: Threat Model Staleness Check

**Design Intent:** A change that adds an interface, a data flow, an external connection, or an AI agent tool flags its application's threat model as stale. The owning team must update the model and the PMO ISSE must re-review it before the change can reach production. Every model is also re-reviewed at least once a year.

**NIST Control Mapping:**

- **SA-11(2) (partial):** claimed for keeping threat models current as the system evolves, a slice of the threat modeling dimension tracked jointly with Application Threat Modeling and AI Threat Modeling. All holders of the enhancement are tracked jointly.
- **Declined:** CM-4 is not claimed, because it covers change impact analysis for deployed resources and the authorized system, not application designs.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.20.1: Architecture-Change-to-Threat-Model Diffing**
    - **Description:** Compare each change touching the application's trust boundaries, authentication paths, external interfaces, or data flows against the threat model of record, and record where the implemented architecture and the modeled one no longer agree.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Detection depends on the machine-readable model repository Threat Modeling Tool Selection and Deployment established. Check the same three change categories the design-review gate uses. It is tagged Automate for the tool-driven comparison.

- **AP-2.20.2: Staleness Alerting and Re-Review Trigger**
    - **Description:** Alert the owning team and open a re-review item whenever the diff exceeds the program's divergence threshold or the model has gone unreviewed longer than the program's defined interval.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The age trigger catches threat changes the diff cannot see. Record both the divergence threshold and the maximum model age with the methodology. It is tagged Automate, while the re-review itself is human work under Application Threat Modeling.

### AP-2.21: Ephemeral/Isolated Build Environments

**Design Intent:** Every pipeline job runs on a fresh containerized runner in Platform Prod, isolated from concurrent jobs and destroyed when the job ends. No build runs on a performer laptop or a long-lived host.

**NIST Control Mapping:**

- **CM-2(6) (partial):** the known runner image is the build environment's own baseline, maintained separately from operational baselines. It is partial because downstream test environments are provisioned by other outcomes.
- **SA-3(1) (partial):** claimed for isolating and disposing of the build environment as a protected preproduction environment. Least-Privilege CI/Build Infrastructure Access and CI Credential and Secrets Management hold the access and credential dimensions, and the Artificial Intelligence focus area holds its own environment classes.
- **SC-39 (partial):** a separate execution focus area per build job is process isolation, cited at the base because neither enhancement describes container-level job isolation. It is tracked jointly with the Artificial Intelligence focus area's other environment-isolation claims.
- **Declined:** SC-7(21) isolates components at the network layer, while this outcome isolates concurrent processes on shared compute, which SC-39 names precisely.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Container, CI/CD Pipeline

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.21.1: Ephemeral, Containerized Build Runner Provisioning**
    - **Description:** Provision a fresh containerized runner from a known image for each build job, and configure the CI system so that no job ever executes on a runner a previous job has used.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-3(1) (partial) mapping. Put the runner image through this capability's scanning and hardening gates. Where a persistent cache is granted for speed, make it content-addressed and read-only to the job.

- **AP-2.21.2: Build Environment Isolation and Teardown Enforcement**
    - **Description:** Enforce that concurrent build jobs cannot reach each other's processes, filesystems, or networks, and that each environment and its storage are destroyed when the job ends whether it succeeded or failed.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-39 (partial) mapping. Tear down failed jobs too, since they are the likeliest to have run something hostile. Where debugging access is needed, grant it through the Identity focus area's privileged access path and destroy the environment on a timer.

### AP-2.22: Least-Privilege CI/Build Infrastructure Access

**Design Intent:** Each team's pipeline identity reaches only its own repositories, its own registry namespace, and its own dev/test spoke. Only the release identity can deploy to a prod spoke, the IL6 transfer gateway, or the edge release path, and it acts only after Certification to Field approves the release.

**NIST Control Mapping:**

- **AC-6 (partial):** claimed for least-privilege scoping of build-system service identities, alongside the Identity focus area's claims. The base is cited because no enhancement addresses scoping a service identity to its pipeline's targets.
- **CM-5 (partial):** claimed for restricting who and what may change the system through the build path. It is one of four slices tracked jointly, with Branch Protection Policy Report holding the source-branch surface.
- **CM-5(5) (partial):** claimed for limiting production-path change privileges and re-evaluating them on a cycle.
- **SA-3(1) (partial):** claimed for the access dimension of protecting the build environment, while Ephemeral/Isolated Build Environments holds the other dimensions.
- **Declined:** AC-6(7) is not re-claimed, since the review runs as a campaign inside Access Reviews, which holds AC-6(7) in full.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application and Service Account Identity, CI/CD Pipeline, Compute, Artifact/Model Registry

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AP-2.22.1: CI Service Account Least-Privilege Scoping**
    - **Description:** Scope each CI service account to the specific repositories, registries, artifact stores, and deployment targets its pipelines require, replacing shared organization-wide build identities with per-pipeline or per-project identities.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-6 and CM-5 (partial) mappings. Replace the single organization-wide build identity, the default that lets one compromised pipeline reach every target. Carry production write access on the short-lived credentials CI Credential and Secrets Management issues.

- **AP-2.22.2: Build Infrastructure Access Review**
    - **Description:** Review the human administrative access to the CI platform, build runners, and artifact registries alongside the standing service account grants, and remove every entitlement the reviewer cannot justify against a current need.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Run this review as a campaign inside the Identity focus area's Access Reviews, which is why it opens no AC-6(7) claim. Hold CI administrative access through the privileged access path rather than as a standing role. The semi-annual cadence reflects how quickly build access changes.

### AP-2.23: Signed/Verified Pipeline Definitions

**Design Intent:** The Platform Team owns signed pipeline templates that every team's pipeline extends, and the pipeline verifies their signatures before it runs a job. A pipeline definition that changed without an approved merge stops the run and alerts the Platform and Security Teams.

**NIST Control Mapping:**

- **CM-14 (partial):** claimed for pipeline definitions, refusing to execute one not signed by a recognized key. Image Signing holds the container image slice.
- **SA-10 (partial):** claimed because signing and verifying the pipeline definition controls the integrity of a configuration item. The base is cited since no enhancement covers a build system verifying its own configuration, and Signed/Verified Training Pipeline Definitions holds the training-orchestrator slice.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** CI/CD Pipeline

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.23.1: Pipeline-as-Code Signing and Verification**
    - **Description:** Sign each pipeline definition when it is approved, and configure the CI system to verify the signature against a recognized key before executing the definition, refusing to run an unsigned or invalidly signed pipeline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-14 and SA-10 (partial) mappings. Use the signing identity Signing Key Management and Infrastructure established, and keep the key out of reach of the CI system itself. It is Level 2 because the reviewed merge path meets the mandatory obligation.

- **AP-2.23.2: Unauthorized Pipeline Modification Detection**
    - **Description:** Compare the pipeline definitions the CI system is actually configured to run against the approved, version-controlled definitions, and alert on any divergence that did not arrive through the reviewed merge path.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the change-integrity dimension of the outcome's SA-10 (partial) mapping. Watch hardest for edits made through the CI platform's console or API, which bypass code review. Route alerts to the Operate pillar's incident handling as integrity events.

### AP-2.24: Build Provenance and Attestation (SLSA)

**Design Intent:** Every build emits signed provenance naming its source revision, runner, pipeline definition, and inputs. Admission control and Certification to Field both verify it. The target is SLSA Build Level 3, which the in-cloud ephemeral runners make reachable.

**NIST Control Mapping:**

- **SR-4 (partial):** claimed for the provenance of how the artifact was produced, tracked jointly with SBOM Generation and Enrichment and Base Image Lineage Report.
- **SR-4(3) (partial):** verifying an attestation at the deployment gate validates that the artifact is genuine and unaltered, with the program's own build as sender. It is tracked jointly with other holders split by artifact class, such as Trusted Internal Package Repository.
- **Declined:** SR-4(4) stays with Vendor SBOM Intake, where software really is acquired, and is not stretched the way the SR-4(3) claim is.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** CI/CD Pipeline, Artifact/Model Registry

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.24.1: Build Provenance Attestation Generation**
    - **Description:** Emit a signed provenance attestation as an output of every build, recording the source revision, the builder identity, the pipeline definition, and the inputs the build consumed.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4 (partial) mapping. Generate the attestation from the build platform, not a step inside the build, which could assert anything. Its trust rests on the runner isolation Ephemeral/Isolated Build Environments provides.

- **AP-2.24.2: Provenance Verification at Deploy Gate**
    - **Description:** Verify each artifact's provenance attestation at the deployment gate against the expected builder, source repository, and pipeline definition, and refuse any artifact whose attestation is absent, unverifiable, or inconsistent with those expectations.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4(3) (partial) mapping. Verify through the Policy-as-Code Evaluation engine alongside the Image Signing check. Write expectations against the specific repository and builder, since an attestation from an unexpected builder is what a compromised pipeline produces.

### AP-2.25: CI Credential and Secrets Management

**Design Intent:** Pipeline jobs authenticate with short-lived credentials bound to their workload identity, and they fetch any remaining secret from their spoke's vault at run time. No long-lived credential is stored in a pipeline variable or repository.

**NIST Control Mapping:**

- **IA-5(6) (partial):** claimed for vaulting build credentials with lifetimes short enough to expire before misuse, a CI slice alongside Secrets and Credentials Protection.
- **IA-5(7) (partial):** claimed for keeping static authenticators out of pipeline configuration. It joins the group jointly tracked with Secret Scanning and the Identity focus area.
- **SA-3(1) (partial):** claimed for the credential dimension of protecting the build environment, while Ephemeral/Isolated Build Environments holds the other dimensions.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Cloud Workload/Native Platform Identity, CI/CD Pipeline

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-2.25.1: Short-Lived/Ephemeral CI Credential Issuance**
    - **Description:** Issue each pipeline run a short-lived, workload-bound credential obtained through federation with the program's identity platform, so that the credential expires with the job rather than persisting as a stored secret.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(6) (partial) mapping. Design it together with the scoping in Least-Privilege CI/Build Infrastructure Access, since neither works alone. Prefer federation with the identity platform over vault-issued tokens, because it removes the bootstrap secret.

- **AP-2.25.2: CI Secrets Vault Integration**
    - **Description:** Integrate the pipeline with the program's secrets vault so that every secret a job needs is retrieved at run time and none is written into pipeline definitions, CI platform variables, or the repository.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(7) (partial) mapping through the vault NPE Credential Vault Integration established. Reject the CI platform's own secret variables, which any pipeline editor can print. Log masking complements this but is easily defeated by encoding.

## AP-3: Testing and Continuous Delivery

### AP-3.1: Test Data Management and Preproduction Data Controls

**Design Intent:** Dev, test, and stage clusters in every application team's spoke run on synthetic or sanitized data, never live mission data. The Data Team produces the sanitized sets by removing incidental imagery of people and anything identifying a source. Stage carries production's configuration but not production's data.

**NIST Control Mapping:**

- **SA-3(2) (partial):** claimed for approving, documenting, and controlling live data in application testing environments. It is partial because infrastructure staging and the Artificial Intelligence focus area's evaluation environments remain, recorded as a gap under the Control Mapping Methodology.
- **Declined:** SA-15(9) is withdrawn into SA-3(2), so nothing is cited under the SA-15 family. SA-3(1) stays with Least-Privilege CI/Build Infrastructure Access. PM-25, SI-12(2), and SA-15(12) stay with Data Minimization Requirement Definition, which this outcome implements.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Database Service, First-Party/Custom Application Code, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AP-3.1.1: Masked and Synthetic Test Data Generation**
    - **Description:** Generate the datasets lower environments run on by masking, tokenizing, or synthesizing every field the program's data classification marks as sensitive, preserving referential integrity and value distribution so the result remains usable for testing without carrying the original content.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the control dimension of the outcome's SA-3(2) (partial) mapping. Preserve referential integrity, or teams quietly return to production copies. Generate low-entropy fields such as postal codes and birth dates rather than transforming them, since they are re-identifiable, and run the pipeline on a schedule to track the schema.

- **AP-3.1.2: Live Data Use Approval and Preproduction Handling Workflow**
    - **Description:** Require a recorded approval before any live or operational data enters a preproduction environment, capturing the approving authority, the data classes involved, the environment and the controls it actually enforces, the authorized retention period, and the disposal step that ends the authorization.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the approve-and-document dimension of the outcome's SA-3(2) (partial) mapping. Give every approval an expiration, condition it on the receiving environment's controls, and verify disposal of derived copies. Record refusals too, since a workflow that never declines is only a log.

### AP-3.2: DAST

**Design Intent:** Every candidate build of a user-facing application is scanned by DAST in its team's stage cluster, both unauthenticated and with test accounts for each role. Findings above the ASP's threshold block Certification to Field.

**NIST Control Mapping:**

- **SA-11 (partial):** claimed for test planning, depth and coverage, and flaw correction across the capability, anchored here as the standing every-build test. It is partial because technique enhancements are claimed separately and SA-11(3) and SA-11(7) have no claimant here.
- **SA-11(8) (partial):** run-time verification against a deployed instance, tracked jointly with Fuzz Testing and Training Pipeline Fuzz Testing.
- **SA-11(9) (partial):** carried by Interactive Application Security Testing (IAST) Instrumentation. It is partial because unsupported runtimes are recorded as a gap.
- **RA-5 (partial):** claimed for the deployed-application scanning surface, an independent slice alongside Container Scanning and others. The base is cited for the reason those slices give.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-3.2.1: DAST Tool Integration Into CD Pipeline**
    - **Description:** Wire the dynamic scanner into the CD pipeline so that each candidate build is deployed to a scan target and exercised automatically before it can be promoted toward production.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(8) and RA-5 (partial) mappings. Run a bounded scan on every build and a full scan on a schedule, since a full crawl does not fit a deployment window.

- **AP-3.2.2: Interactive Application Security Testing (IAST) Instrumentation**
    - **Description:** Instrument the deployed scan target with an interactive analysis agent so the dynamic scan's traffic is observed from inside the running process, reporting the code path, data flow, and query each request actually reached rather than only the response it produced.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(9) (partial) mapping and part of its SA-11(8) (partial) mapping, observing instrumented code under real input. SA-11(1) stays with SAST. Keep the agent in the test build and never in the release artifact, as distinct from Runtime Application Self-Protection (RASP). It is Level 3 but rises to Level 1 wherever the tailored baseline includes SA-11(9), and a program on an unsupported runtime records that fact.

- **AP-3.2.3: Authenticated Scan Configuration**
    - **Description:** Configure the scanner with credentials, session handling, and coverage for each of the application's user roles so that the functionality behind the authentication boundary is exercised rather than only the pages an anonymous client can reach.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** An unauthenticated scan covers only the part of the application an attacker ignores. Verify that authenticated views were actually reached, since a scanner that loses its session keeps reporting. Issue scan accounts as non-person entities scoped to the test environment, and revise the configuration when authentication flows or roles change.

- **AP-3.2.4: Finding Triage and Remediation SLA**
    - **Description:** Set the severity-tiered timeframes a confirmed dynamic finding must be corrected within, triage each result to separate real findings from scanner noise, and track every confirmed finding to closure against that clock.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Adopt the remediation tiers of the Vulnerability and Patch Management Plan (VPMP) and document only deviations. Triage from the start, since dynamic scanners report many non-vulnerabilities. Disposition a finding that misses its tier through the Exception and Risk Acceptance Workflow.

### AP-3.3: Application Security and Development (ASD) STIG Compliance

**Design Intent:** Every first-party application is evaluated against the ASD STIG before Certification to Field. Each applicable requirement is mapped to the control or setting that meets it, and the evaluation results are part of the release evidence. Open findings carry into STIG Risk Tracking.

**NIST Control Mapping:**

- **CM-6 (partial):** claimed for establishing application-layer settings and documenting approved deviations, which the checklist mapping and gate exception path supply. The ASD STIG governs how the application is built and configured, which no other baseline claimant such as Baseline Configuration Standards reaches.
- **CM-6(1) (partial):** the automated application-layer checklist evaluation, split from the base the same way Container Hardening Verification splits its own, which holds another slice.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-3.3.1: ASD STIG Checklist Mapping to Application Controls**
    - **Description:** Map every applicable ASD STIG requirement to the specific application control, configuration setting, or design element that satisfies it, and record each requirement the application cannot meet with its justification and compensating control.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the settings-establishment and deviation-documentation dimensions of the outcome's CM-6 (partial) mapping. Map each requirement to a named implementation in Control-to-Requirement Traceability Mapping rather than an assertion. Disposition non-applicable items with a written rationale, and remap on each new STIG release or architecture change.

- **AP-3.3.2: Automated STIG Compliance Scanning**
    - **Description:** Evaluate the automatable subset of the ASD STIG checklist against every candidate build and its deployed configuration, emitting a machine-readable result that carries an explicit not-evaluated status for the manual-review items and that the pipeline gate and the program's compliance reporting both consume.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-6(1) (partial) mapping. Effort is High because DISA publishes no SCAP content for the ASD STIG, so the program writes and maintains its own checks. Emit machine-readable output for the gate, the finding register, and compliance aggregation, and never count manual-review items as passing.

- **AP-3.3.3: STIG Finding Remediation Within CD Gate**
    - **Description:** Set the finding severity at which the CD pipeline refuses to promote the artifact, and correct or formally exempt every finding at or above that line before deployment proceeds.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Halt the promotion, since an open finding that reaches production becomes a POA&M item in STIG Risk Tracking. The threshold is a documented PMO ISSE risk decision. Record accepted deviations in the ASD STIG Checklist Mapping to Application Controls deviation record with an expiration, while vulnerability acceptances route to the Exception and Risk Acceptance Workflow.

### AP-3.4: API Security Testing

**Design Intent:** Every API with a published schema is tested from that schema in stage, including authorization tests for each role and partner. Today those are the partner API, the feedback endpoints, and the model endpoints the mission teams call.

**NIST Control Mapping:**

- **SA-11(2) (partial):** carried by Business Logic and Abuse Case Testing, which executes the abuse cases Application Threat Modeling's models imply. It holds the vulnerability analysis dimension for conventional applications, tracked jointly with Training Pipeline Misuse/Abuse Case Testing.
- **SA-11(6) (partial):** schema-driven review of every declared operation and its authorization. It is partial because undeclared interfaces belong to Runtime API Inventory and Governance.
- **SI-10 (partial):** pre-deployment verification that the application rejects malformed input. Web Application Firewall holds the runtime enforcement slice, and no enhancement describes these cases better than the base.
- **SI-10(6) (partial):** verifies that injection payloads never reach an interpreter. Web Application Firewall holds its own edge-filtering claims on this enhancement.
- **Declined:** authorization abuse testing opens no AC-3 or AC-6 claim, since it verifies enforcement the Identity focus area establishes. Rate limiting tests likewise verify the SC-5-family protections Network and Environment holds.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** API/Interface Contract

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-3.4.1: API Schema/Contract Security Testing**
    - **Description:** Generate and execute security test cases directly from the application's OpenAPI or Swagger definition so that every declared operation, parameter, and response is exercised, and flag each divergence between the deployed API's actual behavior and the contract it publishes.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(6) (partial) mapping. Treat divergence from the contract as a finding, since an undeclared parameter or endpoint is an unreviewed interface. Cover GraphQL introspection, query depth and batching limits, and field-level authorization, plus gRPC server reflection, supplying proto descriptors so gRPC methods are enumerable.

- **AP-3.4.2: Authentication/Authorization Abuse Testing**
    - **Description:** Attempt each API operation as an unauthenticated client, as an authenticated client holding lower privilege, and as one requesting another user's or tenant's objects, and record every request the API serves that it should have refused.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Target object-level authorization, which scanners miss because it requires knowing which identity owns which object. Design cases from the authorization model and refresh them when it changes. Work results under the Finding Triage and Remediation SLA clock.

- **AP-3.4.3: Rate Limiting and Injection Testing**
    - **Description:** Send request volumes above the API's declared limits and payloads carrying SQL, command, template, and deserialization injection patterns into every parameter the schema exposes, and record where throttling fails to engage or a payload reaches an interpreter.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-10 and SI-10(6) (partial) mappings. Send payloads to the application directly, not through the Web Application Firewall, since the WAF is a compensating layer. Test that rate limiting counts per identity and leaks nothing, and run volume tests only in a test environment on a controlled schedule.

- **AP-3.4.4: Business Logic and Abuse Case Testing**
    - **Description:** Derive test cases from the threat models Application Threat Modeling produces and execute them against the running application, exercising step reordering and skipping, concurrent and replayed submission of a multi-step approval, and manipulation of the quantity, price, and state values the workflow assumes only it can set.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(2) (partial) mapping and turns threat models into tests for flaws where every request is valid but the sequence is not. Cover skipped steps, concurrent double-spend, replayed approvals, and unchecked client-supplied values, re-running when workflows change. It is Level 2 but mandatory where the baseline includes the enhancement.

### AP-3.5: Penetration Testing

**Design Intent:** The third-party penetration testers test all of KESTREL at least once a year and the paths reachable from outside every six months. They also test after any major change, such as a new spoke, interconnection, or external API. Fleet systems are tested on spares or a simulator. Each finding becomes a POA&M item and is retested before it closes. The testers act as an independent check on the design the PMO ISSE produced.

**NIST Control Mapping:**

- **CA-8 (full):** Penetration Test Scoping and Scheduling sets the frequency and targets, while tracking and retest carry the corrective action. Findings enter the Plan of Action and Milestones (POA&M), and unremediable ones go through the Exception and Risk Acceptance Workflow.
- **CA-8(1) (partial):** the independent testing agent the scoping activity requires, with the contracting share held by the Manage pillar.
- **SA-11(5) (partial):** the testing the program commissions against its fielded system, with performer obligations flowed down through the Manage pillar. It is tracked jointly with the Artificial Intelligence focus area's Red Teaming and Red-Team Findings Sign-Off.
- **Declined:** CA-8(2) is adversary emulation measuring detection and response, which belongs to the Operate pillar. CA-8(3) covers facility testing the PSO owns.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, Compute, Identity Platform

**External Dependencies:** The penetration testing provider, under each engagement's rules of engagement.

**Security Impact:** Moderate

**Activities:**

- **AP-3.5.1: Penetration Test Scoping and Scheduling**
    - **Description:** Define the target set, rules of engagement, permitted techniques, and testing frequency for each engagement, and schedule tests so that a major release or architecture change is followed by one rather than covered by an expired result.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the frequency and target dimensions of the outcome's CA-8 (full) mapping and the independence requirement of its CA-8(1) (partial) mapping. Write rules of engagement that include production, credential theft, and key integrations, or the test measures a system the program does not run. Treat the annual cadence as a floor and retest after major authentication or interface changes.

- **AP-3.5.2: Findings Remediation Tracking and Validation**
    - **Description:** Convert every accepted penetration test finding into a tracked item carrying an owner, a severity, and a remediation date, and validate each proposed fix against the technique that produced the finding rather than against its written description.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the corrective-action dimension of the outcome's CA-8 (full) mapping. Move findings that miss their timeframe into the POA&M through the Manage pillar. Record whether the fix addressed the instance or the underlying pattern.

- **AP-3.5.3: Retest/Closure Verification**
    - **Description:** Have the tester re-execute the original attack path against the remediated system, and close the finding only on a documented failed exploitation attempt.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Retest with the original tester, who knows which preconditions the fix had to remove. Record what was retried and what happened, since a closure without that is an assertion. Where a compensating control closes a finding, the retest shows what it blocks for the risk acceptance decision.

### AP-3.6: Fuzz Testing

**Design Intent:** Coverage-guided fuzzing targets every parser that takes untrusted input. These include the feedback endpoints that accept released products from the IL6 enclave, the partner API, and the ingest code that parses each payload vendor's raw formats. Fuzzing runs on each change to those parsers and continuously in the dev/test spokes.

**NIST Control Mapping:**

- **SA-11(8) (partial):** the malformed-input slice, which the enhancement names directly, tracked jointly with DAST and Training Pipeline Fuzz Testing.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, API/Interface Contract

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-3.6.1: Fuzz Testing Tool Integration**
    - **Description:** Deploy coverage-guided fuzzing against the application's parsers, deserializers, and API entry points, build a harness and seed corpus for each selected target, and run the campaign continuously against the current build rather than as a scheduled pass.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(8) (partial) mapping. Harness quality decides results, so target parsers directly and seed corpora from real traffic. Compile the fuzzed build with coverage instrumentation, never ship it, and run campaigns continuously rather than inside a pipeline timeout.

- **AP-3.6.2: Crash/Finding Triage and Remediation Workflow**
    - **Description:** Deduplicate each crash to the underlying defect, attach a minimized reproducer, assess exploitability, and route the result into the development backlog with a severity and an owner.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Deduplicate crashes, or the queue is abandoned within a week. Exploitability assessment stays human judgment. Deliver a minimized reproducer so developers can confirm the fix.

## AP-4: Certification to Field (CtF)

### AP-4.1: Branch Protection Policy Report

**Design Intent:** Every repository's protected branches require a second reviewer, passing checks, and signed commits, with no administrator bypass. A daily scan reports any repository that has drifted from those settings, and it opens a ticket to its owning team. The report is part of Certification to Field's evidence.

**NIST Control Mapping:**

- **CM-5 (partial):** claimed for restricting who and what may change the program's source branches. It is one of four slices tracked jointly, with Least-Privilege CI/Build Infrastructure Access holding the build-infrastructure boundary.
- **CM-5(1) (partial):** the source platform's automated enforcement and its record, shared with Application Rollback, Progressive Delivery, and Feature Flag Governance for the flag platform.
- **Declined:** CM-3(1) stays with Pre-Merge Sensitive Repo File Change Detection, and this outcome supplies the enforcement that makes its hold unavoidable.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** CI/CD Pipeline

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AP-4.1.1: Branch Protection Rule Enforcement Scanning**
    - **Description:** Enumerate every repository directly from the source platform and evaluate each against the program's required branch protection settings, emitting a machine-readable finding for every rule that is missing, weakened, or exempts administrators.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-5(1) (partial) mapping. Apply the rules to administrators and owners too, or the protection is documentation. Enumerate repositories from the platform rather than a maintained list.

- **AP-4.1.2: Non-Compliant Repository Remediation Workflow**
    - **Description:** Route each non-conforming repository to its owner with the specific settings to restore, apply the required configuration centrally wherever the platform supports organization-level policy, and hold any repository that cannot conform under a recorded, expiring exception.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the deviation-handling dimension of the outcome's CM-5 (partial) mapping. Apply settings centrally through organization-level policy where possible. Handle repositories that cannot comply, such as vendor mirrors, as expiring exceptions rather than removing them from scope.

- **AP-4.1.3: Branch Protection Compliance Reporting**
    - **Description:** Publish the portfolio's branch protection conformance as a standing report showing which repositories conform, which do not, which are operating under exception, and how long each open deviation has been outstanding.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Report deviation age, since a percentage alone cannot show whether the same repositories keep failing. Retain each report as evidence that restrictions held across the assessment period.

### AP-4.2: Artifact Bundle Integrity Verification

**Design Intent:** The digest of every member of a release bundle is recorded when the bundle is assembled. Each digest is checked again at deployment to a prod spoke, at staging for the IL6 transfer, and at loading on a ground control station. A bundle that fails any check is stopped and reported to the Security Team.

**NIST Control Mapping:**

- **SI-7(6) (partial):** cryptographic detection of unauthorized change across the release bundle between build and deployment, distinct from the host-integrity SI-7 claims. Offline/Air-Gapped Model Integrity Verification holds the model-package slice, tracked jointly.
- **CM-14 (partial):** the bundle members outside the container image, such as manifests, charts, configuration, and migration scripts. It is one of six CM-14 slices tracked jointly, with Image Signing holding container images.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** CI/CD Pipeline, Artifact/Model Registry, Container

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-4.2.1: Build-to-Deploy Artifact Hash/Signature Verification**
    - **Description:** Record the digest and signature of every bundle member at build time in a signed release manifest, and re-compute and re-verify each member against that manifest at the deployment boundary.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(6) and CM-14 (partial) mappings. The signed manifest is the control, so the build produces it and the deployment path cannot rewrite it. For air-gapped delivery, the verifying key or trust anchor must reach the enclave by an independent path established in advance, not on the same media.

- **AP-4.2.2: Artifact Bundle Tamper Detection and Blocking**
    - **Description:** Halt the deployment on any digest mismatch, missing member, or unexpected addition, and raise the failure as a security event routed into the program's incident response process rather than as a pipeline error.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Treat an integrity failure as a security event, since even benign causes are control failures. Block unconditionally and disposition through incident response rather than the release gate's override workflow.

### AP-4.3: Approver and Reviewer Audit Log

**Design Intent:** Every review, approval, dismissal, and override in the source repository is forwarded to the security monitoring platform, where the Platform Team's administrators cannot change it. Each approval is checked against the approver's entitlement at the time, so an approval from someone not entitled to give it is flagged.

**NIST Control Mapping:**

- **AC-5 (partial):** enforces that the identity approving a change is not its author. Defining the full set of separated duties is a governance obligation, and Key Access Separation of Duties holds a further slice tracked jointly.
- **CM-5(4) (partial):** enforces dual authorization at the merge, while AC-5 carries the separation determination. It is partial because it covers only merges to protected source branches.
- **AU-12 (partial):** audit records for code review and approval events, a narrow event class, while the Operate pillar holds audit generation generally.
- **AU-9(3) (partial):** cryptographic protection of those records against platform administrators, shared with Training Job Audit Logging for training records.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** CI/CD Pipeline, Identity Lifecycle and Governance, Security Information and Event Management (SIEM) Platform

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-4.3.1: Approval/Review Event Capture and Immutable Logging**
    - **Description:** Export every review submission, approval, dismissal, and protection-override event from the source platform to an append-only store outside that platform's administrative control, binding each record cryptographically so later modification is detectable.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-12 and AU-9(3) (partial) mappings. Capture overrides and dismissals, which matter more to an assessor than approvals. Export to the program's own log pipeline rather than a separate store.

- **AP-4.3.2: Separation-of-Duties Validation**
    - **Description:** Verify on every merge to a protected branch that no approving identity also authored a commit in the change, and refuse the merge where the two resolve to the same person or the same non-person identity.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-5 and CM-5(4) (partial) mappings. Resolve identities to the person through the Identity focus area's account records, since second accounts and bots defeat account-level checks, which is why effort is Moderate. A team too small for a second approver documents its compensating review for the AO rather than disabling the check.

### AP-4.4: Runtime Security Baseline

**Design Intent:** Each release carries a versioned runtime baseline covering its workload identity, privileges, filesystem, resource limits, and exposed interfaces. Stage runs the release against that baseline before Certification to Field, so a release that would run differently in production is caught first.

**NIST Control Mapping:**

- **CM-2 (partial):** the baseline of a deployed application release, an asset class no other CM-2 claimant reaches. Secure Platform Services and Application Baselines sets per-platform configuration rather than per-release settings.
- **CM-6(1) (partial):** automated evaluation of the composed release, where an overriding manifest can make compliant components a non-compliant deployment. Per-component checks such as Container Hardening Verification hold other slices.
- **Declined:** CM-6 is not claimed at the base, since ASD STIG Compliance and Container Hardening Verification hold deviation handling, and deviations here use Hardening Exception and Waiver Tracking.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Container

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-4.4.1: Runtime Configuration Baseline Definition**
    - **Description:** Define and version the security-relevant runtime settings every release must satisfy, covering workload identity, privilege and filesystem posture, resource limits, exposed interfaces, transport configuration, logging, disabled diagnostic features, the cross-origin resource sharing allowed-origin policy, and the HTTP security response headers and cookie attributes the application must emit, namely content security policy, HTTP Strict Transport Security, X-Content-Type-Options, frame-ancestors, and the Secure, HttpOnly, and SameSite cookie flags, then publish the result where the conformance check reads it and document the baseline in the ASP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** State each entry as a setting with a required value that a check can evaluate. Derive from the platform baseline, container benchmark, and ASD STIG, adding only application-specific settings. Revise when architecture, platform, or adopted standards change.

- **AP-4.4.2: Pre-Deployment Baseline Conformance Check**
    - **Description:** Evaluate each candidate release as composed for deployment against the runtime baseline, and fail the certification gate on any deviation the program has not formally accepted.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-6(1) (partial) mapping. Evaluate the rendered deployment after overlays apply, since overlays usually introduce the weakening. Express rules through the Policy-as-Code Evaluation engine so they also apply at admission.

### AP-4.5: Deployment Risk Threshold Evaluation

**Design Intent:** The pipeline combines each release's findings into one risk score against thresholds the PMO ISSE sets in the ASP. A release within the thresholds proceeds on the pipeline's evidence. A release outside them goes to the PMO ISSE, who approves it, sends it back, or escalates it for risk acceptance.

**NIST Control Mapping:**

- **RA-3 (partial):** a risk assessment of each candidate release, updated when it changes, while system-level assessment is held by the Manage pillar. The base is cited because the enhancements address supply chain, intelligence, and analytics.
- **RA-7 (partial):** release-level response to findings per the program's risk tolerance, one slice the Manage pillar's Risk Acceptance Process enumerates alongside the others.
- **Declined:** CA-6 is not claimed, because the go/no-go gate operates inside an authorization the AO already granted.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AP-4.5.1: Risk Scoring Model Definition**
    - **Description:** Define how the structured output of each upstream scanning and testing outcome is normalized, weighted, and combined into a single release risk score, and document the model, its weights, and its inputs alongside the program's other gate criteria in the ASP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-3 (partial) mapping. Normalize severities across tools before scoring. Weight exploitability, reachability, and external exposure with the AO's expectations in view, and require upstream tools to emit machine-readable results.

- **AP-4.5.2: Automated Go/No-Go Gate Enforcement**
    - **Description:** Enforce the promotion decision automatically by comparing each release's computed score and its individually disqualifying findings against the documented threshold, and stop the deployment when either is exceeded.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-7 (partial) mapping. Add disqualifying conditions that block regardless of score, such as an externally reachable critical, an unsigned artifact, or a failed integrity check. Record the decision, inputs, and score with the release.

- **AP-4.5.3: Risk Acceptance and Exception Workflow for Threshold Overrides**
    - **Description:** Route every request to field a release above the threshold through a recorded decision carrying the accepting authority, the specific findings accepted, the compensating controls, and an expiration, and hold promotion until that record exists.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the risk-tolerance dimension of the outcome's RA-7 (partial) mapping. A sanctioned override keeps the threshold from being lowered. Acceptances expire and become POA&M items if they persist, and the PMO ISSE or above approves them, never the blocked engineer.

### AP-4.6: Application Rollback, Progressive Delivery, and Feature Flag Governance

**Design Intent:** Every prod spoke keeps the previous certified release ready to roll back to. New releases reach a small share of traffic first, and they widen only if security and health signals stay clean. Feature flags are configuration in the repository, so changing one is a reviewed change like any other.

**NIST Control Mapping:**

- **CP-10(4) (partial):** restoring a fielded application to a signed, attested prior release within a defined time. It is tracked jointly with the Artificial Intelligence focus area's Rollback/Kill-Switch Mechanism and Rollback/Kill-Switch Readiness Check.
- **CM-5 (partial):** access restrictions on the runtime feature flag, the one change path reaching production without passing any other. It is one of four slices tracked jointly, with Branch Protection Policy Report holding the source branch.
- **CM-5(1) (partial):** the flag platform's automated enforcement and change record, while Branch Protection Policy Report holds the source-platform share.
- **Declined:** the CP-10 base belongs to the Operate pillar's recovery focus area. CP-12 does not apply, since a rollback runs a certified configuration. CM-3 and CM-3(2) stay with Asset Lifecycle Change Control. SI-2 belongs to Patch Testing, Staged Rollout, and Rollback. CM-2(3) stays with Registry Hygiene Report.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Container, Database Service

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-4.6.1: Verified Rollback Path to a Previously Certified Release**
    - **Description:** Provide a single operator action that returns a fielded environment to a designated prior release within the program's stated recovery time, and condition that action on the target still carrying the signature, attestation, and certification record the deployment gate would require of it today.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-10(4) (partial) mapping and is tagged Automate because reversal runs on one instruction. Roll back the deployment as a set, since irreversible migrations bound the reach. Verify the target against the current gate, recording any knowing exception through Risk Acceptance and Exception Workflow for Threshold Overrides, and rely on Registry Hygiene Report for retention depth.

- **AP-4.6.2: Progressive Delivery and Automated Abort on Security Signal**
    - **Description:** Expose each new release to a bounded population first and advance it through defined stages only while the promotion criteria hold, aborting the rollout automatically back to the prior release when an authentication failure rate, authorization denial pattern, runtime protection event, or error signature the program has designated crosses its threshold.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Name security signals explicitly in the promotion criteria, since an authorization failure produces no errors or latency. Design stages to be representative and large enough to signal, and share one reversal mechanism with the rollback path. It is Level 2 because the sibling rollback meets the mandatory obligation.

- **AP-4.6.3: Security-Relevant Feature Flag Change Control**
    - **Description:** Classify which flags alter security-relevant behavior, restrict who may change those flags in a fielded environment, require the same review and approval a code change to that behavior would receive, and record every change with its actor, prior value, new value, and justification.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-5 (partial) and CM-5(1) (partial) mappings. Classify flags that switch authorization, validation, cryptography, logging, rate limits, or diagnostics, building the list from threat models and the runtime baseline. Retire stale flags and retain change history like Approver and Reviewer Audit Log evidence. A program with no flag mechanism records that fact.

### AP-4.7: Application Registration and Inventory Logging

**Design Intent:** Deployment to a prod spoke fails unless the application is registered in the asset inventory with its owning team, product owner, data handled, and current version. Registration happens once at intake and updates automatically with each release.

**NIST Control Mapping:**

- **CM-8 (partial):** the application as an inventoried component, which spans hosts Asset Inventory and Discovery holds but is none of them. A host list cannot say which system a finding affects.
- **CM-8(1) (partial):** updating the inventory as part of each deployment, so it is current by construction.
- **Declined:** CM-8(4) stays with Resource Tagging and Ownership Strategy, whose owner and classification values the record reuses.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Database Service

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-4.7.1: Application Registration in Authoritative Inventory**
    - **Description:** Create or update the application's record in the program's authoritative inventory as a required step of the deployment, capturing its identity, version, environment, exposed endpoints, and the source repository and build that produced it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-8(1) (partial) mapping. Have the deployment write the record, since it already holds every value and asking teams leaves gaps. Link the record to the source repository and build, so an incident can find which running applications contain a component.

- **AP-4.7.2: Inventory Record Enrichment**
    - **Description:** Populate each application record with its accountable owner, mission criticality, and the classification of the data it processes, drawing those values from the taxonomies the program already maintains rather than defining new ones.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Point at the Data focus area's classification and Resource Tagging and Ownership Strategy's owner taxonomy rather than restating them. Set criticality from documented mission dependency, not team estimates. Update on reassignment, mission change, or data change.

## AP-5: Operations and Continuous Monitoring

### AP-5.1: Architecture Risk Tracking

**Design Intent:** Design risks that a threat model identified and the program chose to accept go into one architecture risk register. Each carries its owner, rationale, compensating measures, and review date. The register feeds the program's risk register, so the AO sees every accepted design risk.

**NIST Control Mapping:**

- **RA-7 (partial):** response and disposition tracking for design-level findings, which survive every release built on the design. It is one RA-7 slice tracked jointly, with the Manage pillar's Risk Acceptance Process carrying the full enumeration.
- **CA-7(4) (partial):** monitoring accepted design risk for effectiveness and change over time. It is partial because compliance monitoring sits with this capability's compliance outcomes and the Manage pillar.
- **Declined:** SA-11(2), SA-15, SA-15(2), and SA-15(8) stay with Application Threat Modeling, whose output this register consumes. RA-3 stays with Deployment Risk Threshold Evaluation and the Manage pillar's risk register.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-5.1.1: Architecture Risk Register Maintenance**
    - **Description:** Record every accepted, partially mitigated, or deferred architecture risk the program's threat models produce as a register entry carrying its affected component, current disposition, compensating controls, accountable owner, and review date, and keep those entries current as later releases change the design they describe.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-7 (partial) mapping. Give every entry an owner and a review date. Reference the originating threat model finding rather than restating it, and update on a new model, design change, or review date.

- **AP-5.1.2: Risk Trend Reporting and Escalation**
    - **Description:** Report the register's movement on a fixed cadence, showing what opened, what closed, and what has aged past its review date, and escalate any risk that crosses the program's documented tolerance to the PMO ISSE and the AO.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-7(4) (partial) mapping. Report movement rather than counts, since a static total hides whether risks are closing. Write escalation triggers in advance, and escalate urgent items without waiting for the quarterly report.

### AP-5.2: STIG Risk Tracking

**Design Intent:** Each open ASD STIG finding against a fielded application is bound to a POA&M item with a remediation milestone. The Security Team reports the open findings with each continuous monitoring cycle.

**NIST Control Mapping:**

- **CA-5 (partial):** cited at the base because CA-5(1) was withdrawn into PM-4. This outcome owns the application-layer STIG register and its POA&M linkage, tracked jointly with the Manage pillar's Plan of Action and Milestones (POA&M).
- **CA-7(3) (partial):** trend analysis over successive STIG results, telling the program whether implementations or check cadence need to change. Unified Vulnerability Dashboard holds the cross-tool RA-5(6) comparison.
- **Declined:** CM-6 and CM-6(1) stay with ASD STIG Compliance, whose machine-readable output feeds this register.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-5.2.1: STIG Finding Register and Ongoing ConMon POA&M Linkage**
    - **Description:** Maintain the register of every open ASD STIG finding on the fielded application, carrying its severity, the release it was found in, its accepted deviation record where one exists, and the identifier of the POA&M item that owns its remediation.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-5 (partial) mapping. The linkage to the plan of action is the point, so no scan finding is missing from the POA&M. Populate the register from machine-readable output, and record whether each closure was a fix or an accepted deviation.

- **AP-5.2.2: STIG Risk Trend Reporting and Escalation**
    - **Description:** Report on a fixed cadence how the open STIG finding population changed since the last period, and escalate to the PMO ISSE and the ISSM any finding that passes its POA&M milestone or any severity band that accumulates above the program's documented tolerance.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-7(3) (partial) mapping. Report finding age, since a stable count hides items carried indefinitely. Escalate milestone slips to the ISSM as well as the PMO ISSE, since they change authorization posture.

### AP-5.3: Trusted Registry ConMon Report

**Design Intent:** Admission control lets a cluster pull only from the program's registry. A continuous check confirms that every running workload resolves to it, and any image from elsewhere raises an alert in the security monitoring platform.

**NIST Control Mapping:**

- **SR-4 (partial):** monitoring that running artifacts still carry their recorded provenance. It is a fourth slice tracked jointly with Base Image Lineage Report and the other provenance outcomes, which record provenance at build time.
- **Declined:** SR-4(2) stays with Base Image Lineage Report. CM-14 is held by the signing outcomes, and a validly signed image from an untrusted registry is still this outcome's finding. CM-7(5) belongs to Execution and Device Control, and CM-8(3) to Deployment Inventory Report.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Artifact/Model Registry, Container

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-5.3.1: Trusted Registry Source Validation**
    - **Description:** Resolve the registry source of every running workload's image against the program's list of approved registries on an ongoing basis, and record each result against the deployment it describes.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4 (partial) mapping. Resolve by registry host and digest, not tag. Where an admission controller enforces the allowlist, use this report to prove enforcement covers every namespace, and record which upstreams each pull-through cache may serve.

- **AP-5.3.2: Non-Trusted Registry Usage Detection and Alerting**
    - **Description:** Alert the security organization whenever a workload resolves to a registry outside the approved list, identifying the image, the namespace or host running it, and the identity that deployed it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Record the deploying identity, since a service account suggests a broken pipeline and a person suggests something worse. Route alerts to the Operate pillar's incident handling. Handle known-benign sources by adding them to the approved list, not by suppressing alerts.

### AP-5.4: Registry Hygiene Report

**Design Intent:** Registry retention keeps every fielded release, the certified release before it for rollback, and every release baselined to the IL6 enclave. Other images expire on the ASP's schedule. A monthly report shows where the registry departs from those rules.

**NIST Control Mapping:**

- **CM-2(3) (partial):** retaining enough prior deployable versions for rollback, at the depth Application Rollback, Progressive Delivery, and Feature Flag Governance requires. It is partial because baseline and template artifacts are retained in the source platform.
- **SI-12 (partial):** the build-artifact retention slice, alongside Model Registry Hygiene Report, with program records management left to the Manage pillar.
- **Declined:** CM-2 is not reopened, since citing CM-2(3) claims only retention depth. SI-12(3) and MP-6 cover sanitization, the Data focus area's subject, while cleanup here is ordinary deletion.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Artifact/Model Registry, Container

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **AP-5.4.1: Stale/Orphaned Image Detection and Cleanup**
    - **Description:** For a repository with no retention window yet on record, decide the window and the minimum rollback depth, drawing the depth from Application Rollback, Progressive Delivery, and Feature Flag Governance's recovery-path requirement, document both in the ASP, and on a scheduled basis delete the images that no running deployment or tagged release references, that fall outside the window on record, and that no rollback target depends on.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the disposal half of the outcome's SI-12 (partial) mapping. Check references before age, so rollback targets survive. Compute reachability from Deployment Inventory Report's observed state, and remove an image together with its signature, SBOM, and attestations.

- **AP-5.4.2: Registry Retention Policy Compliance Reporting**
    - **Description:** Report registry contents against the program's documented retention rules, showing which repositories exceed their window, which have fallen below the minimum rollback depth, and what was removed in the period.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-2(3) (partial) mapping through the rollback-depth column. Document retention rules with the other release criteria rather than leaving them as tool settings. Report what was removed, since deleting a referenced item is otherwise silent.

### AP-5.5: Deployment Inventory Report

**Design Intent:** The deployment inventory reads the versions actually running in every prod spoke and the edge model versions each aircraft reports at connection. It compares them with what Certification to Field approved, so anything running that was never certified is flagged.

**NIST Control Mapping:**

- **CM-8(2) (partial):** keeping the inventory current from observed runtime state on the application-deployment axis. Asset Inventory and Discovery holds the device and platform axis, and Model Registry Hygiene Report holds model artifacts.
- **CM-8(3) (partial):** detecting unauthorized application versions on otherwise compliant hosts, which other discovery outcomes such as Asset Inventory and Discovery cannot see.
- **Declined:** CM-8 base and CM-8(1) are not reopened, and CM-8(4) stays with Resource Tagging and Ownership Strategy. CM-2 and CM-6(1) stay with Runtime Security Baseline, which checks settings rather than which release is present. CA-7 stays with Unified Vulnerability Dashboard.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-5.5.1: Deployed Version/Environment Inventory Collection**
    - **Description:** Collect the running application version, image digest, environment, and host or namespace from each deployment platform continuously, and write the result into the program's authoritative inventory as observed state held alongside the authorized record.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-8(2) (partial) mapping. Store observed and authorized state as separate fields, or the inventory mirrors drift instead of detecting it. Read the platform's API rather than the pipeline's record.

- **AP-5.5.2: Inventory Drift Detection**
    - **Description:** Compare observed deployment state against the authorized record on every collection cycle, and raise each unmatched version, unexpected environment, and missing deployment as a drift finding routed for disposition.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-8(3) (partial) mapping. Separate unauthorized versions, which route to incident handling, from authorized versions in the wrong place and silently vanished deployments. Never close drift by updating the authorized record to match.

### AP-5.6: Unified Vulnerability Dashboard

**Design Intent:** One dashboard combines every scanner's and tester's findings for each application, deduplicated and ranked by risk. The owning teams, the Security Team, and the PMO ISSE all work from it. The CSSP's analysts can read it through their host pool.

**NIST Control Mapping:**

- **RA-5(6) (full):** automated comparison of successive scan results, centralized for the focus area, with STIG results arriving through STIG Risk Tracking.
- **RA-5(10) (full):** correlating scanner output to find multi-vulnerability and multi-hop exposure. No other outcome claims either enhancement, while the scanning outcomes such as Container Scanning cite the RA-5 base.
- **CA-7 (partial):** status reporting for the application portfolio's vulnerability posture, alongside AMP Compliance Verification and others, with the Continuous Monitoring Plan (ConMon) holding strategy and metrics. Unlike Deployment Risk Threshold Evaluation's per-release score, this is the continuing view across everything fielded.
- **Declined:** RA-5(4) stays with External Attack Surface Management. The RA-5 base is not claimed, since this outcome performs no scanning.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, Compute, Database Service

**External Dependencies:** The CSSP, whose analysts read the dashboard through the CSSP host pool.

**Security Impact:** Moderate

**Activities:**

- **AP-5.6.1: Vulnerability Data Aggregation Across Scanning Tools**
    - **Description:** Ingest the machine-readable output of every scanning and testing outcome in the focus area into a common finding schema, normalized through SARIF for scan and test tool output and through the CycloneDX and VEX documents the dependency-scanning activities already produce, then deduplicate the findings that describe the same weakness in the same component and correlate across sources so exposure paths no single tool reports become visible.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Extensive
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-5(6) and RA-5(10) mappings. Resolve component identity through package URLs, CPEs, or image digests, and append results per run. Require SARIF output from tools, mapping native output where needed, and ingest CycloneDX SBOMs and VEX statements directly. The cross-ecosystem identity work makes this a multi-team build.

- **AP-5.6.2: Unified Risk Scoring and Prioritization View**
    - **Description:** Present the aggregated findings as a ranked view driven by exploitability, reachability, asset criticality, and remediation-clock status, so that the order the list is worked in reflects program risk rather than raw severity counts.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Reuse the weighting from Risk Scoring Model Definition rather than a second model. Make the top of the list resolve to a component, owner, and fix, reading criticality from Application Registration and Inventory Logging. Record that CISA KEV and EPSS need a documented in-enclave mirror when isolated, and that reachability is analyst judgment until instrumentation exists.

- **AP-5.6.3: Dashboard Access and Stakeholder Reporting**
    - **Description:** Give the PMO ISSE, ISSM, development teams, and the AO scoped access to the cut of the view each one needs, and issue a recurring posture report generated from the same data so the program's written status statements and its dashboard cannot disagree.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-7 (partial) mapping. Give developers their own components with fixes and the AO portfolio aging and trend. Scope access, since a ranked exploitable list is a targeting document, and generate reports from the store.

### AP-5.7: Runtime API Inventory and Governance

**Design Intent:** The DMZ's edge services and the cloud hub report every API endpoint actually answering requests. Each is compared with the schemas registered at intake, so an undocumented route or a retired version still answering is flagged to its owning team.

**NIST Control Mapping:**

- **SA-11(6) (partial):** reviews the undeclared interfaces API Security Testing defers here, tracked jointly with that outcome and Training Pipeline API/Interface Testing.
- **CM-7(1) (partial):** identifying undeclared HTTP routes and deciding their fate, a surface host and wire monitoring cannot see. Web Application Firewall holds the enforcement dimension of the same obligation through API Gateway Runtime Policy Enforcement.
- **Declined:** AC-3 and AC-6 stay with the Identity focus area, whose mechanisms the record names. The SC-5 family is not reopened, since this outcome enumerates rather than limits. CM-8(4) stays with Resource Tagging and Ownership Strategy. AC-4 governs cross-domain flows, not which interfaces exist.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** API/Interface Contract, Load Balancer/Reverse Proxy/API Gateway

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-5.7.1: Shadow/Undocumented API Discovery**
    - **Description:** Discover the API endpoints actually serving traffic by observing gateway, service-mesh, and load-balancer telemetry, and flag every route no published schema declares as an undocumented interface requiring disposition.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-11(6) and CM-7(1) mappings. Discover by observing traffic, and treat superseded API versions and rarely used routes as findings. Parse GraphQL operation names and resolve gRPC methods from the :path pseudo-header against the proto registry, so the inventory holds operations rather than single routes.

- **AP-5.7.2: API Inventory Enrichment**
    - **Description:** Record for each inventoried API its accountable owner, the classification of the data it carries, and the authentication and authorization method it enforces, drawing those values from the taxonomies the program already maintains rather than defining new ones.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Record owner, data handled, and authentication method, since each answers a question asked under time pressure. Point at the Data focus area's classification and Resource Tagging and Ownership Strategy's taxonomy rather than restating them. Record an unknown authentication method as a task, distinct from a confirmed absence, which is a finding.

### AP-5.8: Secrets Management Audit

**Design Intent:** The secrets present in every deployed environment are enumerated and reconciled against what each spoke's vault issued. A secret nobody issued, or one nothing has used since its last rotation, is flagged for removal.

**NIST Control Mapping:**

- **IA-5(7) (partial):** finds static authenticators in the deployed runtime, such as image layers, environment variables, mounted configuration, and job definitions, which source gates cannot see. It joins the jointly tracked group, with Secret Scanning holding the source gate.
- **Declined:** no IA-5 base claim is opened, because rotation runs through the Identity focus area's vault machinery.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Compute, Application and Service Account Identity

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-5.8.1: Runtime Secrets Inventory and Usage Audit**
    - **Description:** Enumerate every secret present in each deployed environment, reconcile the result against what the vault issued, and correlate each entry with vault access records so that unvaulted, orphaned, and idle credentials all become visible in one inventory.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(7) (partial) mapping. Reconcile against the vault, since a credential the vault never issued cannot be rotated on request. Enumerate the surfaces deployment adds, which keeps this distinct from Secret Scanning.

- **AP-5.8.2: Audit Finding Remediation and Rotation**
    - **Description:** Close each audit finding by rotating and revoking the exposed credential through the program's vault, moving the consuming workload onto a vault-issued reference, and retiring the credentials the usage audit shows nothing is calling.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Rotate rather than delete, since every clone, layer, backup, and log still holds the exposed value. Rotation runs through the Identity focus area's vault, while this activity owns disposition and verifying the consuming workload still works. Apply the same verification before retiring an idle credential.

### AP-5.9: Runtime Application Self-Protection (RASP)

**Design Intent:** RASP instruments every internet-reachable application, starting in monitor mode and moving to blocking once each application's rules are tuned. Today those applications are the analyst portal, the signals workbench, and the partner API. RASP events go to the security monitoring platform.

**NIST Control Mapping:**

- **SI-7(17) (partial):** in-process instrumentation enforcing policy is application self-protection at runtime. It is partial because client-side, mobile, and desktop software falls outside the focus area and is recorded as a gap, and neither Web Application Firewall nor host protection can see input reaching a query.
- **Declined:** SI-4 is not claimed, since this outcome enforces rather than adds a monitoring surface. SI-10 stays with the application, verified by API Security Testing and compensated by Web Application Firewall.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** First-Party/Custom Application Code, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-5.9.1: RASP Agent Deployment and Application Instrumentation**
    - **Description:** Deploy the runtime self-protection agent into each fielded application's runtime, verify continuously that it is loaded and reporting for every deployed instance, and treat an instance running without it as a coverage gap rather than a tolerated exception.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(17) (partial) mapping and rises to Level 1 wherever the tailored baseline includes the enhancement. Reconcile coverage against Deployment Inventory Report, since workloads deployed differently silently lack the agent. Treat the agent as a dependency and decide its fail-open or fail-closed behavior deliberately, and record unsupported runtimes.

- **AP-5.9.2: RASP Detection and Blocking Policy Definition**
    - **Description:** Define which detection classes the agent refuses outright, which it reports without interrupting the request, and which are suppressed, and record the policy and each per-application deviation with the program's other runtime baseline decisions in the ASP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Start in report-only mode and promote near-unambiguous classes to blocking first, such as unexpected deserialization types or path escapes. Route every block as a security event. The policy is a documented PMO ISSE risk decision, and it rises to Level 1 with its sibling wherever the tailored baseline includes SI-7(17).

### AP-5.10: Vulnerability Disclosure Program

**Design Intent:** KESTREL's internet-reachable endpoints are enrolled in the DoD Vulnerability Disclosure Program, which sets what researchers may test. Reports it relays reach the Security Team, which triages them and tracks each one to closure like a penetration test finding.

**NIST Control Mapping:**

- **RA-5(11) (full):** establishes the public vulnerability reporting channel, distinct from commissioned Penetration Testing. A funded bug bounty is a separate later decision, since a channel works without one.
- **Declined:** RA-7 is not claimed, since validated reports go through Vulnerability and Patch Management and Deployment Risk Threshold Evaluation. IR-6 is not claimed, because an exploited finding moves to the Operate pillar's incident process.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API

**External Dependencies:** The DoD Cyber Crime Center, which runs the DoD Vulnerability Disclosure Program.

**Security Impact:** Moderate

**Activities:**

- **AP-5.10.1: Vulnerability Disclosure Policy Publication and Researcher Intake Channel**
    - **Description:** Publish a disclosure policy naming the systems in scope, the testing a researcher is authorized to perform, the program's response commitments, and a monitored intake channel, operate that channel so a report reaches a named recipient rather than an unread mailbox, and document the policy in the ASP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-5(11) (full) mapping. Include a safe-harbor statement, or researchers will not report. Publish a security.txt file at the well-known path, and settle scope and authorization language with counsel and the PSO first.

- **AP-5.10.2: Reported Finding Triage and Disposition Workflow**
    - **Description:** Validate each received report against the fielded system within a defined acknowledgment and triage window, rate it using the program's existing severity scheme, and route confirmed findings into the same remediation and POA&M path an internally discovered finding takes.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Meet the published acknowledgment clock. Give every report a written disposition, including duplicates and rejections. Enter confirmed findings into the existing remediation register on the same terms as scanner findings.

- **AP-5.10.3: Researcher Acknowledgment and Coordinated Disclosure Timeline**
    - **Description:** Agree a disclosure date with the reporter at triage, keep them informed as remediation proceeds, and credit them at publication unless they decline.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Negotiate the disclosure timeline, since the reporter need not wait. A restricted program agrees early on what it can say rather than going quiet. Give credit, which costs nothing.

### AP-5.11: Compliance Evidence Collection Automation

**Design Intent:** The pipeline files every scan result, gate decision, approval record, attestation, and conformance report in one evidence store as it is produced. Each is tagged to its outcome and control. Certification to Field and the SCA both draw from that store rather than asking teams to gather evidence.

**NIST Control Mapping:**

- **CA-7(6) (partial):** automated collection keeping the Application focus area's monitoring results accurate, current, and available, tracked jointly with the Manage pillar's Compliance Evidence Collection and Retention. Control tagging records design intent and does not make an artifact compliance evidence.
- **Declined:** CA-5 and PM-4 belong to the Manage pillar and STIG Risk Tracking. CA-7(1) does not apply, since automated collection is not independent assessment. SI-12 retention belongs to the Manage pillar's repository.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API, Storage/Database

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-5.11.1: Automated Evidence Artifact Collection and Control Tagging**
    - **Description:** Collect each evidence artifact the focus area's capabilities emit at the moment it is produced, store it with the release, environment, and timestamp it describes, and tag it to the control or controls that artifact supports.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-7(6) (partial) mapping. Collect at production time, since evidence regenerated before an assessment proves only that the tool runs. Derive tags from the outcomes' NIST Control Mapping values, and store artifacts immutably with context.

- **AP-5.11.2: Evidence Freshness/Staleness Tracking**
    - **Description:** Assign each evidence type a validity window derived from the cadence of the activity that produces it, and flag every artifact and every control whose most recent artifact has passed that window.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the currency dimension of the outcome's CA-7(6) (partial) mapping. Signal staleness at the control level, reading validity windows from each producing activity's ConMon Activity value. Report controls with no artifact separately, as the more serious state.

- **AP-5.11.3: Evidence Export Pipeline**
    - **Description:** Export the tagged, current evidence set in a structured format the program's traceability artifact and its assessors consume directly, on a defined cadence and on demand ahead of an assessment.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The export hands design-intent mappings and artifacts to the traceability artifact, which the SABER is not. Use OSCAL so the SSP tooling and assessors consume it without transcription. Keep the flow one-way and correct at the source.

### AP-5.12: Fielded Dependency Vulnerability Monitoring

**Design Intent:** Every fielded release's SBOM is matched daily against new vulnerability disclosures. A newly vulnerable dependency opens a ticket to the owning team with the VPMP's deadline, and the fix ships as a rebuilt release through the normal pipeline.

**NIST Control Mapping:**

- **SI-2 (partial):** covers third-party libraries embedded in first-party code, a population Vulnerability and Patch Management leaves silent. It is partial because deployment and program-wide exception handling remain with that outcome.
- **RA-5 (partial):** the fielded dependency scanning surface, held alongside Dependency Review and Container Scanning and disjoint by lifecycle stage. The base is cited for the reason those slices give.
- **Declined:** SR-3 and SR-5(2) stay with Dependency Review, since this outcome re-scans already admitted components.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Third-Party Dependency (Embedded Library/Package), Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **AP-5.12.1: Continuous Dependency Vulnerability Rescanning**
    - **Description:** Re-scan the resolved dependency set of every fielded application against current vulnerability data on a recurring cadence, independent of any pull request or release event, and route each newly-disclosed finding to Dependency Patch Timeframe Policy's clock.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-5 (partial) mapping. Scan the resolved transitive set, not the declared manifest. Feed findings to Unified Vulnerability Dashboard and route them to Dependency Patch Timeframe Policy for a remediation clock.

- **AP-5.12.2: Dependency Patch Timeframe Policy**
    - **Description:** Set by severity the maximum time a newly-disclosed vulnerable dependency version may remain in a fielded application before it is remediated, and document the resulting timeframes in the VPMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-2 (partial) mapping by setting the remediation period Continuous Dependency Vulnerability Rescanning findings are measured against. It parallels Patch/Vulnerability Remediation SLA Policy with severity-tiered timeframes.

## AP-6: Application Security Planning

### AP-6.1: Application Security Plan (ASP)

**Design Intent:** The PMO ISSE authors KESTREL's ASP, since it sets the Certification to Field thresholds, and the Platform Team writes the pipeline sections. The Security Team reviews it, and the Configuration Control Board approves it. It is revised each year and whenever a threshold or the coding standard changes.

**NIST Control Mapping:**

- **SA-15 (partial):** claimed for periodic review of the complete documented development process, standards, and tools as one package. The contributing outcomes, such as Secure Coding Standard Definition, hold their own SA-15 slices, and the claim is tracked jointly.
- **Declined:** CM-9 belongs to the Configuration Management Plan (CMP). PL-2 belongs to the System Security Plan (SSP). SA-3 is not reopened, since this plan compiles standards rather than performing lifecycle stages.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **AP-6.1.1: ASP Development and Authoring**
    - **Description:** Author the Application Security Plan, consolidating the non-functional security requirements, threat modeling methodology, secure coding and component standards, license and provenance criteria, release risk-scoring model, and runtime hardening and disclosure policy produced across the focus area's capabilities into a single governing document.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Consolidate the determinations from the focus area's capabilities, such as Secure Coding Standard Definition and Risk Scoring Model Definition, once they exist. This activity carries no independent claim, since SA-15 rests on ASP Periodic Review and Revision.

- **AP-6.1.2: ASP Review and Approval**
    - **Description:** Route the drafted ASP through stakeholder review and secure formal approval from the accountable authority before it takes effect.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent claim. Fix the plan's distribution and modification rights at approval, since it gathers coding standards, approved components, and release thresholds in one place.

- **AP-6.1.3: ASP Periodic Review and Revision**
    - **Description:** Review the ASP on a defined cadence and revise it to reflect changes in the program's secure coding standards, approved component catalog, threat landscape, or governing requirements.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-15 (partial) periodic-review claim. Review the whole process, standards, and tools package on a fixed cadence, keeping the plan current as its source determinations change.
