# DA: Data

*KESTREL SADD, Section 5 (Protect). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## DA-1: Data Awareness and Classification

### DA-1.1: Data Discovery, Labeling, and Classification

**Design Intent:** KESTREL's label set combines the CUI category, dissemination markings such as releasability to partner nations, the owning mission team, and the payload vendor whose terms apply. The Data Team labels every record at ingest and keeps the catalog. Discovery scans run across the data lake zones, the cloud databases, the report index, the service desk, and backups. They find anything unlabeled or labeled inconsistently with its content.

**NIST Control Mapping:**

- **CM-12 (partial):** the framework's only claim of the control, for documenting where sensitive information resides and which components hold it. It is partial because tracking location changes over time also rests on the DMP's retention and disposition schedule.
- **CM-12(1) (full):** the two activities are the automated tooling that identifies information on system components, across unstructured and structured stores.
- **AC-16 (partial):** associates classification attributes with information in storage, a partial slice. AC-16(3) is held by the Artificial Intelligence focus area, and AC-16(7) and AC-16(10) by Attribute-Based Data and Application Access Enforcement (ABAC).
- **AC-16(1) (partial):** associates attributes dynamically as data is created, ingested, or changed, a partial slice beyond the scheduled sweep.
- **Declined:** RA-2 belongs to the Manage pillar's Security Categorization, while this outcome only labels data against those information types.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Object/File Storage, Self-Hosted Third-Party Application (COTS), Database Service, Analytics/Warehouse Service

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **DA-1.1.1: Data Discovery and Classification**
    - **Description:** Deploy discovery scanning across the program's file shares, object storage, collaboration platforms, and endpoints, and apply the program's classification labels to the sensitive information those scans locate.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-12, CM-12(1), and AC-16(1) mappings. Run the first pass in report-only mode and tune the detection patterns before letting it write labels, since mislabeling at scale is hard to undo. Store ownership records from the Device and Infrastructure focus area are a practical prerequisite for adjudicating labels.

- **DA-1.1.2: Database Classification and Integration**
    - **Description:** Enable the native sensitivity-classification features of the program's database and data-warehouse platforms, and feed the column- and field-level labels they produce into the same classification inventory the discovery scanner writes to.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-16 (partial) mapping for structured data. It is Level 2 because the sibling activity meets the discovery floor, while the value here is column-level granularity. Integrating labels with DLP, rights-management, and access-policy tooling is what makes the work pay off.

### DA-1.2: Attribute-Based Data and Application Access Enforcement (ABAC)

**Design Intent:** One policy engine decides data access from user and data attributes, namely team, payload vendor rights, role, partner nation, and the record's labels. Its enforcement points are every application and partner-facing API, each data lake zone, and the report index's retrieval. KESTREL holds no classified compartments, so the payload vendor split is enforced like a compartment, and flows between zones are allowed only where F18 permits. Policy changes are tested against a fixed set of access cases before deployment.

**NIST Control Mapping:**

- **AC-3(13) (partial):** enforces attributes at the data and application layers. The Identity focus area's Adaptive, Risk-Based Access Control holds the access-time slice, and the two are tracked together.
- **AC-3(3) (partial):** the framework's only claim, for the classification and compartment rule no user or data owner can override. It is partial because it covers only the access paths this outcome's enforcement points sit on.
- **AC-4(1) (partial):** uses attributes to enforce flow between compartments inside one classification level. Cross Domain Solution (CDS) Transfer Procedures holds the other flow slices for movement between levels.
- **AC-16(7) (partial):** ensures every enforcement point reads the same attribute the same way, in partial support of the decision point design.
- **AC-16(10) (partial):** the schema activity defines and changes the attribute types and values available, as one partial slice of the enhancement.
- **AC-24 (partial), AC-24(1) (partial):** the framework's only claims, for deciding each request before enforcement and passing the result to enforcement points. They are partial because enforcement coverage depends on the access paths integrated.
- **AC-21 (partial):** the framework's only claim, for checking a partner's clearance, compartment, and need-to-know against the information's labels before a share. It is partial because access outside program systems is verified through the PSO.
- **Declined:** AC-16 at the base is held by Data Discovery, Labeling, and Classification. AC-16(3) is held by the Artificial Intelligence focus area's Retrieval-Augmented Generation (RAG) and Vector Store Security.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** First-Party/Custom Application Code, API/Interface Contract, Database Service, Object/File Storage, Directory/Platform Core Infrastructure

**External Dependencies:** The payload vendors, whose data rights terms the vendor attributes encode.

**Security Impact:** High

**Activities:**

- **DA-1.2.1: Attribute and Policy Schema Definition**
    - **Description:** Define the subject, resource, action, and environmental attributes the program's access policies may reference, fix each attribute's permitted values and authoritative source, and document the schema and its change process in the DMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-16(10) and AC-16(7) mappings. Name an authoritative source for every attribute, and admit only attributes the program can actually keep current. Version the schema, because a policy set cannot be reasoned about once its vocabulary shifts underneath it.

- **DA-1.2.2: Policy Decision Point/Policy Engine Deployment**
    - **Description:** Deploy the policy decision point that evaluates access requests against the attribute schema, and configure it to return an explicit allow or deny decision, with any accompanying obligations, for every request routed to it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-24 (partial) mapping. Availability and latency decide whether the deployment holds, since every consulting application depends on the engine. Choose fail-closed or fail-open deliberately, and turn on decision logging at deployment so the program can explain why any access was permitted.

- **DA-1.2.3: Policy Enforcement Point Integration at Data and Application Access Paths**
    - **Description:** Integrate enforcement points into the program's application entry points, API gateways, and data access layers so that every path reaching a protected resource consults the policy decision point before data is returned.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-3(13) and AC-24(1) mappings. Coverage is the whole control, so enumerate access paths such as service accounts with direct database credentials before integrating them. Integrate application and data enforcement together, since an application-only deployment just moves access to the data tier.

- **DA-1.2.4: Classification-to-Attribute Mapping and Policy Testing**
    - **Description:** Map each classification label the discovery outcome assigns to the resource attributes the policy schema defines, and test the resulting policies against known allow and deny cases before they take effect.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is tagged Automate for the policy-as-code test suite, and it runs on a change to the policy set, schema, or classification scheme. Write deny cases first, because allow-only tests also pass when policy grants everyone access. Test against the deployed decision point, not a local evaluator.

- **DA-1.2.5: Clearance, Compartment, and Need-to-Know Attribute Integration**
    - **Description:** Integrate each user's clearance level, compartment and program accesses, and need-to-know determinations from their authoritative records as subject attributes the policy decision point evaluates, and withdraw an attribute as soon as the record withdraws the access it represents.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's AC-3(13) (partial) mapping. The authoritative records are the PSO's clearance and access records, which the SABER consumes but does not manage. It is Level 2 because AC-3(13) sits outside the system baselines, but it is mandatory wherever the program holds sensitive compartmented information or special access program data. Drive the integration from source events so a revoked read-in leaves the attribute store promptly.

- **DA-1.2.6: Compartment Separation and Flow Enforcement**
    - **Description:** Enforce classification and compartment policy as a non-discretionary rule no user or data owner can override, and block or route for review any flow that would move information into a compartment, program, or classification its labels do not permit.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-3(3) (partial) and AC-4(1) (partial) mappings, and also the outcome's AC-21 (partial) mapping for shares to mismatched recipients. Movement between classification levels goes through Cross Domain Solution (CDS) Transfer Procedures instead. It is Level 2 because AC-3(3) and AC-4(1) sit outside the system baselines, but it is mandatory wherever the program holds sensitive compartmented information or special access program data. Write the aggregation combinations the classification guidance identifies into the policy.

### DA-1.3: Data Provenance and Lineage Verification

**Design Intent:** Every feed is tagged with its origin at ingest, and provenance is written to an append-only log the Data Team cannot edit. Feeds include aircraft recordings, federated updates, analyst corrections, and products released from the IL6 enclave. Training snapshots and partner releases verify provenance before they use a record, so data of unknown origin never trains a model or reaches a partner.

**NIST Control Mapping:**

- **SR-4 (partial):** the ingested-data slice of provenance, one of several partial SR-4 slices tracked together, with other slices held by the Application and Artificial Intelligence focus areas. Dataset Lineage and Version Control declined SR-4 because this outcome is its dependency.
- **SR-4(2) (partial):** traces a record through its transformations, while the Application focus area holds base-image ancestry under the same enhancement.
- **SR-4(3) (partial):** validates at consumption that a record is genuine and unaltered, while Model Provenance and Integrity Verification holds the model-artifact slice.
- **AU-9(3) (partial):** cryptographically protects the provenance ledger at capture, against modification by a platform administrator. Audit Log Integrity Protection holds the general claim over centrally held records.
- **Declined:** AU-10(1) and AU-10(2) stay with Dataset Lineage and Version Control, since this outcome claims the custody record rather than non-repudiable attribution.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Object/File Storage, Database Service, First-Party/Custom Application Code, AI/ML System, Industrial Controller/SCADA

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DA-1.3.1: Data Source/Origin Tracking**
    - **Description:** Register every feed, dataset, and external source the program ingests along with its owner, transfer mechanism, and authorization basis, and reject ingestion from any source absent from that register.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4 (partial) mapping. It is tagged Automate for the enforced rejection at the ingestion path. The register's value is making an unregistered feed visible, since an unmanaged integration and a deliberate injection look the same until someone asks who owns the source.

- **DA-1.3.2: Provenance Metadata Capture and Immutable Logging**
    - **Description:** Capture origin, transfer, and transformation metadata at each ingestion and processing step, and write it to an append-only store the processing pipelines have no permission to modify or delete.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4(2) (partial) mapping. Immutability is the substance of the activity, because a record the transforming pipeline can rewrite proves nothing once that pipeline is compromised. Set a long retention for these records in the DMP's disposition schedule.

- **DA-1.3.3: Provenance Verification at Consumption/Use Points**
    - **Description:** Check the provenance record where data is read for analysis, training, or operational use, and block or flag any record whose chain of custody is missing, incomplete, or unverifiable.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SR-4(3) (partial) mapping and is tagged Automate for the check in the consumption path. Decide per consumption point whether an unverifiable record blocks or flags, and record it in the DMP, since blocking an operational feed has an availability cost.

### DA-1.4: Database and Storage Threat Detection

**Design Intent:** The cloud provider's threat detection runs on every cloud database and storage service. Access analytics in the security monitoring platform cover the data lake zones on premises. Alerts cover unusual reads, bulk exports, and access from an unexpected spoke, and the Security Team investigates each one.

**NIST Control Mapping:**

- **SI-4 (partial):** an independent base claim scoped to the data-service layer, watching the shape of data access that endpoint and network detection do not see. Other partial slices sit at the resolution, endpoint, and network layers.
- **SI-4(2) (partial):** near-real-time automated analysis of data-service events, a partial slice alongside identity-platform monitoring.
- **SI-4(5) (partial):** alerts on system-generated indications of compromise, a partial slice alongside OT/Legacy Passive Monitoring.
- **Declined:** IR-4 belongs to the Operate pillar, and the investigation activity here only covers triage and handoff.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Database Service, Object/File Storage, Virtual Machine/Server

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider supplies the database threat detection service.

**Security Impact:** Moderate

**Activities:**

- **DA-1.4.1: Threat Detection Tool Deployment for Data Services**
    - **Description:** Enable the native threat detection service on each managed database and storage platform the program operates, and deploy equivalent agent-based or log-based detection for the self-managed data services those native services do not reach.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4 and SI-4(2) mappings. Coverage is usually lost on the self-managed half, such as a legacy database on a virtual machine that often holds the oldest, most sensitive data. Forward findings to central monitoring so they correlate with identity and network events.

- **DA-1.4.2: Anomalous Query/Access Pattern Alerting**
    - **Description:** Tune the detection rules to alert on the access patterns that matter for this program's data, including bulk reads, unusual export volumes, privilege escalation against the data plane, and connections from unexpected principals or networks, and record the thresholds in the DMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(5) (partial) mapping and is tagged Automate for the rule-driven alerting. Run a baseline period before enforcing volume thresholds, so legitimate analytics workloads do not flood the source with noise. Record thresholds in the DMP rather than only in the tool.

- **DA-1.4.3: Threat Finding Investigation Workflow**
    - **Description:** Define who triages each data-service threat finding, what evidence is collected before the finding is closed, and how a confirmed finding is escalated into the program's incident response process.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Name the data owner as a participant, since only the owner can say whether an account had a business reason to read the data. Collect evidence at triage, before the platform's own logs age out. Escalation hands confirmed findings to the Operate pillar's incident response process.

### DA-1.5: Data Loss Prevention (DLP) and Monitoring

**Design Intent:** KESTREL's data leaves only by named paths, so DLP watches each one. The partner-facing APIs and the cross domain transfer gateway check every release against its markings, and anything not releasable is blocked. The experimentation workspaces and VDI desktops block downloads and clipboard. Insider risk analytics flag bulk reads across zones, and the data security dashboard shows all of it to the Security Team.

**NIST Control Mapping:**

- **AC-4 (partial):** enforces flow authorizations by the content's classification, a partial slice disjoint from the Network and Environment focus area's position-based flow slices. The base is cited because the filter enhancements address cross-domain transfer.
- **SI-4(18) (partial):** analyzes outbound content at egress points, a partial slice alongside DNS Advanced Protection's covert-channel claim.
- **AC-2(12) (partial):** monitors accounts for atypical data access to feed insider risk scoring, a partial slice alongside the Identity focus area's Emergency Access.
- **Declined:** PM-12 belongs to the Operate pillar's User/Entity Behavior Analytics (UEBA) / Insider Threat Detection, which this outcome complements.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Network Infrastructure, Application/API, Object/File Storage, Database Service

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DA-1.5.1: DLP Policy/Rule Definition**
    - **Description:** Define the content patterns, classification labels, and destination conditions that constitute a DLP violation for each data class, state the action each violation triggers, and record the rule set and its exception process in the DMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Write rules against classification labels first, since labels survive reformatting and copying, and keep pattern rules for unlabeled residue. Define rules for the program's own controlled markings and nicknames early, because vendor content packs cannot supply them. Give the exception process equal attention, so users have a sanctioned path for releasable files.

- **DA-1.5.2: Insider Risk Behavioral Analytics**
    - **Description:** Score each principal's data-access behavior against its own history and its peer group to surface the staging patterns that precede exfiltration, including bulk collection, off-hours access, and reads outside an assigned scope.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-2(12) (partial) mapping and is tagged Automate for the scoring engine. It covers access to the program's classified data holdings for data owners, while the Operate pillar's enterprise layer serves the insider threat program. Settle scope, retention, and score visibility with the PSO and program counsel, and record them in the DMP.

- **DA-1.5.3: Monitoring and Response Configuration**
    - **Description:** Deploy the DLP policy across the program's egress paths, covering mail, web and cloud upload, endpoint peripherals, and managed file transfer, and set each rule to monitor, warn, or block according to the action the policy assigns it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-4 and SI-4(18) mappings and is tagged Automate for inline inspection and blocking. Start each rule in monitor mode and promote it to block once its false-positive rate is known. The endpoint agent enforces the same policy on the peripheral path, complementing the Device and Infrastructure focus area's Device Control.

- **DA-1.5.4: Data Security Posture Dashboard**
    - **Description:** Build a dashboard presenting classification coverage across the program's stores, DLP incident volume and disposition, and encryption compliance as one posture view for the PMO ISSE and data owners.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it presents what other outcomes produce, and it is Level 2 for that reason. Put classification coverage first, because every other figure depends on it. Draw encryption figures from the Data Encryption capability's compliance monitoring.

### DA-1.6: Data Rights Management (DRM)

**Design Intent:** Report documents released to partner nations carry rights protection that limits them to the receiving nation and expires them on the foreign disclosure officer's terms. Machine-readable detections released through the partner API are not wrapped, since partner systems consume them directly. Their release is governed by the release review and the memoranda of agreement instead.

**NIST Control Mapping:**

- **AC-3(8) (partial), AC-3(9) (partial):** the framework's only claims, for revoking access after an attribute change and for releasing information only to environments that enforce protection.
- **SC-28(1) (partial):** encryption bound to the file itself, a partial slice disjoint from the storage-tier claims of the Data Encryption capability.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Application/API, Object/File Storage, Human Authentication

**External Dependencies:** Each partner nation, whose systems must honor the rights protection under its memorandum of agreement.

**Security Impact:** Low

**Activities:**

- **DA-1.6.1: DRM Policy Classification Mapping**
    - **Description:** Decide which classification labels and document types require persistent rights protection, and record in the DMP the mapping and the permitted rights sets for view, print, copy, forward, and offline access.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Scope persistent rights narrowly to documents released outside the program's control, since applying them everywhere drives users around the control. Set the offline access window here, because it is both the usability parameter and the revocation gap.

- **DA-1.6.2: Persistent Access Control/Encryption Binding**
    - **Description:** Configure the rights management service to encrypt each in-scope file and bind its assigned rights set to it at creation or release, so that opening the file anywhere requires a rights evaluation against the program's identity platform.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-3(9) and SC-28(1) mappings. It is tagged Automate because protection applies from the classification label rather than the author's choice. Confirm file-format coverage first, since rights binding is weak for engineering, imagery, and archive formats, and manage rights-service keys under the KMP.

- **DA-1.6.3: DRM Revocation and Expiration Enforcement**
    - **Description:** Configure the revocation and expiration paths so that a released file's rights can be withdrawn or allowed to lapse, and exercise both on a recurring basis to confirm a revoked file is unreadable at its next rights evaluation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-3(8) (partial) mapping. Exercise revocation rather than assume it, since a cached offline license stays readable until it expires. Configure expiration too, because it does not depend on anyone remembering to revoke.

### DA-1.7: Dataset De-Identification and Disclosure Review

**Design Intent:** KESTREL releases no datasets outside the program today. Any future dataset release, such as one to a partner nation or a research laboratory, needs de-identification of incidental imagery of people. It also needs a re-identification test and approval from the privacy officer and the foreign disclosure officer. KESTREL publishes no public content beyond its vulnerability disclosure listing.

**NIST Control Mapping:**

- **SI-19 (partial):** decides and applies de-identification to a dataset prepared for release. It is partial because the Artificial Intelligence focus area holds the slices for data inside training and inference pipelines, split by artifact class.
- **SI-19(3) (partial):** the framework's only claim, for the documented decision to disclose a de-identified dataset outside the program's control.
- **SI-19(4) (partial):** removes, masks, or replaces direct identifiers in a release dataset, on the same partial artifact-class split as the base.
- **SI-19(8) (partial):** runs the motivated-intruder test against the released dataset. The Artificial Intelligence focus area's Privacy-Attack Testing holds the model-weights slice, and the two are tracked together.
- **AC-22 (full):** Publicly Accessible Content Review designates posters, trains them, and reviews content before and after posting, and no other outcome claims the control.
- **Declined:** SI-19(6) is not claimed, since many programs use masking with no perturbation mechanism, though a differentially-private release could become a future slice. AC-3(9) stays with Data Rights Management, because a de-identified release carries no persistent technical control.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Database Service, Object/File Storage

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DA-1.7.1: De-Identification Technique Application for Release Datasets**
    - **Description:** For a classification tier with no technique yet on record, decide the masking, generalization, or differential-privacy technique and the utility floor the released dataset has to meet and document that mapping in the DMP, then apply the technique and parameters the DMP assigns to each dataset slated for release or sharing outside the program and document the basis on which the de-identified result is released.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-19 (partial), SI-19(4) (partial), and SI-19(3) (partial) mappings. SI-19(3) sits here because the release act cannot be separated from the technique decision, so record why the technique and parameters suffice for each disclosure. It is Level 2 as written and rises to Level 1 for any program whose tailored baseline includes SI-19(3). Draw parameters from the DMP, and treat free text, imagery, and geospatial detail as the likeliest re-identification paths.

- **DA-1.7.2: Motivated-Intruder Re-Identification Testing**
    - **Description:** Perform a motivated-intruder re-identification test against the de-identified dataset, using publicly available and reasonably obtainable auxiliary information, before the dataset is released.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-19(8) (partial) mapping, and it is tracked with the Artificial Intelligence focus area's Privacy-Attack Testing. It is Level 2 as written and rises to Level 1 where the tailored baseline includes SI-19(8) for dataset release. Use auxiliary data a real intruder could obtain, such as public records and breach corpora. It is not tagged Automate because choosing sources and linkage strategies is analyst work. A successful re-identification blocks the release and returns the dataset for stronger parameters or a narrower scope, with the finding recorded against the DMP. A program releasing both a dataset and a model from the same corpus should run both test suites before either release.

- **DA-1.7.3: Publicly Accessible Content Review**
    - **Description:** Designate the individuals authorized to post information to publicly accessible systems, review proposed content for nonpublic information before it is posted, and review posted content periodically, removing anything nonpublic that is found.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-22 (full) mapping. Many classified programs publish nothing and tailor it out. However, a program with any public presence, such as a recruiting page or a released dataset, needs the review.

### DA-1.8: Media Protection Policy and Procedures

**Design Intent:** Removable media is prohibited except for the aircraft's mission storage modules, which are marked CUI, logged when they leave an aircraft, and transported in controlled containers. Failed drives and retired storage modules are sanitized on site before disposal. KESTREL holds no classified data, so no media is downgraded, and data moves to and from the IL6 enclave only through the cross domain solution.

**NIST Control Mapping:**

- **MP-1 (partial):** the media-protection procedures this outcome issues, while the Manage pillar holds policy issuance and review. MP-1 has no enhancements, and neither do MP-2, MP-3, MP-4, or MP-7.
- **MP-3 (partial):** carried by the marking activity, with policy obligations held by the Manage pillar.
- **MP-2 (partial), MP-4 (partial), MP-5 (partial), MP-5(3) (partial):** carried by the handling and transport activity, MP-5(3) for the custodian used when media leaves a controlled area.
- **MP-7 (partial):** the procedural half of media use restriction, tracked with the Device and Infrastructure focus area's Device Control, which holds the technical half.
- **MP-6 (partial), MP-6(1) (partial):** the physical-media slice of sanitization and its verification, while Resource Decommissioning Governance holds the logical teardown slice.
- **MP-6(2) (partial):** periodic testing of sanitization equipment and procedures.
- **MP-8 (partial):** the downgrading process that sanitizes or reclassifies media for reuse or release at a lower level, distinct from MP-6 disposal.
- **MP-8(1) (partial):** documents that process, its methods, and its tools.
- **MP-8(2) (partial):** periodic testing of downgrading equipment, tracked jointly with the MP-6(2) claim since the same equipment usually serves both.
- **MP-8(3) (partial):** the controlled unclassified information case, met when media leaves an IL5 environment.
- **MP-8(4) (partial):** the classified-information case, the usual driver on a multi-enclave program.
- **SI-12(3) (partial):** disposal techniques applied to information itself, which other focus areas' registry hygiene outcomes declined and left to the Data focus area.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Virtual Machine/Server, Industrial Controller/SCADA

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **DA-1.8.1: Media Marking and Labeling Procedures**
    - **Description:** Define how each class of digital and non-digital media is marked with its classification, handling caveats, and accountability identifier, and state the exemptions permitted within designated controlled areas.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's MP-3 (partial) mapping. Draw marking conventions from the security classification guide, and extend them to media types the guide does not list. State the controlled-area exemption explicitly, because unmarked media inside the area becomes unmarked media outside it.

- **DA-1.8.2: Removable Media Handling and Transport Controls**
    - **Description:** Specify who may use, store, and transport removable media, under what accountability record, and with what protection in transit, and restrict use to media the program has issued and registered.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's MP-2, MP-4, MP-5, MP-5(3), and MP-7 mappings. Write the procedure against the Device and Infrastructure focus area's Device Control, so the allowlist and the issuing process match. Address media that bridges into air-gapped or OT environments explicitly.

- **DA-1.8.3: Media Sanitization and Destruction Procedures**
    - **Description:** Define the sanitization or destruction method required for each media type and classification prior to reuse, transfer, or disposal, and require verification and a signed record for every action performed.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's MP-6, MP-6(1), MP-6(2), and SI-12(3) mappings. Choose the method from media type and classification together, and default to destruction for high-classification flash media. The verification and signed record are the substance of MP-6(1). Test degaussing and destruction equipment on a defined cadence, which also covers the MP-8(2) claim where the equipment downgrades.

- **DA-1.8.4: Media Downgrading Procedures**
    - **Description:** Define the downgrading process, methods, and tools required to sanitize media from a higher classification or sensitivity level for reuse or release at a lower one, and require documented approval, tracking, and verification for every downgrading action performed.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's MP-8, MP-8(1), MP-8(2), MP-8(3), and MP-8(4) mappings. Downgrading returns media to service at a lower level, such as moving from a SAP-unique enclave to collateral SECRET, unlike sanitization, which ends its life. MP-8(2) shares the MP-6(2) equipment testing, extended to any dedicated downgrading equipment. Mirror MP-6(1)'s approval and verification discipline, since a failed downgrade is a disclosure.

### DA-1.9: Data Management Plan (DMP)

**Design Intent:** The Data Team authors KESTREL's DMP, with the retention schedule, minimization rules, and classification scheme in one document. The intelligence mission leads approve retention for their data, and the privacy officer approves the handling of personal information. The Configuration Control Board approves the DMP, and it is revised each year and whenever a new payload vendor or data type is added.

**NIST Control Mapping:**

- **SI-12 (partial):** retention and disposition of the program's data holdings. Program-wide records management stays with the Manage pillar, and other focus areas hold build and model artifact retention.
- **SI-12(1) (partial):** the deciding half of limiting retained personal information, tracked with Inference-Time PII Handling, which holds the applying half.
- **SI-12(2) (partial):** minimizes personal information in test, training, and research data, which the Artificial Intelligence focus area's Privacy Requirements Definition defers to this outcome.
- **Declined:** SI-12(3) is held by Media Sanitization and Destruction Procedures.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Storage/Database, Application/API, Compute, AI/ML System, Device/Workstation

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DA-1.9.1: DMP Development and Authoring**
    - **Description:** Author the Data Management Plan, consolidating the classification scheme, provenance requirements, detection thresholds, DLP and rights-management policy, retention and disposition schedules, and minimization requirements produced across the focus area's capabilities into a single governing document.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Author the DMP after the discovery sweep, so it documents the real data estate rather than an intended one. After its One-Time issuance, DMP Periodic Review and Revision keeps it current.

- **DA-1.9.2: Data Retention and Disposition Schedule Definition**
    - **Description:** Set the retention period and the disposition action for each data and classification type the program holds, aligned to the governing records schedule, and document the result in the DMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-12 (partial) mapping. State a disposition action for each holding, naming the method from Media Sanitization and Destruction Procedures rather than just delete. Keep provenance and audit records long and inference and telemetry records short, accepting the cost of each choice.

- **DA-1.9.3: Data Minimization Requirement Definition**
    - **Description:** Determine what data the program is permitted to collect and retain for each stated purpose, and state in the DMP the resulting minimization requirements, including the limits on personal information in test, training, and research data.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-12(1) and SI-12(2) mappings and is the framework's single holder of the data minimization determination. Watch test and training copies, where production extracts land with weaker controls. State what may be collected and kept for a purpose, rather than what must be deleted later.

- **DA-1.9.4: DMP Review and Approval**
    - **Description:** Route the drafted DMP through stakeholder review and secure formal approval from the accountable authority before it takes effect.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Include the data owners in this review, since the plan's retention, minimization, and rights-protection determinations constrain what they may keep and share.

- **DA-1.9.5: DMP Periodic Review and Revision**
    - **Description:** Review the DMP on a defined cadence and revise it to reflect changes in the program's data holdings, classification scheme, retention obligations, or the tooling that enforces them.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity supersedes the One-Time issuance produced by DMP Development and Authoring. A new data source, classification tier, or enforcement tool triggers a revision without waiting for the annual review.

## DA-2: Data Encryption

### DA-2.1: Classification-Tied Document/Field-Level Encryption

**Design Intent:** Each data lake zone encrypts with its own key, so a workload that escapes the network controls still cannot read another team's or vendor's data. Fields holding personal information in the service desk and the cloud databases are encrypted at the field level. Scans confirm that every labeled record sits under the key its label requires.

**NIST Control Mapping:**

- **SC-28(1) (partial):** label-keyed encryption of a single document or column. It is partial because Default Data at Rest Encryption holds the storage tier, and Data Rights Management (DRM) holds revocable rights.
- **Declined:** the SC-28 base stays with Default Data at Rest Encryption. The AC-16 family is not reopened, since Data Discovery, Labeling, and Classification produces the labels and Attribute-Based Data and Application Access Enforcement (ABAC) owns the vocabulary.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Object/File Storage, Database Service, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **DA-2.1.1: Classification-Label-to-Encryption-Policy Mapping**
    - **Description:** Assign each classification label an encryption requirement naming the algorithm, the granularity it applies at, and the key ownership tier it draws from, and record the resulting mapping in the DMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Write the mapping as a few tiers rather than one rule per marking. Take each row's key tier from the sibling Encryption Key Ownership and Control decision. Leave rights, expiration, and revocation to Data Rights Management (DRM).

- **DA-2.1.2: Document/Field-Level Encryption Enforcement at Creation/Ingestion**
    - **Description:** Configure the program's document platforms and database engines to apply the mapped encryption to an item at the moment it is created, ingested, or relabeled, so that protection does not wait for a scheduled sweep to find it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-28(1) (partial) mapping. It is tagged Automate because the platform applies protection from the label. Settle encrypted columns with application owners before enabling the policy, and make relabeling re-invoke the policy.

- **DA-2.1.3: Encryption Compliance Scanning**
    - **Description:** Scan the program's document stores and database columns against the label-to-encryption mapping, and report each item whose applied encryption does not match what its classification tier requires.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is tagged Automate for the tool-driven inspection. Report items predating the policy as a remediation backlog, and items created after it as enforcement failures. Scope and log the scanner's own read access like any privileged read of classified holdings.

### DA-2.2: TLS Encryption Enforcement

**Design Intent:** Every service accepts only TLS 1.2 or later, with TLS 1.3 preferred, using the approved cipher suites. Service-to-service connections use mutual TLS with program PKI certificates. Plaintext connection attempts are blocked and logged.

**NIST Control Mapping:**

- **SC-8 (partial):** protects the confidentiality and integrity of data-service sessions, a partial slice split by subject from Secure File Transfer and Management Protocols. The Network and Environment and Identity focus areas declined SC-8 and left it here.
- **SC-8(1) (partial):** the negotiated version, cipher suite, and certificate that provide that protection, on the same partial split. Approved Cryptographic Algorithm/Protocol Baseline Enforcement issues the algorithm baseline.
- **Declined:** SC-8(2) is not claimed, since the program has no need for confidentiality across interruptions. SC-8(3) and SC-8(4) are not implemented and are rarely selected.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Application/API, Database Service, Object/File Storage, Message Queue/Event Stream, Virtual Machine/Server, Load Balancer/Reverse Proxy/API Gateway

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **DA-2.2.1: Minimum TLS Version/Cipher Suite Enforcement Policy**
    - **Description:** Set the minimum TLS version, permitted cipher suites, and permitted key exchange and signature algorithms the program's data services may negotiate, drawn from the approved cryptographic baseline, and record the policy and its exception path in the KMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Provide a bounded exception path, since some appliance will always fail the minimum. Expect to set the floor above platform defaults, which favor interoperability. Add an event-driven review trigger on any change to the approved algorithm baseline.

- **DA-2.2.2: TLS Certificate Deployment Across Data Services**
    - **Description:** Issue and install a valid server certificate from the program's certificate authority on every database, storage, messaging, and API endpoint that terminates a client connection, and configure each to present it on all inbound sessions.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SC-8(1) (partial) mapping. Renewal, binding, and revocation belong to Automated Certificate Renewal and Certificate Lifecycle and Revocation, which is why this activity is not tagged Automate. Hunt for self-signed certificates on internal data services, which teach clients to skip validation.

- **DA-2.2.3: Non-TLS Connection Detection and Blocking**
    - **Description:** Configure each data service to refuse plaintext and downgraded connections outright, and monitor the connection logs for clients still attempting them so the dependency can be found and moved before the refusal breaks it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-8 (partial) mapping. It is tagged Automate for enforcement on every connection. Detect before blocking, so the connection log names unknown dependents before an outage does. Treat services that permit downgrade like those that accept plaintext.

### DA-2.3: Secure File Transfer and Management Protocols

**Design Intent:** Files move only over HTTPS or SFTP, including recordings crossing the ground segment conduit. Administrative SSH and RDP run only through the privileged access platform or a VDI session, never directly. Every transfer is logged to the security monitoring platform. The payload processing workstation's transfer is the one exception, under CCSD tailoring action 3.

**NIST Control Mapping:**

- **SC-8 (partial), SC-8(1) (partial):** the transfer and management protocols administrators and batch jobs use, tracked with TLS Encryption Enforcement, which holds the data-service session slice.
- **AC-17(2) (partial):** the ciphers, key exchanges, and authentication methods SSH and RDP will negotiate, while Secure Remote Access holds the session key and certificate slice.
- **AU-12 (partial):** the file-transfer event class, one subject slice alongside other audit record classes held elsewhere.
- **Declined:** the AC-17 base, AC-17(1), and AC-17(3) stay with Secure Remote Access, which owns the remote-access path. CM-7(1) stays with Insecure Services and Protocols, which disables cleartext listeners.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Virtual Machine/Server, Object/File Storage, Network Infrastructure, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DA-2.3.1: SFTP/FTPS/HTTPS Enforcement**
    - **Description:** Require SFTP, FTPS, or HTTPS on every path files move along, migrate the transfers still running over plaintext FTP, Telnet, or TFTP onto one of them, and disable those listeners once nothing depends on them.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SC-8 and SC-8(1) (partial) mappings. The hard transfers are unowned scheduled jobs with embedded credentials, where finding the owner is the real work. It is not tagged Automate because migration is engineering coordinated with the system owner.

- **DA-2.3.2: SSH/RDP Hardening for Remote Management Access**
    - **Description:** Harden the SSH and RDP services on the program's data and infrastructure hosts to the approved algorithm baseline by permitting only key or certificate authentication and network-level authentication and by disabling the legacy ciphers, key exchanges, and message authentication codes each service still offers by default.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-17(2) (partial) mapping. Put the hardened settings in the host baseline that Baseline Configuration Standards maintains, so existing drift detection covers them. Disable SSH password authentication, which makes Remote Access Key Management load-bearing.

- **DA-2.3.3: File Transfer Audit Logging**
    - **Description:** Log every file transfer with its initiating identity, source and destination, file name and size, and completion status, and forward those records to the program's central log store under the retention the DMP sets.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-12 (partial) mapping. It is tagged Automate because the transfer service emits the records. Capture the destination field, which most services omit by default and which an exfiltration investigation needs. Feed these records to Data Loss Prevention (DLP) and Monitoring rather than building a second detection stack.

### DA-2.4: Default Data at Rest Encryption

**Design Intent:** At-rest encryption is on by default for every disk, storage service, database, and backup, and configuration checks block any resource without it. Confidential computing is not required today. It is the first option to consider if a workload ever needs mission data protected in use.

**NIST Control Mapping:**

- **SC-28 (partial):** the framework's single holder of general at-rest protection for the storage tier. It is partial because the label-keyed and rights-bound cases sit with other outcomes in the focus area.
- **SC-28(1) (partial):** encryption at the volume, disk, and database tier, one of several SC-28(1) slices tracked together, alongside Data Rights Management (DRM).
- **SC-39(1) (partial):** the confidential-computing half, while the Artificial Intelligence focus area's On-Device Extraction Resistance holds the physically held device case, split by environment.
- **Declined:** SC-28(2) is a media-handling matter for Media Protection Policy and Procedures. SC-28(3) belongs to HSM and Hardware Root-of-Trust Management. The SC-39 base is held by the Application and Artificial Intelligence focus areas.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Storage/Database, Virtual Machine/Server, Application/API

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.

**Security Impact:** High

**Activities:**

- **DA-2.4.1: Encryption for VMs and Storage**
    - **Description:** Enable at-rest encryption by default on every virtual machine disk, object and file storage service, and database instance the program operates, and set the platform policy so that a resource created without it is either encrypted automatically or refused.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-28 and SC-28(1) (partial) mappings. It is not tagged Automate because the deliverable is configuration and scope. Cover backups, snapshots, replicas, and temporary and swap volumes, which fall outside a default set on the primary resource. Draw each service's key from the tier Encryption Key Ownership and Control assigns.

- **DA-2.4.2: Confidential Computing and Column Level Encryption**
    - **Description:** Deploy confidential-computing instances for the workloads whose data must stay unreadable to the platform operator while it is being processed, and apply column-level or always-encrypted database features to the specific fields that warrant protection from a privileged database administrator.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-39(1) (partial) mapping for hardware-isolated execution, with the column-level half under the SC-28(1) claim. It applies more narrowly than the outcome's Deployment Type, since confidential computing is unavailable in most isolated enclaves running older equipment. Measure the performance cost against the real workload, and require workloads to verify attestation.

- **DA-2.4.3: Encryption Compliance Monitoring and Enforcement**
    - **Description:** Continuously evaluate the program's compute and storage resources against the required encryption configuration, alert on any resource found unencrypted or encrypted under the wrong key ownership tier, and apply the platform policy that remediates or blocks it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is tagged Automate for policy-as-code evaluation and automatic remediation. Its results feed Data Security Posture Dashboard. Treat the wrong key tier as a finding just like missing encryption, which only a check reading both setting and policy catches.

### DA-2.5: Encryption Key Ownership and Control

**Design Intent:** KESTREL owns and controls the keys for every store holding mission data, models, or backups. Those keys come from the HSM-backed key management service under keys rooted in the on-premises HSMs. Platform-managed keys are allowed only for dev/test data that is synthetic or sanitized. The KMP maps each data class to its key ownership tier.

**NIST Control Mapping:**

- **SC-12 (partial):** the requirements-determination half, stating key access and control requirements per data class. Key Management Policies and Infrastructure and Key Lifecycle Automation jointly hold the establishing and managing half under the KMP.
- **Declined:** the base is cited because no enhancement describes an ownership decision. SC-12(1), SC-12(2), SC-12(3), and SC-12(6) are infrastructure properties left to implementing capabilities. SC-13 belongs to Approved Cryptographic Algorithm/Protocol Baseline Enforcement, and SC-28(3) to HSM and Hardware Root-of-Trust Management.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Storage/Database, Compute, Application/API, Self-Hosted Model

**External Dependencies:** The IL5 cloud provider, whose HSM-backed key management service holds the cloud keys under its provisional authorization.

**Security Impact:** Moderate

**Activities:**

- **DA-2.5.1: Customer-Managed-Key Adoption Decision and Requirements Definition**
    - **Description:** Determine which workloads and data classes require customer-managed keys and which may use platform-managed keys, state the availability, rotation, recovery, and separation-of-duties requirements each choice carries, and record the decision in the KMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-12 (partial) mapping. Customer-managed keys remove the operator's ability to decrypt but add an availability dependency and rule out some managed services. Identify those services before writing the requirement, so it does not create a standing exception on day one.

- **DA-2.5.2: Data Classification-to-Key-Ownership-Tier Mapping**
    - **Description:** Map each classification tier to the key ownership tier its data must use, and publish that mapping so the provisioning policy and the encryption compliance checks evaluate against one source rather than two.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Express the requirement by classification tier rather than named system, so it is evaluated against labels Data Discovery, Labeling, and Classification assigns. Publish it as data Encryption Compliance Monitoring and Enforcement can read. Remove any tier with no classification assigned.

## DA-3: Cryptographic Management

### DA-3.1: FIPS 140 / Approved Cryptographic Module Baseline

**Design Intent:** KESTREL uses only FIPS 140-3 validated modules, with Level 3 for the HSMs and the datalink crypto modules that protect CCSD row 13's key material. The KMP lists the approved algorithms, key lengths, and protocols. Scans of code, configuration, and traffic flag non-compliant use. KESTREL holds no classified data, so NSA-approved cryptography applies only within the cross domain solution, which its provider operates.

**NIST Control Mapping:**

- **SC-13 (full):** the framework's only citation, since the three activities enumerate cryptographic uses, bind each to approved algorithms and validated modules, and measure the estate. SC-13 has no enhancements, and other outcomes draw their permitted suites from this baseline.
- **Declined:** IA-7 covers operator authentication to a module, so HSM and Hardware Root-of-Trust Management claims it.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Storage/Database, Application/API, Network Infrastructure

**External Dependencies:** The aircraft and datalink manufacturers, who supply the datalink crypto modules.

**Security Impact:** High

**Activities:**

- **DA-3.1.1: FIPS 140-Validated Module Selection and Inventory**
    - **Description:** Identify every cryptographic module the program relies on, select those carrying a current FIPS 140-3 validation at the level the program's categorization requires, and maintain an inventory recording each module's certificate number, validated version, and the systems depending on it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SC-13 (full) mapping. Record each module's operating state, such as FIPS mode and patched version, alongside its certificate number. Add an event-driven review trigger when a module's validation status changes.

- **DA-3.1.2: Approved Cryptographic Algorithm/Protocol Baseline Enforcement**
    - **Description:** Publish the approved algorithms, key lengths, modes, and protocol versions permitted for each of the program's cryptographic uses in data at rest, data in transit, and key management, record the baseline and its exception path in the KMP, and configure the platform, service, and application settings that hold each use to it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the substance of the outcome's SC-13 (full) mapping. Write the baseline by cryptographic use rather than as one estate-wide list. It is not tagged Automate, since Non-Compliant Cryptographic Usage Detection and Remediation measures conformance.

- **DA-3.1.3: Non-Compliant Cryptographic Usage Detection and Remediation**
    - **Description:** Scan the program's services, endpoints, certificates, and key stores for algorithms, key lengths, and protocol versions outside the approved baseline, and drive each finding to either remediation or a recorded, time-bounded exception.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is tagged Automate for the tool-driven inspection. Scan the whole estate, since the best findings are unscoped appliances, embedded libraries, and test endpoints. Unremediable findings join the baseline's exception population and seed Post-Quantum Cryptography Readiness.

- **DA-3.1.4: NSA-Approved Cryptography for Classified Data**
    - **Description:** Identify every cryptographic use that protects classified information and require NSA-approved cryptography for each in place of validated commercial modules alone, whether a Type 1 product or a Commercial Solutions for Classified (CSfC) layered solution built to an NSA-published capability package.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's SC-13 (full) mapping. For classified information, CNSSP 15 requires NSA-approved cryptography, which FIPS 140-3 validation alone does not satisfy. A CSfC solution is approved only as built to its capability package, so deviations need approval. Type 1 keying material comes through NSA's key management infrastructure under the Key Management Plan (KMP).

### DA-3.2: Post-Quantum Cryptography Readiness

**Design Intent:** The cryptographic inventory records every place KESTREL relies on quantum-vulnerable public-key cryptography, with the program PKI, the datalinks, and code signing first. The transition plan follows the CNSA 2.0 timelines, and every new design must let algorithms change without redesign.

**NIST Control Mapping:**

- **Declined:** no SP 800-53 Rev 5 control covers post-quantum transition planning, so the outcome is unmapped. SC-13 stays with FIPS 140 / Approved Cryptographic Module Baseline, where completed steps become enforceable. SA-8 is held by the Application focus area.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Application/API, Compute, Network Infrastructure, Storage/Database

**External Dependencies:** The aircraft and datalink manufacturers, who supply the datalink crypto modules. Their roadmaps set when the datalinks can move to quantum-resistant algorithms.

**Security Impact:** Moderate

**Activities:**

- **DA-3.2.1: Cryptographic Inventory for PQC Migration**
    - **Description:** Inventory every place the program depends on quantum-vulnerable public-key cryptography, including key exchange, digital signatures, certificate chains, code signing, and key wrapping, and record for each the data it protects and how long that data must stay confidential.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Keep this inventory separate from FIPS 140-Validated Module Selection and Inventory, since it records where quantum-vulnerable algorithms are used. Record each entry's confidentiality lifetime to prioritize harvest-now-decrypt-later targets. Include vendor-embedded cryptography, because those vendor engagements must open earliest.

- **DA-3.2.2: CNSA 2.0 Algorithm Transition Planning**
    - **Description:** Sequence the program's move to CNSA 2.0 approved algorithms against the inventory's priorities and the timelines the transition guidance sets, identify the platform and vendor dependencies that gate each step, and record the resulting plan and milestones in the KMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Sequence the plan around supplier support for HSMs, identity platforms, and certificate authorities. Plan hybrid modes as an interoperability bridge, and account for larger certificates and handshakes. Handle symmetric and hashing upgrades separately so the public-key migration does not stall them.

- **DA-3.2.3: Crypto-Agility Design Requirements**
    - **Description:** Require that systems the program builds or acquires reference cryptographic algorithms through configuration rather than hardcoded identifiers, keep trust anchors and algorithm choices replaceable without a code change, and record the requirement so it is levied at design and acquisition rather than discovered at migration.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Levy the requirement through design reviews and acquisition language, since retrofitting agility is expensive. Require negotiated algorithm identifiers, multi-chain trust stores, tolerance for larger keys and signatures, and no fixed-width key fields. The same path will serve future algorithm deprecations.

### DA-3.3: Key Management Policies and Infrastructure

**Design Intent:** Cloud workloads draw their keys from the cloud provider's HSM-backed key management tier, and production uses only that tier. The on-premises HSMs hold the root keys, the program PKI, code signing, and the datalink key material. One key policy covers both, managed by the Platform Team's Tier 0 administrators.

**NIST Control Mapping:**

- **SC-12 (partial):** the establishment half, standing up the infrastructure keys are generated, stored, and served from. Encryption Key Ownership and Control and Key Lifecycle Automation hold the other halves, all tracked together.
- **Declined:** SC-12(1) belongs to Key Escrow and Recovery Procedures, and SC-12(2), SC-12(3), and SC-12(6) to HSM and Hardware Root-of-Trust Management.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Secrets Vault, Compute, Application/API, Directory/Platform Core Infrastructure

**External Dependencies:** The IL5 cloud provider, whose HSM-backed key management service holds the cloud keys under its provisional authorization.

**Security Impact:** High

**Activities:**

- **DA-3.3.1: Centralized Key Management Infrastructure**
    - **Description:** Deploy the program's central key management service, integrate it with the identity platform for authentication and with the program's logging pipeline for key-operation records, and make it the single source workloads obtain and use keys through rather than local key stores.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-12 (partial) mapping. Build regional or enclave-level redundancy in from the start, since a key service outage is a total data outage. Decide early whether one service spans all environments or each runs its own with a documented boundary.

- **DA-3.3.2: Vault Service Tier Selection**
    - **Description:** Select the key management and secrets vault service tier that meets the program's required FIPS 140-3 validation level, hardware protection, availability, and transaction throughput, and record the selection and its rationale in the KMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: High
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Tier fixes the hardware protection level, availability, and throughput ceiling, and changing it later means re-encrypting. Recurring cost is High because hardware-backed tiers are standing capacity, so size against the protection level FIPS 140 / Approved Cryptographic Module Baseline requires. A tier needing a dedicated module commits the program to HSM and Hardware Root-of-Trust Management.

### DA-3.4: HSM and Hardware Root-of-Trust Management

**Design Intent:** The on-premises HSMs generate and hold KESTREL's most consequential keys, namely the root certificate authority, code signing, and CCSD row 13's datalink key material. These keys never exist outside an HSM or a datalink crypto module. HSM administration needs two people, and every HSM operation is logged to the security monitoring platform.

**NIST Control Mapping:**

- **SC-28(3) (full):** the framework's only citation, which the Data Encryption capability reserved here. It is full because the hardware key store this outcome deploys is the protected storage the enhancement asks for.
- **SC-12(2) (partial), SC-12(3) (partial):** producing symmetric and asymmetric keys inside validated hardware. They are partial because Key Lifecycle Automation holds key control and distribution.
- **SC-12(6) (partial):** the program's physical retention of keys used by external services, a partial slice tracked with Encryption Key Ownership and Control, which decides where it applies.
- **IA-7 (partial):** the framework's only citation, for HSM operator authentication and role verification. It is partial because software modules authenticate callers through the identity platform.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Cryptographic Hardware/HSM, Secrets Vault, Application/API

**External Dependencies:** The aircraft and datalink manufacturers, who supply the datalink crypto modules.

**Security Impact:** High

**Activities:**

- **DA-3.4.1: HSM Deployment and Provisioning**
    - **Description:** Deploy the program's hardware security modules or dedicated cloud HSM instances, complete the initial provisioning ceremony that establishes their administrative roles and partitions, and bind the key management service to them so keys designated for hardware protection are generated and retained inside the module boundary.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-28(3) (full) and SC-12(6) (partial) mappings. Run provisioning as a scheduled, witnessed ceremony with named roles and split credentials, since redoing it means re-keying. Decide module backup and recovery at the same time, and record the balance in the KMP.

- **DA-3.4.2: Hardware Root-of-Trust Key Generation and Attestation**
    - **Description:** Generate the program's designated symmetric and asymmetric keys inside the hardware module or platform root of trust so private material is never exported in the clear, and require attestation evidence that a given key was generated in and remains resident in that hardware.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-12(2) and SC-12(3) (partial) mappings. Require attestation, which separates a hardware-protected key from an asserted one. Verify non-exportability at creation, since it cannot be added later. Use the algorithms FIPS 140 / Approved Cryptographic Module Baseline permits.

- **DA-3.4.3: HSM Access Control and Audit Logging**
    - **Description:** Authenticate every operator to the module in a defined administrative or cryptographic-user role, require quorum authorization for the module operations that would alter its configuration or its key material, and forward the module's own audit log to the program's central log store.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-7 (partial) mapping. Require quorum (M-of-N) authorization for destructive and configuration operations, with split credentials set at provisioning. Export the module log, since internal logs have finite capacity, and feed it to Key Access Monitoring.

### DA-3.5: Key Lifecycle Automation

**Design Intent:** Key rotation is automated on the KMP's cadence for every key class, and datalink keys rotate on Fleet Operations' schedule. The hierarchy runs from HSM-held root keys to the cloud's customer-managed keys. Keys whose loss would destroy data, such as backup keys, are escrowed in the HSMs under split knowledge.

**NIST Control Mapping:**

- **SC-12 (partial):** the managing half, covering rotation, distribution, and destruction against the sibling's infrastructure. Key Management Policies and Infrastructure and Encryption Key Ownership and Control hold the other halves, all tracked together.
- **SC-12(1) (full):** the framework's only citation, since Key Escrow and Recovery Procedures maintains availability on key loss exactly as the enhancement describes.
- **Declined:** IA-5(6) stays with the Identity focus area's Automated Secret Rotation (Secrets and Credentials Protection), which rotates authenticators rather than key material.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Storage/Database, Compute, Application/API

**External Dependencies:** The IL5 cloud provider, whose HSM-backed key management service holds the cloud keys under its provisional authorization.

**Security Impact:** Moderate

**Activities:**

- **DA-3.5.1: Automated Key Rotation**
    - **Description:** Configure automatic rotation for every key the program manages at the cadence its key use and classification tier require, so that a new key version is issued and adopted without an operator initiating it, and record the cadences in the KMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SC-12 (partial) mapping. It is tagged Automate because the key service rotates on a schedule. Confirm first that applications resolve keys by identifier and that superseded versions stay decryptable. Record rotation cadence and re-encryption of existing data as separate decisions.

- **DA-3.5.2: Key Hierarchy and BYOK**
    - **Description:** Define the program's key hierarchy, separating root and key-encryption keys from the data-encryption keys they wrap, establish the bring-your-own-key (BYOK) path for importing externally generated key material under that hierarchy where the program must originate its own keys, and document the hierarchy and BYOK path in the KMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SC-12 (partial) mapping. Use a key hierarchy, which makes rotation affordable by re-wrapping only data keys. Under bring-your-own-key, the program must generate material securely, transport it under an approved wrapping key, and keep a tested recovery copy.

- **DA-3.5.3: CMK Provisioning and Configuration**
    - **Description:** Provision the customer-managed keys the classification-to-key-ownership mapping calls for, and configure each storage service, database, and workload to encrypt under the key its data class requires rather than under the platform default.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity implements the key provisioning Encryption Key Ownership and Control requires. Make key naming and tagging machine-readable for Encryption Compliance Monitoring and Enforcement. Choose key granularity deliberately, since cost, rotation burden, and blast radius all move with it.

- **DA-3.5.4: Key Escrow and Recovery Procedures**
    - **Description:** Establish and test the procedures for retaining, protecting, and recovering escrowed key material when an operational key is lost, destroyed, or rendered unusable, define who may authorize a recovery and under what conditions, and record the procedures in the KMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-12(1) (full) mapping. Rehearse recovery annually against real escrowed material, since an untested procedure is worth nothing when needed. Require multiple named authorities for recovery, under Key Access Separation of Duties, so escrow does not undo the purpose of customer-managed keys. The Operate pillar's Backup Encryption Key Lifecycle Management draws on these procedures.

### DA-3.6: Key Access Separation of Duties

**Design Intent:** Key administrators, key users, and key auditors are separate roles. The Platform Team's Tier 0 administrators manage keys, workload identities use them, and the Security Team audits them. No identity holds two of these roles, and key operations by any other identity alert the Security Team.

**NIST Control Mapping:**

- **AC-5 (partial):** separates the identity requesting a key operation from the identity that performs it and the one that audits it. It is partial because Approver and Reviewer Audit Log holds the code-change separation, and roles come from Privileged Access Control.
- **AC-6(9) (partial):** the framework's only citation, for logging privileged key operations. It is partial because estate-wide privileged logging stays with the Operate pillar.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Privileged Access Management, Secrets Vault, Cryptographic Hardware/HSM

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DA-3.6.1: Separation of Duties Enforcement**
    - **Description:** Define the key management, key usage, and key audit roles, assign each to distinct identities in the key management service and the identity platform, and configure the permissions so that no identity can both authorize and perform a key operation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-5 (partial) mapping. Close the platform's escape hatches, such as a tenant owner who can rewrite the key service's access policy, which is usually the real work. A program too small to staff three roles records that condition and its compensating arrangement for the AO.

- **DA-3.6.2: Key Access Monitoring**
    - **Description:** Log every key operation and administrative action against the key management service and its modules with the initiating identity, the key and operation invoked, and the result, and alert on the operations that indicate misuse, including bulk decryption, key export attempts, policy changes, and deletion.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-6(9) (partial) mapping. Alert on pattern changes and on rare, irreversible, or pre-exfiltration operations rather than on raw counts. Send records, including those from HSM Access Control and Audit Logging, to the central log store for Operate pillar correlation.

### DA-3.7: Certificate Policies and Integration

**Design Intent:** The program PKI issues KESTREL's device, workload, and code-signing certificates from issuing authorities under the HSM-held root. A certificate management service distributes them. User and partner certificates come from DoD PKI and External Certificate Authorities, whose trust anchors the identity provider holds.

**NIST Control Mapping:**

- **SC-17 (partial):** the issuance and certificate-authority slice. Server and Services Authentication holds the relying-party slice and Certificate Lifecycle and Revocation the revocation slice, all tracked together.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** PKI/Certificate Authority, Application/API, Cryptographic Hardware/HSM, Network Infrastructure

**External Dependencies:** DoD PKI and External Certificate Authorities, which issue user and partner certificates.

**Security Impact:** High

**Activities:**

- **DA-3.7.1: Certificate Management Infrastructure**
    - **Description:** Deploy the certificate management service that requests, issues, stores, and distributes the program's certificates, integrate it with the key management service so private keys are generated and held under program key infrastructure, and define and document in the KMP the certificate profiles and issuance policy each certificate purpose uses.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the issuance half of the outcome's SC-17 (partial) mapping. Define purpose-specific profiles, since validity, key usage, name constraints, and algorithms live there. Prefer short validity periods once Automated Certificate Renewal is running.

- **DA-3.7.2: Certificate Authorities Integration**
    - **Description:** Establish the program's trust relationships with its internal issuing authority and with the enterprise, Government, or commercial authorities it chains to or relies on, and define which authority issues for which certificate purpose.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the certificate-authority half of the outcome's SC-17 (partial) mapping. Assign an authority explicitly to each purpose, since workload, external endpoint, code-signing, and person certificates differ. Build an offline or hardware-protected root with online issuing authorities beneath it.

### DA-3.8: Automated Certificate Renewal

**Design Intent:** Workload and service certificates renew automatically ahead of expiry through an automated enrollment protocol, and each renewed certificate is rebound to its service without an operator. Aircraft and station certificates renew during maintenance windows.

**NIST Control Mapping:**

- **Declined:** no distinct control is claimed, because renewal carries out SC-17 decisions that Certificate Policies and Integration and Certificate Lifecycle and Revocation already hold.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Application/API, Virtual Machine/Server, Load Balancer/Reverse Proxy/API Gateway

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **DA-3.8.1: Automated Renewal Configuration**
    - **Description:** Configure automated renewal for every certificate the program issues, triggered at a defined interval ahead of expiry through the certificate service's native renewal or an ACME-style agent, so that renewal completes without an operator initiating it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is tagged Automate for scheduled renewal. Set lead time as a multiple of validity, wide enough for several retries. Hand certificates the program does not issue, or appliances without an agent, to Certificate Lifecycle and Revocation's monitoring.

- **DA-3.8.2: Automatic Certificate Binding**
    - **Description:** Configure each service, load balancer, and gateway to pick up its renewed certificate and reload without manual intervention, so that a certificate renewed by the service is also the certificate actually presented on the wire.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is tagged Automate for rebinding and reload on renewal. Keep it separate from renewal, since a renewed but unbound certificate is the classic outage. Verify what the endpoint actually presents, and route services that cannot reload cleanly through change control.

### DA-3.9: Certificate Lifecycle and Revocation

**Design Intent:** A certificate inventory and dashboard track every certificate KESTREL issues or trusts, and alerts fire on approaching expiry or on issuance nobody requested. Revocation procedures cover every case, including an aircraft declared lost, whose device certificates are revoked at once.

**NIST Control Mapping:**

- **SC-17 (partial):** the revocation and status-publication slice, a partial claim tracked with Certificate Policies and Integration and Server and Services Authentication. A revocation is effective only where relying parties run Credential Status Checking (OCSP/CRL).
- **Declined:** IA-5(2) is held by the Identity focus area's credential outcomes, which consume this revocation state.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Application/API, Virtual Machine/Server, Network Infrastructure, PKI/Certificate Authority

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DA-3.9.1: Certificate Monitoring and Alerting**
    - **Description:** Monitor the program's certificate estate for approaching expiry, unexpected or unauthorized issuance, weak or non-compliant profiles, and chain or hostname configurations that will fail validation, and alert the owning team with enough lead time to act.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SC-17 (partial) mapping. Monitor what endpoints actually present, since the program did not issue most problem certificates. Alert on unexpected issuance for program hostnames separately from expiry.

- **DA-3.9.2: Certificate Inventory and Dashboard Maintenance**
    - **Description:** Maintain the authoritative inventory of the program's certificates with their owner, purpose, issuing authority, expiry, and binding location, and present it as a dashboard showing coverage, upcoming expirations, and non-compliant or unmanaged certificates.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is tagged Visualize for the estate view. Keep ownership current, because it decides whether alerts produce action. Lead with the unmanaged count, which measures the gap between what the program manages and what it runs.

- **DA-3.9.3: Revocation Procedures**
    - **Description:** Establish and exercise the procedures for revoking a certificate on compromise, decommissioning, or role change, define who may authorize a revocation, publish the resulting status through the program's CRL and OCSP responders within a defined time, and document the revocation procedures in the KMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the substance of the outcome's SC-17 (partial) mapping. State a maximum publication interval rather than the responder default. Revoke on decommissioning and role change, not only compromise. Coordinate with Automated Certificate Renewal for replacement and with Operate pillar incident response for containment.

### DA-3.10: Secrets Vault Access Controls

**Design Intent:** Each spoke's vault grants each workload identity only the secrets it needs. Humans hold no standing vault access and activate it just in time through the privileged access platform.

**NIST Control Mapping:**

- **AC-6(1) (partial):** authorizes access to the vault's security functions and key management information, a partial slice alongside Security Team Visibility.
- **Declined:** AC-3(7) is held by Non-Privileged Access Control and Privileged Access Control, whose role model this outcome reuses.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Cloud Workload/Native Platform Identity, Privileged Access Management, Application/API, Secrets Vault

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **DA-3.10.1: Secrets Vault Access Policy Configuration**
    - **Description:** Configure the vault's access policy to grant each principal only the specific secrets, keys, and operations its function requires, separate managing a secret from reading it and using a key from exporting or deleting it, and document the access policy in the KMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-6(1) (partial) mapping. Separate managing a secret from reading it. Design vault layout with the policy, using separate vaults per environment and trust boundary. Key Access Separation of Duties takes precedence where a permission grants a key operation.

- **DA-3.10.2: Secrets Vault Workload Identity and JIT Access**
    - **Description:** Configure workloads to authenticate to the vault using their platform-native identity rather than a stored credential, and require human access to vault secrets and key operations to be obtained through time-bounded elevation rather than held as a standing assignment.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity configures the vault to accept Cloud Workload Identities and require Just in Time Access, rather than rebuilding either. That closes the bootstrapping problem of a stored credential used to reach the vault. Eliminate standing human access to production vaults first.

### DA-3.11: Secrets Vault Network Security Hardening

**Design Intent:** Every vault is reached only through a private endpoint in its own spoke, with public network access disabled and its resource firewall limited to that spoke's workloads.

**NIST Control Mapping:**

- **SC-7(21) (partial):** isolates the key and secrets infrastructure as a component. Network Topology Design and Subnet Allocation and Segmentation Plan holds the network-wide slice, and the two are tracked together.
- **Declined:** the SC-7 base stays with that outcome for overall boundary architecture.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Private Connectivity/Dedicated Circuit, Application/API, Identity Platform

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.

**Security Impact:** Moderate

**Activities:**

- **DA-3.11.1: Secrets Vault Private Endpoint and Firewall**
    - **Description:** Provision a private endpoint for the vault inside the program's network and configure its firewall to accept traffic only from the subnets, services, and administrative networks with an established need, denying all other sources by default.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7(21) (partial) mapping. Verify private DNS from a real client, since public resolution silently bypasses the endpoint. Scrutinize each trusted-services exemption, which may admit any tenant of that platform.

- **DA-3.11.2: Public Network Access Disablement**
    - **Description:** Disable the vault's public network access entirely once private connectivity is verified, so the private endpoint is the only path to the service rather than an additional one, and confirm that the public endpoint no longer answers.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Treat disablement as its own verified step, since a private endpoint changes nothing while the public path stays open. Establish the administrative and break-glass path over the private network first, and record it in the KMP. Identify unknown external clients before flipping the toggle.

### DA-3.12: Secrets Vault Protection and Monitoring

**Design Intent:** Every vault has soft delete and purge protection enabled, so a deleted vault or key can be recovered within the retention window and cannot be purged by one person. Vault operations and threat detection alerts go to the security monitoring platform.

**NIST Control Mapping:**

- **SI-4 (partial):** monitors the vault and key management infrastructure itself, a partial slice that the Identity focus area's Secrets Continuous Monitoring assigns here.
- **Declined:** Secrets Vault Deletion Protection is left unmapped, since no control describes an anti-purge safeguard. CP-9 covers backups, and SC-12(1) is held by Key Escrow and Recovery Procedures.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Secrets Vault, Application/API, Identity Platform

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.

**Security Impact:** Moderate

**Activities:**

- **DA-3.12.1: Secrets Vault Deletion Protection**
    - **Description:** Enable soft delete with a defined recovery window and purge protection on the vault and its secrets, keys, and certificates, so that a deletion is reversible for that period and cannot be made permanent within it by any single identity.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Rely on purge protection rather than soft delete, which the deleting identity can reverse. Enable it deliberately, since it is irreversible, with a recovery window long enough to cover a holiday weekend. It carries no control claim but is Level 1, because losing key material is unrecoverable.

- **DA-3.12.2: Secrets Vault Monitoring and Threat Detection**
    - **Description:** Monitor the vault service for anomalous authentication and retrieval patterns, permission and policy changes, deletion and purge attempts, and provider threat-detection signals, and route the alerts into the program's security operations workflow.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4 (partial) mapping. It watches the vault as a system, while Secrets Continuous Monitoring watches secret consumption. Alert above all on an identity reading many secrets quickly, and correlate in the Operate pillar with Key Access Monitoring records.

### DA-3.13: Key Management Plan (KMP)

**Design Intent:** The Platform Team's Tier 0 administrators author KESTREL's KMP, with Fleet Operations writing the datalink key procedures. The Security Team reviews it, and the Configuration Control Board approves it. It is revised each year and whenever an algorithm, key tier, or post-quantum milestone changes.

**NIST Control Mapping:**

- **SC-1 (partial):** the cryptographic and key management slice of SC policy and procedures, with the rest held by Network and Environment and governance outcomes. SC-1 has no enhancements.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Storage/Database, Compute, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **DA-3.13.1: KMP Development and Authoring**
    - **Description:** Author the Key Management Plan, consolidating the approved algorithm baseline, key ownership and hierarchy decisions, rotation cadences, escrow and recovery procedures, certificate and revocation policy, and vault tier and access arrangements produced across the capability into a single governing document.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Author the KMP once the determinations it consolidates exist, such as Approved Cryptographic Algorithm/Protocol Baseline Enforcement and Vault Service Tier Selection. KMP Periodic Review and Revision keeps its One-Time issuance current.

- **DA-3.13.2: KMP Review and Approval**
    - **Description:** Route the drafted KMP through stakeholder review and secure formal approval from the accountable authority before it takes effect.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)

- **DA-3.13.3: KMP Periodic Review and Revision**
    - **Description:** Review the KMP on a defined cadence and revise it to reflect changes in the approved algorithm baseline, the key and certificate infrastructure, the post-quantum transition plan, or governing requirements.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity supersedes the One-Time issuance produced by KMP Development and Authoring. Add an event-driven trigger on any change to the approved algorithm baseline or a post-quantum transition milestone.
