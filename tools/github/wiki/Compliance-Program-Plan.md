> **Notional system.** KESTREL is fictional. This page stands in for a governing document in KESTREL's self-hosted Confluence. Its names and decisions are invented to show a completed Compliance Program Plan.

# KESTREL Compliance Program Plan

This plan brings together how KESTREL keeps track of the rules it must follow and proves that it follows them. It covers the obligations that bind KESTREL, and how its controls are scheduled for assessment and by whom. It also sets the scope of the annual security review and how internal and external audits run. It carries out the design decisions in the [Compliance](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/13-compliance.md) section of the SADD.

The [Continuous Monitoring Plan](Continuous-Monitoring-Plan) and the [Privacy Program Charter and Policy](Privacy-Program-Charter-and-Policy) are separate documents, and this plan does not restate them.

**NIST Control Mapping:** none for the plan as a whole. Each section carries its own: Sections 1 and 5 carry none. Section 2 carries CA-2 (partial), CA-2(1), CA-2(3), and CA-7(1). Section 3 carries CA-2 (partial), CA-2(2), and CA-7(5). Section 4 carries PM-14.

> **Phasing.** The requirement mapping and the assessment scheduling start in Phase 2. The annual security review and the audit program start in Phase 3, with the SCA's assessment for the ATO. The first post-ATO assessment cycle starts after the ATO decision on 2028-09-30.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| Plan Version | 0.1 |
| Date | 2026-11-26 |
| Prepared By | PMO ISSE, with the ISSM, the parent organization's internal review office, and program legal counsel |
| Approved By | Each section's own authority, as Approval sets out |
| Source SADD Version | 0.9 |
| Source SIP Version | 0.8 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-26 | PMO ISSE | Initial draft for review |

---

## Purpose and Scope

This plan covers every obligation that binds KESTREL and every assessment and audit of it. Its readers are the people who answer for compliance: the ISSM, the SCA, the PMO ISSE, the internal review office, and program counsel. It sets methods and criteria. The dated schedules, registers, and reports those methods produce are living data, listed in the appendix.

---

## 1. Regulatory and Framework Requirement Mapping

*Traces to CO-1.1.1, CO-1.1.2, and CO-1.1.3. From Phase 2.*

**What binds KESTREL.** The PMO ISSE keeps an inventory of every obligation, with the authority that binds KESTREL to it and the part of KESTREL it reaches.

| Obligation | Why it binds KESTREL | What it reaches |
|---|---|---|
| DoDI 8510.01 | KESTREL is a DoD system authorized under the RMF | The whole system |
| CNSSI 1253 | KESTREL is a national security system | Control selection, through the CCSD |
| The Cloud Computing SRG, at IL5 | KESTREL's cloud segment runs at IL5 | The cloud spokes and hub |
| DoDI 5200.48 | KESTREL holds CUI | Marking, handling, and release |
| EO 12333 and DoDM 5240.01 | KESTREL collects intelligence | Collection and retention of any U.S. person information |
| The Privacy Act and DoDI 5400.11 | KESTREL holds personal information | User records and imagery of people |
| DoDI 5400.16 | KESTREL holds personal information | The Privacy Impact Assessment |
| DoDI 8530.01 | KESTREL is a DoD information system | Its relationship with the CSSP |
| DoDM 8140.03 | KESTREL has a cyber workforce | Qualifications for privileged and security roles |
| OMB M-21-31 | DoD adopted it for event logging | Logging and log retention |
| DFARS 252.204-7012 | The performer's contract flows it down | The performer's laptops that hold source code |
| CNSSP 15 and CNSA 2.0 | KESTREL is a national security system | Cryptography and every new acquisition |
| The DoD AI Cybersecurity Risk Management Tailoring Guide | The AO directs it | KESTREL's models and agents |

Three more obligations are tracked here but met outside the SADD: airworthiness certification, Section 508 accessibility, and foreign disclosure.

**The method.** Each obligation is broken down into discrete, testable requirements, never left at the level of a whole instrument or one of its chapters. Each requirement is then mapped to the outcome or control implementation that meets it. A crosswalk drawn only at the chapter level cannot be checked for truth, so the mapping always reaches the requirement itself.

**Gaps.** A requirement with no matching outcome is recorded in the requirement register as a gap, with a named owner and a path to closure. A gap with no owner goes to the POA&M.

**The watch.** The PMO ISSE watches for new and revised obligations and checks the inventory each quarter, together with the AI regulatory mapping in the AI/ML Governance Charter. The inventory and the gap analysis are re-run whenever an instrument is revised, a contract is modified, or KESTREL takes on a new mission or kind of data. A contract modification is the trigger most often missed, so the supply chain lead tells the PMO ISSE about each one.

---

## 2. Control Assessment Scheduling and Assessor Coordination

*Traces to CO-2.2.1 and CO-2.2.2. From Phase 2.*

**Placing controls in tiers.** Each control's assessment frequency depends on how quickly its implementation decays and what its failure would cost, not on spreading families evenly across the year. Every control is assessed at least once in a three-year cycle, with about a third of the families each year. Controls that change often, and the High-integrity key, signing, and datalink controls, are assessed each quarter or continuously. The Continuous Monitoring Plan holds the resulting tiers and the frequency it permits for each.

**Who assesses.**

| Assessor | Role | Independence |
|---|---|---|
| The SCA | Runs the independent assessments in each cycle | Independent. The SCA reports to the AO, outside the program's reporting line. |
| The ISSOs | Run self-assessments between the SCA's cycles | Not independent, since they report to the ISSM within the program. Their results inform, but never replace, the SCA's determination. |

Independence comes from the reporting line, not the employer. An assessor who reports to the owner of the system they assess is not independent, whatever their contract says.

**Accepting an external assessment.** An inherited control is accepted on its provider's assessment instead of being assessed directly, but only when all of these hold:

- The provider's authorization is current, and its most recent assessment falls within its own renewal period.
- The assessment covers the specific service KESTREL uses, in the regions or sites where it uses it. Azure Government's IL5 audit scope in both US Gov regions is an example.
- KESTREL's configuration of the service stays within what the provider's authorization assumes.
- No open finding in the provider's package affects the control KESTREL inherits.

The ISSM confirms these each quarter under the inherited control check, and the AO approves accepting each provider's results.

**Completion.** Each scheduled assessment is tracked from assignment to a delivered determination. A cycle that slips by more than 30 days is reported to the AO.

---

## 3. Annual Security Review Scope and Methodology

*Traces to CO-2.3.1 and CO-2.3.3. From Phase 3.*

**Scope.** The SCA's annual security review covers that year's third of the control families, every control in the quarterly tier, and a check that earlier fixes still hold. It spans the cloud, the data center, the alternate site, and the fleet.

**Methods.** For each control, the SCA chooses examination, interview, or testing as NIST SP 800-53A describes, and the Security Assessment Plan records the choice. Controls KESTREL implements directly are tested wherever a test is possible, rather than examined on documents alone.

**Specialized assessments.** These are chosen against KESTREL's actual threats, not included wholesale.

| Assessment | Included | Why |
|---|---|---|
| Vulnerability scanning | Yes, drawing on ACAS's continuous results | Every host is scanned anyway, so the review samples and verifies them |
| Penetration testing | Yes, the annual test by the independent provider | It tests what an outside attacker could reach |
| AI red teaming | Yes, for each new use case and foundation model change | KESTREL's models and agents face attacks a network test does not cover |
| Insider threat assessment | Yes, reviewing the behavior analytics and access reviews | Insiders hold source code and mission data |
| Adversary emulation | From Phase 4, when it is fielded | It tests whether detections fire |

**What the review does not cover.** Operational aircraft in flight are never tested, so the fleet is assessed only through the spare aircraft, the spare stations, and the simulator. Controls inside a provider's own infrastructure are covered by the provider's assessment, under Section 2. The review states these limits in its determination, so an untested surface is never read as covered.

**Findings.** Determinations go into the Security Assessment Report in eMASS. Findings go to the POA&M and the risk register, not to a separate record kept here.

---

## 4. Internal Audit Program

*Traces to CO-3.1.1, CO-3.1.2, and CO-3.1.4. From Phase 3.*

**The charter.** The parent organization's internal review office audits whether KESTREL's plans and procedures are carried out as written. It may examine any KESTREL process and record. It reports to the parent organization's head of internal review, outside the program manager's reporting line, so it is independent of what it audits. An ISSM auditing plans the ISSM wrote would be reviewing their own work, which is why the audit sits outside the program.

**What it audits.** The scope is named plan by plan.

- The governing plans: the AMP, CMP, VPMP, ASP, AISP, DMP, KMP, IRP, CP, SCRM plan, and Continuous Monitoring Plan
- The charters: governance, risk, AI/ML governance, and privacy
- The records those plans should produce, such as change records, access reviews, backup restore tests, exception approvals, and AI review board decisions

**What counts as a finding.** A finding is any place where practice diverges from the documented procedure. Each audit compares the procedure with three things. These are the records it should have produced, the state it should have left the system in, and the account of the people who actually perform it. The office interviews the performers, not only the process owners, since the gap usually lies between what an owner believes happens and what the performer actually does.

**The schedule.** Every governing plan is audited at least once every two years. The order follows the risk charter's remediation ranking and the Continuous Monitoring Plan's cadence, so plans that protect the High-integrity rows come first.

**Findings.** Each finding is tracked in Jira until its fix is verified.

**Review of the charter.** The audit charter is reviewed each year and whenever the office's mandate or the program's structure changes. The independence of the reporting line is checked first at each review, since growth tends to erode it without anyone deciding to.

---

## 5. External Audit Coordination

*Traces to CO-3.2.1 and CO-3.2.2. From Phase 3.*

**Who may audit KESTREL.** External audits and inspections include inspectors general, GAO, and JFHQ-DODIN's Command Cyber Operational Readiness Inspections. DCMA and DIBCAC review the performer's laptops under CMMC, which KESTREL relies on.

**Intake.** Every request goes to the program manager, never to a shared inbox. The program manager opens a Jira record of the requesting body, the authority it audits under, the scope and period requested, and the response deadline. If a request reaches beyond what the body's authority entitles it to, program counsel negotiates the scope before anything is provided.

**One coordinating point.** The ISSM assembles each response from the program evidence repository. Evidence is drawn from the repository rather than requested again from the people who produced it.

**Releasability review.** This step is never skipped, even under deadline pressure. Before anything leaves KESTREL, the ISSM reviews each artifact for CUI marking and releasability, with program counsel. The foreign disclosure officer joins if any recipient is foreign. The review also considers the package as a whole, since a collection of documents can be more sensitive than any one of them.

**The record.** The ISSM records what was provided, to whom, and when. Findings go to the POA&M and are tracked until they close on KESTREL's record and the auditor's.

---

## Appendix: Reference Data and Live Registers

Each item below is living data, kept where the people who use it work.

**Requirement-to-Control Mapping and Gap Analysis Register** *(CO-1.1.2, from Phase 2)*: The crosswalk of every requirement to the outcome that meets it, and every gap with its owner, in Confluence. The AI/ML Governance Charter's regulatory rows join it rather than forming a second register.

**Control Assessment Calendar** *(CO-2.2.1, from Phase 2)*: The dated calendar for each cycle, in Jira, laid out from the Continuous Monitoring Plan's tiers.

**Assessment Completion Tracking** *(CO-2.2.3, from Phase 2)*: Each cycle's progress in Jira, shown on the compliance dashboard in Splunk from Phase 3.

**Annual Security Review Determination Record** *(CO-2.3.2, from Phase 3)*: The SCA's determination for every control in scope, in the SAR in eMASS.

**Audit Schedule** *(CO-3.1.2, from Phase 3)*: The internal review office's dated schedule, in Jira.

**Audit Findings Tracking** *(CO-3.1.3, from Phase 3)*: Each internal audit finding in Jira, through to its verified fix.

**External Audit Intake Record** *(CO-3.2.1, from Phase 3)*: Each request's Jira record, with its body, authority, scope, period, and deadline.

**External Audit Response Package** *(CO-3.2.2, from Phase 3)*: The evidence provided for each engagement, with its releasability review, recorded in the evidence repository.

**External Audit Findings Tracking** *(CO-3.2.3, from Phase 3)*: Each external finding in the POA&M, closed on both KESTREL's record and the auditor's.

---

## Approval

Each section is approved by its own authority.

| Section | Approved By |
|---|---|
| 1. Regulatory and Framework Requirement Mapping | The ISSM |
| 2. Control Assessment Scheduling and Assessor Coordination | The AO, who accepts each provider's assessment in place of KESTREL's own |
| 3. Annual Security Review Scope and Methodology | The AO |
| 4. Internal Audit Program | The parent organization's head of internal review |
| 5. External Audit Coordination | The ISSM, with program counsel for releasability |

**Status:** Pending. Each section is reviewed by its authority before it takes effect.

**Circulated To:** the SCA, the ISSOs, the internal review office, the supply chain lead, program counsel, the foreign disclosure officer, and the team leads whose processes are audited.

---

## Periodic Review and Revision

Each section revises on its own triggers:

- **Requirement mapping:** each year, and whenever an instrument is revised, a contract is modified, or KESTREL takes on a new mission or kind of data
- **Assessment scheduling:** each year, within the frequencies the Continuous Monitoring Plan allows
- **Annual security review:** each year, as the cycle recurs
- **Internal audit:** the charter each year, and whenever the office's mandate or the program's structure changes
- **External audit coordination:** as intake and coordination practice matures with experience
- **Any section:** a product substitution recorded in the Security Implementation Plan, for any product the section names
