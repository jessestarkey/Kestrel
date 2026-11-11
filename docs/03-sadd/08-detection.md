# DE: Detection

*KESTREL SADD, Section 5 (Operate). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## DE-1: Intelligent Detection Systems

### DE-1.1: Platform-Native Threat Detection

**Design Intent:** The cloud provider's native detection services are on for every subscription, cluster, database, storage service, and the tenant, and the directory's own threat detection is on in the data center. The Security Team reviews their coverage against MITRE ATT&CK each quarter and tunes noisy alerts. Gaps they find go to custom rules in the security monitoring platform. The CSSP's analysts read the native detection consoles directly through their host pool.

**NIST Control Mapping:**

- **SI-4 (partial):** claimed at the base for the provider-native detection service layer. Enablement and tuning stand the monitoring up, while Detection Capability Review and Addressing Detection Gaps set the monitoring objectives. The Protect pillar's SI-4 claims cover other surfaces, and none observes what a provider's own detection service reports.
- **SI-4(2) (partial):** claimed for the near-real-time automated analysis the managed services perform over platform control plane, workload, and managed-service events. It is one partial slice, split from the others by event class, alongside Identity Platform Threat Detection and Hardening.
- **Declined:** SI-4(1) is held by the Network and Environment focus area's IDPS outcome. SI-4(24) is left to the sibling Correlated Threat Detection and Analytics outcome. CA-7 belongs to the Manage pillar's Continuous Monitoring Program, which Detection Capability Review feeds.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Database Service, Object/File Storage, Directory/Platform Core Infrastructure

**External Dependencies:** The IL5 cloud provider, whose native detection and logging services KESTREL inherits under its provisional authorization. The CSSP, which reads the native detection consoles.

**Security Impact:** Moderate

**Activities:**

- **DE-1.1.1: Platform-Native Detection Service Enablement and Tuning**
    - **Description:** Enable the detection service each cloud platform, operating system, and managed service provides across every account, subscription, and platform instance in the program's footprint, and tune each service's severity thresholds and suppression rules to the environment it is watching.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the deploy-the-monitoring-capability dimension of the outcome's SI-4 (partial) mapping and the whole of its SI-4(2) (partial) mapping. Enablement is per account and subscription, so verify coverage rather than assume it, since an account created outside the landing zone is usually the gap. It is not tagged Automate because it is ongoing runtime detection rather than a pipeline gate.

- **DE-1.1.2: Detection Capability Review**
    - **Description:** Assess what the enabled detection services actually cover against the adversary techniques the program's threat model names, and record the covered, partially covered, and uncovered techniques as the standing statement of detection coverage.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the monitoring-objectives dimension of the outcome's SI-4 (partial) mapping. Assess coverage against one technique taxonomy the program keeps, so findings compare across cycles. Record which entries are asserted from documentation and which the Adversary Emulation and Detection Validation outcome has demonstrated.

- **DE-1.1.3: Addressing Detection Gaps**
    - **Description:** Assign an owner and a closure path to each uncovered technique the review identifies, choosing for each whether the gap is closed by a custom rule, an additional telemetry source, a new detection product, or a documented acceptance.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the remaining monitoring-objectives dimension of the outcome's SI-4 (partial) mapping. Most closures land as custom content authored through Custom XDR/Platform-Native Detection Rule Creation, while this activity owns the decision and the owner. An accepted gap goes through the Manage pillar's Plan of Action and Milestones (POA&M) capability.

- **DE-1.1.4: Alert Quality Optimization**
    - **Description:** Measure the true-positive rate, duplication, and analyst disposition time of each detection service's alert stream, and suppress, merge, or re-tier the rules whose output is not worth the attention it consumes.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** A queue analysts close without reading is no better than a detection never enabled, and this activity prevents that. Record suppressions in the CMP with a reason and an expiry. It is Level 1 because the mandatory detections depend on being read.

- **DE-1.1.5: Detection Coverage/MITRE ATT&CK Mapping Visualization Dashboard**
    - **Description:** Build the dashboard that renders the program's detection coverage against the MITRE ATT&CK matrix, showing per technique which detections exist, which have been validated by emulation, and which remain uncovered.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This is the capability's designated Visualize instance. It reads the Adversary Emulation and Detection Validation outcome's results, so a technique moves from covered to validated only after something has executed against it. It carries no independent control citation.

### DE-1.2: Adversary Emulation and Detection Validation

**Design Intent:** A breach and attack simulation platform runs known techniques against the cloud spokes, the data center, and identity each month, and confirms which ones the security monitoring platform caught. The Security Team and the CSSP run a purple team exercise each quarter. Every missed technique becomes a tracked detection fix. Fleet systems are emulated only on spares or the simulator.

**NIST Control Mapping:**

- **CA-8(2) (full):** claimed here because the Application focus area's Penetration Testing outcome explicitly leaves it to the Operate pillar. The emulation and purple team activities are the simulated adversary attempts, exercise planning sets the rules of engagement, and the findings activity turns results into change. Penetration testing asks whether a system can be compromised, while this outcome asks whether the program would see it.
- **Declined:** CA-2(2) belongs to the Manage pillar's CA-2 assessment apparatus, and claiming it here would create a second assessment program. RA-10 belongs to the sibling Enterprise Threat Hunting Program. SI-4 is not claimed, since emulation exercises monitoring rather than performing it.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Device/Workstation, Identity Platform, Network Infrastructure, Application/API

**External Dependencies:** The CSSP, which joins each purple team exercise.

**Security Impact:** Moderate

**Activities:**

- **DE-1.2.1: Breach and Attack Simulation Platform Deployment**
    - **Description:** Deploy a breach and attack simulation platform with agents in the environments the program actually runs, and schedule it to execute its technique library continuously so each detection is exercised on a cadence rather than at an annual event.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This is the one Automate activity in this outcome, since the platform is a scheduled, tool-driven check replacing manual validation of each detection. Simulate destructive techniques in non-executing mode or confine them to a test environment. It is Level 3 because the emulation exercises below are the minimum a program needs.

- **DE-1.2.2: Adversary Emulation Exercise Planning and Execution**
    - **Description:** Scope each emulation campaign to the tradecraft of a specific actor the program's threat model names, agree the rules of engagement and the safety stops with the system owners, and execute the campaign end to end while recording which actions produced a detection and which did not.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the core of the outcome's CA-8(2) (full) mapping, the simulated adversary attempt under agreed rules of engagement. Emulate a named actor's documented tradecraft so the result tests the detections the program actually needs. Keep a minute-by-minute execution record, since reconstruction after the telemetry window rolls is guesswork. It is not tagged Automate because it is human-led.

- **DE-1.2.3: Purple Team Exercise Coordination**
    - **Description:** Run the emulation with the detection engineers in the room and the timeline shared, so a technique that fails to alert is diagnosed and the rule rewritten within the session rather than months later.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the collaborative dimension of the outcome's CA-8(2) (full) mapping. Purple team sessions do not replace the unannounced campaign, which measures the program as it actually operates. It is not tagged Automate because it is human-led.

- **DE-1.2.4: Detection Efficacy Findings and Remediation Tracking**
    - **Description:** Convert each missed or late detection into a tracked item carrying an owner, the technique that produced it, and a remediation date, and close it only after the technique has been re-executed and the detection observed to fire.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the corrective-action dimension of the outcome's CA-8(2) (full) mapping. Close findings by re-executing the technique, since a new rule is untested until then. Results feed the Platform-Native Threat Detection outcome's coverage review and dashboard.

### DE-1.3: Correlated Threat Detection and Analytics

**Design Intent:** The security monitoring platform is the one place every telemetry source lands, and it correlates endpoint, identity, network, cloud, application, and ground segment events with each other. Threat intelligence and indicator feeds from the CSSP enrich every alert. Detection rules are written as code in the Security Team's repository and deployed through the pipeline after review.

**NIST Control Mapping:**

- **SI-4(16) (partial):** claimed for Security Telemetry Centralization and Unified XDR Platform Deployment, which correlate monitoring output across endpoint, network, identity, cloud, data-service, and OT surfaces. It is partial because the platform mechanics and the SI-4(12) residual belong to the sibling SIEM Platform capability, and Production Abuse Monitoring holds an ML-serving slice.
- **SI-4(24) (partial):** claimed for Indicator of Compromise (IOC) Feed Management as the program-wide indicator lifecycle. It is partial because Endpoint Detection holds the slice for custom indicators deployed to the EDR platform.
- **SI-5 (partial):** claimed for receipt of threat-actor, campaign, and indicator intelligence and its dissemination into detection content. Vulnerability and Patch Management holds the vulnerability-advisory slice.
- **Declined:** SI-5(1) covers advisories to personnel, not machine-readable detection content. PM-16 belongs to the Manage pillar's Threat Intelligence capability. AU-6(3) is reserved for the SIEM Platform capability. IR-4(4) stays with the Extended Detection and Response (XDR) activity, which uses it for endpoint response triggering.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Identity Platform, Device/Workstation, Network Infrastructure, Application/API, OT/ICS Device

**External Dependencies:** The CSSP, which receives forwarded telemetry and adds its own detection under its service agreement. It also supplies threat intelligence and indicator feeds.

**Security Impact:** High

**Activities:**

- **DE-1.3.1: Security Telemetry Centralization**
    - **Description:** Route the security-relevant telemetry from every detection and logging source the program operates into one analytic surface with a common schema and a common entity resolution, so that a host, an account, and an address mean the same thing to every rule that reads them.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SI-4(16) (partial) mapping, since correlation needs comparable sources. Entity resolution matters most, because a join fails silently when two sources name one principal differently. It consumes what the Comprehensive Logging capability collects. Its pipeline stays separate from Data Source Connections, because the SIEM platform carries its own retention and audit-log-integrity obligations.

- **DE-1.3.2: Unified XDR Platform Deployment**
    - **Description:** Deploy the unified detection and response platform as the program's cross-source correlation engine, configuring it to assemble related detections across endpoint, identity, network, cloud, and data-service telemetry into single prioritized incidents.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's SI-4(16) (partial) mapping as the detection and correlation half of the XDR platform. The response half, and IR-4(4), stay with the Extended Detection and Response (XDR) activity. It is not tagged Automate because it is an ongoing correlation layer rather than a pipeline gate.

- **DE-1.3.3: Custom XDR/Platform-Native Detection Rule Creation**
    - **Description:** Author the detection rules the program's own environment, mission, and threat model require and that no vendor content ships with, covering the gaps the coverage review identifies and the tradecraft the hunts and emulation exercises surface.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it is how this outcome's SI-4(16) content and Platform-Native Threat Detection's SI-4 objectives get expressed. Its inputs are Addressing Detection Gaps, Detection Efficacy Findings and Remediation Tracking, and Hunt Finding-to-Detection-Rule Conversion, so it is event-driven. Deploy every rule through the version-controlled pipeline rather than a console.

- **DE-1.3.4: Threat Intelligence Enrichment**
    - **Description:** Attach the known actor, campaign, malware-family, and reputation context to each alert as it is raised, so that an analyst opens a finding with its provenance already present rather than assembling it by hand.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SI-5 (partial) mapping, the receipt of external intelligence and its dissemination to analysts. It is tagged Automate for lookup in the alerting path. Scope enrichment to context, not verdict, so a third-party reputation score never silently closes an alert. Source curation belongs to the Manage pillar's Threat Intelligence capability.

- **DE-1.3.5: Indicator of Compromise (IOC) Feed Management**
    - **Description:** Operate the indicator lifecycle end to end, ingesting indicators from the program's subscribed and shared sources, deduplicating and aging them against a defined confidence and expiry policy, and distributing the surviving set to every detection platform that can act on it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(24) (partial) mapping and part of its SI-5 (partial) mapping. It is tagged Automate for the ingestion and distribution pipeline. Define confidence tiers and aging rules in the CMP, since an indicator set that only grows drives false positives that retire the mechanism. It receives the Manage pillar's Indicator Hand-Off to Operate Pillar's IOC Feed Management.

- **DE-1.3.6: Detection-Rule-as-Code / Version-Controlled Rule Deployment Pipeline**
    - **Description:** Hold every detection rule in version control and deploy it through a pipeline that tests it against historical telemetry, requires a peer review, and promotes it to the platform automatically, so that rule changes are reviewed, attributable, and reversible.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is tagged Automate as a named practice and the gate rule changes pass through. It carries no independent control citation. It lets the program explain why a detection stopped firing and revert a rule quickly. Backtest each rule against retained telemetry before promotion.

### DE-1.4: Enterprise Threat Hunting Program

**Design Intent:** The Security Team runs a monthly threat hunt, drawn from threat intelligence about adversaries likely to target ISR programs and from each model's threat model. Hunts cover the cloud, the data center, identity, and the ground segment's passive sensor data. Every hunt that finds something, or finds a blind spot, ends with a new detection rule.

**NIST Control Mapping:**

- **RA-10 (partial):** claimed as the cross-source, program-wide slice. Endpoint Detection's Advanced Threat Hunting holds the endpoint slice, and the two are tracked jointly. RA-10 has no enhancements, so the base citation is the most specific available.
- **Declined:** SI-4 is held by the monitoring outcomes that instrument the query tooling. RA-3 belongs to the Manage pillar.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Identity Platform, Device/Workstation, Network Infrastructure, Application/API, OT/ICS Device

**External Dependencies:** The CSSP, which supplies the threat intelligence behind hunt hypotheses.

**Security Impact:** Moderate

**Activities:**

- **DE-1.4.1: Hunt Hypothesis Development and Prioritization**
    - **Description:** Write each hunt as a falsifiable statement about what an adversary would have had to do in this program's specific architecture, derive the telemetry that would confirm or refute it, and rank the backlog by the consequence of the technique and the confidence that current detections would miss it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the establish-the-capability dimension of the outcome's RA-10 (partial) mapping. Each hypothesis must name the telemetry that would refute it, which keeps hunts from becoming open-ended browsing. Prioritize techniques the coverage review marks uncovered.

- **DE-1.4.2: Cross-Source Hunt Execution**
    - **Description:** Execute each prioritized hypothesis against the full centralized telemetry surface, pivoting freely across identity, endpoint, network, cloud, data-service, and OT sources, and record the queries run and the scope covered whether or not the hunt finds anything.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the core of the outcome's RA-10 (partial) mapping, the search for threats evading existing controls. Record negative results too, since they show what the program has looked for. Hand confirmed findings to the Response focus area as incidents.

- **DE-1.4.3: Hunt Finding-to-Detection-Rule Conversion**
    - **Description:** Turn each hunt that produced a durable, repeatable signal into a detection rule authored through Custom XDR/Platform-Native Detection Rule Creation, and close the hunt only once that rule is deployed or the finding is documented as not automatable.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the disrupt dimension of the outcome's RA-10 (partial) mapping. Record why a signal is not automatable, so the backlog does not re-hunt the same ground. It is not tagged Automate because conversion is analyst judgment, while deployment runs through the Automate-tagged pipeline.

### DE-1.5: Deception Technology

**Design Intent:** Canary credentials sit in every spoke's vault and in the directory, decoy hosts sit in each data center segment, and a decoy dataset sits in each data lake zone. None of them has a legitimate user. Any touch alerts the Security Team at the highest priority, with the decoy's location attached.

**NIST Control Mapping:**

- **SC-26 (full):** the honeytoken and decoy activities place components designed to be attacked, and trigger alerting provides the detection and analysis the control names. The control has no enhancements, so the base citation is the most specific available.
- **Declined:** SC-35 describes outbound-seeking honeyclients, while this outcome fields only inbound decoys. SI-4-family controls are not claimed, since the decoy generates the trigger itself. AC-2-family controls do not fit canary accounts, which exist to be misused rather than assigned.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Virtual Machine/Server, Directory/Platform Core Infrastructure, Application and Service Account Identity, Object/File Storage, Device/Workstation, Segmentation Policy

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **DE-1.5.1: Honeytoken and Canary Credential Deployment**
    - **Description:** Plant credentials, API keys, session tokens, documents, and directory accounts that no legitimate process ever uses, in the locations an intruder searches first, and register each one so that any authentication or access attempt against it is attributable to the token that was taken.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SC-26 (full) mapping and returns the most per unit of effort. Placement is the whole design, since an unfindable token reports nothing and a findable-by-admins token raises false positives. Keep the token inventory restricted and outside the systems it covers.

- **DE-1.5.2: Decoy System/Honeypot Deployment**
    - **Description:** Stand up decoy hosts, services, shares, and cloud resources that present as the lateral-movement targets an intruder would reach for next, instrument them to record every interaction in full, and isolate them so they cannot be used as a foothold into anything real.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's SC-26 (full) mapping, including analysis. Constrain each decoy's network position, credentials, and outbound reach so compromising it leads nowhere. Enroll decoys in the asset inventory, marked as decoys, so vulnerability and compliance processes skip them.

- **DE-1.5.3: Deception Trigger Alerting and Investigation Routing**
    - **Description:** Route every deception trigger to the security operations queue as a high-severity, high-confidence alert carrying the decoy touched and the full interaction record, and hand confirmed triggers directly to the incident response process without intermediate triage scoring.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the detection dimension of the outcome's SC-26 (full) mapping. Do not score, correlate, or age a deception trigger, since it has no benign explanation. Route it to the Response focus area under the IRP, and feed it to the correlation surface without waiting on that correlation.

### DE-1.6: User/Entity Behavior Analytics (UEBA) / Insider Threat Detection

**Design Intent:** Behavioral baselines cover every person role, including analysts, administrators, data scientists, developers, and partner accounts. Bulk reads, access outside normal hours, and reads of another team's or vendor's data raise a user's risk score. The Security Team investigates high scores and refers insider threat indicators to the PSO's program.

**NIST Control Mapping:**

- **PM-12 (partial):** claimed here because the Data focus area's Data Loss Prevention (DLP) and Monitoring outcome leaves it to this outcome. It is partial because the insider threat program itself belongs to the PSO and program counsel, outside the SABER. This outcome and User Activity Monitoring supply its technical layer. PM-12 has no enhancements, so the base citation is the most specific available.
- **AC-2(12) (partial):** claimed for the general person and non-person account population, monitored against its own and peer history. It is partial because Emergency Access holds the break-glass slice and the DLP outcome holds the classified-data-access slice.
- **Declined:** SI-4(12) is reserved for the SIEM Platform capability, which this outcome's alerting rides on.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Identity Platform, Device/Workstation, Application/API, Database Service, Object/File Storage

**External Dependencies:** The PSO's insider threat program, which receives referrals and owns every case.

**Security Impact:** Moderate

**Activities:**

- **DE-1.6.1: Behavioral Baseline Profiling**
    - **Description:** Build and continuously maintain a behavioral profile for every person account and every service or workload account, covering its normal access scope, volume, timing, source, and peer-group comparison, over an observation window long enough to include the program's periodic work cycles.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the monitoring half of the outcome's AC-2(12) (partial) mapping and part of its PM-12 (partial) mapping. It is tagged Automate for the profiling engine. Include non-person accounts, since their regular behavior makes deviations meaningful. Span the program's own cycles, such as a quarterly close, so normal operations do not alert.

- **DE-1.6.2: Anomalous Behavior Alerting and Risk Scoring**
    - **Description:** Score each principal's live behavior against its maintained profile, raise an alert when the deviation crosses the program's defined threshold, and record the thresholds, the contributing signal weights, and the escalation tiers in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the report-atypical-usage half of the outcome's AC-2(12) (partial) mapping. It is tagged Automate for the scoring engine. Use a cumulative, decaying score, since the pattern that matters is an accumulation of small deviations. Set thresholds knowing a low one puts the program's own workforce under investigation.

- **DE-1.6.3: Insider Threat Indicator Correlation and Investigation**
    - **Description:** Correlate the behavioral scores with the other indicator classes the insider threat function receives, run each correlated case through the program's defined investigation workflow with the cross-discipline participants that workflow names, and hand substantiated cases to the incident response process.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the core of the outcome's PM-12 (partial) mapping, namely the correlation and case handoff the program's technical staff perform for the insider threat team. It is Level 2 because PM-12 sits outside the system baselines, though it is mandatory where the insider threat program depends on the technical team. It consumes the Data focus area's Insider Risk Behavioral Analytics output as one indicator class. Collection limits, access, and the case standard are set with the PSO and program counsel, and security incidents go to the Response focus area under the IRP.

### DE-1.7: Network/OT Intrusion and Anomaly Detection

**Design Intent:** Intrusion detection runs on the data center hub and on sensors fed by the SDN fabric's mirrored traffic, covering the paths the cloud hub never sees. In the ground segment, the passive sensors' anomaly detection is the intrusion detection. Alerts are triaged by the Security Team, and ground segment alerts also go to Fleet Operations.

**NIST Control Mapping:**

- **SI-4(11) (partial):** claimed for Network Intrusion Detection System (NIDS) Deployment, whose tap-fed sensors analyze egress and east-west paths for anomalies. It is partial because the cloud counterpart sits with the IDPS outcome, and OT/Legacy Passive Monitoring declined it for interior process traffic.
- **Declined:** The rest of the SI-4 family is held elsewhere. SI-4(1) belongs to the Network and Environment focus area's IDPS outcome. SI-4(4) belongs to Industrial Protocol Filtering (DPI). SI-4(7) is held by IDPS Mode Configuration and EDR Blocking/Enforcement Mode, and nothing here enforces. SI-4(13) and SI-4(5) stay with OT/Legacy Passive Monitoring, which collects, profiles, and alerts on process segments, while this outcome only correlates the normalized OT telemetry. IR-4 and IR-5 belong to the Response focus area.

**Deployment Type:** On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Intrusion Detection/Prevention System (IDPS), OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DE-1.7.1: Network Intrusion Detection System (NIDS) Deployment**
    - **Description:** Deploy tap or SPAN-fed intrusion detection sensors across the program's on-premises egress points and internal east-west paths, select and maintain the signature and protocol-anomaly rule sets those sensors run, and operate them in detection-only mode with findings forwarded to the correlation surface.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(11) (partial) mapping, scoped to paths the cloud-native IDPS tier does not reach. Run sensors detection-only, since an inline device on an internal path adds an availability dependency. Place sensors where traffic aggregates, including east-west paths. It is not tagged Automate because it is ongoing runtime detection.

- **DE-1.7.2: OT/ICS-Aware Anomaly Detection**
    - **Description:** Author and maintain protocol-aware OT detection content on the enterprise correlation surface over the normalized process-network telemetry the logging capability delivers, so that a control-system anomaly is read alongside the identity, endpoint, and network activity surrounding it rather than only in the control room.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since OT/Legacy Passive Monitoring already holds SI-4(13) and SI-4(5). It adds enterprise correlation of OT signals, strictly read-only over collected records. It is Level 2 because that outcome's control-room alerting meets the mandatory floor.

- **DE-1.7.3: Anomaly Alert Triage and Escalation Workflow**
    - **Description:** Define the triage workflow for network and OT anomalies, naming the network and control engineers who must help adjudicate each one, the evidence collected at triage rather than at escalation, and the criteria that promote a triaged anomaly to an incident, and document the triage workflow and promotion criteria in the IRP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Name the engineer, or on the OT side the asset owner, as a participant, since only they know whether a conversation had an operational reason. Collect evidence at triage before sensor buffers age it out. Escalate confirmed anomalies to the Response focus area under the IRP, where OT containment stays human-in-the-loop.

### DE-1.8: Identity Threat Detection

**Design Intent:** The identity provider's sign-in and directory logs and the cloud tenant's entitlement changes all feed the security monitoring platform. Risky sign-ins include a partner from an unexpected network, an operator signed in at a station they are not badged into, and a performer laptop that suddenly reports as non-compliant. A compromised account is disabled at once, and an identity posture score is reported each month.

**NIST Control Mapping:**

- **AU-2 (partial):** claimed for Identity Audit Record Coverage Confirmation and Review, which selects the identity event types to log, confirms each is present, and reviews that selection on a cadence. It is partial because it covers only identity records. AU-12 generation stays with Infrastructure and Identity Logging.
- **AU-6 (partial):** claimed at the base, scoped to identity audit records. Identity Audit Record Coverage Confirmation and Review and Authentication Activities Monitoring review them for unusual activity and report findings. SIEM Capabilities holds the other record classes.
- **SI-4(5) (partial):** claimed for Risky Sign-In Pattern Detection and Compromised Account Identification, the identity-platform slice of the split by indication source. Identity Platform Threat Detection and Hardening holds SI-4(2) for defending the platform itself.
- **Declined:** AU-12 belongs to Infrastructure and Identity Logging, which generates the records analyzed here. AU-6(1), AU-6(3), AU-11, and AU-9 belong to the SIEM Platform capability. AC-2(12) belongs to User/Entity Behavior Analytics (UEBA) / Insider Threat Detection, which detects atypical account behavior rather than credential compromise.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Identity Platform, Cloud Account/Subscription/Tenant Boundary, Application/API, Device/Workstation

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **DE-1.8.1: Identity Audit Record Coverage Confirmation and Review**
    - **Description:** Establish the identity audit record set the program's detection depends on, confirming that the authentication, directory-change, entitlement-grant, consent, and privileged-operation event classes are all present and analyzable, and review them on a defined cadence for indications of inappropriate or unusual activity.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-6 (partial) mapping and the whole of its AU-2 (partial) mapping. Confirm the event classes detection needs are logged and read, especially consent grants and out-of-process permission changes. Raise any missing class against Infrastructure and Identity Logging rather than building a second collection path.

- **DE-1.8.2: Authentication Activities Monitoring**
    - **Description:** Monitor the authentication event stream continuously across the program's identity providers, federated relying parties, and legacy authentication paths, so that every credential use is observable regardless of which path it took.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's AU-6 (partial) mapping. Cover legacy and non-federated authentication paths, since adversaries pick the least-watched protocol. It is not tagged Automate because it is ongoing observability rather than a pipeline gate.

- **DE-1.8.3: Risky Sign-In Pattern Detection**
    - **Description:** Detect the sign-in patterns that indicate credential abuse, including impossible travel, anonymizing infrastructure, unfamiliar device and location combinations, password spray and credential stuffing shapes, and multi-factor fatigue prompting, and tune the risk levels those detections assign to the program's own travel and access patterns.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SI-4(5) (partial) mapping, a platform-generated compromise indication rather than a behavioral score. Tune risk levels to the program's operating pattern, such as deployed locations or shared egress, so impossible-travel findings stay meaningful. Conditional access enforcement belongs to the Identity focus area.

- **DE-1.8.4: Compromised Account Identification**
    - **Description:** Identify the accounts showing confirmed compromise indications by correlating risky sign-in signals with credential exposure in breach and dark-web sources, anomalous token and session activity, and post-authentication actions characteristic of takeover, and route each identified account for immediate credential and session response.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's SI-4(5) (partial) mapping. Cover tokens and sessions, since a stolen refresh token survives a password reset and an attacker-registered authenticator survives both. Response runs through the Identity focus area and the Response focus area under the IRP.

- **DE-1.8.5: SIEM Platform Integration**
    - **Description:** Connect the identity platform's audit, risk, and detection outputs to the program's correlation surface with the entity identifiers preserved, so an identity finding can be joined to the endpoint, network, and data activity of the same principal.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation. It connects identity sources to the correlation surface, using an identifier the endpoint and network sources share so the feed correlates. It is not tagged Automate because it is a standing integration.

- **DE-1.8.6: Cloud Infrastructure Identity Threat Monitoring**
    - **Description:** Extend identity threat detection to the cloud infrastructure entitlement layer, monitoring the role assumptions, cross-account and cross-tenant grants, entitlement escalations, and access-key usage, since a cloud identity compromise shows itself there rather than through an interactive sign-in.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Treat the cloud entitlement layer as its own surface, since role assumption by a workload, a key used from a new region, or a widened policy produces no sign-in event. Author content against the provider's control-plane records without a second collection. Identity Platform Threat Detection and Hardening's SI-4(2) claim is not reopened.

- **DE-1.8.7: Identity Security Posture Scoring**
    - **Description:** Compute and publish a recurring identity security posture score covering multi-factor coverage, privileged account count, stale and orphaned account volume, legacy authentication use, and standing entitlement breadth, and track its movement over time rather than only its current value.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is tagged Visualize because it surfaces posture as an actionable metric. It carries no independent control citation and reports rather than enforces, with each score component remediated by the owning Identity focus area outcome. Track the trend rather than the absolute number.

### DE-1.9: User Activity Monitoring

**Design Intent:** KESTREL has no classified endpoints, so CNSSD 504's user activity monitoring mandate does not apply. KESTREL still records every privileged session on the privileged access workstations and in the VDI host pools. The Security Team reviews those recordings when an alert fires, and on a sample each month. Indicators go to the PSO's insider threat program.

**NIST Control Mapping:**

- **AU-14 (partial):** covers recording and reviewing session content for general users on classified endpoints. Privileged Credential Vaulting and Session Brokering holds the privileged-session slice.
- **AU-14(1) (full):** user activity monitoring starts session audits at system start-up, so no session begins unobserved.
- **PM-12 (partial):** a second technical contribution, alongside User/Entity Behavior Analytics (UEBA) / Insider Threat Detection, to the insider threat program the PSO owns outside the SABER.
- **Declined:** AC-2(12) belongs to User/Entity Behavior Analytics (UEBA) / Insider Threat Detection, since this outcome captures rather than scores. AC-8 is held by the Identity focus area, whose banner carries the monitoring notice.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Virtual Desktop Infrastructure (VDI), Privileged Access Workstation (PAW), Security Information and Event Management (SIEM) Platform

**External Dependencies:** The PSO's insider threat program, which receives referrals and owns every case.

**Security Impact:** High

**Activities:**

- **DE-1.9.1: User Activity Monitoring Deployment on Classified Endpoints**
    - **Description:** Deploy the user activity monitoring agent on every classified endpoint so that capture begins at system start-up, protect the agent and its captured data from tampering by the users it monitors, and alert when an endpoint stops reporting.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-14 (partial) and AU-14(1) (full) mappings. Alert on loss of reporting, since a user who disables the agent has disabled the control.

- **DE-1.9.2: Monitoring Policy, Trigger, and Reviewer Definition**
    - **Description:** Define with the PSO and program counsel what activity is captured, the triggers that bring captured activity to review, who may review it, and how long it is retained, and document the result as the program's user activity monitoring policy.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The PSO and counsel set monitoring policy, not the engineers deploying the agent. Triggers such as marking matches, removable media, printing, and off-pattern activity bring sessions to review, while the rest is retained for investigations. Restrict reviewers, since they see the most sensitive record the program holds.

- **DE-1.9.3: Review, Triage, and Insider Threat Program Referral**
    - **Description:** Review the activity each trigger surfaces against the monitoring policy, dispose of benign matches with a recorded reason, and refer substantiated concerns to the insider threat program the PSO owns rather than investigating them within the security operations team.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's PM-12 (partial) contribution. Security operations establishes what happened, while the insider threat program decides what it means about a person. A referral that is also an incident, such as spillage, runs through the Response focus area at the same time.

## DE-2: Comprehensive Logging

### DE-2.1: Infrastructure and Identity Logging

**Design Intent:** Control-plane activity logs from every subscription and the tenant, together with the identity provider's authentication and directory change logs, flow to the security monitoring platform. Configuration checks alert when a source stops sending. Identity logs are kept longer than the default, as the log retention strategy sets.

**NIST Control Mapping:**

- **AU-12 (partial):** the infrastructure control plane and identity estate slice, the first of eight source-class slices in this capability. Protect pillar outcomes hold subject slices such as Approver and Reviewer Audit Log, and Identity Threat Detection declined AU-12 in favor of this outcome. The whole set is tracked jointly.
- **AC-2(4) (partial):** claimed for Identity Change Tracking, which records the five account actions the enhancement names. It is partial because review and alerting belong to Identity Threat Detection.
- **AU-1 (partial):** the procedures half, carried by Audit and Accountability Procedures for all of Comprehensive Logging. The Governance focus area's Security Policy Framework holds the policy tier.
- **Declined:** AU-6 stays with Identity Threat Detection. AU-11, AU-9, and AU-12(1) belong to the SIEM Platform capability, which owns retention, integrity, and the system-wide audit trail.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Human Authentication, Identity Lifecycle and Governance, Directory/Platform Core Infrastructure, Cloud Account/Subscription/Tenant Boundary, Object/File Storage

**External Dependencies:** The IL5 cloud provider, whose native detection and logging services KESTREL inherits under its provisional authorization.

**Security Impact:** High

**Activities:**

- **DE-2.1.1: Control-Plane Activity Log Collection Centralization**
    - **Description:** Enable the control-plane activity log on every cloud account, subscription, tenant, and on-premises management platform the program operates, and route all of them to a single destination held outside the account that produced them.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping. Send records to a destination outside the account they describe, so an intruder holding that account cannot delete them. Verify regional and per-tenant coverage. Retention and immutability belong to the SIEM Platform capability.

- **DE-2.1.2: Consistent Logging Coverage Enforcement (infrastructure/identity sources)**
    - **Description:** Evaluate every account, subscription, and identity tenant continuously against the infrastructure and identity logging configuration the program requires, and remediate or block the ones that do not meet it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the all-components dimension of the outcome's AU-12 (partial) mapping. It is tagged Automate as policy-as-code replacing a manual audit of logging settings. It catches the account stood up outside the landing zone, which is usually the least governed one.

- **DE-2.1.3: Authentication Events Capture**
    - **Description:** Capture the successful, failed, and challenged authentication events from every identity provider, federated relying party, and legacy authentication path in the program's estate, preserving the principal, source, method, and outcome on each record.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping, the generation half paired with Authentication Activities Monitoring. Keep failed and challenged attempts, since password sprays and MFA fatigue show only there. Include legacy and non-federated paths.

- **DE-2.1.4: Identity Change Tracking**
    - **Description:** Capture every account creation, modification, enabling, disabling, and removal event, together with the group membership, role assignment, entitlement grant, consent, and directory configuration changes the estate produces, recording the acting principal on each.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-2(4) (partial) mapping and part of its AU-12 (partial) mapping. Capture consent grants and out-of-process permission changes, which default audit settings often miss. Record any change class the platform cannot emit in the CMP.

- **DE-2.1.5: Identity Log Retention Extension**
    - **Description:** Determine how long identity audit records must remain queryable to cover the program's investigation window, configure retention beyond the identity platform's default period to meet it, and document the period and its basis in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** AU-11 belongs to the SIEM Platform capability's Log Retention Strategy, so this activity sets only the identity-specific retention period. Default platform retention is often thirty days, shorter than typical dwell time. Cost is recurring, since extension is usually a licensing tier or paid export.

- **DE-2.1.6: Audit and Accountability Procedures**
    - **Description:** Document the procedures that implement the program's audit and accountability policy across every logging outcome, covering event selection, collection, retention, protection, review, and the response to logging failures, and review them annually.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-1 (partial) mapping for the procedures half. It covers all of Comprehensive Logging, so the per-source decisions sit in one procedure set.

### DE-2.2: Data Service Logging

**Design Intent:** Data-plane audit logs are on for every cloud database, storage service, vault, queue, and the data lake zones. Every read of a vault secret and every data lake access is logged with the identity that made it. The pipeline turns these logs on when it creates a resource, so no data service starts without them.

**NIST Control Mapping:**

- **AU-12 (partial):** the second of this capability's eight source-class slices, scoped to data-service events and disjoint from the other slices, on the basis set out under Infrastructure and Identity Logging.
- **Declined:** SI-4-family controls are held by Database and Storage Threat Detection and Secrets Vault Protection and Monitoring, which analyze these records.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Storage/Database, Infrastructure-as-Code (IaC), CI/CD Pipeline

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **DE-2.2.1: Resource Level Data Plane Logs**
    - **Description:** Enable the data-plane audit stream on each storage account, object store, file service, and platform service the program operates, so that individual read, write, delete, and list operations are recorded rather than only the management operations performed against the resource.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping, recording whether an intrusion reached a data store. Recurring cost is High because providers meter it per operation. Decide which stores warrant it against the Data focus area's classification and document that in the CMP.

- **DE-2.2.2: Log Storage Operations**
    - **Description:** Record every read, write, delete, retention-change, and export operation performed against the program's own log storage destinations, and route those records to a destination the log storage administrators do not control.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping applied to the logging system itself. Route these records away from the store they describe, so an administrator cannot edit both. AU-9 belongs to the SIEM Platform capability.

- **DE-2.2.3: Database Activity Auditing**
    - **Description:** Enable native database auditing on every relational engine the program operates, covering privileged operations, schema changes, permission grants, failed authorizations, and access to the tables holding the program's most sensitive data.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping and feeds Database and Storage Threat Detection. Scope audited objects by classification in the CMP, while auditing privileged and schema-changing operations everywhere. Keep failed authorization attempts in full.

- **DE-2.2.4: Secrets Access Monitoring**
    - **Description:** Enable the access log on every secrets, key, and certificate store the program operates, recording each secret read, write, list, rotation, and permission change with the requesting identity attached, so that retrieval of a credential is an event rather than an inference.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping as the record layer beneath Secrets Vault Monitoring and Threat Detection and the Identity focus area's Secrets Continuous Monitoring. Record list and read operations individually, so bulk enumeration shows as a signal.

- **DE-2.2.5: NoSQL Operations Tracking**
    - **Description:** Enable operation-level auditing on the document, key-value, graph, and wide-column stores the program operates, covering the query, index, and administrative operations those engines expose in place of the statement-level audit a relational engine provides.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping. It is separate from Database Activity Auditing because NoSQL engines log at the request or collection level without statement text. Scope it on the same classification basis, recorded in the CMP.

- **DE-2.2.6: Other Data Services Coverage**
    - **Description:** Enumerate the remaining data-bearing services the program operates, including message queues, event streams, caches, search indexes, analytics and warehouse services, and data pipelines, and enable each one's audit stream on the same terms as the stores above.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping for services no checklist names, such as a message queue carrying database records. Enumerate newly adopted services each period. Record any service with no audit stream in the CMP with its compensating record.

- **DE-2.2.7: Data Service Logging Automation**
    - **Description:** Express the required audit configuration for each data-service class as policy-as-code and deploy it through the program's infrastructure pipeline, so a newly created storage account, database, secrets store, or other data service inherits its audit settings at provisioning rather than acquiring them afterward.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it deploys the other activities' configuration. It is tagged Automate as a named practice. It stays separate from Container and Orchestration Logging Automation because data-service and cluster provisioning pipelines differ.

- **DE-2.2.8: Consistent Logging Coverage Enforcement (data-service sources)**
    - **Description:** Evaluate every storage account, database, secrets store, and other data service the program operates continuously against the audit configuration required for its class, and remediate or flag each instance that does not meet it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the all-components dimension of the outcome's AU-12 (partial) mapping. It is tagged Automate for continuous policy evaluation. It confirms the setting exists, while Audit Processing Failure and Silent-Source Alerting detects sources that go quiet.

### DE-2.3: Container and Orchestration Platform Logging

**Design Intent:** Every cluster's API server audit log, container runtime events, and image pull records go to the security monitoring platform. The pipeline enables these when it creates a cluster, so the dev, test, stage, prod, and training clusters are all covered.

**NIST Control Mapping:**

- **AU-12 (partial):** the third of this capability's eight source-class slices, scoped to container and orchestration events and disjoint from the other slices, on the basis set out under Infrastructure and Identity Logging.
- **Declined:** this outcome claims only audit-record generation. CM-2 and CM-7 stay with Secure Compute Baselines, SI-3 with Malicious Code Protection, RA-5 with Container Scanning, and SR-4 with Base Image Lineage Report and Trusted Registry ConMon Report.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Container, Container Orchestration Control Plane, Artifact/Model Registry, CI/CD Pipeline, Infrastructure-as-Code (IaC)

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DE-2.3.1: Kubernetes Control Plane Logging**
    - **Description:** Enable the API server audit log on every cluster the program operates under an audit policy that records authenticated requests, authorization decisions, exec and port-forward operations, secret access, and admission-controller outcomes, and ship it off the cluster.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping for cluster control-plane events. The audit policy is the deliverable, since the default records almost nothing and record-everything gets discarded unread. Keep exec and port-forward events at full request detail.

- **DE-2.3.2: Container Runtime Monitoring**
    - **Description:** Collect the container runtime event stream from every node the program operates, covering container start, stop, image pull, mount, privilege, and process-execution events, and forward it with the pod, namespace, and node identity attached.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping for container runtime events. The SI-3 (partial) claim of Container/Workload Runtime Protection (CWPP) is not reopened. Attach workload identity at collection, since container IDs vanish in minutes. It is Level 2 above the mandatory control-plane log.

- **DE-2.3.3: Container Image Tracking**
    - **Description:** Record every image push, pull, tag, promotion, and deletion event the program's registries produce, alongside the digest actually deployed to each cluster, so the image running in production can be traced back to the build that produced it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping for registry and deployment events. It feeds inventory, SR-4 provenance, and registry hygiene reporting without restating them. Key records to the image digest, not the mutable tag. It is Level 2 above the mandatory pre-deployment supply-chain controls.

- **DE-2.3.4: Container and Orchestration Logging Automation**
    - **Description:** Express the required audit configuration for the cluster control plane, container runtime, and image registry as policy-as-code and deploy it through the program's infrastructure pipeline, so a newly created cluster or registry inherits its audit settings at provisioning rather than acquiring them afterward.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it deploys the other activities' configuration. It is tagged Automate as a named practice. It stays separate from Data Service Logging Automation because cluster audit policy is admitted through the orchestration platform itself.

- **DE-2.3.5: Consistent Logging Coverage Enforcement (container/orchestration sources)**
    - **Description:** Evaluate every cluster, container runtime, and image registry the program operates continuously against the audit configuration required for its class, and remediate or flag each instance that does not meet it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the all-components dimension of the outcome's AU-12 (partial) mapping. It is tagged Automate for continuous policy evaluation across clusters and registries. It confirms the setting exists, while Audit Processing Failure and Silent-Source Alerting detects sources that go quiet.

### DE-2.4: Application/API Logging

**Design Intent:** Every application emits structured security events in a common format, including the authenticated user, each authorization decision, and each data access and release. Every AI agent also logs each tool call with its parameters, its result, and the human approval behind it. Every model endpoint logs its callers and quota decisions.

**NIST Control Mapping:**

- **AU-12 (partial):** the fourth of this capability's eight source-class slices, scoped to application, API, serverless, workflow, and agentic tool-call events and disjoint from the other slices, on the basis set out under Infrastructure and Identity Logging.
- **AU-3 (partial):** claimed for Structured Application Logging as the framework's only AU-3 claim. It is partial because provider-emitted source classes fix their own record content, which the coverage-enforcement activities verify.
- **Declined:** AU-3(1) adds detail beyond the required set, AU-3(2) is withdrawn in Rev 5, and AU-3(3) limits personally identifiable information, so the AU-3 base is cited.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Application/API, Serverless/Platform Service, Load Balancer/Reverse Proxy/API Gateway, AI/ML System

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DE-2.4.1: Web Application Activities Logging**
    - **Description:** Instrument each of the program's web applications to record its request, session, authentication, authorization, and state-changing events, preserving the acting user, source, and outcome on every record.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping for application-tier events, which only the application can attribute to a principal. Instrument authorization denials, in-application privilege changes, and state-changing transactions.

- **DE-2.4.2: API Gateway Operations Monitoring**
    - **Description:** Enable request and response logging on every API gateway the program operates, capturing the calling principal, route, method, status, latency, and policy decision for each call traversing the gateway.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping and feeds Runtime API Inventory and Governance, whose claims are not reopened. Record the calling principal, not just the client address.

- **DE-2.4.3: Serverless Function Execution Tracking**
    - **Description:** Enable invocation and execution logging on every serverless function and event-driven workload the program runs, recording the invoking principal or event source, the execution identity assumed, the duration, and the completion status.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping, since the execution record is all a serverless workload leaves behind. Record the invoking event source with the identity, so a bucket-triggered invocation is not attributed to the program itself.

- **DE-2.4.4: Business Process Workflows Logging**
    - **Description:** Record the business-transaction events the program's workflow, orchestration, and approval systems produce, covering the initiation, approval, modification, and completion of each transaction with the principal responsible for each step.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping, showing when a system was misused exactly as designed. It feeds Insider Threat Indicator Correlation and Investigation. It is Level 2, and a program may scope it to its highest-consequence workflows.

- **DE-2.4.5: Structured Application Logging**
    - **Description:** Define the program's structured log schema, fixing the event type, timestamp, source, principal, outcome, and correlation identifier every application record must carry, and require the program's applications to emit machine-parseable records conforming to it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-3 (partial) mapping, fixing the event type, time, location, source, outcome, and identity elements. Require a correlation identifier from the start. Enforce conformance through the shared logging library rather than per-application review.

- **DE-2.4.6: APM Telemetry**
    - **Description:** Collect the application performance telemetry the program's services produce, including distributed traces, dependency calls, error rates, and latency distributions, and carry the same request identifiers on it that the security records use.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since performance telemetry is not an audit record. Share a request identifier with the audit records so attacks can be told from outages. It is Level 3, and recurring cost is High because platforms price by trace volume.

- **DE-2.4.7: Application Security Event Logging**
    - **Description:** Emit an explicit security event from within each application for authentication failures, authorization denials, input-validation rejections, session anomalies, and administrative actions, distinct from the application's general request log.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping. It is separate from Web Application Activities Logging so security events stay findable rather than buried in request logs. Record authorization denials and input-validation rejections, which only the application observes.

- **DE-2.4.8: Agentic AI Tool-Call and Action Logging**
    - **Description:** Instrument each agentic tool-calling loop to emit a structured record of every tool call and action it takes, carrying the timestamp, tool called, parameters, result, agent session identifier, and, where applicable, the session termination reason.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping for agentic tool calls, recorded whether dispatched, blocked, or escalated. It is separate from Application Security Event Logging because a tool call needs its own schema of action, parameters, and result. Record each decision from Agentic Tool-Call/Action Output Validation and the principal Delegated Authority Attribution resolves. This record set is what AI/ML Incident Runbook Development and Red Team Finding Remediation Tracking and Validation read to investigate and confirm agentic incidents.

### DE-2.5: Host and Endpoint Logging

**Design Intent:** Log agents and EDR run on every virtual machine, privileged access workstation, and VDI desktop. They collect Windows security events and Linux system and audit logs, and they report agent health so a silenced agent is noticed.

**NIST Control Mapping:**

- **AU-12 (partial):** the fifth of this capability's eight source-class slices, scoped to host and endpoint events and disjoint from the other slices, on the basis set out under Infrastructure and Identity Logging. It is disjoint from Edge-Attack-Surface Logging's edge-tier records.
- **Declined:** SI-4-family controls are held by Endpoint Detection for the sensors forwarding here.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Virtual Machine/Server, Device/Workstation

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **DE-2.5.1: VM Monitoring Agents Deployment**
    - **Description:** Deploy the log-collection agent to every virtual machine and compute host in the program's fleet through the golden image and the provisioning pipeline, and treat enrollment as a property of the host rather than as a post-provisioning task.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping as the collection substrate, and opens no SI-4 claim since the detection sensor is EDR Sensor Deployment. Build the agent into the image so coverage holds as hosts are provisioned.

- **DE-2.5.2: Windows Security Event Collection**
    - **Description:** Collect the security, system, application, and PowerShell operational event logs from every Windows host under an audit policy that records the logon, privilege-use, process-creation, and object-access events detection content is written against.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping, and the audit policy is the deliverable. Enable process creation with command line, which defaults omit. Scope script-block logging to likely targets and record that scope in the CMP.

- **DE-2.5.3: Linux System Log Gathering**
    - **Description:** Collect the authentication, audit subsystem, kernel, and service logs from every Linux host under an audit rule set that records privileged command execution, authentication events, and changes to the files and configurations the host's security posture rests on.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping, separate from Windows because the audit subsystems differ. Maintain the rule set alongside the hardening baseline so a removed rule is a reviewable change.

- **DE-2.5.4: Endpoint Protection Monitoring**
    - **Description:** Forward the detection, quarantine, policy-change, tamper, and agent-health events the program's endpoint protection and detection agents produce into the central log pipeline alongside the operating-system records from the same hosts.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping without reopening Endpoint Detection's SI-4 (partial) claim. It lands endpoint detections beside other record classes. Forward agent health and tamper events, since a silent agent looks like a quiet host.

### DE-2.6: Edge-Attack-Surface Logging

**Design Intent:** The WAF's evaluated and blocked requests, the edge services' rate-limit hits, and the partner API's schema rejections all go to the security monitoring platform. There they are correlated per source and per partner to show attack attempts and API abuse.

**NIST Control Mapping:**

- **AU-12 (partial):** the sixth of this capability's eight source-class slices, scoped to edge-attack-surface events and disjoint from the other slices, on the basis set out under Infrastructure and Identity Logging. The edge and API tier owns these records, disjoint from Host and Endpoint Logging.
- **Declined:** enforcement claims are not reopened. SI-10 and CM-7(1) stay with Web Application Firewall, SC-5 with API Abuse Protection, and SA-11(6) and the other CM-7(1) half with Runtime API Inventory and Governance.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Network Infrastructure, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DE-2.6.1: Web Application Attack Monitoring**
    - **Description:** Collect the web application firewall's request records, including the rule matched, the action taken, and enough of the request to characterize the payload, for every request the WAF evaluated rather than only for the ones it blocked.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping for the WAF's events, without reopening Web Application Firewall's SI-10 (partial) claim. Record evaluated requests, not only blocks, to see reconnaissance. Bound payload capture in the CMP so the log does not store submitted credentials.

- **DE-2.6.2: Layer 7 Attack Attempt Capturing**
    - **Description:** Capture the application-layer attack attempts the edge tier observes beyond the WAF's own rule matches, including protocol abuse, request smuggling, bot and automation signatures, and credential-stuffing request shapes, as records carrying the source and the pattern matched.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping for attacks signatures miss, such as credential stuffing. It generates records without acting, so boundary controls are not reopened. It is Level 2 above the WAF and application floor.

- **DE-2.6.3: API Abuse Tracking**
    - **Description:** Record the abuse signals the program's API tier observes, including quota and rate-limit rejections, enumeration and scraping access patterns, anomalous parameter and object-identifier sequences, and repeated authorization failures attributable to a single caller.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping beneath enforcement outcomes whose SC-5 and inventory claims are not reopened. Record every refused attempt. Repeated authorization failures from one caller are the highest-value pattern, since they reveal object-identifier enumeration.

### DE-2.7: Network Security Logging

**Design Intent:** Flow logs from every spoke, the SDN fabric's flow telemetry, both hubs' allow and deny events, and both sides' DNS query logs go to the security monitoring platform. They are stitched into one view of each connection across the circuit.

**NIST Control Mapping:**

- **AU-12 (partial):** the seventh of this capability's eight source-class slices, scoped to network fabric events and disjoint from the other slices, on the basis set out under Infrastructure and Identity Logging. It claims the records, not the telemetry platform.
- **Declined:** SI-4 stays with Network Telemetry and Security Posture Visualization, which established the platform consumed here. SI-4 and SI-4(18) for resolver records stay with DNS Advanced Protection. SI-4(16) stays with Correlated Threat Detection and Analytics.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Routing/Switching Fabric, Network Firewall, DNS Infrastructure, Load Balancer/Reverse Proxy/API Gateway, Network Telemetry/Monitoring Platform

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DE-2.7.1: Network Flow Logs Capturing**
    - **Description:** Enable flow record collection across the program's virtual networks, subnets, network interfaces, and physical routing and switching estate, capturing source, destination, port, protocol, byte and packet counts, and disposition for every conversation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping, turning on sources the Centralized Network Telemetry and Analytics Platform carries. Cover east-west paths, not only the perimeter. Recurring cost is High, so record sampling decisions in the CMP.

- **DE-2.7.2: Firewall Activity Monitoring**
    - **Description:** Collect the allow, deny, session, and rule-change events from every firewall in the program's estate, cloud-native and physical alike, preserving the identity of the matched rule on each record.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping. Record the matched rule identifier with each event. Collect rule-change events too, since investigators reach for them first.

- **DE-2.7.3: DNS Query Data Collection**
    - **Description:** Collect the resolver query and response logs from every DNS resolution path the program operates, covering cloud-provider resolvers, on-premises servers, and endpoint-forwarded resolution, with the querying host or workload identity attached.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping and feeds DNS Advanced Protection, whose claims are not reopened. Attribute queries to the querying workload, not the forwarder. Record encrypted resolution that bypasses program resolvers as a coverage gap.

- **DE-2.7.4: Network Event Correlation**
    - **Description:** Stitch the flow, firewall, resolver, and proxy records describing one connection into a single record before forwarding, resolving address, port, and identity fields to a common representation so downstream analysis reads one account of the connection rather than four fragments of it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation and does not reopen the SI-4(16) (partial) claim held by Correlated Threat Detection and Analytics. It stitches records of one connection across address translation before detection reads them. It is Level 2 above the mandatory record generation.

- **DE-2.7.5: Network Traffic Flow Analytics**
    - **Description:** Derive the conversation-level analytics the flow record set supports, including top talkers, protocol and volume baselines, first-seen conversations, and unexpected egress destinations, and publish them as a standing view of what the network is actually carrying.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it consumes the Centralized Network Telemetry and Analytics Platform. It is tagged Visualize as a report surfacing status in actionable form. It describes what is normal, leaving maliciousness to detection content.

### DE-2.8: OT/Legacy Telemetry Ingestion and Normalization

**Design Intent:** The ground segment's passive sensors and the ground control stations' own logs are collected in the IT/OT DMZ, normalized to the platform's schema, and forwarded to the security monitoring platform. So is the payload processing workstation's legacy event log, which is translated from its older format.

**NIST Control Mapping:**

- **AU-12 (partial):** the eighth of this capability's source-class slices, scoped to OT and legacy telemetry capture and disjoint from the other slices, on the basis set out under Infrastructure and Identity Logging. Its normalized output feeds OT/Legacy Passive Monitoring and, through Security Telemetry Centralization, the enterprise correlation surface.
- **Declined:** SI-4(13) and SI-4(5) stay with OT/Legacy Passive Monitoring, which profiles, tunes, and alerts on process segments. AU-3 is not claimed, since a legacy protocol's record content cannot be changed at the source and is only reconstructed here. AU-3 sits with Application/API Logging.

**Deployment Type:** On-Premises, Cyber-Physical System (OT/ICS)

**Affected Components:** Industrial Controller/SCADA, Legacy IT (Unpatchable, Non-Industrial), OT/ICS Passive Network Monitoring, Virtual Machine/Server

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DE-2.8.1: OT/Legacy Protocol Telemetry Collection**
    - **Description:** Capture process-network protocol telemetry from the passive taps and span ports already positioned on the program's OT and legacy segments, decoding the industrial protocols in use into structured records without transmitting, polling, or otherwise placing anything on the segment.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping for telemetry capture, without reopening OT/Legacy Passive Monitoring's claims. Collect non-disruptively from existing taps, since an active poll can cause the consequence monitoring exists to prevent. Record undecodable proprietary protocols in the CMP rather than counting them as coverage.

- **DE-2.8.2: Telemetry Normalization to Common Schema for SIEM Ingestion**
    - **Description:** Map the decoded OT and legacy telemetry onto the program's common event schema, populating the event type, timestamp, source, asset, and outcome fields consistently so a process-network record can be joined to the identity, endpoint, and network records around it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping and produces the output Security Telemetry Centralization and OT/ICS-Aware Anomaly Detection consume. It is tagged Automate for the transformation pipeline. Resolve asset identity against the OT/Legacy Passive Protocol-Aware Discovery inventory rather than inferring it from an address.

- **DE-2.8.3: Legacy System Log Format/Protocol Translation**
    - **Description:** Translate the log output legacy IT systems produce in formats the enterprise pipeline cannot read, such as serial console streams, fixed-width mainframe records, and proprietary historian exports, into parseable records carried on the same common schema.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-12 (partial) mapping for legacy IT records in pre-pipeline formats, applying wherever a legacy IT system exists. Watch any intermediary, such as a terminal server or scheduled export, since it joins the audit path. It is Level 2 above the modern estate's mandatory logging.

## DE-3: SIEM Platform

### DE-3.1: SIEM Capabilities

**Design Intent:** The security monitoring platform runs on premises and receives every source class the logging outcomes produce. Its correlation rules come from the Security Team's rule repository, and its response automation is limited to what Endpoint Response allows. Dashboards serve the Security Team and the CSSP. AI-assisted triage summarizes alerts through a CSP-hosted foundation model, but it only advises and takes no action.

**NIST Control Mapping:**

- **AU-6 (partial):** the platform-executed review, analysis, and reporting across every record class except identity, which Identity Threat Detection holds. The two are tracked jointly. Detection content is authored by the Intelligent Detection Systems capability.
- **AU-6(1) (full):** carried by AI-Powered Analysis Integration and Detection/Correlation Rule Configuration, which integrate review through automated mechanisms. Identity Threat Detection, Endpoint Response, and Production Abuse Monitoring each reserved it for this capability.
- **AU-6(3) (full):** carried by Data Source Connections and Detection/Correlation Rule Configuration, which correlate records across repositories. The same outcomes, including the Extended Detection and Response (XDR) activity, reserved it here.
- **AU-7 (full):** the framework's only AU-7 claim, for report generation and for preserving original record content and order beside the normalized copy.
- **AU-7(1) (full):** the field-level process, sort, and search capability investigations run through.
- **AU-12(1) (partial):** the compilation half, assembling a system-wide trail from every source class. Time Synchronization holds the tolerance half, and the two are tracked jointly.
- **SI-4(12) (partial):** the program-wide residual Production Abuse Monitoring reserved, while that outcome holds the other, ML-serving slice.
- **Declined:** AU-12 belongs to the Comprehensive Logging capability. IR-family controls belong to the Response focus area and to Endpoint Response.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Security Information and Event Management (SIEM) Platform, Identity Platform, Network Infrastructure, Application/API, Device/Workstation, OT/ICS Device, Third-Party API Model

**External Dependencies:** The CSSP, which receives forwarded telemetry and adds its own detection under its service agreement. The IL5 cloud provider hosts the foundation model the triage assistant uses.

**Security Impact:** High

**Activities:**

- **DE-3.1.1: SIEM Platform Deployment**
    - **Description:** Field the SIEM platform itself, sizing its ingestion, indexing, and query capacity against the daily volume the program's source classes actually produce and placing an instance wherever an enclave cannot route its records outward.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Extensive
    - **Cost:** One-Time: High; Recurring: Extensive
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-7 (full) and AU-7(1) (full) mappings. Size ingestion against measured volume, since an undersized tier silently drops sources. An isolated enclave needs its own instance, which drives the recurring cost.

- **DE-3.1.2: Data Source Connections**
    - **Description:** Connect every source class the sibling Comprehensive Logging capability generates to the platform, and verify for each connection that records arrive parsed onto the common schema with their entity fields resolved rather than as unparsed text.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-6(3) (full) and AU-12(1) (partial) mappings. Confirm each connector parses as well as ingests. Silent-source watching belongs to Audit Processing Failure and Silent-Source Alerting. Keep this pipeline separate from Security Telemetry Centralization so the SIEM's correlation does not depend on a path this outcome does not control.

- **DE-3.1.3: Detection/Correlation Rule Configuration**
    - **Description:** Configure the platform's correlation engine, rule thresholds, suppression windows, and alert routing so that a matched rule raises an alert to the security organization with the records that produced it attached and the destination it is routed to already decided.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AU-6 (partial), AU-6(1) (full), and AU-6(3) (full) mappings and part of its SI-4(12) (partial) mapping. It configures the engine, thresholds, and alert routing, while Correlated Threat Detection and Analytics authors the detection logic. It is not tagged Automate because it is a configuration activity.

- **DE-3.1.4: Response Action Automation**
    - **Description:** Enable the response actions a matched rule may take on its own, covering enrichment, ticket creation, tagging, suppression, and notification, and explicitly bound which of them may fire before an analyst has read the alert.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's SI-4(12) (partial) mapping and is tagged Automate. Stop at enrichment, ticketing, and notification unless the Response focus area's procedures authorize more, and take no IR-family citation. Exclude OT and safety-critical systems from automation and route them to the human-in-the-loop path.

- **DE-3.1.5: Dashboard Monitoring**
    - **Description:** Build the platform views the security organization works from, covering the live alert queue and its aging, ingestion health and volume per connected source, and the summary of detection and response posture that leadership reads.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the report-generation dimension of the outcome's AU-7 (full) mapping and part of its AU-7(1) (full) mapping. It is the capability's designated Visualize instance, showing what the program is detecting rather than what it can detect. Build the ingestion-health view first.

- **DE-3.1.6: AI-Powered Analysis Integration**
    - **Description:** Integrate the platform's AI-assisted analysis into the triage path, scoping what it may summarize, correlate, and recommend, and require every assertion it makes to be traceable to the underlying records before an analyst acts on it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the core of the outcome's AU-6(1) (full) mapping and is tagged Automate as a named practice. Require summaries to trace back to their source records. A program-hosted model is governed under the Artificial Intelligence focus area. It is Level 3, does not apply without a vendor route, and is costed on consumption pricing.

### DE-3.2: Log Retention Strategy

**Design Intent:** Security logs stay searchable for 12 months and then move to the archive for 18 more, following OMB M-21-31. Alert and investigation records are kept for as long as their case or POA&M item requires, if longer. All security telemetry is also forwarded to the CSSP, which keeps its own copy under its service agreement.

**NIST Control Mapping:**

- **AU-4 (full):** tiering allocates enough storage to meet the program's retention periods.
- **AU-4(1) (full):** External Forwarding off-loads records onto systems other than those audited.
- **AU-11 (full):** reserved here by Infrastructure and Identity Logging and Training Job Audit Logging, whose source-specific periods act as floors under the program-wide policy set here.
- **AU-11(1) (full):** cited with the base because retaining records and still being able to read them fail independently.
- **Declined:** AU-5(1) belongs to Audit Processing Failure and Silent-Source Alerting.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Security Information and Event Management (SIEM) Platform, Backup/Archive Repository, Analytics/Warehouse Service

**External Dependencies:** The CSSP, which receives forwarded telemetry and adds its own detection under its service agreement.

**Security Impact:** Moderate

**Activities:**

- **DE-3.2.1: Tiered Storage Routing**
    - **Description:** Assign each record class to a hot, cold, or archive tier according to how long it stays worth querying interactively, configure the platform to move records between tiers automatically as they age, and document the tier boundaries and their basis in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-4 (full) mapping. Set the hot-to-cold boundary by how far back live investigations reach, not by cost alone. Measure rehydration latency and per-query cost before choosing it.

- **DE-3.2.2: Long-Term/Archive Retention Policy Configuration**
    - **Description:** Set the retention period each record class must meet against the program's investigation window and its AO-approved and regulatory obligations, configure the archive tier to enforce that period, and record each period and its basis in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-11 (full) and AU-11(1) (full) mappings. Run periodic restore-and-read tests, since an unparseable format or a rotated key destroys an archive. Where retention exceeds the vendor's maximum, meet the residual through External Forwarding.

- **DE-3.2.3: External Forwarding**
    - **Description:** Forward the record classes downstream systems require to their destinations, such as the program's data lake, a mission partner's archive, or a third-party retention service, and verify that each destination retains what it received before treating the forward as satisfying any retention obligation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-4(1) (full) mapping. Confirm the destination's own retention before counting the forward. In an isolated enclave, forward through the approved cross-domain path as an auditable transfer.

- **DE-3.2.4: Security Alert and Detection Data Retention/Archival Policy**
    - **Description:** Decide how long alerts, incident records, detection results, and analyst dispositions are kept independently of the raw telemetry that produced them, and document the period, its basis, and what each retained alert must carry in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity contributes the detection-data dimension of the outcome's AU-11 (full) mapping. Keep alert records longer than raw telemetry, with enough context to stand alone, since they are small and cheap. Incident case records follow the Response focus area's IRP terms, and the longer period governs.

### DE-3.3: Audit Log Integrity Protection

**Design Intent:** Log storage is write-once until retention expires, so no one, including the platform's own administrators, can change or delete a record early. Security Team members administer the platform's content, while the Platform Team runs its infrastructure, and neither can do the other's job. A source that goes silent or an ingestion failure alerts the Security Team.

**NIST Control Mapping:**

- **AU-5 (full), AU-5(1) (full):** carried by Audit Processing Failure and Silent-Source Alerting, which adds the silent-source watch the Consistent Logging Coverage Enforcement activities deferred here.
- **AU-9 (partial):** scoped to the centralized destination and its logging tooling, as Log Storage Operations deferred. Two Protect pillar outcomes hold their source-side stores, and the set is tracked jointly.
- **AU-9(2) (full):** the repository sits on a system separate from those audited.
- **AU-9(3) (partial):** cryptographic protection of centrally held records for the general source population. Approver and Reviewer Audit Log, Training Job Audit Logging, and Data Provenance and Lineage Verification hold the other slices.
- **AU-9(4) (full):** only a subset of privileged users may manage audit logging.
- **Declined:** AU-9(6) governs read access rather than administration, and would map onto the same activity if tailored in. AU-5(2) is covered by the alerting timeframe the AO sets on the base.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Security Information and Event Management (SIEM) Platform, Privileged Access Management

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **DE-3.3.1: Write-Once/Immutable Log Storage Configuration**
    - **Description:** Configure the centralized log store with an immutability or retention lock that prevents modification and deletion of a record before its retention period expires, including by the account that administers the store itself, and bind stored records cryptographically so that later alteration is detectable.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-9 (partial), AU-9(2) (full), and AU-9(3) (partial) mappings. Use a compliance-mode lock, since a governance-mode lock can be shortened by a privileged account. Add cryptographic binding so integrity holds against the operator too.

- **DE-3.3.2: Log Administrator and System Administrator Duty Separation**
    - **Description:** Restrict administration of the logging platform, its retention settings, and its collection configuration to a role held only by people who hold no administrative rights on the systems being audited, and record the separated roles and the break-glass exception in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-9(4) (full) mapping. Verify effective permissions, since a tenant's global administrator often holds implicit authority over the log workspace. Keep break-glass access, with every use alerting through Audit Processing Failure and Silent-Source Alerting.

- **DE-3.3.3: Audit Processing Failure and Silent-Source Alerting**
    - **Description:** Alert the security organization when the logging pipeline fails, when its allocated storage volume approaches capacity, and when a source that reported yesterday has stopped reporting today, and decide for each case what the platform does next.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-5 (full) and AU-5(1) (full) mappings. Build a per-source arrival expectation, since a silent source raises no error. Decide in advance whether a full log overwrites or halts, and record that in the CMP. Watch every connection Data Source Connections establishes.

### DE-3.4: Time Synchronization

**Design Intent:** The data center runs its own time servers, disciplined by GNSS and checked against DoD's authoritative time service. Every data center host, network device, and ground segment device syncs to them. Cloud workloads use the provider's time service, and drift between the two sides is monitored. Timestamps everywhere are UTC in one format, and drift alerts the Platform Team.

**NIST Control Mapping:**

- **AU-8 (full):** cited bare, since its Rev 5 enhancements were withdrawn. Timestamp Format Validation covers internal-clock, UTC or offset, and granularity requirements.
- **AU-12(1) (partial):** the tolerance half, with the compilation half held by SIEM Capabilities and tracked jointly.
- **SC-45 (full), SC-45(1) (full):** claimed across the Windows, Linux, and NTP activities and drift monitoring. Rev 5 moved the Rev 4 AU-8(1) and AU-8(2) synchronization obligations here.
- **SC-45(2) (full):** the designated secondary source. Where an enclave cannot separate it geographically, the AO tailors the parameter to separate power and network paths.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Virtual Machine/Server, Device/Workstation, Network Infrastructure, Directory/Platform Core Infrastructure, Industrial Controller/SCADA

**External Dependencies:** The IL5 cloud provider's time service, and DoD's authoritative time service that the data center's time servers check against.

**Security Impact:** High

**Activities:**

- **DE-3.4.1: Windows Time Sync**
    - **Description:** Configure the Windows estate to take time from the focus area hierarchy's authoritative root, and configure that root to synchronize against the program's designated authoritative source rather than against its own virtualization host.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SC-45 (full) and SC-45(1) (full) mappings. Check that a virtualized forest-root domain controller is not taking time from the hypervisor. Confirm no member has a manual override.

- **DE-3.4.2: Linux Time Sync**
    - **Description:** Point the Linux and container-host estate at the program's designated authoritative source through a single managed client, and disable or remove the competing time daemons a distribution ships enabled by default.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SC-45 (full) and SC-45(1) (full) mappings. Watch for two sync clients on one host, which causes intermittent offset. Count coverage per host, since containers share the kernel clock.

- **DE-3.4.3: Custom NTP Servers**
    - **Description:** Stand up the program's own stratum time servers where an external or provider-operated source cannot be reached or accredited, designate a primary and a secondary on separate power and network paths, and point the estate's clients at both.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-45(2) (full) mapping and part of its SC-45(1) (full) mapping. Isolated enclaves need a locally disciplined reference, such as a GPS-backed appliance. Authenticate the time protocol where supported. It is Level 2 because a reachable accredited source meets the obligation.

- **DE-3.4.4: Timestamp Format Validation**
    - **Description:** Verify that every source writes timestamps in UTC or with an explicit offset and at the granularity the program requires, and normalize at ingest the sources that do neither.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-8 (full) mapping. Reject local time without an offset, which reorders events at daylight-saving boundaries and across zones. Flag sources that record only whole seconds.

- **DE-3.4.5: Time Drift Monitoring**
    - **Description:** Measure each host's clock offset against the authoritative source continuously, alert when a host exceeds the tolerance the program's correlation depends on, and record that tolerance and its basis in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the compare-and-synchronize half of the outcome's SC-45(1) (full) mapping and the whole of its AU-12(1) (partial) mapping. Derive the tolerance from what correlation needs. Measure continuously, since drift returns whenever a host loses its sync path.
