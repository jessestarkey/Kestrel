# KESTREL Categorization and Control Selection Document (CCSD)

> **Notional system.** KESTREL is fictional. The names, dates, and decisions below are invented to show a completed CCSD, and nothing here describes a real program or a real authorization.

This document is KESTREL's RMF Step 2 (Select), built from the SABER's CCSD template and its owning outcome, Categorization and Control Selection Document (CCSD) (`GV-5.4`). It lists the information KESTREL handles, assigns each type a provisional impact value, and proposes the control selection and tailoring that follow. The PMO ISSE drafted it, the SCA reviewed it, and the AO approved version 1.0. The SADD is built against that approved version.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| CCSD Version | 1.1 (draft, in SCA review). Version 1.0 is the approved version. |
| Date | 2026-11-11 |
| Prepared By | KESTREL PMO ISSE |
| Reviewed By | Security Control Assessor (SCA) |
| Approved By | KESTREL Authorizing Official (AO) |
| Authorization Framework | DoD RMF (DoDI 8510.01) |
| Cloud Impact Level (DoD Cloud Computing SRG) | IL5 |
| Classification / Handling | CUI. Together, the inventory below shows what KESTREL collects and how it processes it, so the whole document is handled as CUI even where a single entry would not need to be. |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-08-14 | KESTREL PMO ISSE | Initial draft for SCA review |
| 0.2 | 2026-09-11 | KESTREL PMO ISSE | Dispositioned SCA comments and added the OT overlay |
| 1.0 | 2026-10-02 | KESTREL PMO ISSE | Approved by the AO, with tailoring action 3 modified |
| 1.1 | 2026-11-11 | KESTREL PMO ISSE | Added the performer interconnection, recorded source code held on performer laptops, moved the foundation model inside the boundary as a cloud-hosted service, recorded each mission team's ownership of its payload vendor's collection, added service desk records as row 18, added the alternate site to the boundary, gave the CSSP pre-approved containment playbooks, and proposed tailoring action 6 for break-glass authentication, for SCA review |

---

## Purpose and Scope

This CCSD lists the information types KESTREL processes, stores, and transmits, and assigns each a provisional impact value. It also proposes the control selection and tailoring that follow from them, for SCA review and AO approval. It covers the one KESTREL authorization boundary: the IL5 cloud's hub and ten spokes, the on-premises mission data center and its alternate site, and the UAS fleet. The IL6 classified enclave that KESTREL exchanges data with is a separate system with its own CCSD, and this document covers only what crosses into or out of KESTREL. It is submitted to the KESTREL AO under DoD RMF.

---

## 1. System Summary

KESTREL is an ISR analytics platform. Twelve unmanned aircraft collect sensor data and run onboard detection models. An IL5 cloud and on-premises backend retrains those models and serves the results to about 300 analysts, the UAS operators, and coalition partners from five nations. The full description, including components, data flows, and users, is in the [system description](01-system-description.md), which serves as the draft of SSP Section 2.

Information enters or leaves the boundary through seven interconnections, each a likely source of an information type:

- **The UAS fleet's RF datalinks** bring in sensor recordings, telemetry, and federated model updates, and carry flight commands out.
- **The partner API** releases detections and reports to coalition partner systems.
- **The Boundary Cloud Access Point** carries every analyst and partner session into the DMZ.
- **The cyber defense service provider** receives security telemetry and incident reports, and its analysts run pre-approved containment playbooks through their host pool.
- **The enterprise cross domain solution** carries baselines low to high into the IL6 enclave, and released analyst reports and model corrections high to low out of it.
- **DoD PKI and External Certificate Authorities** supply the trust anchors for user and partner credentials.
- **The performer's enterprise network and laptops** carry source code to and from the development environment, and display-only administration sessions into the admin VDI pool.

---

## 2. Information Type Inventory

*Traces to `GV-5.4.1`.*

KESTREL's mission types come from the Defense and National Security (D.1) and Intelligence Operations (D.3) areas of NIST SP 800-60 Vol. 2 Rev. 1. SP 800-60 names these types but gives no provisional values for them, since it leaves national security systems to the agency that operates them. KESTREL is a national security system because it involves intelligence activities and the command and control of military aircraft. Its mission values are therefore set by the program and justified one at a time in Section 3. The support types map to SP 800-60 types that do carry recommended values.

KESTREL transits no information on behalf of another party. Every type it carries is either its own or is released to a party under an agreement.

| # | Information Type | NIST SP 800-60 / CNSSI 1253 Identifier | Source | Owner | Where Held Inside the Boundary | Notes |
|---|---|---|---|---|---|---|
| 1 | Raw sensor collection | D.3, Intelligence Collection | Aircraft sensor payloads, over the datalinks | KESTREL mission owner, with Mission Team 1 holding EO/IR and Mission Team 2 holding RF collection | Aircraft storage, ground control stations, each mission team's data lake zone, backup and archive | Includes incidental imagery of people, the program's only PII outside its user records. Each payload vendor's data rights confine its raw collection to its own team's zone |
| 2 | Processed sensor products and detections | D.3, Intelligence Processing | Onboard and cloud detection models | KESTREL mission owner | Mission data lake, detection model serving, analyst portal | |
| 3 | Analyst reports and corrections | D.3, Intelligence Analysis and Production | Analysts, and released products from the IL6 enclave through the cross domain solution | KESTREL mission owner | Mission data lake, mission report index, feedback endpoints | Report excerpts also travel in prompts to the foundation model the cloud provider hosts inside the boundary, with provider-side prompt logging disabled |
| 4 | Released intelligence to partners | D.3, Intelligence Dissemination | Analysts, through the partner API | KESTREL mission owner, with foreign disclosure approval | Partner API, mission data lake | Only products approved for release to each partner nation |
| 5 | Collection requests and mission plans | D.3, Intelligence Planning | Analysts, operators, and the mission-planning agent | KESTREL operations lead | Mission-planning agent, mission data lake | Agent drafts take effect only after an operator approves them |
| 6 | UAS command and control | D.1, Operational Defense | Ground control stations | KESTREL operations lead | Ground control stations, aircraft, command and payload datalinks | Flight commands, telemetry, and loaded flight plans |
| 7 | Model training data | D.20.1, Research and Development (closest match) | Mission data lake, analyst corrections, federated updates from the aircraft | KESTREL AI lead | Mission data lake, training cluster, federated learning aggregator | No catalog type covers training corpora, so the closest type is used and its values are raised in Section 3. It never leaves the boundary, since data scientists work only inside the experimentation workspaces |
| 8 | Trained models and model lineage | C.3.5.1, System Development (closest match) | Training cluster | KESTREL AI lead | Artifact and model registry, detection model serving, aircraft | Includes the edge models loaded onto the aircraft and the models sent to the IL6 enclave |
| 9 | Source code, infrastructure as code, and pipeline definitions | C.3.5.1, System Development | Developers and ML engineers | KESTREL engineering lead | Source repository and CI/CD pipeline | Developers also keep clones on performer laptops outside the boundary, protected under the performer's CMMC Level 2 controls and the interconnection agreement |
| 10 | Signed releases and baselines | C.3.5.2, Lifecycle/Change Management | CI/CD pipeline | KESTREL engineering lead | Artifact and model registry, every prod spoke, ground control stations | Includes the periodic baselines sent low to high to the IL6 enclave |
| 11 | Configuration baselines and infrastructure state | C.3.5.4, IT Infrastructure Maintenance | Platform administrators and the pipeline | KESTREL engineering lead | Source repository, cloud control planes, data center management systems | |
| 12 | Credentials and security configuration | C.3.5.5, Information Security | Identity provider, privileged access platform, secrets vaults | KESTREL ISSM | Secrets vaults, privileged access platform, identity provider | User, workload, and pipeline credentials and the security settings that govern them |
| 13 | Command link and root signing key material | C.3.5.5, Information Security | PKI and HSMs | KESTREL ISSM | HSMs, and the datalink crypto modules in the aircraft and ground control stations | Generated in the HSMs and loaded into the datalink modules with a key loader. It never enters the IL5 cloud. |
| 14 | Security telemetry and audit records | C.3.5.8, System and Network Monitoring | Every KESTREL segment | KESTREL ISSM | Security monitoring platform, backup and archive | Also sent to the cyber defense service provider, whose analysts also read it in place through the CSSP host pool |
| 15 | User identity and authentication records | C.2.8.9, Personal Identity and Authentication | Users and DoD PKI or External Certificate Authority credentials | KESTREL ISSM | Identity provider and directory | |
| 16 | Fleet and ground equipment maintenance records | C.3.1.1, Facilities, Fleet, and Equipment Management | OT maintainers and vendor support | KESTREL operations lead | Mission data center, ground control stations | |
| 17 | Backup and archive copies | C.3.5.6, Record Retention | Mission data lake, registries, and configuration | KESTREL ISSM | Backup and archive | Held under retention lock and a longer retention rule than the live copies |
| 18 | Service desk records | C.3.1.2, Help Desk Services | Users, IT Operations, and the Security Team | KESTREL IT Operations lead | Service desk platform | Tickets, access requests and approvals, and change records |

The Data focus area's Data Discovery, Labeling, and Classification (`DA-1.1`) checks this list against what is actually stored. A discovery result with no row here is a finding against this document.

---

## 3. Provisional Impact Values

*Traces to `GV-5.4.2`.*

Values follow the FIPS 199 levels as qualified by CNSSI 1253. The mission types have no catalog value, so their rationale explains each value in full. Every other row gives the catalog value and a reason for any departure from it.

| # | Information Type | Confidentiality | Integrity | Availability | Catalog Recommended (C/I/A) | Rationale for Any Departure |
|---|---|---|---|---|---|---|
| 1 | Raw sensor collection | Moderate | Moderate | Moderate | None (D.3) | Disclosure would reveal where KESTREL collects and what its sensors can see. Raw collection lost after a mission cannot be collected again, so availability is Moderate rather than Low. |
| 2 | Processed sensor products and detections | Moderate | Moderate | Moderate | None (D.3) | Corrupted detections mislead analysts, but analysts review every detection before it becomes a report, which keeps integrity at Moderate. |
| 3 | Analyst reports and corrections | Moderate | Moderate | Moderate | None (D.3) | Corrections feed retraining, so integrity matters, but Certification to Field tests every retrained model before release. |
| 4 | Released intelligence to partners | Moderate | Moderate | Moderate | None (D.3) | Release to the wrong partner is a foreign disclosure violation, which the release approval controls rather than the impact level. |
| 5 | Collection requests and mission plans | Moderate | Moderate | Low | None (D.3) | A plan that is late delays a collection but does not endanger an aircraft, since an operator approves every plan before it flies. |
| 6 | UAS command and control | Moderate | **High** | Moderate | None (D.1) | A forged or altered command can cost an aircraft or put it where it must not fly, so integrity is High. Availability stays Moderate because each aircraft runs a lost-link procedure that returns it safely without a command link. |
| 7 | Model training data | Moderate | Moderate | Low | L/M/L | Confidentiality is raised to Moderate because the data is mission collection under another name. Poisoned data is caught at the certification gate, so integrity stays at the catalog value. |
| 8 | Trained models and model lineage | Moderate | **High** | Low | L/M/L | Confidentiality is raised because a model reveals what KESTREL looks for. Integrity is High because an altered edge model runs on the aircraft, past every gate. |
| 9 | Source code, infrastructure as code, and pipeline definitions | Moderate | Moderate | Low | L/M/L | Confidentiality is raised because the code reveals the capability and its defenses. |
| 10 | Signed releases and baselines | Moderate | **High** | Low | L/M/L | A tampered release reaches production, the aircraft, and the IL6 enclave together, so integrity is High. |
| 11 | Configuration baselines and infrastructure state | Moderate | Moderate | Low | L/L/L | Configuration shows how every boundary is defended, which raises confidentiality. An altered baseline weakens every component built from it, which raises integrity. |
| 12 | Credentials and security configuration | Moderate | Moderate | Low | L/M/L | Disclosed credentials open Moderate data, so confidentiality is raised to match. |
| 13 | Command link and root signing key material | **High** | **High** | Moderate | L/M/L | A disclosed datalink key lets an adversary send authenticated commands to an aircraft, and a disclosed signing key lets one sign a malicious model or flight software package every aircraft will accept. Either can cost an aircraft or misdirect a mission, which is severe harm, so confidentiality and integrity are High. Losing the keys outright grounds the fleet until it is re-keyed, which raises availability to Moderate. |
| 14 | Security telemetry and audit records | Moderate | Moderate | Low | M/M/L | Matches catalog. |
| 15 | User identity and authentication records | Moderate | Moderate | Moderate | M/M/M | Matches catalog. |
| 16 | Fleet and ground equipment maintenance records | Moderate | Moderate | Low | L/L/L | Together, the records show how many aircraft can fly, which raises confidentiality. A false record can return an unready aircraft to flight, which raises integrity. |
| 17 | Backup and archive copies | Moderate | Moderate | Moderate | L/L/L | The copies hold rows 1 to 12 but never the row 13 keys, which stay in the HSMs, so confidentiality follows rows 1 to 12. The contingency plan's recovery objectives depend on the copies being intact and reachable, which raises integrity and availability. |
| 18 | Service desk records | Moderate | Moderate | Low | L/L/L | Tickets describe incidents and vulnerabilities, which raises confidentiality. Access approvals recorded here drive provisioning, so an altered record could grant access, which raises integrity. |

---

## 4. System-Level Categorization (carried in)

> Carried in from Security Categorization (`GV-5.5.1`). The SSP records it with the AO's concurrence (`GV-5.5.2`), and the SSP is the record if the two ever disagree.

| Objective | System Impact Level | Basis |
|---|---|---|
| Confidentiality | High | High-water mark, set by row 13 alone |
| Integrity | High | High-water mark, set by rows 6, 8, 10, and 13 |
| Availability | Moderate | High-water mark of rows 1 to 18 |

**AO concurrence:** 2026-08-28, KESTREL AO memorandum concurring in the categorization.

KESTREL's High confidentiality comes from one narrow type, the key material in row 13, while every other type is Moderate or below. That key material lives only in the HSMs and the datalink crypto modules, so the SADD can concentrate the High confidentiality controls there. Availability stays at Moderate, and a program that collapsed the three objectives into one High baseline would carry High availability controls that no information type here calls for.

---

## 5. Baseline Selection

*Traces to `GV-5.4.4`.*

KESTREL is a national security system, so its controls are selected per objective under CNSSI 1253 rather than from one collapsed baseline. The selection draws on the CNSSI 1253 baseline columns for High confidentiality, High integrity, and Moderate availability. The control identifiers below are NIST SP 800-53 Rev 5. The Rev 4 to Rev 5 reconciliation lives in the program's requirements traceability artifact.

---

## 6. Overlays and Cloud Impact-Level Requirements

*Traces to `GV-5.4.4`.*

| Overlay or Requirement Set | Applies? | Notes |
|---|---|---|
| Classified Information Overlay | No | KESTREL holds no classified information. The IL6 enclave applies it under its own CCSD. |
| SAP Overlay(s) | No | KESTREL is not a special access program. |
| Intelligence Community (IC) Overlay | No | KESTREL is a DoD system under a DoD AO, not a system of an IC element. Revisit if an IC customer's data enters the boundary. |
| Privacy Overlay (Low / Moderate / High) | Yes, Low | The only PII outside user records is incidental imagery of people in raw collection. KESTREL never indexes or retrieves it by person, which keeps the tier at Low. |
| Space Platform Overlay | No | The aircraft are not space platforms. |
| Cross Domain Solution (CDS) Overlay | No | The overlay applies to the cross domain solution itself, which the enterprise provider owns and authorizes. KESTREL's side of the connection falls under Cross Domain Solution (CDS) Transfer Procedures (`NE-2.10`) and the interconnection agreement. |
| Cloud Computing Overlay | Yes | Applies to every IL5 spoke and the cloud hub. |
| DoD Cloud Computing SRG Impact-Level Requirements | IL5 | Adds separation from non-DoD tenants, connection through the Boundary Cloud Access Point, cyber defense service provider alignment, and data location in the United States. KESTREL's High integrity is why its cloud provider holds an IL5 provisional authorization built on a High baseline, so the provider's integrity controls can be inherited. The one High confidentiality type, the row 13 key material, is held on premises and in the fleet, never in the IL5 cloud, so no cloud-hosted type exceeds Moderate confidentiality. |
| NIST SP 800-82 Rev. 3 OT Overlay | Yes | Applies to the UAS fleet, whose aircraft, ground control stations, and launch equipment are OT. It adds safety-driven guidance to controls such as AC-11 and SI-2, which Section 7 relies on. |
| DoD AI Cybersecurity Risk Management Tailoring Guide | Yes, as tailoring guidance | Applies to the detection models, the LLM analyst assistant, and the mission-planning agent. It informs tailoring rather than adding a control set of its own. |

---

## 7. Tailoring Actions

*Traces to `GV-5.4.4`.*

| # | Control / Enhancement (Rev 5) | Action | Rationale | SABER Outcomes Affected | SCA Comment | AO Decision |
|---|---|---|---|---|---|---|
| 1 | SI-8 | Removed | KESTREL runs no email service. Analysts use the parent organization's enterprise email, which sits outside the boundary and carries its own SI-8 implementation. | `NE-3.6` drops out of the SADD | Concur. Confirm in the SSP that no KESTREL component sends or receives mail. | Approved |
| 2 | AC-11 | Scoped | Session lock does not apply to ground control stations while an aircraft is airborne, because a locked station during flight is a safety hazard. Operators stay at the station, and the station sits in a controlled operating area. AC-11 still applies to every other KESTREL device and to the stations on the ground. | `ID-2.6` (Device Lock, `ID-2.6.7`) | Concur, with the physical control documented in the SSP as the compensating measure. | Approved |
| 3 | SI-2 | Compensating control | The payload processing workstation runs an operating system its vendor no longer patches, and Payload Vendor A certifies its conversion software only on that system. It runs isolated in the OT zone with application allow-listing, and reaches the data lake through a single firewalled conduit. | `DI-4.8`, `DI-3.5` (Compensating Control Baseline Definition, `DI-3.5.2`) | Concur, but the measure has no end date. | Modified: approved until the replacement workstation fields, and no later than 2027-09-30 |
| 4 | SR-11(3) | Added | Ground control stations and aircraft avionics include parts bought through vendor service channels. A periodic rescan for counterfeit components covers parts that enter after initial receipt. The enhancement is in no NIST baseline. | `GV-3.4` | Concur. | Approved |
| 5 | SA-9(5) | Added | The SRG's IL5 requirements and the hosted model service's terms both turn on where data is processed. Selecting the control makes the location a recorded parameter, namely United States regions within the cloud provider's IL5 authorization. Version 1.1 narrows the parameter to that one provider, since the foundation model is now one of its hosted services. | `AP-2.9`, `AI-8.3` | Concur. | Approved |
| 6 | IA-2(1) | Compensating control | The directory and ground segment break-glass accounts use console-only passwords rather than a second factor, because their recovery cannot depend on the PKI or the directory they may be recovering. Logon is restricted to named consoles, each password is split between two custodians and sealed, any use alerts the Security Team and the CSSP, sessions end automatically after four hours, and the password is rotated after every use. Every other privileged account keeps phishing-resistant MFA, and the two cloud break-glass accounts use two different phishing-resistant methods. | `ID-4.6` (Emergency Account Authentication Protections, `ID-4.6.2`) | Pending SCA review of version 1.1 | Pending, with an annual review proposed |

**Organization-defined parameters:** recorded in the parameter table kept with the SCTM. The parameters this CCSD sets directly are the SA-9(5) location above and the AC-11 exception window, namely while an aircraft under that station's control is airborne.

---

## 8. Approved Control Set

The AO approved the selection on 2026-10-02 as version 1.0. The approved set is the CNSSI 1253 selection from Section 5, plus the overlays in Section 6, as modified by the five actions in Section 7. Two actions added controls, one removed a control, and two kept a control while changing how it applies. The Security Controls Traceability Matrix (`GV-5.9.1`) records each approved control with its inherited, shared, or program-owned designation, and the SADD is built against this set.

This notional example does not reproduce the per-family control counts a real CCSD would state here.

---

## Review and Approval

**Drafted By:** KESTREL PMO ISSE, 2026-08-14

**SCA Review:** Security Control Assessor, 2026-09-04, with comments dispositioned in Section 7

**AO Approval:** KESTREL Authorizing Official, 2026-10-02, approved version 1.0

**Version 1.1:** drafted 2026-11-11 for the new performer interconnection and the retired foundation model vendor interconnection, both revision triggers under Periodic Review and Revision. It changes no impact value and no control selection, and it awaits SCA review and AO approval.

---

## Periodic Review and Revision

> Per CCSD Periodic Update (`GV-5.4.3`).

**Review Cadence:** Change triggers review rather than a calendar.

**Revision Triggers (event-driven):**

- A new data source, mission, interconnection, or user population, such as a new coalition partner, a new sensor payload, or a new feed into the training data
- An information type retired
- A Security Impact Analysis record (`GV-5.11.3`) that flags a CCSD update
- A change to the overlays or IL5 requirements in Section 6
- Fielding of the replacement payload processing workstation, which closes tailoring action 3

An update that moves a provisional value goes to Security Categorization (`GV-5.5.3`) for reassessment before Section 4 changes. A revised control selection goes back through SCA review and AO approval before the SADD is revised against it.
