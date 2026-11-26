> **Notional system.** KESTREL is fictional. This page stands in for a Security Impact Analysis record in KESTREL's Jira Service Management, kept with the change record it analyzes. Its names and decisions are invented to show a completed record.

# SIA-2026-0001: Persistent Memory for the Coding Agent

> **Timing.** KESTREL's interim authorization to test is not yet granted. This record therefore analyzes the change against what the AO has approved so far, namely CCSD 1.0, and against the SADD as submitted. Sections 1 to 4 are complete. Section 5 waits for the change to be built in Phase 3.

## Record Control

| Field | Value |
|---|---|
| SIA Record ID | SIA-2026-0001 |
| Change Record ID | Commit 777de80 in the KESTREL repository, standing in for the GitLab merge request |
| Originating Change Process | Model or prompt change, under System Prompt Governance and agent configuration (`AI-8.10`) |
| Requested By | Engineering lead, as the coding agent's sponsor |
| Analyst | ISSM |
| Date Opened | 2026-11-26 |
| Status | Approved to implement, verification pending in Phase 3 |
| Classification / Handling | CUI |

---

## 1. Change Description and Classification

*Traces to GV-5.11.1.*

**What is changing, and why.** The coding agent gains persistent memory, so it can carry what it learns about a repository from one session to the next. Until now it kept nothing after a session ended. It will keep two kinds of notes:

- **Repository notes**, such as a repository's build steps and conventions, recalled by any session on that repository
- **User notes**, holding one developer's preferences, recalled only in that developer's sessions

A note is written only when a developer asks for one or approves one the agent proposes. Notes live in an Azure AI Search index in Platform Prod, which only the OpenHands server's identity can reach. They expire after 180 days unless a developer confirms them again. The mission-planning agent stays stateless, since its drafts reach a station.

**Standard change.** No. Agent memory is a new capability, not a change inside an approved baseline.

| Touches | Yes / No | Which |
|---|---|---|
| Components | Yes | A new Azure AI Search index in Platform Prod. New OPA policy and LLM Guard screening on the coding agent's memory path. |
| Authorization boundary | No | Everything stays inside Platform Prod |
| Interconnections | No | None added or changed |
| Information types | Yes | No new type. Content from source code (CCSD row 9) and developer identity (row 15) is now also held in the memory index. |
| Control implementations | Yes | AC-3, SI-7(1), and SI-12 gain implementations through AI-8.15. SC-28, AU-12, and CM-8 extend to the new index. |

**Asset-level analysis received.** The AI/ML Governance Review Board's design review keeps the coding agent at the Moderate tier and AL 2, as the charter and the AISP record. The board reviews it again before the agent is fielded. Model Deployment Risk Threshold Evaluation (`AI-6.5`) tests the deployed configuration then.

---

## 2. Security and Privacy Impact Determination

*Traces to GV-5.11.2.*

| Authorization Element | Impact | Determination and Rationale |
|---|---|---|
| Boundary | None | The index sits in Platform Prod, behind the same hub, with no new path in or out |
| Interconnections | None | Nothing outside the boundary reaches the index or the notes |
| Information types | None | No type is added. Row 9 and row 15 content is held in one more place, at the same impact levels, so the CCSD's ratings still hold. |
| Categorization | None | Rows 9 and 15 keep their ratings, and no row's rating moves |
| Control implementations | Strengthened | AC-3: scopes per repository and per user, with nothing shared across teams. SI-7(1): a keyed hash checked on every recall. SI-12: entries expire after 180 days. SC-28: the index uses customer-managed keys. AU-12: every write and every blocked write is logged to Splunk. CM-8: the index joins the asset inventory. |
| Privacy | Touches PII | User notes carry the developer's identity and preferences. The record is referred to the privacy officer under CO-4.2.1 to screen whether the PIA needs reassessment. |

**Affected controls to verify after implementation (carried to Section 5):** AC-3, SI-7(1), SI-12, SC-28, AU-12, and CM-8.

**Analyst's conclusion.** The change adds a store and the controls around it, inside the existing boundary, holding information types the CCSD already rates. It weakens no control. The new risk is memory poisoning, which the write rules, screening, and alerting answer, and which AI Cyber T&E tests before fielding.

---

## 3. Emergency Change

Not applicable. This change went through normal review.

---

## 4. Significance Determination and Routing

*Traces to GV-5.11.3.*

**Significant:** No.

**Criterion met, or why none is met.** None of KESTREL's agreed reauthorization triggers under Ongoing Authorization (`GV-5.10`) applies.

- No new interconnection, partner nation, spoke, payload vendor, or foundation model
- No change to the CCSD's information types
- No activation of the alternate site
- No change to CCSD tailoring action 3 or 6

| Routing | Date | Decision / Reference |
|---|---|---|
| SCA review | Pending | The SCA sees this record with the SADD 0.9 review |
| AO decision | Not required | The change is not significant |
| Reported in Periodic Authorization Status Reporting (`GV-5.10.3`) | The first quarterly report after the interim authorization to test | Pending |

**Documentation updates required:**

| Artifact | Required? | Owner | Done |
|---|---|---|---|
| SADD, the AI-8.15 design intent | Yes | PMO ISSE | 2026-11-25, version 0.9 |
| Security Implementation Plan, the AI-8.15 record | Yes | PMO ISSE | 2026-11-25, version 0.7 |
| AI/ML Security Plan, Sections 3, 4, 8, and 9 | Yes | ML Team lead | 2026-11-25, version 0.2 |
| AI/ML Governance Charter, the inventory | Yes | PMO ISSE | 2026-11-25, version 0.2 |
| SSP, the AI-8.15 narrative | Yes | ISSM | When the SSP is drafted |
| SCTM | No | ISSM | AI-8.15's controls were already claimed, and the counts did not change |
| CCSD | No | PMO ISSE | No information type or rating changes |
| Authorization package | No | PMO ISSE | It is compiled later from the documents above |
| Interconnection agreement | No | PMO ISSE | No interconnection changes |
| PIA screening | Yes | Privacy officer | Pending |
| Review board's review before fielding | Yes | Chief engineer, as chair | Pending, in Phase 3 |

---

## 5. Post-Change Control Verification

*Traces to GV-5.11.4. Pending until the change is built in Phase 3.*

**Change implemented on:** Pending.

| Control ID | Implemented Correctly | Operating as Intended | Meeting Its Security and Privacy Requirements | Method / Evidence | Verified By / Date |
|---|---|---|---|---|---|
| AC-3 | Pending | Pending | Pending | Test: a session on one repository cannot recall another repository's notes, and one developer cannot recall another's | Pending |
| SI-7(1) | Pending | Pending | Pending | Test: an entry altered in the index is rejected on recall | Pending |
| SI-12 | Pending | Pending | Pending | Inspection: an entry past 180 days without confirmation is gone | Pending |
| SC-28 | Pending | Pending | Pending | CO-1.2 result: the index uses a customer-managed key | Pending |
| AU-12 | Pending | Pending | Pending | Test: a write the agent attempts from processed content is blocked and appears in Splunk | Pending |
| CM-8 | Pending | Pending | Pending | Inspection: the index is in Jira Service Management Assets with its owner | Pending |

**Failures:** None yet.

---

## Closure

**Closed By:** Pending, once Section 5 is complete.

**Retention:** Kept with its change record in Jira Service Management for the life of the system. The DMP sets that period for configuration records, CCSD row 11.
