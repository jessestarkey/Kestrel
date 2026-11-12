# KESTREL Security Implementation Plan

> **Notional system.** KESTREL is fictional. The names, dates, budgets, and decisions below are invented to show a Security Implementation Plan in progress. The products are real and are named only to show realistic choices, which implies no endorsement and no claim about any product's current authorization.

This plan carries KESTREL's SADD into RMF Step 3. It names the products that implement each SADD outcome, tailors each choice to where it runs, names the team that delivers it, and places it in a rollout sequence. Its records become the stories and tasks in KESTREL's issue tracker. It is split across files so each focus area can be read on its own. This file holds the document-wide sections, and each focus area's file holds its part of Section 4.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| SIP Version | 0.1 |
| Date | 2026-11-11 |
| Prepared By | KESTREL PMO ISSE, with the performer's team leads |
| Approving Authority | KESTREL program manager, who controls the program's engineering staff, contracts, and budget |
| Source SADD Version | 0.2, submitted for AO approval as 1.0 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-11 | KESTREL PMO ISSE | Initial draft against SADD 0.2 |

---

## 1. Purpose and Source

This plan carries KESTREL's SADD, version 0.2, into RMF Step 3. It records the products and services chosen for each of the SADD's {{NREC}} in-scope outcomes and the tailoring each choice needs across the cloud, the data center, the alternate site, and the fleet. It also names the team accountable for delivering each one and places it in a four-phase rollout built around KESTREL's funding, dependencies, and schedule. The SADD is still awaiting AO approval, so this plan is drafted against version 0.2 and is re-baselined when the SADD is approved as 1.0.

**Approving authority note:** the AO approves the SADD, but only the program manager commits the staff, contracts, and budget this plan assumes. The program manager therefore approves this plan.

**Platform choices.** KESTREL standardizes on Microsoft Azure Government at IL5 for the cloud, with US Gov Virginia as the primary region and US Gov Arizona for recovery. Active Directory in the mission data center remains the identity system of record, with Microsoft Entra ID as its cloud projection. A self-hosted Atlassian and GitLab stack inside Platform Prod holds the work itself. Jira tracks the work, GitLab holds source and runs the pipeline, and Confluence holds the governing plans and runbooks. A Palo Alto Networks rule base, managed once in Panorama, runs on both hubs and the alternate site. Splunk in the data center is the security monitoring platform.

**Authorization of each product.** Before any product is bought, Inherited Control Validation (`GV-5.12`) confirms its DoD authorization at the impact level it will run at. A product that fails that check is substituted, and the substitution is recorded in this plan and, if it changes a control's implementation, in the SSP and SCTM.

**Known product risk.** Atlassian has announced the end of its Data Center products. The Configuration Control Board re-evaluates the Jira, Jira Service Management, and Confluence choice by the end of Phase 3, while there is still time to migrate before support ends.

---

## 2. Rollout Phasing Strategy

The phases follow dependencies first. Identity, keys, the pipeline, and logging come before anything that relies on them, and detection comes after the telemetry it reads. Phases are set per activity, since the activities under one outcome often differ in urgency. An activity's SABER Maturity Level sets its default. Level 1, which the SABER marks as required for ATO, keeps its capability's place in the dependency sequence and must land by the end of Phase 3, when the ATO decision is due. Level 2 waits for Phase 2 at the earliest, and Level 3 waits for Phase 4. A pin moves an activity earlier only where KESTREL's design depends on it from the first build, or where building it in costs far less than retrofitting it, and each pin states its reason in its record. A record starts in the phase of its earliest activity and stays open until its last one lands, so one outcome remains one story.

An interim authorization to test (`GV-5.7`) covers Phases 1 to 3. Integration during those phases uses synthetic data, spare aircraft, and the simulator, so no live mission data or flight depends on a system that is not yet authorized.

{{PHASES}}

---

## 3. Implementation Record

Each record in Section 4 follows the template's record pattern. Every record cites its SADD outcome by ID rather than restating the design intent or control mapping, which stay in the SADD. Each record also carries a table giving every activity under its outcome its phase and the seven activity-level metadata fields. The metadata is carried unchanged from the SABER, and they are re-rated only where a product decision changes the effort, cost, or timing the SABER assumed.

Every record's status is Not Started, since the plan precedes Phase 1.

---

## 4. Implementation Records by Focus Area

{{STATUS}}

---

## 5. Issue Tracker Mapping

KESTREL's issue tracker is Jira Software Data Center in Platform Prod. GitLab merge requests link to their Jira issues through the GitLab integration, and Confluence holds the plans and runbooks the issues point to.

| SABER Level | Issue Tracker Level | Notes |
|---|---|---|
| Focus area | Initiative | One initiative per focus area, in Jira's plans hierarchy |
| Capability | Epic | The capability ID and title become the epic name |
| Outcome | Story | The outcome ID is the story's external ID field, and the story links to the SADD outcome. Its fix version is the phase of its earliest activity |
| Activity | Sub-task | The activity ID is the sub-task's external ID field, and its fix version is its own phase |

**Metadata field carry-over:** each of the seven activity-level fields in Section 4 becomes a Jira custom field on the sub-task, namely Control Type, Cross-Cutting Discipline, Maturity Model, ConMon Activity, Level of Effort, Cost, and Time Estimation. Each story and sub-task carries its phase as a Jira fix version, and each story carries its Accountable Team in the Jira team field, so the plan's sequence is the tracker's sequence. The import is generated from this plan's records, so no one transcribes it by hand.

---

## 6. Contracting and Procurement Cross-References

Each contract below groups the products bought under one vehicle. The Records column counts the Section 4 records that depend on it. Every contract draws from the Standard Security Clause Library (`GV-3.2.1`), and the four marked as needing a new clause must have that clause written before award.

{{CONTRACTS}}

**Government-furnished, so no contract is needed:** {{GOV}}.

**Open source, adopted through the ASP's approved component catalog:** {{OSS}}.

---

## Approval

**Approved By:** Pending. The KESTREL program manager approves this plan once the SADD is approved.

**Circulated To:** the performer's team leads, the contracting officer, the program's budget lead, the ISSM, and the CSSP for its containment role.

**Approval Date:** Pending.

**Published To:** Confluence, with the stories and sub-tasks imported into Jira.

---

## Periodic Review and Revision

**Review Cadence:** quarterly, by the PMO ISSE and the team leads, with each revision approved by the program manager.

**Revision Triggers:**
- A selected product is substituted, including after a failed authorization check
- A SADD revision adds or removes an outcome
- A dependency slips, or a phase's funding status changes
- The Atlassian Data Center decision is made

Where a substitution changes what a control's implementation actually is, not just which product provides it, the change also goes to the SSP and the SCTM.
