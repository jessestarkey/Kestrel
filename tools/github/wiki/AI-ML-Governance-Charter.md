> **Notional system.** KESTREL is fictional. This page stands in for a governing document in KESTREL's self-hosted Confluence. Its names, thresholds, and decisions are invented to show a completed AI/ML Governance Charter.

# KESTREL AI/ML Governance Charter

This charter sets out how KESTREL decides which AI it builds and runs, and on what terms. It covers the use case inventory, the program-level AI threat assessment, the responsible AI policy, and the AI/ML Governance Review Board. It also covers the regulatory mapping, the risk tiering of AI suppliers, and a quarterly posture report. It carries out the design decisions in the [Governance](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/11-governance.md) and [Artificial Intelligence](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/06-artificial-intelligence.md) sections of the SADD. The [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/11-governance.md) is the record of each product selection.

This charter governs use cases. The AI/ML Security Plan (AISP) governs how models are built, tested, and served. Each model's threat model and model card stay with the model.

**NIST Control Mapping:** None for the charter as a whole. It bundles the AI/ML governance outcomes for the board and the teams that bring it use cases. Each section carries its own mapping.

> **When each section takes effect.** Sections 1 and 4 take effect in late Phase 1, so the board can approve the first use cases before training. Until the responsible AI policy in Section 3 is issued, the board judges use cases against the AISP. Sections 2, 3, 5, 6, and 7 take effect in Phase 2.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| Charter Version | 0.2 |
| Date | 2026-11-25 |
| Prepared By | PMO ISSE, with the chief engineer as board chair, the privacy officer, program legal counsel, the ML Team lead, and the intelligence mission leads |
| Approved By | Each section's own authority, as listed under Approval |
| Source SADD Version | 0.9 |
| Source SIP Version | 0.7 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-25 | PMO ISSE | Initial draft |
| 0.2 | 2026-11-25 | PMO ISSE | Recorded the coding agent's persistent memory, which the board reviews again before the agent is fielded, and named each tier's assurance level as the AISP sets it |

---

## Purpose and Scope

This charter is the single reference for everyone who proposes, approves, or oversees AI on KESTREL. It covers every AI use case inside the boundary, wherever its model runs. It also covers AI features vendors switch on inside products KESTREL owns. Each section revises on its own trigger, as Periodic Review and Revision lists.

---

## 1. AI/ML Use Case Inventory and Risk Tiering

*Traces to GV-4.1.1, GV-4.1.2, GV-4.1.3, and GV-4.1.4.*

**NIST Control Mapping:** PM-5 (partial), RA-3 (partial), and PM-11 (partial).

**How use cases enter.** Every AI use case enters through the application intake request with an AI section, under AI Use Case Intake and Onboarding (`AI-1.1`). The request names the sponsor, the data needed, any action the use case can take, and a proposed tier. The sponsor is the intelligence mission lead for a mission use case and the ISSM for a security use case. The engineering lead sponsors a development use case.

**Discovery.** Each quarter the PMO ISSE runs a discovery sweep, checking these against the inventory:

- Azure AI service usage in every subscription
- Procurement records for anything sold with AI
- AI features vendors have switched on in products KESTREL owns

Anything found that was never submitted goes through intake, or is switched off.

**What is registered.** The inventory registers the use case, meaning the decision or action the AI supports. Each entry links to the Jira Service Management Assets records of the model versions it runs on. A change to one model therefore resolves to every use case it affects. An entry survives retraining and a model swap, since only its links change.

**Risk tiers.** A use case's tier rises with what a wrong or manipulated output could do, and with any ability to act. Model size and sophistication do not set the tier.

| Tier | Criteria | Review | Testing | Reassessed |
|---|---|---|---|---|
| High | Can act, or can affect a flight, an aircraft, or a release to partners | Full board | AI Cyber T&E at AL 4, red teaming, and the OT-adjacent assessment if it reaches the fleet | Every 6 months |
| Moderate | Produces mission output a person reviews before it is used, or changes code a person reviews | Full board | AI Cyber T&E at AL 2 or AL 3, as the AISP sets | Every year |
| Low | Internal support with no mission effect and no ability to act | PMO ISSE desk review | AI Cyber T&E at AL 1 | Every year |

**Reassessment.** A use case is re-tiered when its purpose, data sources, autonomy, or users change, not only its model. A tier increase sends the use case back to the board for a new decision.

**The inventory today.**

| Use case | Sponsor | Models | Can act | Tier |
|---|---|---|---|---|
| Onboard detection | Intelligence mission leads | Onboard EO/IR and RF detection models | No, it cues the operator in flight | High |
| Cloud detection | Intelligence mission leads | Cloud EO/IR and RF detection models | No, analysts review every detection | Moderate |
| Imagery sanitizing | Intelligence mission leads | Person-detection model | No, but its misses reach partner releases | High |
| LLM analyst assistant with report search | Mission Team 1's mission lead | Foundation model deployment, embedding model | No | Moderate |
| Mission-planning agent | Mission Team 2's mission lead | Foundation model deployment | Yes, it drafts flight plans an operator approves | High |
| AI-assisted alert triage | ISSM | Foundation model deployment | No, it summarizes and takes no action | Low |
| Coding agent | Engineering lead | Foundation model deployment | Yes, it opens merge requests a developer approves, and keeps notes per repository and developer | Moderate |

**Platform models.** A model adopted before any use case is listed here with its sponsor, provisional tier, and removal review date. It is reached only from ML Dev/Test until a use case is certified on it. KESTREL has none today.

**Review and retirement.** The PMO ISSE reviews the inventory each quarter with the discovery sweep. A retired use case is closed with its date and reason, and its model links are removed.

---

## 2. Program-Level AI Threat Assessment

*Traces to GV-4.2.1 and GV-4.2.2.*

**NIST Control Mapping:** None for the architecture baseline, and RA-3 (partial) for the ranking.

**Takes effect in Phase 2.**

**Architecture baseline.** Each year the PMO ISSE maps KESTREL's whole AI estate as one architecture in Threagile, kept as YAML in GitLab. The map covers trust zones, external interfaces, and the paths between models, use cases, and agents. It includes both agents and every use case on the foundation model. It is drawn from the SADD. It is updated whenever the SADD records a material change, such as a new use case, data path, or interface.

**Ranking.** The PMO ISSE ranks the MITRE ATLAS techniques that matter most across that map. Each technique is scored for likelihood and impact under the risk charter's method, not by how many findings it has. The program's custom Threagile image carries the AI risk rules, each citing its ATLAS techniques. The ranking uses each model's threat model and red team findings rather than repeating them. It goes to the board and to the ML and mission teams, and it feeds each model's threat model.

---

## 3. Responsible AI Policy and Principles

*Traces to GV-4.3.1 and GV-4.3.2.*

**NIST Control Mapping:** None. The SABER declines a mapping for this outcome, since its principles sit above any one control.

**Takes effect in Phase 2.** Until then, the board judges use cases against the AISP.

KESTREL adopts the DoD AI ethical principles. Each is written below as a commitment a reviewer can test a design against, mapped to the outcomes that enforce it.

| Principle | KESTREL's commitment | Enforced by |
|---|---|---|
| Responsible | Every use case has a named sponsor, and every model a named owner in the ML Team | AI Use Case Intake and Onboarding (`AI-1.1`), Model Registration and Inventory Logging (`AI-6.7`) |
| Equitable | Each detection model's recall in every tested condition stays within 10 points of its overall recall. Conditions include terrain, lighting, weather, and sensor type. | Out-of-Distribution Robustness Testing (`AI-5.5`), Model Deployment Risk Threshold Evaluation (`AI-6.5`) |
| Traceable | Analysts can see when AI contributed to a product, and every certified model traces to its data and code | Model Card Generation (`AI-5.8`), Dataset Lineage and Version Control (`AI-2.4`), AI-BOM Generation (`AI-4.15`) |
| Reliable | Each model meets its use case's certified thresholds in production, and drift beyond them triggers re-certification | Model Deployment Risk Threshold Evaluation (`AI-6.5`), Model Drift Detection and Alerting (`AI-9.1`) |
| Governable | No model commands an aircraft. A person approves every AI agent action affecting a flight. Every model can be withdrawn at once. | OT and Safety-Critical AI Governance (`AI-1.8`), Agentic Tool-Call/Action Output Validation (`AI-8.7`), Rollback/Kill-Switch Mechanism (`AI-8.14`) |

Evaluating performance across groups of people has no outcome to map to, since KESTREL's models do not decide about individuals. Section 5 records it as an open gap rather than forcing a fit.

The policy is part of every user's training on JKO.

> **Privacy.** This policy does not restate the privacy policy. KESTREL's program-wide privacy position lives there. This section covers only what AI adds on top.

---

## 4. AI/ML Governance Review Board

*Traces to GV-4.4.1, GV-4.4.2, and AI-1.8.1.*

**NIST Control Mapping:** PM-11 (partial) for the review workflow. The prohibited use case list carries no mapping of its own, since its technical enforcement stays with AI-1.8.4.

**Takes effect in late Phase 1.**

**Members.** The program office charters the board, and the chief engineer chairs it. Its members are the PMO ISSE, the privacy officer, program legal counsel, the ML Team lead, and the use case's sponsor. The foreign disclosure officer joins for any use case that touches a partner release. A quorum is the chair or the PMO ISSE, plus the privacy officer or counsel, the ML Team lead, and the sponsor.

**The review path.**

| Tier | Path | Turnaround |
|---|---|---|
| Low | A recorded desk review by the PMO ISSE, who may send it to the full board | 5 business days |
| Moderate | Full board | 10 business days |
| High | Full board, with the use case's threat model in hand | 10 business days |

Every use case gets one of three recorded decisions before any corpus is assembled or any engineering starts:

- Approved
- Approved with conditions, each naming its owner and deadline
- Rejected, with the basis stated

**Platform models.** The board admits a platform model for experimentation only. If no use case is certified on it by its recorded date, the board reviews it for removal.

**What the board decides and does not.**

| The board decides | It escalates | It may not decide |
|---|---|---|
| Whether a use case may proceed, and on what conditions | A disputed decision, to the steering committee | Accepting risk, which goes through Risk Acceptance Process (`RK-1.4`) |
| A use case's tier | A condition the team will not accept, to the steering committee | Certifying a model, which is the PMO ISSE's Certification to Field |
| Treatment of each AI supplier finding, under Section 6 | | Approving a release to a partner, which is the foreign disclosure officer's |

**Prohibited use cases.** The board rejects these at intake without review:

- A model that commands an aircraft, its flight controls, or its payload
- A model or agent that selects or nominates targets without an analyst's judgment
- An agent whose action reaches a station by any path other than the operator approval queue (F34)
- A model or agent that changes a ground control station, launch equipment, or datalink setting
- An agent that loads keys, firmware, or models onto fleet equipment

Onboard detection models only cue the operator. Agent tool scoping enforces this list technically, under OT and Safety-Critical AI Governance (`AI-1.8`). The list is part of the AI and OT training for the ML Team, the mission teams, and Fleet Operations. The board reviews it each year.

**Reporting.** The board sends a posture report to the steering committee each quarter, as Section 7 sets out.

---

## 5. AI/ML Regulatory and Framework Mapping

*Traces to GV-4.5.1.*

**NIST Control Mapping:** None. The SABER declines a mapping for this outcome, since its subject is the AI framework landscape rather than one control.

**Takes effect in Phase 2.**

| Source | Basis |
|---|---|
| DoD AI Cybersecurity Risk Management Tailoring Guide | Binding, as the AO directs |
| DoD AI ethical principles, and the Responsible AI strategy and implementation pathway | Binding departmental policy |
| NIST AI Risk Management Framework | Voluntary alignment |
| OWASP Securing Agentic Applications | Voluntary alignment, through SABER v2.0 |

The basis matters. An unmet binding requirement is a finding for the POA&M. An unmet voluntary one is a choice the board records.

The PMO ISSE breaks each source into testable requirements and maps each to the outcome that satisfies it. The rows join the Compliance focus area's regulatory mapping register (`CO-1.1`), not a second register here. An unmatched requirement becomes a gap with a named owner. A new or revised AI directive is assessed within a quarter of issue.

**Permanently open gaps.** Three requirements have no technical control to map to. KESTREL records each as an owned gap instead of forcing it onto the nearest test.

| Gap | Owner | KESTREL's position |
|---|---|---|
| Documented human oversight | PMO ISSE | The approval gates are built, but their sufficiency is a judgment the board re-records each year |
| Disparate performance across groups of people | ML Team lead | KESTREL's models do not decide about individuals. The Equitable commitment in Section 3 covers performance across conditions instead. |
| Disclosure to people an automated decision affects | Program legal counsel | ISR subjects are not notified. Disclosure runs to analysts and product consumers through AI marking. |

---

## 6. AI/ML Vendor/Model Risk Tiering

*Traces to GV-4.6.1.*

**NIST Control Mapping:** RA-7 (partial).

**Takes effect in Phase 2.**

Each AI supplier starts at the tier the SCRM plan's vendor process gives it. The board then raises the tier for exposures a standard questionnaire does not ask about.

| Supplier and model | Starting tier | AI exposures | AI tier |
|---|---|---|---|
| Microsoft, for the Azure OpenAI foundation model | Moderate | Training corpus not attested. Model versions retire on the provider's schedule. Abuse monitoring is an exemption Microsoft grants, not a setting. If access ends, every LLM use case stops, with no fallback model. | High |
| OpenHands, the coding agent's open-source framework | Low | No supplier stands behind it. Its releases change agent behavior. | Moderate |
| Public pretrained backbones for the detection models | Low | Training data not attested, and a backbone could carry a backdoor. Each enters only through Artifactory after scanning. | Moderate |

Any supplier risk KESTREL chooses to carry goes through Risk Acceptance Process (`RK-1.4`). The board decides treatment but accepts nothing itself. Each vendor-delivered model is registered in Assets once its risk is treated, and each use case certified on it is then linked.

---

## 7. AI/ML Governance Posture Report

*Traces to GV-4.4.4, AI-6.7.1, AI-6.7.2, and GV-4.6.3.*

**NIST Control Mapping:** PM-6 (partial).

**Takes effect in Phase 2.** The PMO ISSE exports this section each quarter for the steering committee and the AO. It draws on the other sections' tracking and the model registries, and recomputes nothing.

**Posture as of 2026-11-25.**

| Measure | Value |
|---|---|
| Use cases by tier | High 3, Moderate 3, Low 1 |
| Use cases approved | None yet. The board is chartered in late Phase 1. |
| Open board conditions | None |
| Open AI supplier findings | None yet. Section 6's tiers are proposed. |
| Open regulatory gaps | The 3 permanent gaps in Section 5 |

**Model inventory.** Both registries are summarized here, self-hosted models from Artifactory and vendor-hosted ones from Assets. Technical fields, such as artifact digests and training runs, stay in the registries.

| Model | Vendor or publisher | Where it runs | Owner | Criticality | Classification | AI tier | Status |
|---|---|---|---|---|---|---|---|
| Onboard EO/IR and RF detection models | KESTREL, from public backbones | Aircraft | ML Team | Tier 1 | CUI | Moderate | Not yet certified |
| Cloud EO/IR and RF detection models | KESTREL, from public backbones | ML Prod | ML Team | Tier 2 | CUI | Moderate | Not yet certified |
| Person-detection model | KESTREL, from a public backbone | Data lake sanitizing pipeline | ML Team | Tier 2 | CUI | Moderate | Not yet certified |
| Embedding model | KESTREL | ML Prod | ML Team | Tier 2 | CUI | Moderate | Not yet certified |
| Foundation model deployment | Microsoft | Azure OpenAI in KESTREL's tenant | ML Team | Tier 2 | CUI | High | Not yet registered |

---

## Appendix: Reference Data and Live Registers

**Review Board Decision/Condition Tracking Record** *(GV-4.4.3)*: Every board decision, its tier, its conditions and their owners, and proof each condition closed before certification. It is held in Jira from late Phase 1.

**AI/ML Vendor/Model Risk Escalation and Remediation Register** *(GV-4.6.2)*: Every AI supplier finding, with its severity, treatment, owner, and target date, held in Jira.

**MITRE ATLAS Program-Level Threat Ranking** *(GV-4.2.2)*: The current ranking from Section 2, held in Confluence. The first is due in Phase 2.

**AI/ML Use Case Inventory** *(GV-4.1.1 and GV-4.1.3)*: The live inventory, held as a Jira project from Phase 1. Section 1 shows it as of this version.

The requirement-to-control traceability record (`GV-4.5.2`) lives with the SCTM, not here. The model registries are summarized in Section 7, not kept here.

---

## Approval

| Section | Approved by | Status |
|---|---|---|
| 1. Use Case Inventory and Risk Tiering | The board's chair | Pending |
| 2. Program-Level AI Threat Assessment | The ISSM | Pending |
| 3. Responsible AI Policy and Principles | The Configuration Control Board, as a standard under the Governance Program Charter | Pending |
| 4. AI/ML Governance Review Board | The program manager, who charters the board for the program office | Pending |
| 5. AI/ML Regulatory and Framework Mapping | The ISSM | Pending |
| 6. AI/ML Vendor/Model Risk Tiering | The ISSM, with any accepted risk routed through RK-1.4 | Pending |
| 7. AI/ML Governance Posture Report | The AO, as its reader | Pending |

**Circulated To:** the board, the intelligence mission leads, program legal counsel, the privacy officer, the ML Team, the mission teams, Fleet Operations, and the steering committee.

---

## Periodic Review and Revision

Each section revises on its own trigger:

- **Use case inventory:** each quarter with the discovery sweep, and when a use case's purpose, data, autonomy, or users change
- **AI threat assessment:** each year, and when the SADD records a material change to the AI estate
- **Responsible AI policy:** each year, under the Governance Program Charter's document lifecycle
- **Review board:** when its membership, scope, or decision thresholds change. The prohibited use case list is reviewed each year.
- **Regulatory mapping:** each year, and within a quarter of a new or revised AI directive
- **Supplier tiering:** each year, and when a supplier or the control baseline changes
- **Posture report:** exported each quarter
- **Any section:** a product substitution recorded in the Security Implementation Plan, for any product the section names
