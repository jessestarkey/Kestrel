# KESTREL Security Architecture and Design Document (SADD)

> **Notional system.** KESTREL is fictional. The names, dates, and decisions below are invented to show a SADD in progress, and nothing here describes a real program or a real authorization.

This SADD is KESTREL's RMF "Step 2.5: Design." It turns the control set the AO approved in the [CCSD](../02-ccsd.md) into an architecture KESTREL's engineers can build, using the SABER v1.3 as the outcome catalog. It is split across files so each focus area can be read and revised on its own. This file holds the document-wide sections, and each focus area's file holds its part of Section 5.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| SADD Version | 0.2 |
| Date | 2026-11-11 |
| Prepared By | KESTREL PMO ISSE |
| Approved By | Pending. Version 0.2 is submitted to the KESTREL AO for approval as version 1.0. |
| Classification / Handling | CUI |
| Security Categorization | Confidentiality High, Integrity High, Availability Moderate (see Section 2) |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-11 | KESTREL PMO ISSE | Initial draft with the document-wide sections and the Identity focus area |
| 0.2 | 2026-11-11 | KESTREL PMO ISSE | Wrote the remaining eleven focus areas, for AO approval |

---

## 1. Purpose and Scope

This SADD translates the control set the AO approved in CCSD version 1.0 into KESTREL's security architecture, applying the SABER's POMAV model (Protect, Operate, Manage, Automate, Visualize). It sits between RMF Step 2 (Select), which produced the approved control set, and RMF Step 3 (Implement), which produces the Security Implementation Plan. It ends where implementation begins.

It covers the one KESTREL authorization boundary, namely the IL5 cloud's hub and ten spokes, the on-premises mission data center and its alternate site, and the UAS fleet. The IL6 enclave is a separate system with its own SADD. This document designs only KESTREL's side of the cross domain connection to it.

**Boundary case-outs:**

- **Personnel and physical security** belong to the PSO, as the SABER itself excludes them. Where an outcome depends on them, such as badge events at the operating sites, its External Dependencies field names the dependency.
- **Enterprise email and collaboration** come from the parent organization and are outside the boundary.
- **Airworthiness** is certified separately. This document covers the cybersecurity of the aircraft and ground systems, not their flight safety.

---

## 2. System Categorization and Tailoring Basis

| Element | Value |
|---|---|
| Authorization Framework | DoD RMF (DoDI 8510.01) |
| Cloud Impact Level (DoD Cloud Computing SRG) | IL5 |
| FIPS 199 / CNSSI 1253 Impact Level (Confidentiality) | High |
| FIPS 199 / CNSSI 1253 Impact Level (Integrity) | High |
| FIPS 199 / CNSSI 1253 Impact Level (Availability) | Moderate |
| Resulting NIST SP 800-53 Rev 5 Baseline | Selected per objective under CNSSI 1253, from the High confidentiality, High integrity, and Moderate availability columns |
| Categorization and Control Selection Document (CCSD) | Version 1.0, approved by the AO on 2026-10-02. Version 1.1, which adds the performer interconnection, is in SCA review and changes no impact value or control selection. |

The PMO ISSE drafted the CCSD, the SCA reviewed it, and the AO approved version 1.0. This SADD is built against that version and does not re-derive it. High confidentiality comes from one information type, the command link and root signing key material, which lives only in the HSMs and the datalink crypto modules. The design concentrates its High confidentiality controls there.

**Applicable overlays,** carried from CCSD Section 6:

| Overlay | Applies? | Notes |
|---|---|---|
| SAP Overlay(s) | No | KESTREL is not a special access program. |
| Classified Information Overlay | No | KESTREL holds no classified information. |
| Privacy Overlay (Low / Moderate / High) | Yes, Low | Incidental imagery of people in raw collection, never indexed or retrieved by person. |
| Intelligence Community (IC) Overlay | No | KESTREL is a DoD system under a DoD AO. |
| Space Platform Overlay | No | |
| Cloud Computing Overlay | Yes | Every IL5 spoke and the cloud hub, together with the SRG's IL5 requirements. |
| Cross Domain Solution (CDS) Overlay | No | The enterprise provider's cross domain solution carries it. KESTREL's side falls under Cross Domain Solution (CDS) Transfer Procedures (`NE-2.10`). |
| NIST SP 800-82 Rev. 3 OT Overlay | Yes | The UAS fleet. |
| DoD AI Cybersecurity Risk Management Tailoring Guide | Yes, as tailoring guidance | The detection models, the LLM analyst assistant, and the mission-planning agent. |

**Adjacent compliance regimes.** Three regimes bear on KESTREL without modifying its control baseline, so they are tracked outside this document. Airworthiness belongs to the program's airworthiness authority. Section 508 accessibility applies to the analyst portal and belongs to the engineering lead. Foreign disclosure and export control govern every release through the partner API and belong to the program's foreign disclosure officer.

---

## 3. Architecture Overview

KESTREL is a hybrid ISR analytics platform inside one IL5 authorization boundary. The IL5 cloud is a hub and ten spokes organized by team. The platform team runs the shared pipeline and registry, the ML team trains and serves every model, and two mission teams, split by payload vendor, run the applications analysts and partners reach through the DMZ. Every spoke-to-spoke flow crosses the cloud hub's NGFW, which denies dev/test to prod traffic and traffic between the two mission teams. The on-premises mission data center holds the authoritative data lake, the identity provider, the PKI and HSMs, and the security monitoring platform, joined to the cloud by a dedicated circuit. An alternate site in a parent organization facility holds a warm standby of identity and the PKI and copies of the backups, on its own circuit. The UAS fleet flies the missions and runs detection models on board. Outside the boundary, an enterprise cross domain solution carries baselines to the IL6 enclave and released products back. The [system description](../01-system-description.md) holds the full diagram and data flows.

**Deployment footprint for this program:**

- [x] Cloud
- [x] On-Premises
- [x] Hybrid
- [x] Cyber-Physical System (OT/ICS)
- [ ] Air-Gapped/Isolated

**Affected Components footprint for this program.** Most checked values come from the component tables in the system description. Values marked † come from its prose, such as its data flows or its users section.

{{FOOTPRINT}}

**POMAV summary:**

| Element | Role in this program |
|---|---|
| **Protect** (Zero Trust Protections) | All six focus areas are in scope. Identity and Device and Infrastructure carry the key material and OT device work behind the High ratings. Application and Artificial Intelligence carry the two release paths, continuous to IL5 production and periodic to the aircraft and the IL6 enclave. |
| **Operate** (Defensive Cyber Operations) | Detection, Response, and Recovery are all in scope. The CSSP monitors around the clock from outside and contains incidents that cannot wait through pre-approved playbooks, while the performer's Security Team tunes detection for KESTREL's OT and AI systems and carries out hands-on response. Recovery must restore an airborne fleet's command path as well as the data lake. |
| **Manage** (Mission Assurance Management) | Governance, Risk, and Compliance are all in scope for one authorization package under one AO, with continuous monitoring across cloud, on-premises, hybrid, and OT environments. |
| **Automate** (cross-cutting) | Automation concentrates in the build and certification pipeline and the model lifecycle, where Application and Artificial Intelligence carry most of the Automate activities. Section 8 gives the counts. |
| **Visualize** (cross-cutting) | Posture views roll up to the security monitoring platform and the program's posture reporting to the AO. Section 8 gives the counts. |

---

## 4. How to Read Section 5

Each focus area file follows the SABER template's outcome block. Every in-scope outcome carries six fields, and every activity beneath it carries its description and the SABER's seven activity fields.

- **Carried from the SABER v1.3 unchanged:** NIST Control Mapping, Security Impact, and every activity field. Deployment Type and Affected Components are carried as well, but narrowed to the values KESTREL actually fields.
- **Written for KESTREL:** Design Intent and External Dependencies. Design Intent says what the outcome requires in KESTREL's terms. It overrides an activity's carried description where the two differ, such as an activity that applies to only part of KESTREL's footprint.
- **Scoped out:** an outcome is dropped when none of its deployment types or affected components are in KESTREL's footprint, or when tailoring removes it. Each focus area file ends with its dropped outcomes and the reason for each.

---

## 5. Pillar, Focus Area, and Capability Design

{{STATUS}}

Three outcomes drop out across the whole framework by decision rather than footprint. Device Compliance (`DI-4.1`) drops because KESTREL owns no laptops, desktops, or mobile devices. Unidirectional Gateways (`NE-2.9`) drops because the ground segment conduit carries traffic both ways. Native Email Messaging Service (`NE-3.6`) drops because KESTREL runs no email service and the AO approved removing SI-8.

Two activities inside in-scope outcomes do not apply. Derived/Mobile Credentials (`ID-2.1.3`) has nothing to issue, since KESTREL has no mobile devices. National Security Systems PKI Hardware Token Management (`ID-2.2.5`) belongs to the IL6 enclave, not to KESTREL. The Security Implementation Plan marks both as not applicable.

One activity runs under a CCSD exception. Emergency Account Authentication Protections (`ID-4.6.2`) uses console-only passwords for the directory and ground segment break-glass accounts under CCSD tailoring action 6, proposed in version 1.1. For those accounts, the SABER mapping's note that emergency accounts reuse the standard authentication policy does not hold.

---

## 6. External System and Service Dependencies

This table rolls up the External Dependencies field from every focus area.

| Dependency | Depended On By (Outcome ID(s)) | Nature of Dependency | Owning Party |
|---|---|---|---|
| DoD PKI | ID-1.1, ID-1.2, ID-2.1, ID-2.2, DA-3.7 | Proofing through CAC issuance, user certificates, and revocation status | DoD PKI |
| External Certificate Authorities and partner PKIs | ID-1.2, ID-2.1, ID-2.2, DA-3.7 | Partner certificates and assertions, and their revocation status | Each issuing authority, under the partner memoranda of agreement |
| IL5 cloud provider | ID-3.1, DI-1.1, DI-2.4, DI-3.1, DI-3.2, DI-3.4, DI-4.6, DI-4.8, NE-1.2, NE-2.1 to NE-2.6, NE-3.3, NE-3.4, NE-3.5, AI-1.3, AI-1.5, AI-8.3, AI-8.9, AI-9.9, DA-1.4, DA-2.4, DA-2.5, DA-3.3, DA-3.5, DA-3.11, DA-3.12, DE-1.1, DE-2.1, DE-3.1, DE-3.4, RS-1.1, RS-1.4, RC-1.2, RC-2.3, RC-3.3, GV-3.1, GV-3.3, GV-4.6, GV-5.6, GV-5.12 | Native workload identity, resource inventory and configuration state, physical hosts and network devices, platform patching, private endpoints and the circuit's cloud side, firewall, DDoS, WAF, and DNS services, the hosted foundation models with their content filters, the HSM-backed key management service, native detection, response actions, and control-plane logging, its security team's contact path, time service, native backup, and a second IL5 region for recovery, inherited under the provisional authorization | Cloud provider |
| Boundary Cloud Access Point | ID-2.5, NE-2.5, NE-2.13, GV-5.6, GV-5.12 | The only inbound path, its network-origin signal, and upstream filtering | DoD |
| Enterprise cross domain service provider | NE-2.10, GV-5.6, GV-5.12 | The cross domain solution, its product selection, and its accreditation | Cross domain service provider, under the interconnection agreement |
| IL6 enclave owner | NE-2.10, AI-7.4, RS-3.5 | Release review for every high-to-low product, and joint handling of any spill traced to one | IL6 enclave program |
| DISA PPSM program | NE-2.12 | The PPSM registry and Category Assurance List | DISA |
| Penetration testing provider | NE-1.5, AP-3.5, AI-5.7, AI-6.3, GV-5.6 | Independent tests of the whole system, its external paths, and its segmentation, and an AI red team for new use cases and foundation model changes, as a check on the design | Provider, under each engagement's rules of engagement |
| Cyber defense service provider | ID-4.1, ID-4.2, DI-1.4, DI-4.8, DI-5.4, DI-5.5, NE-3.1, NE-3.2, NE-3.5, NE-3.7, AP-5.6, AI-9.4, DE-1.1, DE-1.2, DE-1.3, DE-1.4, DE-3.1, DE-3.2, RS-1.2, RS-1.3, RS-1.5, RS-1.6, RS-1.7, RS-3.1, RS-3.2, RS-4.1, GV-3.1, GV-5.6, GV-5.12, RK-2.1, RK-2.2, RK-2.3 | Analysts in the CSSP host pool with read access and pre-approved containment playbooks, forwarded telemetry, IAVM relay, threat intelligence, signatures, external exposure reports, purple team participation, its own retained copy of security telemetry, round-the-clock triage, directives, and reporting to the DoD reporting chain | CSSP, under its service agreement |
| Performer laptops and device management | ID-2.5, ID-4.2, NE-2.7, AP-2.1, AP-2.4, AI-3.4, RS-1.6, GV-2.3, GV-3.2, GV-5.6 | CMMC Level 2 laptops as the origin for developer and Tier 1 sessions, and each laptop's compliance signal | The performer, under the interconnection agreement |
| Parent organization's and performer's personnel systems | ID-1.8 | Departure signals that trigger deprovisioning | Parent organization and performer |
| PSO's physical access control systems | ID-1.10 | Badge events at the data center, the alternate site, and each operating site | PSO |
| PSO's insider threat program | DE-1.6, DE-1.9, RS-3.5 | Receives insider threat referrals and spill reports, and owns every case | PSO |
| Parent organization's alternate site | RC-2.3, RC-3.3, RC-3.4, GV-5.6, GV-5.12 | The warm standby for the data center's Tier 1 services, a second HSM, and a copy of the backups | Parent organization, under a facility agreement |
| Second circuit provider | RC-3.4 | A second dedicated circuit on a separate path to the cloud | Circuit provider |
| Parent organization's enterprise services | GV-1.1, GV-2.3 | Enterprise security policy KESTREL's policy sits beneath, and phishing exercises on its email systems | Parent organization |
| DoW CIO, DoD, and NIST AI guidance | GV-1.6, GV-4.5 | The zero trust reference architecture and target, and the AI frameworks and directives KESTREL maps to | DoW CIO, DoD, and NIST |
| Security Control Assessor | RK-1.5, RK-1.6, RK-1.7, CO-2.2 | Independent assessment, and the Security Assessment Plan, SAR, and RAR | SCA, for the AO |
| DoD intelligence producers and DC3's DIB Cybersecurity program | RK-2.1, RK-2.2, RK-2.3 | Threat intelligence, and indicator sharing on the performer's side | DoD and DC3 |
| Requirement issuers and DISA's STIG and SCAP content | CO-1.1, CO-1.2 | The statutes, regulations, and issuances binding KESTREL, and the baselines its scans evaluate against | DoD, OMB, and DISA |
| External auditors and inspectors | CO-3.2 | Audits and inspections by inspectors general, GAO, cyber readiness inspectors, DCMA, and DIBCAC | Each auditing body |
| DoD component privacy office | CO-4.1, CO-4.2 | Oversight of the privacy program and approval of each privacy impact assessment | DoD component |
| DoD authoritative time service | DE-3.4 | Reference the data center's time servers check against | DoD |
| Aircraft, ground station, payload, and launch equipment vendors | ID-3.7, ID-4.7, DI-2.4, DI-3.4, DI-3.5, DI-4.8, DI-4.9, NE-2.8, NE-2.11, NE-3.9, AP-2.6, AP-2.12, AI-8.12, DA-1.2, DA-3.1, DA-3.2, DA-3.4, RC-1.4, GV-3.1, GV-3.2, GV-3.3, GV-3.4 | Devices that accept program-issued identities, support under agreement, hardening guidance, firmware and patch validation, datalink crypto modules, documented command sets, the payload vendors' certified conversion software, SBOMs for every delivery, the aircraft's onboard trusted execution environment, the datalink crypto modules and their post-quantum roadmap, and the data rights terms the vendor attributes encode | Each vendor |
| Public package indexes and image sources | AP-2.7, AP-2.14, AI-4.6 | Third-party packages and the upstream images the hardened bases derive from, reached only through the package mirror | Each index's maintainers |
| Pretrained model and foundation model publishers | AI-1.3, AI-1.5, AI-4.7, AI-8.3, GV-3.3, GV-4.6 | Pretrained checkpoints with their signatures or digests, and the foundation model versions the cloud provider serves | Each publisher |
| Partner nations | DA-1.6, RS-1.6, GV-5.6 | Honoring rights protection on released report documents, and receiving notice when their data is affected | Each partner nation, under its memorandum of agreement |
| DoD Vulnerability Disclosure Program | AP-5.10 | Researcher reports against KESTREL's internet-reachable endpoints | DoD Cyber Crime Center |

---

## 7. Control Mapping Coverage Summary

The coverage table is generated from every in-scope outcome's NIST Control Mapping and lives in [control-coverage.md](control-coverage.md). It covers all twelve focus areas already, since the mappings are carried from the SABER. KESTREL's in-scope outcomes claim {{NCTRL}} controls and enhancements.

---

## 8. Cross-Cutting Discipline Rollup (Automate / Visualize)

{{AVROWS}}

**Automate:** automation concentrates where KESTREL releases things, namely the build pipeline, Certification to Field, and the model lifecycle. These are the gates every release to production, the aircraft, and the IL6 enclave must pass.

**Visualize:** posture views roll up through the security monitoring platform and the posture reporting to the AO, with OT and AI posture shown alongside the IT estate rather than in separate tools.

---

## 9. Gap Register

| Control ID | Gap Description | Resolution | Status |
|---|---|---|---|
| PE family | Only PE-2 and PE-3 are claimed, both partially, by physical and logical access correlation (`ID-1.10`). | Addressed outside the SABER's scope. The PSO owns physical security, the IL5 cloud segments inherit it from the cloud provider, and the alternate site inherits it from the parent organization's facility. | Closed |
| PS family | Only PS-7 is claimed, partially, by vendor support access (`ID-4.7`). | Addressed outside the SABER's scope. The PSO owns personnel security. | Closed |
| Full selection check | This register is checked against the claims in Section 7. The check against every control in the CNSSI 1253 selection waits for the SCTM's per-control list. | Re-run when the SCTM is built from Section 7. | Open |

SI-8 is not a gap. The AO removed it in CCSD tailoring action 1, and its one owning outcome dropped out with it.

---

## 10. Approval and Periodic Review

**Approved By:** Pending. Version 0.2 is submitted to the KESTREL AO for approval as version 1.0.

**Review Cadence:** Annually, and whenever a revision trigger below occurs.

**Revision Triggers:** a CCSD revision that changes the approved control set, an overlay applied or removed, a categorization change, or the fielded architecture diverging from what this document describes. Fielding the replacement payload processing workstation is a known trigger, since it closes CCSD tailoring action 3.
