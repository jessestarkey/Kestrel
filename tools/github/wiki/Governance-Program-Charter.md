> **Notional system.** KESTREL is fictional. This page stands in for a governing document in KESTREL's self-hosted Confluence. Its names, thresholds, and decisions are invented to show a completed Governance Program Charter.

# KESTREL Governance Program Charter

This charter sets out how KESTREL is governed. It covers KESTREL's policies, its security roles, and the two bodies that decide. It also covers exceptions, the zero trust roadmap, and the rules every user signs. It carries out the design decisions in the [Governance section of the SADD](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/11-governance.md). The [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/11-governance.md) is the record of each product selection.

**NIST Control Mapping:** None for the charter as a whole. It bundles several Governance outcomes for the leaders who read them, and each section carries its own mapping.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| Charter Version | 0.1 |
| Date | 2026-11-25 |
| Prepared By | PMO ISSE, with the ISSM, the program manager, and the chief engineer |
| Approved By | Each section's own authority, as listed under Approval |
| Source SADD Version | 0.5 |
| Source SIP Version | 0.3 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-25 | PMO ISSE | Initial draft |

---

## Purpose and Scope

This charter is the single reference for KESTREL's governance leadership. It binds everything inside KESTREL's authorization boundary. That includes every KESTREL location, the fleet, and the performer laptops that hold source code. It binds every person with a KESTREL account, whether government, performer, partner, vendor, or CSSP. Each section revises on its own trigger, as Periodic Review and Revision lists.

---

## 1. Purpose, Scope, and Policy Framework

*Traces to GV-1.1.1, GV-1.1.2, GV-1.1.3, GV-2.1.1, GV-2.1.2, and GV-2.1.3.*

**NIST Control Mapping:** PM-1 (partial).

**Tiers.** KESTREL's documents sit in three tiers beneath DoD issuances and the parent organization's enterprise policy. Each lower tier cites the tier above it by name and version.

| Tier | What it holds | Approved by |
|---|---|---|
| Policy | KESTREL's one system security policy | The program manager signs it |
| Standards | The governing plans: the AMP, CMP, VPMP, ASP, AISP, DMP, KMP, IRP, CP, SCRM plan, and ConMon plan, plus the privacy policy and the responsible AI policy | The Configuration Control Board, except the ConMon plan, which the AO approves |
| Procedures | The runbooks beneath each standard, such as the break-glass retrieval runbook | The ISSM |

**What each standard covers.** Each statement in the system security policy maps to the control families it satisfies. A change to the tailored control set can then be traced to the documents it touches.

| Standard | Main control families |
|---|---|
| Account Management Plan (AMP) | AC, IA |
| Configuration Management Plan (CMP) | CM, and parts of SC and SI |
| Vulnerability and Patch Management Plan (VPMP) | RA, SI |
| Application Security Plan (ASP) | SA, SI |
| AI/ML Security Plan (AISP) | SA, SI, RA |
| Data Management Plan (DMP) | MP, and parts of SC |
| Key Management Plan (KMP) | SC |
| Incident Response Plan (IRP) | IR |
| Contingency Plan (CP) | CP |
| Supply Chain Risk Management Plan (SCRM) | SR |
| Continuous Monitoring Plan (ConMon) | CA |
| Privacy policy | PT |
| Responsible AI policy | No 800-53 family. It sets the AI/ML Governance Review Board's criteria. |

**Scope statements.** Each document names the locations, environments, and people it binds. The system security policy binds everything this charter binds. A standard may narrow its own scope but never widen it.

**Drafting.** The document's owner drafts it from its SABER template in Confluence. The owner is named in the SADD, such as the ISSM for the IRP or the Platform Team for the CMP. The owner coordinates with every team the document names, and the ISSM reviews it before it goes for approval.

**Review.** Every document is reviewed each year. It is reviewed earlier when an incident, an assessment, or a significant change calls for it. A boundary change, a re-categorization, or the AO's retailoring of the control set also triggers a review. It covers the system security policy and every standard the change touches.

**Retirement.** A new version names the version it supersedes. The old version is withdrawn from Confluence's working space and archived read-only for 6 years. Policies a machine can enforce are also written as code in GitLab, such as the admission and OPA policies. The code cites the document it enforces.

---

## 2. Governance Roles, Responsibilities, and Appointments

*Traces to GV-1.2.1, GV-1.2.2, GV-1.2.3, GV-1.3.1, GV-1.3.2, and GV-1.3.3.*

**NIST Control Mapping:** PM-1 (partial) and PM-2 (partial).

| Role | Held by | Accountable for | Decides | Qualification |
|---|---|---|---|---|
| Authorizing Official (AO) | The government AO | Accepting KESTREL's residual risk | The authorization, and every risk or exception above the PMO ISSE's delegation | Appointed by the component |
| System owner | The program manager | KESTREL as a whole, under the AO | The system security policy, funding, and shutdown of a mission service | Government program manager |
| Information owners | Those CCSD Section 2 names, with the intelligence mission leads owning the mission data | The data their CCSD rows cover | Who may receive their data | Government |
| PMO ISSE | The program office's ISSE | The CCSD, the SADD, the SIP, and Certification to Field | Release approvals, and Very Low and delegated Low risks and exceptions | DoDM 8140.03 qualified for the ISSE work role |
| ISSM | The performer's ISSM, appointed by the program manager | The authorization package, the POA&M, ConMon, and incident response | Declaring incidents, and approving procedures and runbooks | DoDM 8140.03 qualified for the ISSM work role |
| ISSOs | Performer staff, appointed by the ISSM | Day-to-day compliance and investigation | Nothing beyond what the ISSM delegates | DoDM 8140.03 qualified for the ISSO work role |
| Security Control Assessor (SCA) | An independent assessor | Assessing KESTREL's controls for the AO | Assessment findings | Independent of the program |
| PSO | The parent organization's security office | Personnel and physical security, and spill reporting | Investigations, and releases of held spill copies with the AO | Appointed by the parent organization |
| Foreign disclosure officer | Program office staff | Releases to partner nations | Each release | Appointed under the program's disclosure authority |
| Privacy officer | Program office staff | Privacy compliance and breach reporting | Privacy assessments | Appointed by the program manager |
| Supply chain lead | Program office staff | Supply chain risk | Supplier assessments | Named in the SCRM plan |
| Team leads | Each performer team's lead | Their team's systems and backlog | Changes inside their own team's scope | Named by the performer |
| CSSP | The cyber defense service provider | Monitoring and first triage | Running pre-approved containment playbooks | Under its service agreement |

**Responsibility matrix.** The SSP holds KESTREL's responsibility matrix. It shows, for each governance activity, who performs it, who approves it, who is consulted, and who is informed. It records that the Security Team and the CSSP hold no administrative roles beyond the exceptions in Privileged Access Control (`ID-4.1`). The ISSM reviews it each year, and on any change of role holder, organization, contract, or boundary.

**Appointment letters.** The program manager appoints the ISSM, and the ISSM appoints each ISSO, by signed letter. Each letter states:

- The person and the role
- The KESTREL boundary it covers
- The authority it confers and the responsibilities the person accepts
- Its effective date
- The appointing official's and the appointee's signatures

The ISSM tracks every letter in Jira. A letter is reissued within 10 business days when its holder's position, the boundary, or the authority changes. A departing holder's letter is terminated on their last day, and the register is updated the same day.

**Appointment register.** The register lists each current holder of an appointed role, with the letter's date.

| Role | Holder | Letter dated |
|---|---|---|
| ISSM | To be appointed | Pending, before Phase 1 begins |
| ISSOs | To be appointed | Pending, after the ISSM's appointment |

---

## 3. Security Governance and Steering Committee

*Traces to GV-1.4.1 and GV-1.4.2.*

**NIST Control Mapping:** PM-29 (partial) and PM-6 (partial).

**Purpose.** The steering committee settles what one team or the Configuration Control Board cannot. That includes cross-team disputes, risk questions above the board, and schedule conflicts with security work.

**Members.** The program manager chairs it. Its members are the chief engineer, the PMO ISSE, the ISSM, each team lead, and the intelligence mission leads. A quorum is the chair or the chief engineer as alternate, plus the PMO ISSE, the ISSM, and half the team leads.

**Cadence.** It meets monthly. The chair may call an out-of-cycle meeting within two business days for a decision that cannot wait.

**What it decides.**

| It decides | It recommends to the AO | It may not decide |
|---|---|---|
| Cross-team disputes over security work | Accepting any risk or exception above the PMO ISSE's delegation | Accepting risk, which belongs to the AO and the PMO ISSE under Risk Acceptance Process (`RK-1.4`) |
| Schedule conflicts, including a slip of up to 30 days on a security deliverable | A slip of more than 30 days on a deliverable the authorization depends on | Changing the CCSD's categorization or tailoring |
| Escalations from the Configuration Control Board | Any change to the authorization boundary | Overriding a Certification to Field decision |

**Relationships.** The committee advises the AO through the ISSM and the PMO ISSE. The Configuration Control Board escalates to it. The AI/ML Governance Review Board reports its decisions to it each quarter.

**Records.** Decisions and actions are tracked in Jira Service Management. A Splunk dashboard shows the security posture to the committee each month.

---

## 4. Configuration Control Board

*Traces to GV-1.5.1 and GV-1.5.2.*

**NIST Control Mapping:** CM-3 (partial).

**Purpose.** The board approves the changes and documents that most shape KESTREL's security.

**Members.** The chief engineer chairs it. Its standing members are the PMO ISSE, the ISSM, the Platform Team lead, and Fleet Operations' operations lead. The lead of any team with a change on the agenda joins them. A quorum is the chair or the PMO ISSE as alternate, plus the ISSM or an ISSO, and the Platform Team lead. A change that touches the fleet also needs the operations lead.

**Cadence.** It meets weekly. An emergency change may run before the board meets under the CMP's emergency path. The board reviews it within two business days, under Asset Lifecycle Change Control (`DI-2.2`).

**What it approves.**

- Changes to the shared rule base on the hubs, the alternate site firewall, and the SDN controller
- Changes to the identity provider
- New or changed interconnections
- Changes to a system prompt's roles and limits
- Every governing plan the AO does not approve

**Escalation.** A change Security Impact Analysis (`GV-5.11`) finds significant goes to the SCA and the AO before it is built. A dispute the board cannot settle, or a change needing a risk acceptance above Low, goes to the steering committee.

**Processes that route through it.** Asset Lifecycle Change Control (`DI-2.2`) sends its high-impact and contested changes here. So does the rule base change process under Network Centralization and Standardization (`NE-1.1`). Changes to system prompts and agent tool lists come through the AISP's change process.

---

## 5. Policy Exception Authority

*Traces to GV-2.2.1.*

**NIST Control Mapping:** None. The SABER leaves this outcome unmapped, since the exception path serves every policy rather than one control.

**Requesting an exception.** A team requests an exception through Jira Service Management. The request names the requirement it departs from, the reason, the scope, the compensating measures, and an end date. A request without an end date is refused, since it would change policy through the wrong channel.

**Approval.** The ISSM scores the risk the exception creates, and approval follows Risk Acceptance Process (`RK-1.4`).

| Risk | Approved by |
|---|---|
| Very Low | The PMO ISSE, under the AO's delegation |
| Low, outside CCSD rows 6, 8, 10, and 13 | The PMO ISSE, under the AO's delegation |
| Low in those rows, or anything higher | The AO |

The approver is never the team whose delivery the requirement blocks. No exception runs longer than one year.

**At expiry.** An exception is remediated, re-justified, or escalated before its end date. One that expires becomes an open finding.

---

## 6. Zero Trust Maturity and Roadmap

*Traces to GV-1.6.1, GV-1.6.2, and GV-1.6.3.*

**NIST Control Mapping:** None. The SABER leaves this outcome unmapped, since its basis is the DoW zero trust strategy rather than 800-53.

**Assessment.** Each year the PMO ISSE rates KESTREL against each pillar of the DoW zero trust reference architecture. The rating covers the cloud, the data center, the alternate site, and the ground segment. Every rating cites the implemented outcome that earns it, never an opinion. The first assessment runs in Phase 2, once enough of Protect is built to rate.

**Target.** KESTREL's target is the department's target level, on the department's timeline.

**Roadmap.** Each gap between a rating and the target becomes a Security Implementation Plan record. Each record has an owner, dependencies, and a target date. Progress goes to the steering committee each quarter. The roadmap is updated when a record closes, when the assessment reruns, or when the department revises its target.

| Pillar | Current rating | Target |
|---|---|---|
| User | First assessment in Phase 2 | Target level |
| Device | First assessment in Phase 2 | Target level |
| Application and workload | First assessment in Phase 2 | Target level |
| Data | First assessment in Phase 2 | Target level |
| Network and environment | First assessment in Phase 2 | Target level |
| Automation and orchestration | First assessment in Phase 2 | Target level |
| Visibility and analytics | First assessment in Phase 2 | Target level |

---

## 7. Rules of Behavior and Acceptable Use

*Traces to GV-2.4.1 and GV-2.4.3.*

**NIST Control Mapping:** PL-4 (full) and PL-4(1) (full).

**The rules.** Every KESTREL user agrees to these rules:

- Use KESTREL only for the work your role requires.
- Handle CUI under its markings, and never move it outside KESTREL except through an approved path.
- Never paste classified content into KESTREL, including into a language model prompt.
- Report a suspected incident or spill to the on-call security analyst at once.
- Never share your CAC, PIN, or session, and never leave a session unlocked and unattended.
- Never reuse a KESTREL identifier or authenticator on another system or site.
- Post nothing about KESTREL's missions, people, or design on social media or a public site.
- Never install software, connect a device, or change a setting outside the approved path.
- Never use an AI agent to do what you could not do yourself.

**Where they are published.** The rules are published in Confluence. Each user signs them through a Jira Service Management form.

**Acknowledgment and lapse.** Every user signs before their account is created and again each year. When the rules change, every user signs again within 30 days. An account whose acknowledgment lapses is disabled in Active Directory through Ansible until the user signs.

**Violations.** The ISSM records each violation and may suspend the account at once. The ISSM refers every violation to the PSO. The PSO decides whether to hand it to the insider threat program, the person's government supervisor or performer management, or law enforcement.

---

## Appendix: Reference Data and Live Registers

**Governance Decision/Action Item Log** *(GV-1.4.3)*: Every steering committee decision and action item, with its owner, due date, and status, held in Jira Service Management. It is carried forward to each meeting until closed.

**Security Program Metrics/Posture Dashboard** *(GV-1.4.4)*: The leadership dashboard in Splunk. It draws on the risk register, the POA&M, compliance status, the AI inventory, and the detection and response metrics.

**Board Decision and Escalation Log** *(GV-1.5.3)*: Every change the Configuration Control Board approved, rejected, or escalated, held in Jira with its rationale and source process. It runs from Phase 1, since the board approves the first rule base and plans.

**Policy Exception Register and Trend Report** *(GV-2.2.2 and GV-2.2.3)*: Every granted exception with its scope, compensating measures, and end date, held in Jira Service Management. The ISSM reports exception trends to the steering committee each quarter.

**User Acknowledgment Record** *(GV-2.4.2)*: Each user's signed acknowledgment of the rules of behavior and the version they signed, held in Jira Service Management.

---

## Approval

| Section | Approved by | Status |
|---|---|---|
| 1. Policy Framework | The program manager | Pending |
| 2. Roles, Responsibilities, and Appointments | The program manager, with the ISSM for the register | Pending |
| 3. Steering Committee | The program manager, with the AO's concurrence | Pending |
| 4. Configuration Control Board | The steering committee | Pending |
| 5. Policy Exception Authority | The AO, who sets the delegation | Pending |
| 6. Zero Trust Maturity and Roadmap | The PMO ISSE, reported to the steering committee | Pending |
| 7. Rules of Behavior and Acceptable Use | The AO | Pending |

**Circulated To:** the steering committee, the Configuration Control Board, the AI/ML Governance Review Board, the ISSOs, and every team lead.

---

## Periodic Review and Revision

Each section revises on its own trigger:

- **Policy framework:** each document's yearly review, and a boundary change, a re-categorization, the AO's retailoring, or a serious incident
- **Roles and appointments:** each year, and on any change of role holder, organization, contract, or boundary
- **Steering committee and board:** when membership, scope, or a decision threshold changes
- **Exception authority:** when the AO changes the delegation or the risk tolerance bands
- **Zero trust roadmap:** each yearly assessment, and when the department revises its target
- **Rules of behavior:** whenever the rules change
