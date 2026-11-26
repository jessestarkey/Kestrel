> **Notional system.** KESTREL is fictional. This page stands in for a governing document in KESTREL's self-hosted Confluence. Its names and decisions are invented to show a completed Privacy Program Charter and Policy.

# KESTREL Privacy Program Charter and Policy

This charter establishes KESTREL's privacy program and states its privacy policy. It covers what personal information KESTREL holds, why, how long, who answers for it, and how a person can have it corrected. The program runs under DoDI 5400.11 and the DoD component privacy program. KESTREL inherits from the component the parts a single system cannot run, such as the system of records notices and breach reporting to OMB. It carries out the design decisions in the [Compliance](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/13-compliance.md) section of the SADD.

**NIST Control Mapping:** PT-1 (full), PM-18 (full), PM-19 (full), PM-5(1) (full), AT-3(5) (full), and PM-22 (full), held through CO-4.1.

> **Phasing.** The Privacy Impact Assessment is approved in Phase 1, before any personal information arrives. This charter is approved in Phase 2. Until then, the PIA and the DMP's minimization and retention rules govern how personal information is handled.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| Charter Version | 0.1 |
| Date | 2026-11-26 |
| Prepared By | Privacy officer, with program legal counsel and the intelligence mission leads |
| Approved By | Configuration Control Board, chaired by the chief engineer, with the program manager as the official accountable for KESTREL's privacy risk |
| Source SADD Version | 0.9 |
| Source SIP Version | 0.8 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-26 | Privacy officer | Initial draft for review |

---

## Purpose and Scope

This charter covers every collection, use, retention, disclosure, and disposal of personal information inside KESTREL's boundary. It applies to every team and every person with a KESTREL account. KESTREL holds little personal information, and none of it is the purpose of the mission, so the program is set at the Privacy Overlay's Low tier. The technical rules for classifying, minimizing, encrypting, and retaining data belong to the Data Management Plan (DMP), and this charter does not restate them. The AI/ML Governance Charter's responsible AI policy builds on this charter for what AI adds.

---

## 1. Privacy Policy and Program Charter

*Traces to CO-4.1.1.*

**The charter.** The program office establishes KESTREL's privacy program, with the privacy officer as its lead. The program answers to these requirements:

- The Privacy Act of 1974
- DoDI 5400.11 and DoD 5400.11-R
- Section 208 of the E-Government Act of 2002, for the Privacy Impact Assessment
- OMB Circular A-130, and OMB M-17-12 for breach response
- The CNSSI 1253 Privacy Overlay, at the Low tier the CCSD sets
- DoD Manual 5240.01, for intelligence oversight of any information about U.S. persons

**What KESTREL holds.** KESTREL holds five kinds of personal information, and no others.

| Information | Why KESTREL holds it | Retrieved by a personal identifier | How long, per the DMP |
|---|---|---|---|
| User account records | To create and manage each person's account | Yes | 3 years after the account is removed |
| Partner credential records | To admit partner and vendor users under their sponsors | Yes | 3 years after the account is removed |
| Service desk records | To support users | Yes | 3 years after the ticket closes |
| User identifiers in security telemetry | To attribute actions for security monitoring | Yes, for investigation | 30 months for logs, and 3 years for alert records |
| Incidental imagery of people | It appears in raw sensor collection, and KESTREL does not seek it | No | 5 years, with raw collection |

**The policy.**

- **Collection.** KESTREL collects personal information only for the purposes in the table above. It collects no Social Security numbers, and accounts key on the CAC DoD ID number. It never collects information about how anyone exercises their First Amendment rights.
- **Use.** Personal information is used only for the purpose it was collected for. No model is trained to identify, track, or re-identify individuals. Lifting that bar would need the AI/ML Governance Review Board, a revised PIA, and a CCSD revision.
- **Imagery of people.** Imagery is never indexed or retrieved by person, so it forms no system of records. It is kept in training data only where a detection task needs it, and the privacy officer approves each new training set's handling. People are blurred or cropped before imagery reaches dev/test data or a partner release.
- **Notice.** The account request form carries a Privacy Act statement.
- **Disclosure.** Records retrieved by identifier are disclosed only under the routine uses of the DoD-wide system of records notice the component privacy office names. No partner release includes personal information.
- **Retention and disposal.** Each kind is kept for the period the DMP sets, then disposed of by the DMP's method.
- **Breaches.** A breach of personal information is an incident under the IRP. The privacy officer reports it through the component privacy office.

**Procedures.** The procedures that carry out this policy sit beside it rather than following later.

| Step | Procedure |
|---|---|
| Assessing new processing | The Privacy Impact Assessment, on DD Form 2930, is approved in Phase 1. A new collection, sensor, AI use case, or partner release triggers a reassessment, and so does any change that would retrieve imagery by person. |
| Minimizing | The DMP's minimization rules apply. Presidio removes identifying text from training records, and from inference logs before they are kept. |
| Screening changes | Security Impact Analysis refers any change touching personal information to the privacy officer, who decides whether the PIA needs reassessment. |
| Correcting | Section 3 sets out the correction process. |
| Training | Section 2 names who takes role-based privacy training. |

**The inventory.** The privacy officer keeps a standing inventory of every system and store that processes personal information. Each one is tagged in Jira Service Management Assets, and the PIA's intake adds a system when it starts processing personal information. The inventory names each system's data steward and the downstream systems that receive its records. It is living data in Assets, not a list in this charter.

---

## 2. Privacy Roles and Responsibilities

*Traces to CO-4.1.2.*

**The privacy officer.** The privacy officer, in the program office, is accountable for KESTREL's privacy program. This is a named role with authority, not a duty added to another job. The privacy officer approves the PIA with the component privacy office, approves each training set's handling, decides PIA referrals, adjudicates disputed corrections, and reports breaches. The privacy officer reports to the program manager, who is accountable for KESTREL's privacy risk. Program legal counsel advises on each.

**Data stewards.** Each system that processes personal information has a named steward.

| Information | Steward |
|---|---|
| User account records | IT Operations lead |
| Partner credential records | IT Operations lead, with each partner's KESTREL sponsor |
| Service desk records | IT Operations lead |
| User identifiers in security telemetry | Security Team lead |
| Incidental imagery of people | Data Team lead, with the intelligence mission leads for their zones |

**Who needs privacy training.** Every user takes DoD CUI and privacy awareness training on JKO before their account is created and each year after. These roles also take role-based privacy training, scoped to what they handle:

- Analysts who handle raw imagery
- Data Team stewards and annotators
- Service desk staff
- Security Team analysts who investigate user activity

---

## 3. PII Accuracy and Correction Request Handling

*Traces to CO-4.1.3.*

**Making a request.** A person who believes KESTREL holds inaccurate information about them asks through Jira Service Management, or through their data steward. The request is acknowledged within 10 working days, as the Privacy Act requires.

**Where a correction is made.** KESTREL corrects the attributes it holds itself, such as a user's team, role, or contact details. CAC attributes are corrected at their source in DoD's records, and partner attributes by the partner's sponsor. In those cases, the steward tells the person where to go, and KESTREL takes the corrected value at its next synchronization.

**Spreading the correction.** An approved correction is made in the authoritative record, Active Directory for account attributes. The steward then confirms it reached every downstream system the inventory lists, such as Entra ID, CyberArk, and the service desk.

**Disputes.** A correction the steward declines, or one that reaches a system outside the steward's authority, goes to the privacy officer to decide. The person is told the outcome and, if declined, the reason.

**The record.** Every request is logged in Jira Service Management with its disposition, including declined requests. The privacy officer reviews the log each year, which shows that requests are actually reviewed rather than granted by default.

---

## Approval

This charter is approved, versioned, and republished through the governance program's policy lifecycle, like every other program policy.

**Approved By:** Pending. Program legal counsel and the component privacy office review version 0.1, and the Configuration Control Board approves it in Phase 2.

**Circulated To:** the data stewards, the intelligence mission leads, the Data Team, IT Operations, the Security Team, the ML Team, and the component privacy office.

**Approval Date:** Pending.

---

## Periodic Review and Revision

**Review Cadence:** Annually, as a floor.

**Revision Triggers:**
- A change in what KESTREL collects, such as a new sensor or a new kind of record
- A change in the authority KESTREL collects under
- A PIA reassessment showing that a system's processing has outgrown its last assessment
- Any proposal to retrieve imagery by person, or to train a model to identify individuals
- A change to a governing statutory, regulatory, or contractual requirement
- A product substitution recorded in the Security Implementation Plan, for any product this document names
