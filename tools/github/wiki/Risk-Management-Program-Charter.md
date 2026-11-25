> **Notional system.** KESTREL is fictional. This page stands in for a governing document in KESTREL's self-hosted Confluence. Its names, thresholds, and decisions are invented to show a completed Risk Management Program Charter.

# KESTREL Risk Management Program Charter

This charter sets out how KESTREL scores, accepts, and ranks risk, and how it watches the threats that create it. It is the machinery KESTREL uses to run the RMF well, not a restatement of the RMF. It carries out the design decisions in the [Risk section of the SADD](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/12-risk.md). The [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/12-risk.md) is the record of each product selection.

The risk register, the Security Assessment Plan, the SAR, the RAR, and the POA&M stay separate documents under their own names. This charter sets the method and criteria they are built and scored against.

**NIST Control Mapping:** None for the charter as a whole. It bundles the Risk focus area's methods for the people who apply them, and each section carries its own mapping.

> **When each section takes effect.** Sections 1, 2, and 6 take effect in Phase 1, since the first findings, acceptances, and backup tiers need them. Sections 3, 4, and 5 take effect in Phase 2. That is when the Security Team names its threat intelligence analyst and the ranking model is built.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| Charter Version | 0.1 |
| Date | 2026-11-25 |
| Prepared By | PMO ISSE, with the ISSM, the program manager, the intelligence mission leads, and Fleet Operations' operations lead |
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

This charter is the single reference for everyone who scores, accepts, or ranks risk on KESTREL. It covers the whole authorization boundary, including the UAS fleet, the ground segment, and KESTREL's AI models and agents. It binds the Security Team, the team leads, the PMO ISSE, the program manager, and the AO. Each section revises on its own trigger, as Periodic Review and Revision lists.

---

## 1. Risk Assessment Methodology

*Traces to RK-1.1.1, RK-1.1.2, and RK-1.1.3.*

**NIST Control Mapping:** PM-9 (partial).

**The model.** KESTREL uses one semi-quantitative method based on NIST SP 800-30. Likelihood and impact are each scored from 1 to 5, and their product gives the rating. Every team scores this way. Nobody keeps a private scale.

**Likelihood.**

| Score | Meaning | Evidence the scorer must hold |
|---|---|---|
| 5 | Exploited now, or certain within a year | Known exploitation in the wild, or a working exploit against KESTREL |
| 4 | Likely within a year | A public exploit, and a reachable path to the weakness |
| 3 | Possible | A reachable path, but no public exploit |
| 2 | Unlikely | Reaching it needs an insider or a prior compromise |
| 1 | Rare | Needs several unlikely conditions at once |

**Impact.** Impact is anchored to the CCSD's categorization, to mission effects, and to privacy harm to individuals.

| Score | Meaning |
|---|---|
| 5 | Could cost an aircraft, compromise the command link, expose CCSD row 13's keys, or tamper with a certified model or signed release |
| 4 | Stops a mission process, exposes partner data, or causes serious privacy harm |
| 3 | Degrades a mission process, or exposes CUI inside the boundary |
| 2 | Disrupts development or analysis with no mission effect |
| 1 | No meaningful effect |

**Rating.**

| Likelihood × impact | Rating |
|---|---|
| 1 to 3 | Very Low |
| 4 to 6 | Low |
| 8 to 12 | Moderate |
| 15 to 16 | High |
| 20 to 25 | Very High |

A likely row 13 key exposure scores 4 × 5 = 20, so the top band is reachable.

**Worked examples.** KESTREL has no assessed findings yet. These examples come from its threat model and are replaced with real findings after the first assessment.

| Example | First score | Final score | Why |
|---|---|---|---|
| A foundation model deployment's public endpoint is re-enabled by a misconfiguration | 3 × 3 = 9, Moderate | 4 × 3 = 12, Moderate | Configuration checks find it within a day, but scanners find public endpoints faster |
| Prompt injection through a retrieved report steers the mission-planning agent | 3 × 2 = 6, Low | 3 × 5 = 15, High | Scored wrong at first. The scorer rated the analyst assistant's output, not the agent's tool use. The agent proposes flight plan changes, and a steered proposal an operator approves could reach an aircraft. That is a score of 5. |
| A lost aircraft's datalink keys are not superseded | 2 × 5 = 10, Moderate | 2 × 5 = 10, Moderate | Impact is top band, but the fleet-wide supersession rule makes it unlikely |

The second example is the one the training dwells on. Score the worst thing the component can do, not the thing it usually does.

**Training.** The Security Team, the ISSOs, and every team lead train on these examples before they score risk. The PMO ISSE runs the training.

**Recalibration.** The PMO ISSE reviews the method each year. An earlier review follows if ratings cluster at one end, or if the AO or the steering committee overturns a score. A shift in the mission, categorization, or threat picture also triggers one. After any change to a scale, the ISSM re-scores every open risk, so two vintages of rating never coexist.

---

## 2. Risk Appetite, Tolerance, and Acceptance-Authority Tiering

*Traces to RK-1.2.1, RK-1.2.2, and RK-1.2.3.*

**NIST Control Mapping:** PM-28 (partial) and PM-9 (partial).

**The statement.** The program manager drafts KESTREL's risk appetite statement, and the AO approves it. KESTREL's appetite is lowest where a failure could reach an aircraft or a key. It is moderate for analytic availability and for development.

| Tier | What it covers | Carried without further action | Treated, or accepted under the appendix's table | Never carried |
|---|---|---|---|---|
| Flight safety and keys | CCSD rows 6, 8, 10, and 13: command and control, certified models, signed releases, and key material | Very Low | Low and above | High and Very High |
| Mission data | Every other CCSD row rated Moderate | Very Low and Low | Moderate and above | Very High |
| Analytic availability and development | Dev/test spokes, training scratch, experimentation, and analytic availability | Very Low and Low | Moderate and above | Very High |

"Never carried" means no authority accepts it. The affected function stops, or the risk is treated until it drops below that band.

**Why authority attaches to roles.** The AO accepts every risk. A standing AO delegation lets the PMO ISSE accept the lowest bands. The interim authorization to test records it, and the ATO decision carries it forward. The delegation names a role, not a person, so it survives a change of holder without reissue. The accepting authority is never the team whose delivery the risk blocks. The appendix holds the band-to-authority table.

**When the authority is unavailable.** A request the PMO ISSE cannot reach waits for the AO. A request the AO cannot reach waits too. Nobody else accepts risk on their behalf. The finding stays open, with its compensating measures in place, until the authority decides.

**Review.** The statement is reviewed each year with the steering committee. It is reviewed sooner after a mission, categorization, or threat change. It is also reviewed when a band is routinely exceeded and accepted anyway, since the tolerance has then already shifted.

---

## 3. Threat Intelligence Program Charter

*Traces to RK-2.1.1, RK-2.1.2, and RK-2.1.3.*

**NIST Control Mapping:** PM-16 (partial).

**Takes effect in Phase 2.**

**Intelligence requirements.**

1. Which adversaries target ISR and unmanned systems, and how?
2. How are datalinks, GNSS, and navigation being attacked?
3. How are AI supply chains and models being attacked, including foundation models and agents?
4. What is being exploited in the products KESTREL runs?

**Sources.**

| Source | Answers | How it reaches KESTREL |
|---|---|---|
| The CSSP | 1, 2, 4 | Advisories and indicators as STIX over TAXII on F31 |
| DoD intelligence products | 1, 2, 3 | Sanitized releases through a cleared government point of contact and the CSSP |
| CISA's Known Exploited Vulnerabilities catalog | 4 | Imported daily into Splunk |
| MITRE ATT&CK, ATT&CK for ICS, and ATLAS | 1, 2, 3 | The technique taxonomy in Section 4 |
| Vendor advisories, such as Microsoft's and Palo Alto Networks' | 4 | Each vendor's security notification service |

Much of what answers requirements 1 to 3 is classified. Only releasable content enters KESTREL, through the cleared point of contact. A source that produces nothing used for two quarters in a row is dropped at the yearly review.

**The analyst function.** One threat intelligence analyst in the Security Team holds the function, named in Phase 2. The role needs a Secret clearance to work with the cleared point of contact, and fluency in ATT&CK and ATLAS. The analyst produces the threat assessments and vets every indicator before detection uses it. KESTREL staffs the role itself. The CSSP's analysts cover leave and surges under its service agreement. One analyst is what KESTREL funds, so the function is chartered for one, not for a team.

**Maturity.** The Security Team assesses the function each year against the Cyber Threat Intelligence Capability Maturity Model (CTI-CMM). The assessment covers requirements coverage, source usefulness, the analyst's throughput, and whether any product changed a decision. Each shortfall becomes a Jira item.

---

## 4. Threat Landscape Monitoring and Reporting

*Traces to RK-2.2.1, RK-2.2.2, and RK-2.2.3.*

**NIST Control Mapping:** RA-3(3) (full) and PM-15 (partial).

**Takes effect in Phase 2.**

**What gets tracked.** An actor or campaign is tracked when it targets ISR or unmanned systems, DoD cloud tenants, or AI models. It is also tracked when it exploits a product KESTREL runs. The register stays at ten entries or fewer, so the analyst can say what each means for KESTREL. Each entry records what the actor targets, how it gains and keeps access, and what KESTREL would see if it were present. Attribution is not the point. Tradecraft and targeting are what the register is for.

**New techniques.** The analyst maps each new technique against the detections built in Splunk Enterprise Security. Techniques are named in MITRE ATT&CK, ATT&CK for ICS, and ATLAS, so new activity compares against prior coverage. A technique that would succeed against KESTREL today becomes a finding in the risk register, scored under Section 1. Datalink jamming and spoofing, and ATLAS techniques against models, are watched first.

**The threat brief.** The analyst sends a threat brief to the steering committee and the risk register each month. Each brief covers:

- What changed since the last brief
- Which KESTREL controls or detections the change bears on
- What the analyst recommends, and who must decide

A change that cannot wait goes to the ISSM at once.

---

## 5. Enterprise Remediation Ranking Model

*Traces to RK-3.1.1, RK-3.1.2, and RK-3.1.3.*

**NIST Control Mapping:** PM-4 (partial).

**Takes effect in Phase 2.**

**The ranking.** One ranking in Jira orders remediation across every team. It sorts in this order:

1. Fixed deadlines from IAVM directives and CYBERCOM orders, earliest first
2. Known exploited flaws on DMZ, Tier 0, or fleet assets
3. Everything else, by priority score

**Priority score.** The score is the Section 1 risk score, times a criticality weight, divided by an effort factor.

| Input | Values |
|---|---|
| Risk score | 1 to 25, from Section 1 |
| Criticality weight | 3 for a Tier 1 asset, 2 for Tier 2, 1 for Tier 3, from the business impact analysis |
| Known exploitation | Adds 10 when the flaw is in CISA's catalog or the CSSP reports it exploited |
| Exposure | Adds 5 when the asset faces the DMZ or the circuits |
| Effort factor | 1 for under a day, 1.5 for under a week, 2 for longer |

A tie goes to the older finding. Effort is in the score because a ranking that ignores it gets worked from the bottom anyway. Fleet work happens only in OT maintenance windows. A fleet item ranked first waits for the next window, while the rest of the ranking is worked in order.

**The weekly forum.** The team leads and the ISSM meet each week to work the ranked backlog and assign capacity in the model's order. Any deviation is recorded in Jira, with its reason and who approved it. An unrecorded deviation means the model has been replaced without anyone saying so.

**Recalibration.** The PMO ISSE recalibrates the weights each quarter against the deviation log and what was actually exploited. Recalibration comes sooner if the deviations keep pointing the same way. After any change, the whole backlog is re-ranked, not just new findings.

---

## 6. Business Impact Analysis Methodology and Criticality Tiering

*Traces to RK-3.2.1 and RK-3.2.3.*

**NIST Control Mapping:** PM-11 (partial).

**Who does it.** The program manager owns the business impact analysis. The intelligence mission leads and Fleet Operations' operations lead set how long each process can be lost.

**Processes.** The analysis covers every mission process. Today those are:

- Flying and controlling the aircraft
- Collecting and ingesting data
- Detecting and analyzing
- Releasing to partners
- Retraining models

Each process is mapped to its CCSD rows. It is traced to what it depends on, such as identity, the PKI, the hubs and circuits, and the security monitoring platform.

**Consequences and horizons.** Each process is scored on what is lost after 1 hour, 4 hours, 24 hours, and 7 days of outage. It is scored against four consequences:

- Flight safety
- Mission effect, such as lost collection or a late product
- Partner trust
- Exposure of data or harm to individuals

Mission consequence drives the score, not cost alone.

**Tiers.** A process lands in the tier of its shortest intolerable outage. These are the same tiers the Contingency Plan's backups and the IRP's criticality use, so KESTREL has one scale, not three.

| Tier | Intolerable outage | Recovery objectives |
|---|---|---|
| Tier 1 | Within 4 hours | 4-hour recovery time, 15-minute recovery point |
| Tier 2 | Within 24 hours | 24 hours for both |
| Tier 3 | Tolerable for a week | 7-day recovery time, 24-hour recovery point |

The method exists in Phase 1, so Tier 1 backups start on provisional objectives. The full analysis in Phase 2 confirms them.

**Review.** The analysis is rerun each year, and for a process that takes on or retires a function. A significant change triggers a rerun too, such as a new partner nation or payload. Results are recorded as tags in Jira Service Management Assets, which set the recovery tiers and incident severity.

---

## Appendix: Reference Data and Live Registers

**Tolerance-to-Acceptance-Authority Tier Table** *(RK-1.2.2)*:

| Residual risk | In CCSD rows 6, 8, 10, and 13 | Elsewhere |
|---|---|---|
| Very Low | The PMO ISSE, under the AO's delegation | The PMO ISSE, under the AO's delegation |
| Low | The AO | The PMO ISSE, under the AO's delegation |
| Moderate | The AO | The AO |
| High | Never carried | The AO, for up to one year |
| Very High | Never carried | Never carried |

If the entitled role is unavailable, the request waits, as Section 2 sets out.

**Threat Actor/Campaign Tracking Register** *(RK-2.2.1)*: Up to ten tracked actors and campaigns, held in Confluence from Phase 2.

**Threat Landscape Assessment Reports** *(RK-2.2.3)*: Each monthly threat brief, held in Confluence and linked from the risk register.

**Business impact analysis results** *(RK-3.2.2)*: Held as tags in Jira Service Management Assets, not in this charter. The Contingency Plan's recovery objectives and the IRP's criticality read from them.

---

## Approval

| Section | Approved by | Status |
|---|---|---|
| 1. Risk Assessment Methodology | The PMO ISSE | Pending |
| 2. Risk Appetite, Tolerance, and Acceptance-Authority Tiering | The AO | Pending |
| 3. Threat Intelligence Program Charter | The ISSM | Pending |
| 4. Threat Landscape Monitoring and Reporting | The ISSM, reported to the steering committee | Pending |
| 5. Enterprise Remediation Ranking Model | The PMO ISSE, with the weekly forum | Pending |
| 6. Business Impact Analysis Methodology and Criticality Tiering | The program manager | Pending |

**Circulated To:** every team lead, the Security Team, the steering committee, the intelligence mission leads, Fleet Operations, and IT Operations.

---

## Periodic Review and Revision

Each section revises on its own trigger:

- **Risk assessment method:** each year, and when ratings cluster, a score is overturned, or the mission, categorization, or threat picture shifts
- **Risk appetite:** each year with the steering committee, and when the acceptance record shows a band routinely exceeded
- **Threat intelligence function:** each year's maturity assessment, and when a source or the analyst changes
- **Threat landscape:** each monthly brief, and the register as actors change
- **Ranking model:** each quarter, and when the risk scales or tolerance bands change
- **Business impact analysis:** each year, and when a process takes on or retires a function
- **Any section:** a product substitution recorded in the Security Implementation Plan, for any product the section names
