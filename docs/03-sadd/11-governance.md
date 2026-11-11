# GV: Governance

*KESTREL SADD, Section 5 (Manage). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## GV-1: Security Governance Structure

### GV-1.1: Security Policy Framework

**Design Intent:** KESTREL's policy tier is one system security policy that the program manager issues beneath DoD issuances and the parent organization's enterprise policy. Its standards are the governing plans this SADD names, namely the AMP, CMP, VPMP, ASP, AISP, DMP, KMP, IRP, CP, and SCRM. Its procedures are the runbooks beneath them. Each policy statement maps to the control families it satisfies, and the policy applies to everyone and everything inside the boundary.

**NIST Control Mapping:**

- **PM-1 (partial):** claimed for the program plan's structure and its description of program management and common controls, which the policy hierarchy and control-family mapping produce. Security Roles and Responsibilities holds the roles clause, and Policy Lifecycle Management holds review and update.
- **AC-1 (partial):** the policy tier, paired with the Identity focus area's Account Management Plan (AMP), which holds the procedures.
- **CM-1 (partial):** paired the same way with the Device and Infrastructure focus area's Configuration Management Plan (CMP).
- **RA-1 (partial), SI-1 (partial):** both paired with the Device and Infrastructure focus area's Vulnerability and Patch Management Plan (VPMP), which holds both families' procedures.
- **SC-1 (partial):** paired with the Data focus area's Key Management Plan (KMP).
- **MP-1 (partial):** paired with the Data focus area's Media Protection Policy and Procedures.
- **IR-1 (partial):** paired with the Response focus area's Incident Response Plan (IRP).
- **CP-1 (partial):** paired with the Recovery focus area's Contingency Plan (CP).
- **AT-1 (partial), AU-1 (partial), CA-1 (partial), IA-1 (partial), PL-1 (partial), SA-1 (partial), SR-1 (partial):** claimed for the policy tier alone, with each family's procedures half held by its owning plan or outcome elsewhere in the framework.
- **MA-1 (partial):** the policy tier, while the Device and Infrastructure focus area's Controlled Maintenance and Support holds the procedures half.
- **Declined:** PE-1 and PS-1 belong to the PSO and sit outside the SABER's scope. PT-1 is left to the Compliance focus area's Privacy Program Charter and Policy Development.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The parent organization, whose enterprise security policy KESTREL's policy sits beneath.

**Security Impact:** Moderate

**Activities:**

- **GV-1.1.1: Policy Framework Structure Definition**
    - **Description:** Define the tiered structure of the program's security documentation, fixing what a policy, a standard, and a procedure each are, which authority approves each tier, and how a document at one tier cites the tier above it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Keep standards and procedures distinct, since a standard states an assessable mandatory value while a procedure states steps. Machine-enforceable policy belongs to Policy-as-Code Implementation for Machine-Enforceable Policies Where Applicable.

- **GV-1.1.2: Policy-to-Control Mapping**
    - **Description:** Map each policy and standard in the framework to the AO-approved tailored control families and controls it satisfies, and record the mapping so that a change to the tailored control set identifies the policies that must change with it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This mapping starts at the AO-tailored control set and asks which policy covers each family, so a family with no policy surfaces as a gap. Re-run it when the AO retailors the control set or applies an overlay.

- **GV-1.1.3: Policy Taxonomy and Scope/Applicability Definition**
    - **Description:** Classify every document in the framework under a defined taxonomy, and write the scope and applicability statement that names which systems, enclaves, environments, and personnel populations each policy binds.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Name the control-system enclave and the air-gapped enclave explicitly rather than leaving them to a general clause. Otherwise a statement written around the enterprise IT estate leaves them governed by nothing.

### GV-1.2: Security Roles and Responsibilities

**Design Intent:** The roles are the AO and the program manager for the government, and the PMO ISSE, who owns the security design and Certification to Field. The performer ISSM owns the authorization package, and the ISSOs own day-to-day compliance. The SCA assesses, the PSO owns personnel and physical security, and each team lead owns their team's systems. A responsibility matrix in the SSP records who decides what. It is reviewed each year and on any change of role holder.

**NIST Control Mapping:**

- **PM-1 (partial):** claimed for the clause requiring the program plan to identify and assign roles and coordination, which Security Policy Framework's PM-1 claim leaves here while it holds the rest.
- **PM-2 (partial):** claimed for defining and assigning roles, while ISSO/ISSM Appointment Letters issues the instrument that confers them. Neither satisfies the control alone, so the other slice is held there.
- **Declined:** PS-2 belongs to the PSO, since position risk designation is not what this outcome records.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-1.2.1: Role Definition for Security Functions**
    - **Description:** Define each security function the program requires, including the ISSO, ISSM, ISSE, SCA, and AO roles the program's authorization framework names, stating for each its accountabilities, its decision authority, and the clearance or qualification it presumes.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Define what each role decides, such as which of the ISSM and the ISSE signs off on a design change. Roles the PSO owns are named here only as interfaces.

- **GV-1.2.2: Role Assignment and RACI/Responsibility-Matrix Documentation**
    - **Description:** Bind every defined security function to a named position in a responsibility matrix that separates who performs each activity from who approves, is consulted on, and is informed of it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Bind roles to positions rather than individuals so the matrix survives job changes. Resolve any cell where one party is both responsible and accountable for a security decision before assessment.

- **GV-1.2.3: Roles and Responsibilities Periodic Review**
    - **Description:** Review the role definitions and the responsibility matrix on the program's defined cadence and after any reorganization, contract change, or boundary change, correcting assignments that no longer match how the program operates.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Look for unowned activities that fell between positions during a reorganization. A gap that reassignment cannot close goes to the Risk focus area's risk register.

### GV-1.3: ISSO/ISSM Appointment Letters

**Design Intent:** The AO appoints the performer ISSM, and the ISSM appoints each ISSO, each by a signed letter. Each letter names the person, the role, the KESTREL boundary it covers, the authority it confers, and its effective date. The ISSM tracks every letter and reissues it whenever a role holder or the boundary changes, such as when the alternate site was added.

**NIST Control Mapping:**

- **PM-2 (partial):** holds the conferral slice, since the letter is the instrument that performs the appointment, while Security Roles and Responsibilities holds definition and assignment. A senior official's letter appointed above the program is filed here rather than reissued.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-1.3.1: Appointment Letter Template Development**
    - **Description:** Develop the appointment letter template, fixing the fields every letter must carry, namely the individual, the role, the system or boundary the appointment covers, the authority conferred, the responsibilities accepted, the effective date, and the signatures of both the appointing official and the appointee.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Make sure the template names the covered boundary, since that is the question an assessor asks. Keep the appointee's signature line, because an unsigned letter records intent rather than acceptance.

- **GV-1.3.2: Appointment Letter Issuance and Tracking**
    - **Description:** Issue a signed letter for every security role the responsibility matrix assigns, and maintain a register recording each letter's holder, role, covered boundary, effective date, and current status.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the conferral half of the outcome's PM-2 (partial) mapping. Reconcile the register against Role Assignment and RACI/Responsibility-Matrix Documentation, and let the register govern on who currently holds a role.

- **GV-1.3.3: Appointment Letter Renewal/Update on Personnel Change**
    - **Description:** Reissue or terminate the affected letters whenever an appointee departs, changes position, or has their covered boundary or authority changed, and update the register within the period the program sets.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Wire departures to this activity through the same personnel trigger as the Identity focus area's Deprovisioning-on-Termination Automation, so a lapsed letter does not stay in force. Issue an interim appointment where a role would otherwise sit vacant.

### GV-1.4: Security Governance and Steering Committee

**Design Intent:** The program manager chairs a monthly security steering committee of the chief engineer, the PMO ISSE, the ISSM, the team leads, and the intelligence mission leads. It settles cross-team disputes, risk questions above the Configuration Control Board, and schedule conflicts with security work. Its decisions and actions are tracked in the service desk, and a leadership dashboard shows the program's security posture each month.

**NIST Control Mapping:**

- **PM-29 (partial):** claimed for establishing a risk executive function with an organization-wide view. Appointing the Senior Accountable Official for Risk Management happens above the program, so the claim stays partial.
- **PM-6 (partial):** claimed for the program-level leadership measures the dashboard reports, while the Risk and Compliance focus areas' posture dashboards hold the other feeder views.
- **Declined:** PM-9 belongs to the Risk focus area, whose thresholds this committee consumes. PM-31 belongs to the Compliance focus area's Continuous Monitoring Plan (ConMon). CA-7 is held across the Protect and Operate pillars, and this outcome performs no assessment. Program posture reporting is better described by PM-6.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-1.4.1: Committee Charter and Membership Definition**
    - **Description:** Charter the committee, stating its purpose, scope, standing membership by position, quorum, and its relationship to the AO, the ISSM, and the program's other decision forums.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** State membership by position. Name the authorities the AO retains, so the committee does not make decisions that later have to be unwound.

- **GV-1.4.2: Meeting Cadence and Decision-Authority Definition**
    - **Description:** Set the committee's standing meeting cadence and the out-of-cycle escalation path, and define which decisions it makes itself, which it recommends to the AO, and what risk-level, cost, or schedule threshold moves a decision from one tier to the other.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the substance of the outcome's PM-29 (partial) mapping. Align thresholds to the Risk focus area's Tolerance-to-Acceptance-Authority Tier Alignment, letting the risk tolerance statement govern on conflict, and define an escalation path between meetings.

- **GV-1.4.3: Governance Decision/Action Item Tracking**
    - **Description:** Record every committee decision and action item with its owner, due date, and current status, and carry open items forward to each subsequent meeting until they close.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Record each decision so an ISSE can point at the authority behind an architecture choice later. Hand items that resolve into accepted risk to the Risk focus area's Risk Acceptance Documentation and Expiration Tracking so they inherit an expiration date.

- **GV-1.4.4: Security Program Metrics/Posture Dashboard for Leadership Reporting**
    - **Description:** Build the leadership-facing dashboard that reports the program's security posture measures, drawing its figures from the risk register, the POA&M, compliance status, the AI/ML governance estate, and the Operate pillar's detection and response feeds rather than recomputing them.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-6 (partial) mapping. It aggregates the Risk and Compliance focus areas' posture dashboards and the AI/ML Governance Posture Report rather than recomputing them, so leadership never gets two answers. It is Level 2 because a periodic written report can meet PM-6.

### GV-1.5: Configuration Control Board

**Design Intent:** The chief engineer chairs the Configuration Control Board. Its members are the PMO ISSE, the ISSM, the Platform Team lead, Fleet Operations' operations lead, and the lead of any team whose change is on the agenda. It meets weekly. It approves changes to the hubs' rule base, the identity provider, interconnections, and every governing plan, and it sends significant changes through Security Impact Analysis. Its decisions are logged with their rationale.

**NIST Control Mapping:**

- **CM-3 (partial):** claimed for the coordination clause, a board that oversees configuration change control at a defined frequency. Asset Lifecycle Change Control, Network Resource Configuration Governance, and System Prompt Governance hold the other clauses, namely review and approval for their asset classes, so one board coordinates all three.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Storage/Database, Application/API, Routing/Switching Fabric, Network Firewall, Prompt/Instruction Layer

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-1.5.1: Board Charter and Membership Definition**
    - **Description:** Charter the configuration control board, stating its purpose, scope, standing membership by position, quorum, and the authority threshold above which a change escalates to the Security Governance and Steering Committee or the AO.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** State membership by position, and include the asset owners and technical leads alongside the ISSM or ISSE. Set the escalation threshold so the board neither rubber-stamps program-wide risk nor refers routine changes upward.

- **GV-1.5.2: Meeting Cadence and Coordination Scope Definition**
    - **Description:** Set the board's standing meeting cadence and the out-of-cycle path for changes routed through the Emergency Change Process, and name the asset-scoped review processes that route their changes through the board's coordination, including Asset Lifecycle Change Control, Network Resource Configuration Governance, and the Artificial Intelligence focus area's System Prompt Governance.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the substance of the outcome's CM-3 (partial) mapping. Size the cadence to change volume so the emergency path does not absorb the load, and name which processes route through the board.

- **GV-1.5.3: Board Decision and Escalation Log**
    - **Description:** Record every change the board coordinates or escalates, its disposition, and the asset-scoped process it originated from, distinct from the individual change records Asset Lifecycle Change Control and Network Resource Configuration Governance each keep.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This log is the board's own oversight record, separate from the asset-scoped change logs, and shows the coordination clause is exercised in fact. It is Level 2 because the charter and cadence activities carry the mandatory obligation.

### GV-1.6: Zero Trust Maturity Assessment and Roadmap

**Design Intent:** The PMO ISSE assesses KESTREL against the DoW zero trust reference architecture's pillars each year, with target level as the goal on the department's timeline. The gaps become a roadmap in the Security Implementation Plan, and progress is reported to the steering committee each quarter.

**NIST Control Mapping:**

- **Declined:** no control covers maturity self-assessment or roadmapping against an external reference architecture. PM-7 and PL-8 cover the program's own architecture, held by the Security Architecture and Design Document (SADD). CA-2 covers control assessment, held by the Compliance focus area. SA-8 is held by the Application focus area's Security Requirements Definition. The gaps this outcome finds become work in cited Protect and Operate outcomes.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API

**External Dependencies:** The DoW CIO, whose zero trust strategy and reference architecture set the target.

**Security Impact:** Moderate

**Activities:**

- **GV-1.6.1: Zero Trust Maturity Self-Assessment**
    - **Description:** Assess the program's current maturity against each pillar of the DoW zero trust reference architecture, evidencing every rating from the Protect and Operate pillars' implemented outcomes rather than from opinion.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Have each pillar score name the implemented outcomes behind it. Record isolated-enclave ratings with a scoped deviation rather than scoring them against capabilities the environment cannot host.

- **GV-1.6.2: Target-Level Gap Identification and Roadmap Development**
    - **Description:** Compare the current maturity assessment against the target level the program is required to reach, and sequence each resulting gap into a roadmap entry with an owner, its dependencies, and a target date.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Express each gap as a named Protect or Operate outcome that is missing or partial, so the roadmap entry becomes the issue-tracker story. Send unfunded gaps to the Risk focus area's risk register with a review date.

- **GV-1.6.3: Roadmap Progress Tracking and Reassessment**
    - **Description:** Track roadmap entries to closure and re-run the maturity assessment on the program's defined cadence, updating the roadmap to reflect delivered capability and any revision to the target level.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Reassess against the current DoW target level, since that target moves. Report progress to the Security Governance and Steering Committee through its posture dashboard.

## GV-2: Policy and Awareness

### GV-2.1: Policy Lifecycle Management

**Design Intent:** Policies and plans are written and versioned in the program's document repository, reviewed by the ISSM, and approved by the Configuration Control Board. Each is reviewed every year, and earlier when an incident, assessment, or significant change calls for it. Superseded versions are retired and archived. Policies a machine can enforce, such as the hub rule base, admission rules, and landing zone guardrails, are written as policy as code.

**NIST Control Mapping:**

- **PM-1 (partial):** claimed for the periodic review, update, and protection of the policy, while Security Policy Framework holds the rest of the control.
- **Declined:** the review-and-update clause of AC-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MP-1, PL-1, RA-1, SA-1, SC-1, SI-1, and SR-1 is discharged here in support of Security Policy Framework's claims, not claimed again. SI-12 belongs to Compliance Evidence Collection and Retention. CM-3 covers system changes, not document changes. No control covers authoring machine-enforceable policy.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-2.1.1: Policy Drafting/Authoring Workflow**
    - **Description:** Define the workflow by which a new or revised security policy is drafted, naming the author, the required contributors, the template each tier uses, and the coordination a draft completes before it enters formal review.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Use a template so every policy states scope, applicability, and enforcement consequence the same way. Draft against the tiers fixed by Policy Framework Structure Definition.

- **GV-2.1.2: Policy Review and Approval Cadence**
    - **Description:** Set the review cadence each policy tier is held to and the event triggers that force an off-cycle revision, and fix the approval authority that must sign a document at each tier before it takes effect.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the review-and-update half of the outcome's PM-1 (partial) mapping. Name event triggers explicitly, such as a boundary change, re-categorization, AO retailoring, or serious incident. Route approval to the authority the structure definition assigns to that tier.

- **GV-2.1.3: Policy Retirement/Supersession Process**
    - **Description:** Establish how a policy is retired or superseded, requiring the superseding document to name what it replaces, the retired version to be withdrawn from circulation, and an archived copy to be retained for the period the program sets.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Retirement prevents two versions of one requirement being in force at once. Withdraw superseded copies from shared drives and wikis too, and archive them so the program can show which rule applied on a given date.

- **GV-2.1.4: Policy Publication and Version Control**
    - **Description:** Publish approved policies to a version-controlled, access-controlled repository every bound population can reach, recording each document's version, effective date, approving authority, and change history.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the protection half of the outcome's PM-1 (partial) mapping, which controls who may publish. Give each isolated or control-system enclave its own distribution path and a way to show its copy is current.

- **GV-2.1.5: Policy-as-Code Implementation for Machine-Enforceable Policies Where Applicable**
    - **Description:** Express the subset of policy statements a system can evaluate, such as required configuration values, permitted regions, and mandatory tagging, as version-controlled code that enforcement points consume directly rather than as prose an engineer transcribes.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Policy-as-code is the named practice behind the Automate tag, and it carries no control citation. Encode only statements with a checkable value that trace to an approved policy. It does not apply to fielded controllers, where IT/OT Zone and Conduit Segmentation (IEC 62443) carries the machine-enforceable slice.

### GV-2.2: Policy Exception Management

**Design Intent:** A team requests an exception through the service desk, naming the requirement, the reason, the compensating measures, and an end date. The ISSM assesses the risk. Exceptions that affect a control in the authorization go to the AO, as CCSD tailoring action 3 did. Expired exceptions alert the ISSM, and exception trends are reported to the steering committee each quarter.

**NIST Control Mapping:**

- **Declined:** no control takes exception management as its subject. CA-5 and PM-4 are the POA&M, reserved for the Risk focus area's Plan of Action and Milestones (POA&M), and an expired exception is handed there. CM-6 covers configuration deviations held by Identity and Application outcomes, which are recorded in this register. PM-9 belongs to the Risk focus area.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-2.2.1: Exception Request and Risk-Based Approval Workflow**
    - **Description:** Define the exception intake, requiring each request to cite the specific policy requirement being deviated from along with its justification, scope, proposed compensating measures, and requested duration, and route it to an approval authority tiered by the risk the deviation creates.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Require each request to name a specific requirement and a duration. Align approval tiers to the Risk focus area's Tolerance-to-Acceptance-Authority Tier Alignment, and route requests above tolerance to Risk Acceptance Process.

- **GV-2.2.2: Exception Tracking and Expiration Enforcement**
    - **Description:** Maintain the register of granted exceptions with each entry's owner, scope, compensating measures, and expiration date, and act at expiry by requiring remediation, re-justification, or escalation rather than letting the entry lapse unnoticed.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Notify the owner and approving authority ahead of expiry so remediation, re-justification, or escalation is a deliberate choice. Send an exception renewed more than once to the Security Governance and Steering Committee.

- **GV-2.2.3: Exception Trend Reporting**
    - **Description:** Report the exception population on a defined cadence by requirement, control family, owning organization, age, and renewal count, so that concentrations of deviation surface as a design signal rather than as a series of individual approvals.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Group the report by requirement rather than requester, since repeated exceptions to one control indicate a problem with the control. Feed it into Security Program Metrics/Posture Dashboard for Leadership Reporting. It is Level 2 because the register and expirations meet the mandatory obligation.

### GV-2.3: Security Awareness and Training Program

**Design Intent:** Every person with access completes DoD cyber awareness and CUI training before getting an account, and each year after. Privileged users and security roles also meet DoDM 8140.03 qualification for their work roles. The parent organization's and performer's email systems run phishing exercises. KESTREL tests IT Operations against pretexted account-reset requests. The identity provider suspends any account whose training has lapsed.

**NIST Control Mapping:**

- **AT-2 (full):** the only claim of the control in the framework, since this outcome is the only place a general literacy training obligation is discharged.
- **AT-2(1) (full):** carried by Simulated Social Engineering Exercise, which runs a simulated-event exercise as part of literacy training.
- **AT-2(2) (full):** insider threat indicators are baseline curriculum content, and reports go to User/Entity Behavior Analytics (UEBA) / Insider Threat Detection.
- **AT-2(3) (full):** social engineering and social mining are baseline curriculum content.
- **AT-2(4) (full):** suspicious communications and anomalous system behavior are baseline curriculum content.
- **AT-3 (full):** the program's general role-based training obligation, which the Response focus area's Incident Response Team Structure and Training and other pillars' specialized instruction feed.
- **AT-4 (full):** covers documenting, monitoring, and retaining individual training activity.
- **AT-1 (partial):** the procedures half, held through the curricula, cadence, and enforcement documented here, while Security Policy Framework holds the policy tier.
- **Declined:** AT-2(5) and AT-2(6), if tailored in, add content to this curriculum. AT-3(1) and AT-3(2) belong to the PSO. AT-3(3) runs under the Response focus area's IR-3(3) claim. AT-3(5) belongs to the Compliance focus area's Privacy Program Management.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The parent organization and the performer, whose enterprise email systems run the phishing exercises.

**Security Impact:** Moderate

**Activities:**

- **GV-2.3.1: Baseline Security Awareness Training**
    - **Description:** Deliver the general literacy training every person with system access completes at onboarding and annually thereafter, covering the program's rules of behavior, its reporting paths, and the recognition of social engineering, insider threat indicators, and anomalous system behavior.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AT-2, AT-2(2), AT-2(3), and AT-2(4) claims. Refresh content on the program's cycle and after any incident a user could have recognized. Host the course locally for isolated enclaves.

- **GV-2.3.2: Simulated Social Engineering Exercise**
    - **Description:** Run a simulated phishing or social-engineering exercise against the user population on a defined cadence, and target follow-up training at the individuals and units each round identifies rather than revising the general curriculum alone.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AT-2(1) (full) mapping. It is not tagged Automate, since a scripted platform still assesses human judgment. Feed results into Baseline Security Awareness Training and Training Completion Tracking and Enforcement so repeat failures get targeted refreshers. It is Level 2 because the baseline curriculum meets AT-2 on its own.

- **GV-2.3.3: Role-Based Specialized Training**
    - **Description:** Establish and run the role-based curricula the program's higher-consequence populations complete before their role is authorized and on the cycle thereafter, covering privileged administrators, developers, control-system operators, and the personnel who build and operate the program's models.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AT-3 (full) mapping. Deliver other pillars' specialized instruction as curricula here, and have each curriculum ready before the role is filled. Write content for control-system operators and model developers against what they actually touch.

- **GV-2.3.4: Training Completion Tracking and Enforcement**
    - **Description:** Track individual completion of the baseline and role-based curricula against the program's access roster, retain the records for the period the program sets, and apply the access consequence that policy defines when the obligation goes unmet.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AT-4 (full) mapping. Reconcile completions against the access roster, not the learning platform's roster, to find people who never enrolled. Enforce non-completion through account suspension in the Identity focus area's account lifecycle machinery.

### GV-2.4: Rules of Behavior and Acceptable Use Policy

**Design Intent:** Every user acknowledges KESTREL's rules of behavior before an account is issued, and again each year. Privileged users sign additional privileged rules, and partner users sign the partner rules their nation's agreement requires. The identity provider records each acknowledgment, and a missing or expired one suspends the account. Violations go to the ISSM and, where they suggest insider risk, to the PSO.

**NIST Control Mapping:**

- **PL-4 (full):** Rules of Behavior Drafting and Publication establishes the rules, and User Acknowledgment Collection and Tracking collects acknowledgments before access and on revision. Policy Lifecycle Management sets the review cadence.
- **PL-4(1) (full):** the acceptable use half covers social media, external sites, public posting, and use of organizational identifiers on external accounts. Drop the claim if the rules omit that content.
- **Declined:** PS-6 and PS-8 belong to the PSO, while PL-4, claimed above, covers the rules themselves. AC-8 is claimed by the Identity focus area's User Authentication Controls through System Use Notification Banner Configuration. PL-1 is held by Security Policy Framework.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-2.4.1: Rules of Behavior Drafting and Publication**
    - **Description:** Write the rules of behavior and their acceptable use provisions, stating the responsibilities and expected behavior for information and system usage, the restrictions on external sites, social media, and public posting, and the prohibition on reusing organization-issued identifiers and authenticators elsewhere, then publish them where every bound population can reach them.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the establish-and-provide element of the outcome's PL-4 (full) mapping and the whole of its PL-4(1) claim. Keep the document short enough that users actually read it. Publish through Policy Lifecycle Management's repository so each acknowledged version can be identified.

- **GV-2.4.2: User Acknowledgment Collection and Tracking**
    - **Description:** Collect a documented acknowledgment from each individual that they have read, understood, and agree to abide by the rules before their access is authorized, and re-collect it on the program's defined cycle and whenever the rules are revised.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the acknowledgment and re-acknowledgment elements of the outcome's PL-4 (full) mapping. Place acknowledgment inside the Identity focus area's provisioning path, and record which version each person acknowledged. Watch for vendor engineers and control-system operators onboarded outside the enterprise process.

- **GV-2.4.3: Non-Acknowledgment/Violation Escalation Workflow**
    - **Description:** Define the escalation path for an individual who has not acknowledged the rules within the required period or is found to have violated them, naming the access consequence, the security-side referral, and the point at which the matter leaves the security organization.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** The security organization withholds or suspends access and refers the matter, while sanctions run through the PSO. Hand deliberate misuse to User/Entity Behavior Analytics (UEBA) / Insider Threat Detection. Give non-acknowledgment an access consequence rather than an endless reminder sequence.

## GV-3: Third-Party and Supply Chain Governance

### GV-3.1: Vendor Security Risk Assessment

**Design Intent:** Every supplier answers a security questionnaire before contract award. Suppliers are tiered by what they can reach. Tier 1 covers anyone touching the fleet, mission data, or keys, such as the cloud provider, the aircraft manufacturer, and the payload vendors. Tier 1 suppliers are reassessed each year and the rest every three years. Findings are tracked to closure. Every self-hosted third-party product is registered in the asset inventory once its assessment passes.

**NIST Control Mapping:**

- **PM-30(1) (partial):** claimed for prioritizing and assessing critical suppliers, while Supply Chain Risk Assessment and Dependency Mapping holds the identification half.
- **SR-6 (partial):** claimed for the general supplier population, while three Artificial Intelligence focus area outcomes hold the other slices, namely model, labeling, and foundation-model API suppliers. The base is cited because SR-6(1) covers testing delivered elements, not supplier review.
- **CM-8 (partial):** claimed for self-hosted third-party and vendor-hosted applications, while the Application focus area's Application Registration and Inventory Logging holds the first-party rest.
- **Declined:** SA-9 is held by Contract Security Requirements and the Artificial Intelligence focus area's foundation-model API outcome. CA-5 and PM-4 are reserved for the Risk focus area's Plan of Action and Milestones (POA&M).

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device, Self-Hosted Third-Party Application (COTS)

**External Dependencies:** The payload vendors, the aircraft and ground equipment manufacturers, the service desk vendor, the cloud provider, the CSSP, and the other suppliers in the vendor population.

**Security Impact:** Moderate

**Activities:**

- **GV-3.1.1: Vendor Security Questionnaire/Assessment Process**
    - **Description:** Establish the security questionnaire and assessment process every vendor completes before onboarding, fixing the questions asked, the evidence and attestations accepted in place of an answer, the reviewer who adjudicates the response, and the disposition that lets an engagement proceed, and record the questionnaire and process in the SCRM.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the assessment element of the outcome's SR-6 (partial) mapping. Name which audit reports or certifications substitute for which questionnaire sections, and ask about foreign ownership, control, or influence and subordinate suppliers from the first version. This activity only records FOCI status and any DCSA mitigation instrument as a tiering input, since the PSO and DCSA own the determination.

- **GV-3.1.2: Vendor Risk Tiering and Periodic Reassessment**
    - **Description:** Define the criteria that place each vendor in a risk tier, covering the sensitivity of the data it handles, the access its products or personnel hold, and the mission consequence of its failure, then set the reassessment frequency each tier carries so the highest-consequence suppliers are revisited on a schedule rather than at renewal, and record the tiering criteria and reassessment frequencies in the SCRM.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the recurring-review element of the outcome's SR-6 (partial) mapping and the prioritization element of its PM-30(1) (partial) mapping. Tier by access rather than contract value. Reassess on the tier's cadence, not at contract renewal.

- **GV-3.1.3: Vendor Assessment Findings Remediation Tracking**
    - **Description:** Record every finding an assessment or reassessment returns with its severity, the vendor commitment and date attached to it, and its current state, and escalate a finding the vendor will not or cannot close to the risk decision that either accepts it or ends the engagement.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Close each finding as a vendor fix, a compensating control, an accepted risk through the Risk focus area's Risk Acceptance Process, or a decision not to use the vendor. Findings that recur across vendors belong in the Contract Security Requirements clause library.

- **GV-3.1.4: Third-Party Application Registration in Authoritative Inventory**
    - **Description:** Register each self-hosted third-party or vendor-hosted application the program adopts in the program's authoritative inventory once its vendor assessment and risk tier are recorded, capturing the vendor, the product name and version, the endpoint or environment it is reached through, its accountable owner, mission criticality, and classification, and linking to its vendor risk tier, its composition record, and its contractual terms rather than restating them.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries a further disjoint slice of the outcome's CM-8 (partial) mapping, namely the self-hosted third-party and vendor-hosted application population. Register the application when the vendor assessment and tier are recorded, not as a separate step. Link the record to the vendor tier, the Application focus area's Vendor SBOM Intake record, and the Standard Security Clause Library terms rather than copying them.

### GV-3.2: Contract Security Requirements

**Design Intent:** The clause library carries DFARS 252.204-7012 and the CMMC clauses, the cloud computing clause, and SBOM delivery. It also carries vulnerability disclosure, incident reporting timelines, and data rights terms for each payload vendor. The supply chain lead verifies that each contract carries the clauses its tier requires and that the prime contract flows them down to subcontractors. The performer's CMMC Level 2 status covers CUI held on its laptops, and it is rechecked at each renewal.

**NIST Control Mapping:**

- **SA-1 (partial):** the acquisition family's procedures half, while Security Policy Framework holds the policy tier.
- **SA-4 (partial):** claimed for the contractual instrument and the documentation, responsibility-allocation, and acceptance-criteria clauses. The Application focus area's Security Requirements Definition and Model Selection and Justification hold the rest, namely the requirement content. Per-acquisition enhancements are tailoring choices in the clause library, and SA-4(1), SA-4(2), and SA-4(8) stay uncited until it carries them as standing clauses.
- **SA-9 (partial):** claimed for provider compliance clauses, oversight roles, and monitoring of the general provider population. Narrower populations are held by the Artificial Intelligence, Application, and Identity focus areas and by Inherited Control Validation.
- **SR-3(3) (full):** sub-tier flow down is exactly the flow-down verification activity. The base SR-3 is held by Supply Chain Risk Assessment and Dependency Mapping.
- **SR-5 (partial):** claimed for the contract tools element, while Hardware and Firmware Provenance Verification holds the procurement-methods element.
- **SR-8 (full):** the only claim of the control, since notification agreements are clause content maintained here and monitored below.
- **PM-17 (full):** the only claim of the control, carried by CUI Protection Requirements for External Systems.
- **SA-4(9) (full):** the clause library requires the developer to identify intended functions, ports, protocols, and services early. The resulting CM-7 decision stays with Platform Service Network Integration.
- **SA-4(10) (full):** the clause library restricts PIV acquisitions to the FIPS 201 approved products list.
- **SA-15(3) (full):** claimed here because only a contract clause can oblige the developer to perform criticality analysis. Supply Chain Risk Assessment and Dependency Mapping reads the results.
- **Declined:** SA-9(2) is a provider disclosure clause, cited here once the library carries it, since it is in the Moderate and High baselines. The program-side CM-7 decision stays with Platform Service Network Integration. SR-5(1) is unheld, and SR-5(2) belongs to Dependency Review and Model Selection and Justification. PS-7 belongs to the PSO, apart from the Identity focus area's access-granting slice.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The performer and every subcontractor, which carry the flowed-down clauses.

**Security Impact:** Moderate

**Activities:**

- **GV-3.2.1: Standard Security Clause Library**
    - **Description:** Build and maintain the library of reusable security clauses acquisitions draw from, covering the security functional and assurance requirements, documentation and its protection, allocation of responsibility for security, privacy, and supply chain risk management, acceptance criteria, right-to-audit and assessment access, compromise and audit-result notification obligations, personnel and data handling terms, and the obligation to flow the same clauses down to subcontractors, and record the clause library in the SCRM.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-4 (partial), SA-9 (partial), SR-5 (partial), and SR-8 (full) mappings, plus its SA-4(9) (full), SA-4(10) (full), and SA-15(3) (full) mappings. Include a right-to-assess clause, and draft clauses with contracting and legal counsel. Tier the library so a clause set matches the acquisition.

- **GV-3.2.2: Contract Security Requirement Flow-Down Verification**
    - **Description:** Verify before award, and at each modification, that the executed contract carries the clause set its acquisition tier requires, and that the prime contractor has flowed the same obligations down into its subcontracts.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-3(3) (full) mapping and the verification half of its SA-4 (partial) mapping. Verify the sub-tier, not only the prime, and do it before award while the program still has leverage.

- **GV-3.2.3: Contract Security Compliance Monitoring**
    - **Description:** Monitor each supplier's performance against the security obligations its contract carries for the life of the agreement, collecting the attestations, assessment results, and notifications the clauses require and recording non-performance as a finding against the vendor.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the monitoring element of the outcome's SA-9 (partial) mapping and the performance half of its SR-8 (full) mapping. The annual cadence covers attestations only, while a supplier compromise notification is handled as an incident through the Response focus area. Record findings in Vendor Security Risk Assessment's remediation register.

- **GV-3.2.4: CUI Protection Requirements for External Systems**
    - **Description:** Require every contractor and external party that processes, stores, or transmits the program's controlled unclassified information on its own systems to protect it to the applicable federal requirements, flow the obligation into contracts and subcontracts, verify compliance before CUI is shared, and document the requirement and its verification method in the SCRM.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-17 (full) mapping. For DoD contractors, DFARS clause 252.204-7012 and NIST SP 800-171 set the requirement. It is Level 2 because PM-17 sits outside the system baselines, but it is mandatory for a program sharing CUI with performers.

### GV-3.3: Supply Chain Risk Assessment and Dependency Mapping

**Design Intent:** The supply chain lead assesses KESTREL's software and hardware supply chain each year and maps the dependencies the mission rests on. These include the aircraft manufacturer, the two payload vendors, the cloud provider, the foundation model's publisher, and the HSM vendor. Single points of supply and countries of origin are recorded, and findings are tracked to closure.

**NIST Control Mapping:**

- **PM-30(1) (partial):** claimed for identifying critical suppliers, while Vendor Security Risk Assessment holds prioritization and assessment.
- **RA-3(1) (partial):** claimed for general supply chain assessment of acquired software and hardware, while Model Selection and Justification holds the model slice.
- **SR-3 (partial):** claimed for the standing organizational process to identify and address supply chain weaknesses. Three Application focus area outcomes hold the other, pipeline-triggered checks, which never reach acquired appliances, services, or equipment.
- **Declined:** RA-9 belongs to Asset Criticality and Business Impact Assessment, and this outcome lays dependencies over that register. SR-3(1) and SR-5(1) are procurement actions this outcome informs, recorded as gaps. SR-7 runs through the program's OPSEC discipline under the PSO. CA-5 and PM-4 are reserved for the Risk focus area's Plan of Action and Milestones (POA&M).

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The payload vendors, the aircraft and ground equipment manufacturers, the service desk vendor, the cloud provider, the CSSP, and the other suppliers in the vendor population.

**Security Impact:** Moderate

**Activities:**

- **GV-3.3.1: Software/Hardware Supply Chain Risk Assessment**
    - **Description:** Assess the supply chain risk carried by the software, hardware, and services the program acquires, examining each source's origin, ownership and control, development and delivery practices, and support commitments, update the assessment on the program's cadence and whenever the supply chain, the system, or its operating environment changes materially, and record the assessment method and scoring scale in the SCRM.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-3(1) (partial) mapping and the process-establishment element of its SR-3 (partial) mapping. Scope it to what arrives through a purchase order, since Dependency Review already covers pipeline components. Score results on the Risk focus area's Risk Assessment Methodology scale.

- **GV-3.3.2: Critical Component/Vendor Dependency Mapping**
    - **Description:** Map which components, services, and vendors the program's mission-essential functions actually depend on, reading criticality from the program's shared asset register rather than rating it again, record where a single supplier, component, or country of origin carries more of that dependency than the program has decided to accept, and record the mapping methodology and concentration criteria in the SCRM.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-30(1) (partial) mapping. Map at least one level below the direct supplier, where shared manufacturers, certificate authorities, or cloud regions hide. Lack of visibility below the prime is itself a finding for the Contract Security Requirements library.

- **GV-3.3.3: Supply Chain Risk Finding Remediation Tracking**
    - **Description:** Record each supply chain risk finding with its owner, its planned treatment, and its target date, and track it to closure or to an explicit risk decision when the treatment available to the program does not reduce the exposure.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Record the treatment path with each finding, such as qualifying a second source or renegotiating at renewal. Escalate a finding whose only honest treatment is acceptance to the Risk focus area's Risk Acceptance Process.

### GV-3.4: Hardware and Firmware Provenance Verification

**Design Intent:** Aircraft, stations, and payloads are bought only from their manufacturers, and data center hardware and HSMs only from authorized resellers. Everything is inspected for tampering and counterfeit parts at receipt. Firmware is accepted only with a valid manufacturer signature. Retired components are sanitized, and the sanitization is verified and recorded before disposal.

**NIST Control Mapping:**

- **SI-7(15) (partial):** claimed for authenticating firmware before installation, while the Application and Artificial Intelligence focus areas' signing outcomes hold the other artifact classes.
- **SR-4 (partial):** claimed for hardware and firmware, the artifact class the other SR-4 claimants do not reach.
- **SR-5 (partial):** claimed for the procurement-methods element, while Contract Security Requirements holds the contract-tools element.
- **SR-9 (partial):** covers only the delivery, receipt, and in-service inspection portion of a tamper protection program, so the claim stays partial.
- **SR-10 (full):** covers inspection at receipt and when indications warrant, such as return from vendor service or travel.
- **SR-11 (full):** the only claim of the control, produced across the sourcing and receipt activities, including reporting detected counterfeits.
- **SR-11(1) (full):** detection training is delivered as a curriculum under Role-Based Specialized Training.
- **SR-11(2) (partial):** claimed for inspecting serviced components before return, while the Configuration Management Plan (CMP) holds the custody records.
- **SR-11(3) (full):** carried by Periodic Counterfeit Component Rescan. It is in no baseline, so carry it where the AO or an overlay requires it.
- **SR-12 (partial):** claimed for physically dispositioning retired hardware and firmware, including OT devices, so components cannot be harvested or exploited. Resource Decommissioning Governance holds data sanitization, and Model Decommissioning and Disposal holds the model slice.
- **Declined:** SR-9(1) is developmental anti-tamper engineering no outcome performs, recorded as a gap. PE-3 and the physical protection family belong to the PSO.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Virtual Machine/Server, Cryptographic Hardware/HSM, Object/File Storage, Network Infrastructure, Device/Workstation, OT/ICS Device, Application/API, AI/ML System

**External Dependencies:** The aircraft, ground equipment, and data center hardware manufacturers and their authorized resellers.

**Security Impact:** High

**Activities:**

- **GV-3.4.1: Trusted Supplier and Authorized Reseller Sourcing Requirements**
    - **Description:** Define the sourcing requirement that binds procurement to original manufacturers, authorized resellers, and suppliers the program has qualified, name the evidence a supplier provides to establish that status, state the approval path for the exceptions a sole-source or obsolescence situation forces, and record the sourcing requirement in the SCRM.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the prevention element of the outcome's SR-11 (full) mapping and its SR-5 (partial) mapping. Provide a sanctioned exception path for end-of-life OT and legacy equipment available only on secondary markets. Record each exception through Policy Exception Management and require heightened inspection at receipt.

- **GV-3.4.2: Counterfeit and Tamper Detection at Receipt**
    - **Description:** Inspect incoming hardware and components on receipt, and again when a serviced or repaired component returns, against the program's defined counterfeit and tamper indicators, covering packaging and seal integrity, markings, serial and lot verification against the supplier's record, and physical characteristics, report a detected counterfeit to its source and to the roles the program names, and record the indicator set and reporting path in the SCRM.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-10 (full), SR-11(2) (partial), and SR-11(1) (full) mappings, the detection and reporting elements of SR-11 (full), and the receipt and in-service portion of SR-9 (partial). Inspect before the component enters service and before packaging is discarded, and train the logistics staff who do it. Inspect equipment returning from service, repair, or travel, and quarantine a detected counterfeit rather than returning it.

- **GV-3.4.3: Periodic Counterfeit Component Rescan**
    - **Description:** Rescan the program's fielded hardware and firmware inventory against the defined counterfeit and tamper indicator set on a fixed, standing frequency, independent of the receipt and in-service indication triggers that drive Counterfeit and Tamper Detection at Receipt, and record each rescan's results and disposition in the device inventory.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-11(3) (full) mapping. It adds a standing rescan of fielded equipment between custody changes, starting with less-controlled or higher-risk locations. It is Level 2 because SR-11(3) is in no baseline, so carry it where the AO or an overlay requires it.

- **GV-3.4.4: Firmware Provenance and Integrity Verification**
    - **Description:** Obtain firmware only from the manufacturer or an authorized distribution channel, verify its signature or published hash against the producer before installation, record the verified version, source, and verification result for each device in the device inventory this activity's Supplemental Guidance names so the provenance of what is running is answerable later, and record the sourcing-and-verification requirement itself in the SCRM rather than in that per-device record.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(15) (partial) and SR-4 (partial) mappings. It is not tagged Automate because OT and legacy devices usually need a manual hash check, though signed-update platforms can automate it. Write the record into the inventory Secure OT/Legacy Device Baselines uses. Removable Media is out of scope, since it has no firmware.

- **GV-3.4.5: Component Disposal and Sanitization Verification**
    - **Description:** Dispose of a hardware or firmware component retired from service or replaced for a supply-chain reason using the defined destruction or disposal technique its classification requires, verify and record that disposition, confirm the component cannot be recovered for counterfeit re-introduction elsewhere in the supply chain or retained for the intelligence value its design and configuration carry, and record the disposal technique-by-classification policy in the SCRM.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-12 (partial) mapping. It covers the physical component's disposition, while Resource Decommissioning Governance covers data sanitization. Run it per retirement or replacement event, including OT and legacy devices that outcome does not reach.

### GV-3.5: Supply Chain Risk Management Plan (SCRM)

**Design Intent:** The Program Office's supply chain lead authors KESTREL's SCRM plan with the SCRM team it names. The ISSM and the PMO ISSE review it, and the Configuration Control Board approves it. It is revised each year and whenever a Tier 1 supplier changes.

**NIST Control Mapping:**

- **PM-30 (partial):** claimed for the program-level supply chain strategy, namely risk appetite, accepted mitigations, and owning roles. It stays partial because it implements any organization-wide strategy above the program.
- **SR-1 (partial):** the procedures half, while Security Policy Framework holds the policy tier.
- **SR-2 (full):** its three clauses map onto the activities without residue. SCRM Development and Authoring develops the plan, SCRM Periodic Review and Revision updates it, and authorization-artifact handling protects it.
- **SR-2(1) (full):** SR-2's only enhancement, since this outcome constitutes the SCRM team itself.
- **Declined:** PM-30(1) is held jointly by Vendor Security Risk Assessment and Supply Chain Risk Assessment and Dependency Mapping.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-3.5.1: SCRM Development and Authoring**
    - **Description:** Author the supply chain risk management plan, consolidating the vendor assessment and tiering criteria, contract clause and flow-down standards, supply chain risk assessment method and dependency picture, and sourcing, inspection, firmware verification, and disposal and sanitization requirements this capability produced, naming the supply chain risk management team, its members' roles and responsibilities, and the activities it leads, and marking and storing the result at the classification and access restriction its content requires.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the plan-development clause of the outcome's SR-2 (full) mapping, the whole of its SR-2(1) (full) mapping, and the protection clause SR-2c requires. Mark and store the plan carefully, since it is a targeting aid. Name SCRM team members by position, drawing on the ISSE, contracting, procurement, logistics, and OT engineering owners.

- **GV-3.5.2: SCRM Review and Approval**
    - **Description:** Route the drafted SCRM through stakeholder review, secure formal approval from the accountable authority, and distribute the approved plan to the contracting, procurement, logistics, and engineering elements it assigns responsibilities to.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Approval sets the review frequency SCRM Periodic Review and Revision runs on. Distribute the plan to receiving, contracting, and other staff outside the security organization. Where supplier content is sensitive, give them a procedural extract.

- **GV-3.5.3: SCRM Periodic Review and Revision**
    - **Description:** Review the SCRM on the cadence its approval fixed, and revise it when a threat to the supply chain, a change in the program's supplier base or dependency picture, an organizational or contracting change, or a problem encountered in applying the plan makes any determination it records wrong.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries SR-2b of the outcome's mapping. Treat the annual cadence as a floor, and revise on external triggers such as a supplier acquisition, ownership change, public compromise, or end of support. Feed in findings from the remediation registers and the dependency mapping refresh.

## GV-4: AI/ML Governance

### GV-4.1: AI/ML Use Case Inventory

**Design Intent:** The AI use case inventory lists every AI use case KESTREL runs or has proposed, with its sponsor, models, data, any actions it can take, and its risk tier. Today those are the onboard and cloud detection models, the embedding model, the LLM analyst assistant, and the mission-planning agent. The risk tier rises with mission impact and with any ability to act, such as drafting flight plans. The inventory is reviewed each quarter against the model registry.

**NIST Control Mapping:**

- **PM-5 (partial):** the only claim of the control, held for the AI/ML portion of the inventory and its periodic update. In a single-system program the rest adds little beyond the SSP, though a multi-boundary program would need to extend it. PM-5(1) belongs to Privacy Program Management.
- **PM-11 (partial):** claimed for determining protection needs from mission processes, which the tier criteria encode. AI/ML Governance Review Board holds PM-11c.
- **RA-3 (partial):** claimed for use-case assessment at the mission and business process tier, before a model is selected. The Application and Artificial Intelligence focus areas' gate outcomes hold the system tier, and Program-Level AI Threat Assessment holds the organization tier.
- **Declined:** CM-8 and CM-8(1) are held by Model Registration and Inventory Logging and Asset Inventory and Discovery, which this register links to. RA-2 belongs to Security Categorization, since a governance tier sets oversight rather than categorization.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, First-Party/Custom Application Code, Self-Hosted Third-Party Application (COTS), Edge/Embedded AI Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-4.1.1: AI/ML System/Use-Case Discovery and Inventory Intake Process**
    - **Description:** Establish the inventory's intake path with the Artificial Intelligence focus area's AI Use Case Intake and Onboarding submissions as its primary feed, and run periodic discovery across procurement records, cloud AI service usage, and the features vendors have enabled inside products the program already owns, so that AI/ML already in use but never submitted is found rather than assumed absent.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-5 (partial) mapping. Use procurement and egress records to find commercial AI services and vendor-enabled models that never used the intake path. Register the use case, linked to versions in Model Registration and Inventory Logging, so the entry persists across retraining.

- **GV-4.1.2: Risk Tiering Methodology and Criteria Definition**
    - **Description:** Define the criteria that place each use case in a risk tier, covering the mission consequence of an incorrect or manipulated output, the sensitivity and processing authority of the data involved, whether a person reviews the output before it is acted on, and who can reach the inference interface, and state what each tier buys in review depth, control rigor, and reassessment frequency.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-3 (partial) and PM-11 (partial) mappings. Tie each tier to required review depth and control rigor, and weigh decision consequence and autonomy over model sophistication. Adjudicate Self-Reported AI Risk and Data Profile Questionnaire answers against evidence.

- **GV-4.1.3: Inventory Periodic Review and Reassessment**
    - **Description:** Review the inventory on the program's cadence and reassess an entry's tier whenever its purpose, data sources, degree of autonomy, or user population changes, closing out entries for use cases the program no longer runs.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the update elements of the outcome's PM-5 (partial) and RA-3 (partial) mappings. Trigger reassessment on repurposing or data changes, and re-run it when Risk Appetite and Tolerance Definition revises thresholds. Retire stale entries, and route a raised tier back through Use-Case Review/Approval Workflow.

### GV-4.2: Program-Level AI Threat Assessment

**Design Intent:** The PMO ISSE maps KESTREL's whole AI estate as one architecture each year, covering its trust zones, external interfaces, and the paths between models, use cases, and agents. The PMO ISSE then ranks the MITRE ATLAS techniques that matter most across it. The assessment goes to the AI/ML Governance Review Board and the ML and mission teams, and it feeds each model's threat model.

**NIST Control Mapping:**

- **RA-3 (partial):** claimed for the organization tier, an aggregate view of the AI estate. Other outcomes hold the system tier and AI/ML Use Case Inventory holds the mission tier.
- **Declined:** PL-8 stays with the Security Architecture and Design Document (SADD). SA-11(2), SA-15, and SA-15(2) stay with AI Threat Modeling, and SA-11(5) with Red Teaming. This outcome rolls their per-model findings up program-wide.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, First-Party/Custom Application Code, Edge/Embedded AI Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-4.2.1: AI Program Architecture and Trust Zone Mapping**
    - **Description:** Draw the AI program's system boundaries, data flows, trust zones, and external interfaces from the SADD, document them as the assessment's architecture baseline, and update them whenever a new data focus area, deployment path, or external interface constitutes a material change.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation and is an AI-scoped extract of the SADD. Revise it on the same material-change triggers that revise the SADD, in the same pass.

- **GV-4.2.2: MITRE ATLAS Program-Level Threat Ranking**
    - **Description:** Assess the mapped architecture against the taxonomy the Artificial Intelligence focus area's AI Threat Modeling has adopted, ordinarily MITRE ATLAS, ranking each applicable attack category by likelihood and impact at the program level and rolling the findings AI Threat Modeling and Red Teaming have already produced per model into that ranking rather than re-deriving them.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-3 (partial) mapping. Build the ranking from the per-model findings of AI Threat Modeling and Red Teaming, looking for weaknesses that only matter across the whole estate. Rank by likelihood and impact rather than finding count.

- **GV-4.2.3: Assessment Review, Distribution, and Consumption**
    - **Description:** Route the completed assessment through the ISSO and the AI/ML Governance Review Board for review, link it into the AO's evidence package, and deliver its ranked findings to Risk Appetite and Tolerance Definition as a threat-picture input to its tolerance bands and to AI Threat Modeling and Red Teaming as the priority weighting for per-model test scope.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation. Feed the ranking to Risk Appetite and Tolerance Definition through its existing threat-picture trigger. Give AI Threat Modeling and Red Teaming a priority weighting, not a reduced scope. Authorization Package Compilation links the artifact into the AO's package.

### GV-4.3: Responsible AI Policy and Principles

**Design Intent:** KESTREL's responsible AI policy adopts the DoD AI ethical principles, which call for AI that is responsible, equitable, traceable, reliable, and governable. It commits that no model commands an aircraft, that a person approves every AI agent action affecting a flight, and that analysts can see when AI contributed to a product. Each principle maps to the AI outcomes that enforce it, and the policy is part of every user's training.

**NIST Control Mapping:**

- **Declined:** no control takes responsible AI principles as its subject. PM-9 is reserved for the Risk focus area. The policy-and-procedures controls do not apply, since Rev 5 has no AI family. PT-1 belongs to Privacy Program Charter and Policy Development, and PT-2, PT-3, and RA-8 to Privacy Requirements Definition. SA-8 is held by Security Requirements Definition. AT-2 and AT-3 are held by the Security Awareness and Training Program, which delivers this instruction the way it does for SR-11(1). Principle-to-Control Mapping links each principle to cited AI outcomes.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, First-Party/Custom Application Code, Edge/Embedded AI Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-4.3.1: Responsible AI Policy Development**
    - **Description:** Author the responsible AI policy, stating the program's commitments on fairness and unwanted bias, on disclosing when and how an AI system participates in a decision, on who is accountable for a model's output, and on safety and human oversight, and write each commitment as something a reviewer can test a design against rather than as an aspiration.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Write each principle so a reviewer could reject a specific proposal with it, and give fairness a named population and measure. Draft with mission owners, legal counsel, and privacy staff, and approve it through Policy Lifecycle Management. It is Level 2, rising to Level 1 for a program bound by a departmental responsible AI directive.

- **GV-4.3.2: Principle-to-Control Mapping**
    - **Description:** Map each principle in the policy to the specific Artificial Intelligence focus area outcomes that enforce it, so that transparency resolves to Model Card Generation, safety resolves to the robustness suites, Red Teaming, and the Rollback/Kill-Switch Mechanism, and a principle with nothing behind it surfaces as a gap rather than standing as a claim.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no control claim, since the outcomes it names hold the enforcement. Map from principle to outcome so unimplemented commitments surface. Record fairness as a gap if no validation suite tests disparate performance, and re-run the mapping when the policy or AI outcomes change.

- **GV-4.3.3: Policy Publication and Awareness**
    - **Description:** Publish the approved responsible AI policy through the program's existing policy repository, and have its content reach the model developers, data scientists, and mission owners it binds as part of their role-based curriculum rather than as a one-time briefing.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries no independent claim, since Policy Publication and Version Control and Role-Based Specialized Training hold the mappings. Target mission owners who propose use cases, not only engineers. Use Baseline Security Awareness Training's local delivery path in isolated enclaves.

### GV-4.4: AI/ML Governance Review Board

**Design Intent:** The chief engineer chairs the AI/ML Governance Review Board. Its members are the PMO ISSE, the privacy officer, program legal counsel, the ML team lead, and the sponsoring intelligence mission lead, with the foreign disclosure officer joining when partner release is involved. The board decides each use case within ten business days by approving it, approving it with conditions, or rejecting it, against the responsible AI policy and the use case's risk tier. Decisions and conditions are tracked to closure, and a posture report goes to the steering committee each quarter.

**NIST Control Mapping:**

- **PM-11 (partial):** claimed for revising mission processes until protection needs are achievable, as a conditioned approval does. AI/ML Use Case Inventory holds PM-11b.
- **PM-6 (partial):** claimed for the AI/ML-estate measures in the posture report, while the steering committee, Risk Register and Tracking, and Compliance Evidence Collection and Retention hold the other slices.
- **Declined:** CA-6 is not claimed because the board decides before any system exists, so there is nothing to authorize. CA-6 is reserved for the Authorization to Operate (ATO) Process, and PM-10 belongs to that capability too. PM-29 is held by the Security Governance and Steering Committee, to which this board escalates.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, First-Party/Custom Application Code, Edge/Embedded AI Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-4.4.1: Review Board Charter and Membership Definition**
    - **Description:** Charter the board, stating its purpose, its standing membership by position across the mission, security, legal, privacy, and data science functions, its quorum, which decisions it makes itself and which it recommends to the AO or the steering committee, and the turnaround it commits to at each risk tier.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** State membership by position, commit to a turnaround fast enough that teams do not prototype first, and name what the board cannot decide. It is Level 2 because a small program can run the function as a standing agenda item of the Security Governance and Steering Committee.

- **GV-4.4.2: Use-Case Review/Approval Workflow**
    - **Description:** Define the review path each risk tier follows, from a recorded desk review by the ISSE for the lowest tier through full board adjudication for the highest, and record an approval, an approval with named conditions, or a rejection for every use case before any data engineering or training work is authorized to begin.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-11 (partial) mapping. Tier review depth so low-consequence work does not queue behind high-consequence work. Write each condition into the intake record Routing and Handoff to Scoping, Requirements, and Design uses, with a named owner, and give every rejection a basis and a route back.

- **GV-4.4.3: Review Board Decision Tracking and Escalation**
    - **Description:** Record every board decision against its use case with the assigned tier, the conditions imposed, and their owners, verify each condition has been met before the use case reaches certification, and escalate a decision the board cannot reach or a condition a team will not accept to the Security Governance and Steering Committee.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Verify conditions at the Artificial Intelligence focus area's Certification to Field gate. Send residual risk the board will not resolve to the Risk focus area's Risk Acceptance Process. Record every decision, since it proves review happened before the work began.

- **GV-4.4.4: AI/ML Governance Posture Report**
    - **Description:** Maintain the AI/ML estate's governance state as a single record in the program's security repository, drawing rather than recomputing the use-case count by risk tier from the sibling AI/ML Use Case Inventory, the board's decision backlog and condition-closure status from Review Board Decision Tracking and Escalation, outstanding findings and the organizational risk tier from AI/ML Vendor/Model Risk Assessment, open items from AI/ML Regulatory Mapping, and the per-model inventory, with each fielded model's registry identifier, vendor, approved deployment environments, accountable owner, mission criticality, and classification, from the Artificial Intelligence focus area's Model Registration and Inventory Logging, and export it on a committed cadence as a report the AO can read without standing access to any of the underlying registers.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-6 (partial) mapping. Maintain it as a markdown record exported to PDF on the committed cadence, and feed it into Security Program Metrics/Posture Dashboard for Leadership Reporting. Draw governance fields from Model Registration and Inventory Logging and risk tiers from AI/ML Vendor/Model Risk Assessment. It is Level 2 because the underlying gates carry the Level 1 obligations.

### GV-4.5: AI/ML Regulatory Mapping (NIST AI RMF, DoD RAI)

**Design Intent:** The PMO ISSE maps KESTREL's AI use cases against the DoD AI Cybersecurity Risk Management Tailoring Guide, the NIST AI RMF, and the DoD Responsible AI strategy. Gaps are traced to the AI outcomes that close them. A new or revised AI directive is assessed within a quarter of issue.

**NIST Control Mapping:**

- **Declined:** no control covers conformance to a framework outside the catalog. PM-1 is already split three ways. CA-2 belongs to Control Assessment Scheduling and Annual Security Review. SI-5 covers security advisories, not AI framework revisions. This outcome holds the AI instruments, while Regulatory Compliance Mapping holds the general set, and the two should feed one register.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** AI/ML System, First-Party/Custom Application Code, Edge/Embedded AI Device

**External Dependencies:** DoD and NIST, whose AI guidance this mapping tracks.

**Security Impact:** Low

**Activities:**

- **GV-4.5.1: Regulatory/Framework Requirement Mapping and Gap Analysis**
    - **Description:** Determine which AI-specific frameworks, directives, and departmental policies bind the program and on what basis, decompose each into discrete testable requirements, and map every requirement to the outcomes that satisfy it, recording each unmatched requirement as a gap with a named owner.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Record whether each instrument binds the program or was adopted voluntarily, and decompose to the requirement rather than the function. Documented human oversight, disparate-performance evaluation, and automated-decision disclosure are owned gaps that no outcome tests, so carry them open on the register. The AI/ML Governance Review Board can require a bias evaluation or disclosure as an approval condition. Add rows to Regulatory Compliance Mapping's combined register.

- **GV-4.5.2: Control-to-Requirement Traceability Maintenance**
    - **Description:** Maintain the traceability record in both directions, so that a change to an outcome identifies the AI framework requirements it affects and a revised requirement identifies the outcomes that must change with it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Keep the record bidirectional and in the program's existing traceability tooling, adding AI requirements against the same control identifiers in SSP Machine-Readable Authoring/Maintenance where OSCAL is used. The Security Controls Traceability Matrix (SCTM) governs on implementation, and this record governs only on which external requirement it answers.

- **GV-4.5.3: AI Regulatory Landscape Monitoring and Update Process**
    - **Description:** Assign a named position responsibility for watching the AI policy and regulatory landscape, and re-run the mapping and gap analysis whenever an instrument the program is bound by is revised, a new one reaches it, or a use case changes in a way that brings it into scope of requirements that did not previously apply.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Run the watch quarterly, since AI policy changes fast, and combine it with Regulatory Compliance Mapping's general watch. Take internal triggers from AI/ML Use Case Inventory's reassessment, such as a use case becoming autonomous, public-facing, or consequential.

### GV-4.6: AI/ML Vendor/Model Risk Assessment

**Design Intent:** The board receives each AI supplier risk finding and decides what to do about it. Findings come from model selection, label integrity, foundation model dependency governance, and vendor assessment. Each AI supplier is tiered, and acceptances of supplier risk are logged with the AO's visibility. Each foundation model and other vendor-delivered model is registered in the inventory once its risk is accepted.

**NIST Control Mapping:**

- **RA-7 (partial):** claimed for responding to supplier and acquired-model findings in line with risk tolerance, a population none of the six other RA-7 claimants reaches.
- **CM-8 (partial):** claimed for vendor-hosted and supplier-delivered models, while Model Registration and Inventory Logging holds the self-hosted rest.
- **Declined:** SR-6 is held by the four supplier assessment outcomes, while this outcome disposes of their findings. PM-30(1) is held by Vendor Risk Tiering and Periodic Reassessment and Critical Component/Vendor Dependency Mapping, and the AI tier here overlays the existing supplier tier. CA-5 and PM-4 are reserved for the Risk focus area's Plan of Action and Milestones (POA&M), and acceptance runs through Risk Acceptance Process.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Third-Party API Model, Self-Hosted Model, Foundation Model, Edge/Embedded AI Device

**External Dependencies:** The cloud provider, the foundation model's publisher, and the publishers of pretrained checkpoints.

**Security Impact:** Moderate

**Activities:**

- **GV-4.6.1: Vendor AI/ML Risk Tiering and Organizational Risk Acceptance Workflow**
    - **Description:** Place each AI/ML supplier and adopted model in an organizational risk tier that folds the AI-specific exposures onto the supplier tier the general vendor process already assigned, and route any residual the program elects to carry into the Risk focus area's Risk Acceptance Process for an authority-tiered decision rather than granting it here.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the risk-tolerance element of the outcome's RA-7 (partial) mapping. Tier on AI-specific exposures, such as undisclosed training data, silent model changes behind an endpoint, and license or availability restrictions. It is Level 2, rising to Level 1 where SR-6 is tailored in and the program fields an externally sourced model. Route acceptance rather than deciding it here, and record the routing.

- **GV-4.6.2: Governance-Level Risk Assessment Findings Escalation and Remediation Tracking**
    - **Description:** Record each AI/ML supplier or model finding escalated from the technical assessments with its severity, its decided treatment, its owner, and its target date, and drive it to a closed disposition of a supplier fix, a compensating control, an accepted residual, or a decision to stop using the supplier or model.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the response element of the outcome's RA-7 (partial) mapping and claims neither CA-5 nor PM-4. It is Level 1 because an undisposed finding is an unanswered control obligation. Realistic dispositions are acceptance, substitution with Model Selection and Justification's runner-up, or withdrawal through the AI/ML Governance Review Board.

- **GV-4.6.3: Third-Party Model Registration in Authoritative Inventory**
    - **Description:** Register each vendor-hosted or supplier-delivered model the program adopts in the program's authoritative inventory once its organizational risk tier is recorded, capturing the vendor, the model name and version, the endpoint the program reaches it through, its accountable owner, mission criticality, and classification, and linking to its organizational risk tier and its data governance terms rather than restating them.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-8 (partial) slice for vendor-hosted and supplier-delivered models. Register the model when Vendor AI/ML Risk Tiering and Organizational Risk Acceptance Workflow records its tier. Link to that tier and to Third-Party Model API Data Governance terms rather than copying them, and send recurring findings to the Standard Security Clause Library.

## GV-5: Authorization Management

### GV-5.1: Security Architecture and Design Document (SADD)

**Design Intent:** The PMO ISSE authors this SADD from the AO-approved CCSD, generating its carried fields from the SABER and writing its design intents by hand. The chief engineer and the ISSM review it, and the AO accepts it as KESTREL's design basis. It is rebuilt whenever the CCSD, the system description, or the SABER version changes.

**NIST Control Mapping:**

- **PL-8 (full):** the elements map onto the activities without residue. SADD Development and Authoring builds the architecture, SADD Periodic Review and Revision updates it, and that revision feeds the Security Implementation Plan and System Security Plan (SSP).
- **PL-8(1) (full):** allocating controls to layers so they reinforce each other is the reason the design step exists.
- **PM-7 (partial):** the SADD conforms to any organization-wide enterprise architecture above the program rather than replacing it, so the claim stays partial.
- **Declined:** PL-8(2) is a supply chain matter for Critical Component/Vendor Dependency Mapping. PM-7(1) covers offloading functions. SA-17 and SA-8 are held by the Application focus area's Security Requirements Definition. PL-2 belongs to the SSP.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **GV-5.1.1: SADD Development and Authoring**
    - **Description:** Apply the SABER's pillars, focus areas, capabilities, and outcomes against the program's AO-scoped requirement set to produce the SADD, recording for each tailored control the outcome or outcomes that satisfy it, the environments it applies in, and the dependencies on external systems and services the design assumes.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the development clause of the outcome's PL-8 (full) mapping together with the whole of its PL-8(1) (full) claim. Resolve each control several focus areas partly satisfy into a named owner and contributors, which is why effort is High. Record a tailored control with no outcome as a framework gap here.

- **GV-5.1.2: SADD Review and Approval**
    - **Description:** Put the drafted SADD in front of the performer engineering leads and the ISSM for review, secure approval from the authority the program's policy hierarchy designates, and issue the approved document to the engineers who will build against it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Approval sets the frequency SADD Periodic Review and Revision runs on. Include performer engineering leads in review so outcomes are costed. Take approval through the Security Governance and Steering Committee where it handles architectural decisions.

- **GV-5.1.3: SADD Periodic Review and Revision**
    - **Description:** Re-examine the SADD on the cadence its approval fixed, revising it when the AO retailors the requirement set, an overlay is applied, the categorization changes, or the architecture in the field diverges from the one the document describes.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the review-and-update and change-propagation clauses of the outcome's PL-8 (full) mapping. Review against the requirement set, since AO retailoring often triggers revision. Push accepted revisions into the Security Implementation Plan and SSP, and take architectural changes routed from Asset Lifecycle Change Control.

### GV-5.2: Security Implementation Plan

**Design Intent:** The PMO ISSE and the performer team leads write the Security Implementation Plan from this SADD. It records the tools chosen for each outcome, the rollout order, and the effort and cost. The Configuration Control Board approves it, and it is revised each quarter as outcomes are built.

**NIST Control Mapping:**

- **Declined:** no control covers product selection and rollout sequencing. PL-2 belongs to the SSP, which records realized implementation. PL-8 belongs to the SADD. SA-3 is held by the Application and Artificial Intelligence focus areas, and SA-2 by Capability Gap Identification and Planning and Security Requirements Definition. PM-3 sits above the program. CM-9 belongs to the Configuration Management Plan (CMP).

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-5.2.1: Security Implementation Plan Development and Authoring**
    - **Description:** Take each SADD outcome and record the tool, cloud service, or product that will implement it, the environment-specific tailoring that choice requires, the team accountable for delivering it, and its position in a rollout sequence built around funding, dependencies, and the program's schedule.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Sequence by dependency, since identity precedes most Protect work and logging precedes Operate detection. Record the outcome each product serves. Author the plan in a form the issue tracker can import, with outcomes as stories and activities as tasks.

- **GV-5.2.2: Security Implementation Plan Review and Approval**
    - **Description:** Circulate the plan to the engineering, contracting, and budget stakeholders whose commitments it assumes, obtain approval from the program authority able to commit those resources, and publish the approved sequence to the teams executing it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Get approval from whoever controls the money and staff the sequence assumes, not only the security organization. Include contracting, since a product decision may need a clause from the Standard Security Clause Library before award.

- **GV-5.2.3: Security Implementation Plan Periodic Review and Revision**
    - **Description:** Revisit the plan on the cadence its approval fixed, and rework the sequence when a selected product is substituted, a SADD revision adds or removes an outcome, a dependency slips, or funding moves, so what is recorded stays what teams are actually working to.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Review quarterly, since the plan tracks procurement and delivery reality and the SSP is written from it. Carry a substitution that changes a control's implementation into the SSP and the Security Controls Traceability Matrix (SCTM).

### GV-5.3: System Security Plan (SSP)

**Design Intent:** The ISSM authors KESTREL's SSP with the ISSOs, recording what was actually built against each SADD outcome. The PMO ISSE reviews it, and the AO approves it with the package. It is maintained in OSCAL, so the SCTM and assessment tools can read it, and it is revised with every significant change.

**NIST Control Mapping:**

- **PL-2 (full):** SSP Development and Authoring produces the contents, SSP Review and Approval takes AO approval and handles distribution, and SSP Periodic Review and Revision handles updates. PL-2 has no active enhancements. Information types come from the Categorization and Control Selection Document (CCSD) and categorization from Security Categorization, and the Security Controls Traceability Matrix (SCTM) opens no second PL-2 claim.
- **PL-1 (partial):** the planning-family procedures half, while Security Policy Framework holds the policy tier.
- **PL-7 (partial):** claimed for the concept of operations content held as a section of the plan. It is partial because relationships with other organizations can extend beyond this outcome.
- **Declined:** PL-4 is not touched, the sibling capability's Rules of Behavior and Acceptable Use Policy holding it full.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **GV-5.3.1: SSP Development and Authoring**
    - **Description:** Author the SSP, defining the system's components, boundary, and operational context, naming its security role holders, carrying in the information types and categorization the sibling outcomes determined, identifying the baseline and overlays in force, and writing an implementation statement for every control in the tailored set.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Extensive
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the development and protection clauses of the outcome's PL-2 (full) mapping, so mark and restrict the document. Have whoever built each control write its statement from what was actually delivered, which is why effort is Extensive. Where the program uses OSCAL, render the document from the machine-readable source.

- **GV-5.3.2: SSP Review and Approval**
    - **Description:** Route the drafted SSP through ISSM and stakeholder review, then have the authorizing official or their designated representative approve it before the plan is implemented, and distribute copies to the personnel and roles the program designates.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the plan-approval and distribution clauses of the outcome's PL-2 (full) mapping. This approval accepts the plan as the assessment baseline, separate from the risk decision in the Authorization to Operate (ATO) Process. Distribute a scoped extract to operating elements and hold the full plan closely.

- **GV-5.3.3: SSP Periodic Review and Revision**
    - **Description:** Review the SSP on the cadence its approval fixed, and update it to address changes to the system or its environment of operation and problems identified during plan implementation or control assessments.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the review and update clauses of the outcome's PL-2 (full) mapping. Treat the annual cadence as a floor, and take event-driven updates from Security Impact Analysis (SIA). Take assessment findings through the Security Assessment Report (SAR) and Plan of Action and Milestones (POA&M).

- **GV-5.3.4: SSP Machine-Readable Authoring/Maintenance**
    - **Description:** Author and maintain the SSP as OSCAL source held under version control, generate the human-readable document from that source, and validate every change against the OSCAL schema in the same pipeline the program uses for code.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** It claims no share of the mapping, since PL-2 is format-neutral. An OSCAL-native SSP feeds the SCTM, the Evidence Export Pipeline, and assessor tooling without transcription. It is Level 3, and the direction of authorship must be settled so OSCAL is not generated from a hand-edited document.

### GV-5.4: Categorization and Control Selection Document (CCSD)

**Design Intent:** KESTREL's CCSD lists its 18 information types with their provisional values and the control selection and tailoring that follow. The AO approved version 1.0, and version 1.1, covering the system's growth since, is in SCA review. The PMO ISSE revises it whenever an information type, interconnection, or boundary changes.

**NIST Control Mapping:**

- **RA-2 (partial):** claimed for categorizing information types and assigning provisional impact values. Security Categorization holds the system half, documentation, and AO approval. Four other outcomes reserved RA-2 here, since this outcome issues the information-type definitions.
- **PL-11 (partial):** claimed for drafting the tailoring and its rationale. It is partial because AO approval after SCA review makes it the baseline.
- **Declined:** RA-2(1) is a cross-system portfolio prioritization above any single system. CM-12 belongs to the Data focus area, which finds where information resides, while this outcome lists authorized types.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **GV-5.4.1: Information Type Identification and Inventory**
    - **Description:** Enumerate every information type the system processes, stores, and transmits, mapping each to the NIST SP 800-60 catalog and to the national security system information types CNSSI 1253 defines, and record its source, its owner, and where inside the boundary it is held.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the identification half of the outcome's RA-2 (partial) mapping. Look for commonly missed types, such as security telemetry, backups under different retention, and transit-only data. Use Data Discovery, Labeling, and Classification to test completeness, and map unusual data to the closest catalog type with a recorded deviation.

- **GV-5.4.2: Provisional Impact Value Assignment per Information Type**
    - **Description:** Assign each information type a provisional confidentiality, integrity, and availability impact value using the FIPS 199 levels as qualified by CNSSI 1253 for national security systems, and write down the rationale for every value departing from the catalog's recommended provisional value.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the provisional-value half of the outcome's RA-2 (partial) mapping. Record the rationale for every adjustment, since aggregation often raises values. Set integrity and availability carefully, because recovery objectives must be supportable under the resulting baseline.

- **GV-5.4.3: CCSD Periodic Update**
    - **Description:** Update the document whenever the system takes on a new data source, mission, interconnection, or user population, and when a type is retired, so that the inventory and its provisional values describe the system as it now operates.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Trigger the update on change through Security Impact Analysis (SIA), such as a new connection under System Interconnection Agreements (ISA/MOU/MOA) or a new training feed. Hand a moved provisional value to Security Categorization for reassessment.

- **GV-5.4.4: Control Selection and Tailoring Draft**
    - **Description:** Draft the program's control selection from the NIST SP 800-53 Rev 5 baseline the sibling Security Categorization selects, applying each overlay and cloud impact-level requirement that binds the program and recording every tailoring action with its rationale, then route the draft to the SCA for review and to the AO for approval and record the approved set in the CCSD.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PL-11 (partial) mapping. Record a rationale for every tailoring action, and build the SADD against the approved set rather than the draft. Cite Rev 5 even where the framework publishes Rev 4 baselines, with reconciliation in the requirements traceability artifact. Where several authorities apply, satisfy each overlay and record mutual acceptance in Inherited Control Validation.

### GV-5.5: Security Categorization

**Design Intent:** KESTREL is categorized High for confidentiality and integrity and Moderate for availability, using CNSSI 1253's per-objective high-water mark over the CCSD's information types. The AO concurred with version 1.0. The categorization is reassessed with every CCSD revision.

**NIST Control Mapping:**

- **RA-2 (partial):** claimed for categorizing the system, documenting the result in the plan, and verifying AO approval. The CCSD holds the information half.
- **PL-10 (partial):** the only claim of the control, since the categorization determines the baseline. It is partial because selection is recorded in the SSP and drawn from CNSSI 1253 for national security systems.
- **Declined:** RA-2(1) is declined at the CCSD for the same reason. PL-11 is claimed at the CCSD, since categorization selects the baseline and tailoring adjusts it.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **GV-5.5.1: System-Level CIA Impact Determination**
    - **Description:** Compute the system's confidentiality, integrity, and availability impact levels from the CCSD's provisional per-type values under the aggregation rule the program is bound by, and write down the reasoning for any level set above or below the highest provisional value.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the system half of the outcome's RA-2 (partial) mapping and the whole of its PL-10 (partial) claim. Document any departure from the high-water mark, whether aggregation raises a level or a real, named separation lowers one. Do not understate availability, since the Contingency Plan (CP) objectives must be supportable.

- **GV-5.5.2: Categorization Documentation and AO Concurrence**
    - **Description:** Record the determination and its supporting rationale in the System Security Plan (SSP), and route it to the authorizing official or their designated representative for review and concurrence before it is used to select the control baseline.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the documentation and approval elements of the outcome's RA-2 (partial) mapping, which are two obligations. Record the result in the SSP and get AO concurrence early, before the program builds to the selected baseline.

- **GV-5.5.3: Categorization Periodic Reassessment**
    - **Description:** Reassess the categorization when the CCSD changes, a new interconnection or mission alters what the system holds or supports, or a threat or consequence assumption behind a level stops holding, and re-route any changed determination for AO concurrence.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Treat a rising categorization as a SADD and Security Implementation Plan revision, not a documentation change. Take triggers from the CCSD's change-driven update and from new connections under System Interconnection Agreements (ISA/MOU/MOA). Ongoing Authorization decides whether a moved level requires reauthorization.

### GV-5.6: System Interconnection Agreements (ISA/MOU/MOA)

**Design Intent:** Each interconnection in the system description has a signed agreement that documents both sides' interfaces and controls. These cover the cloud provider, the Boundary Cloud Access Point, the CSSP, the cross domain service provider, each partner nation, the performer, the penetration testing provider, and the alternate site's facility. Each agreement is reviewed each year and whenever its connection changes.

**NIST Control Mapping:**

- **CA-3 (full):** the only claim of the control, with its three elements mapping onto the activities without residue. Identification documents the interface, development and approval puts it under agreement, and periodic review updates it.
- **CA-3(7) (partial):** claimed for identifying transitive downstream exchanges. Stopping those exchanges is boundary enforcement held by the Network and Environment focus area, so the claim stays partial.
- **Declined:** CA-3(6) is a runtime boundary check closest to Cross Domain Solution (CDS) Transfer Procedures. CA-9 is held by Platform Service Network Integration for internal connections.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Remote Access/VPN Gateway, Private Connectivity/Dedicated Circuit, Cross-Domain/Boundary Transfer, Object/File Storage, External/Federated Trust, API/Interface Contract, Industrial Controller/SCADA

**External Dependencies:** Every interconnected party listed in the system description, as a signatory to its agreement.

**Security Impact:** Moderate

**Activities:**

- **GV-5.6.1: Interconnecting System Identification and Boundary Documentation**
    - **Description:** Identify every external system the program exchanges information with, document each connection's interface characteristics, the information types and impact level crossing it, the controls each side relies on and the responsibilities each party holds, and record the downstream systems that information can reach through those connections.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the documentation element of the outcome's CA-3 (full) mapping and the identification element of its CA-3(7) (partial) claim. Hunt for forgotten file drops, vendor support tunnels, and inherited interfaces, reconciling against the Network and Environment focus area's flow records. Ask where each partner forwards the data.

- **GV-5.6.2: ISA/MOU/MOA Development and Signatory Approval**
    - **Description:** Develop the agreement instrument appropriate to each exchange, carry the documented interface, requirements, controls, responsibilities, and impact level into its terms, and obtain signature from the authority on each side empowered to bind their organization.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the approval and management element of the outcome's CA-3 (full) mapping. Expect the other party's approval chain to set the schedule. Include compromise notification terms the Incident Response Plan (IRP) can follow and terms for a lapsed authorization, and have someone who can bind each organization sign.

- **GV-5.6.3: Interconnection Agreement Periodic Review and Renewal**
    - **Description:** Revalidate every agreement on the program's review cycle and on any change to either system's categorization, controls, or authorization status, and renew, revise, or terminate the exchange rather than letting an expired agreement carry live traffic.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the review-and-update element of the outcome's CA-3 (full) mapping. Pair each expiry date with the boundary rule permitting the flow so termination is enforceable, and re-check transitive connections at renewal. Route a partner's lapsed authorization to Ongoing Authorization and, if needed, Risk Acceptance Process.

### GV-5.7: Authorization to Operate (ATO) Process

**Design Intent:** The ISSM submits the package to the AO, and AO determinations and conditions are tracked to closure in the POA&M. Before full authorization, an interim authorization to test covers integration on spare aircraft and the simulator, so no live mission data or flight depends on an unauthorized system.

**NIST Control Mapping:**

- **CA-6 (partial):** claimed for assigning the AO, accepting inherited common controls, and authorizing operation and common controls. Ongoing Authorization holds the update element.
- **PM-10 (partial):** claimed for managing system state through an authorization process tied to organizational risk management. Security Roles and Responsibilities and ISSO/ISSM Appointment Letters hold the rest, namely role designation.
- **Declined:** CA-6(1) assumes multiple AOs within one organization, which the framework does not assume, the same basis on which IR-8(1) is left to tailoring. CA-6(2) is claimed by Inherited Control Validation. CA-5 and PM-4 are reserved for the Risk focus area's Plan of Action and Milestones (POA&M), which this outcome reads. CA-2 is the Compliance focus area's.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **GV-5.7.1: ATO Package Submission**
    - **Description:** Submit the versioned package the sibling Authorization Package Compilation assembled on the program's established path, confirming first that it matches the AO's stated package requirements and that no artifact in it has been superseded since it was packaged.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the state-management element of the outcome's PM-10 (partial) mapping. Assemble against the AO's stated package requirements, and confirm the artifacts agree with each other. Authorization Package Compilation does the collection.

- **GV-5.7.2: AO Risk Determination and Adjudication Tracking**
    - **Description:** Track the package through the authorizing official's review to a recorded determination, logging every request for information, every clarification returned, and the terms of the decision including its type, its duration, and any inherited common controls accepted.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the whole of the outcome's CA-6 (partial) mapping. Record acceptance of inherited common controls and the decision's terms, such as duration, scope limits, and conditions. Record any residual the AO carries through the Risk focus area's Risk Acceptance Process.

- **GV-5.7.3: ATO Condition/POA&M Closure Tracking**
    - **Description:** Track each condition the authorization imposed and each plan of action item it rests on to verified closure against the Risk focus area's Plan of Action and Milestones (POA&M), escalating any item whose slip would reach the authorization's terms.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity claims neither CA-5 nor PM-4 and reads the POA&M rather than building a second one. Flag which items the authorization was conditioned on, and escalate a condition before it lapses, since a lapse is a status change for Ongoing Authorization.

- **GV-5.7.4: Interim Authorization to Test**
    - **Description:** Where testing in the operational environment or with live data must begin before the authorization decision, request an interim authorization to test from the AO that states the test's scope, duration, connections, data, and the conditions on which it ends, and hold the test within those terms.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's CA-6 (partial) mapping for a bounded test authorization, which DoD RMF calls an interim authorization to test (IATT). It is Level 2 because many programs test only in isolated environments with synthetic data. It ends at the authorization decision or expiry and never carries into operation.

### GV-5.8: Authorization Package Compilation

**Design Intent:** The ISSM compiles the package from each artifact's owning outcome, checks it for completeness and quality, and versions each submission. The PMO ISSE attests that the package matches what was built. The model evidence annex comes from each model's AI Cyber T&E record.

**NIST Control Mapping:**

- **Declined:** no control covers collecting and packaging, and each artifact carries its producing outcome's citation, such as PL-2, RA-2, CA-3, and PL-8. CA-2 is reserved for the Compliance focus area. SA-5 covers developer documentation. CA-6 belongs to the Authorization to Operate (ATO) Process.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-5.8.1: Authorization Package Artifact Inventory and Collection**
    - **Description:** Maintain the list of artifacts the package must contain, naming the outcome and the position accountable for each, and collect the current approved revision of every one ahead of a submission.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Name the owning outcome for each artifact so a missing item has someone to chase. Derive the list from the AO's requirements, and pull from Compliance Evidence Collection and Retention where an artifact already lives there.

- **GV-5.8.2: Authorization Package Completeness/Quality Review**
    - **Description:** Review the assembled set for missing artifacts, superseded revisions, unsigned approvals, and statements that contradict each other across documents, returning each defect to the outcome that owns the artifact rather than correcting it inside the package.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Send defects back to the source artifact rather than editing inside the package. Check that categorization, boundary, and interconnections agree across artifacts, and run the review early enough that defects can be fixed before submission.

- **GV-5.8.3: Authorization Package Version Control and Submission Packaging**
    - **Description:** Package the reviewed set as a single versioned submission recording the revision of every artifact it contains and the date it was assembled, and retain it so that any past submission can be reproduced exactly as the AO received it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Retain each submission as a reproducible snapshot, while every artifact stays with its owning outcome. Decide the package's marking deliberately, since the aggregate is usually more sensitive than any single artifact.

- **GV-5.8.4: Package Accuracy Attestation**
    - **Description:** Have the program's designated security authority sign a statement that the system was implemented in accordance with its approved design and that the assembled package is complete and accurate, tying each assertion to a named artifact in the package and disclosing any control whose evidence is not yet produced along with the date it will be.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The attestation records what the program asserts, while the Security Assessment Report (SAR) records what the assessor found. Under JSIG it is the System Validation Letter and is mandatory where the AO requires one. Disclose evidence gaps with dates, and reissue on Ongoing Authorization's trigger criteria.

- **GV-5.8.5: Model Assessment Evidence Annex**
    - **Description:** Attach each fielded model's certification evidence to the authorization package as a model-specific annex to the SSP, namely its AI Cyber T&E Plan, validation report with operational addenda, model card, red team sign-off, and risk acceptances, and replace the annex whenever Certification to Field certifies a new version.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Authorize the hosting system normally and annex each model's assessment evidence to the package, which the DoD AI Cybersecurity Risk Management Tailoring Guide calls "Assess Only". Build the annex from existing Artificial Intelligence focus area artifacts, and do not field a new version until its annex is in the package. Ongoing Authorization's trigger criteria decide whether it needs notification or reauthorization.

### GV-5.9: Security Controls Traceability Matrix (SCTM)

**Design Intent:** The ISSM maintains the SCTM in OSCAL, carrying each control in the tailored set to its SADD outcome, its implementation in the SSP, its inheritance status, and its evidence. It starts from this SADD's control coverage table. It is validated against the SSP before each submission and updated with every change.

**NIST Control Mapping:**

- **Declined:** PL-2's control-description element is held by the System Security Plan (SSP), and the SCTM renders the same obligation as a matrix. No control covers the reconciliation this outcome adds. CA-2 belongs to the Compliance focus area. PL-11 drafting is claimed at the CCSD.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-5.9.1: SCTM Development**
    - **Description:** Build a row for every control and enhancement in the tailored set, recording the implementation that satisfies it, the outcome or component providing it, whether it is system-specific, inherited, or hybrid, and the evidence artifact supporting it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Fill in inheritance status and confirm the provider agrees it offers the control. Seed rows from the outcome-level NIST Control Mapping, then record what was actually built. A tailored control with no row is a gap.

- **GV-5.9.2: SCTM Review and Validation against SSP**
    - **Description:** Compare every row against the corresponding implementation statement in the SSP, and reconcile any control where the matrix and the plan describe the implementation, its provider, or its inheritance status differently.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The SSP governs on implementation, so correct the matrix unless the SSP is wrong, in which case send the fix to SSP Periodic Review and Revision. Treat the semi-annual pass as a floor that catches changes missed on the change path.

- **GV-5.9.3: SCTM Periodic Update**
    - **Description:** Update the matrix when the AO retailors the control set, an overlay is applied, the categorization moves the baseline, or an implementation is replaced, and carry the same change into the SSP so the two move together.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Update on AO retailoring and on implementation changes, connecting to Asset Lifecycle Change Control to catch the latter. Keep rows for removed controls with their disposition recorded.

- **GV-5.9.4: SCTM Automation via Machine-Readable Format (OSCAL) for Tool-Based Control Traceability**
    - **Description:** Maintain the matrix as OSCAL rather than as a spreadsheet, generating it from the same machine-readable source the SSP is authored in so that a control's implementation is stated once and rendered into both artifacts.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Generate the SSP and SCTM from one source so they cannot disagree, paired with SSP Machine-Readable Authoring/Maintenance. It is Level 3, with the most value for large tailored sets or shared common controls.

### GV-5.10: Ongoing Authorization

**Design Intent:** Continuous monitoring results feed the ISSM's view of KESTREL's authorization posture. The triggers for AO review are agreed in advance. They include a new interconnection, partner nation, spoke, payload vendor, or foundation model, any change to the CCSD's information types, and activation of the alternate site. The ISSM reports authorization status to the AO each quarter.

**NIST Control Mapping:**

- **CA-6 (partial):** claimed for updating authorizations at a defined frequency, while the Authorization to Operate (ATO) Process holds the other four elements.
- **Declined:** CA-6(1) is declined at the ATO Process, and CA-6(2) is held by Inherited Control Validation. CA-7 is not claimed, since its strategy elements belong to the Continuous Monitoring Plan (ConMon), its monitoring slices are held elsewhere, including CA-7(3), CA-7(4), and CA-7(6), and this outcome consumes monitoring and acts on it under CA-6. PM-31 belongs to ConMon, and CA-5 and PM-4 to the Plan of Action and Milestones (POA&M).

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **GV-5.10.1: Continuous Monitoring Data Feed into Authorization Posture**
    - **Description:** Take the control status, assessment results, drift findings, and remediation state the Compliance focus area's continuous monitoring program produces, and maintain them as a current view of whether each authorization condition and each control the decision rested on still holds.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity consumes monitoring from the Compliance focus area's Continuous Monitoring Plan (ConMon) and related outcomes. Judge whether each finding touches a control the authorization rested on. Start with the sources the program already has.

- **GV-5.10.2: Risk-Based Reauthorization Trigger Criteria**
    - **Description:** Agree with the authorizing official in advance which system changes, categorization changes, findings, and elapsed intervals require reauthorization, which require notification only, and which require nothing, and publish the criteria where the people making changes will encounter them.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Agree criteria with the AO in advance, written against changes engineers recognize, such as new interconnections, categorization increases, hosting changes, replaced controls, or lapsed conditions. AI programs add new model versions, prompt or guardrail changes, new use cases, and failed adversarial re-tests. Publish them in Asset Lifecycle Change Control and the Configuration Management Plan (CMP), apply them through Security Impact Analysis (SIA), and reuse them for attestation reissue and categorization reassessment.

- **GV-5.10.3: Periodic Authorization Status Reporting**
    - **Description:** Report authorization posture to the authorizing official on the committed cadence, covering the standing of each condition, the changes assessed against the trigger criteria since the last report, and any control whose status has moved in a way that bears on the decision.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the practical half of the outcome's CA-6 (partial) claim. Report as exceptions against the trigger criteria, drawing figures from the posture view and Compliance focus area reporting. It is not tagged Visualize because it delivers a reported determination.

### GV-5.11: Security Impact Analysis (SIA)

**Design Intent:** Every change the Configuration Control Board sees gets a Security Impact Analysis record, which asks whether the change alters anything the authorization was granted against. Standard changes run against a standing classification. Significant changes go to the AO before they are made, and each change's controls are verified afterward.

**NIST Control Mapping:**

- **CM-4 (partial):** claimed for system-level impact analysis covering boundary, interconnections, information types, categorization, and SCTM implementations. Asset Lifecycle Change Control and System Prompt Governance hold the other, asset-level slices. It also covers network, identity, and OT changes and routes privacy impacts to Privacy Impact Assessments (PIA).
- **CM-4(2) (full):** carried by Post-Change Control Verification, which checks that affected controls work after a change. No other outcome claims it.
- **Declined:** CM-4(1) stays with Pre-Implementation Change Testing and Validation. CM-3 stays with the change processes and the Configuration Control Board, since this outcome informs approval. CA-6 belongs to the Authorization to Operate (ATO) Process and Ongoing Authorization.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **GV-5.11.1: SIA Intake and Change Classification**
    - **Description:** Route every proposed change from each change process in the framework, including asset, network, identity, application release, model and prompt, and OT/ICS maintenance changes, into a single SIA intake, and classify each by the components, interconnections, and controls it touches before any of them is approved.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the intake half of the outcome's CM-4 (partial) mapping. Take results from existing asset-level analyses, and analyze network, identity, and OT/ICS changes directly. Record standard changes pre-classified by the Configuration Control Board against that classification, and make sure no change class bypasses intake.

- **GV-5.11.2: Security and Privacy Impact Determination and SIA Record**
    - **Description:** Determine each change's security and privacy impact on the boundary, interconnections, information types, categorization, and control implementations the authorization rests on, and record the determination, its rationale, and the analyst in a per-change SIA record the SCA and AO can request.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the analytical core of the outcome's CM-4 (partial) mapping, asking whether a change affects anything the authorization was granted against. Route PII changes to Privacy Impact Assessments (PIA). Keep a self-explanatory SIA record per change.

- **GV-5.11.3: Significance Determination and Authorization Routing**
    - **Description:** Decide each analyzed change's significance against the sibling Ongoing Authorization's reauthorization trigger criteria, route every significant change to the SCA and AO before it is implemented, and flag the SSP, SCTM, CCSD, and authorization package updates each change requires.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Apply Risk-Based Reauthorization Trigger Criteria, and report non-significant changes through Periodic Authorization Status Reporting. Analyze emergency changes retrospectively and report significant ones to the AO. Owning outcomes make the flagged SSP, SCTM, and CCSD updates.

- **GV-5.11.4: Post-Change Control Verification**
    - **Description:** After a change is implemented, verify that the controls its SIA record identified as affected are implemented correctly, operating as intended, and still meeting their security and privacy requirements, and record the result against that SIA record.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-4(2) (full) mapping. It checks control function, unlike Post-Change Configuration Validation, which checks the baseline. Scope it from the SIA record, and reuse Automated Technical Control Compliance Monitoring results where they exist.

### GV-5.12: Inherited Control Validation

**Design Intent:** Before KESTREL inherits any control, the ISSM confirms the provider's authorization is current. The providers are the cloud provider's IL5 provisional authorization, the Boundary Cloud Access Point, the CSSP, the cross domain service provider, and the alternate site's facility. Each provider's customer responsibility matrix is merged into the SCTM. Provider authorization status is checked each quarter, and the reciprocity terms are recorded with each agreement.

**NIST Control Mapping:**

- **SA-9 (partial):** claimed for requirements, oversight, and compliance monitoring of providers whose controls the authorization inherits. Other outcomes hold the other provider slices.
- **CA-6(2) (partial):** claimed for systems answering to more than one authority. It is partial because the authorities perform the authorization acts, and this outcome records their terms.
- **Declined:** CA-2(3) is held by Control Assessment Scheduling. CA-6 acceptance of inherited controls belongs to the Authorization to Operate (ATO) Process, which this outcome supports.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The IL5 cloud provider and DISA, which publishes its provisional authorization. The Boundary Cloud Access Point, the CSSP, the cross domain service provider, and the parent organization's facility, for the controls KESTREL inherits from each.

**Security Impact:** High

**Activities:**

- **GV-5.12.1: Provider Authorization Verification**
    - **Description:** Before inheriting any control, verify that the provider's offering holds a current authorization at the impact level the program requires, covering the specific services the program uses rather than the provider as a whole, and record the authorization, its level, and its expiry.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's SA-9 (partial) mapping. Verify per service and impact level, since a provider's IL5 compute authorization may not cover a later-added service. For DoD cloud, this is the provisional authorization at the required impact level.

- **GV-5.12.2: Customer Responsibility Matrix Integration into the SCTM**
    - **Description:** Bring each provider's customer responsibility matrix into the SCTM, recording every affected control as inherited, shared, or program-owned, and assign each shared and program-owned responsibility to the outcome that implements it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's SA-9 (partial) mapping. Assign every shared responsibility in the provider's matrix to a named SABER outcome so nothing falls between the two sides.

- **GV-5.12.3: Provider Authorization Status Monitoring**
    - **Description:** Monitor each provider's authorization status, responsibility matrix revisions, and significant changes for as long as the program inherits from it, and route any change that affects an inherited control to the Security Impact Analysis (SIA).
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's SA-9 (partial) mapping for the monitoring element. Run a provider's lapse, scope reduction, or new conditions through the same significance determination as an internal change.

- **GV-5.12.4: Reciprocity and Joint Authorization Terms**
    - **Description:** Where the program accepts another authority's authorization or the system answers to more than one authority, record the terms on which each authority accepts the other's decisions, which overlays and conditions each imposes, and how a change approved by one reaches the other.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-6(2) (partial) mapping. It is Level 2, but mandatory for a system holding both SCI and SAP data. Record the terms before the first change tests them.
