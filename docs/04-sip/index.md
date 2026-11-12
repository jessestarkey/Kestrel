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

This plan carries KESTREL's SADD, version 0.2, into RMF Step 3. It records the products and services chosen for each of the SADD's 363 in-scope outcomes and the tailoring each choice needs across the cloud, the data center, the alternate site, and the fleet. It also names the team accountable for delivering each one and places it in a four-phase rollout built around KESTREL's funding, dependencies, and schedule. The SADD is still awaiting AO approval, so this plan is drafted against version 0.2 and is re-baselined when the SADD is approved as 1.0.

**Approving authority note:** the AO approves the SADD, but only the program manager commits the staff, contracts, and budget this plan assumes. The program manager therefore approves this plan.

**Platform choices.** KESTREL standardizes on Microsoft Azure Government at IL5 for the cloud, with US Gov Virginia as the primary region and US Gov Arizona for recovery. Active Directory in the mission data center remains the identity system of record, with Microsoft Entra ID as its cloud projection. A self-hosted Atlassian and GitLab stack inside Platform Prod holds the work itself. Jira tracks the work, GitLab holds source and runs the pipeline, and Confluence holds the governing plans and runbooks. A Palo Alto Networks rule base, managed once in Panorama, runs on both hubs and the alternate site. Splunk in the data center is the security monitoring platform.

**Authorization of each product.** Before any product is bought, Inherited Control Validation (`GV-5.12`) confirms its DoD authorization at the impact level it will run at. A product that fails that check is substituted, and the substitution is recorded in this plan and, if it changes a control's implementation, in the SSP and SCTM.

**Known product risk.** Atlassian has announced the end of its Data Center products. The Configuration Control Board re-evaluates the Jira, Jira Service Management, and Confluence choice by the end of Phase 3, while there is still time to migrate before support ends.

---

## 2. Rollout Phasing Strategy

The phases follow dependencies first. Identity, keys, the pipeline, and logging come before anything that relies on them, and detection comes after the telemetry it reads. Phases are set per activity, since the activities under one outcome often differ in urgency. An activity's SABER Maturity Level sets its default. Level 1, which the SABER marks as required for ATO, keeps its capability's place in the dependency sequence and must land by the end of Phase 3, when the ATO decision is due. Level 2 waits for Phase 2 at the earliest, and Level 3 waits for Phase 4. A pin moves an activity earlier only where KESTREL's design depends on it from the first build, or where building it in costs far less than retrofitting it, and each pin states its reason in its record. A record starts in the phase of its earliest activity and stays open until its last one lands, so one outcome remains one story. Work finishing in Phase 3 is due by 2028-04-30, two months before the ATO decision, so the SCA has time to assess it.

An interim authorization to test (`GV-5.7`) covers Phases 1 to 3. Integration during those phases uses synthetic data, spare aircraft, and the simulator, so no live mission data or flight depends on a system that is not yet authorized.

| Phase | Target Timeframe | Dependencies Satisfied / Rationale | Funding Status | Major Outcomes in This Phase |
|---|---|---|---|---|
| Phase 1, Foundation | 2027-01-01 to 2027-06-30 | Builds what everything else assumes, namely the landing zone and hubs, identity and privileged access, keys and PKI, the pipeline, logging into the security monitoring platform, and the governance bodies and core plans. | Funded (FY27 base) | 348 activities. 120 records start here: ID (25), DI (12), NE (13), AP (26), DA (16), DE (10), GV (18) |
| Phase 2, Protect and Operate | 2027-07-01 to 2027-12-31 | Needs Phase 1 identity, keys, pipeline, and logging. Hardens and watches the estate, adds application security gates, data protection, backup and recovery, detection content, and incident response, and brings AI governance up before any AI build. | Funded (FY27 and FY28 base) | 526 activities. 139 records start here: ID (4), DI (12), NE (9), AP (27), AI (9), DA (10), DE (6), RS (20), RC (15), GV (12), RK (7), CO (8) |
| Phase 3, Mission, AI, and Fleet | 2028-01-01 to 2028-06-30 | Needs Phase 2 gates and detection. Builds the AI lifecycle controls, model serving guardrails, and the fleet and ground segment controls, and ends with the SCA assessment and the ATO decision. | Pending approval (FY28 RDT&E and O&M) | 259 activities. 98 records start here: ID (3), DI (4), NE (6), AI (70), DE (2), RC (1), GV (3), RK (7), CO (2) |
| Phase 4, Maturity | 2028-07-01 to 2028-12-31 | Needs a fielded system to tune against. Adds the Level 3 maturity outcomes, such as deception, breach and attack simulation, RASP, and post-quantum migration planning. | Unfunded (FY28 and FY29 requests) | 37 activities. 6 records start here: AP (2), DA (1), DE (3) |

---

## 3. Implementation Record

Each record in Section 4 follows the template's record pattern. Every record cites its SADD outcome by ID rather than restating the design intent or control mapping, which stay in the SADD. Each record also carries a table giving every activity under its outcome its phase and the seven activity-level metadata fields. The metadata is carried from the SABER. It is re-rated only where a governing plan sets a different cadence or a product decision changes the effort, cost, or timing the SABER assumed, and the record marks each re-rated value with its source. An activity that does not apply to KESTREL is marked not applicable with its reason, and the SADD lists the same activities.

Every record's status is Not Started, since the plan precedes Phase 1.

---

## 4. Implementation Records by Focus Area

| Pillar | Focus Area | Records | Activities |
|---|---|---|---|
| Protect | [ID: Identity](02-identity.md) | 32 | 140 |
| Protect | [DI: Device and Infrastructure](03-device-and-infrastructure.md) | 28 | 105 |
| Protect | [NE: Network and Environment](04-network-and-environment.md) | 28 | 124 |
| Protect | [AP: Application](05-application.md) | 55 | 150 |
| Protect | [AI: Artificial Intelligence](06-artificial-intelligence.md) | 79 | 181 |
| Protect | [DA: Data](07-data.md) | 27 | 81 |
| Operate | [DE: Detection](08-detection.md) | 21 | 97 |
| Operate | [RS: Response](09-response.md) | 20 | 60 |
| Operate | [RC: Recovery](10-recovery.md) | 16 | 41 |
| Manage | [GV: Governance](11-governance.md) | 33 | 116 |
| Manage | [RK: Risk](12-risk.md) | 14 | 44 |
| Manage | [CO: Compliance](13-compliance.md) | 10 | 33 |
| | **Total** | **363** | **1172** |

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

| Contract | Selected Product / Service | Required Contract Clause(s) | Source | Status | Records |
|---|---|---|---|---|---|
| C01 | Microsoft Azure Government (IL5) | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, DFARS 252.239-7010 | Standard Security Clause Library | Open | 142 |
| C02 | Microsoft 365 DoD and Windows enterprise licensing | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, DFARS 252.239-7010 | Standard Security Clause Library | Open | 51 |
| C03 | Atlassian Data Center (Jira Software, Jira Service Management, Confluence) | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery, vulnerability disclosure | Standard Security Clause Library | Open | 119 |
| C04 | GitLab Ultimate, self-managed | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery, vulnerability disclosure | Standard Security Clause Library | Open | 50 |
| C05 | JFrog Artifactory Enterprise+ with Xray, self-hosted | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery, vulnerability disclosure | Standard Security Clause Library | Open | 35 |
| C06 | Splunk Enterprise, Enterprise Security, SOAR, and UBA, self-hosted | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery, vulnerability disclosure | Standard Security Clause Library | Open | 71 |
| C07 | CyberArk Privileged Access Manager, self-hosted | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery, vulnerability disclosure | Standard Security Clause Library | Open | 17 |
| C08 | Palo Alto Networks VM-Series, PA-Series, and Panorama | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery, firmware signing | Standard Security Clause Library | Open | 17 |
| C09 | Cisco ACI, APIC, and Identity Services Engine | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery, firmware signing | Standard Security Clause Library | Open | 8 |
| C10 | Entrust nShield 5 HSMs | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, FIPS 140-3 Level 3 validation, firmware signing | Standard Security Clause Library | Open | 11 |
| C11 | Keyfactor Command, self-hosted | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery | Standard Security Clause Library | Open | 11 |
| C12 | Infoblox NIOS and Threat Defense | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery | Standard Security Clause Library | Open | 4 |
| C13 | Nozomi Networks Guardian and Central Management Console | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery | Standard Security Clause Library | Open | 8 |
| C14 | Corelight sensors | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery | Standard Security Clause Library | Open | 5 |
| C15 | Veeam Data Platform | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery | Standard Security Clause Library | Open | 15 |
| C16 | NetApp StorageGRID | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, firmware signing | Standard Security Clause Library | Open | 14 |
| C17 | Acalvio ShadowPlus, on-premises | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery | Standard Security Clause Library | Open | 1 |
| C18 | AttackIQ Enterprise, on-premises | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery | Standard Security Clause Library | Open | 1 |
| C19 | Contrast Security Assess and Protect, on-premises | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery | Standard Security Clause Library | Open | 1 |
| C20 | Microchip SyncServer S650 time servers | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, firmware signing | Standard Security Clause Library | Open | 2 |
| C21 | Red Hat Enterprise Linux and Ansible Automation Platform | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery | Standard Security Clause Library | Open | 11 |
| C22 | Pomerium Enterprise, self-hosted | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, SBOM delivery, vulnerability disclosure | Standard Security Clause Library | Open | 2 |
| C23 | Bastille Enterprise RF detection | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, firmware signing | Standard Security Clause Library | Open | 1 |
| C24 | Yubico YubiKey 5 FIPS Series | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, FIPS 140-3 validation | Standard Security Clause Library | Open | 2 |
| C25 | ExpressRoute circuits from two carriers on separate paths | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, path diversity | New clause needed (path diversity) | Open | 4 |
| C26 | Aircraft, ground control station, and launch equipment manufacturer | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, DFARS 252.204-7021, SBOM delivery, firmware signing, onboard TEE support | New clause needed (onboard TEE support) | Open | 12 |
| C27 | Payload Vendor A and Payload Vendor B | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, DFARS 252.204-7021, SBOM delivery, data rights terms | Standard Security Clause Library | Open | 1 |
| C28 | Penetration testing provider, including AI red team | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, DFARS 252.204-7021, rules of engagement | New clause needed (AI red team scope) | Open | 2 |
| C29 | Tenable Attack Surface Management and GitGuardian public monitoring | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30 | Standard Security Clause Library | Open | 2 |
| C30 | Blancco Drive Eraser | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30 | Standard Security Clause Library | Open | 3 |
| C31 | CSSP service agreement amendment for containment playbooks | Containment role and playbook terms | New clause needed (CSSP containment role) | Open | 3 |

**Government-furnished, so no contract is needed:** DC3's DIB Cybersecurity program, DD Form 2930, DISA SCAP Compliance Checker and STIG Viewer, Iron Bank hardened images from Platform One, Joint Knowledge Online training, Tenable Security Center (ACAS), eMASS, the CSSP, the DISA Boundary Cloud Access Point, the DoD PPSM registry, the DoD Vulnerability Disclosure Program, the PSO's physical access control system, the Supplier Performance Risk System, the cross domain service provider's enterprise CDS.

**Open source, adopted through the ASP's approved component catalog:** Adversarial Robustness Toolbox, cert-manager, ClamAV, cleanlab, compliance-trestle (OSCAL), CVAT, Flower federated learning, garak, Great Expectations, gVisor sandboxed containers, KServe, kube-bench, lakeFS, Microsoft Presidio, MLflow tracking, ModelScan, ONNX Runtime quantization, Open Policy Agent (Gatekeeper and Conftest), ORAS offline bundles, OWASP Dependency-Track, OWASP Threat Dragon with MITRE ATLAS, Packer, PyRIT, Ratify, Semantic Kernel, Sigstore Cosign, SonarQube for IDE, Syft (CycloneDX), Terraform, Trivy misconfiguration scanning, Velociraptor.

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
