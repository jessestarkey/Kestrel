> **Notional system.** KESTREL is fictional. This page stands in for a governing plan in KESTREL's self-hosted Confluence. Its names, thresholds, and decisions are invented to show a completed Continuous Monitoring Plan.

# KESTREL Continuous Monitoring Plan (ConMon)

This plan sets what KESTREL monitors, how often each control is checked and assessed, and who hears the result. It carries out the design decisions in the [Compliance section of the SADD](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/13-compliance.md). The [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/13-compliance.md) selects the tools that collect each metric, and a substitution there revises this plan.

**NIST Control Mapping:** CA-1 (partial), CA-7 (partial), CA-7(3) (partial), and PM-31 (partial), held through CO-2.1.

> **Interim plan in Phase 1.** The interim authorization to test runs from the first build, so this plan takes effect in two steps. The AO approves it as the interim ConMon plan in Phase 1, covering the metrics marked Phase 1 below. The AO approves the full plan in Phase 2, when the remaining metrics and the trend analysis begin. A metric marked Phase 2 or Phase 3 starts when its producing outcome is built.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| ConMon Version | 0.1 |
| Date | 2026-11-25 |
| Prepared By | KESTREL ISSM, with the Platform Team and the Security Team as owners of the monitoring tools |
| Approved By | The AO |
| Source SADD Version | 0.5 |
| Source SIP Version | 0.3 |
| Source SCTM Version | None yet. The SCTM's first version follows in Phase 1, and this plan's frequencies are rechecked against it. |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-25 | KESTREL ISSM | Initial draft, marking the metrics that form the interim plan for Phase 1 |

---

## Purpose and Scope

This plan covers KESTREL's whole authorization boundary. That includes every KESTREL location, the fleet and ground segment, and KESTREL's AI models and agents. The ground segment and the fleet follow the same metrics as the rest, checked in the ways their equipment allows. Every outcome that schedules a check or an assessment uses the frequencies the AO approves here.

---

## 1. Monitoring Strategy and Metrics

*Traces to CO-2.1.1.*

KESTREL monitors what would change a decision. Each metric below names the decision that follows when it crosses its threshold, and the owner who makes it. A metric no decision depends on is dropped. Where a metric's tool does not exist yet, it starts in the phase shown.

| Focus Area | Metric | Producing Outcome | Threshold That Triggers Action | Owner | From |
|---|---|---|---|---|---|
| Identity | Accounts dormant 35 days and still enabled | ID-1.8 | Any | Platform Team | Phase 1 |
| Identity | Access reviews completed on time | ID-1.9 | Any review past its due date | ISSM | Phase 1 |
| Identity | Standing privileged role assignments outside break-glass | ID-4.3 | Any | Platform Team | Phase 1 |
| Identity | Break-glass account use | ID-4.6 | Any use | ISSM | Phase 1 |
| Identity | AI agent tool approvals past their expiry | ID-3.3 | Any still in use | Owning team lead | Phase 3 |
| Device and Infrastructure | Critical and high vulnerabilities past their VPMP deadline | DI-4.8 | Any | Owning team | Phase 1 |
| Device and Infrastructure | Unapproved configuration drift on Tier 0 or DMZ assets | DI-4.4 | Any | Platform Team | Phase 1 |
| Device and Infrastructure | Agentable hosts without a reporting EDR sensor | DI-5.4 | Any for more than 24 hours | Platform Team | Phase 1 |
| Device and Infrastructure | Assets without a resolving owner | DI-1.3 | Any for more than 14 days | Platform Team | Phase 1 |
| Device and Infrastructure | Fleet configuration drift from the manufacturer baseline | DI-4.7 | Any | Fleet Operations | Phase 3 |
| Network and Environment | Firewall running policy differing from its repository | NE-1.1 | Any for more than 1 business day | Platform Team | Phase 1 |
| Network and Environment | Public access re-enabled on a managed service | NE-2.1 | Any | Platform Team | Phase 1 |
| Network and Environment | Reachable services missing from the PPSM baseline | NE-2.12 | Any | Security Team | Phase 2 |
| Network and Environment | Rogue access points or unauthorized radios | NE-1.8 | Any | Security Team | Phase 2 |
| Application | Pipeline gate overrides | AP-4.5 | Any without a recorded approval | PMO ISSE | Phase 1 |
| Application | Fielded dependencies with critical vulnerabilities past deadline | AP-5.12 | Any | Owning team | Phase 2 |
| Application | Unsigned images admitted to a cluster | AP-2.13 | Any | Platform Team | Phase 2 |
| AI | Model drift past its certified threshold | AI-9.1 | Any | ML Team | Phase 3 |
| AI | Canary prompt failures | AI-9.5 | Any | ML Team | Phase 3 |
| AI | Agent actions outside approved scope | AI-8.7 | Any | Owning team lead | Phase 3 |
| Data | Certificates within 30 days of expiry without a renewal | DA-3.9 | Any | Platform Team | Phase 1 |
| Data | Key operations by an identity outside its role | DA-3.6 | Any | Security Team | Phase 1 |
| Detection | Tier 1 log sources silent | DE-3.1 | Any for more than 1 hour | Security Team | Phase 1 |
| Detection | Telemetry feed to the CSSP stalled | RS-1.7 | Any for more than 1 hour | Platform Team | Phase 1 |
| Detection | Time drift between the cloud and the data center | DE-3.4 | More than 1 second | Platform Team | Phase 1 |
| Response | Incidents acknowledged within the IRP's deadlines | RS-2.5 | Below 95 percent in a month | ISSM | Phase 2 |
| Recovery | Tier 1 backup jobs missed or failed | RC-1.6 | Any | IT Operations | Phase 1 |
| Recovery | Restore tests failed | RC-3.2 | Any | IT Operations | Phase 2 |
| Governance | Expired exceptions still in effect | GV-2.2 | Any | ISSM | Phase 1 |
| Governance | Accounts with lapsed training or rules of behavior still enabled | GV-2.3 | Any | Platform Team | Phase 1 |
| Governance | CCSD tailoring action 3's date | GV-5.10 | The replacement payload processing workstation not fielded by 2027-07-31 | PMO ISSE | Phase 1 |
| Governance | CCSD tailoring action 6's annual review | GV-5.10 | Review not held within 30 days of its anniversary | PMO ISSE | Phase 1 |
| Risk | POA&M milestones overdue | RK-1.8 | Any | ISSM | Phase 1 |
| Risk | Risk acceptances within 30 days of expiry | RK-1.4 | Any without a renewal decision | ISSM | Phase 1 |
| Compliance | Hosts not scanned in their scan window | CO-1.2 | Any | Platform Team | Phase 1 |
| Compliance | Evidence gaps for controls in the next assessment cycle | CO-1.3 | Any 30 days before the cycle | ISSOs | Phase 2 |

**Ground segment and fleet.** Fleet equipment is never actively scanned in flight. Its metrics come from the passive sensors and from checks in maintenance windows or on landed aircraft.

---

## 2. Monitoring and Assessment Frequencies

*Traces to CO-2.1.1.*

**Monitoring frequencies.** Automated Technical Control Compliance Monitoring (`CO-1.2`) schedules from this table.

| Check | Frequency |
|---|---|
| Configuration and policy checks in the cloud | Continuous, with results every 24 hours |
| Firewall policy comparison | On every pipeline run, and every 24 hours |
| Authenticated vulnerability scans of on-premises hosts | Every 7 days |
| Container and benchmark checks | On every build, and every 24 hours on running clusters |
| Log source health and telemetry to the CSSP | Every 5 minutes |
| Dormancy | Every 24 hours |
| Fleet baseline checks | In each maintenance window, and on each landed aircraft before its next flight |
| POA&M milestones and risk acceptances | Every month |

**Assessment frequencies.** Every control is assessed at least once in a three-year cycle, with a third of the families each year. Controls that change often or protect High integrity are assessed more often. The SCA runs the independent assessments. The ISSOs self-assess between them in Jira.

| Control Family | Assessment Frequency | Basis for the Tier |
|---|---|---|
| SC, for the key, signing, and datalink controls | Every quarter | They protect CCSD rows 6, 10, and 13, whose failure could put commands or code on an aircraft |
| AC and IA, for privileged access | Every quarter | Privileged access decays fast, and its failure is severe |
| CM and SI, for configuration and flaw remediation | Every quarter by self-assessment, and in Year 2 by the SCA | They change with every release |
| AC, IA, AU, PE, PS, and PT | Year 1 of each cycle | Access and accountability, assessed together |
| CM, SI, RA, SA, SR, MA, and MP | Year 2 of each cycle | Configuration, flaws, and the supply chain |
| CP, IR, AT, PL, PM, and CA | Year 3 of each cycle | Plans, readiness, and program management |
| SC, apart from the key, signing, and datalink controls | Year 1 of each cycle | Boundary and transmission protection |
| Inherited controls | When each provider's assessment renews | Accepted on the provider's current assessment under Inherited Control Validation (`GV-5.12`) |

The first cycle starts after the ATO decision on 2028-09-30. Before then, the SCA assesses every control for the ATO itself.

The Security Team has confirmed it can staff these frequencies. A frequency nobody can resource is raised before approval, never missed afterward.

---

## 3. Security Status Reporting

*Traces to CO-2.1.1.*

| Recipient | Cadence | Content | Out-of-Cycle Trigger |
|---|---|---|---|
| AO | Monthly in summary | Metrics against thresholds, open POA&M items by severity, and accepted risks | Any threshold breach on a CCSD row rated High, namely rows 6, 8, 10, and 13 |
| AO | Quarterly in full | The summary, plus assessment results, POA&M milestone status, and authorization status under GV-5.10 | A reauthorization trigger under GV-5.10 |
| Program manager | Monthly | The AO's summary, plus schedule effects of open findings | Any item the AO is told of out of cycle |
| Steering committee | Monthly | The posture dashboard, the risk register, and exception trends each quarter | A finding that needs a decision above the Configuration Control Board |
| PMO ISSE | Weekly | Pipeline gate results, and findings against the security design | A gate override, or a finding that changes the SADD |
| CSSP | Continuous | All telemetry, through Splunk | A stalled feed |

**One picture for the AO.** The ISSM builds every AO report from the Splunk posture dashboard and eMASS, not from each tool's own report. The quarterly report is also the authorization status report under Periodic Authorization Status Reporting (`GV-5.10.3`). The AO therefore receives one consistent picture.

**Reporting at once.** The ISSM tells the AO within one business day when any of these occur:

- A threshold breach on CCSD row 6, 8, 10, or 13
- A reauthorization trigger, such as a new interconnection or a slip of CCSD tailoring action 3's date
- An assessment cycle slipping by more than 30 days

---

## 4. Monitoring and Assessment Procedures

*Traces to CO-2.1.1.*

**Who runs each monitor.** The Platform Team operates the scanning and configuration tools, ACAS, Defender for Cloud, and Azure Policy. The Security Team reads every result in Splunk and reviews each finding. Fleet Operations runs the fleet checks in maintenance windows. Nobody reviews a monitor they operate.

**From failed check to finding.** A failed check opens a Jira Service Management ticket to the asset's owning team. The ticket carries the VPMP deadline for its severity. A finding that will miss its deadline becomes a POA&M item in eMASS before the deadline passes. Plan of Action and Milestones (`RK-1.8`) governs it. An ISSO closes a finding only after verifying the fix by the original check.

**Evidence.** Every result is filed in the program evidence repository, held in immutable Blob storage, under Compliance Evidence Collection and Retention (`CO-1.3`). Each artifact is tagged to its control and outcome. Fleet and OT evidence is entered by hand after each maintenance window.

**Feeding each assessment.** Before each cycle, the ISSOs check the repository for gaps and stale artifacts. The ISSM hands the SCA the monitoring results for the cycle's controls. The SCA's Security Assessment Plan then tests what monitoring does not already show, rather than repeating it.

---

## 5. Trend Analysis and Cadence Adjustment

*Traces to CO-2.1.3.*

**When and who.** The ISSM and the PMO ISSE analyze the monitoring results as a whole every six months. The first analysis follows the full plan's approval in Phase 2.

**What they look for.**

- A metric or frequency whose findings nobody acts on, which is dropped or retuned
- A finding learned from an audit, an incident, or a vendor notice, which shows a missing metric
- Several clean cycles in a row, which justify a longer interval
- Repeated findings in one place, which justify a shorter interval

Relaxing a frequency is as legitimate as tightening one. Each proposed change goes to the AO for approval under Periodic Review and Revision, and nothing changes until the AO approves it.

---

## Appendix: Live Records

**Monitoring Trend Analysis Record** *(CO-2.1.3)*: Each analysis's date, the results reviewed, the changes proposed, and the AO's decision on each, held in Confluence.

---

## Approval

**Reviewed By:** The ISSM, and the program manager as system owner.

**Approved By:** Pending. The AO approves the interim plan in Phase 1 and the full plan in Phase 2.

**Approval Date:** Pending.

---

## Periodic Review and Revision

**Review Cadence:** Annually, as a floor.

**Revision Triggers:**
- The trend analysis proposes a change the AO approves
- A finding from an audit, an incident, or a vendor notice shows a missing metric
- The AO retailors the control set, arriving through a new SCTM version
- A significant change to the system or its boundary, such as a new spoke or the fleet's integration in Phase 3
- A product substitution recorded in the Security Implementation Plan, for any tool this document names
