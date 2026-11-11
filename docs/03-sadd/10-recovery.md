# RC: Recovery

*KESTREL SADD, Section 5 (Operate). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## RC-1: Backup Automation and Coverage

### RC-1.1: Backup Coverage Strategy

**Design Intent:** Backup coverage follows three criticality tiers. Tier 1 holds the identity provider, the PKI and HSM backups, the hubs' rule base, and the ground segment's configuration. Tier 2 holds the data lake, the model registry, the mission teams' applications and databases, and the security monitoring platform. Tier 3 holds dev/test, training scratch, and experimentation. The coverage list also includes the system's security documentation. Gaps across supported, unsupported, and OT systems are reviewed each year.

**NIST Control Mapping:**

- **CP-9 (partial):** This outcome fixes what is in scope and how often, which is one dimension of a CP-9 claim shared across this capability's outcomes. The three execution workstreams back up their populations, Backup Policy Enforcement binds the parameters, and Backup Compliance and Coverage Monitoring verifies the binding. They are tracked jointly, and none is sufficient alone.
- **Declined:** CP-9(3), CP-9(5), CP-9(7), and CP-9(8) belong to Backup Data Protection, and CP-9(6) to Disaster Recovery Capabilities. Tiering here is the closest fit for CP-9(3), but CP-9(3) concerns storage of copies, not what to back up. CP-9(1) sits with Backup Health and Operations Monitoring, and CP-9(2) with Backup Recovery Testing. CP-9(4) was withdrawn in Rev 5. CP-1, CP-2, and the family's planning controls belong to the Contingency Planning capability, matching the allocation of IR-1 and IR-8 in the Response focus area and SC-1 in the Data focus area. CP-2(8) is declined because the Response focus area's Asset Criticality and Business Impact Assessment already declined it, so tiers here are read from that shared asset register.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Identity Platform, Network Infrastructure, Device/Workstation, Application/API, OT/ICS Device, AI/ML System

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RC-1.1.1: Backup Scope/Coverage Requirements Definition**
    - **Description:** Determine which systems, data classes, and items of system and security documentation require backup and at what frequency, tier each against the criticality rating the program already holds, and record the result as the coverage baseline the CP consolidates.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the scoping dimension of the outcome's CP-9 (partial) mapping. System documentation is the element programs most often omit, and the gap surfaces when a rebuilt system has to be reconfigured from memory. Derive frequency from each tier's recovery point objective rather than the platform's default menu. Where that objective is not yet fixed, state the needed frequency and let Recovery Readiness confirm it.

- **RC-1.1.2: Coverage Gap Analysis across Supported, Unsupported, and OT/Legacy Backup Workstreams**
    - **Description:** Compare the coverage baseline against what each of the three execution workstreams can actually protect, and record every asset that falls between them as a named gap with an owner and a disposition of protect, accept, or retire.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Assets are lost in the space between the three workstreams, since a service nobody enrolled is absent from every workstream's status view. That is why this analysis runs at the strategy level. It differs from the reconciliation Backup Compliance and Coverage Monitoring runs, because it asks whether any mechanism able to protect the asset exists at all.

- **RC-1.1.3: Backup Coverage Strategy Periodic Review and Update**
    - **Description:** Review the coverage baseline on its defined cycle, revise it whenever a system is added or retired, a criticality tier changes, or a recovery point objective is revised, and reissue it to the workstreams and the policy standard built against it.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The annual cadence is a floor, and the change triggers keep the baseline true, since a new system reaching production will not wait for a review date. Reissue the baseline after each revision, so the policy standard and the three workstreams build against the current version.

### RC-1.2: Automated Backup for Supported Services

**Design Intent:** The backup platform protects every supported service class automatically, including virtual machines, cloud databases, storage, the directory, the data lake, and the model registry. Schedules and retention come from each resource's tier. Infrastructure as code is backed up by its repository, so rebuilding is a pipeline run.

**NIST Control Mapping:**

- **CP-9 (partial):** carries the execution share of the shared CP-9 (partial) claim for the platform-supported population. Supported is a property of the chosen backup product, so the boundary against Backup Unsupported Services is re-drawn at each coverage review.
- **Declined:** CP-9(8) belongs to Backup Data Protection's encryption outcome, with keys managed through Backup Encryption Key Lifecycle Management.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Virtual Machine/Server, Database Service, Object/File Storage, Directory/Platform Core Infrastructure, Self-Hosted Model, Backup/Archive Repository, Infrastructure-as-Code (IaC)

**External Dependencies:** The IL5 cloud provider, whose native backup service and second IL5 region KESTREL relies on under its provisional authorization.

**Security Impact:** High

**Activities:**

- **RC-1.2.1: Automated Backup Job Deployment and Scheduling**
    - **Description:** Deploy and schedule the platform's backup jobs across every supported service class as code, so that a job is reproducible, reviewable, and recreated identically when a region, subscription, or enclave is stood up.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the core of the outcome's CP-9 (partial) mapping. Deploying jobs as code makes every environment match, including the disaster recovery region nobody would configure by hand. Version job definitions with the policy standard, so a tier's frequency change propagates everywhere.

- **RC-1.2.2: Backup Schedule/Retention/Scope Parameter Configuration**
    - **Description:** Set each job's frequency, retention period, and capture scope from the tier the coverage baseline assigned, and choose application-consistent capture wherever a crash-consistent copy would restore a database nobody can open.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Consistency decides whether a copy is usable, and a crash-consistent snapshot of a running database needs repair before it can be read. Set retention per tier, since retention drives this capability's recurring cost. Read any longer records-management floor from the Data focus area's DMP. Exclude scratch volumes, caches, and replicas, which slow every restore without adding anything recoverable.

### RC-1.3: Backup Unsupported Services

**Design Intent:** Services the backup platform cannot enroll use their own export, captured on the same tier schedule. These include the service desk platform, the SDN controller, the vault contents, and the network appliances. Foundation model deployments need no backup, since their configuration is code and the weights are the provider's.

**NIST Control Mapping:**

- **CP-9 (partial):** carries the execution share of the shared CP-9 (partial) claim for the population no backup platform enrolls. It is the share most often assumed rather than verified, such as the ticketing system or appliance configurations.
- **Declined:** IA-5(7) is not reopened for custom job credentials, which are vaulted through the Identity focus area's Secrets and Credentials Protection.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Virtual Machine/Server, Database Service, Self-Hosted Third-Party Application (COTS), Backup/Archive Repository, Network Infrastructure, Application and Service Account Identity, First-Party/Custom Application Code

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RC-1.3.1: Native Backups**
    - **Description:** Enable and configure each unsupported service's own backup or export capability at the frequency its tier requires, and route the output into the program's protected backup store rather than leaving it in the service's own storage.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** A vendor's retained copy inside its own tenant shares a failure domain with what it protects, so routing the export out matters more than enabling it. Native retention is often shorter than the program's standard, so land exports where the program's retention applies. A service that exports only through an interactive action belongs in the custom path.

- **RC-1.3.2: Custom Backups**
    - **Description:** Build, schedule, and monitor a purpose-written export job for each in-scope service with no usable native capability, drawing its credentials from the vault and emitting an explicit success or failure signal the health monitoring can consume.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Custom jobs often break on an API change or rotated credential yet still exit cleanly, so the signal reports what was produced rather than that the job ran. Give each job a named owner who understands the exported object. Validate output size and structure at write time, since a scheduler cannot tell a zero-byte export from a good one.

### RC-1.4: OT/Legacy Configuration and Engineering Backup

**Design Intent:** Fleet Operations captures each ground control station's configuration, the launch and recovery equipment's logic, and each aircraft's firmware and model versions during maintenance windows, using the manufacturers' offline tools. The payload processing workstation is backed up as a full disk image, since its software cannot be reinstalled on a supported system. Restores to fleet equipment happen only in a maintenance window with Fleet Operations present.

**NIST Control Mapping:**

- **CP-9 (partial):** carries the execution share of the shared CP-9 (partial) claim for the control-system population, covering system-level and configuration information rather than user data.
- **CM-2(3) (partial):** claimed as a fourth slice, split by artifact class with the build-artifact, model-artifact, and patch-rollback slices held by the Application and Artificial Intelligence focus areas. Its subject, retaining prior versions for rollback, is what this archive provides.
- **Declined:** citing CM-2(3) does not reopen CM-2, since Secure OT/Legacy Device Baselines sets what the configuration should be while this outcome retains what it was. MA-2 is declined because restoration scheduling is a safety agreement, not controlled maintenance.

**Deployment Type:** On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Industrial Controller/SCADA, Legacy IT (Unpatchable, Non-Industrial), Backup/Archive Repository, OT/ICS Zone-Conduit Segmentation (IEC 62443)

**External Dependencies:** The aircraft and ground equipment manufacturers, whose offline backup tools capture the equipment's configuration.

**Security Impact:** Moderate

**Activities:**

- **RC-1.4.1: Engineering Workstation/PLC Configuration Backup**
    - **Description:** Export controller logic, HMI projects, and engineering workstation project files through the vendor's supported offline or passive method, never through an agent or poller that writes to or queries a device carrying live process load.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Active polling can stop a fragile PLC, so take the capture from the engineering workstation's copy or within an agreed window. The workstation's source project often exists in one place and holds symbols and comments the compiled binary lacks. Trigger captures on configuration or firmware change rather than on a calendar.

- **RC-1.4.2: OT Asset Firmware and Configuration Version Archival**
    - **Description:** Retain a defined number of prior firmware and configuration versions per asset, each recorded with the date and the change that produced it, so a restoration can target a version known to have run correctly rather than the most recent one captured.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-2(3) (partial) mapping. The latest capture is the wrong default when the captured change caused the fault, so a one-version archive is a copy rather than a rollback capability. Set version depth from how far back a fault might plausibly start. Record what changed and who made it for each version.

- **RC-1.4.3: OT Backup Restoration Coordination with Plant Operations**
    - **Description:** Agree with operations, in advance and in writing, which restorations may be performed only inside a scheduled maintenance window, who may authorize one outside a window, and what state the process must be placed in before a restoration begins.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Reloading a controller mid-process can do more damage than the fault, so the authority belongs to the people accountable for the physical process. Write the agreement once, revisit it when the process or equipment changes, and name the emergency path explicitly. This activity is why the control-system deployment carries an operations dependency.

### RC-1.5: Backup Policy Enforcement

**Design Intent:** One backup policy per tier sets schedule, retention, and immutability, and the pipeline binds it to each resource from its criticality tag. A resource without a tier tag cannot be deployed, so no resource is created without backup.

**NIST Control Mapping:**

- **CP-9 (partial):** carries the enforcement share of the shared CP-9 (partial) claim. Automated Backup for Supported Services parameterizes the jobs, while this outcome owns the policy object and the rule that assigns it.
- **Declined:** CM-6(1) covers security configuration baselines held by the Device and Infrastructure focus area, and a backup schedule is not a security setting. SI-12 is declined because retention schedules belong to the Data focus area's DMP.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Virtual Machine/Server, Database Service, Object/File Storage, Directory/Platform Core Infrastructure, Backup/Archive Repository, Cloud Account/Subscription/Tenant Boundary, Infrastructure-as-Code (IaC)

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RC-1.5.1: Automated Backup Policy Assignment/Binding to In-Scope Resources**
    - **Description:** Bind the tier-appropriate backup policy to every in-scope resource automatically from its tags, subscription, and placement, and report as an exception any resource that matches no rule rather than leaving it silently unbound.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the core of the outcome's CP-9 (partial) mapping. Bind by rule rather than by resource list, so coverage survives growth. The unmatched-resource report makes the binding trustworthy, since ninety percent coverage looks the same as full coverage from the console. Enforce assignment continuously, because a tag change can move a resource to a different tier.

- **RC-1.5.2: Backup Policy Definition and Scope/Retention Standards**
    - **Description:** Define the program's backup policy tiers, stating for each the schedule, retention period, and capture scope it guarantees, and record the standard in the CP as the reference the binding mechanism and the compliance monitoring both evaluate against.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Keep the tier count small enough that engineers can tell the policies apart, since a sprawl of near-identical tiers usually means exceptions are becoming policies. State what each tier guarantees rather than what a platform offers. A service that cannot meet its tier then surfaces as a gap for the coverage strategy.

### RC-1.6: Backup Health and Operations Monitoring

**Design Intent:** Every backup job's completion, duration, and failure is monitored, and a failure alerts the Platform Team's backup operators. Restorability is verified on a sample each week. A backup and recovery dashboard shows each tier's current state.

**NIST Control Mapping:**

- **CP-9(1) (full):** Backup Integrity/Restorability Verification tests copies for media reliability and integrity across all three workstreams. The claim is full because nothing else in the framework tests a backup copy's soundness.
- **CA-7 (partial):** claimed for ongoing monitoring of backup and recovery measures and the dashboard's status reporting. The continuous monitoring strategy and other subject slices remain with the Manage pillar's Continuous Monitoring Program and other outcomes.
- **Declined:** CP-9(2) is reserved for Backup Recovery Testing, since a readable checksum proves nothing about restoring a system.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Virtual Machine/Server, Database Service, Object/File Storage, Directory/Platform Core Infrastructure, Industrial Controller/SCADA, Backup/Archive Repository, First-Party/Custom Application Code

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RC-1.6.1: Backup Health Monitoring**
    - **Description:** Collect job outcome, duration, and age of last successful run for every backup across the three workstreams, and treat a job that has stopped reporting as a failure rather than as an absence of news.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Track the age of the last successful run, since a console showing no failures looks the same as one whose collector stopped. Ingest the OT path's last-export record deliberately, or the program monitors only two of three workstreams. Collect duration too, since a job whose runtime doubles will soon miss its window.

- **RC-1.6.2: Alert Configuration**
    - **Description:** Route each failure and stale-backup condition to the owner recorded for the affected resource, with a severity taken from its criticality tier and a defined interval after which an unacknowledged alert escalates.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** Alert by tier, such as an immediate page for the top tier and a daily digest below it, since uniform alerting teaches engineers to ignore backup alerts. Resolve the owner through the ownership taxonomy rather than a shared list. Give escalation a stated interval and a named recipient.

- **RC-1.6.3: Backup Integrity/Restorability Verification**
    - **Description:** Run the backup platform's own integrity, checksum, and catalog verification against stored copies on a defined cycle, and treat a copy that fails as an open finding against the resource it was meant to protect rather than as a job to rerun and forget.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-9(1) (full) mapping. It catches silent corruption, which job monitoring cannot see because the job that wrote a corrupt copy succeeded. It proves a copy is readable and consistent, while Backup Recovery Testing proves restorability under CP-9(2). A monthly cycle covers the older copies the platform does not recheck on write.

- **RC-1.6.4: Backup/DR Posture Dashboard**
    - **Description:** Present job success rate, age of the last good copy against each tier's recovery point objective, and outstanding coverage gaps in one view keyed to criticality tier, and scope access to the audiences that act on it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-7 (partial) mapping. The view reports rather than determines, drawing its objectives and test results from Recovery Readiness and its gap figures from Backup Compliance and Coverage Monitoring. Key the view to criticality tier, and scope access, since a map of what the program cannot recover helps an adversary. It is Level 2 because the alerting activities already meet the mandatory floor.

### RC-1.7: Backup Compliance and Coverage Monitoring

**Design Intent:** Each week the inventory is compared with what is actually protected and at which tier's settings. Any resource below its tier's requirements opens a ticket to the Platform Team.

**NIST Control Mapping:**

- **CP-9 (partial):** carries the verification share of the shared CP-9 (partial) claim, turning the other five into a demonstrable state. Backup Health and Operations Monitoring asks whether existing jobs run, while this outcome asks whether the right things have jobs and correct retention.
- **Declined:** CM-8 and CM-8(3) are not reopened, since the inventory belongs to the Device and Infrastructure focus area's Asset Inventory and Discovery and an unprotected resource is not an unauthorized one. CA-7 is held by the sibling monitoring outcome, which reports these findings.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Identity Platform, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **RC-1.7.1: Backup Policy/Retention Compliance Monitoring**
    - **Description:** Evaluate each protected resource's bound policy against the schedule, retention period, and capture scope its tier requires, and report every divergence identified by the tier it failed rather than as one undifferentiated list.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Divergence usually arrives as a local override never reverted, such as retention shortened during a storage squeeze. Name the override's author and date so the exception process can act. Route retention below the Data focus area's DMP schedule as both a records and a recovery finding. Report by failed tier rather than by count.

- **RC-1.7.2: Backup Coverage Gap Identification and Remediation**
    - **Description:** Reconcile the asset inventory against the set of resources holding a backup policy, open an owned item for every qualifying resource with none, and close it by binding a policy, recording an approved exception, or retiring the resource.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Give every gap one of three dispositions, so no item stays open while everyone assumes someone else owns it. Escalate an unmanaged asset to the owning discovery outcome rather than absorbing it as a backup finding. Run monthly, so a gap is found before its first restore is needed.

## RC-2: Backup Data Protection

### RC-2.1: Backup Access and Operations Security

**Design Intent:** Backup administration belongs to a small set of named operators in the Platform Team, separate from the administrators of the systems they protect. Deleting backups, shortening retention, or changing a policy needs a second approver through the privileged access platform, and the Security Team audits every such action.

**NIST Control Mapping:**

- **AC-6(1) (partial):** a third disjoint subject slice of this enhancement, tracked with the slices other focus areas hold. It covers authorization of the backup platform's administrative functions and its catalog, which lists every system the program judged worth recovering.
- **CP-9(7) (full):** Destructive Backup Operation Protection is exactly the dual authorization for deleting backup information the enhancement describes. This capability also carries CP-9d, which the Backup Automation and Coverage capability's six-way claim does not reach. Backup Data Encryption's CP-9(8) carries confidentiality and integrity, and Backup Immutability and Redundancy carries availability.
- **Declined:** AC-3(7) is not reopened, since backup roles bind to the Identity focus area's Privileged Access Control role model. IA-2(1) and IA-2(2) stay with the Identity focus area's User Authentication Controls.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Backup/Archive Repository, Privileged Access Management, Virtual Machine/Server, Self-Hosted Third-Party Application (COTS)

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **RC-2.1.1: Access Control Configuration**
    - **Description:** Define the backup platform's administrative roles at the least privilege each duty needs, keep the role that manages jobs separate from the role that can delete copies or shorten retention, and bind every one of them to identities the Identity focus area issues rather than to accounts local to the platform.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-6(1) (partial) mapping. Separate the backup administrator from the administrator of the protected system, or one account can encrypt production and delete its copy. Find and remove the local administrative account created at installation. Elevate into destructive roles through the Identity focus area's Just in Time Access.

- **RC-2.1.2: Destructive Backup Operation Protection**
    - **Description:** Require a second named authorizer and a re-assertion of multi-factor authentication before any operation that deletes a backup copy, shortens a retention period, disables a job, or removes an immutability lock, and record every such request with both identities whether or not it was approved.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-9(7) (full) mapping. Enumerate the protected operations, since a retention period edited down to a day empties recovery without any logged deletion. The second authorizer should sit outside the backup team, and denied requests are recorded as detection signals. Where the platform lacks dual authorization, grant the destructive permission only through Just in Time Access with an approver.

### RC-2.2: Backup Data Encryption

**Design Intent:** Backups are encrypted in transit and at rest under KESTREL-controlled keys rooted in the HSMs. The backup keys are escrowed under split knowledge as the KMP requires, so losing a key never means losing the backups.

**NIST Control Mapping:**

- **CP-9(8) (full):** the enhancement's subject, cryptographic protection of backup information against disclosure and modification, is this outcome's. It carries the confidentiality and integrity elements of CP-9d.
- **Declined:** SC-28 and SC-28(1) are not reopened, since the backup store falls under the Data focus area's Default Data at Rest Encryption, which holds SC-28 and a tracked SC-28(1) slice. SC-12 belongs to the Data focus area's key management outcomes and the KMP, which names this capability as a consumer.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Backup/Archive Repository, Cryptographic Hardware/HSM, First-Party/Custom Application Code, Self-Hosted Model

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **RC-2.2.1: Encryption Configuration**
    - **Description:** Enable encryption in transit to the backup store and at rest within it for every job across the three backup workstreams, selecting the algorithms and key strengths the Data focus area's approved cryptographic baseline permits rather than accepting the backup platform's defaults.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the disclosure-prevention half of the outcome's CP-9(8) (full) mapping. Apply the customer-managed-key decision from the Data focus area's Encryption Key Ownership and Control, since a platform-managed key defends against little beyond a stolen disk. Check the unsupported workstream, whose exports often land in the clear on a staging host. Verify encryption on stored copies, since older copies may predate the setting.

- **RC-2.2.2: Backup Encryption Key Lifecycle Management**
    - **Description:** Register the keys protecting backup data in the program's key management service, set their rotation cadence against the longest retention period any copy under them carries, and record the escrow and recovery arrangement for each in the KMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the key-material half of the outcome's CP-9(8) (full) mapping and opens no SC-12 claim. It draws lifecycle and escrow from the Data focus area's Key Lifecycle Automation and Key Escrow and Recovery Procedures. Keep keys decryptable for the full retention of the data, since key destruction can void the recovery position. Test that keys are reachable without the system being restored, especially in an air-gapped enclave.

### RC-2.3: Backup Immutability and Redundancy

**Design Intent:** Every backup is locked against change or deletion until its retention expires, even by a fully privileged account. Copies leave the data center on two paths. One goes to the alternate site, and the other goes to immutable storage in the cloud provider's second IL5 region, so no single site or region holds every copy.

**NIST Control Mapping:**

- **CP-9 (partial):** claimed partial for the availability element of CP-9d as a disjoint slice, separate from the six-way claim Backup Automation and Coverage tracks. No CP-9 enhancement describes a write-once retention lock.
- **CP-9(3) (full):** the placement dimension of Geographic Redundancy.
- **CP-9(5) (full):** the transit dimension of Geographic Redundancy, timed against the recovery objectives.
- **Declined:** CP-9(7) is not claimed, since immutability makes deletion impossible rather than requiring two approvers. CP-6 belongs to Alternate Site and Telecommunications Readiness, which establishes the site. CP-9(6) describes a live standby system and belongs to Disaster Recovery Capabilities.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Backup/Archive Repository, Private Connectivity/Dedicated Circuit, Cloud Account/Subscription/Tenant Boundary

**External Dependencies:** The IL5 cloud provider, whose native backup service and second IL5 region KESTREL relies on under its provisional authorization. The parent organization, which hosts KESTREL's alternate site under a facility agreement.

**Security Impact:** High

**Activities:**

- **RC-2.3.1: Immutability Configuration**
    - **Description:** Lock stored copies under a write-once, read-many retention policy for the period each criticality tier requires, using the platform's compliance-mode lock rather than a governance-mode lock the account that set it can also release, confirm that no administrative role can shorten or remove it, and record the retention-lock period per tier in the CP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-9 (partial) mapping. Use compliance mode rather than governance mode, since a lock a privileged account can shorten is only a policy. Set the lock period with the Data focus area's DMP in view, because locked copies cannot be removed later. Prove the lock by attempting a privileged deletion against a test scope.

- **RC-2.3.2: Geographic Redundancy**
    - **Description:** Replicate each critical system's backup to a facility or region far enough from the primary that no single fire, flood, power event, or regional platform outage reaches both, set the transfer window so the secondary copy is never staler than its tier's recovery point objective, and record the placement and transfer-window arrangements in the CP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-9(3) (full) and CP-9(5) (full) mappings, through placement and transfer timing. Separation concerns shared failure domains, including a shared tenant and credentials, not distance. Fix the replication scope to the coverage baseline's tiers rather than the bill. In an air-gapped enclave, offline media under the Data focus area's Media Protection Policy and Procedures replaces replication, and rotation bounds the recovery point.

## RC-3: Recovery Readiness

### RC-3.1: Recovery Objective Definition (RTO/RPO)

**Design Intent:** Tier 1 has a recovery time of 4 hours and a recovery point of 15 minutes. Tier 2 has 24 hours for both. Tier 3 has a recovery time of 7 days and a recovery point of 24 hours. Raw collection has an extra safety net, since aircraft storage modules keep each recording until the data lake confirms it. These objectives are checked against every recovery test, and any tier that misses is raised to the AO.

**NIST Control Mapping:**

- **CP-2(3) (full):** the enhancement's subject, resuming essential functions within a defined period, is the recovery time objective set here. The plan section recording it belongs to the Contingency Planning capability.
- **CP-9 (partial):** no Rev 5 enhancement covers the recovery point objective, so the base is claimed as a further disjoint slice. The other CP-9 holders back up at a frequency consistent with the objective, while this outcome sets it.
- **Declined:** CP-2(8) is declined because the Response focus area's Asset Criticality and Business Impact Assessment reserved it for the capability that owns the CP, and tiers are read from that shared register.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Identity Platform, Network Infrastructure, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RC-3.1.1: RTO/RPO Determination per System/Data Criticality Tier**
    - **Description:** Derive a recovery time objective and a recovery point objective for each criticality tier from the mission consequence the Manage pillar's BIA established, and record both per tier in the CP as the reference the backup frequencies, replication windows, and failover designs are built against.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-2(3) (full) and CP-9 (partial) mappings. Set objectives per tier, since per-system figures are unmaintainable and the tier is the unit backup and failover designs use. Derive figures from consequence rather than current capability. Where the enterprise BIA has not reached a process, state the needed objective and its assumption for the BIA to confirm. Price a zero objective as a continuously replicated standby.

- **RC-3.1.2: RTO/RPO Validation against Actual Recovery Test Results**
    - **Description:** Compare each tier's published objective against the elapsed time and data loss the restoration tests and disaster recovery exercises actually produced, and close the difference either with a funded engineering change or with a revised objective, recording which was chosen and who approved it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the verification side of the outcome's CP-2(3) (full) mapping. Every gap gets one of two dispositions, namely invest until the result meets the objective or lower the objective and accept the exposure through the Manage pillar's risk capabilities. Take measurements from Backup Recovery Testing and Disaster Recovery Capabilities. Propagate a revised figure back to backup frequencies, transfer windows, and the Backup/DR Posture Dashboard.

### RC-3.2: Backup Recovery Testing

**Design Intent:** Each quarter, the Platform Team restores a sample from every tier using only the written procedure, and measures the result against the tier's objectives. A full restore of the identity provider and of one mission team's prod spoke runs once a year. Models are restored from the registry and verified against their signatures.

**NIST Control Mapping:**

- **CP-9(2) (full):** Backup Health and Operations Monitoring reserved this enhancement for this outcome, whose sampled restoration inside contingency plan testing matches it element for element. A checksum proves a copy is readable, while this outcome proves a system can be restored.
- **CP-4 (partial):** one of three slices divided by test method, with this outcome covering component-level restoration and Disaster Recovery Capabilities holding the other two. The three are tracked jointly.
- **Declined:** CP-4(1) and CP-4(2) are held by Disaster Recovery Capabilities. CP-10 is declined because Recovery and Return-to-Operations Validation reserved CP-2 and CP-10 for the capability that owns the CP.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Application/API, Identity Platform, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RC-3.2.1: Recovery Testing Strategy**
    - **Description:** Define which systems are restore-tested, on what cadence, from which copy population, and against what success criterion, rotating the sample so every tier and all three workstreams are reached across a full cycle, and record the schedule in the CP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the scoping and cadence dimension of the outcome's CP-4 (partial) mapping. Design the sample so it rotates across the estate rather than repeating the easiest database. State the success criterion in advance in elapsed time to service and data lost. Include prerequisites such as the identity platform, key management service, and network path in the test's scope.

- **RC-3.2.2: Recovery Procedure Validation**
    - **Description:** Execute the sampled restoration using only the written procedure, record the elapsed time and the data lost against the tier's objectives, and raise every improvised step as a defect against the procedure rather than repairing it in the moment and moving on.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-9(2) (full) mapping and the execution half of its CP-4 (partial) mapping. Have someone other than the procedure's author perform the restoration. Restore into an isolated environment and compare against the original. Hand results to RTO/RPO Validation against Actual Recovery Test Results as measurements, with OT restorations run on spare hardware or in an agreed window.

### RC-3.3: Disaster Recovery Capabilities

**Design Intent:** The cloud spokes can be rebuilt in the cloud provider's second IL5 region from infrastructure as code and the replicated backups. The data center's Tier 1 services fail over to a warm standby at the alternate site, so identity and the PKI keep working if the data center is lost. A full failover exercise runs each year and a contingency plan tabletop runs each half year, and their findings update the CP.

**NIST Control Mapping:**

- **CP-4 (partial):** a three-way split by test method, with this outcome holding the full-scale and discussion-based slices. Backup Recovery Testing holds the component-level slice, and the three are tracked jointly.
- **CP-4(1) (full):** coordinating contingency plan testing with related plan owners, which pairs with the Response focus area's IR-3(2) claim. CP-2(1) covers coordination during plan development, while testing is run here.
- **CP-4(2) (full):** testing the plan at the alternate processing site, which Alternate Site and Telecommunications Readiness establishes.
- **CP-9(6) (full):** claimed on the reservation Backup Immutability and Redundancy recorded. Its subject is a standby able to resume the mission, which this outcome maintains, and the exercise demonstrates activation without loss or disruption.
- **Declined:** CP-4(3) and CP-4(5) describe automated testing and fault injection this human-led exercise does not build, the same ground on which the Response focus area declined IR-3(1). CP-4(4) was withdrawn into CP-10 in Rev 5. CP-10 is reserved for the capability that owns the CP.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Network Infrastructure, Application/API, Directory/Platform Core Infrastructure, Industrial Controller/SCADA

**External Dependencies:** The IL5 cloud provider, whose native backup service and second IL5 region KESTREL relies on under its provisional authorization. The parent organization, which hosts KESTREL's alternate site under a facility agreement.

**Security Impact:** Moderate

**Activities:**

- **RC-3.3.1: Full-Scale Disaster Recovery/Failover Exercise**
    - **Description:** Fail the mission-critical systems over to their secondary instances at the alternate site under exercise conditions, operate the mission from there for a defined period, then fail back, recording the actual time to service and the data lost against each tier's objectives.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-4 (partial), CP-4(1) (full), and CP-4(2) (full) mappings and the demonstration clause of its CP-9(6) (full) mapping. Include failback, the half most often cut and most often failing. Run the exercise from the alternate site with the people who would staff it, which surfaces badge, image, and license problems. Include incident response and external providers, and exercise control systems in simulator or discussion form.

- **RC-3.3.2: CP Tabletop Exercise Facilitation**
    - **Description:** Facilitate a discussion-based walkthrough of the CP against a realistic disruption scenario, without failing over any live system, that exercises who holds authority to declare activation, the order in which systems and sites are restored, and the handoffs and communication paths between roles, and record every decision the group could not reach as a finding.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries one of the outcome's two locally-held CP-4 (partial) slices, namely the discussion-based method. Run it often and cheaply between full-scale exercises, following the graduated pattern of NIST SP 800-84. Work the scenario against the CP itself, testing activation authority, recovery order, and handoffs. CP-4(1) is held by Full-Scale Disaster Recovery/Failover Exercise, and control systems are walked through in discussion form.

- **RC-3.3.3: DR Exercise Findings Remediation and Plan Update**
    - **Description:** Log every defect either exercise exposed against the procedure, architecture element, or CP section responsible for it, assign an owner and a due date to each, and close them before that exercise's next cycle rather than carrying them forward as known limitations.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the review-and-corrective-action clause of the outcome's CP-4 (partial) mapping. It stays separate from the Response focus area's Exercise Findings and Plan Update Tracking, since the two feed different plans and owners. Route each finding by what it changes, such as a missed objective to RTO/RPO Validation against Actual Recovery Test Results. Close findings before the next exercise.

### RC-3.4: Alternate Site and Telecommunications Readiness

**Design Intent:** The alternate site is a parent organization facility that hosts KESTREL's warm standby, a second HSM, and a copy of the backups. A second dedicated circuit on a separate path links it to the cloud. The agreement names who may activate it and how quickly it must accept the workload.

**NIST Control Mapping:**

- **CP-2(2) (full):** capacity planning for processing, telecommunications, and environmental support, which spans both activities.
- **CP-6 (full):** the alternate storage site and its agreements, taken on the reservation Backup Immutability and Redundancy recorded with CP-9(3) and CP-9(5).
- **CP-6(1) (full):** separation of the alternate storage site from the primary.
- **CP-6(2) (full):** configuring the storage site to meet the recovery objectives. CP-9(5) covers how fast copies arrive, while this covers serving them back in time.
- **CP-6(3) (full):** the accessibility analysis for the storage site and the mitigations against an area-wide disruption.
- **CP-7 (full):** the alternate processing site, its agreements, equipment, and controls equivalent to the primary's. The Protect pillar's controls apply at the alternate unchanged, closing the most common failover gap.
- **CP-7(1) (full):** separation of the alternate processing site from the primary.
- **CP-7(2) (full):** accessibility of the processing site under the disruptions that would make it necessary.
- **CP-7(3) (full):** priority-of-service provisions written into the site agreements.
- **CP-7(4) (full):** preparing the site to be used as the operational site rather than merely reserved.
- **CP-8 (full):** the alternate telecommunications service supporting essential mission and business functions.
- **CP-8(1) (full):** priority-of-service provisions in the telecommunications agreements.
- **CP-8(2) (full):** elimination of single points of failure across the paths.
- **CP-8(3) (full):** separation of the primary and alternate providers.
- **CP-8(4) (full):** the providers' own contingency plans, written into an agreement this outcome negotiates.
- **CP-8(5) (full):** a periodic circuit-level failover test, distinct from Disaster Recovery Capabilities' site-level exercise.
- **Declined:** CP-7(6), CP-2(6), and CP-2(7) are plan elements the Contingency Planning capability owns. PE-17 is declined because physical security belongs to the PSO and sits outside the SABER's scope.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Application/API, Directory/Platform Core Infrastructure, Network Infrastructure, Industrial Controller/SCADA

**External Dependencies:** The parent organization, which hosts KESTREL's alternate site under a facility agreement. The circuit provider, which supplies the second dedicated circuit on a separate path.

**Security Impact:** Moderate

**Activities:**

- **RC-3.4.1: Alternate Processing/Work Site Designation and Agreement**
    - **Description:** Select and contract the alternate processing and work sites with priority-of-service provisions and a stated activation window, stage the equipment, connectivity, capacity, and access the essential functions require so operations can begin there rather than be arranged there, analyze what would make the site unreachable during an area-wide event, and record the site and agreement arrangements in the CP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-6, CP-6(1), CP-6(2), CP-6(3), CP-7, CP-7(1), CP-7(2), CP-7(3), and CP-7(4) mappings and the processing and environmental portion of its CP-2(2) mapping. Judge separation by shared failure domains, such as power grid, carrier footprint, provider control plane, and administrative credentials. Match site readiness to the recovery time objective, and raise any mismatch with the AO. Stage images, licenses, and credentials that work when the primary identity platform is down.

- **RC-3.4.2: Alternate Telecommunications Service Agreement and Redundancy**
    - **Description:** Contract an alternate telecommunications service sized for the essential functions, confirm that its physical path, carrier, and building entry share no failure focus area with the primary, require both providers to hold their own contingency plans, fail production traffic onto it on a defined cycle to prove it carries the load, and record the agreement and circuit arrangements in the CP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-8, CP-8(1), CP-8(2), CP-8(3), CP-8(4), and CP-8(5) mappings and the telecommunications portion of its CP-2(2) mapping. Verify path diversity against circuit and facility records rather than the order form, and re-verify after provider changes. Write priority-of-service into contracts and enroll in national priority programs in advance. In an air-gapped enclave, the obligation covers transport between facilities, or media courier where none exists.

### RC-3.5: Manual/Fail-Safe Operational Fallback Readiness

**Design Intent:** The fleet keeps flying without the cloud or the data center. Operators fly from the ground control stations with local smart card sign-in, and aircraft keep recordings on their storage modules until the lake returns. Analysts work from the last delivered products, and mission planning reverts to manual if the planning agent is unavailable. The program manager authorizes activating fallback, and operators drill it each year.

**NIST Control Mapping:**

- **CP-2(5) (full):** continuing essential functions until full restoration is exactly what manual and degraded-mode operation provides. The plan section describing it belongs with the CP.
- **CP-3 (full):** role-based contingency training on assignment, on system change, and at a defined frequency, with content reviewed on its own cycle.
- **CP-3(1) (full):** the simulated events the degraded-mode drills supply.
- **Declined:** CP-3(2) concerns realism mechanisms for a constructed training environment, while these drills use the real procedures. IR-4(3) stays with the Response focus area's Human-in-the-Loop Containment, which owns the isolation decision while this outcome owns the operator's procedure. CP-13 is held by the Identity focus area's Emergency Access.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, First-Party/Custom Application Code, Self-Hosted Third-Party Application (COTS), Industrial Controller/SCADA

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RC-3.5.1: Manual Operational Procedure Documentation**
    - **Description:** Write the procedure that carries each mission-critical process without its supporting systems, naming the inputs to be captured by hand, the approvals that substitute for automated ones, the limits of what can be done in that mode, and the reconciliation that returns the manual record to the system when it comes back, and record the procedures in the CP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the documentation half of the outcome's CP-2(5) (full) mapping. Include reconciliation on return, so hand-recorded transactions rejoin the system of record. State how long each mode can be sustained. Have the people who perform the work author the procedure, keep it reachable while systems are down, and define physical-process modes jointly with the operations authority.

- **RC-3.5.2: Fail-Safe/Degraded-Mode Operational Training and Drills**
    - **Description:** Train every person holding a contingency role in the manual and degraded-mode procedures within a defined period of taking that role, refresh the training on the program's cycle and whenever the procedure or the underlying system changes, and run drills that exercise the procedures under simulated disruption conditions.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CP-3 (full) and CP-3(1) (full) mappings. Train people within a defined period of assuming a role rather than at the next annual cycle. Draw drill scenarios from disruptions the program has seen or credibly faces, and review content after each drill or real activation. In control-system environments, run drills under the operations authority in an agreed window or on a simulator.

- **RC-3.5.3: Fallback Trigger Criteria and Activation Authority Definition**
    - **Description:** Fix the observable conditions that place a process into its manual or degraded mode, name the role authorized to declare the fallback and the role authorized to end it, and record both in the CP so that the decision is not improvised by whoever noticed the outage first.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the activation half of the outcome's CP-2(5) (full) mapping. Write criteria as observable conditions, such as an outage exceeding a stated duration. Name the authority to return to normal operations, since resuming too early can re-enter the fault. For a security incident, state which Response focus area severity levels invoke a fallback, and for a physical process, assign authority to the operations authority.

## RC-4: Contingency Planning

### RC-4.1: Contingency Plan (CP)

**Design Intent:** The Platform Team authors KESTREL's CP, with Fleet Operations writing the fleet sections and each team writing its restoration order. The ISSM reviews it, and the Configuration Control Board approves it. It holds the contingency roster and says what is shared with the CSSP, partners, and the AO during a disruption. It is revised each year and after every exercise.

**NIST Control Mapping:**

- **CP-1 (partial):** this outcome holds the partial slice of contingency-specific procedures, while the family-level policy sits with the Manage pillar's Security Policy Framework. CP-1 has no enhancements in Rev 5.
- **CP-2 (full):** the five activities below perform the base's clauses end to end, and the plan consolidates the determinations sibling outcomes record. Sibling outcomes hold CP-2(2), CP-2(3), and CP-2(5), which add elements without weakening the base claim. Here, CP-2a.3 and CP-2a.6 are decided directly. CP-2c marks the boundary with the IRP, which governs response to an adversary while the CP governs restoration of the mission.
- **CP-2(1) (full):** coordination during plan development is claimed here, while Disaster Recovery Capabilities holds CP-4(1) for testing coordination.
- **CP-2(6) (full), CP-2(7) (full):** the plan elements for transfer to the alternate sites and coordination with external providers, reserved here by Alternate Site and Telecommunications Readiness. CP-2(6) covers continuity by moving to alternate sites, unlike the broader CP-2(5).
- **CP-2(8) (full):** claimed for identifying critical assets in the plan, closing the deferral the Response focus area and this focus area's earlier outcomes recorded. Assets are read from the shared register and the Manage pillar's Business Impact Analysis (BIA) rather than rated again.
- **CP-7(6) (full):** planning for circumstances that preclude return to the primary site, reserved here by Alternate Site and Telecommunications Readiness and often missing outright.
- **CP-10 (full):** claimed full on the reservation Recovery and Return-to-Operations Validation recorded. The plan provides for recovery to a known state, defining that state, the restoration sequence, and the reconstitution steps. The focus area's restoration mechanisms claim no part of it.
- **Declined:** CP-10(4) is held by the Artificial Intelligence and Application focus areas for component-level restoration. CP-10(2) and CP-10(6) describe implemented mechanisms this plan does not build. The nearest work to CP-10(6) is Backup Data Protection's CP-9 enhancements. CP-10(1), CP-10(3), and CP-10(5) were withdrawn in Rev 5.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Identity Platform, Network Infrastructure, Device/Workstation, Application/API, AI/ML System, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RC-4.1.1: CP Development and Authoring**
    - **Description:** Consolidate into a single contingency plan what the focus area's other capabilities produced, namely the coverage baseline, recovery objectives and restoration priorities, critical assets and the essential functions they support, tested restoration procedures, manual fallbacks, and alternate site, telecommunications, and external provider arrangements, along with the known-state definition and reconstitution criteria that validate a restored system before it returns to normal operations and the circumstances under which the program would not return to the primary site at all, and mark, store, and restrict access to it at the level its content requires.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the plan-development clauses of the outcome's CP-2 (full) mapping, namely CP-2a.1, CP-2a.2, CP-2a.4, CP-2a.5, CP-2c, and CP-2h. It also carries the outcome's CP-2(1), CP-2(6), CP-2(7), CP-2(8), CP-7(6), and CP-10 (full) mappings and the procedures half of its CP-1 (partial) mapping. Under CP-2(1), coordinate with related plan owners, the alternate site operator, plant operations, and external providers while writing. Settle restoration order with mission owners in advance, and protect the plan as sensitive.

- **RC-4.1.2: CP Review and Approval**
    - **Description:** Circulate the drafted CP to the stakeholders who would have to execute it, secure formal approval from the accountable authority, and put a current copy in the hands of every person, organizational element, and external party the plan assumes will act on it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries CP-2a.7 and CP-2b of the outcome's mapping and the dissemination clause of its CP-1 (partial) mapping. Distribute after approval, giving the alternate site operator, telecommunications provider, and plant operations the portions that name them. Keep copies reachable while systems are down. Approval also fixes the review frequency CP Periodic Review and Revision follows.

- **RC-4.1.3: CP Periodic Review and Revision**
    - **Description:** Revisit the CP on the cadence its approval fixed, revise it for changes to the organization, the systems it covers, or the environment of operation and for problems encountered during its execution or testing, and communicate each revision to everyone holding a copy.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries CP-2d through CP-2g of the outcome's mapping and the review clause of its CP-1 (partial) mapping, superseding the One-Time issuance. Notify every holder of a revision, so stale copies do not circulate. Route lessons into Recovery Testing Strategy and the training drills as well as the plan text. Annual review is the floor, and exercise findings, validation gaps, and new systems drive most revisions.

- **RC-4.1.4: Contingency Roster and Contact Information**
    - **Description:** Name the recovery coordinator, the disaster recovery execution team, the alternate site and telecommunications liaisons, and the plant operations authority for any control-system segment, along with contact information that reaches each of them outside business hours and a backup for any role a single point of failure would otherwise leave unfilled, and record the roster in the CP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the CP-2a.3 clause of the outcome's CP-2 (full) mapping. It names who fills the contingency roles that the training and fallback activities define. Keep contacts reachable without the identity platform, and name a backup for every role.

- **RC-4.1.5: Contingency Information Sharing and Disclosure Procedures**
    - **Description:** Determine what contingency-plan information may be shared with a mutual aid partner, another agency, or an external service provider during an active disruption, at what classification or handling restriction, and who is authorized to release it, consistent with the program's legal and regulatory disclosure obligations, and record the determination in the CP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the CP-2a.6 clause of the outcome's CP-2 (full) mapping. Decide with program counsel and the PSO, since external disclosure is a classification and legal question first. It sets the disclosure boundary for plan content and event information, not the provider relationships CP Development and Authoring covers. For a reportable incident, defer to the Response focus area's external notification procedures.
