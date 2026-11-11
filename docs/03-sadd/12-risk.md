# RK: Risk

*KESTREL SADD, Section 5 (Manage). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## RK-1: Risk Assessment and Treatment

### RK-1.1: Risk Assessment Methodology

**Design Intent:** The PMO ISSE defines one semi-quantitative method based on NIST SP 800-30, scoring likelihood and impact on five-point scales and combining them in a matrix. Impact is anchored to the CCSD's categorization and to mission effects. Anything that could cost an aircraft, compromise the command link, or expose CCSD row 13's key material scores at the top. The Security Team and the team leads are trained on the method, and the PMO ISSE reviews it each year.

**NIST Control Mapping:**

- **PM-9 (partial):** Claimed by prior reservation for the method component of the risk management strategy, which the scoring model, its guidance, and its recalibration produce. The tolerance component is held by the sibling Risk Appetite and Tolerance Definition, and the two claims are tracked together. The third component, risk mitigation approaches, is claimed by no outcome, though the sibling Risk Acceptance Process and Plan of Action and Milestones (POA&M) discharge it in practice. PM-9 has no enhancements in SP 800-53 Rev 5.
- **Declined:** RA-3's conduct, integration, and documentation elements are already held elsewhere, and defining the scoring method is not conducting an assessment. RA-1's family policy belongs to Security Governance Structure's Security Policy Framework, with a procedure slice in the Vulnerability and Patch Management Plan (VPMP). PM-28 belongs to the sibling Risk Appetite and Tolerance Definition.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **RK-1.1.1: Risk Assessment Methodology Definition**
    - **Description:** Select the scoring model the program will use, fix the likelihood and impact scales and the matrix or formula that combines them, and document the resulting methodology together with the evidence a scorer must hold before assigning a rating.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the develop element of the outcome's PM-9 (partial) mapping. Choose qualitative or quantitative honestly, since a quantitative model the program cannot feed with loss data produces false precision. Make the top band reachable, and treat any change to the units as a change to the outcomes that consume them, such as Supply Chain Risk Assessment and Dependency Mapping and the Enterprise Remediation Ranking Model.

- **RK-1.1.2: Methodology Application Guidance and Training**
    - **Description:** Write worked examples applying the methodology to real findings from the program's own estate, and instruct the roles that score risk through the Security Awareness and Training Program's role-based curriculum rather than a parallel training program.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the implement-consistently element of the outcome's PM-9 (partial) mapping. Draw worked examples from findings the program has already scored, including at least one scored wrongly the first time. AT-2 and AT-3 stay with the Security Awareness and Training Program.

- **RK-1.1.3: Methodology Periodic Review and Update**
    - **Description:** Recalibrate the methodology on the cadence its approval fixed, adjusting the scales when the register shows ratings clustering at one end, when a scored decision is overturned on appeal, or when the program's mission, categorization, or threat picture changes.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the review-and-update element of the outcome's PM-9 (partial) mapping. Read the score distribution, since a register where nearly everything is moderate has a scale that stopped discriminating. After a scale change, rescore the existing population and re-express the sibling Risk Appetite and Tolerance Definition's bands in the new units in the same cycle.

### RK-1.2: Risk Appetite and Tolerance Definition

**Design Intent:** KESTREL's appetite is lowest for risk to flight safety, the command link, and key material, where only Very Low residual risk is tolerated without AO action. It is moderate for analytic availability and for development environments. Each tolerance band maps to an acceptance authority. The ISSM may accept Low, the program manager Moderate, and only the AO High or Very High. The statement is reviewed each year with the steering committee.

**NIST Control Mapping:**

- **PM-28 (partial):** Its tolerance, trade-off, distribution, and review elements map directly onto this outcome's three activities. The assumptions and constraints elements stay with the sibling Risk Assessment Methodology's scoring model, so the claim is partial. PM-28 has no enhancements in SP 800-53 Rev 5.
- **PM-9 (partial):** Claimed by the same prior reservation for the tolerance component of the risk management strategy, while the sibling Risk Assessment Methodology holds the method component.
- **Declined:** RA-7 belongs to the outcomes that actually respond to findings, including the sibling Risk Acceptance Process. Setting the tolerance is not responding to a finding, so claiming RA-7 here would misstate what this outcome does.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RK-1.2.1: Risk Appetite/Tolerance Statement Development**
    - **Description:** Write the appetite and tolerance statement, setting for each mission-criticality and data-sensitivity tier the residual risk the program will carry without further action, the band that requires treatment, and the band never carried, along with the priorities and trade-offs behind each.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the tolerance and trade-off elements of the outcome's PM-28 (partial) mapping and the whole of its PM-9 (partial) slice. Express the bands in the sibling Risk Assessment Methodology's units so a rating maps to a band without translation. Avoid a single organization-wide band, and publish the statement where risk owners and approval workflows will see it.

- **RK-1.2.2: Tolerance-to-Acceptance-Authority Tier Alignment**
    - **Description:** Map each tolerance band to the authority entitled to accept a risk that lands in it, from the ISSO and ISSM through the PMO ISSE to the authorizing official, and record the mapping in the place the program's acceptance and exception workflows will read it from.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Write the ladder once here, since the sibling Risk Acceptance Process, Policy Exception Management, the AI/ML Governance Review Board, and the AI/ML Vendor/Model Risk Assessment all read it by name. Make the authorizing official the top rung, bind each tier to a role rather than a person, and state who decides when the entitled authority is unavailable.

- **RK-1.2.3: Periodic Review and Revision**
    - **Description:** Revisit the appetite and tolerance statement on the cadence its approval fixed and whenever the mission, categorization, threat picture, or the program's own acceptance record indicates the bands no longer describe what is actually being carried.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the review-and-update element of the outcome's PM-28 (partial) mapping. Use the acceptance record as input, since a band that is routinely exceeded and accepted is a tolerance already revised in practice. When thresholds move, re-run the consuming outcomes and set a transition position for acceptances granted under the old band. The AI/ML Governance capability's Program-Level AI Threat Assessment feeds AI/ML threat changes here, and AI/ML tiers stay in these bands.

### RK-1.3: Risk Register and Tracking

**Design Intent:** The ISSM keeps one risk register that receives risks from every source. Sources include threat models and the architecture risk register, penetration tests, the SCA, continuous monitoring, AI certification acceptances, and supply chain assessments. Each risk carries an owner, a score, a treatment, and a review date, and it links to its POA&M items and SCTM controls. The steering committee reviews the register each month, and a risk posture dashboard shows it to leadership.

**NIST Control Mapping:**

- **RA-3 (partial):** Claimed for the element that integrates organization and mission-level results with system-level risk assessments, which a single register fed from every tier performs. Other outcomes hold the conduct element, and the sibling Risk Assessment Report (RAR) holds documentation and update. The base is cited because RA-3's enhancements do not address integration.
- **PM-6 (partial):** Claimed by prior reservation for the risk register population's own performance measures. Security Governance and Steering Committee holds the leadership-level aggregation above it. PM-6 has no enhancements in Rev 5.
- **Declined:** CA-5 and PM-4 belong to the sibling Plan of Action and Milestones (POA&M), which holds the remediation commitment while this register holds the risk. CA-7(4) belongs to the Application focus area's Architecture Risk Tracking, and CA-7's strategy and frequency to the Continuous Monitoring Plan (ConMon).

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RK-1.3.1: Risk Register Structure and Intake Process**
    - **Description:** Define the register's schema, namely the fields every entry carries and the states it can occupy, and open a named intake route from each finding source the program has so that a risk identified anywhere reaches the register regardless of who happened to notice it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-3 (partial) integration claim. Include fields for the source finding and the affected control, and populate the treatment decision from the SP 800-30/SP 800-39 response taxonomy of mitigate, accept, avoid, and transfer/share. Name the intake routes, such as STIG Risk Tracking and the sibling Emerging Technology Risk Assessment, and deduplicate on intake rather than at review.

- **RK-1.3.2: Risk Owner Assignment and Status Tracking**
    - **Description:** Assign every register entry a named individual accountable for its treatment and hold each entry's status current through that owner, rather than through a periodic sweep performed by the security organization on everyone's behalf.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Assign each risk to a named person rather than a team. A risk the program cannot own, such as a supplier weakness or an inherited common control, is escalated rather than assigned to whoever is nearest. Owners maintain their own status, since status kept by the security organization goes stale between reviews.

- **RK-1.3.3: Risk Register Periodic Review and Reporting**
    - **Description:** Work the register on a fixed cadence with the owners present, re-scoring entries whose circumstances changed and closing those whose treatment completed, then report the population's shape to the steering committee and the ISSM.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Report the population's shape, namely aging by score band and owner, rather than a list of open entries. Escalate decisions the review cannot settle through Governance Decision/Action Item Tracking. Send an entry nobody intends to treat to the sibling Risk Acceptance Process rather than leaving it open.

- **RK-1.3.4: Risk Register Automation/Integration with POA&M and SCTM**
    - **Description:** Integrate the register with the POA&M and the SCTM so that a risk, the remediation plan answering it, and the control it bears on are linked records maintained once, and generate the views each of the three needs from that single store rather than from three synchronized copies.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity discharges the automation content CA-5(1) contributed to PM-4, though the claim stays with the sibling Plan of Action and Milestones (POA&M). Link records rather than synchronizing them, and pair the work with SCTM Automation via Machine-Readable Format (OSCAL) for Tool-Based Control Traceability. It is Level 2 because many programs maintain the three by hand.

- **RK-1.3.5: Enterprise Risk Posture Dashboard**
    - **Description:** Build the view showing register status by score band and owner, POA&M item aging against milestone dates, and every entry currently sitting above the program's tolerance thresholds, refreshed from the integrated store rather than assembled by hand before each meeting.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-6 (partial) mapping. The threshold-breach panel matters most, showing each entry above tolerance as treated, accepted, or neither. Build it on the sibling integration activity rather than on exports, and feed the Security Program Metrics/Posture Dashboard for Leadership Reporting rather than duplicating it.

### RK-1.4: Risk Acceptance Process

**Design Intent:** A risk owner proposes an acceptance through the service desk, and the ISSM scores it against the tolerance bands, which route it to the right authority. Every acceptance records its rationale, compensating measures, and an expiry no later than one year. CCSD tailoring action 3, which expires on 2027-09-30, is the model. Acceptances are re-reviewed before they expire, and an expired acceptance becomes an open finding.

**NIST Control Mapping:**

- **RA-7 (partial):** Claimed for the population no gate covers, namely general risk register entries and residuals routed here by name from other outcomes. Seven other outcomes hold gate-level slices, such as Vulnerability and Patch Management. A request under Policy Exception Management whose residual exceeds tolerance is escalated here. RA-7 has no enhancements in SP 800-53 Rev 5.
- **Declined:** CA-6 belongs to the Authorization Management capability, since these decisions are made under a delegation inside an existing authorization rather than being a CA-6 authorization act. CA-5 and PM-4 belong to the sibling Plan of Action and Milestones (POA&M), and a finding both accepted now and scheduled later carries an entry in each.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RK-1.4.1: Risk Acceptance Request and Approval Workflow**
    - **Description:** Open the route by which a risk owner proposes an acceptance with its residual score, the compensating measures relied on, and a proposed duration, and send each request to the authority the sibling Risk Appetite and Tolerance Definition's tier alignment entitles to grant it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-7 (partial) mapping, and routing by tolerance band is what enforces it. The entitled authority is never the team whose delivery the finding blocks. Require compensating measures in each request, and send a request that cannot state a duration to Policy Exception Management or to the AO.

- **RK-1.4.2: Risk Acceptance Documentation and Expiration Tracking**
    - **Description:** Record each granted acceptance in the risk register as an entry carrying the accepted risk, the granting authority, the compensating measures, and a mandatory expiration date, and track those dates so an expiry surfaces before it passes rather than after.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Give every acceptance an expiration, following the Artificial Intelligence focus area's log. Hold acceptances in the sibling risk register so the dashboard shows accepted risk beside open risk. Reference the source finding rather than restating it, so a re-tested finding updates one record.

- **RK-1.4.3: Risk Acceptance Periodic Re-Review**
    - **Description:** Re-decide each acceptance at its expiration and on the program's review cadence against the current tolerance bands, and treat one that has been extended repeatedly as a finding about the program rather than about the risk.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Re-decide rather than renew, against the tolerance bands as they now stand. Report the extension count, since it separates a program that keeps re-deciding from one that decided once. Where the condition has become remediable, close the acceptance and open a sibling Plan of Action and Milestones (POA&M) item.

### RK-1.5: Security Assessment Plan

**Design Intent:** The SCA authors the Security Assessment Plan for each assessment cycle. It covers the cloud, the data center, the alternate site, the fleet through spares and the simulator, and the AI models through their evidence annexes. The ISSM and the PMO ISSE review its scope against the SCTM, and the AO approves it. It is revised each cycle and whenever the boundary changes.

**NIST Control Mapping:**

- **CA-2 (partial):** Claimed for developing the control assessment plan and having the AO approve it before the assessment. The sibling Security Assessment Report (SAR) holds the report elements, while Control Assessment Scheduling and Annual Security Review hold assessor selection and execution. Outcomes that declined CA-2 toward the Compliance focus area assess nothing, so this split by element honors them. Treat CA-2 as met only when all of these are built.
- **Declined:** CA-2(1), CA-2(2), and CA-2(3) concern who assesses and how, so they stay with Control Assessment Scheduling and Annual Security Review. None describes plan authoring more precisely than the CA-2 base. PL-2 belongs to the System Security Plan (SSP), since the plan describes testing rather than implementation.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The SCA, who assesses KESTREL independently for the AO.

**Security Impact:** Moderate

**Activities:**

- **RK-1.5.1: Security Assessment Plan Development and Authoring**
    - **Description:** Author the security assessment plan, listing each control and enhancement in the tailored set that the cycle will assess, the examine, interview, and test procedures that determine effectiveness for each, and the assessment environment, team composition, and role assignments it will run under.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the plan-development element of the outcome's CA-2 (partial) mapping. Draw the control list from the Security Controls Traceability Matrix (SCTM) rather than a second copy. Use the catalog's assessment procedures and write local ones only for tailored and overlay controls. Author the plan with any independent assessor, since a procedure they reject is a deferred scoping argument.

- **RK-1.5.2: Security Assessment Plan Review and Approval**
    - **Description:** Circulate the plan to the ISSM and the assessment team for review, and obtain the authorizing official's or designated representative's approval of it before any assessment activity begins.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the review-and-approval element of the outcome's CA-2 (partial) mapping. Obtain approval before fieldwork, since approval after it does not meet the control. An approved plan ends the scope argument, and it also fixes the cadence the sibling revision activity runs on.

- **RK-1.5.3: Security Assessment Plan Periodic Review and Revision**
    - **Description:** Revise the assessment plan whenever the AO retailors the control set, the system changes materially, or a previous cycle showed a procedure that could not produce a determination, and re-approve it on the cadence its approval fixed.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Use the previous report as the main input, since a control failed for want of evidence signals a procedure defect. Control Assessment Scheduling sets which controls each cycle covers, while this activity revises the plan. AO retailoring arrives through the SCTM, so a current SCTM makes revision a diff.

### RK-1.6: Security Assessment Report (SAR)

**Design Intent:** The SCA writes the SAR, recording a determination and its evidence for every control assessed. The ISSM checks it for factual accuracy without changing any determination, and the SCA delivers it to the AO with the package.

**NIST Control Mapping:**

- **CA-2 (partial):** Claimed for producing the assessment report and providing results to defined roles. The sibling Security Assessment Plan holds the plan elements, and Control Assessment Scheduling and Annual Security Review hold the rest. Recurring cycle findings are reported through this outcome rather than a second format.
- **Declined:** CA-2(1), CA-2(2), and CA-2(3) go with assessor selection. RA-3 belongs to the sibling Risk Assessment Report (RAR), since a control determination is not a statement of risk. CA-5 and PM-4 belong to the sibling Plan of Action and Milestones (POA&M), which keeps remediation commitments out of the assessor's report.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The SCA, who assesses KESTREL independently for the AO.

**Security Impact:** High

**Activities:**

- **RK-1.6.1: SAR Development and Authoring**
    - **Description:** Document, for every control and enhancement the approved plan placed in scope, the assessor's determination, the evidence examined to reach it, and the specific weakness or deficiency behind any determination other than satisfied.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the report-production element of the outcome's CA-2 (partial) mapping. Protect the evidence citation when the schedule compresses, and record a determination for every scoped control, including those that passed. Write each weakness with its component and condition so a POA&M item can be opened directly from it.

- **RK-1.6.2: SAR Review and Validation**
    - **Description:** Check the report against the approved assessment plan for coverage, confirm that every determination is supported by the evidence cited, and resolve factual disputes with the system owner before delivery rather than after.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Keep validation factual rather than editorial, which preserves the report's independence. Check coverage against the plan to catch scoped controls no procedure was run against. Record both positions on an unresolved dispute rather than dropping the finding.

- **RK-1.6.3: SAR Delivery to AO/Stakeholders**
    - **Description:** Deliver the validated SAR to the authorizing official and to the ISSM, system owner, and program stakeholders the program's distribution list names, and record each delivery together with the handling caveats the report carries.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the results-provision element of the outcome's CA-2 (partial) mapping. Settle the recipient list in advance, including the risk owners in the sibling Risk Register and Tracking, not the AO alone. The SAR keeps the system's marking and PSO handling path. It enters the package through Authorization Package Compilation, while its weaknesses go to the sibling Plan of Action and Milestones (POA&M).

### RK-1.7: Risk Assessment Report (RAR)

**Design Intent:** The SCA writes the RAR. It reads the SAR's findings, the open risk register, and the current threat picture together to show what they mean for KESTREL's mission. It is reviewed with the ISSM and the PMO ISSE and delivered to the AO alongside the SAR.

**NIST Control Mapping:**

- **RA-3 (partial):** Claimed for documenting results in a risk assessment report and for reviewing, disseminating, and updating them. Other outcomes hold the conduct element, and the sibling Risk Register and Tracking holds integration. The base is cited because RA-3's enhancements do not address reporting. The RAR stays separate from the SSP, which records implementation rather than remaining risk.
- **Declined:** CA-2 belongs to the sibling Security Assessment Plan and Security Assessment Report (SAR), since a risk synthesis is not a control determination. CA-5 and PM-4 remain with the sibling Plan of Action and Milestones (POA&M), since stating a risk is not committing to remediate it.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The SCA, who assesses KESTREL independently for the AO.

**Security Impact:** High

**Activities:**

- **RK-1.7.1: RAR Development and Authoring**
    - **Description:** Convert the SAR's deficiency determinations, the register's open entries, and the current threat picture into stated risks, scoring each on the program's methodology and recording the threat source, the vulnerability, the mission function affected, and the residual remaining after in-place controls.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the documentation element of the outcome's RA-3 (partial) mapping. Synthesize rather than transcribe, since five low findings that defeat one control objective are one material risk, and a lone high finding may be less. Take threat context from the Threat Intelligence capability, and score in the sibling Risk Assessment Methodology's units.

- **RK-1.7.2: RAR Review and Validation**
    - **Description:** Review the report with the ISSM and the risk owners, confirming that each stated risk traces to a SAR finding or register entry, that scores were applied consistently with the methodology, and that no material finding was lost in the synthesis.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the review element of the outcome's RA-3 (partial) mapping. Check traceability both ways, so every risk has a finding and every finding is either in a risk statement or recorded as immaterial. Check scoring consistency across authors, and turn any assumed compensating control into a register entry.

- **RK-1.7.3: RAR Delivery to AO/Stakeholders**
    - **Description:** Issue the reviewed RAR to the authorizing official and the stakeholders the program names, then update and reissue it when a significant change to the system, its environment of operation, or its threat picture invalidates the risk it described.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the dissemination and update elements of the outcome's RA-3 (partial) mapping. Significant change is defined by Risk-Based Reauthorization Trigger Criteria, so a reauthorization trigger also triggers a risk restatement. The report enters the package through Authorization Package Compilation, and under ongoing authorization it anchors the AO's status reporting.

### RK-1.8: Plan of Action and Milestones (POA&M)

**Design Intent:** The ISSM opens a POA&M item for every weakness KESTREL intends to fix, whether it comes from the SAR, a penetration test, continuous monitoring, or a STIG finding. Each item carries its owner, corrective action, resources, and dated milestones. Milestones are reviewed each month and reported to the AO each quarter. An item closes only when its fix is verified and the evidence is attached.

**NIST Control Mapping:**

- **CA-5 (partial):** Claimed by prior reservation for the program-level POA&M process, milestone monitoring, and closure verification. The Application focus area's STIG Risk Tracking holds the application-layer register feeding it. CA-5 is cited at the base because CA-5(1) was withdrawn into PM-4.
- **PM-4 (partial):** Claimed for the process that develops, maintains, and reports plans of action and reviews them against the risk strategy. The strategy and priorities are held by the sibling Risk Assessment Methodology, the sibling Risk Appetite and Tolerance Definition, and the Enterprise Risk Prioritization capability. PM-4 has no enhancements in Rev 5.
- **Declined:** RA-7 belongs to the sibling Risk Acceptance Process, so a finding both remediated and accepted carries an entry in each. CA-7 remains with the Continuous Monitoring Plan (ConMon). ATO Condition/POA&M Closure Tracking reads this plan rather than keeping a second register.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **RK-1.8.1: POA&M Item Creation and Tracking**
    - **Description:** Open an item for each finding the program will remediate, linking it to the source finding and the control it bears on and recording the planned corrective action, the resources required, the milestones, the scheduled completion date, and the accountable owner.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the development and maintenance elements of the outcome's CA-5 (partial) and PM-4 (partial) mappings. Every SAR weakness needs an item or an acceptance, and every item needs a source finding. Items arrive from every finding source, such as STIG Risk Tracking and Vulnerability and Patch Management. Fill the resource estimate, which CA-5 names explicitly.

- **RK-1.8.2: POA&M Milestone Monitoring and Status Reporting**
    - **Description:** Track each item against its milestone dates as they come due, escalating a slip before the scheduled completion date rather than reporting it afterwards, and report the plan's status on the cadence the program's reporting requirements set.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the reporting element of the outcome's PM-4 (partial) mapping. Watch for a missed interim milestone with an unchanged end date. Report slip rate and aging through the sibling Enterprise Risk Posture Dashboard. Escalate slips on authorization-condition items on the authorization's terms, since ATO Condition/POA&M Closure Tracking reads them from here.

- **RK-1.8.3: POA&M Closure Verification and Evidence Collection**
    - **Description:** Close an item only against evidence that the weakness is actually corrected, retesting or rescanning where the finding originated in a test or a scan, and file that evidence through the program's evidence repository rather than inside the plan itself.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Verify closure separately rather than on the owner's assertion, and retest by the method that produced the finding. Where the fix changed an implementation, update the SSP through SSP Periodic Review and Revision. File closure evidence through Compliance Evidence Collection and Retention.

### RK-1.9: Emerging Technology Risk Assessment

**Design Intent:** The chief engineer and the PMO ISSE watch the technologies likely to reach KESTREL, such as new foundation models and agent frameworks, new payload sensors, new datalink and satellite communications, and post-quantum cryptography. Each one is assessed before adoption through the intake path, and the risks it brings that the current controls do not cover go into the register.

**NIST Control Mapping:**

- **Declined:** No SP 800-53 Rev 5 control covers assessing a technology the program has not adopted, so this outcome is unmapped. Its exposures enter the register and are treated under cited outcomes. RA-3's elements are fully allocated, and a candidate outside the boundary is not a system in the RA-3 sense. PM-15 and PM-16 belong to the Threat Intelligence capability. SA-2 and SA-3 belong to Capability Gap Identification and Planning. SI-5 covers advisories, and a technology trend is not an SI-5 advisory.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **RK-1.9.1: Emerging Technology Horizon Scanning**
    - **Description:** Maintain a watch list of technologies plausibly reaching the program's estate within its planning horizon, drawn from standards bodies, vendor roadmaps, research publications, and the program's own engineering intentions, and refresh it on a set cadence.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Scope the watch list to what could plausibly reach this program. Use the program's own engineering roadmap and prototypes as the main input, since most new technology arrives from inside. It is Level 3 because no assessor requires a watch list.

- **RK-1.9.2: Technology Adoption Risk Assessment Process**
    - **Description:** Assess each watch-list technology that reaches a serious adoption discussion for the exposures it would introduce, the controls the program would need before fielding it, and the exposures the existing tailored control set could not cover, and score the result on the program's risk methodology.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Focus on the control gap rather than the score, since uncovered risks need a design answer before purchase. Hand AI or ML candidates to AI/ML Use Case Inventory and AI/ML Vendor/Model Risk Assessment. Record an environment where the technology cannot be fielded as a scoped exclusion.

- **RK-1.9.3: Emerging Tech Risk Findings Integration into Risk Register**
    - **Description:** Enter each assessed technology's material exposures into the risk register as owned entries carrying a treatment decision, so that an exposure identified before adoption stays visible after it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Enter findings through the sibling Risk Register Structure and Intake Process's named routes, scored on the same methodology as live risks. Close an entry for a declined technology with its reasoning rather than deleting it, since the question usually returns.

## RK-2: Threat Intelligence

### RK-2.1: Threat Intelligence Program

**Design Intent:** The Security Team runs KESTREL's threat intelligence function, with a named analyst role. Its requirements focus on adversaries targeting ISR and unmanned systems, attacks on datalinks and navigation, and attacks on AI supply chains and models. Sources are the CSSP, DoD intelligence products, and the performer's DIB threat sharing. The Security Team reviews the program and its sources each year.

**NIST Control Mapping:**

- **PM-16 (partial):** Claimed by prior reservation from Correlated Threat Detection and Analytics for the threat awareness program itself, namely its requirements, sources, analysts, and maturity review. The sibling Indicator Sharing and Enrichment holds the sharing capability the control requires, and the two are tracked together.
- **Declined:** PM-16(1) belongs to the sibling Indicator Sharing and Enrichment. PM-15's contact is performed by that sibling and Threat Landscape Monitoring rather than by the charter. SI-5 is held by Correlated Threat Detection and Analytics and Vulnerability and Patch Management, since the charter chooses sources rather than receiving advisories. RA-10 belongs to the Enterprise Threat Hunting Program.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The CSSP and DoD intelligence producers, which supply threat intelligence. DC3's DIB Cybersecurity program, through the performer.

**Security Impact:** Moderate

**Activities:**

- **RK-2.1.1: Threat Intelligence Program Charter and Source/Feed Strategy**
    - **Description:** Charter the threat intelligence function, stating the intelligence requirements the program needs answered, the commercial, government, open-source, and community feeds selected to answer each one, and the review point at which a source answering none of them is dropped.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the program-implementation half of the outcome's PM-16 (partial) mapping. Write requirements before the source list, focusing on questions whose answer would change a decision. Review the recurring feed cost at renewal. The sources set here are the means for the sibling Threat Landscape Monitoring's RA-3(3) claim.

- **RK-2.1.2: Threat Intelligence Analyst Function/Roles Definition**
    - **Description:** Define the analyst function by position rather than by name, stating who is accountable for producing the program's threat assessments, the skills and access the role requires, and whether the function is staffed internally, drawn from a parent organization, or bought as a service.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** In most programs this function is a fraction of one position, so state that plainly while keeping accountability with a named role. Where the function is bought or drawn from a parent organization, the program still owns requirements and tasking. Train the role through the Security Awareness and Training Program's role-based curriculum.

- **RK-2.1.3: Program Maturity Assessment and Periodic Review**
    - **Description:** Assess the threat intelligence function against a stated maturity model on the program's cadence, scoring requirements coverage, source utility, analyst throughput, and whether anything the function produced changed a decision, and record the shortfalls as improvement items.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the review dimension of the outcome's PM-16 (partial) mapping. Measure whether intelligence changed any detection, remediation order, or risk score, rather than reporting volume. Send shortfalls that represent real exposure to the sibling capability's Risk Register and Tracking. It is Level 3 because no assessor requires a maturity score.

### RK-2.2: Threat Landscape Monitoring

**Design Intent:** The intelligence analyst tracks the actors and campaigns likely to target KESTREL's mission and the techniques they are adopting. These include datalink jamming and spoofing and MITRE ATLAS techniques against models. A monthly threat brief goes to the steering committee and the risk register, and urgent changes go to the ISSM at once.

**NIST Control Mapping:**

- **RA-3(3) (full):** The three activities determine the current threat environment on an ongoing basis, using the sources the sibling Threat Intelligence Program selects. No other outcome claims the enhancement.
- **PM-15 (partial):** Claimed for maintaining currency with security practices through community contact, which the tradecraft watch performs. The sibling Indicator Sharing and Enrichment holds the information-sharing purpose, and the Security Awareness and Training Program serves education. PM-15 has no enhancements in Rev 5.
- **Declined:** The RA-3 base stays with its existing holders, since threat context is an input to assessments rather than one. RA-3(2) belongs in the Risk Assessment Report (RAR) where a program has all-source access. RA-3(4) is out of SABER scope, since predictive analytics needs a dedicated analytic capability no program architecture defines. SI-5 is held by Correlated Threat Detection and Analytics and Vulnerability and Patch Management. SI-5(1) stays unclaimed because a leadership report is not an automated alert.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** The CSSP and DoD intelligence producers.

**Security Impact:** Moderate

**Activities:**

- **RK-2.2.1: Strategic Threat Actor/Campaign Tracking**
    - **Description:** Maintain the tracked set of threat actors and campaigns credibly relevant to this mission, sector, and technology estate, recording for each what it targets, how it gains and keeps access, and what the program would expect to observe if it were present.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's RA-3(3) (full) mapping. Keep the tracked set short and relevant to this program. End each profile with observable expectations the Enterprise Threat Hunting Program can hunt from, and do not argue attribution.

- **RK-2.2.2: Emerging TTP (tactics, techniques, procedures) Monitoring**
    - **Description:** Watch for tradecraft newly observed in the wild, map each technique against the controls and detections the program has actually built, and record the ones that would currently succeed as findings rather than as reading.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's RA-3(3) (full) mapping together with its PM-15 (partial) claim. Map techniques to a common taxonomy so each can be compared against existing coverage. Enter a technique that would currently succeed into the sibling capability's Risk Register and Tracking. Do not tune only for novelty, since most intrusions use old tradecraft.

- **RK-2.2.3: Threat Landscape Reporting to Leadership/Risk Function**
    - **Description:** Issue a periodic threat landscape assessment to the steering committee, the ISSM, and the risk function, stating what changed since the last one, which of the program's controls the change bears on, and what it recommends be done differently.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Write the report against decisions rather than events. It supplies the threat context for the Risk Assessment Report (RAR) and informs the Enterprise Remediation Ranking Model. Track resulting decisions through Governance Decision/Action Item Tracking.

### RK-2.3: Indicator Sharing and Enrichment

**Design Intent:** KESTREL shares and receives indicators through the CSSP and, for the performer's side, through DC3's DIB Cybersecurity program. The analyst vets each incoming indicator for quality and relevance before it reaches detection. Vetted indicators go to the indicator feeds in the security monitoring platform.

**NIST Control Mapping:**

- **PM-16 (partial):** Claimed for the cross-organization information-sharing capability the control requires. The sibling Threat Intelligence Program holds the program itself, and the two are tracked together.
- **PM-16(1) (full):** The structured exchange and machine-readable hand-off are the automated sharing mechanisms, and no other outcome shares intelligence outside the program.
- **PM-15 (partial):** Claimed for sharing security information through institutionalized contact with selected groups. The sibling Threat Landscape Monitoring holds the currency purpose, and the Security Awareness and Training Program serves education. PM-15 has no enhancements in Rev 5.
- **Declined:** Internal indicator distribution belongs to Indicator of Compromise (IOC) Feed Management under SI-4(24) and SI-5, and alert-time context to Threat Intelligence Enrichment under SI-5. This outcome supplies the vetted indicators those mechanisms distribute.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Third-Party Application (COTS), Security Information and Event Management (SIEM) Platform, Cross-Domain/Boundary Transfer

**External Dependencies:** The CSSP, and DC3's DIB Cybersecurity program through the performer.

**Security Impact:** Moderate

**Activities:**

- **RK-2.3.1: Inter-Org/ISAC Indicator Sharing Participation**
    - **Description:** Join the sharing organizations, information sharing and analysis centers, and government sharing programs relevant to the mission and sector, execute the membership and handling agreements each requires, and stand up the structured-format exchange the program will use to both receive and contribute indicators.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-15 (partial) mapping and part of its PM-16 (partial) and PM-16(1) (full) mappings. Contribute as well as consume. Settle handling rules, including any PSO release determination, before an indicator is queued. The exchange typically uses STIX and TAXII. It is not tagged Automate because the substance is membership and release discipline rather than transport.

- **RK-2.3.2: Strategic Indicator Curation and Quality Vetting**
    - **Description:** Vet each candidate indicator for provenance, confidence, age, and relevance to the program's own estate before admitting it, and reject or down-confidence the ones whose only claim is that they appeared on a list.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's PM-16 (partial) mapping. Vet on provenance and relevance rather than volume. Assign confidence and expiry here, while Indicator of Compromise (IOC) Feed Management enforces aging under the CMP. It is not tagged Automate because it is analyst judgment.

- **RK-2.3.3: Indicator Hand-Off to Operate Pillar's IOC Feed Management**
    - **Description:** Deliver the vetted indicator set to the Operate pillar's Indicator of Compromise (IOC) Feed Management in the structured, machine-readable form its ingestion path consumes, carrying each indicator's source, confidence, and expiry rather than the value alone.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's PM-16(1) (full) mapping. Ship source, confidence, and expiry with each indicator, typically as STIX over TAXII. In an air-gapped enclave delivery follows the approved transfer rotation, which is why the outcome cites Cross-Domain/Boundary Transfer.

## RK-3: Enterprise Risk Prioritization

### RK-3.1: Risk-Based Remediation Prioritization

**Design Intent:** One ranking orders remediation across every team. It combines the risk score, the asset's mission criticality, known exploitation, and exposure, so a known exploited flaw on a DMZ-facing or fleet asset outranks everything else. The team leads and the ISSM agree priorities each week, and the PMO ISSE recalibrates the model each quarter against what was actually exploited.

**NIST Control Mapping:**

- **PM-4 (partial):** Claimed by prior reservation for the organization-wide priorities for risk response, which the ranking model, workflow, and recalibration write down. The sibling Plan of Action and Milestones (POA&M) holds the rest of PM-4 and reviews against these priorities. PM-4 has no enhancements in SP 800-53 Rev 5.
- **Declined:** RA-7 belongs to outcomes that dispose of findings, and ordering work disposes of none. Holders of RA-7 slices include Vulnerability and Patch Management and the sibling Risk Acceptance Process, so claiming RA-7 here would misstate this outcome. PM-28 and PM-9 stay with the sibling Risk Appetite and Tolerance Definition and Risk Assessment Methodology. RA-5 stays with Vulnerability and Patch Management, whose ranking this model consumes. CA-5 remains with the sibling Plan of Action and Milestones (POA&M), since re-ranking reorders that plan.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RK-3.1.1: Enterprise Remediation Ranking Model**
    - **Description:** Define the ranking function that orders remediation work across the program from the finding's score on the risk methodology, its tolerance band, the mission criticality the business impact analysis assigned the affected process, and the effort the fix requires, and state how ties are broken.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-4 (partial) mapping. Take scores from Risk Assessment Methodology, bands from Risk Appetite and Tolerance Definition, and criticality from the sibling Business Impact Analysis (BIA). Include effort, and state the tie-break.

- **RK-3.1.2: Cross-Team Remediation Prioritization Workflow**
    - **Description:** Run the recurring forum in which the ranked backlog is worked across teams, allocating the program's remediation capacity against the model's order and recording every deviation from it with the reason and the authority that approved it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Record every deviation from the model. Plan against real capacity. Resequencing moves milestone dates on the sibling Plan of Action and Milestones (POA&M) rather than creating a second schedule. Send a finding that cannot be sequenced to the sibling Risk Acceptance Process.

- **RK-3.1.3: Prioritization Periodic Recalibration**
    - **Description:** Recalibrate the ranking model on a set cadence against what the program actually worked, adjusting the weights when the deviation record shows the model and the practice disagreeing consistently in the same direction.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Use the deviation log as input, since a consistent one-way override means a weight is wrong. Recalibrate whenever the methodology scales or tolerance bands change. Re-rank the existing backlog after a change so the queue holds one vintage of priority.

### RK-3.2: Business Impact Analysis (BIA)

**Design Intent:** The business impact analysis works through KESTREL's mission processes, namely flying and controlling the aircraft, collecting and ingesting data, detecting and analyzing, releasing to partners, and retraining models. The intelligence mission leads and Fleet Operations set how long each process can be lost. The results set the criticality tiers that Recovery's recovery objectives and the incident severity model use. The analysis is reviewed each year and after any significant change.

**NIST Control Mapping:**

- **PM-11 (partial):** Claimed for defining mission and business processes with their protection needs, which the analysis does. AI/ML Use Case Inventory and the AI/ML Governance Review Board hold the other two elements. PM-11 has no enhancements in SP 800-53 Rev 5.
- **Declined:** RA-9 covers components rather than mission processes, and Asset Criticality and Business Impact Assessment plus the AI robustness outcomes already hold it. CP-2(8) belongs to the Contingency Plan (CP), which reads this outcome. CP-2(3) belongs to Recovery Objective Definition (RTO/RPO). RA-2 belongs to Security Categorization, which bounds this analysis.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Identity Platform, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RK-3.2.1: BIA Methodology Definition and Criticality Tiering**
    - **Description:** Define how business impact will be measured, fixing the consequence categories the analysis scores against, the time horizons over which loss is assessed, and the criticality tiers a scored process lands in, and record the tiers against the asset register the recovery and response determinations already read.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's PM-11 (partial) mapping. Score against mission consequence rather than cost. Ask what is lost after an hour, a day, and a week, since RTO/RPO Determination per System/Data Criticality Tier reads those horizons. Align tiers with Business Impact Classifications.

- **RK-3.2.2: BIA Execution per System/Mission-Critical Process**
    - **Description:** Work each system and mission-critical process through the methodology with its mission owner, recording the essential functions it supports, the impact of its loss over each defined horizon, the upstream dependencies it cannot run without, and the criticality tier that results.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the substance of the outcome's PM-11 (partial) mapping. Trace derivative dependencies such as identity, network, and data pipelines, which owners usually omit. Interview the mission owner rather than the system owner, and avoid reducing the work to a survey.

- **RK-3.2.3: BIA Periodic Review and Update**
    - **Description:** Re-run the analysis for an affected process whenever the mission it supports, the systems supporting it, or its dependencies change materially, and review the whole population on the program's cadence so that no criticality tier is older than the estate it describes.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the update dimension of the outcome's PM-11 (partial) mapping. Trigger review on mission changes, which no configuration process notices. When a tier moves, re-run Recovery Objective Definition (RTO/RPO), the Contingency Plan (CP), and Asset Criticality and Business Impact Assessment.
