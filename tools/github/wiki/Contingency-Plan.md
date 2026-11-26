> **Notional system.** KESTREL is fictional. This page stands in for a governing plan in KESTREL's self-hosted Confluence. Its names, objectives, and decisions are invented to show a completed Contingency Plan.

# KESTREL Contingency Plan (CP)

This plan sets how KESTREL keeps its mission running through a disruption and restores what was lost. It covers backups, recovery objectives, the alternate site, and the manual fallbacks for when systems are down. Responding to an adversary belongs to the [Incident Response Plan](Incident-Response-Plan) (IRP), and an exercise rehearses the handoff between the two. It carries out the design decisions in the [Recovery](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/10-recovery.md) section of the SADD. The [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/10-recovery.md) is the record of each product selection, and a substitution there revises this plan.

**NIST Control Mapping:** CP-1 (partial) and CP-2 (full), held through RC-4.1.

> **Phasing.** This plan is approved in Phase 2. Tier 1 backups, immutability, and provisional Tier 1 objectives already run from Phase 1, under the provisional objectives in Section 3. The business impact analysis confirms them in Phase 2. Fleet restores and fleet drills start in Phase 3, when the fleet integrates.
>
> **A printed copy.** This plan is printed and kept at the data center, the alternate site, and each operating site. It must be readable when the identity provider is down.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| CP Version | 0.1 |
| Date | 2026-11-26 |
| Prepared By | Platform Team lead, with Fleet Operations for the fleet and ground segment sections and each team for its restoration order |
| Reviewed By | ISSM |
| Approved By | Configuration Control Board, chaired by the chief engineer |
| Source SADD Version | 0.9 |
| Source SIP Version | 0.7 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-26 | Platform Team lead | Initial draft for Configuration Control Board review |

---

## Purpose and Scope

This CP covers every system and mission process inside KESTREL's boundary, in every location, and the fleet. It plans for the loss of a service, a site, the cloud hub, or the data center for good. It does not cover the parent organization's facilities or people, which its continuity and emergency plans cover. Section 7 names where they meet.

---

## 1. Essential Functions, Critical Assets, and Coverage Scope

*Traces to RK-3.2.2 and RC-1.1.1.*

**Essential functions.** The program manager owns the business impact analysis, which the mission leads and Fleet Operations' operations lead fill in. The results below are provisional until it completes in Phase 2.

| Function | Longest it can be lost | Depends on | Tier |
|---|---|---|---|
| Flying and controlling the aircraft | Never. The fleet flies without the cloud or the data center, as Section 5 sets out. | The stations, the datalinks, and the ground segment's own sign-in | 1 |
| Signing and releasing software and models | 4 hours | Identity, the PKI and HSMs, the pipeline, and the registry | 1 |
| Collecting and ingesting data | 24 hours, since aircraft keep their recordings | The data lake, the circuits, and the ingest pipelines | 2 |
| Detecting and analyzing | 24 hours | The data lake, the mission applications, and the models | 2 |
| Releasing to partners | 24 hours | The partner API, the rights protection tenant, and the data lake | 2 |
| Retraining models | 7 days | The training cluster and the snapshots | 3 |

Every function also rests on identity, the PKI, the hubs and circuits, and the security monitoring platform. Each asset's tier is a criticality tag in Jira Service Management Assets.

**What each tier backs up.**

| Tier | What it covers | How often |
|---|---|---|
| 1 | The identity provider, the PKI, CyberArk, the hubs' rule base, the ground segment's configuration, each spoke's Key Vault, the source repository, the pipeline configuration, and the artifact and model registry | Continuous replication or log shipping, plus a daily full backup |
| 2 | The data lake, the mission teams' applications and databases, the service desk, and Splunk | Daily |
| 3 | Dev/test, training scratch, and experimentation | Weekly |

Every tier also backs up its runbooks and its OpenTofu, so a restore never depends on what was lost. HSM key backups go only to the standby HSM at the alternate site, wrapped, and never into Veeam.

---

## 2. Contingency Roster and Contact Information

*Traces to RC-4.1.4.*

| Role | Primary | Backup |
|---|---|---|
| Recovery coordinator | Platform Team lead | IT Operations lead |
| Restore team | The Platform Team's restore operators | IT Operations administrators |
| Tier 0 recovery | The Platform Team's Tier 0 administrators | A second Tier 0 administrator, from the other shift |
| Alternate site liaison | The parent organization's facility manager at the alternate site | That facility's deputy manager |
| Telecommunications liaison | IT Operations' network lead, with each carrier's account team | The Platform Team's network engineer |
| Fleet operations authority | Fleet Operations' operations lead | Fleet Operations' deputy operations lead |
| Authority to declare fallback and activate the alternate site | Program manager | Chief engineer |

**Reaching people.** Each person on the roster has two ways to be reached that do not need the identity provider. The paging service sends an incident ID and severity only. The printed call tree beside each copy of this plan lists each person's government phone. The names and numbers sit in the printed roster, updated each quarter and whenever someone on it changes.

---

## 3. Recovery Objectives and Restoration Priorities

*Traces to RC-3.1.1 and RC-4.1.1.*

**Objectives.** The program manager approves these from the business impact analysis. The Tier 1 figures are provisional from Phase 1 until the analysis confirms them in Phase 2.

| Tier | Recovery time objective | Recovery point objective |
|---|---|---|
| 1 | 4 hours | 15 minutes |
| 2 | 24 hours | 24 hours |
| 3 | 7 days | 24 hours |

Raw collection has an extra safeguard. Aircraft storage modules keep each recording until the backup that holds it completes. A tier that misses its objective in a test is raised to the AO.

**Restoration order.** The mission owners agreed this order in advance, so nobody argues it during an event.

1. Identity, with Active Directory before its cloud projection
2. The PKI and the HSMs
3. CyberArk and each spoke's Key Vault
4. The hubs' rule base and the circuits
5. Splunk, so the rest of the recovery is watched
6. The source repository, the pipeline, and the registry
7. The ground segment's configuration, if it was lost
8. The data lake, then each mission team's zone in its own spoke
9. The mission applications, the partner API, and the service desk
10. Tier 3, last

**The known state.** Each system is restored to its last backup from before the disruption. After an incident, the IRP's lead names a backup from before the compromise. A restored system returns to service only when it passes these checks:

- Its image and configuration match their signed baselines
- A compliance scan passes under the CMP
- Every credential it held is rotated, if an incident led to the restore
- Splunk shows its logs arriving

---

## 4. Backup Policy, Retention, and Geographic Protection

*Traces to RC-1.5.2, RC-2.3.1, and RC-2.3.2.*

**Policy by tier.** One policy per tier sets schedule, retention, and immutability. The pipeline binds it to each resource from its criticality tag, and an untagged resource cannot be deployed. Azure Backup applies it in the cloud, and Veeam applies it on premises.

| Tier | Schedule | Kept for |
|---|---|---|
| 1 | Continuous replication or log shipping, plus a daily full backup | 35 daily copies and 12 monthly copies |
| 2 | Daily | 35 daily copies and 12 monthly copies |
| 3 | Weekly | 4 weekly copies |

**Immutability.** Every copy is locked until its retention ends. StorageGRID's S3 Object Lock and immutable Blob storage hold each one in compliance mode. No account can shorten or remove the lock, however privileged. A spill caught in a locked copy is sanitized by destroying that backup set's key, under the KMP.

**Geographic protection.** Copies leave the data center on two paths. One goes to the alternate site, and the other to immutable storage in US Gov Arizona. No single site or region holds every copy. Replication runs often enough to meet each tier's recovery point. While the cloud hub is down, the data center keeps local copies, and the alternate site's standby runs on its last replication.

---

## 5. Restoration Testing and Manual/Degraded-Mode Fallback

*Traces to RC-3.2.1, RC-3.5.1, and RC-3.5.3.*

**Restore testing.** Each quarter, the Platform Team restores a sample from every tier, using only the written procedure. The sample rotates so every Tier 1 system is restored at least once a year.

- **Pass.** The restore finishes within its tier's recovery time, holds data within its recovery point, and passes Section 3's checks.
- **Yearly.** A full restore of the identity provider and of one mission team's prod spoke.
- **The registry.** Every model, signed release, and baseline is verified against its signature after the restore.
- **The fleet, from Phase 3.** Fleet Operations restores fleet captures to the spares or the simulator.

A failed test is a finding, and the restore procedure is fixed before the next quarter.

**Manual fallbacks.**

| Process | How it keeps running | What it cannot do | Reconciling afterward |
|---|---|---|---|
| Flying the aircraft | Operators fly from the stations with local smart card sign-in | Load new plans or edge models from the cloud | None needed, since the stations keep their own records |
| Collecting data | Aircraft keep recordings on their storage modules, which hold about 72 hours | Fly past that limit without losing recordings | Recordings are ingested oldest first when the lake returns |
| Mission planning | Planners draft plans by hand at the stations, if the planning agent is unavailable | Draft with the agent | Each manual plan is entered into the planning queue afterward |
| Analysis | Analysts work from the last delivered products | Analyze new collection | New collection is analyzed in arrival order |
| Partner releases | Paused | Release anything | Releases resume in queue order |
| Retraining | Paused | Retrain any model | Resumes from the last snapshot |

**Triggers.** Fallback starts when one of these is observed:

- Both circuits to the cloud hub are down for more than an hour
- The data center or the cloud hub is lost
- Identity is unavailable beyond its 4-hour recovery time
- The IRP's containment isolates a site or a hub

**Authority.** The program manager declares fallback and ends it, or the chief engineer if the program manager cannot be reached. Fleet Operations' operations lead may move the fleet to station-only operation at once to protect an aircraft in flight. The program manager confirms that decision afterward.

Every contingency role trains within 30 days of assignment, after a system change, and each year. Fleet drills start in Phase 3.

---

## 6. Alternate Site and Telecommunications Arrangements

*Traces to RC-3.4.1, RC-3.4.2, and RC-4.1.1.*

**The alternate site.** A parent organization facility in a different region, over 250 miles from the data center, so no regional event reaches both. The facility agreement names:

- The program manager and the chief engineer as the only people who may activate it
- Tier 1 services running there within their 4-hour recovery time
- Work seats for the Platform Team and the Tier 0 administrators within 24 hours
- KESTREL's priority access in an area-wide emergency

**What is staged there.**

- Warm standbys for Tier 1, including domain controllers, an issuing certificate authority, and CyberArk
- A second nShield HSM, with the escrowed keys
- A copy of every backup
- Two privileged access workstations

**When it could still be unreachable.** Three events could still cut KESTREL off from the site. A DISN outage could cover the region, the parent organization's own emergency could take the facility first, or a travel restriction could keep staff away. In each case, Tier 2 restores into recovery spokes in US Gov Arizona, managed from the cloud.

**Telecommunications.** The data center's two circuits come from different carriers. Each runs on its own path, through its own building entry, to a different meet-me point. No single carrier, path, or meet-me point can isolate it. Every carrier agreement carries priority restoration and the carrier's own contingency plan. Production traffic fails from one circuit to the other each quarter. The alternate site has its own circuit to the cloud hub over DISN, which the yearly failover exercise proves.

**Not returning to the data center.** If the data center is destroyed, or cannot return within 30 days, KESTREL does not wait for it. Tier 2 services stay in the recovery spokes in US Gov Arizona, each mission team's zone in its own spoke. The alternate site becomes the on-premises primary. Activating the alternate site is an AO review trigger, and so is this decision.

---

## 7. Coordination with Related Plans and Information Sharing

*Traces to RC-4.1.1 and RC-4.1.5.*

**Who a real disruption brings in.**

| Party | Its plan or role |
|---|---|
| Security Team lead | Owns the IRP, which runs alongside this plan whenever an adversary caused the disruption |
| The parent organization | Its continuity of operations plan and occupant emergency plans for the data center and the alternate site |
| The alternate site's facility manager | Operates the site under the facility agreement |
| Fleet Operations' operations lead | The fleet's operations authority |
| The CSSP | Monitors the recovery, under its service agreement |
| Microsoft | Restores provider services, under its authorization |
| The circuit carriers | Restore the circuits, under priority restoration |

Each party was consulted while this plan was drafted. The record of that coordination sits with the plan in Confluence.

**Sharing during a disruption.** Contingency information is CUI.

- The program manager decides what is shared with any outside party.
- Anything shared with a partner nation goes through the foreign disclosure officer first.
- Carriers and Microsoft receive only what their restoration needs, such as circuit or service identifiers.
- Reporting to DC3 and the CSSP follows the IRP.

---

## Approval

**Approved By:** Pending. The ISSM reviews version 0.1, and the Configuration Control Board approves it in Phase 2.

**Circulated To:** the Platform Team, IT Operations, Fleet Operations, every team lead, the Security Team, the CSSP, and the alternate site's facility manager.

**Approval Date:** Pending.

---

## Periodic Review and Revision

**Review Cadence:** Annually, as a floor, and after every exercise.

**Revision Triggers:**
- A change to the organization, the systems the plan covers, or where they run
- The business impact analysis completing in Phase 2, or changing after it
- The fleet's arrival in Phase 3
- A problem found while running or testing the plan
- A restore test, failover, or exercise showing an objective, a site, or a procedure no longer matches what KESTREL can do
- A change to someone on the roster
- A change to a governing requirement
- A product substitution recorded in the Security Implementation Plan, for any product this document names
