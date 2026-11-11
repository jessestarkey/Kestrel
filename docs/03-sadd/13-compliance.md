# CO: Compliance

*KESTREL SADD, Section 5 (Manage). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## CO-1: Regulatory and Framework Compliance

### CO-1.1: Regulatory Compliance Mapping

**Design Intent:** The PMO ISSE inventories what binds KESTREL and on what authority. That includes DoDI 8510.01 and the Cloud Computing SRG at IL5, and the CUI program under DoDI 5200.48. It also includes DFARS 252.204-7012 and the CMMC clauses for the performer, the Privacy Act and DoDI 5400.11, and the foreign disclosure rules governing partner releases. Each is broken into requirements and mapped to the outcomes that satisfy it, and gaps go to the gap register. The inventory is checked each quarter for new or revised issuances.

**NIST Control Mapping:**

- **Declined:** No SP 800-53 Rev 5 control takes conformance to an obligation outside the catalog as its subject, which is why AI/ML Regulatory Mapping declined every control it examined. PM-1 is not reopened, since its clauses already split across Security Policy Framework and two other outcomes. CA-1 stays with Security Policy Framework, and this outcome writes no assessment procedure. CA-2 and its three enhancements are reserved for Control Assessment Scheduling and Annual Security Review, since a crosswalk is not an assessment result. SI-5 covers vulnerability advisories, and a revised acquisition rule is not one.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** DoD, OMB, and the other issuers whose requirements bind KESTREL.

**Security Impact:** Moderate

**Activities:**

- **CO-1.1.1: Regulatory/Framework Requirement Inventory**
    - **Description:** Identify every statutory, contractual, and framework obligation the program is bound by, recording for each one the instrument, the authority or contract clause that binds the program to it, and the part of the program it reaches.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The basis matters as much as the instrument, since a voluntarily adopted framework and a flowed-down contract clause call for different responses to the same unmet requirement. The instruments most often missed arrive by flow-down, so read the contract file and the subcontract terms that Contract Security Requirements maintains alongside the published sources. Record which holding, such as CUI, export-controlled data, or personal information, triggers which instrument so the inventory can be re-derived when holdings change.

- **CO-1.1.2: Requirement-to-Control Mapping and Gap Analysis**
    - **Description:** Decompose each inventoried instrument into discrete testable requirements, map every requirement to the outcomes and control implementations that satisfy it, and record each requirement nothing satisfies as a gap with a named owner and a route to closure.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Decompose to the requirement rather than to a framework's top-level focus area, since a crosswalk drawn at that altitude reads as coverage it does not prove. Map to the outcome and control identifier the Security Controls Traceability Matrix (SCTM) already carries rather than restating implementations. The register also absorbs the AI-specific rows from Control-to-Requirement Traceability Maintenance, so carry the source instrument on every row. A gap with no owning outcome goes on the Plan of Action and Milestones (POA&M).

- **CO-1.1.3: Regulatory Landscape Monitoring and Update Process**
    - **Description:** Assign a named position to watch the statutory, acquisition, and framework landscape that binds the program, and re-run the inventory and gap analysis whenever an instrument is revised, a new clause is flowed down, or the program takes on a holding or mission that brings it into scope of requirements that did not previously apply.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Run this watch and its AI/ML Regulatory Mapping counterpart as one function with two subject lists, since the same person usually notices both kinds of change. The trigger that produces the most missed obligations is a contract modification adding a clause, so the watch covers the contract file and not only the standards bodies. Where a revision changes an existing requirement, re-run as a diff against the current register, which keeps a quarterly cadence affordable.

### CO-1.2: Automated Technical Control Compliance Monitoring

**Design Intent:** Scheduled scans evaluate every surface against its baseline. Authenticated scans with DISA SCAP content cover hosts, configuration checks cover the cloud, benchmark checks cover containers, and manufacturer baselines cover fleet equipment. Their machine-readable results feed one compliance status view. Drift from a baseline alerts the owning team, and each finding is tracked to closure under the VPMP's deadlines.

**NIST Control Mapping:**

- **CA-7(6) (partial):** claimed for keeping technical control monitoring results accurate, current, and available through automated scheduling, consolidation, and a staleness signal. The Application focus area's Compliance Evidence Collection Automation holds the rest of the enhancement for its own evidence artifacts, and the two are tracked jointly.
- **Declined:** CM-6, CM-6(1), and CM-6(2) are not reopened, since Device Compliance, the configuration monitoring outcomes, and others already set and check those settings, and this outcome only consumes their results. CA-7 at the base is held in slices by other outcomes, with its strategy elements reserved for the Continuous Monitoring Plan (ConMon), so the scheduling activity follows the ConMon cadence. CA-7(1) goes with the assessor-selection element reserved for Control Assessment Scheduling and Annual Security Review, alongside CA-2 and its three enhancements. CA-7(3) is trend analysis, held by STIG Risk Tracking and the ConMon. CA-7(5) covers determinations about results, which belong to the sibling capability. CA-5 and PM-4 remain the Plan of Action and Milestones (POA&M)'s, so remediation binds to existing POA&M items.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Database Service, Object/File Storage, Network Infrastructure, Directory/Platform Core Infrastructure, First-Party/Custom Application Code, Self-Hosted Third-Party Application (COTS), Industrial Controller/SCADA, Legacy IT (Unpatchable, Non-Industrial), AI/ML System

**External Dependencies:** DISA, which publishes the STIGs and SCAP content the scans use.

**Security Impact:** Moderate

**Activities:**

- **CO-1.2.1: Technical Control Compliance Status Aggregation and Scheduling**
    - **Description:** Set the running order and frequency of the program's STIG and benchmark evaluations against the cadence the ConMon fixes, and ingest each evaluation's machine-readable output into a single compliance status store keyed to the asset and the baseline it was checked against.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the currency and availability dimensions of the outcome's CA-7(6) (partial) mapping. Ingest the machine-readable output rather than a rendered report, since the raw result carries the rule identifiers later comparison depends on. Flag any asset that has not reported inside its expected window, because a scanner that silently stopped covering a subnet otherwise produces a clean view.

- **CO-1.2.2: Compliance Drift Detection and Alerting**
    - **Description:** Compare each incoming evaluation against the asset's last accepted state and alert the accountable owner when a rule that previously passed now fails, or when a newly covered rule fails on its first evaluation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the accuracy dimension of the outcome's CA-7(6) (partial) mapping. Alert on the transition rather than the standing state, so long-accepted deviations do not bury the one that changed. Route the alert to the asset owner rather than the compliance function. The OT/ICS case ends at the alert, with no automated correction.

- **CO-1.2.3: Non-Compliant Finding Remediation Tracking**
    - **Description:** Track every non-compliant finding to a disposition of fixed, deviated, or accepted, and bind any finding that will not close inside the program's remediation window to the POA&M item that owns it rather than opening a milestone here.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity builds no second plan of action. The Plan of Action and Milestones (POA&M) holds the corrective action and closure, and this activity binds findings from surfaces STIG Risk Tracking does not cover. Record whether a finding closed by a fix or by an approved deviation granted through Policy Exception Management. An OT finding usually disposes as a tracked deviation with a compensating control, since its change window is a plant outage.

### CO-1.3: Compliance Evidence Collection and Retention

**Design Intent:** One program evidence repository receives the pipeline's evidence store, continuous monitoring results, and each team's process records. Each artifact is tagged to its control and outcome. Artifacts are held for their record class's retention, and authorization evidence is held for the life of the authorization. Before each assessment cycle, the ISSOs check the repository for gaps and stale artifacts, and a compliance posture dashboard shows its state.

**NIST Control Mapping:**

- **SI-12 (partial):** claimed for retaining the program's compliance and assessment evidence, such as assessment reports, scan results, attestations, POA&M history, and audit artifacts, a population no other outcome holds. Policy Lifecycle Management, the Data Management Plan (DMP), and others declined it and named this outcome for program records. The base is cited because SI-12(1), SI-12(2), and SI-12(3) address personal information and disposal techniques, held by the DMP, Inference-Time PII Handling, and Media Sanitization and Destruction Procedures.
- **PM-6 (partial):** claimed for the dashboard activity, which Security Governance and Steering Committee and other outcomes named as the control-level feeder view. The claims are disjoint by population and tracked together, and PM-6 has no enhancements in Rev 5.
- **Declined:** AU-11 and AU-11(1) are held in full by Log Retention Strategy over the audit record estate, which is a different store from this evidence repository. CA-7(6) belongs to the sibling Automated Technical Control Compliance Monitoring, which left only the retention half, the SI-12 claim above, to this outcome. CA-2 and its enhancements are reserved for Control Assessment Scheduling and Annual Security Review. AU-9 is not reopened, since Audit Log Integrity Protection holds it for the audit record estate.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Backup/Archive Repository, CI/CD Pipeline, First-Party/Custom Application Code, Virtual Machine/Server, Serverless/Platform Service

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **CO-1.3.1: Evidence Collection Automation (per control/assessment cycle)**
    - **Description:** Receive each pillar's evidence feed into the program repository as artifacts are produced, tagging every artifact with the control it supports, the assessment cycle it falls in, and the system state it describes.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is unrelated to the identically named Response focus area activity, which captures forensic artifacts off a compromised system. Receive evidence from pipelines that already produce it, such as the Evidence Export Pipeline, rather than re-collecting it and creating two copies with two timestamps. Artifacts captured at production time show a control operated across the period, while a set regenerated before an assessment shows only that the tool still runs. Control-system evidence is entered by hand.

- **CO-1.3.2: Evidence Repository Management and Retention Policy Enforcement**
    - **Description:** Operate the evidence repository under access control, immutability, and versioning appropriate to the classifications it holds, and enforce a retention period per evidence class that meets the longest obligation the requirement register carries for it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-12 (partial) mapping. Set retention from the longest applicable obligation in Regulatory Compliance Mapping's register rather than from the assessment cycle, since contract clauses often outlive the authorization. Keep the store append-only for artifacts and versioned for records that legitimately change, such as POA&M status history. Make disposition a deliberate, recorded action rather than a silent platform expiry.

- **CO-1.3.3: Evidence Completeness/Quality Validation**
    - **Description:** Check the collected set against the controls the assessment cycle covers, flagging every control with no artifact, every artifact past the validity window its producing cadence implies, and every artifact that does not actually show what it is tagged as showing.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Report a control with no artifact and one with a stale artifact separately, since the first is a collection gap and the second is a cadence problem. The quality check is human, which is why Control Type is Process, because automation can confirm a screenshot exists but not that it shows the required setting. Run the check ahead of the cycle Control Assessment Scheduling sets, since a gap found a quarter early is a task rather than a finding.

- **CO-1.3.4: Compliance Posture Dashboard**
    - **Description:** Build a view that shows each control's current status alongside the age of its supporting evidence, open audit findings by source and severity, and POA&M items aging against their milestone dates, refreshing it from the repository and the registers rather than assembling it ahead of each review.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-6 (partial) mapping. It feeds Security Program Metrics/Posture Dashboard for Leadership Reporting rather than duplicating it. Lead with control status read against evidence age, since a control reported satisfied on eleven-month-old evidence is the row an assessor opens first. Read audit findings from Internal Audit Program and External Audit Coordination rather than re-tracking them.

## CO-2: Continuous Monitoring Program

### CO-2.1: Continuous Monitoring Plan (ConMon)

**Design Intent:** The ISSM authors KESTREL's continuous monitoring plan. It names the metrics monitored, how often each is collected, how often each control is assessed, and who receives the results. The AO approves it, and it is revised each year and with every significant change. Security status goes to the AO each month in summary and each quarter in full.

**NIST Control Mapping:**

- **CA-1 (partial):** claimed for the procedures dimension of the assessment, authorization, and monitoring family, which Security Policy Framework left to this plan. It follows the plan-type pattern that pairs AC-1 with the AMP, CM-1 with the CMP, SC-1 with the KMP, IR-1 with the IRP, and CP-1 with the CP. The assessment cadence is documented here, so Control Assessment Scheduling opens no separate CA-1 claim. The authorization-procedures dimension remains a recorded gap, and the review and designated-official clauses are held by Policy Lifecycle Management and Security Roles and Responsibilities.
- **CA-7 (partial):** claimed for developing the continuous monitoring strategy, its metrics, and its monitoring and assessment frequencies, as reserved by Ongoing Authorization and two other outcomes. The ongoing-assessment and monitoring elements are held as partial slices by AMP Compliance Verification and other outcomes. This outcome tells those monitors how often to run rather than acting as another one.
- **CA-7(3) (partial):** claimed for trend analysis over the program's monitoring results as a whole, deciding whether frequencies, metrics, or activity types should change. STIG Risk Tracking holds the application-layer finding slice, and the two are tracked jointly.
- **PM-31 (partial):** claimed as the organization-level twin of CA-7 for the same three elements plus program-level status reporting. The ongoing-monitoring, correlation, and response clauses are performed by the outcomes this plan directs, so the claim stays partial. PM-31 has no enhancements in SP 800-53 Rev 5.
- **Declined:** CA-7(4) is Architecture Risk Tracking's, and CA-7(6) is split between Compliance Evidence Collection Automation and Automated Technical Control Compliance Monitoring. CA-7(1) is Control Assessment Scheduling's and CA-7(5) is Annual Security Review's, since the plan neither employs an assessor nor reaches a finding. CA-2 is split between the Security Assessment Plan, the Security Assessment Report (SAR), and the two sibling outcomes below. CA-6 is held by Ongoing Authorization and Authorization to Operate (ATO) Process, which also declined CA-6(1) and CA-6(2). CA-5 and PM-4 remain the Plan of Action and Milestones (POA&M)'s.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **CO-2.1.1: ConMon Development and Authoring**
    - **Description:** Author the continuous monitoring plan, naming the metrics the program will monitor, how often each is monitored and how often each control family's effectiveness is assessed, who receives security status reporting and on what cadence, and the procedures the program's assessment and monitoring functions run under.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the strategy, metric, and frequency elements of the outcome's CA-7 (partial) and PM-31 (partial) mappings and the whole of its CA-1 (partial) claim. Choose a metric only if a decision changes when it moves. Tier assessment frequencies by how fast each control decays rather than spreading them evenly across a calendar. Write frequencies precisely enough that Automated Technical Control Compliance Monitoring and Control Assessment Scheduling can build their schedules from them without interpretation.

- **CO-2.1.2: ConMon Review and Approval**
    - **Description:** Circulate the plan to the ISSM and the system owner for review and obtain the authorizing official's approval of it, recording the approved monitoring and assessment frequencies as the cadence every dependent outcome schedules against.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** AO approval makes a frequency binding rather than aspirational. Raise any cadence the program cannot resource before approval, since an agreed quarterly check is a decision while a monthly one performed twice a year is a finding. Approval also fixes the cadence the sibling revision activity runs on.

- **CO-2.1.3: ConMon Periodic Review and Revision**
    - **Description:** Revise the plan on the cadence its approval fixed and whenever the accumulated monitoring record shows that a frequency, metric, or type of monitoring activity is producing findings nobody acts on or missing findings the program discovers by other means, then re-approve the revised cadence.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-7(3) (partial) mapping, covering monitoring results as a whole rather than the application-layer population STIG Risk Tracking holds. Revise downward as readily as upward, since several clean cycles justify relaxing a frequency. The most useful input is a finding learned from an audit, an incident, or a vendor notice, which shows a metric or activity type is missing.

### CO-2.2: Control Assessment Scheduling

**Design Intent:** Every control is assessed at least once in a three-year cycle, with a third of the families each year. Controls that change often, such as identity, configuration, vulnerability, and AI model controls, are assessed each quarter or continuously. The SCA runs the independent assessments, and the ISSOs run self-assessments between them. Completion is tracked, so a slipped cycle reaches the AO.

**NIST Control Mapping:**

- **CA-2 (partial):** claimed for selecting the assessor or assessment team. The control is split four ways, with Security Assessment Plan holding plan development, Security Assessment Report (SAR) holding reporting, and Annual Security Review holding the assessment itself. All four claims are partial, so treat CA-2 as satisfied only when all four are built. Earlier outcomes such as Zero Trust Maturity Assessment and Roadmap declined CA-2 in favor of this outcome and Annual Security Review.
- **CA-2(1) (full):** employing independent assessors, claimed in full because nothing else in the framework employs an assessor.
- **CA-2(3) (full):** leveraging external assessment results that meet the program's acceptance requirements, claimed in full because nothing else decides whether an external result substitutes for the program's own.
- **CA-7(1) (full):** employing independent assessors for ongoing monitoring, taken from Automated Technical Control Compliance Monitoring. The assignment activity names assessors for every cycle, including the annual review's, so the enhancement is not split.
- **Declined:** CA-2(2) is left to Annual Security Review, since choosing which forms of assessment to include is that outcome's methodology decision. CA-7 at the base is the Continuous Monitoring Plan (ConMon)'s, and this outcome only turns its frequencies into dated cycles. CA-1 is discharged at the ConMon, where the calendar is documented as a procedure. CA-5 and PM-4 remain the Plan of Action and Milestones (POA&M)'s.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The SCA, who runs the independent assessments.

**Security Impact:** Moderate

**Activities:**

- **CO-2.2.1: Control Assessment Calendar/Cadence Definition**
    - **Description:** Place every control in the tailored set into a frequency tier and lay the tiers onto a dated calendar, giving each control family a cycle that the ConMon's approved assessment frequencies allow rather than one chosen here.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Draw the control list from the Security Controls Traceability Matrix (SCTM) rather than restating it, so the calendar never drifts from what the AO tailored. Tier by how quickly a control decays and what its failure costs, since a calendar with everything on an annual cycle is not a schedule. Each cycle runs against the Security Assessment Plan, so this activity sets the sequence and dates rather than the procedures.

- **CO-2.2.2: Assessor Assignment and Coordination**
    - **Description:** Name the assessor or assessment team for each scheduled cycle, determine the independence that cycle requires, and coordinate access, scheduling, and any external organization's assessment results the program will leverage instead of assessing a control itself.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-2 (partial), CA-2(1) (full), CA-2(3) (full), and CA-7(1) (full) mappings in full. Independence depends on the reporting line, so record that an assessor does not report to the system owner being assessed. Settle in advance what a leveraged external assessment must contain and how recent it must be, which applies to the inherited and common controls the SCTM records. An engaged independent assessor co-authors the assessment plan.

- **CO-2.2.3: Assessment Completion Tracking and Reporting**
    - **Description:** Track each scheduled cycle from assignment through to a delivered determination, and report cycles completed, slipped, and not started against the calendar so a control that has gone unassessed past its tier's interval is visible as a finding rather than as a blank.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Surface any control whose last determination has aged past its tier's interval, since a determination without a date reads like one reached last week. Show it on the Compliance Posture Dashboard rather than a separate tracker. The determinations themselves are delivered through the Security Assessment Report (SAR), while this activity reports only whether each cycle ran.

### CO-2.3: Annual Security Review

**Design Intent:** The ISSM leads an annual security review across the whole boundary, including the cloud, the data center, the alternate site, and the fleet. It records a determination and evidence for every control in that year's scope and confirms that earlier fixes still hold. Its findings go to the risk register and the POA&M, and its report goes to the AO.

**NIST Control Mapping:**

- **CA-2 (partial):** claimed for assessing the controls annually to determine whether they are implemented correctly, operating as intended, and producing the desired outcome. Security Assessment Plan, Security Assessment Report (SAR), and Control Assessment Scheduling hold the other three elements. Findings are reported through the SAR rather than a second report format.
- **CA-2(2) (full):** including specialized forms of assessment, such as vulnerability scanning and malicious user testing, in the control assessment at a defined frequency. Red Teaming and Adversary Emulation and Detection Validation declined it in favor of this outcome, whose scope activity decides which of their techniques the annual cycle includes.
- **CA-7(5) (full):** validating that policies are established and controls operate consistently, taken from Automated Technical Control Compliance Monitoring. It is full because that outcome's view is only an input, and nothing else asks whether a control is implemented consistently across enclaves.
- **Declined:** CA-7 at the base belongs to the Continuous Monitoring Plan (ConMon), and CA-7(1) to Control Assessment Scheduling. CA-7(3) is split between the ConMon and STIG Risk Tracking, CA-7(4) is Architecture Risk Tracking's, and CA-7(6) is split between Compliance Evidence Collection Automation and Automated Technical Control Compliance Monitoring. CA-6 is held by Authorization to Operate (ATO) Process and Ongoing Authorization, which declined CA-6(1) and CA-6(2). CA-5 and PM-4 remain the Plan of Action and Milestones (POA&M)'s, so the integration activity opens items there.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **CO-2.3.1: Annual Review Scope and Methodology Definition**
    - **Description:** Fix which controls the annual cycle covers, which examine, interview, and test methods determine effectiveness for each, and which specialized forms of assessment the cycle includes, such as vulnerability scanning, malicious user testing, and insider threat assessment.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the selection half of the outcome's CA-2(2) (full) mapping and defines the actions its CA-7(5) (full) mapping employs. Take the standing procedures from the Security Assessment Plan, and feed any defect back through that plan's revision activity. State any surface that cannot be assessed in the window, since an unstated omission reads as coverage. Choose specialized forms against the program's actual threat picture rather than including all of them.

- **CO-2.3.2: Annual Review Execution and Findings Documentation**
    - **Description:** Execute the cycle against the defined scope, recording for every control in scope a determination of whether it is implemented correctly, operating as intended, and producing the intended outcome, along with the evidence examined and the specific weakness behind any determination other than satisfied.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the assess-the-controls element of the outcome's CA-2 (partial) mapping, the execution half of its CA-2(2) (full) mapping, and the performing half of its CA-7(5) (full) mapping. Reach the consistency determination by comparing implementations across enclaves rather than assessing each in isolation. Record a determination for every control in scope, including satisfied ones, so the record demonstrates coverage. Recurring cost is High because assessment labor is usually the program's largest recurring compliance expense.

- **CO-2.3.3: Annual Review Findings Integration into Risk Register/POA&M**
    - **Description:** Open a POA&M item for every weakness the cycle recorded that the program intends to remediate and a risk register entry for every one it intends to carry, linking each back to the determination it came from rather than restating it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity creates no second plan of action or register. Remediated findings become Plan of Action and Milestones (POA&M) items, and carried exposures go to Risk Register and Tracking. The point is that no weakness ends up with neither an item nor an acceptance. Accept a carried exposure through the Risk Acceptance Process so it inherits an expiration date.

## CO-3: Audit Management

### CO-3.1: Internal Audit Program

**Design Intent:** An auditor appointed by the program manager, independent of the performer teams, audits whether KESTREL's plans and procedures are carried out as written. Audits cover areas such as change records, access reviews, backup restore tests, and AI board decisions. The audit schedule reaches every governing plan at least once every two years. Findings are tracked until the fix is verified, and the audit charter is reviewed each year.

**NIST Control Mapping:**

- **PM-14 (full):** claimed because the control's subject is a process ensuring that security and privacy testing, training, and monitoring plans are developed, maintained, executed, and reviewed against the risk management strategy, which is what an audit does. The plans themselves keep their own citations, such as the ConMon's CA-7 and the AT-2, AT-3, AT-4, IR-3, and CP-4 holders. It is full because nothing else oversees the plan population as a whole. The outcome reviews against Risk Assessment Methodology and Risk-Based Remediation Prioritization rather than setting them. PM-14 has no enhancements in SP 800-53 Rev 5.
- **Declined:** Annual Security Review asks whether controls work, while this outcome asks whether the program follows its own documents, and the two fail independently. CA-2 is split across Security Assessment Plan, Security Assessment Report (SAR), Control Assessment Scheduling, and Annual Security Review. CA-2(1) and CA-2(3) are held full at Control Assessment Scheduling and CA-2(2) at Annual Security Review. CA-7 and its enhancements are already placed, and an audit examines conduct rather than control state. The AU family covers system audit records, which an audit engagement reads as evidence rather than produces. CA-5 and PM-4 remain the Plan of Action and Milestones (POA&M)'s. PM-1 and CA-1 stay with Security Policy Framework and Policy Lifecycle Management, so an outdated policy finding routes to them.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **CO-3.1.1: Internal Audit Charter and Scope Definition**
    - **Description:** Charter the internal audit function, fixing its authority to examine any process in the program, the reporting line that keeps it independent of the processes it audits, the population of plans and procedures inside its scope, and the criteria for recording a divergence from documented process as a finding.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the implement-a-process element of the outcome's PM-14 (full) mapping. Independence depends on the reporting line, so an ISSM auditing plans the ISSM wrote is a self-review. Name each plan and procedure in scope along with its owning position, rather than describing a category. State in advance which evidence decides whether a skipped step is a finding or an outdated document.

- **CO-3.1.2: Audit Schedule/Cadence and Execution**
    - **Description:** Lay out the audit schedule against the ConMon's approved cadence and the risk the program's remediation priorities attach to each process, then execute each engagement by comparing the documented process against the records it should have produced, the system state it should have left, and the accounts of the people who perform it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the developed-and-maintained and continue-to-be-executed determinations of the outcome's PM-14 (full) mapping and its review-for-consistency element. Review each plan against Risk Assessment Methodology, Risk Appetite and Tolerance Definition, and Risk-Based Remediation Prioritization. Interview the people who perform a process rather than its owners, since that is where practice diverges. Schedule by risk rather than rotating evenly, reaching first the processes whose failure would go unnoticed until an incident.

- **CO-3.1.3: Audit Findings Tracking and Remediation Verification**
    - **Description:** Track every audit finding to a disposition and verify remediation by re-examining the process itself rather than by accepting the owner's account, opening a POA&M item for any finding that will not close inside the program's remediation window.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity builds no second plan of action. Findings go to the Plan of Action and Milestones (POA&M) or Risk Register and Tracking and display on the Compliance Posture Dashboard. Close a finding only after re-examination shows changed practice, since an updated document alone changes nothing. A kept divergence is resolved by amending the document through Policy Lifecycle Management or by a bounded deviation through Policy Exception Management, never by rewriting the standard inside the audit report.

- **CO-3.1.4: Internal Audit Charter Periodic Review and Revision**
    - **Description:** Review the internal audit charter on the program's defined cadence and whenever the audit function's mandate or the program's organizational structure changes, updating its scope, its independence and reporting-line arrangement, and its finding criteria to match.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control claim, since the sibling activities already discharge PM-14, and PM-1 and CA-1 were declined at the outcome level. It audits the charter itself, the one document nothing else checks for currency. Revisit the independence and reporting-line arrangement first, since growth or reorganization most often erodes it. Feed revisions into the schedule and finding criteria the sibling activities use.

### CO-3.2: External Audit Coordination

**Design Intent:** The ISSM is the single intake point for external audits and inspections. These include inspectors general, GAO, cyber readiness inspections, and DCMA or DIBCAC reviews of the performer. The ISSM confirms each request's authority, scope, and deadline. Evidence is packaged from the program evidence repository rather than assembled anew, and findings are tracked to closure in the POA&M.

**NIST Control Mapping:**

- **Declined:** No SP 800-53 Rev 5 control covers receiving and answering an audit an external body conducts on the program. CA-2(3) is the reverse direction, consuming someone else's assessment, and is held full at Control Assessment Scheduling with CA-2(1) and CA-7(1). CA-2(2) and CA-7(5) are full at Annual Security Review, and nothing is assessed here to claim CA-2. The AU family covers audit records rather than engagements. PM-14 is Internal Audit Program's. SI-12 stays with Compliance Evidence Collection and Retention, from which this outcome draws a dated subset. SR-8 covers receiving supplier audit results and is Contract Security Requirements'. PM-6 is the Compliance Posture Dashboard's, and CA-5 and PM-4 remain the Plan of Action and Milestones (POA&M)'s. Record any AO-tailored audit-response requirement through gap identification.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Backup/Archive Repository, First-Party/Custom Application Code, Virtual Machine/Server, Serverless/Platform Service

**External Dependencies:** Inspectors general, GAO, DoD cyber readiness inspectors, DCMA, and DIBCAC, whose audits and inspections KESTREL responds to.

**Security Impact:** Moderate

**Activities:**

- **CO-3.2.1: External Audit Request/Notification Intake Process**
    - **Description:** Establish the intake path by which an external audit request or notification reaches a named position, recording for each one the requesting body, the authority it audits under, the scope and period it covers, and the response deadline it carries.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Record the authority the requesting body audits under, such as a statute, a contract clause in Regulatory Compliance Mapping's register, or an agreement in System Interconnection Agreements (ISA/MOU/MOA). Negotiate any request exceeding that instrument before answering it. Route intake to a named position rather than an inbox, so one response goes out. Triage scope on arrival, since the calendar commitment is negotiable only at the start.

- **CO-3.2.2: Audit Evidence Packaging and Response Coordination**
    - **Description:** Coordinate the response through a single point that assembles the requested artifacts from the program's evidence repository, reviews each one for classification, marking, and releasability before it leaves the program, and records what was furnished to whom on what date.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Assemble the response from Compliance Evidence Collection and Retention's repository rather than requesting fresh copies. Never skip the releasability review, since markings, proprietary content, or aggregation can change an artifact's sensitivity once it leaves the program. Keep a complete record of what was furnished, because the finding will be written against it. Plan hand extraction of isolated-enclave evidence into the response window.

- **CO-3.2.3: External Audit Findings Tracking and Closure**
    - **Description:** Track each finding the external body issues through the program's own registers to a recorded closure, furnishing whatever evidence of closure the auditor requires and confirming the finding is retired on the auditor's record as well as the program's.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Route an external finding to a Plan of Action and Milestones (POA&M) item or a Risk Register and Tracking entry, with acceptance through the Risk Acceptance Process. Only the auditor's closure counts, since an unretired finding returns as a repeat finding. Contest a disputed finding through the requesting body's reconsideration path and record that as the disposition. Carry the source instrument on each item, as Requirement-to-Control Mapping and Gap Analysis does.

## CO-4: Privacy Compliance

### CO-4.1: Privacy Program Management

**Design Intent:** The privacy officer is accountable for KESTREL's privacy program under DoDI 5400.11. The personal information it holds is user account records, service desk records, and incidental imagery of people in the collection. The privacy policy covers how each is collected, used, kept, and disposed of. Users can request correction of their own account records through the service desk. The program is reviewed each year.

**NIST Control Mapping:**

- **PT-1 (full):** claimed in full because Security Policy Framework declined PT-1 outright and left it to this capability, and Responsible AI Policy and Principles restated that. All three clauses land here, namely the policy and procedures at the charter activity, the designated official at the roles activity, and review at the periodic review activity. PT-1 has no enhancements in SP 800-53 Rev 5. The policy is still versioned and reissued through Policy Lifecycle Management.
- **PM-18 (full):** no other outcome claims the privacy program plan, which is the privacy counterpart of PM-1. It covers program structure, resources, requirements, controls, the senior privacy official and other roles, coordination, senior approval, and periodic review. PT-1 governs the privacy policy, while PM-18 governs the plan for the program that issues and staffs it. PM-18 has no enhancements in Rev 5.
- **PM-19 (full):** claimed nowhere else, for appointing the privacy official with authority, accountability, and resources. Since no separate privacy appointment outcome exists, one activity defines, assigns, and confers the role. A formal designation letter is filed in ISSO/ISSM Appointment Letters' register without opening a second PM-2 claim. PM-19 has no enhancements in Rev 5.
- **PM-5(1) (full):** claimed by prior reservation from AI/ML Use Case Inventory, which holds PM-5 partial for AI/ML and left the inventory of systems processing personal information to this outcome. The charter activity establishes the register, PIA Trigger Criteria and Intake Process populates it, and the review activity updates it. The base PM-5 is not reopened.
- **AT-3(5) (full):** claimed by prior reservation from Security Awareness and Training Program, which holds AT-3 full. This outcome names the personnel who process personal information and the content they need, while Role-Based Specialized Training delivers it. Neither AT-2 nor the AT-3 base is reopened.
- **PM-22 (full):** claimed for the process to correct or amend inaccurate personal information and propagate the correction to the system of record and every downstream recipient. PII Accuracy and Correction Request Handling runs both clauses, reading recipients from the charter's inventory. It is full because PM-22 has no enhancements in SP 800-53 Rev 5 and no other outcome corrects a value once found wrong.
- **Declined:** None of these controls has an activity here. PM-20, PM-21, PM-26, and PM-27 cover a public privacy webpage, disclosure accounting, redress, and oversight reporting. Like PM-20, they are department-level Privacy Act obligations outside SABER scope. PM-21 also sits on the Privacy Act boundary left unclaimed under PT-6. PM-24 applies only to a matching program under PT-8, which nothing establishes. PM-23 needs a data governance body, which no outcome charters. PM-25 stays with Data Minimization Requirement Definition, the single holder of minimization under SI-12(2). PT-4, PT-5, PT-6, PT-7, and PT-8 describe instruments no outcome issues, and Model Card Generation already declined PT-5.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The DoD component's privacy office, which oversees the privacy program.

**Security Impact:** Moderate

**Activities:**

- **CO-4.1.1: Privacy Program Charter and Policy Development**
    - **Description:** Charter the privacy program and author the privacy policy and its implementing procedures, fixing how the program collects, uses, retains, discloses, and disposes of personal information, the structure and resources the program receives, the requirements it answers to, the senior official who approves it, and the obligation to maintain a standing inventory of systems processing personally identifiable information under it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PT-1 (full) policy and procedures clause and the substance of its PM-18 (full) mapping. It also establishes the register the PM-5(1) (full) claim rests on and states the instruction content AT-3(5) (full) requires. Write the procedures with the policy, saying who decides collection and against what criteria. Draft with counsel and mission owners, since the policy mainly constrains what the mission may collect. Version it through Policy Lifecycle Management, and grant departures only through Policy Exception Management.

- **CO-4.1.2: Privacy Roles and Responsibilities Definition**
    - **Description:** Appoint the official accountable for the program's privacy position with the authority and resources to carry it, name the data steward responsible for each system that processes personal information, and identify the personnel whose work involves that processing so their required instruction can be scoped.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-19 (full) mapping, the designation clause of its PT-1 (full) mapping, the roles clause of its PM-18 (full) mapping, and the personnel determination behind AT-3(5) (full). Give the official real authority and time, since a title held alongside a full engineering workload is a privacy position on paper only. Bind a data steward position to each system on the inventory, reconciled against Role Assignment and RACI/Responsibility-Matrix Documentation. The recurring cost is staffing, and cutting it to collateral duty makes the capability nominal.

- **CO-4.1.3: PII Accuracy and Correction Request Handling**
    - **Description:** Establish a process for an individual, or the data steward acting for them, to request correction or amendment of inaccurate personally identifiable information, and propagate each approved correction to the authoritative system of record and to every downstream system or recipient the personally identifiable information inventory shows received the uncorrected value.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-22 (full) mapping. Read the systems to notify from the charter activity's inventory rather than rebuilding a recipient list per request. Route disputed corrections, or ones beyond the steward's authority, to the privacy official for adjudication. Log every request, disposition, and notified system, declines included. A request that questions whether the program should hold the data routes to PIA Trigger Criteria and Intake Process.

- **CO-4.1.4: Privacy Program Periodic Review**
    - **Description:** Review the charter, the privacy policy and procedures, the role and steward assignments, and the personally identifiable information inventory on the program's defined cadence and after any change in what the program collects or the authority it collects under, correcting whatever no longer matches how the program operates.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the review and update clauses of the outcome's PT-1 (full) and PM-18 (full) mappings and the defined-frequency update element of its PM-5(1) (full) mapping. Look for systems whose assessment predates their current processing, and route them to PIA Periodic Review/Reassessment on System Change. Unlike Internal Audit Program, this review asks whether the procedures are still right rather than whether people follow them. Send gaps such as an unfunded steward position to Risk Register and Tracking, with acceptance through the Risk Acceptance Process.

### CO-4.2: Privacy Impact Assessments (PIA)

**Design Intent:** KESTREL maintains a privacy impact assessment on DD Form 2930. It is reassessed whenever a new collection, sensor, AI use case, or partner release would process personal information. Incidental imagery is never retrieved by personal identifier, so KESTREL operates no system of records. Any capability that would retrieve by person must complete a new assessment first. The responsible AI policy prohibits identifying individuals, so such a capability also needs AI/ML Governance Review Board approval.

**NIST Control Mapping:**

- **RA-8 (partial):** claimed for assessments before developing or procuring IT that processes personal information, or starting a new collection, across the program's non-ML systems. Privacy Requirements Definition holds the ML slice, and ML use cases keep flowing through AI Use Case Intake and Onboarding. RA-8 has no enhancements in SP 800-53 Rev 5, so the population split lives in this rationale.
- **PT-2 (partial), PT-3 (partial):** claimed on the same population basis for PT-2a and PT-3a, which determine the authority for processing and the purposes it is limited to. PT-2b and PT-3c are enforcement, run by Data Discovery, Labeling, and Classification and Attribute-Based Data and Application Access Enforcement (ABAC). PT-3d, monitoring processing changes, is held by the reassessment activity. Privacy Requirements Definition keeps the ML slice of PT-2, PT-3, and RA-8, as Responsible AI Policy and Principles recorded.
- **Declined:** PT-2(1), PT-2(2), PT-3(1), and PT-3(2) cover tagging and automation, which sit on the enforcement side. PT-3b is PT-5's subject, which Model Card Generation declined, and is recorded as a gap since no outcome issues a privacy notice. RA-3 is less specific than RA-8, and RA-3 is already split across Deployment Risk Threshold Evaluation and two other outcomes. RA-2 is Security Categorization's. SI-12(1) and SI-12(2) stay with Data Minimization Requirement Definition and Data Retention and Disposition Schedule Definition.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Storage/Database, Application/API, Compute, Directory/Platform Core Infrastructure, Identity Lifecycle and Governance, Device/Workstation, AI/ML System, Industrial Controller/SCADA

**External Dependencies:** The DoD component's privacy office, which reviews and approves each assessment.

**Security Impact:** Moderate

**Activities:**

- **CO-4.2.1: PIA Trigger Criteria and Intake Process**
    - **Description:** Define the criteria that oblige an assessment, covering the development or procurement of any system that will process personal information and the initiation of any new collection of it, and establish the intake path that routes a triggered assessment to the privacy official and registers the system on the personally identifiable information inventory.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the trigger element of the outcome's RA-8 (partial) mapping and populates the PM-5(1) (full) register Privacy Program Management holds. Write the trigger against the collection, not only the system, since unassessed collections are usually additions to systems already fielded. Wire it into Application Intake and Onboarding, AI Use Case Intake and Onboarding, and Asset Lifecycle Change Control rather than relying on self-report. Route ML use cases to Privacy Requirements Definition instead.

- **CO-4.2.2: PIA Execution and Documentation**
    - **Description:** Conduct the assessment before the system is developed or procured and before the collection begins, documenting the authority the processing rests on, the purposes it is limited to, the personal information collected and its sources, how it is used, shared, retained, and disposed of, and the privacy risks identified with the mitigation selected against each.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PT-2 (partial) and PT-3 (partial) mappings and the substance of its RA-8 (partial) mapping. Run the assessment before fielding, since one run afterward documents a decision rather than informing it. Get the authority finding in writing from counsel, because possession is not permission. Read retention and minimization values from the Data Management Plan (DMP) and Data Minimization Requirement Definition. Accept unmitigated risks through the Risk Acceptance Process and open POA&M items for planned mitigations.

- **CO-4.2.3: PIA Periodic Review/Reassessment on System Change**
    - **Description:** Reassess an existing assessment whenever the system takes on a new data element, source, recipient, or purpose, or a changed retention period, and work through the assessed population on the program's cadence so no assessment omits processing the system has started or describes processing it has stopped.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries PT-3d and the update dimension of the outcome's RA-8 (partial) mapping. Privacy-relevant changes rarely arrive labeled as such, so wire reassessment to the Security Impact Analysis (SIA) performed before each change. A change of purpose that no longer fits the original authority returns through PIA Trigger Criteria and Intake Process as a new determination rather than an update.
