> **Notional system.** KESTREL is fictional. This page stands in for a governing plan in KESTREL's self-hosted Confluence. Its names, retention periods, and decisions are invented to show a completed Data Management Plan.

# KESTREL Data Management Plan (DMP)

This plan sets what data KESTREL holds, how each kind is labeled and protected, who may reach it, and how long it is kept. It governs the data itself. The cryptography that protects it belongs to the [Key Management Plan](Key-Management-Plan) (KMP). This plan names which protection each label needs, and the KMP says how it is built. It carries out the design decisions in the [Data](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/07-data.md) section of the SADD. The [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/07-data.md) is the record of each product selection, and a substitution there revises this plan.

**NIST Control Mapping:** SI-12 (partial), SI-12(1) (partial), and SI-12(2) (partial), held through DA-1.9.

> **Phasing.** This plan is approved in late Phase 1, before prior collection arrives over F28. The attribute schema, retention schedule, and minimization rules apply from then. Provenance checks at use, threat detection, DLP, insider risk analytics, rights protection, and encryption by label start in Phase 2. Partner rights protection is set up as each partner onboards in Phase 3.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| DMP Version | 0.1 |
| Date | 2026-11-26 |
| Prepared By | Data Team lead, with the intelligence mission leads for retention and the privacy officer for personal information |
| Approved By | Configuration Control Board, chaired by the chief engineer |
| Source SADD Version | 0.9 |
| Source SIP Version | 0.7 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-26 | Data Team lead | Initial draft for Configuration Control Board review |

---

## Purpose and Scope

This DMP covers every kind of data inside KESTREL's boundary, as the CCSD's 18 information types list it. Data Discovery, Labeling, and Classification (`DA-1.1`) checks that list against what is actually stored. The privacy program governs who is accountable for personal information. This plan sets only the technical rules for it. The media marking and sanitization procedures sit with Media Protection, and this plan names which method each disposition uses.

---

## 1. Data Classification and Access Attributes

*Traces to DA-1.2.1.*

One policy, in the OPA policy decision service, decides data access from these attributes. No access policy may reference an attribute that is not listed here.

**Subject attributes.**

| Attribute | Values | Source |
|---|---|---|
| Team | Each KESTREL team, such as Mission Team 1, Mission Team 2, or the Data Team | Entra ID, from Active Directory groups |
| Role | Analyst, operator, engineer, administrator, or auditor | Entra ID, from Active Directory groups |
| Payload vendor rights | Vendor A, Vendor B, both, or none | The Data Team's catalog, from each person's signed vendor agreements |
| Partner nation | One partner nation, for a partner client only | The partner sponsorship record |

**Resource attributes.**

| Attribute | Values | Source |
|---|---|---|
| Information type | CCSD rows 1 to 18 | The label written at ingest |
| Owning team | The team whose zone holds the record | The label written at ingest |
| Payload vendor | Vendor A, Vendor B, or none | The label written at ingest |
| Releasability | Not releasable, or releasable to named nations | The foreign disclosure officer's approval |
| Provenance | Verified or unverified | The provenance ledger |

**Action attributes.** Read, write, export, release, and train.

**Environment attributes.** The spoke or host the request comes from, and whether it arrives from a KESTREL VDI pool.

**The payload vendor split.** Vendor A and Vendor B data are kept apart like compartments. A person, a workload, or a training run reaches vendor data only with matching vendor rights.

**Changing the schema.** A new attribute or value is a GitLab merge request to the policy repository. The Data Team lead and the Security Team approve it. The change must pass the fixed access cases (`DA-1.2.4`) before it deploys. A new attribute also goes to the Configuration Control Board.

---

## 2. Provenance and Anomaly Detection

*Traces to DA-1.3.3 and DA-1.4.2.*

**Provenance at each point of use, from Phase 2.** Every record's origin is in the provenance ledger from ingest. Where its record cannot be verified, each point of use either blocks it or flags it.

| Point of use | Unverified provenance | Why |
|---|---|---|
| Training snapshots | Blocks | Data of unknown origin must never train a model |
| Partner releases, through the partner API | Blocks | An unverified record must never reach a partner |
| The cross domain transfer to the IL6 enclave | Blocks | The enclave trusts what KESTREL sends |
| Federated updates from aircraft | Blocks | An unverified update could poison the aggregate |
| Analyst workbenches | Flags, and shows the record as unverified | Blocking live mission data would cost more than the risk |
| The report index for the LLM analyst assistant | Flags, and marks the content untrusted in the prompt | The assistant still needs recent reports |

**Anomalous access, from Phase 2.** Defender for SQL and Defender for Storage watch the cloud data services. Splunk Enterprise Security watches StorageGRID's audit logs and the report index's logs. The analytics alert on each of these:

- One identity reading more than ten times its usual daily volume from any zone
- An export from a zone outside the named release paths
- A role assignment or bucket policy change on a data store, outside the pipeline
- Access from a spoke, host, or identity that has never reached that zone before
- Any request that crosses the payload vendor split, even if it is denied

The CSSP triages each alert, and the zone's mission lead joins the investigation. The IRP sets when an alert becomes an incident.

---

## 3. Insider Risk Monitoring

*Traces to DA-1.5.2. From Phase 2.*

**Scope.** The PSO and program counsel set this scope with the Data Team. Monitoring covers only what users do on KESTREL systems.

- Data access and exports
- DLP events
- Privileged actions
- Sign-ins at unusual times or from unusual places

It never covers personal accounts, devices KESTREL does not own, or the content of a person's communications. All users are told of it in their access agreement.

**The record.** Splunk Enterprise Security keeps each user's risk score and the events behind it for one year. A record referred to the PSO is kept as the PSO's case requires.

**Who may see a score.** The Security Team lead, the ISSM, and the PSO. No manager sees a score unless the PSO decides to share it in a case.

---

## 4. Rights Management and Release Review

*Traces to DA-1.6.1 and DA-1.7.1.*

**Rights by document type.** Purview Information Protection, in KESTREL's Microsoft 365 DoD tenant, wraps documents that leave KESTREL.

| Document | Wrapped | Rights granted |
|---|---|---|
| Report released to a partner nation | Yes, limited to that nation | View, and print with a watermark. No copy, forward, or edit. Offline access for 7 days. Expires on the foreign disclosure officer's terms. |
| Machine-readable detections released to a partner | No. The partner's systems consume them under the release review and the memorandum of agreement. | Not applicable |
| Any document inside KESTREL | No. The access policy in Section 1 protects it. | Not applicable |

**Release datasets.** KESTREL releases no datasets outside the program today. Partner products and IL6 baselines are released under their own reviews. A first dataset release needs this plan revised first. It also needs the privacy officer's and the foreign disclosure officer's approval, and a re-identification test.

| Data in a future release | Technique | Utility floor |
|---|---|---|
| Identifying text | Removal and masking, with Presidio | Labels, times, and places kept |
| Imagery with people | Blurring or cropping people, with the person-detection model | Vehicles, equipment, and terrain left clear |

The privacy officer's approved techniques already apply to training and test data, as the AISP sets out.

---

## 5. Retention, Minimization, and Encryption Requirements

*Traces to DA-1.9.2, DA-1.9.3, and DA-2.1.1.*

**Retention and disposition.** The intelligence mission leads approve these periods for mission data, and the program manager for the rest. Where another plan sets the period, this table points to it, so the two cannot disagree. Object Lock holds each record until its period ends.

| Row | Data | Kept for | Disposition |
|---|---|---|---|
| 1 | Raw sensor collection | 5 years | Deleted with every version purged. Drives leaving service are sanitized under the SCRM plan. |
| 2 | Processed products and detections | 10 years | Deleted with every version purged |
| 3 | Analyst reports and corrections | The life of the system | Transferred under the program's records schedule |
| 4 | Released intelligence | The life of the system, for the release record | Wrapped partner copies expire on the foreign disclosure officer's terms |
| 5 | Collection requests and mission plans | 3 years | Deleted with every version purged |
| 6 | Command and control telemetry and flight logs | 3 years, or longer if a safety investigation holds them | Deleted with every version purged |
| 7 | Model training data | While any certified model traces to it, as the AISP sets | Deleted with every version purged |
| 8 | Trained models and lineage | As the AISP sets | As the AISP sets |
| 9 | Source code, infrastructure as code, and pipeline definitions | The life of the system | Archived with the repository |
| 10 | Signed releases and baselines | As the ASP's registry retention sets | Deleted from Artifactory and purged |
| 11 | Configuration baselines and infrastructure state | The life of the system | Archived with the repository |
| 12 | Credentials and security configuration | Until replaced or revoked, as the KMP sets | Destroyed as the KMP sets |
| 13 | Command link and root signing key material | As the KMP sets | Zeroized as the KMP sets |
| 14 | Security telemetry and audit records | 30 months, and 3 years for alert records, as the CMP sets | Deleted when the archive tier expires |
| 15 | User identity and authentication records | 3 years after the account is removed | Deleted with every version purged |
| 16 | Fleet and ground equipment maintenance records | The life of the aircraft or equipment, plus 3 years | Deleted with every version purged |
| 17 | Backup and archive copies | As the CP sets for each tier | The backup set's key is destroyed |
| 18 | Service desk records | 3 years after the ticket closes | Deleted with every version purged |

Incident evidence follows the IRP's retention terms. A litigation hold or an investigation suspends any disposition here.

**Minimization.** KESTREL collects and keeps only what its mission and its operation need.

- Mission data is collected only against approved collection requests.
- Incidental imagery of people is the only personal information in the collection. It is kept only where a detection task needs it.
- Test, training, and research data hold no identifying text, and no imagery of people unless the AISP's privacy requirements allow it.
- Identity and service desk records hold only the fields their process uses. KESTREL collects no Social Security numbers.

**Encryption by label, from Phase 2.** Every algorithm is AES-256, which CNSA 2.0 allows. The KMP sets the key ownership for each.

| Label | Granularity | Keys |
|---|---|---|
| Each team's or vendor's data lake zone | Object, under the zone's own key | Customer-supplied, from the nShield HSMs |
| Personal fields in KESTREL-built databases | Column | Customer-managed, in the spoke's Key Vault |
| The service desk database | Database, through transparent encryption | Customer-managed, since column encryption would break its queries |
| Every other store | Volume or service | Customer-managed, as the KMP's key ownership table sets |

Scans confirm each labeled record sits under the key its label requires (`DA-2.1.3`).

---

## Appendix: Reference Data

**DLP Rule Set and Exception Process** *(DA-1.5.1, from Phase 2)*: Data leaves KESTREL only by named paths, so the rules sit on each one. The rule set is held in GitLab and loaded by each enforcing product.

| Path | What a violation is | Action |
|---|---|---|
| The partner API | A record not releasable to the requesting nation | Blocked, and the foreign disclosure officer is told |
| The cross domain transfer gateway | A record outside the transfer's approved types | Blocked, and the Security Team is alerted |
| GitLab pushes | Mission data or a secret in a push | Blocked before it reaches a branch performer laptops can clone |
| VDI desktops | A download or clipboard copy out of the desktop | Blocked |
| Bulk reads across zones | Reads outside a team's usual pattern | Alerted in Splunk Enterprise Security |

An exception is requested in Jira with the reason. The zone's data owner and the Security Team approve it, and it expires after 30 days.

---

## Approval

**Approved By:** Pending. The intelligence mission leads approve the retention periods for their data, and the privacy officer approves the handling of personal information. The Configuration Control Board then approves version 0.1 in late Phase 1.

**Circulated To:** the Data Team, the mission teams, the ML Team, the Platform Team, the Security Team, the privacy officer, the foreign disclosure officer, and the PSO.

**Approval Date:** Pending.

---

## Periodic Review and Revision

**Review Cadence:** Annually, as a floor.

**Revision Triggers:**
- A new payload vendor, data source, or information type
- A first dataset release outside the program
- A change to the DLP, rights protection, or discovery tools
- A change to a records schedule or other governing requirement
- A finding that a retention period, a technique, or a minimization rule no longer matches what KESTREL holds
- A product substitution recorded in the Security Implementation Plan, for any product this document names
