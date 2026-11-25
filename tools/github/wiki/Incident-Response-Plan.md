> **Notional system.** KESTREL is fictional. This page stands in for a governing plan in KESTREL's self-hosted Confluence. Its names, thresholds, and decisions are invented to show a completed Incident Response Plan.

# KESTREL Incident Response Plan (IRP)

This plan governs how KESTREL responds to an adversary, from declaring an incident through containment, reporting, and the review that follows. It is the platform-independent policy layer above KESTREL's runbooks, which hold the step-by-step actions. It carries out the design decisions in the [Response section of the SADD](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/09-response.md) and names the products that enforce them. The [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/09-response.md) is the record of each product selection, and a substitution there revises this plan.

**NIST Control Mapping:** IR-1 (partial) and IR-8 (full), held through RS-4.1.

> **Interim IRP in Phase 1.** The interim authorization to test runs from the first build, so part of this plan takes effect early. Sections 1, 2, 3, 6, and 8 form the interim IRP, approved in Phase 1. They cover declaring an incident, reporting it, and who acts. Sections 4, 5, and 7 and the runbooks take effect when the full IRP is approved in Phase 2. The fleet rules in Section 5 apply from Phase 3, when the fleet integrates.
>
> Until the full IRP is approved, containment is manual. The owning team acts at the ISSM's direction, and the CSSP's containment playbooks start in Phase 2. Responders preserve an affected host and its logs and reimage nothing without the ISSM's approval.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| IRP Version | 0.1 |
| Date | 2026-11-24 |
| Prepared By | KESTREL ISSM, with Fleet Operations, the ML Team, the CSSP, the PSO, and program counsel |
| Approved By | Configuration Control Board, chaired by the chief engineer |
| Source SADD Version | 0.5 |
| Source SIP Version | 0.3 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-24 | KESTREL ISSM | Initial draft, marking the sections that form the interim IRP for Phase 1 |

---

## Purpose and Scope

This IRP covers every component inside KESTREL's authorization boundary. That includes the IL5 cloud, the mission data center, the alternate site, the UAS fleet, and KESTREL's AI models and agents. It also covers a performer laptop holding KESTREL source code, though the performer handles that laptop's own response. It does not cover the IL6 enclave, which has its own plan, beyond the spill reporting in Section 6. Restoring the mission after an incident belongs to the Contingency Plan. The yearly functional exercise rehearses the handoff between the two plans.

---

## 1. Team Structure, Authorities, and Resourcing

*Traces to RS-1.2.1, RS-1.2.3, and RS-1.2.4.*

| Role | Who holds it | Authority |
|---|---|---|
| Incident lead | The ISSM, or an ISSO the ISSM names | Declares and closes incidents, sets severity, directs containment and eradication, and makes every report to the AO |
| Investigators | The ISSOs and security analysts | Investigate in Splunk Enterprise Security, collect evidence, and run approved playbooks |
| Around-the-clock containment | The CSSP | Runs the pre-approved containment playbooks when an incident cannot wait for the Security Team, and holds no administrative role |
| System owners | The Platform Team, IT Operations, the Data Team, and Fleet Operations | Carry out containment and eradication on their own systems at the incident lead's direction |
| Model owner | The ML Team | Accountable for any model implicated in an incident, including withdrawing a model version |
| Use case owner | The team that sponsors the use case | Decides whether a use case keeps running, including the mission-planning agent and the coding agent |
| Flight authority | Fleet Operations' operations lead, or the shift lead at the operating site | Approves any action that touches a station, launch equipment, or a datalink, under Section 5 |
| Shutdown authority | The program manager | Approves taking a mission service offline, on the incident lead's recommendation |

**On-call coverage.** One security analyst is on call at all times on a weekly rotation. Jira Service Management reaches the analyst through the paging service. An ISSO backs up the analyst, and the ISSM is the next step. The CSSP monitors around the clock, so it covers the minutes before the on-call analyst responds.

**Escalation.** A severity 1 or 2 incident also pages the ISSM and the affected team's lead. An AI incident of severity 1 or 2 goes to the AI/ML Governance Review Board within one business day. The board decides whether the use case keeps running and whether its certification stands. An AI incident carries no reporting duty beyond Section 3, unless it exposes personal information or partner data.

**Resourcing.** The Security Team staffs two ISSOs and four security analysts, enough for the on-call rotation and its backup. Every responder trains on KESTREL's tools and runbooks before joining the rotation, then again each year. Training uses simulated incidents in the exercise environment. The program manager funds the CSSP agreement, Splunk Enterprise Security, Splunk SOAR, and the paging service through the program budget. The program manager's endorsement of this staffing is a standing commitment, reviewed with this plan each year.

---

## 2. Incident Classification, Severity, and Escalation Triggers

*Traces to RS-2.4.1, RS-2.5.1, RS-2.5.2, and DE-1.7.3.*

**Asset criticality.** Each asset carries a criticality tag in Jira Service Management Assets, set from the business impact analysis. The asset's owning team is accountable for the rating.

| Criticality | What it covers today | Mission consequence | Response commitment |
|---|---|---|---|
| Tier 1 | The command link, the ground control stations, the identity provider, the HSMs and PKI, the privileged access platform, the hubs' rule base, and the pipeline's signing and registry path | Loss stops identity, signing, release, or flight control | Contain within 1 hour of declaration |
| Tier 2 | The data lake, the mission teams' applications and databases, the service desk, and the security monitoring platform | Loss degrades collection, analysis, or release | Contain within 4 hours |
| Tier 3 | Dev/test, training scratch, and experimentation | Loss delays engineering work only | Contain within 1 business day |

Until the business impact analysis is approved, the tiers above are provisional, matching the backup tiers in the Contingency Plan.

**Severity.** Splunk Enterprise Security computes severity from four inputs. They are the asset's criticality, the sensitivity of the data at risk, the incident's scope, and whether it can affect an aircraft. The highest input sets the floor.

| Severity | Any of these | Acknowledge within | Paging route |
|---|---|---|---|
| 1 | Can affect an airborne aircraft or flight control. Confirmed compromise of a Tier 1 asset. Confirmed loss of partner data or personal information. | 15 minutes | On-call analyst, ISSO, ISSM, and the affected team's lead, at any hour |
| 2 | Confirmed compromise of a Tier 2 asset. Confirmed exposure of CUI inside the boundary. An AI agent acting outside its approved scope. | 30 minutes | On-call analyst, ISSM, and the affected team's lead, at any hour |
| 3 | Confirmed compromise confined to Tier 3. A malicious event blocked before it took effect. | 4 hours | On-call analyst, in business hours |
| 4 | A policy violation with no compromise | Next business day | Security Team queue |

A detection the analyst cannot yet confirm is scored one level lower until it is confirmed. Any responder may raise a severity. Only the incident lead may lower one, and the reason is recorded on the incident record.

**AI incident types.**

| Incident type | Example | Usual severity |
|---|---|---|
| Training data poisoning | A tampered training snapshot reaches a model in training | 2, or 1 if the model is fielded |
| Prompt injection | Instructions hidden in a retrieved report steer a model's output | 2 |
| Jailbreak abuse | A user makes the foundation model ignore its system prompt | 3, or 2 if data leaves the user's need to know |
| Model theft | Model weights leave the registry or a serving endpoint | 1 for an onboard model, 2 otherwise |
| Personal information in model output | A model returns personal information the user may not see | 1 |
| Concept drift by an adversary | A detection model's accuracy falls as an adversary changes signatures | 2 |
| AI agent misuse | An agent calls tools outside its approved scope, bypasses an approval, or chains tool calls it was not granted | 2, or 1 if it touches a flight |
| Tampered or misbehaving edge model | An onboard model fails its hash check or behaves outside its certified envelope | 1 |
| Foundation model compromise | The provider reports a compromise of the deployment KESTREL uses | 2 |

**Declaring an incident.** A correlated Splunk Enterprise Security alert above the declaration threshold opens a record in Jira Service Management. The record carries the asset's owner, team, criticality, and recent changes from Assets. The on-call analyst confirms and declares the incident, or closes the record with a reason.

**Network and OT anomalies.** The CSSP triages a network or OT anomaly first. Platform Team network engineers adjudicate IT anomalies, and Fleet Operations' OT maintainers adjudicate ground segment ones. The adjudicator saves the Corelight or Nozomi capture to the incident record before the sensor buffer rolls. An anomaly becomes an incident when any of these holds:

- The adjudicator confirms it as malicious.
- It stays unexplained four hours after triage on a Tier 1 asset, or one business day on any other.
- It touches a command and control path to an aircraft.

---

## 3. Reporting, Notification, and External Communications

*Traces to RS-1.6.1, RS-1.6.2, and RS-1.6.4.*

| Obligation | Trigger | Deadline from discovery | Who reports | How |
|---|---|---|---|---|
| CSSP | Every declared incident | At declaration, automatically | Jira Service Management | Notification to the CSSP's operations center |
| DoD reporting chain | Every reportable event under CJCSM 6510.01B | The timeline CJCSM 6510.01B sets for its category | The CSSP | The CSSP's own reporting channel |
| AO | Severity 1 or 2 | 1 hour for severity 1, 4 hours for severity 2 | The ISSM | Phone, then the AO incident report template in Confluence |
| AO | Severity 3 or 4 | The monthly continuous monitoring report | The ISSM | The monthly report |
| Partner nations | Partner data affected | 24 hours after the AO is told | The foreign disclosure officer | The channel each memorandum of agreement names |
| DoD component privacy office | Personal information breached | The timelines DoD privacy policy sets, with the privacy officer told within 1 hour | The privacy officer | The component's breach report |
| DC3 | A performer laptop holding KESTREL source code is involved | 72 hours, under DFARS 252.204-7012 | The performer | The DIBNet portal |
| Vendor | The incident involves a vendor's product | When the incident lead decides the vendor is needed | The ISSM | The vendor's support agreement |

**What may be disclosed.** A vendor learns only what it needs to fix its product, and never CUI about KESTREL's missions. A partner nation learns what its agreement allows, cleared by the foreign disclosure officer. Nothing classified is disclosed through any KESTREL channel.

**Who speaks for the program.** Only the program manager speaks for KESTREL outside the reporting chain. The program office's public affairs officer reviews each statement first. No responder speaks to the press or posts about an incident.

**Exchange with the CSSP.** During an incident, the Security Team and the CSSP share indicators, scope, and techniques on the incident record. Indicators also travel as STIX over TAXII on F31, and the Security Team vets each one before use. Both sides handle what they share as CUI.

---

## 4. Evidence Handling and Legal and Compliance Requirements

*Traces to RS-2.3.4.*

**Collection.** Defender XDR live response collects memory and files, and a Splunk SOAR playbook takes cloud disk snapshots. Evidence goes to the retention-locked evidence store, a NetApp StorageGRID bucket with S3 Object Lock that only the Security Team can read. Analysts examine copies on the isolated forensic workstation. Captures never include key material, and datalink crypto modules and HSMs are never imaged.

**Retention.** Program counsel, the PSO, and the AO set these periods.

| Evidence | Kept for |
|---|---|
| Captures from a severity 1 or 2 incident | 3 years after the incident closes |
| Captures from a severity 3 or 4 incident | 1 year after the incident closes |
| Captures from an incident reported to DC3 | At least 90 days after the report, and 3 years after closure |
| The incident record and chain of custody log | For the life of the system |

**Legal hold.** Program counsel, the PSO, or the AO may place a hold on any evidence. A hold stops deletion until program counsel releases it with the AO's concurrence. The ISSM records each hold and release on the incident record.

**Chain of custody.** The record for each item captures:

- What was collected, from which asset, and its hash.
- Who collected it, when, and with which tool.
- Every person who handled it afterward, and why.
- Where it is stored, and any hold on it.

---

## 5. Containment Authorities

*Traces to RS-3.1.3, RS-3.3.1, and RS-3.3.2.*

**Automated actions.** Splunk SOAR runs each containment playbook and updates the incident record at each step. Its service identity can take only the actions below. It cannot change policy beyond quarantine or touch break-glass accounts, Tier 0, or fleet systems.

| Action | Disruption | How it runs |
|---|---|---|
| Enrich an alert, open a ticket, or send a notification | None | Unattended |
| Isolate a host outside production with Defender XDR | Low | Unattended |
| Move a cloud workload into a Panorama quarantine policy | High | Security Team approval in the playbook |
| Move a data center host into an ACI quarantine endpoint group | High | Security Team approval in the playbook |
| Disable an account and revoke its sessions in Entra ID and Defender XDR | High | Security Team approval in the playbook |
| Suspend a workload or AI agent identity | High | Security Team approval in the playbook |

An approval request carries the incident record and the action requested. The on-call ISSO or the ISSM decides within 15 minutes for severity 1 and within 1 hour otherwise. The decision is recorded before the action runs. If nobody answers in time, the action stays held, unless the CSSP judges the incident cannot wait. The CSSP may then run the playbook on its own authority, which pages the Security Team at once. The Security Team reviews or reverses every CSSP run by the next business day.

**Fleet and ground segment actions.** No playbook touches fleet systems or an operating site's admission control. Fleet Operations runs every fleet action by hand, using the Pre-Approved Manual Containment Runbook.

| Asset | While an aircraft under its control is airborne | On the ground |
|---|---|---|
| Ground control station | Prohibited | Operations approval |
| Launch and recovery equipment | Prohibited | Operations approval |
| Datalink | Prohibited | Operations approval |
| Ground segment firewall rule change | Operations approval | Operations approval |
| An operating site's conduit, cut at the data center side | Operations approval, limited to 4 hours | Fleet Operations may act, limited to 4 hours |
| Operating site services | Operations approval | Fleet Operations may act |

An operations approval comes from the operations lead or the shift lead at that site. The request carries the incident record and the action requested. If no one answers within 10 minutes, the action stays held. The incident lead then escalates to the operations lead's chain. Nothing runs without an answer.

Cutting a conduit holds any flight plan queued on F34, so it needs the operations lead's concurrence while a plan is pending. It also blinds OT monitoring at that site. After 4 hours the operations lead and the ISSM must renew the cut, or Fleet Operations restores the conduit. Before a station is isolated, the manual runbook recovers its airborne aircraft safely. The aircraft's lost-link procedure is the fallback if a station is lost in flight.

---

## 6. Classified Data Spillage Notification

*Traces to RS-3.5.4.*

A spill is classified information found on a KESTREL system. The likeliest path is a high-to-low product carrying classified content, which KESTREL's content and marking checks catch. Another is classified text pasted into a language model prompt. Spill reporting runs separately from Section 3, on the deadlines security policy sets.

| Who is told | By whom | Deadline from discovery | Path |
|---|---|---|---|
| The ISSM | Whoever finds the spill | At once | Phone or in person |
| The PSO | The ISSM | 1 hour | Phone or in person |
| The AO | The ISSM | 4 hours, or sooner if the PSO directs | Secure phone, or the parent organization's classified network |
| The original classification authority | The PSO | As the PSO directs | The PSO's own channel |
| The CSSP | The ISSM | 4 hours | Secure phone |
| The IL6 enclave's owner, when the spill came through a high-to-low product | The ISSM | 4 hours | The enclave's security office, by secure phone |

No spill report travels over a KESTREL system or the Microsoft 365 DoD tenant, since either may hold the spilled content. Reports name the incident ID and never restate the classified content.

The ISSM leads the spill response and traces every copy. The Data Team, Platform Team, ML Team, IT Operations, and Fleet Operations each sanitize their own copies. Every affected copy stays held until the PSO and the AO release it.

---

## 7. Response Performance Metrics and Continuous Improvement

*Traces to RS-2.5.4 and RS-3.7.1.*

A response metrics dashboard in Splunk Enterprise Security tracks the measures below. The ISSM reports them in the monthly continuous monitoring report.

| Metric | What it measures |
|---|---|
| Mean time to detect | From the earliest evidence of adversary activity to the alert |
| Mean time to triage | From the alert to declaration or closure |
| Mean time to contain | From declaration to containment, by severity |
| Mean time to recover | From containment to the system's return to service |
| Open incidents | By severity, and by age |
| Acknowledgment adherence | The share of incidents acknowledged within Section 2's deadlines |
| Reporting adherence | The share of reports made within Section 3's deadlines |

**Lessons-learned review.** Every severity 1 or 2 incident ends with a review within 10 business days of closure. The incident lead runs it, with the responders, the owning team's lead, and the CSSP. Fleet Operations joins when the fleet was involved, and the ML Team when a model was. The review is blameless. Its findings name the detection that missed, the procedure that failed, or the design weakness behind the incident. They never name a person. Each finding becomes a Jira item, and design findings go to the PMO ISSE. Exercises feed their findings through the exercise program instead.

---

## 8. Cyber Defense Service Provider Coordination

*Traces to RS-1.7.1.*

KESTREL's CSSP works under its service agreement, which defines its detection and response role, its analysts' VDI access, and its containment playbooks.

| Function | The CSSP | KESTREL's Security Team |
|---|---|---|
| Monitoring | Around the clock, from all telemetry Splunk forwards | Business hours, plus the on-call analyst |
| Triage | First triage of every alert | Confirms and declares incidents |
| Threat intelligence | Supplies advisories and indicators, which land on incident records automatically | Vets each indicator before use |
| Containment | Runs the pre-approved playbooks when an incident cannot wait | Approves and runs every other action, or directs the owning team |
| Reporting | Reports to the DoD reporting chain | Reports to the AO |

A stalled telemetry feed to the CSSP raises an alert in Splunk, and the Platform Team restores it. The Security Team tells the CSSP of every declared incident through Jira Service Management. The CSSP tells the Security Team of what it finds through its operations center and the incident record.

**Directives.** The ISSM receives each CSSP directive, logs it in Jira Service Management, and assigns an owner. The owner acts by the directive's deadline. The ISSM closes the directive with evidence and confirms closure to the CSSP. A directive that cannot be met by its deadline goes to the AO with a plan.

---

## Appendix: Referenced Companion Documents

Each runbook is versioned against the IRP version it executes under. None is written yet, and all are due with the full IRP in Phase 2 unless noted.

**Cloud Platform-Native Incident Response Runbooks** *(RS-1.1.1)*: One runbook each for a compromised subscription, an exposed storage service, and a stolen workload identity. Each uses the cloud provider's native response actions. The Security Team writes them with the Platform Team.

**AI/ML Incident Runbooks** *(RS-1.1.3)*: One runbook each for a poisoned training snapshot, prompt injection through retrieved reports, and a misbehaving AI agent. Others cover a tampered or misbehaving onboard edge model, and a foundation model incident on the provider's side. Each names the detection that raises it and its action, such as withdrawing a model version or suspending an agent's identity. The ML Team writes them.

**Pre-Approved Manual Containment Runbook** *(RS-3.3.3)*: The manual isolation steps for each asset type in the ground segment. It covers the safe state each step needs and the safe recovery of airborne aircraft before a station is isolated. Fleet Operations writes it before the fleet integrates in Phase 3.

---

## Approval

**Approved By:** Pending. The Configuration Control Board approves the interim IRP in Phase 1 and the full plan in Phase 2. The CSSP confirms the split in Section 8 before either approval.

**Circulated To:** the Security Team, the Platform Team, IT Operations, the Data Team, the ML Team, Fleet Operations, every team lead, the PSO, the privacy officer, the foreign disclosure officer, program counsel, and the CSSP.

**Approval Date:** Pending.

---

## Periodic Review and Revision

**Review Cadence:** Annually, as a floor.

**Revision Triggers:**
- A change to the response team, its roles, or its resourcing
- A change to KESTREL's reporting obligations or the CSSP's service agreement
- A change to the criticality or severity models, including approval of the business impact analysis
- A change to the systems this plan covers, such as the fleet's integration in Phase 3
- A problem found during an incident, an exercise, or the plan's own execution
- A product substitution recorded in the Security Implementation Plan, for any product this document names
