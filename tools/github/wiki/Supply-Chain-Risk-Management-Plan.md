> **Notional system.** KESTREL is fictional. This page stands in for a governing plan in KESTREL's self-hosted Confluence. Its names, tiers, and decisions are invented to show a completed Supply Chain Risk Management Plan.

# KESTREL Supply Chain Risk Management Plan (SCRM)

This plan sets who KESTREL buys from, what it requires of them, and how it checks what arrives. It is written for the contracting, procurement, and receiving staff outside the security organization, as much as for the security team. It carries out the design decisions in the [Governance](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/11-governance.md) section of the SADD. The [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/11-governance.md) is the record of each product selection, and its contracting table lists every contract this plan governs.

**NIST Control Mapping:** SR-1 (partial), SR-2 (full), and SR-2(1) (full), held through GV-3.5.

> **Phasing.** This plan is approved in Phase 2. Vendor questionnaires, the clause library, trusted sourcing, and inspection at receipt start in Phase 1, before the first awards. They run on the supply chain lead's interim procedure until this plan replaces it. The supply chain assessment and the dependency map start in Phase 2. Fleet inspection and rescans start in Phase 3, when the fleet arrives.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| SCRM Version | 0.2 |
| Date | 2026-11-26 |
| Prepared By | Supply chain lead, with the SCRM team |
| Reviewed By | ISSM and PMO ISSE |
| Approved By | Configuration Control Board, chaired by the chief engineer |
| Source SADD Version | 0.9 |
| Source SIP Version | 0.7 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-26 | Supply chain lead | Initial draft for Configuration Control Board review |
| 0.2 | 2026-11-26 | Supply chain lead | Added developer training and personnel screening clauses to the Tier 1 set |

---

## Purpose and Scope

This SCRM plan covers every supplier of hardware, software, or services to KESTREL. That includes open-source components, which have no supplier to contract with. It does not cover the technical checks on what is delivered, such as SBOMs, build provenance, and signing. Those belong to the Application Security Plan (ASP) and the AI/ML Security Plan (AISP). DoD and provider services, such as the IL5 cloud provider and the CSSP, are relied on through their authorizations under Inherited Control Validation (`GV-5.12`). This plan covers only what their contracts add.

---

## 1. SCRM Team and Roles

*Traces to GV-3.5.1.*

The SCRM team is a standing group that meets each month and whenever a Tier 1 supplier changes. Its members are named by position.

| Position | Role on the team |
|---|---|
| Supply chain lead, Program Office | Chairs the team and owns this plan |
| Contracting officer | Puts the clauses into each contract and enforces them |
| Program legal counsel | Reviews licenses, data rights, and FOCI findings |
| PMO ISSE | Ties supplier risk to the SADD and the risk register |
| ISSM | Receives counterfeit and compromise reports |
| Platform Team's data center lead | Owns receipt and inspection of data center hardware |
| Fleet Operations' operations lead | Owns receipt and inspection of fleet equipment |
| ML Team lead | Brings AI suppliers and model publishers |

**What the team leads.**

- Vendor assessment and tiering
- The clause library and its flow-down
- The yearly supply chain assessment and dependency map
- Counterfeit reporting and disposal of suspect parts
- Tracking every supplier finding to closure

---

## 2. Vendor Assessment and Risk Tiering

*Traces to GV-3.1.1 and GV-3.1.2.*

**Before award.** Every commercial supplier answers KESTREL's security questionnaire before a contract is awarded, including the Phase 1 awards. The questionnaire asks about:

- Ownership, and any foreign ownership, control, or influence
- The supplier's own key suppliers and where they are based
- Its NIST SP 800-171 assessment score and CMMC status
- Its secure development and delivery practice
- Its vulnerability disclosure and incident reporting
- Its support commitments and end-of-life notice

**Checks before award.** The supply chain lead checks each supplier's score in the Supplier Performance Risk System. The contracting officer confirms the supplier is not excluded under FAR 52.204-25, and is not named in a FASCSA order under FAR 52.204-30.

**Evidence accepted instead of an answer.** A current certificate can answer the practice questions it covers. KESTREL accepts a CMMC certificate, a SOC 2 Type II report, or an ISO/IEC 27001 certificate. No evidence answers the ownership questions, which every supplier must answer itself.

**Decision.** The supply chain lead reviews each response, and the SCRM team decides one of three outcomes.

- Proceed
- Proceed with conditions, each with an owner and a date
- Do not award

**Tiers.** A supplier's tier comes from what it can reach.

| Tier | Criteria | Examples today | Reassessed |
|---|---|---|---|
| 1 | Reaches the fleet, mission data, or keys, or builds what reaches them | The aircraft manufacturer, both payload vendors, Microsoft, Entrust, CyberArk, Palo Alto Networks, GitLab, JFrog, Keyfactor, the penetration testing provider, and the performer | Every year |
| 2 | Holds security configuration, telemetry, or backups, but no mission data | Atlassian, Splunk, Veeam, NetApp, Cisco, Infoblox, Nozomi Networks, Corelight, the circuit carriers | Every three years |
| 3 | Reaches no KESTREL data | Blancco, the paging service, the time server vendor | Every three years, with a shorter questionnaire |

A supplier moves up a tier when what it can reach grows. The AI/ML Governance Charter may raise an AI supplier's tier further for AI exposures.

**Open-source components.** Open source has no supplier to question or contract with. Its admission runs through the ASP's approved component catalog instead. The supply chain lead watches each admitted product for a change of ownership. Promptfoo is the first case to check, since a larger company acquired it.

---

## 3. Contract Security Requirements

*Traces to GV-3.2.1 and GV-3.2.4.*

**The clause library.** The library holds every security clause KESTREL uses, grouped so each contract carries only what its risk needs. Its full text is in the appendix.

| Clause set | Applies to | Adds |
|---|---|---|
| Base | Every contract | DFARS 252.204-7012, FAR 52.204-25, FAR 52.204-30, and CNSA 2.0 support or an approved exception |
| Software | Any software or software service | SBOM delivery, vulnerability disclosure, and notice of a compromise or a failed audit |
| Hardware | Any hardware or firmware | Firmware signing, sourcing through authorized channels, and DFARS 252.246-7007 and 252.246-7008 for counterfeit parts |
| Tier 1 | Every Tier 1 supplier | DFARS 252.204-7021, right to audit, developer training on the security functions it delivers, screening of the personnel who work on KESTREL components, personnel and data handling terms, and flow-down to subcontractors |
| Specific | One contract each | Payload vendor data rights, path diversity and priority restoration for circuits, onboard trusted execution support, AI red team scope, and the CSSP containment role |

**Acquisition requirements.** Each acquisition also states the security functions the product must provide and the design information the supplier must deliver. It also states the supplier's configuration and supply chain duties. The PMO ISSE writes these from the SADD.

**Checking contracts.** The supply chain lead confirms each contract carries its clause sets at award, and that they flow down to subcontractors. Compliance is checked each year, not only at renewal. A gap becomes a supplier finding.

**CUI on supplier systems.** A supplier that holds KESTREL's CUI on its own systems must meet DFARS 252.204-7012 and NIST SP 800-171. Today those are the performer, whose laptops hold source code, and the penetration testing provider. Before any CUI is shared, the supply chain lead confirms the supplier's SPRS score and its CMMC Level 2 status. The same terms flow to any subcontractor that will hold the CUI.

---

## 4. Supply Chain Risk Assessment and Dependency Mapping

*Traces to GV-3.3.1 and GV-3.3.2. From Phase 2.*

**The assessment.** Each year the supply chain lead assesses every Tier 1 supplier and the products KESTREL depends on most. Each source is examined for:

- Its origin, and where its key parts are made
- Its ownership and control
- Its development and delivery practice
- Its support commitments, and how long they run

Each finding is scored on the risk charter's scale, from likelihood and impact, and not on a separate scale. The assessment is also updated within 30 days of a material change. Examples are a supplier acquisition, a public compromise, or a new Tier 1 supplier.

**The dependency map.** The map traces which suppliers and components each essential function rests on. It takes each function's criticality from the business impact analysis tags in Jira Service Management Assets, rather than rating it again.

**Concentration criteria.** The map flags any of these:

- One supplier behind more than one Tier 1 service
- A component with a single source and no qualified alternative
- A key part made in a country the SCRM team names as a concern
- Any of the above one tier below a direct supplier, found from its questionnaire and SBOMs

**Known concentrations.** Microsoft provides the cloud, the Microsoft 365 tenant, Windows, and the foundation model. The aircraft manufacturer is the single source for the aircraft, stations, and launch equipment. Entrust is the single source for the HSMs. Each is recorded in the map with its treatment.

---

## 5. Sourcing, Inspection, and Firmware Provenance

*Traces to GV-3.4.1, GV-3.4.2, and GV-3.4.4.*

**Sourcing.** KESTREL buys aircraft, stations, and payloads only from their manufacturers. Data center hardware and HSMs come only from the manufacturer or an authorized reseller. A reseller proves its status with the manufacturer's current authorization. A sole-source or obsolete part bought elsewhere needs the SCRM team's approval, a stricter inspection, and a risk acceptance under Risk Acceptance Process (`RK-1.4`).

**Inspection.** Every hardware item is inspected when it arrives, and again when it returns from vendor service.

- Packaging and tamper seals are intact
- Markings and labels match the manufacturer's
- Serial and lot numbers match the order and the manufacturer's records
- Weight, finish, and connectors match a known-good unit

The Platform Team inspects data center hardware from Phase 1. Fleet Operations inspects fleet equipment from Phase 3.

**Rescans.** Under CCSD tailoring action 4, stations and aircraft avionics are rescanned for counterfeit parts each year, at a maintenance window. Parts that entered through vendor service channels since the last scan are the focus.

**Suspect parts.** A suspect part is quarantined at once and is never installed. The supply chain lead reports it to its source, to GIDEP, to the contracting officer, and to the ISSM.

**Firmware.** Firmware comes only from the manufacturer or its authorized channel. Its signature is verified before it is installed. If it is unsigned, its hash is checked against the manufacturer's published value instead. Each verified version is recorded against its device in Jira Service Management Assets.

---

## 6. Component Disposal and Sanitization

*Traces to GV-3.4.5.*

Some components are retired from service, or replaced for a supply chain reason. Each is disposed of so nobody can recover it for resale or study it. Every KESTREL component is CUI.

| Component | Method |
|---|---|
| Drives and storage modules | Purged on site with Blancco to NIST SP 800-88, verified, then shredded |
| HSMs and datalink crypto modules | Zeroized on site, then destroyed through the manufacturer's process |
| Aircraft avionics and station boards | Keys zeroized and storage wiped, then physically destroyed |
| A suspect counterfeit part | Kept as evidence until GIDEP and the source close the report, then destroyed. It is never returned for credit. |

Each disposal is recorded in Jira Service Management Assets with its method and a certificate of destruction.

---

## Appendix: Reference Data and Live Registers

Each item below is living data kept where the team works with it.

**Standard Security Clause Library, full text** *(GV-3.2.1)*: Held in Confluence with the contracting officer and program counsel, organized by the clause sets in Section 3. The four specific clauses the contracting table marks as new are written before their awards.

**Critical Component/Vendor Dependency Map** *(GV-3.3.2, from Phase 2)*: Held in Confluence, with each concentration finding and its treatment.

**Vendor Assessment Findings Register and Supply Chain Risk Finding Register** *(GV-3.1.3, GV-3.3.3)*: Held in Jira. A vendor finding the supplier will not close goes to the steering committee.

**Software/Hardware Supply Chain Risk Assessment, completed report** *(GV-3.3.1, from Phase 2)*: Held in Confluence, updated each year.

**Third-Party Application Registry** *(GV-3.1.4)*: Each self-hosted third-party product's record in Jira Service Management Assets, added once its assessment passes. It links to the supplier's tier and contract rather than restating them.

---

## Approval

**Approved By:** Pending. The ISSM and the PMO ISSE review version 0.1, and the Configuration Control Board approves it in Phase 2.

**Circulated To:** the SCRM team, the contracting officer, the Platform Team, Fleet Operations, the ML Team, and the Security Team.

**Approval Date:** Pending.

---

## Periodic Review and Revision

**Review Cadence:** Annually, as a floor.

**Revision Triggers:**
- A supplier acquisition, ownership change, or public compromise
- A change to a Tier 1 supplier
- A component reaching end of support
- A change in KESTREL's supplier base or dependency map
- A change in contracting rules or the clause library
- A register finding, or a dependency map refresh, that can only close by changing this plan
- A product substitution recorded in the Security Implementation Plan, for any product this document names
