# KESTREL Security Architecture and Design Document (SADD)

> **Notional system.** KESTREL is fictional. The names, dates, and decisions below are invented to show a SADD in progress, and nothing here describes a real program or a real authorization.

This SADD is KESTREL's RMF "Step 2.5: Design." It turns the control set the AO approved in the [CCSD](../02-ccsd.md) into an architecture KESTREL's engineers can build, using the SABER v1.3 as the outcome catalog. It is split across files so each focus area can be read and revised on its own. This file holds the document-wide sections, and each focus area's file holds its part of Section 5.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| SADD Version | 0.1 |
| Date | 2026-11-11 |
| Prepared By | KESTREL PMO ISSE |
| Approved By | Pending. The KESTREL AO approves the SADD once every focus area is written. |
| Classification / Handling | CUI |
| Security Categorization | Confidentiality High, Integrity High, Availability Moderate (see Section 2) |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-11 | KESTREL PMO ISSE | Initial draft with the document-wide sections and the Identity focus area |

---

## 1. Purpose and Scope

This SADD translates the control set the AO approved in CCSD version 1.0 into KESTREL's security architecture, applying the SABER's POMAV model (Protect, Operate, Manage, Automate, Visualize). It sits between RMF Step 2 (Select), which produced the approved control set, and RMF Step 3 (Implement), which produces the Security Implementation Plan. It ends where implementation begins.

It covers the one KESTREL authorization boundary, namely the IL5 cloud's hub and ten spokes, the on-premises mission data center, and the UAS fleet. The IL6 enclave is a separate system with its own SADD. This document designs only KESTREL's side of the cross domain connection to it.

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

KESTREL is a hybrid ISR analytics platform inside one IL5 authorization boundary. The IL5 cloud is a hub and ten spokes organized by team. The platform team runs the shared pipeline and registry, the ML team trains and serves every model, and two mission teams, split by payload vendor, run the applications analysts and partners reach through the DMZ. Every spoke-to-spoke flow crosses the cloud hub's NGFW, which denies dev/test to prod traffic and traffic between the two mission teams. The on-premises mission data center holds the authoritative data lake, the identity provider, the PKI and HSMs, and the security monitoring platform, joined to the cloud by a dedicated circuit. The UAS fleet flies the missions and runs detection models on board. Outside the boundary, an enterprise cross domain solution carries baselines to the IL6 enclave and released products back. The [system description](../01-system-description.md) holds the full diagram and data flows.

**Deployment footprint for this program:**

- [x] Cloud
- [x] On-Premises
- [x] Hybrid
- [x] Cyber-Physical System (OT/ICS)
- [ ] Air-Gapped/Isolated

**Affected Components footprint for this program.** Most checked values come from the component tables in the system description. Values marked † come from its prose, such as its data flows or its users section.

- [x] **Compute**
    - [x] Virtual Machine/Server
    - [x] Container
    - [x] Container Orchestration Control Plane
    - [x] Serverless/Platform Service
    - [x] Cryptographic Hardware/HSM
    - [x] Cloud Account/Subscription/Tenant Boundary †
- [x] **Storage/Database**
    - [x] Database Service
    - [x] Object/File Storage
    - [x] Artifact/Model Registry
    - [ ] Removable Media
    - [x] Message Queue/Event Stream
    - [ ] Cache
    - [ ] Search Index
    - [x] Analytics/Warehouse Service
    - [x] Vector Store/Embedding Index
    - [x] Security Information and Event Management (SIEM) Platform
    - [x] Secrets Vault
    - [x] Backup/Archive Repository
- [x] **Network Infrastructure**
    - [x] Routing/Switching Fabric
    - [x] Wireless/RF Infrastructure
    - [x] Segmentation Policy
    - [x] Network Firewall
    - [x] Load Balancer/Reverse Proxy/API Gateway
    - [x] Web Application Firewall
    - [x] DDoS Protection
    - [x] Intrusion Detection/Prevention System (IDPS)
    - [x] Service-Native/Resource-Level Firewall
    - [x] DNS Infrastructure
    - [x] Remote Access/VPN Gateway
    - [ ] Network Access Control (NAC)
    - [x] Private Connectivity/Dedicated Circuit
    - [ ] Managed Service Network Integration
    - [x] Cross-Domain/Boundary Transfer
    - [ ] Industrial Protocol Filtering (OT DPI)
    - [x] OT/ICS Zone-Conduit Segmentation (IEC 62443)
    - [x] OT/ICS Passive Network Monitoring
    - [x] Network Telemetry/Monitoring Platform
- [x] **Identity Platform**
    - [x] Directory/Platform Core Infrastructure
    - [x] Identity Lifecycle and Governance †
    - [x] Human Authentication
    - [x] Cloud Workload/Native Platform Identity †
    - [x] Application and Service Account Identity †
    - [x] AI Agent Identity
    - [x] OT/Legacy Device Identity
    - [x] Privileged Access Management
    - [x] PKI/Certificate Authority
    - [x] External/Federated Trust †
- [x] **Device/Workstation**
    - [ ] Managed Device (Laptop/Desktop)
    - [ ] Mobile Device
    - [x] Virtual Desktop Infrastructure (VDI)
    - [x] Privileged Access Workstation (PAW)
- [x] **Application/API**
    - [x] First-Party/Custom Application Code
    - [x] Third-Party Dependency (Embedded Library/Package)
    - [x] Self-Hosted Third-Party Application (COTS)
    - [x] API/Interface Contract
    - [x] Client-Side/Browser-Executed Code
    - [ ] Third-Party Runtime Service Dependency
    - [x] Infrastructure-as-Code (IaC)
    - [x] CI/CD Pipeline
- [x] **AI/ML System**
    - [x] Third-Party API Model
    - [x] Self-Hosted Model
    - [x] Base/Pretrained Model †
    - [x] Fine-Tuned Model
    - [x] Foundation Model
    - [x] Embedding Model
    - [x] Retrieval-Augmented Generation (RAG)
    - [x] AI Agent
    - [x] Prompt/Instruction Layer
    - [x] AI Interface/Inference Endpoint
- [x] **OT/ICS Device**
    - [x] Industrial Controller/SCADA
    - [x] Legacy IT (Unpatchable, Non-Industrial)
    - [x] Edge/Embedded AI Device

**POMAV summary:**

| Element | Role in this program |
|---|---|
| **Protect** (Zero Trust Protections) | All six focus areas are in scope. Identity and Device and Infrastructure carry the key material and OT device work behind the High ratings. Application and Artificial Intelligence carry the two release paths, continuous to IL5 production and periodic to the aircraft and the IL6 enclave. |
| **Operate** (Defensive Cyber Operations) | Detection, Response, and Recovery are all in scope. The CSSP monitors around the clock from outside, while the performer's Security Team tunes detection for KESTREL's OT and AI systems and carries out hands-on response. Recovery must restore an airborne fleet's command path as well as the data lake. |
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

| Pillar | Focus Area | Outcomes In / Out | Activities | Status |
|---|---|---|---|---|
| Protect | [ID: Identity](02-identity.md) | 32 / 0 | 140 | Written |
| Protect | [DI: Device and Infrastructure](03-device-and-infrastructure.md) | 28 / 1 | 105 | Written |
| Protect | [NE: Network and Environment](04-network-and-environment.md) | 28 / 2 | 124 | Written |
| Protect | [AP: Application](05-application.md) | 55 / 0 | 150 | Written |
| Protect | [AI: Artificial Intelligence](06-artificial-intelligence.md) | 79 / 0 | 181 | Written |
| Protect | DA: Data | 27 / 0 | 81 | Pending |
| Operate | DE: Detection | 21 / 0 | 97 | Pending |
| Operate | RS: Response | 20 / 0 | 60 | Pending |
| Operate | RC: Recovery | 16 / 0 | 41 | Pending |
| Manage | GV: Governance | 33 / 0 | 116 | Pending |
| Manage | RK: Risk | 14 / 0 | 44 | Pending |
| Manage | CO: Compliance | 10 / 0 | 33 | Pending |

Three outcomes drop out across the whole framework by decision rather than footprint. Device Compliance (`DI-4.1`) drops because KESTREL owns no laptops, desktops, or mobile devices. Unidirectional Gateways (`NE-2.9`) drops because the ground segment conduit carries traffic both ways. Native Email Messaging Service (`NE-3.6`) drops because KESTREL runs no email service and the AO approved removing SI-8.

---

## 6. External System and Service Dependencies

This table rolls up the External Dependencies field from every written focus area, and it grows as each focus area is written.

| Dependency | Depended On By (Outcome ID(s)) | Nature of Dependency | Owning Party |
|---|---|---|---|
| DoD PKI | ID-1.1, ID-1.2, ID-2.1, ID-2.2 | Proofing through CAC issuance, user certificates, and revocation status | DoD PKI |
| External Certificate Authorities and partner PKIs | ID-1.2, ID-2.1, ID-2.2 | Partner certificates and assertions, and their revocation status | Each issuing authority, under the partner memoranda of agreement |
| IL5 cloud provider | ID-3.1, DI-1.1, DI-2.4, DI-3.1, DI-3.2, DI-3.4, DI-4.6, DI-4.8, NE-1.2, NE-2.1 to NE-2.6, NE-3.3, NE-3.4, NE-3.5, AI-1.3, AI-1.5, AI-8.3, AI-8.9, AI-9.9 | Native workload identity, resource inventory and configuration state, physical hosts and network devices, platform patching, private endpoints and the circuit's cloud side, firewall, DDoS, WAF, and DNS services, and the hosted foundation models with their content filters, inherited under the provisional authorization | Cloud provider |
| Boundary Cloud Access Point | ID-2.5, NE-2.5, NE-2.13 | The only inbound path, its network-origin signal, and upstream filtering | DoD |
| Enterprise cross domain service provider | NE-2.10 | The cross domain solution, its product selection, and its accreditation | Cross domain service provider, under the interconnection agreement |
| IL6 enclave owner | NE-2.10, AI-7.4 | Release review for every high-to-low product | IL6 enclave program |
| DISA PPSM program | NE-2.12 | The PPSM registry and Category Assurance List | DISA |
| Penetration testing provider | NE-1.5, AP-3.5, AI-5.7, AI-6.3 | Independent tests of the whole system, its external paths, and its segmentation, and an AI red team for new use cases and foundation model changes, as a check on the design | Provider, under each engagement's rules of engagement |
| Cyber defense service provider | ID-4.2, DI-1.4, DI-4.8, DI-5.4, DI-5.5, NE-3.1, NE-3.2, NE-3.5, NE-3.7, AP-5.6, AI-9.4 | Read-only analysts in the CSSP host pool, forwarded telemetry, IAVM relay, threat intelligence, signatures, and external exposure reports | CSSP, under its service agreement |
| Performer laptops and device management | ID-2.5, ID-4.2, NE-2.7, AP-2.1, AP-2.4, AI-3.4 | CMMC Level 2 laptops as the origin for developer and Tier 1 sessions, and each laptop's compliance signal | The performer, under the interconnection agreement |
| Parent organization's and performer's personnel systems | ID-1.8 | Departure signals that trigger deprovisioning | Parent organization and performer |
| PSO's physical access control systems | ID-1.10 | Badge events at the data center and operating sites | PSO |
| Aircraft, ground station, payload, and launch equipment vendors | ID-3.7, ID-4.7, DI-2.4, DI-3.4, DI-3.5, DI-4.8, DI-4.9, NE-2.8, NE-2.11, NE-3.9, AP-2.6, AP-2.12, AI-8.12 | Devices that accept program-issued identities, support under agreement, hardening guidance, firmware and patch validation, datalink crypto modules, documented command sets, the payload vendors' certified conversion software, SBOMs for every delivery, and the aircraft's onboard trusted execution environment | Each vendor |
| Public package indexes and image sources | AP-2.7, AP-2.14, AI-4.6 | Third-party packages and the upstream images the hardened bases derive from, reached only through the package mirror | Each index's maintainers |
| Pretrained model and foundation model publishers | AI-1.3, AI-1.5, AI-4.7, AI-8.3 | Pretrained checkpoints with their signatures or digests, and the foundation model versions the cloud provider serves | Each publisher |
| DoD Vulnerability Disclosure Program | AP-5.10 | Researcher reports against KESTREL's internet-reachable endpoints | DoD Cyber Crime Center |

---

## 7. Control Mapping Coverage Summary

The coverage table is generated from every in-scope outcome's NIST Control Mapping and lives in [control-coverage.md](control-coverage.md). It covers all twelve focus areas already, since the mappings are carried from the SABER. KESTREL's in-scope outcomes claim 491 controls and enhancements.

---

## 8. Cross-Cutting Discipline Rollup (Automate / Visualize)

| Focus Area | Automate Activities | Visualize Activities |
|---|---|---|
| ID: Identity | 32 | 1 |
| DI: Device and Infrastructure | 26 | 4 |
| NE: Network and Environment | 32 | 1 |
| AP: Application | 79 | 6 |
| AI: Artificial Intelligence | 93 | 2 |
| DA: Data | 23 | 2 |
| DE: Detection | 14 | 4 |
| RS: Response | 9 | 1 |
| RC: Recovery | 3 | 1 |
| GV: Governance | 3 | 1 |
| RK: Risk | 2 | 1 |
| CO: Compliance | 3 | 1 |
| **Total** | **319** | **25** |

**Automate:** automation concentrates where KESTREL releases things, namely the build pipeline, Certification to Field, and the model lifecycle. These are the gates every release to production, the aircraft, and the IL6 enclave must pass.

**Visualize:** posture views roll up through the security monitoring platform and the posture reporting to the AO, with OT and AI posture shown alongside the IT estate rather than in separate tools.

---

## 9. Gap Register

| Control ID | Gap Description | Resolution | Status |
|---|---|---|---|
| PE family | Only PE-2 and PE-3 are claimed, both partially, by physical and logical access correlation (`ID-1.10`). | Addressed outside the SABER's scope. The PSO owns physical security, and the IL5 cloud segments inherit it from the cloud provider. | Closed |
| PS family | Only PS-7 is claimed, partially, by vendor support access (`ID-4.7`). | Addressed outside the SABER's scope. The PSO owns personnel security. | Closed |
| Full selection check | This register is checked against the claims in Section 7. The check against every control in the CNSSI 1253 selection waits for the SCTM's per-control list. | Re-run when the SCTM is built from Section 7. | Open |

SI-8 is not a gap. The AO removed it in CCSD tailoring action 1, and its one owning outcome dropped out with it.

---

## 10. Approval and Periodic Review

**Approved By:** Pending. The KESTREL AO approves version 1.0 once every focus area is written.

**Review Cadence:** Annually, and whenever a revision trigger below occurs.

**Revision Triggers:** a CCSD revision that changes the approved control set, an overlay applied or removed, a categorization change, or the fielded architecture diverging from what this document describes. Fielding the replacement payload processing workstation is a known trigger, since it closes CCSD tailoring action 3.
