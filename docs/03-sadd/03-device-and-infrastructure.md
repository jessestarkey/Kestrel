# DI: Device and Infrastructure

*KESTREL SADD, Section 5 (Protect). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## DI-1: Asset Management

### DI-1.1: Asset Inventory and Discovery

**Design Intent:** The service desk platform's configuration management database is KESTREL's one asset inventory. The cloud provider's resource inventory feeds it for every spoke. Agents feed it for the data center and the alternate site, with the SDN controller adding the data center's network devices, so nothing depends on manual entry. Every spoke is its own subscription under KESTREL's tenant, and a subscription created outside the landing zone raises an alert. License tracking covers every licensed product and model, such as each payload vendor's conversion software, the service desk platform, and each foundation model's terms of use.

**NIST Control Mapping:**

- **CM-8 (partial):** cited at the base for the authoritative component inventory. Partial because the OT and legacy assets active discovery cannot safely reach are inventoried by OT/Legacy Passive Protocol-Aware Discovery, and the two track CM-8 jointly.
- **CM-8(1) (partial):** carried by Asset Inventory Record, which is updated as assets are provisioned, changed, and retired. Partial because this slice covers the compute, storage, and platform-service estate, while the Application and Artificial Intelligence focus areas hold their own artifact-class slices.
- **CM-8(2) (partial):** carried by Asset Discovery, whose continuous scanning and agent reporting keep the inventory current. Partial on the same asset-class basis as CM-8(1), and not extended to the passive sibling, whose currency depends on observed traffic.
- **CM-8(3) (partial):** cited for active, automated discovery of unmanaged or unauthorized components. Partial because OT/Legacy Passive Protocol-Aware Discovery carries the OT half. Asset Discovery finds unrecorded assets in governed accounts, while Unsanctioned Cloud Account and Landing-Zone Bypass Detection finds the ungoverned accounts themselves.
- **CM-10 (full):** carried by Software License and Usage Restriction Tracking, which tracks license terms, licensed quantities, and peer-to-peer file sharing.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Storage/Database, Device/Workstation, Application/API

**External Dependencies:** The IL5 cloud provider's resource inventory and event interfaces.

**Security Impact:** High

**Activities:**

- **DI-1.1.1: Asset Inventory Record**
    - **Description:** Stand up and continuously maintain the authoritative inventory record of the program's compute, storage, and platform-service assets, capturing each asset's identifying attributes and keeping the record current as assets are provisioned, changed, and retired.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This record carries the outcome's CM-8 (partial) and CM-8(1) (partial) obligations, and downstream Device and Infrastructure capabilities read from it. Asset Discovery feeds it new assets, and Passive Discovery-to-Inventory Reconciliation lands OT and legacy assets in this same record. Level of Effort is High because one record spanning cloud, on-premises, and platform-service estates usually needs a CMDB and custom integration to each source.

- **DI-1.1.2: Asset Discovery**
    - **Description:** Deploy active discovery across every plane the estate spans, namely network scanning and agent-based reporting for addressable hosts, provider resource-inventory and resource-graph APIs or a cloud security posture management platform for cloud-hosted resources, and event-driven subscription to resource-creation events for the ephemeral compute, container, and serverless resources that live and die inside a single scan interval, so any asset absent from the inventory and any unmanaged or unauthorized device surfaces for reconciliation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** These mechanisms carry the outcome's CM-8(3) (partial) and CM-8(2) (partial) mappings, and the devices they surface flow into Asset Inventory Record. Network scanning alone is not enough for a cloud or hybrid estate. Managed services, serverless functions, and short-lived containers are only visible through the provider's resource-inventory API and resource-creation event stream.

- **DI-1.1.3: Unsanctioned Cloud Account and Landing-Zone Bypass Detection**
    - **Description:** Detect cloud subscriptions, accounts, and projects that hold running resources but were never enrolled under the governed landing zone, and route each one for reconciliation into the inventory or for decommissioning, so that no cloud footprint operates outside the program's guardrails.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the cloud slice of the outcome's CM-8(3) (partial) mapping. An unenrolled account is an unauthorized component that Asset Discovery cannot see, since it only queries known accounts. Reconcile the provider's organization or billing hierarchy against the accounts Cloud Landing Zones governs, and secure that organization-level view early. Bring findings under landing-zone governance and into Asset Inventory Record, or drive them into Secure Decommissioning Procedures.

- **DI-1.1.4: Asset Inventory Dashboard**
    - **Description:** Build the dashboard that surfaces inventory coverage, drift between discovered and recorded assets, and the current set of unmanaged or unauthorized devices, giving the security organization an at-a-glance view of inventory completeness.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** It draws on Asset Inventory Record, Asset Discovery, and Discovery Coverage Validation Across OT Segments/Conduits rather than computing anything itself. It is Level 2 because the visualization strengthens rather than establishes ATO posture. Its effort and cost sit a tier below Asset Inventory Record's.

- **DI-1.1.5: Software License and Usage Restriction Tracking**
    - **Description:** Track the software in the asset inventory against its license terms and licensed quantities, prohibit or control peer-to-peer file sharing technology, and remove or license any usage the tracking finds outside its terms.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-10 (full) mapping. Draw the software list from the asset inventory rather than a separate license register. Track open source obligations, such as attribution and source disclosure, alongside commercial entitlements.

### DI-1.2: OT/Legacy Passive Protocol-Aware Discovery

**Design Intent:** Passive sensors on the ground segment network fingerprint the ground control stations, launch and recovery equipment, and payload processing workstation from their own traffic. They never probe a device, so discovery cannot disturb a station during a flight. Aircraft are inventoried by tail number from Fleet Operations' records and reconciled each time one connects to a station. Every sensor reports to the same inventory as the IT estate.

**NIST Control Mapping:**

- **CM-8 (partial):** cited at the base and partial because this outcome inventories the OT and legacy assets that active probes could disrupt. Asset Inventory and Discovery holds the rest, and the two track CM-8 jointly.
- **CM-8(3) (partial):** passive fingerprinting and reconciliation detect unmanaged OT components where active detection cannot run. This is the passive half of CM-8(3), with Asset Inventory and Discovery holding the rest.

**Deployment Type:** On-Premises, Cyber-Physical System (OT/ICS)

**Affected Components:** OT/ICS Device, OT/ICS Passive Network Monitoring

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DI-1.2.1: Passive Sensor/Tap Deployment**
    - **Description:** Deploy passive network taps and monitoring sensors at the OT network segments and conduits, positioned to observe industrial protocol traffic without injecting packets or otherwise interacting with the monitored devices.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** The taps and sensors listen without transmitting, so discovery never adds traffic that could disrupt a control system. Place new sensors as OT segments and conduits are added. One-time cost is High because it covers a protocol-aware monitoring platform plus physical tap or SPAN infrastructure at every segment and conduit.

- **DI-1.2.2: Industrial Protocol-Aware Asset Fingerprinting**
    - **Description:** Configure the passive sensors to parse the industrial protocols in use, such as Modbus, DNP3, and EtherNet/IP, and to fingerprint each observed device's identity, type, and firmware revision where the protocol carries it, building an asset record from communication patterns without ever probing the device.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Fingerprint depth varies by protocol. EtherNet/IP exposes vendor, product, and firmware revision, while Modbus exposes no firmware attribute without an active query. Where passive observation cannot get firmware, source it from engineering records, vendor data, or an OT-approved selective active query. Firmware Version and Patch-Level Baseline Tracking and OT Baseline Configuration Drift Detection depend on that field.

- **DI-1.2.3: Passive Discovery-to-Inventory Reconciliation**
    - **Description:** Reconcile the passively discovered and fingerprinted OT and legacy assets into the authoritative inventory Asset Inventory and Discovery maintains, matching to existing records where they exist and flagging observed-but-unrecorded devices as unmanaged.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is where the outcome's CM-8 (partial) and CM-8(3) (partial) contributions land in the shared inventory. Matching fingerprinted assets to Asset Inventory Record covers the OT inventory share, and flagging unrecorded devices covers OT unauthorized-component detection.

- **DI-1.2.4: Discovery Coverage Validation Across OT Segments/Conduits**
    - **Description:** Continuously compare the documented OT segment and conduit topology against the segments where sensors actually observe traffic, flagging any segment producing no telemetry as a coverage gap so that no OT segment becomes a discovery blind spot.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** It compares the OT topology of record against observed sensor telemetry and flags unmonitored segments, replacing a manual segment-by-segment audit. Gaps drive additional Passive Sensor/Tap Deployment. Establishing the ground-truth topology remains OT-engineering work.

### DI-1.3: Resource Tagging and Ownership Strategy

**Design Intent:** Every asset carries required tags for its owning team, spoke or data center segment, environment, data classification, mission criticality, and end-of-support date. Assets tied to a payload vendor's data rights also carry that vendor's tag, which lets the vendor split be checked from the inventory. The pipeline's policy-as-code checks reject untagged cloud resources at deployment, and Fleet Operations tags fleet equipment when it is received.

**NIST Control Mapping:**

- **CM-8(4) (full):** assigning every asset an accountable owner and keeping that tag current is the accountability information CM-8(4) requires. No other outcome contributes to it.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Device/Workstation, Application/API, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DI-1.3.1: Resource Organization**
    - **Description:** Define how discovered assets are grouped and organized, by environment, business unit, and system boundary, so ownership and policy apply to coherent asset groupings rather than to individual assets one at a time.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity gives owners and tags a coherent grouping but does not itself carry the outcome's CM-8(4) obligation. That is why it is Level 2, while the Tagging Framework and Tagging Enforcement are mandatory. Revisit the scheme as environments, business units, and boundaries change.

- **DI-1.3.2: Tagging Framework**
    - **Description:** Define the tag taxonomy applied to every asset, with required tags for owner, environment, data classification, mission-impact criticality tier, system boundary, and the vendor end-of-life and end-of-support dates for the asset's hardware, operating system, or platform version, which establishes the accountable-owner metadata that satisfies the inventory's accountability-information requirement.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity defines the owner tag that carries the outcome's CM-8(4) obligation, plus environment, classification, criticality, boundary, and end-of-life tags. The criticality tier feeds Risk-Based Prioritization Criteria, so define it in the program's own mission-impact language. The end-of-life and end-of-support dates feed End-of-Life and End-of-Support Refresh Planning, so record them separately where the vendor publishes them separately.

- **DI-1.3.3: Tagging Enforcement**
    - **Description:** Deploy tool-enforced controls that verify required tags are present and current on every asset, blocking or flagging untagged resources so ownership and classification metadata does not decay as assets are provisioned and changed.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** Tool-driven validation keeps the CM-8(4) accountability information from decaying. Time Estimation is Long-term because enforcement must be negotiated with asset-owning teams, the estate back-tagged, and policy run in audit mode before blocking. OT and legacy assets that cannot carry tags keep this metadata on the inventory record instead.

### DI-1.4: Security Team Visibility

**Design Intent:** The Security Team and the CSSP's analysts get read access to the asset inventory, discovery results, and tags, and no right to change them. Inventory and tag data flow into the security monitoring platform, so every alert there carries its asset's owner, team, and criticality. The same data feeds vulnerability prioritization and incident response.

**NIST Control Mapping:**

- **AC-6(1) (partial):** cited for Security Organization Permissions, which authorizes security personnel's access to inventory, discovery, and tagging information. Partial because only this access half of the outcome maps to a control.
- **Declined:** no control is claimed for Operational Security Integration, which routes asset data into Operate pillar workflows that own their own controls. No 800-53 control cleanly fits that interface.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Identity Lifecycle and Governance, Application/API

**External Dependencies:** The CSSP, whose analysts read asset context through the CSSP host pool.

**Security Impact:** Low

**Activities:**

- **DI-1.4.1: Security Organization Permissions**
    - **Description:** Grant security personnel least-privilege but sufficient read and audit access across the asset inventory, discovery, and tagging tooling, giving the security organization the access it needs to monitor the inventory without over-provisioning administrative rights.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is where the outcome's AC-6(1) (partial) mapping lands. Rely on the Identity focus area's access-management and RBAC machinery to enforce the grants. Scope access to read and audit without administrative control, and re-review it as roles change.

- **DI-1.4.2: Operational Security Integration**
    - **Description:** Feed the asset inventory and tagging data into the security organization's operational workflows, namely SOC monitoring, vulnerability management, and incident response, so asset context is available where security operations act on it rather than siloed in the asset-management tooling.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity routes inventory and tagging data into the Operate pillar's SOC, vulnerability-management, and incident-response workflows, which own their own controls. It is the half of the outcome AC-6(1) does not reach. It is Level 2 because it strengthens operations rather than being required for ATO.

## DI-2: Asset Lifecycle

### DI-2.1: Secure Resource Provisioning

**Design Intent:** Every cloud resource is created by infrastructure as code through the shared pipeline from the Platform Team's landing zone modules. Those modules set secure defaults, and policy-as-code checks block a resource that departs from them. A second reviewer approves each infrastructure change, as with application code. Console creation is denied outside break-glass. Data center and alternate site servers are built from the same kind of templates through the configuration automation platform.

**NIST Control Mapping:**

- **CM-6(1) (partial):** cited at the enhancement because Secure-By-Default Provisioning applies secure settings through automated mechanisms such as IaC modules, hardened images, and guardrails. Partial because the ongoing manage and verify dimensions belong to Compute Configuration Monitoring and the other Configuration Policy Orchestration drift outcomes.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Infrastructure-as-Code (IaC)

**External Dependencies:** The parent organization's facility, which hosts the alternate site's equipment under the facility agreement.

**Security Impact:** Moderate

**Activities:**

- **DI-2.1.1: Secure-By-Default Provisioning**
    - **Description:** Configure the provisioning mechanisms, namely infrastructure-as-code modules, hardened base images, and landing-zone guardrails, so every compute, storage, and platform-service resource is created with secure configuration settings applied by default, and document the required secure defaults in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is where the outcome's CM-6(1) (partial) mapping lands. The secure defaults it enforces are documented in the CMP. Drift verification after provisioning belongs to Compute Configuration Monitoring and its Configuration Policy Orchestration siblings.

- **DI-2.1.2: Provisioning Approval Workflows**
    - **Description:** Establish the approval workflow that reviews and authorizes each resource provisioning request, confirming the secure-by-default baseline and required tags are in place before the resource is deployed, and document the approval process in the CMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation. It is the human gate that confirms Secure-By-Default Provisioning's CM-6(1) baseline before deployment. It is event-driven and Level 2 because it strengthens rather than establishes the secure baseline.

### DI-2.2: Asset Lifecycle Change Control

**Design Intent:** A merged pull request is the change record for anything defined as code, and the service desk holds the record for everything else. Each change is tested in the owning team's stage cluster before it reaches production. Changes to the hubs' shared rule base, the identity provider, or a new interconnection go to the Configuration Control Board. Emergency changes run through the privileged access platform and receive a retrospective review within two business days.

**NIST Control Mapping:**

- **CM-3 (partial):** cited at the base because Change Approval Workflow and Emergency Change Process cover the review, approval, documentation, and expedited clauses for compute, storage, and platform-service assets. Partial because the Manage pillar's Configuration Control Board holds the change control element clause.
- **CM-3(2) (full):** carried by Pre-Implementation Change Testing and Validation, which tests and documents an approved change in a non-production environment before finalizing it. Post-Change Configuration Validation is not the carrier, since it checks a change already implemented.
- **CM-4 (partial):** cited at the base for Change Risk Assessment, which analyzes a change's security impact before implementation. Partial because System Prompt Governance holds the prompt slice and Security Impact Analysis (SIA) holds the system-level slice.
- **CM-4(1) (partial):** cited for Pre-Implementation Change Testing and Validation, since analyzing a change in a separate test environment is this enhancement's subject. Partial because the analytical determination stays with Change Risk Assessment under CM-4.
- **Declined:** CM-4(2) is held by Security Impact Analysis (SIA) through Post-Change Control Verification, while this capability validates against the secure baseline rather than per control.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Storage/Database, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DI-2.2.1: Change Approval Workflow**
    - **Description:** Establish the change approval workflow that routes every proposed change to a provisioned asset through review and documented approval or disapproval before implementation, send escalations and standing oversight to the Manage pillar's Configuration Control Board, and document the workflow in the CMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This is where the outcome's CM-3 (partial) base obligation lands, namely the review, approval, and documentation of changes to provisioned assets. It consumes Change Risk Assessment's analysis as an input. It is event-driven because approvals happen per change request.

- **DI-2.2.2: Change Risk Assessment**
    - **Description:** Analyze each proposed change for its potential security impact, including affected components, blast radius, and control implications, before implementation, and document the impact-analysis criteria and results in the CMP so the approval decision rests on an assessed risk.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity performs the outcome's CM-4 (partial) impact analysis before a change is implemented, scoped to compute, storage, and platform-service assets. Its output feeds Change Approval Workflow and the system-level Security Impact Analysis (SIA). Pre-Implementation Change Testing and Validation then checks the prediction against a real execution, which is why CM-4(1) sits there.

- **DI-2.2.3: Pre-Implementation Change Testing and Validation**
    - **Description:** Exercise each approved change in a non-production or staging environment representative of the target configuration, confirm it produces the intended result without breaking a dependent function or weakening a security control, and record the test evidence in the change record before the change is finalized in production.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the whole of the outcome's CM-3(2) (full) mapping and its CM-4(1) (partial) mapping. Hold the staging environment to the same Baseline Configuration Standards definitions as production, or the test predicts nothing. Where a change cannot be tested outside production, record a documented exception with the compensating verification performed. Security patches instead follow Patch Testing, Staged Rollout, and Rollback.

- **DI-2.2.4: Post-Change Configuration Validation**
    - **Description:** Validate after implementation that each change applied as intended and that the asset still conforms to its secure baseline by running post-change configuration and compliance checks, and capture the result in the change record before closing it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's CM-3 (partial) mapping by supplying the evidence that closes a change record. It does not carry CM-3(2), since it runs after the change reaches the asset. It validates against the baseline Secure-By-Default Provisioning establishes and Baseline Configuration Standards maintains.

- **DI-2.2.5: Emergency Change Process**
    - **Description:** Define the expedited change path for urgent changes that cannot wait for the standard approval cycle, requiring documented justification at implementation and mandatory retrospective review and impact analysis afterward, and document the emergency-change criteria and after-the-fact review requirement in the CMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This is the emergency variant of change control, carrying part of the outcome's CM-3 (partial) obligation. It cites the base because no CM-3 enhancement covers expedited changes. The retrospective review reuses Change Approval Workflow and Change Risk Assessment after implementation, and the Configuration Control Board's out-of-cycle path brings the change to the board.

### DI-2.3: Resource Decommissioning Governance

**Design Intent:** Cloud resources are removed through the same infrastructure as code that created them. Removal revokes their workload identities and deletes their spoke vault secrets and encryption keys. Data center drives are sanitized on site before they leave, and HSMs are zeroized. An aircraft or ground control station leaving service has its keys zeroized and its onboard storage wiped. Orphaned resources are those whose owning team or tag no longer resolves. Refresh planning tracks the payload processing workstation's replacement against its 2027-09-30 deadline, and a slip goes to the AO before the workstation connects.

**NIST Control Mapping:**

- **MP-6 (partial):** cited at the base for wiping a retired resource so no residual data survives. Partial because it covers compute, storage, and platform-service resources rather than all physical media, and access reclamation relies on the Identity focus area's deprovisioning controls.
- **MP-6(1) (partial):** covers the governed review, approval, tracking, documentation, and verification of each sanitization, carried by Secure Decommissioning Procedures. Partial for the same two reasons as MP-6.
- **CM-8 (partial):** cited at the base for Orphaned Resource Detection, which clears recorded resources that have outlived their owner or purpose. Partial, and independent of the discovery outcomes' CM-8 claim, which targets unrecorded components instead.
- **SA-22 (partial):** carried by End-of-Life and End-of-Support Refresh Planning, the framework's only claim on SA-22. Partial because replacement runs through Secure Resource Provisioning and Secure Decommissioning Procedures, while Unpatchable/Legacy Asset Compensating Controls supplies the mitigations a justification record points to.
- **Declined:** CM-8(3) belongs to the Asset Management discovery outcomes, and CM-8(4) belongs in full to Resource Tagging and Ownership Strategy.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Application/API, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DI-2.3.1: Secure Decommissioning Procedures**
    - **Description:** Establish the procedure that securely retires a resource by sanitizing or wiping its storage so no residual data remains, deallocating it, and reclaiming the identities, keys, and network access it held, and that tracks, documents, and verifies each retirement, and document the decommissioning and sanitization requirements in the CMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The outcome's MP-6 (partial) and MP-6(1) (partial) mappings land here, covering the sanitization and its governance. Scope is the logical teardown of compute, storage, and platform-service resources, while identity, key, and network access reclamation runs through the Identity focus area's deprovisioning controls. It is event-driven because it runs per retirement.

- **DI-2.3.2: Orphaned Resource Detection**
    - **Description:** Deploy tool-driven detection that continuously scans the inventory for resources that still exist but have lost a valid owner, purpose, or business justification, such as stale, unattributed, or long-idle resources, route each finding to an owner for reconciliation or into the decommissioning procedure, and document the orphaned-resource criteria and disposition in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity delivers the outcome's independent CM-8 (partial) mapping by scanning for unowned, purposeless, or idle resources. Reconcile each finding to an owner using Resource Tagging and Ownership Strategy metadata, or drive it into Secure Decommissioning Procedures. It is Level 2 because it strengthens accountability rather than gating ATO.

- **DI-2.3.3: End-of-Life and End-of-Support Refresh Planning**
    - **Description:** Forecast which assets are nearing the vendor end-of-life and end-of-support dates on their inventory tags, drive each into a refresh, upgrade, or preemptive-isolation workflow early enough for the work to be funded and scheduled, and record in the CMP the justification, offsetting controls, and approving authority for any component authorized to stay in service after support ends.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-22 (partial) mapping. Its input is the end-of-support date the Tagging Framework requires, so watch for assets where that date was never populated. Set the forecast lead time from how long a refresh actually takes, often quarters. Where a component must stay in service unsupported, the justification names the offsetting controls from Unpatchable/Legacy Asset Compensating Controls.

### DI-2.4: Controlled Maintenance and Support

**Design Intent:** Data center and alternate site hardware maintenance is scheduled through the service desk, escorted, and recorded, and failed drives stay on site for sanitization. Fleet Operations maintains the ground control stations and launch equipment only in scheduled windows, with vendor sessions brokered and recorded under Access Process for Third-Party Support (`ID-4.7`). Diagnostic tools and media are approved and scanned before use. Spare stations and aircraft parts cover the mission's tolerance, and they double as the test articles for penetration testing.

**NIST Control Mapping:**

- **MA-1 (partial):** the procedures half of the maintenance policy requirement, with the policy tier held by the Governance focus area's Security Policy Framework.
- **MA-2 (partial):** controlled maintenance for the IT estate, including records, approvals, component removal, media sanitization, and post-maintenance checks. Partial because OT/Legacy Scheduled Maintenance-Window Access holds the OT and legacy slice.
- **MA-3 (full):** carried by Maintenance Tool Approval and Control, which approves, controls, monitors, and periodically reviews maintenance tools across the program.
- **MA-3(1) (partial):** inspecting maintenance tools brought into IT facilities. Partial because OT/Legacy Scheduled Maintenance-Window Access holds the OT and legacy slice.
- **MA-3(2) (partial):** checking diagnostic media for malicious code before use on IT assets.
- **MA-3(3) (full):** preventing removal of maintenance equipment holding program information without sanitization, destruction, or exemption, for every asset class.
- **MA-6 (full):** obtaining maintenance support and spare parts within a defined time of failure.
- **Declined:** MA-4 is held by Access Process for Third-Party Support, and MA-5 by OT/Legacy Scheduled Maintenance-Window Access, while escort of uncleared maintainers is the PSO's.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Device/Workstation, OT/ICS Device

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider maintains the cloud hardware. The aircraft and ground equipment manufacturers provide support under their maintenance agreements.

**Security Impact:** Moderate

**Activities:**

- **DI-2.4.1: Maintenance Procedures Documentation**
    - **Description:** Document the program's procedures for maintaining IT assets, covering scheduling, approval, on-site and off-site repair, component removal and sanitization, and post-maintenance checks, and record them in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's MA-1 (partial) mapping for the procedures half. The procedures sit in the Configuration Management Plan (CMP), because maintenance is a change to the estate and runs through the same records.

- **DI-2.4.2: Controlled Maintenance Scheduling, Approval, and Records**
    - **Description:** Schedule, approve, and record every maintenance action on IT assets, approve any removal of a component from the facility and sanitize its media first, and confirm afterward that the controls the maintenance touched still function.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's MA-2 (partial) mapping. Sanitize removed media under the Data focus area's Media Protection Policy and Procedures, and destroy failed storage locally in classified environments. Maintenance that changes configuration goes through Security Impact Analysis (SIA) and its Post-Change Control Verification.

- **DI-2.4.3: Support Agreements and Spare Parts**
    - **Description:** Identify the components whose failure the mission cannot absorb, and hold support agreements and spare parts that restore each within a defined time of failure derived from the program's recovery objectives.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's MA-6 (full) mapping. Set restoration times from Recovery Objective Definition (RTO/RPO), and keep a spare on hand where a support agreement cannot meet them. Isolated environments usually need more spares on site.

- **DI-2.4.4: Maintenance Tool Approval and Control**
    - **Description:** Maintain the list of approved maintenance and diagnostic tools, inspect tools and test media brought into IT facilities before use, and prevent any maintenance equipment holding program information from leaving the facility unless it has been sanitized or destroyed or an exemption has been approved.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's MA-3 (full), MA-3(1) (partial), MA-3(2) (partial), and MA-3(3) (full) mappings. A diagnostic laptop is the likeliest thing to cross a classified boundary, so the exit check matters as much as entry inspection. OT entry inspection stays with Maintenance Tool and Diagnostic Equipment Inspection.

## DI-3: Baseline Configuration Standards

### DI-3.1: Secure Configurations

**Design Intent:** DISA STIGs and SRGs are the hardening basis, with the Cloud Computing SRG's IL5 requirements for the cloud. The landing zone defines the hub and ten spokes as subscriptions under one tenant, each with its own guardrail policies. The Platform Team's infrastructure as code modules encode that design, so a new spoke is built the same way as the existing ten. Both hubs, the access proxy, the VDI brokers, and the cross domain transfer gateway fail closed.

**NIST Control Mapping:**

- **CM-2 (partial):** cited at the base for the baseline framework and methodology, namely the reference architecture, hardening frameworks, landing zones, and IaC. Partial because Secure Compute Baselines and the other sibling outcomes claim CM-2 independently for their own asset classes.
- **CM-2(2) (partial):** carried by Infrastructure-as-Code (IaC) Templates, since a version-controlled repository keeps the baseline current, complete, and available automatically. Partial because it reaches only what the templates express. The IT baseline siblings inherit this enhancement rather than claiming it again.
- **SC-24 (full):** carried by Fail-Secure State Definition, which defines the known failure state for each component class and preserves recovery state information.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Infrastructure-as-Code (IaC)

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.

**Security Impact:** High

**Activities:**

- **DI-3.1.1: Architecture Frameworks**
    - **Description:** Adopt and document the program's secure reference architecture, namely the authoritative set of architectural patterns, trust boundaries, and design standards the program's secure baselines are built to conform to.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity, with Configuration Frameworks, establishes the basis for the outcome's CM-2 (partial) mapping. Cloud Landing Zones and Infrastructure-as-Code (IaC) Templates encode its intent. It is event-driven because the architecture is revised as the technology stack evolves.

- **DI-3.1.2: Configuration Frameworks**
    - **Description:** Select, tailor, and document the configuration-hardening frameworks the program's baselines derive from, such as CIS Benchmarks and DISA STIGs, as the authoritative source of the hardening settings each concrete baseline applies, and record the adopted framework and its tailoring in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-2 (partial) mapping alongside Architecture Frameworks, supplying the hardening source each baseline outcome applies. Automated application and scanning live in Secure Resource Provisioning and Configuration Policy Orchestration. It is event-driven because new benchmark and STIG versions are adopted on release.

- **DI-3.1.3: Cloud Landing Zones**
    - **Description:** Define and build the cloud landing zone architecture, namely the hardened account, subscription, and network scaffolding with policy-as-code guardrails, so new cloud resources deploy already inside a governed security boundary.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** The guardrails are policy-as-code that continuously enforces the boundary new resources land in, and Secure-By-Default Provisioning applies them at creation. This activity is cloud-only, while its siblings also cover on-premises, hybrid, and air-gapped deployments.

- **DI-3.1.4: Infrastructure-as-Code (IaC) Templates**
    - **Description:** Build the infrastructure-as-code template mechanism that encodes the adopted reference architecture, configuration frameworks, and landing zone decisions as version-controlled, repeatable, deployable infrastructure definitions.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-2(2) (partial) mapping, and the four IT baseline siblings inherit it. Secure-By-Default Provisioning consumes these modules, and the baseline outcomes produce the images that ride on them. Treat the repository as the authoritative baseline, so any out-of-band change is reconciled back into the templates.

- **DI-3.1.5: Fail-Secure State Definition**
    - **Description:** Define for each component class the known secure state it fails to on the failures the program identifies, configure components to reach that state and preserve the state information needed for recovery, and verify the behavior before relying on it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-24 (full) mapping. It is Level 2 because SC-24 is in the High baseline only, and it is mandatory where the program's baseline is High. Where failing secure conflicts with failing safe in OT, resolve it with Manual/Fail-Safe Operational Fallback Readiness.

### DI-3.2: Secure Compute Baselines

**Design Intent:** One VDI golden image serves every host pool, and each pool adds only its own tools. Virtual machine images cover the experimentation workspaces, the payload vendors' conversion servers, and the data center's other servers. Container base images are hardened and minimal, built from the package mirror, and rebuilt rather than patched in place. Every managed Kubernetes cluster shares one baseline, whether it is a dev, test, stage, prod, or training cluster. BMC hardening applies to the physical servers in the data center and at the alternate site.

**NIST Control Mapping:**

- **CM-2 (partial):** the golden images and orchestration baseline for compute assets. Partial because Secure Configurations, Secure Storage Baselines, Secure Platform Services and Application Baselines, and the OT outcome each claim CM-2 independently for their own scope.
- **CM-6 (partial):** carried by Baseboard Management Controller (BMC) Hardening, which applies the controller's documented secure settings. Partial and cited at the base because controllers are configured through their own interface rather than the automated pipeline CM-6(1) describes.
- **CM-7 (partial):** hardening each compute baseline to mission-essential services, ports, and software is CM-7's base intent. Partial because Unapproved Service Usage Monitoring and Alerting holds CM-7(1) and Execution and Device Control holds CM-7(2) and CM-7(5).
- **IA-5 (partial):** carried by Baseboard Management Controller (BMC) Hardening, for replacing each controller's vendor-default authenticator. Partial and cited at the base since the change-default-authenticators obligation is the base requirement.
- **Declined:** CM-2(2) is inherited from Infrastructure-as-Code (IaC) Templates rather than claimed twice. CM-6(1) drift checking is Compute Configuration Monitoring's.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Virtual Machine/Server, Container, Container Orchestration Control Plane, Virtual Desktop Infrastructure (VDI), Application/API

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider hardens the cloud's physical hosts and their management controllers.

**Security Impact:** High

**Activities:**

- **DI-3.2.1: Virtual Desktop Golden Image**
    - **Description:** Build and harden the golden image for the program's virtual desktop infrastructure, applying the adopted configuration-hardening framework and removing unnecessary services, software, and ports, and maintain it as the authoritative VDI baseline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity delivers a hardened, least-functionality baseline for the virtual desktop form factor, contributing to the outcome's CM-2 (partial) and CM-7 (partial) mappings.

- **DI-3.2.2: Virtual Machine Golden Images**
    - **Description:** Build and harden the golden base images for the program's server and workload virtual machines, one per approved OS platform, applying the configuration-hardening framework, stripping each to only mission-essential functionality, and maintaining them as the authoritative VM baselines.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** These images contribute to the outcome's CM-2 (partial) and CM-7 (partial) mappings for the virtual-machine form factor, and Secure-By-Default Provisioning deploys them. Re-baseline them as OS releases, framework versions, and patches require.

- **DI-3.2.3: Container Golden Images**
    - **Description:** Build and harden the program's base container images as minimal, framework-conformant images with unnecessary packages, shells, and services removed, from which application images are layered, and maintain them as the authoritative container baselines in the trusted registry.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** These base images contribute to the outcome's CM-2 (partial) and CM-7 (partial) mappings for containers, applying least functionality at the image layer. Build-time scanning belongs to the Application focus area and Configuration Policy Orchestration. Provenance comes from the Application focus area's Image Signing outcome, an inheritance that does not extend to the VM or virtual desktop images.

- **DI-3.2.4: Container Orchestration Secure Baselines**
    - **Description:** Define the secure baseline for the container orchestration platform, covering the hardened control-plane and node configuration, Pod Security Standards, default network policies, and RBAC defaults for the program's clusters, and maintain it as the authoritative orchestration baseline, such as a hardened Kubernetes configuration.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This baseline contributes to the outcome's CM-2 (partial) and CM-7 (partial) mappings for the orchestration platform. It defines the cluster baseline, while the Application focus area's Policy-as-Code Evaluation outcome enforces it at admission time.

- **DI-3.2.5: Baseboard Management Controller (BMC) Hardening**
    - **Description:** Bring the out-of-band management controllers in the program's physical compute hardware, namely iDRAC, iLO, IPMI, and Redfish interfaces, under a documented baseline that replaces every vendor-default credential, disables unneeded and legacy network-facing services, and binds each interface to a dedicated management network rather than one carrying production traffic, and maintain that definition as the authoritative BMC baseline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-6 (partial) and IA-5 (partial) mappings and contributes to CM-2 (partial). A management controller runs below the host OS and can reimage the host, so a default credential there is a whole-host compromise. Isolate the management plane through High-Risk Workload Isolation, and patch controller firmware through Patching and Updates. It does not apply to cloud-hosted compute.

### DI-3.3: Secure Storage Baselines

**Design Intent:** Every cloud database and storage service disables public access, accepts connections only from private endpoints in its own spoke, and sends access logs to the security monitoring platform. On premises, each data lake zone's access policy admits only its own team's workloads, the Data Team, and the ML training zone where F18 allows. The backup repository is reachable only from the backup service.

**NIST Control Mapping:**

- **CM-2 (partial):** covers secure defaults for cloud object, file, and database services, and their on-premises and self-hosted equivalents. Partial because Secure Configurations and the other baseline outcomes claim CM-2 independently for their own scope.
- **Declined:** CM-2(2) is inherited from Infrastructure-as-Code (IaC) Templates. CM-6(1) live conformance belongs to Storage Configuration Monitoring. CM-7 does not fit, since these baselines govern settings and exposure rather than stripping functions.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Database Service, Object/File Storage

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **DI-3.3.1: Cloud Storage Secure Baselines**
    - **Description:** Define and maintain the secure baseline configuration for the program's cloud object and file storage services, which blocks public access by default, enforces private network isolation, and enables access and audit logging, as the authoritative storage-service baseline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This baseline contributes to the outcome's CM-2 (partial) mapping for object and file storage. Data encryption belongs to the Data focus area's Default Data at Rest Encryption. Revise the baseline as provider features and the adopted framework change.

- **DI-3.3.2: Cloud Database Secure Baselines**
    - **Description:** Define and maintain the secure baseline configuration for the program's managed database services, which disables public network exposure, enforces private connectivity and firewall restrictions, and enables native audit and diagnostic logging, as the authoritative database-service baseline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This baseline contributes to the outcome's CM-2 (partial) mapping for managed databases. Enable native audit and diagnostic logging as a default, with the Operate pillar handling analysis. Transparent data encryption belongs to Default Data at Rest Encryption.

- **DI-3.3.3: On-Premises Storage Secure Baselines**
    - **Description:** Harden the program's on-premises file and block storage into a documented baseline that scopes share and export permissions to named hosts and identities, removes anonymous and legacy-protocol access paths, confines the array's management interfaces to the management network, and enables file-access audit logging, and maintain it as the authoritative on-premises storage baseline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This baseline contributes to the outcome's CM-2 (partial) mapping for on-premises file and block storage. Export lists, authentication, and legacy protocol versions are set on the array, so state each explicitly. Volume encryption, owned by Default Data at Rest Encryption, does not substitute for a correct export list.

- **DI-3.3.4: On-Premises Database Secure Baselines**
    - **Description:** Establish the hardening standard for the program's self-hosted database instances, covering removal of default and sample accounts, schemas, and demonstration databases, least-privilege role and object grants, restriction of the listener and its network exposure to authorized application hosts, and enablement of the engine's native audit logging, and maintain it as the authoritative self-hosted database baseline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This baseline contributes to the outcome's CM-2 (partial) mapping for self-hosted databases. Self-hosted engines arrive with permissive defaults, so state audit logging, network restriction, and account hygiene explicitly. Do not defer native audit logging, since the engine alone sees privileged queries. Encryption belongs to Default Data at Rest Encryption.

### DI-3.4: Secure Platform Services and Application Baselines

**Design Intent:** Platform service baselines cover every managed service, such as the spoke secrets vaults, the feedback endpoints' queues and functions, the database services, and each foundation model deployment. Every foundation model deployment's baseline requires a private endpoint and provider-side prompt logging disabled. Where the provider grants that as an approved exemption rather than a setting, the approval is the baseline's evidence. Application baselines cover how the mission teams' applications are hosted, and COTS products such as the service desk platform and the payload vendors' conversion software follow their vendors' guidance.

**NIST Control Mapping:**

- **CM-2 (partial):** covers secure defaults for managed platform services and application-hosting configuration. Partial because Secure Configurations and the other baseline outcomes claim CM-2 independently for their own scope.
- **CM-7 (partial):** disabling unneeded platform features, public endpoints, sample content, and management interfaces is least functionality at the platform layer. Partial alongside Secure Compute Baselines, with CM-7(1) review held by Unapproved Service Usage Monitoring and Alerting.
- **Declined:** CM-2(2) is inherited from Infrastructure-as-Code (IaC) Templates. CM-6(1) live conformance belongs to Platform Services and Application Configuration Monitoring.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** First-Party/Custom Application Code, Self-Hosted Third-Party Application (COTS), Serverless/Platform Service

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. Payload Vendor B publishes the deployment guidance for its conversion software.

**Security Impact:** Moderate

**Activities:**

- **DI-3.4.1: Cloud Platform Services Secure Baselines**
    - **Description:** Define and maintain the secure baseline configurations for the program's managed cloud platform services, namely PaaS offerings, serverless functions, and managed integration and messaging services, disabling unnecessary features and default public endpoints and enforcing least-privilege service settings and private connectivity, as the authoritative platform-service baselines.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** These baselines contribute to the outcome's CM-2 (partial) and CM-7 (partial) mappings for managed platform services. This activity is cloud-only, unlike the outcome as a whole. Revise it as provider features and the adopted framework change.

- **DI-3.4.2: Secure Application Baselines**
    - **Description:** Define and maintain the secure infrastructure- and runtime-configuration baseline for how applications are deployed on their hosting platform, covering hardened application-server, web-server, and runtime settings, disabled sample and default content, and restricted management interfaces, as the authoritative application-hosting baseline for both applications the program builds and self-hosted third-party or COTS applications it deploys and operates, distinct from the Application focus area's code-level security controls.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This baseline contributes to the outcome's CM-2 (partial) and CM-7 (partial) mappings for application hosting. Its scope is deployment and runtime configuration, not code, which the Application focus area governs. It applies equally to self-hosted COTS products and across all four environments.

### DI-3.5: Secure OT/Legacy Device Baselines

**Design Intent:** Fleet Operations adopts each manufacturer's hardening guidance for the ground control stations, launch and recovery equipment, and aircraft. An asset that cannot be hardened to a current baseline gets a compensating control baseline instead. The payload processing workstation would get one only if it connects before its replacement fields. It would then run isolated in the OT zone with application allow-listing, per CCSD tailoring action 3. Approved firmware for each aircraft and station model is tracked in the inventory.

**NIST Control Mapping:**

- **CM-2 (partial):** covers vendor hardening, compensating-control, and firmware baselines for OT and legacy devices. Partial because the other baseline outcomes claim CM-2 independently. For a device that holds no configuration, the baseline is the required controls around it.
- **Declined:** CM-2(2) needs an automated mechanism these devices cannot host, which also keeps OT Baseline Configuration Drift Detection at CM-6 rather than CM-6(1). CM-7 is not claimed because the vendor guide is adopted wholesale. CM-8 stays with the discovery outcomes and Orphaned Resource Detection.

**Deployment Type:** On-Premises, Cyber-Physical System (OT/ICS)

**Affected Components:** OT/ICS Device, OT/ICS Zone-Conduit Segmentation (IEC 62443), OT/ICS Passive Network Monitoring

**External Dependencies:** The aircraft and ground equipment manufacturers, for hardening guidance and approved firmware. Payload Vendor A, which certifies its conversion software only on the workstation's current operating system.

**Security Impact:** Moderate

**Activities:**

- **DI-3.5.1: OT/ICS Vendor Hardening Guide Adoption**
    - **Description:** Adopt and document the OT and ICS device vendors' own published, device- and model-specific hardening guides as the authoritative secure baseline for each OT and legacy device that can be configured directly, in place of the generic CIS and STIG benchmarks the IT-asset baselines derive from, and record the adopted guides in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-2 (partial) mapping for OT and legacy devices that can be hardened directly. Use the vendor's guide rather than a generic benchmark, which could disable functions the process depends on. Unconfigurable devices go to Compensating Control Baseline Definition.

- **DI-3.5.2: Compensating Control Baseline Definition**
    - **Description:** Define and document the baseline of compensating controls required around each OT and legacy device that cannot be hardened or configured directly at all, namely network-layer isolation, gateway-based protection, and passive monitoring, to stand in for the device-level baseline the device itself cannot support, and record the baseline in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-2 (partial) mapping for devices that cannot be hardened or modified. It documents the required controls around the device, drawing on OT/Legacy Passive Protocol-Aware Discovery and OT/Legacy Device Identity Controls rather than redefining them.

- **DI-3.5.3: Firmware Version and Patch-Level Baseline Tracking**
    - **Description:** Establish and maintain the approved firmware version and patch level for each OT and legacy device model as a documented baseline, separate from applying the patches themselves, so downstream drift and compliance monitoring has a known-good version standard to check actual devices against, and record the baseline in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's CM-2 (partial) mapping, since the approved firmware level is a configuration baseline rather than a CM-8 concern. OT/ICS Vendor-Validated Patch Remediation applies updates toward this target. OT Baseline Configuration Drift Detection confirms devices reached it.

## DI-4: Configuration Policy Orchestration

### DI-4.2: Policy Service Restrictions

**Design Intent:** The permitted services, ports, and protocols for each asset type are set in the CMP and enforced twice. Host firewalls enforce them on every KESTREL-owned host, and the hubs' shared rule base enforces them on the network. The scope is every spoke, the data center, the privileged access workstations, and the VDI desktops. Fleet equipment follows its manufacturer's service list.

**NIST Control Mapping:**

- **CM-7 (partial):** cited at the base for the ongoing, environment-wide policy on which services, ports, and protocols may run on live assets. Partial and independent of the definition-time CM-7 claims held by Secure Compute Baselines and Secure Platform Services and Application Baselines.
- **Declined:** CM-7(1) review belongs to Unapproved Service Usage Monitoring and Alerting, and CM-7(2) and CM-7(5) belong to Execution and Device Control.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Device/Workstation, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DI-4.2.1: Service Restriction Policy Framework**
    - **Description:** Define the program's service restriction policy, namely the permitted set of network-facing and operating-system-level services, ports, and protocols and the prohibited or nonsecure ones, and document it as the authoritative least-functionality standard in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This framework is the policy the outcome's CM-7 (partial) mapping rests on, derived from the Baseline Configuration Standards service sets. Unapproved Service Detection reviews live assets against it. Revise it as approved services, protocols, and mission needs change.

- **DI-4.2.2: Policy Scope and Enforcement**
    - **Description:** Determine which asset classes and environments the service restriction policy binds to and which enforcement points apply it, namely host-based firewalls, service managers, and platform service controls, and document that scope and enforcement approach in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity completes the outcome's CM-7 (partial) mapping by fixing where the policy applies and through which enforcement mechanisms. Unapproved Service Usage Monitoring and Alerting reviews live assets against that scope. Revise it as the asset footprint and enforcement options change.

### DI-4.3: Unapproved Service Usage Monitoring and Alerting

**Design Intent:** Vulnerability scans and cloud configuration checks look for services running outside the CMP's permitted list. Findings alert in the security monitoring platform and open a service desk ticket to the asset's owning team. A finding on a DMZ-facing or Tier 0 asset goes to the Security Team at once.

**NIST Control Mapping:**

- **CM-7(1) (partial):** cited at the enhancement because reviewing the live environment for unnecessary or nonsecure functions is CM-7(1)'s subject. Partial because this outcome reviews, identifies, and alerts, while disabling flagged services runs through response and patch content. The Network and Environment and Application focus areas hold the other surfaces of this enhancement.
- **Declined:** CM-7(2) and CM-7(5) belong to Execution and Device Control.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Device/Workstation, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **DI-4.3.1: Unapproved Service Detection**
    - **Description:** Periodically scan the live environment to enumerate running services, listening ports, and installed software on the program's assets and flag any that fall outside the service restriction policy as unnecessary, nonsecure, or unapproved.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is the review-and-identify dimension of the outcome's CM-7(1) (partial) mapping. It scans services, ports, and software against the policy Policy Service Restrictions maintains, and Alert and Response Workflows acts on what it flags.

- **DI-4.3.2: Alert and Response Workflows**
    - **Description:** Route the out-of-policy services Unapproved Service Detection flags into automated alerts and a defined response and disposition workflow, and document the severity thresholds and disposition steps in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the alerting-and-routing dimension of the outcome's CM-7(1) (partial) mapping. It turns a flagged service into an owned disposition, while responders and remediation content perform the actual removal. Severity thresholds and disposition steps are documented in the CMP.

### DI-4.4: Compute Configuration Monitoring

**Design Intent:** Configuration scans compare every virtual machine, VDI desktop, and cluster against its baseline, and admission control rejects workloads that depart from the cluster baseline. Drift alerts go to the owning team and the Security Team. A compute compliance dashboard shows posture by team and spoke for the Platform Team, the Security Team, and the CSSP.

**NIST Control Mapping:**

- **CM-6(1) (partial):** cited at the enhancement because automated scanning of live compute against its baseline is CM-6(1)'s manage-and-verify function. Partial because it is the compute member of a joint claim with Secure Resource Provisioning, Storage Configuration Monitoring, and Platform Services and Application Configuration Monitoring.
- **Declined:** CM-2 stays with Secure Compute Baselines, and CM-7 stays with that capability and Unapproved Service Usage Monitoring and Alerting, since this outcome only measures against them.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Virtual Machine/Server, Container, Container Orchestration Control Plane, Virtual Desktop Infrastructure (VDI), Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DI-4.4.1: Compute Baseline Drift Detection and Alerting**
    - **Description:** Continuously scan the program's live virtual desktops, virtual machines, containers, and orchestration platform against their documented Secure Compute Baselines and raise an alert whenever a running asset's configuration has drifted from the baseline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is where the verify dimension of the outcome's CM-6(1) (partial) mapping lands for compute. It scans the live fleet against the baseline Secure Compute Baselines maintains, and Compute Configuration Compliance Dashboard/Reporting tracks the drift.

- **DI-4.4.2: Compute Configuration Compliance Dashboard/Reporting**
    - **Description:** Build and maintain a dashboard that surfaces the compute fleet's configuration-compliance posture, namely per-asset baseline conformance, open drift findings, and remediation status, as a single view for the PMO ISSE and asset owners.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** It reports the drift Compute Baseline Drift Detection and Alerting produces rather than scanning itself. It is Level 2 because the detection activity meets the mandatory obligation. Level of Effort is Low because it is a reporting view over existing findings.

### DI-4.5: Storage Configuration Monitoring

**Design Intent:** Cloud configuration checks watch every cloud database and storage service for public access, disabled logging, or a loosened resource firewall. On premises, each data lake zone's access policy is compared against its baseline, so access that crosses the vendor split is caught. Findings feed a storage compliance dashboard.

**NIST Control Mapping:**

- **CM-6(1) (partial):** cited at the enhancement because continuous checking of live storage and database services against baseline is CM-6(1)'s manage-and-verify function. Partial as the storage member of the joint claim with Secure Resource Provisioning and the compute and platform monitoring outcomes.
- **Declined:** CM-2 stays with Secure Storage Baselines, since this outcome only measures against it.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Database Service, Object/File Storage

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DI-4.5.1: Storage Baseline Drift Detection and Alerting**
    - **Description:** Continuously scan the program's cloud object storage, file storage, and managed database services against their documented Secure Storage Baselines and alert whenever a service has drifted toward public exposure, lost network isolation, or had audit logging disabled.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is where the verify dimension of the outcome's CM-6(1) (partial) mapping lands for storage and database services. It checks each service against the baseline Secure Storage Baselines maintains, excluding encryption. Storage Configuration Compliance Dashboard/Reporting surfaces the drift.

- **DI-4.5.2: Storage Configuration Compliance Dashboard/Reporting**
    - **Description:** Build and maintain a dashboard that surfaces the configuration-compliance posture of the program's storage and database services, namely per-service baseline conformance, public-exposure and logging findings, and remediation status, as a single view for the PMO ISSE and service owners.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** It reports the findings Storage Baseline Drift Detection and Alerting produces rather than scanning itself. It is Level 2 because the detection activity carries the mandatory verify obligation.

### DI-4.6: Platform Services and Application Configuration Monitoring

**Design Intent:** Cloud configuration checks watch every platform service against its baseline. The check with the highest priority is a re-enabled public endpoint on any foundation model deployment. Provider-side prompt logging is confirmed off each year where these checks cannot read it. The same checks cover how each application is hosted, and findings appear on the platform and application compliance dashboard.

**NIST Control Mapping:**

- **CM-6(1) (partial):** cited at the enhancement because automated evaluation of live platform and hosting configuration against baseline is CM-6(1)'s manage-and-verify function. Partial as the platform member of the joint claim with Secure Resource Provisioning and the compute and storage monitoring outcomes.
- **Declined:** CM-2 and CM-7 stay with Secure Platform Services and Application Baselines and Unapproved Service Usage Monitoring and Alerting, since this outcome only evaluates against them.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Serverless/Platform Service, First-Party/Custom Application Code, Self-Hosted Third-Party Application (COTS)

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider exposes the configuration state these checks read.

**Security Impact:** Moderate

**Activities:**

- **DI-4.6.1: Platform/Application Baseline Drift Detection and Alerting**
    - **Description:** Continuously scan the program's managed platform services, PaaS and serverless offerings, and application-hosting configuration against their documented Secure Platform Services and Application Baselines and alert whenever a live configuration has drifted, such as a re-enabled public endpoint or a loosened platform-service setting.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is where the verify dimension of the outcome's CM-6(1) (partial) mapping lands for platform services and application hosting. It checks against the baseline Secure Platform Services and Application Baselines maintains, excluding application code. Platform/Application Configuration Compliance Dashboard/Reporting surfaces the drift.

- **DI-4.6.2: Platform/Application Configuration Compliance Dashboard/Reporting**
    - **Description:** Build and maintain a dashboard that surfaces the configuration-compliance posture of the program's platform services and application-hosting configuration, namely per-service baseline conformance, open drift findings, and remediation status, as a single view for the PMO ISSE and service owners.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** It reports the drift Platform/Application Baseline Drift Detection and Alerting produces rather than scanning itself. It is Level 2 because the detection activity meets the mandatory obligation. Level of Effort is Low, matching the compute and storage dashboards.

### DI-4.7: OT Baseline Configuration Drift Detection

**Design Intent:** The ground segment's passive sensors capture each station's and launch system's configuration from its traffic, and Fleet Operations exports configuration during maintenance windows where the equipment allows. Both are compared against the manufacturer baseline. Drift alerts go to Fleet Operations and the Security Team, and nothing is changed automatically on fleet equipment.

**NIST Control Mapping:**

- **CM-6 (partial):** cited at the base because non-agentable OT devices can only be passively observed, never automatically configured, so CM-6(1) would overclaim. Partial and independent, not joined to the CM-6(1) joint claim of the IT monitoring outcomes.
- **Declined:** CM-6(1) is not claimed, for the automated-management reason above.

**Deployment Type:** On-Premises, Cyber-Physical System (OT/ICS)

**Affected Components:** OT/ICS Device, OT/ICS Passive Network Monitoring

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **DI-4.7.1: Passive Configuration State Capture**
    - **Description:** Passively capture the live configuration state of the program's OT and legacy devices from the network through the passive protocol-aware monitoring that OT/Legacy Passive Protocol-Aware Discovery already established under Asset Management, without installing agents on or actively scanning the devices.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the observe dimension of the outcome's CM-6 (partial) mapping. It reuses the passive collection from OT/Legacy Passive Protocol-Aware Discovery. It stays strictly read-only, never probing or writing to devices.

- **DI-4.7.2: Drift Alerting and Operator Notification**
    - **Description:** Compare each OT and legacy device's captured configuration state against its documented Secure OT/Legacy Device Baseline and, on detecting drift, raise an alert that notifies a human operator for disposition rather than remediating the device automatically.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the verify dimension of the outcome's CM-6 (partial) mapping. It compares captured state against Secure OT/Legacy Device Baselines and alerts a human operator, never pushing configuration back. That lack of automated response is why the outcome claims CM-6 rather than CM-6(1).

### DI-4.8: Vulnerability and Patch Management

**Design Intent:** The VPMP sets KESTREL's remediation deadlines, with priority raised for assets in the DMZ, Tier 0, and the fleet. Patches move from dev to test to stage before production. Container images are rebuilt and redeployed rather than patched in place. Data center and alternate site servers are patched one node of each redundant pair at a time. Fleet patches must be validated by the manufacturer, tried on a spare, and loaded in a maintenance window. The payload processing workstation's flaws run under CCSD tailoring action 3 until 2027-09-30.

**NIST Control Mapping:**

- **SI-2 (partial):** Patch/Vulnerability Remediation SLA Policy sets the remediation time period, and this outcome owns identify, report, policy, and tracking. Partial because Patch Testing, Staged Rollout, and Rollback tests before install, and Patching and Updates and OT/ICS Vendor-Validated Patch Remediation apply the fix, all tracked jointly.
- **SI-2(2) (partial):** cited for Patch Compliance Tracking and Reporting, which automatically determines whether updates are installed.
- **SI-2(3) (partial):** the same SLA policy sets the severity-tiered benchmarks for corrective action that this enhancement names, partial on the same basis as the SI-2 base.
- **SI-5 (partial):** carried by IAVM/Security Directive Intake and Compliance Tracking, which implements external alerts and directives within their own time frames. Partial because internal alert generation belongs to the Operate pillar.
- **RA-5 (partial):** claimed only for Risk-Based Prioritization Criteria, which ranks findings by organizational risk. Partial because scanning belongs to the Vulnerability Scanning activity in Endpoint Security.
- **RA-7 (partial):** carried by Exception and Risk Acceptance Workflow, which formally accepts the risk of a vulnerability that cannot meet the SLA. Partial because Unpatchable/Legacy Asset Compensating Controls holds the mitigate-in-place slice.
- **CM-2(3) (partial):** carried by Patch Testing, Staged Rollout, and Rollback for retaining prior known-good versions so a backout is possible. Partial because other focus areas hold the build-artifact, model-artifact, and controller-logic slices.
- **Declined:** SI-5(1) needs an automated broadcast, not analyst intake. CM-3 is not re-claimed because network device patches go through Network Resource Configuration Governance, though this outcome still sets their SLA.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Device/Workstation, Storage/Database, Self-Hosted Third-Party Application (COTS), Network Infrastructure, Industrial Controller/SCADA

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider patches the cloud platform beneath KESTREL. IAVM directives arrive through the CSSP, and the aircraft and ground equipment manufacturers validate fleet patches.

**Security Impact:** High

**Activities:**

- **DI-4.8.1: Patch/Vulnerability Remediation SLA Policy**
    - **Description:** Define the program's remediation service-level policy, namely the maximum time allowed to remediate a flaw at each severity tier measured from discovery, and document it as the authoritative remediation-timeframe standard in the vulnerability and patch management plan (VPMP).
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-2 (partial) and SI-2(3) (partial) mappings, setting the remediation period as severity-tiered benchmarks. State that a CISA Known Exploited Vulnerabilities due date overrides the internal tier, as IAVM/Security Directive Intake and Compliance Tracking does for IAVA, IAVB, and IAVT directives. Revise the SLAs as risk tolerance and threats change.

- **DI-4.8.2: Risk-Based Prioritization Criteria**
    - **Description:** Define the criteria for ranking discovered vulnerabilities for remediation and the concrete inputs each criterion is computed from, namely CVSS base scores adjusted by their temporal and environmental metrics for severity, CISA Known Exploited Vulnerabilities catalog membership and EPSS scores for exploitability, the asset's mission-impact criticality tag for criticality, and its network reachability for exposure, so scan findings are prioritized by an organizational assessment of risk, and document the criteria in the VPMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-5 (partial) mapping for prioritization, while scanning belongs to the Vulnerability Scanning activity. Define each input explicitly. Use CVSS with temporal and environmental metrics for severity, treat CISA KEV membership as an override, and use EPSS for the rest. Read asset criticality from the Tagging Framework's criticality tag.

- **DI-4.8.3: Patch Testing, Staged Rollout, and Rollback**
    - **Description:** Designate the pilot and canary population a patch is released to first, sequence the rollout rings it advances through as it proves stable, specify the backout procedure and the prior known-good image or configuration version each ring can be restored from, and document the rings, promotion criteria, and rollback triggers in the VPMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the test-before-install slice of the outcome's SI-2 (partial) mapping and the CM-2(3) (partial) mapping for retained prior versions. Design the pilot ring to represent the estate rather than whoever volunteers, and state promotion criteria. Set the retention depth so a backout is actually executable. Document a deviation path for KEV-listed vulnerabilities under active exploitation.

- **DI-4.8.4: Patching and Updates**
    - **Description:** Deploy and apply security patches and updates to managed endpoints and compute hosts through an automated patch-management mechanism, covering system and device firmware, including UEFI/BIOS, TPM firmware, baseboard management controller firmware, and device and option-ROM firmware, alongside operating-system and application updates and vendor-issued updates for the program's self-hosted third-party and COTS applications, and correct the identified flaws within the remediation SLAs the vulnerability and patch management plan (VPMP) sets.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SI-2 (partial) mapping as the dimension that actually applies the patch. It executes the tested rings within the SLAs set in the VPMP, which is why it cites the base rather than SI-2(5). Include system, TPM, BMC, and option-ROM firmware, plus self-hosted COTS vendor packages. In an air-gapped enclave, run against an internal repository fed by governed offline transfer.

- **DI-4.8.5: OT/ICS Vendor-Validated Patch Remediation**
    - **Description:** Apply firmware and software updates to the OT and ICS devices that can accept them only after the ICS product vendor has validated the update for that specific device model and configuration, schedule the application into a coordinated maintenance window, re-validate device and process operation before the window closes, and document the vendor-validation requirement and window coordination in the VPMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the correct dimension of the outcome's SI-2 (partial) mapping for patchable OT and ICS devices. The gate is the ICS product vendor's approval of the update for that model. Plan windows through Maintenance Window Scheduling and Change Coordination, target the level Firmware Version and Patch-Level Baseline Tracking documents, and confirm it with OT Baseline Configuration Drift Detection. Devices with no fix go to Unpatchable/Legacy Asset Compensating Controls.

- **DI-4.8.6: Patch Compliance Tracking and Reporting**
    - **Description:** Track and report each asset class's patch-compliance status against the remediation SLAs by consuming vulnerability scan and patch-status data, surfacing which components are within or past their remediation deadline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-2(2) (partial) mapping by automatically determining whether updates are installed. It measures Vulnerability Scanning findings against the SLAs Patch/Vulnerability Remediation SLA Policy sets, without scanning or patching itself.

- **DI-4.8.7: Exception and Risk Acceptance Workflow**
    - **Description:** Establish the workflow for formally accepting the risk of a vulnerability or missing patch that cannot be remediated within the standard SLA, capturing the justification, compensating controls, approval authority, and review date, and document it in the VPMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-7 (partial) mapping, formally accepting the risk of flaws that cannot meet the SLA. It ties to Unpatchable/Legacy Asset Compensating Controls where controls offset the accepted risk. It is event-driven because acceptance is raised per flaw or asset.

- **DI-4.8.8: IAVM/Security Directive Intake and Compliance Tracking**
    - **Description:** Establish the channel that receives the Information Assurance Vulnerability Management alerts and security directives issued to the program, such as IAVA, IAVB, and IAVT notices and the equivalent tasking orders, determines which of the program's assets each applies to, and tracks remediation against the directive's own mandated compliance date rather than the program's remediation SLA, and document the intake channel and compliance-tracking procedure in the VPMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-5 (partial) mapping, implementing external directives within their own time frames. It is partial because internal alerts and noncompliance notification run through the Operate pillar. SI-5(1) is not claimed because intake is analyst-performed. Track directives separately from scan findings, and route unmeetable dates through Exception and Risk Acceptance Workflow.

### DI-4.9: Unpatchable/Legacy Asset Compensating Controls

**Design Intent:** Any asset that cannot be patched gets its own segment, intrusion prevention at its only path, and tighter monitoring. The payload processing workstation is the only candidate, and only if its replacement slips past 2027-09-30. It would sit in its own OT zone segment under application allow-listing. A single conduit would carry its converted recordings to Mission Team 1's data lake zone and nothing else. The data center hub's intrusion prevention signatures would shield its known vulnerabilities at that conduit. The passive sensors and the security monitoring platform would watch it under tighter alert thresholds than the rest of the fleet.

**NIST Control Mapping:**

- **RA-7 (partial):** cited at the base for the mitigate-in-place slice of risk response for un-remediable flaws. Partial because Exception and Risk Acceptance Workflow holds the formal acceptance slice, which this outcome's compensating controls offset.
- **SI-4 (partial):** claimed for Enhanced Monitoring for Unpatchable Assets, a general elevation of monitoring on these assets. Partial because the program-wide monitoring apparatus lives in the Operate pillar's Detection focus area.
- **Declined:** SC-7 and the IPS and WAF controls belong to the Network and Environment focus area, which these activities inherit. SA-22 belongs to End-of-Life and End-of-Support Refresh Planning, which keeps assets from arriving here unplanned.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Device/Workstation, Application/API, OT/ICS Device, Segmentation Policy, OT/ICS Zone-Conduit Segmentation (IEC 62443), Web Application Firewall, Intrusion Detection/Prevention System (IDPS)

**External Dependencies:** Payload Vendor A, whose replacement workstation retires this asset.

**Security Impact:** High

**Activities:**

- **DI-4.9.1: Network Segmentation and Isolation Enforcement**
    - **Description:** Constrain each unpatchable asset's network reachability by placing it behind the Network and Environment focus area's segmentation and isolation controls, namely dedicated zones and conduits and restrictive allow/deny rules, so a flaw that cannot be fixed cannot be reached from outside the asset's enforced boundary.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity places an unpatchable asset behind the Network and Environment focus area's segmentation controls, so the outcome claims no SC-7 of its own. It is the mandatory floor of this outcome's response and applies to every unpatchable asset.

- **DI-4.9.2: Virtual Patching**
    - **Description:** Shield the unpatchable asset's known vulnerabilities in transit by deploying the Network and Environment focus area's IPS and WAF signatures to block or neutralize exploit traffic targeting those flaws, standing in for the code-level fix the asset cannot receive.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity maintains virtual patches on the Network and Environment focus area's WAF and IDPS, so the outcome claims no SI-3 or boundary control for it. It is Level 2 because it layers above the isolation floor. It applies less to air-gapped assets and non-IP OT protocols with no inspection point.

- **DI-4.9.3: Enhanced Monitoring for Unpatchable Assets**
    - **Description:** Subject each unpatchable asset to heightened monitoring beyond the fleet baseline, namely tighter alert thresholds, closer traffic and behavior scrutiny, and priority triage, so attempted exploitation of the unfixable flaw is detected quickly even though no patch can prevent it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4 (partial) mapping, raising monitoring on assets that cannot be fixed. It uses the Operate pillar's Detection apparatus rather than a separate stack. It applies across every environment, including air-gapped and OT.

## DI-5: Endpoint Security

### DI-5.1: Execution and Device Control

**Design Intent:** Application allow-listing runs deny-by-default on the privileged access workstations, the VDI desktops, and every data center and cloud virtual machine. The privileged access workstations accept no removable media, and the VDI desktops already block drive and USB redirection. Cameras and microphones are disabled on the privileged access workstations and in the VDI image.

**NIST Control Mapping:**

- **CM-7(2) (partial):** Attack Surface Reduction's rule-based blocking of high-risk execution vectors is program-execution prevention. Partial because it covers the agentable endpoint and compute fleet rather than all of least functionality.
- **CM-7(5) (partial):** Application Control's deny-by-default allowlist is this enhancement's method, partial for the same agentable-fleet scope. With CM-7(2), it fulfills what Secure Compute Baselines defers here.
- **MP-7 (partial):** Device Control's restriction on removable media, cited at the base and partial for the EPP-enforced slice rather than all media handling.
- **SC-41 (partial):** Device Control's logical restriction of USB, Bluetooth, and other I/O ports. Partial because it does not cover physical port removal.
- **CM-11 (full):** carried by Application Control, whose allowlist blocks unapproved installs. The Governance focus area's Rules of Behavior and Acceptable Use Policy states the user policy.
- **SC-18 (partial):** carried by Application Control and Attack Surface Reduction, which define allowed scripts and block macro and obfuscated-script vectors. Partial because the Application focus area covers mobile code the program's own applications serve.
- **SC-15 (full):** carried by Collaborative Computing Device Control, which blocks remote activation of cameras and microphones and shows when they are in use.
- **Declined:** the CM-7 base and CM-7(1) stay with the baseline outcomes and Unapproved Service Usage Monitoring and Alerting.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Device/Workstation, Virtual Machine/Server

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **DI-5.1.1: Attack Surface Reduction**
    - **Description:** Configure the EPP's attack-surface-reduction rules to block common execution-based attack vectors before they run on the endpoint, namely Office applications spawning child processes, obfuscated or macro-launched scripts, credential-theft attempts against LSASS, and executable content launched from email or removable media.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-7(2) (partial) mapping and part of its SC-18 (partial) mapping, blocking high-risk vectors such as macro-launched and obfuscated scripts. With Application Control, it fulfills the forward reference from Secure Compute Baselines. It complements Malicious Code Protection without claiming SI-3.

- **DI-5.1.2: Device Control**
    - **Description:** Restrict which removable media and peripheral device classes, namely USB mass storage, Bluetooth, and other portable I/O devices, may connect to and transfer data on managed endpoints, blocking or read-only-restricting unauthorized devices per policy, and document the permitted device classes and exception process in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's MP-7 (partial) and SC-41 (partial) mappings, for removable media and peripheral ports respectively. Both are partial because they cover the logical, EPP-enforced slice. Document the permitted device classes and exception process in the CMP.

- **DI-5.1.3: Application Control**
    - **Description:** Enforce application allowlisting on managed endpoints so that only explicitly authorized executables, scripts, and installers may run under a deny-by-default, permit-by-exception policy, and document the allowlist and its exception process in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Extensive
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-7(5) (partial) mapping and its SC-18 (partial) mapping, since an allowlist of scripts defines acceptable mobile code. Document the allowlist and exception process in the CMP. Effort is Extensive and Long-term because every business unit's software must be adjudicated, the policy run in audit mode first, and an exception path staffed indefinitely.

- **DI-5.1.4: Collaborative Computing Device Control**
    - **Description:** Prohibit remote activation of cameras, microphones, and other collaborative computing devices, provide users an explicit indication when one is in use, and disable or physically remove them on endpoints used in spaces where they are not permitted.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-15 (full) mapping. In classified spaces, procure endpoints without cameras and microphones or disable them in firmware, since an indicator light is not enough. The PSO decides what may enter a secure space.

### DI-5.2: Malicious Code Protection

**Design Intent:** Behavioral anti-malware runs on every privileged access workstation, VDI desktop, and virtual machine. Runtime protection sensors run on every Kubernetes cluster, including the training cluster's GPU nodes. Web and network protection on the VDI desktops allow only the management endpoints those desktops need. Malicious-domain filtering already happens at both sides' DNS resolvers.

**NIST Control Mapping:**

- **SI-3 (partial):** shared across five activities, each blocking a different malicious-code path, from the core behavioral engine to CWPP for workloads. Partial and cited at the base because no SI-3 enhancement fits these preventive mechanisms more precisely.
- **Declined:** Network Protection and Web Protection claim no SC-7, which belongs to the Network and Environment focus area. Host-boundary SC-7(12) sits in Host Hardening and Integrity Protection.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Device/Workstation, Virtual Machine/Server, Container

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DI-5.2.1: Behavioral Anti-Malware**
    - **Description:** Deploy and enable the EPP's behavioral and heuristic anti-malware engine across managed endpoints and compute hosts to detect and block known and novel malicious code at execution based on file signatures, runtime behavior, and machine-learning models.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This engine is the core of the outcome's SI-3 mapping and the mandatory floor the other four slices layer above. SI-3 is cited at the base and partial because the five activities share it. Recurring cost is Moderate because of the per-endpoint subscription.

- **DI-5.2.2: Ransomware-Protected Folders**
    - **Description:** Enable controlled folder access on managed endpoints so that only trusted, authorized processes may modify designated protected directories, blocking ransomware and other unauthorized processes from encrypting or altering their contents.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SI-3 (partial) mapping, letting only trusted processes modify protected folders as a targeted ransomware defense. It is Level 2 because it layers above the mandatory anti-malware floor.

- **DI-5.2.3: Network Protection**
    - **Description:** Enable host-level network protection on the endpoint to block outbound connections to known-malicious IP addresses and focus areas using reputation and threat-intelligence sources, cutting off command-and-control callbacks and malicious downloads at the device before they complete.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SI-3 (partial) mapping by blocking host connections to malicious IPs and domains. It claims no SC-7, since boundary control belongs to the Network and Environment focus area. It is Level 2 as a reputation layer above the anti-malware floor.

- **DI-5.2.4: Web Protection**
    - **Description:** Enable web protection on the endpoint to block access to known-malicious and phishing URLs and unwanted web content at the browser and network layer, preventing users from reaching sites that deliver malware or harvest credentials.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SI-3 (partial) mapping, blocking malicious and phishing URLs at the browser layer while Network Protection works at the connection layer. Like Network Protection, it claims no SC-7. It is Level 2 above the anti-malware floor.

- **DI-5.2.5: Container/Workload Runtime Protection (CWPP)**
    - **Description:** Deploy cloud workload protection platform sensors across the program's containers, container hosts, and cloud compute workloads so that malicious processes, container escapes, privilege-escalation attempts, and execution of binaries absent from the deployed image are detected and blocked on the workload itself.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SI-3 (partial) mapping as its container and cloud-workload slice. Image-immutability enforcement falls under Application Control's existing CM-7(5) claim. Image scanning belongs to the Application focus area and Vulnerability Scanning, so no RA-5 is claimed. It is Level 2 because Behavioral Anti-Malware meets the floor.

### DI-5.3: Host Hardening and Integrity Protection

**Design Intent:** Exploit protection, tamper protection, and default-deny host firewalls apply to every privileged access workstation, VDI desktop, and virtual machine. The Security Team owns the tamper protection policy, so a Platform Team administrator cannot switch off the agent that watches their own activity.

**NIST Control Mapping:**

- **SC-7(12) (partial):** Host Firewalls enforces default-deny inbound rules on endpoints, servers, and mobile devices, which is what SC-7(12) was written for. Partial for the host slice, leaving perimeter SC-7 to the Network and Environment focus area.
- **SI-7 (partial):** Tamper Protection keeps the EPP/EDR agent from being disabled or altered. Partial because External Runtime Service and Client-Side Code Governance holds another base slice, and Endpoint Detection holds the SI-7 enhancements.
- **SI-16 (partial):** Exploit Protection enforces DEP, ASLR, and control-flow guard on the agentable fleet. Partial as the enforcement half, tracked with the Application focus area's Secure Coding Standards and Build Hardening.
- **SC-3 (full):** carried by Security Function Isolation, which isolates a host's security functions from its other functions.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Device/Workstation, Virtual Machine/Server

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DI-5.3.1: Exploit Protection**
    - **Description:** Enable the EPP's exploit-protection mitigations on managed endpoints and compute hosts, namely data execution prevention, address space layout randomization, and control-flow guard, to keep memory-corruption exploitation techniques from succeeding against running processes.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-16 mapping through DEP, ASLR, and control-flow guard. It is partial because it excludes OT and legacy assets, and the Application focus area's Compiler and Linker Hardening Flag Enforcement holds the build half. It is Level 1 as a baseline defensive floor.

- **DI-5.3.2: Tamper Protection**
    - **Description:** Enable the EPP/EDR agent's tamper-protection controls so that its processes, services, drivers, registry keys, and configuration cannot be disabled, uninstalled, or modified by malware or an unauthorized user, and restrict any change to authenticated management channels.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7 mapping by keeping the EPP/EDR agent's processes, drivers, and configuration from being disabled or altered. It is partial because it covers only the agent's own integrity. It is Level 1 because a disabled agent leaves every other endpoint control unenforced.

- **DI-5.3.3: Host Firewalls**
    - **Description:** Configure and enforce host-based firewall rulesets on managed endpoints, servers, and mobile devices under a default-deny inbound posture, permitting only the ports and services the service restriction policy authorizes, and document the host-firewall rule baseline in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7(12) mapping, which Rev 5 wrote for host-based boundary mechanisms. Unlike Network Protection and Web Protection, it enforces a host boundary rather than reputation blocking. Its allowed ports and services follow Policy Service Restrictions and are documented in the CMP.

- **DI-5.3.4: Security Function Isolation**
    - **Description:** Isolate each host's security functions from its non-security functions using hardware-backed or hypervisor-enforced protections, so that compromised application code cannot alter the code and data that enforce security on the same host.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-3 (full) mapping. It is Level 2 because SC-3 is in the High baseline only, and it is mandatory where the program's baseline is High. Virtualization-based protection is the usual mechanism, and it is what keeps Tamper Protection from being switched off by an administrator-level attacker.

### DI-5.4: Endpoint Detection

**Design Intent:** EDR sensors run in blocking mode on every agentable host and report to the security monitoring platform, which forwards their telemetry to the CSSP. Hosts that run payload vendor software start in audit mode until the vendor software is profiled. File integrity monitoring covers the identity provider, PKI, privileged access platform, and privileged access workstations. Boot integrity attestation covers the privileged access workstations and data center servers, with trusted launch for cloud virtual machines. The SDN controller reports any device it does not know.

**NIST Control Mapping:**

- **RA-5 (partial):** Vulnerability Scanning discovers vulnerabilities on endpoints and compute hosts. Partial because Risk-Based Prioritization Criteria holds the prioritization dimension.
- **RA-5(2) (partial):** the same activity keeps the scanned-for vulnerability list current through a continuously updated feed. Partial for this outcome's endpoint and compute fleet.
- **RA-5(5) (partial):** the privileged access the scanner holds, which enables authenticated scanning. Partial for this outcome's fleet.
- **RA-10 (partial):** Advanced Threat Hunting searches endpoint telemetry for compromise that evades existing controls.
- **SI-4 (partial):** EDR Sensor Deployment covers deploying monitoring across the fleet, and EDR Passive/Audit Mode covers observing and alerting. Partial because the two share it.
- **SI-4(2) (partial):** carried by EDR Passive/Audit Mode for near-real-time analysis of endpoint events. Partial because other outcomes hold other event classes.
- **SI-4(5) (partial):** carried by EDR Passive/Audit Mode for alerting personnel on indications of compromise, partial on the same event-class basis.
- **SI-4(7) (partial):** carried by EDR Blocking/Enforcement Mode for automatically killing, quarantining, or blocking malicious processes.
- **SI-4(24) (partial):** shared by Custom File Indicators and Custom Network Indicators for file and network IOCs.
- **SI-7(1) (partial):** carried by Endpoint File Integrity Monitoring for detecting unauthorized changes to critical files.
- **SI-7(7) (partial):** carried by the same activity, which routes change alerts into incident response. Partial because incident handling belongs to Automated Incident Creation and Enrichment.
- **SI-7(9) (partial):** carried by Boot Integrity and Device Health Attestation for measured-boot, TPM-backed verification.
- **SI-7(10) (partial):** carried by the same activity for secure-boot protection of boot firmware.
- **Declined:** Unmanaged/Rogue Device Discovery carries no citation, since it feeds the existing CM-8(3) discovery and NAC quarantine rather than re-claiming them.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Device/Workstation, Virtual Machine/Server

**External Dependencies:** The CSSP, which supplies threat intelligence indicators and joins the Security Team's threat hunts.

**Security Impact:** High

**Activities:**

- **DI-5.4.1: Vulnerability Scanning**
    - **Description:** Deploy and operate the authenticated vulnerability scanning mechanism that discovers and continuously monitors known vulnerabilities and security misconfigurations across managed endpoints and compute hosts, feeding its findings to Risk-Based Prioritization Criteria (Vulnerability and Patch Management, Configuration Policy Orchestration) for ranking and remediation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-5 (partial) mapping for scanning, while Risk-Based Prioritization Criteria ranks the findings. RA-5(5) covers the privileged access that enables authenticated scanning, so provision and protect scan credentials. RA-5(2) covers a continuously updated plugin feed, since a stale feed reports a clean fleet by omission.

- **DI-5.4.2: Endpoint File Integrity Monitoring (FIM)**
    - **Description:** Deploy file integrity monitoring on managed endpoints and compute hosts to baseline and continuously watch critical system files, directories, and registry locations, alerting when they are changed in an unauthorized or unexpected way that indicates tampering or compromise.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-7(1) mapping, checking system file, directory, and registry integrity. It surfaces changes outside the authorized process rather than re-claiming Asset Lifecycle Change Control's CM-3. It also carries the outcome's SI-7(7) (partial) mapping by forwarding each change into Automated Incident Creation and Enrichment.

- **DI-5.4.3: Advanced Threat Hunting**
    - **Description:** Conduct proactive, analyst-driven hunts across endpoint telemetry to search for indicators of compromise and adversary tradecraft that evade automated detection, and route confirmed findings to Endpoint Response and the incident-response process.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-10 mapping. It is partial because the hunt covers endpoint telemetry only. It is not tagged Automate because it is human-led and hypothesis-driven. It is Level 3 and event-driven, launched on new intelligence and hypotheses.

- **DI-5.4.4: Custom File Indicators**
    - **Description:** Define and deploy custom file-based indicators of compromise, namely cryptographic hashes, YARA rules, and file attributes, to the EDR platform so it detects and alerts on known-malicious files specific to the program's threat model.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SI-4(24) mapping for file-based IOCs, such as hashes and YARA rules, while Custom Network Indicators carries network IOCs. Loading indicator content is a definition task, so it is not tagged Automate.

- **DI-5.4.5: Custom Network Indicators**
    - **Description:** Define and deploy custom network-based indicators of compromise, namely malicious IP addresses, domains, URLs, and traffic signatures, to the EDR platform so it detects and alerts on adversary command-and-control and exfiltration infrastructure specific to the program's threat model.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the other half of the outcome's SI-4(24) mapping, the network-based IOCs. It alerts on adversary infrastructure, while Network Protection blocks connections under SI-3. It does not re-claim SC-7.

- **DI-5.4.6: EDR Blocking/Enforcement Mode**
    - **Description:** Configure the EDR sensor in blocking mode so it automatically kills, quarantines, or blocks a detected malicious process on the endpoint without waiting for analyst action, and document the block-mode policy scope and exclusions in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(7) mapping, letting the sensor kill, quarantine, or block a malicious process automatically. It differs from preventive blocking and from Endpoint Response's analyst-driven containment. It is Level 2 because blocking is usually enabled after audit-mode tuning. Document block-mode scope and exclusions in the CMP.

- **DI-5.4.7: EDR Passive/Audit Mode**
    - **Description:** Run the EDR sensor in passive audit mode to observe, log, and alert on suspicious and malicious activity without automatically blocking it, supporting sensor tuning, staged rollout, and environments where automatic blocking carries unacceptable operational risk.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the observe-and-alert slice of the outcome's SI-4 base, plus SI-4(2) for near-real-time analysis and SI-4(5) for alerting personnel. Other outcomes hold SI-4(2) and SI-4(5) for other event classes and surfaces. It provides the non-blocking posture for tuning and risky environments. It is Level 1 as the mandatory detection floor.

- **DI-5.4.8: EDR Sensor Deployment**
    - **Description:** Install and enroll the EDR sensor agent across the managed endpoint and compute fleet through automated deployment tooling so that every reachable host reports telemetry to the EDR platform, establishing the coverage the outcome's other EDR detection and response activities depend on.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the deploy-coverage slice of the outcome's SI-4 base, shared with EDR Passive/Audit Mode. One-time cost is High because this is where the EDR platform is acquired, and recurring cost is Moderate for the per-endpoint subscription. Level of Effort stays Moderate since the rollout is a tool-driven push.

- **DI-5.4.9: Unmanaged/Rogue Device Discovery**
    - **Description:** Use the EDR platform's network-visibility data to identify devices communicating on the network that lack an enrolled EDR sensor, surfacing EDR coverage gaps as a detection signal for reconciliation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent mapping. It flags devices without an enrolled EDR sensor, giving an agent-coverage view of unmanaged devices. It feeds the existing CM-8(3) discovery claims and the Network and Environment focus area's NAC quarantine rather than claiming either. It is Level 2 above the primary discovery mechanisms.

- **DI-5.4.10: Boot Integrity and Device Health Attestation**
    - **Description:** Enable and verify secure boot, measured boot, and TPM-backed health attestation on managed endpoints and compute hosts so that each device's boot process integrity is validated and unattested or failing devices are surfaced for reconciliation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries SI-7(9) for measured-boot attestation and SI-7(10) for secure-boot firmware protection, both partial for the TPM-capable fleet. They stay distinct from Endpoint File Integrity Monitoring's SI-7(1) and Tamper Protection's SI-7 base. It is Level 2 because it depends on TPM-capable hardware.

### DI-5.5: Endpoint Response

**Design Intent:** The Security Team takes every endpoint response action under the IRP, namely isolation, file remediation, and live response, and live response sessions are recorded. The CSSP may also isolate a host through a pre-approved playbook when an incident cannot wait, which pages the Security Team at once. Automated response is limited to isolating a non-production host, and a production host is isolated only with its owning team told at once. No one isolates fleet equipment through this outcome.

**NIST Control Mapping:**

- **IR-4 (partial):** Device Response handles device-level remediation, and File Response handles quarantine, deletion, and restore of files. Partial because the Response focus area holds planning, coordination, and program-wide execution.
- **IR-4(1) (partial):** Automated Investigation and Response performs on-device automated triage and remediation. Partial because the Response focus area's SOAR Capabilities holds the program-wide orchestration slice, tracked jointly.
- **IR-4(4) (partial):** Extended Detection and Response correlates endpoint, network, identity, and cloud detections into one incident view.
- **IR-4(5) (partial):** Device Isolation network-quarantines a compromised host automatically or on analyst request, keeping its management channel open.
- **IR-4(12) (partial):** Live Response gives analysts an interactive session on the live device. Partial because Evidence Preservation and Forensic Capabilities holds offline examination and chain of custody.
- **Declined:** AU-6 correlation is the Operate pillar's SIEM territory and is not re-claimed.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Device/Workstation, Virtual Machine/Server

**External Dependencies:** The CSSP, under the detection and response split in its service agreement.

**Security Impact:** Moderate

**Activities:**

- **DI-5.5.1: Extended Detection and Response (XDR)**
    - **Description:** Deploy and operate the XDR platform so it correlates detections and telemetry across endpoint, network, identity, and cloud sources into a unified, prioritized incident view from which the endpoint response actions in this outcome are triggered.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-4(4) mapping, partial for the endpoint-anchored slice. It is the correlation layer the other response activities trigger from. It claims no AU-6, which belongs to the Operate pillar's SIEM. It is Level 2 above single-source EDR.

- **DI-5.5.2: Automated Investigation and Response**
    - **Description:** Configure the XDR/EDR platform's automated investigation capability to triage incoming alerts, gather related context and evidence, and take or recommend remediation actions with minimal analyst involvement, and document the automated-response scope and approval boundaries in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-4(1) mapping, partial for the endpoint slice. The Response focus area's SOAR content decides which automated actions are authorized. Document the endpoint automation scope and approval boundaries in the CMP. It is Level 3.

- **DI-5.5.3: Device Response**
    - **Description:** Use the EDR/XDR platform to take remote remediation actions on a compromised device, including killing a malicious process, deleting a malicious registry key or dropped artifact, and running an approved remediation script, without physically accessing the host.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's IR-4 base mapping for device-level remediation, such as killing processes and running approved scripts. File Response holds the file-level slice, and Device Isolation quarantines rather than remediates. It is analyst-invoked per incident.

- **DI-5.5.4: Device Isolation**
    - **Description:** Configure and use the EDR/XDR platform's network-isolation capability to quarantine a compromised host from the network on demand or by automated trigger, blocking its lateral communication while preserving it and its management channel for investigation, and document the isolation scope and release criteria in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-4(5) mapping, quarantining a compromised host while keeping its management channel. Document isolation scope and release criteria in the CMP. The Response focus area's playbooks decide when automatic isolation fires.

- **DI-5.5.5: File Response**
    - **Description:** Use the EDR/XDR platform to act on malicious files across the fleet, quarantining or deleting a confirmed-malicious file wherever it is found and restoring a file from quarantine when a detection is determined to be a false positive.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's IR-4 base mapping for file-level response, quarantining, deleting, or restoring malicious files across the fleet. It is the after-detection counterpart to Malicious Code Protection's SI-3 blocking and does not re-claim it.

- **DI-5.5.6: Live Response**
    - **Description:** Establish an interactive live-response session capability that gives an authorized analyst a real-time remote shell on a compromised endpoint for hands-on forensic collection, examination, and remediation, and restrict session initiation to authenticated, authorized responders.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-4(12) mapping for the live on-device session. Evidence Preservation and Forensic Capabilities holds the offline slice and chain of custody, tracked jointly. Restrict session initiation to authenticated, authorized responders. It is Level 3.

## DI-6: Configuration Management Planning

### DI-6.1: Configuration Management Plan (CMP)

**Design Intent:** The Platform Team authors KESTREL's CMP, with Fleet Operations writing the OT and legacy sections and IT Operations the maintenance sections. The Security Team reviews it, and the Configuration Control Board approves it. It is revised each year and after any significant change, such as a new spoke or interconnection.

**NIST Control Mapping:**

- **CM-1 (partial):** the configuration-management slice of the policy-and-procedures requirement. Partial because other focus areas and governance outcomes hold the wider CM policy.
- **CM-9 (full):** this is the framework's only configuration management plan. CMP Development and Authoring writes the plan, CMP Review and Approval secures approval and sets distribution limits, and CMP Periodic Review and Revision keeps it current.
- **Declined:** CM-9(1) is a separation-of-duties arrangement this outcome does not take on.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Storage/Database, Device/Workstation, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DI-6.1.1: CMP Development and Authoring**
    - **Description:** Author the Configuration Management Plan, consolidating the secure-provisioning criteria, adopted hardening frameworks, change-control workflows, decommissioning requirements, compliance and service-restriction policy, and endpoint-protection and response thresholds produced across the focus area's capabilities into a single governing document.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity captures determinations from Asset Lifecycle, Baseline Configuration Standards, Configuration Policy Orchestration, and Endpoint Security, so author it once they exist. It carries the bulk of the outcome's CM-9 (full) mapping. State configuration roles, responsibilities, and item identification explicitly rather than implying them.

- **DI-6.1.2: CMP Review and Approval**
    - **Description:** Route the drafted CMP through stakeholder review and secure formal approval from the accountable authority before it takes effect.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the review-and-approval clause of the outcome's CM-9 (full) mapping. The approved CMP is useful to an adversary, so set its distribution list, storage location, and modification rights at approval.

- **DI-6.1.3: CMP Periodic Review and Revision**
    - **Description:** Review the CMP on a defined cadence and revise it to reflect changes in provisioning mechanisms, baseline standards, endpoint protection tooling, or governing requirements.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity supersedes the One-Time issuance from CMP Development and Authoring, keeping the plan current as its determinations change.

## DI-7: Vulnerability and Patch Management Planning

### DI-7.1: Vulnerability and Patch Management Plan (VPMP)

**Design Intent:** The Security Team authors KESTREL's VPMP, since it owns the POA&M and continuous monitoring, with IT Operations writing the patch windows and Fleet Operations the fleet procedures. The Configuration Control Board approves the VPMP, and risk acceptances under it go to the AO. It is revised each year and whenever an exception such as CCSD tailoring action 3 changes.

**NIST Control Mapping:**

- **RA-1 (partial):** the plan's prioritization and risk-acceptance content. Partial because other focus areas and Manage pillar outcomes hold the wider RA policy.
- **SI-1 (partial):** the plan's remediation timeframes and procedures. Partial because other focus areas and Manage pillar outcomes hold the wider SI policy.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Storage/Database, Device/Workstation, Network Infrastructure, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DI-7.1.1: VPMP Development and Authoring**
    - **Description:** Author the Vulnerability and Patch Management Plan, consolidating the remediation service levels, risk-based prioritization criteria, security-directive intake and compliance-tracking procedure, and exception and risk-acceptance workflow produced across the focus area's capabilities into a single governing document.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity captures determinations from the Vulnerability and Patch Management activities and Unpatchable/Legacy Asset Compensating Controls, so author it once they are settled. VPMP Periodic Review and Revision keeps it current.

- **DI-7.1.2: VPMP Review and Approval**
    - **Description:** Route the drafted VPMP through stakeholder review and secure formal approval from the accountable authority before it takes effect.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The plan's timeframes are what assessors measure findings against and what exceptions are granted from. Therefore, they need the accountable authority's signature.

- **DI-7.1.3: VPMP Periodic Review and Revision**
    - **Description:** Review the VPMP on a defined cadence and revise it to reflect changes in the program's threat environment, risk tolerance, scanning and patching tooling, or governing requirements.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity supersedes the One-Time issuance from VPMP Development and Authoring. Use accumulated exceptions as a standing input, since a tier routinely risk-accepted signals an unrealistic SLA to correct in the plan.

## Scoped Out

These outcomes drop out of KESTREL's design, each for the reason given.

| Outcome | Reason |
|---|---|
| DI-4.1: Device Compliance | Out of scope. KESTREL owns no laptops, desktops, or mobile devices. Performers reach it from their own CMMC Level 2 laptops and the program office from the parent organization's managed devices, and each owner enforces its own devices' compliance. |
