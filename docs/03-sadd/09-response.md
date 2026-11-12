# RS: Response

*KESTREL SADD, Section 5 (Operate). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## RS-1: Incident Preparation

### RS-1.1: Incident Response Development

**Design Intent:** Runbooks cover the cloud provider's own incident types, such as a compromised subscription, an exposed storage service, or a stolen workload identity. They use the provider's native response actions. AI/ML runbooks cover a poisoned training snapshot, a compromised or misbehaving AI agent, a foundation model incident on the provider's side, and a lost aircraft carrying an onboard model. Each runbook names the team that executes it.

**NIST Control Mapping:**

- **IR-4 (partial):** the procedure layer of the incident handling capability, split by dimension from the endpoint-mechanism slice Endpoint Response holds. It is partial because live handling, containment, and lessons learned sit with this focus area's later capabilities.
- **Declined:** IR-4(1), IR-4(4), IR-4(5), and IR-4(12) stay with Endpoint Response. IR-4(11) is claimed by the sibling Incident Response Team Structure and Training outcome. SI-4 and SI-4(2) stay with the Detection focus area's Platform-Native Threat Detection, which enables the provider's detection service.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Object/File Storage, Artifact/Model Registry, Application and Service Account Identity, AI Agent Identity, AI/ML System

**External Dependencies:** The IL5 cloud provider, whose native threat protection and response actions the cloud runbooks use.

**Security Impact:** Moderate

**Activities:**

- **RS-1.1.1: Cloud Platform-Native Incident Response Runbook Development**
    - **Description:** Write a runbook for each incident type the program's cloud platforms actually produce, naming the provider console and API actions that triage, contain, collect evidence from, eradicate on, and restore the affected resource, and version every runbook alongside the IRP it executes under.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the core of the outcome's IR-4 (partial) mapping. Scope the set by what the environment produces, such as a compromised access key, an exposed storage container, an unauthorized compute workload, and a control-plane privilege escalation. Each runbook names the account, role, and permission a responder needs to execute it.

- **RS-1.1.2: Cloud-Native Threat Protection Platform Integration**
    - **Description:** Connect the cloud provider's native threat protection service into the response path by binding its findings and case objects to the program's incident record and enabling the response actions the runbooks invoke, so responders work from one place rather than from each provider's console in turn.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's IR-4 (partial) mapping, connecting the provider's findings to the procedure that acts on them. Enabling and tuning the detection service stays with the Detection focus area's Platform-Native Threat Detection, so no SI-4 claim is reopened. It is Level 2 because responders can still open each provider console directly, only more slowly.

- **RS-1.1.3: AI/ML Incident Runbook Development**
    - **Description:** Write a runbook for each AI-specific failure mode the program's fielded models can produce, such as data poisoning, prompt injection exploitation, model theft, adversarial concept drift, agentic scope violation, high-risk-action approval gate bypass, and unauthorized tool-call chaining, naming for each the detection source that raises it, the model-specific action it triggers, whether kill-switch invocation, version rollback, serving-traffic quarantine, revocation of the model's service identity and API keys, or revocation of an agent's delegated credential and forced session termination, and the point at which the model registry is consulted to identify every deployment the incident's scope reaches.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries a further slice of the outcome's IR-4 (partial) mapping, split from the cloud runbooks by platform class. Containment is ordinarily the Artificial Intelligence focus area's Rollback/Kill-Switch Mechanism rather than host network isolation, while an irreversible agentic action calls for revoking the agent's delegated credential. Agentic scope violation and unauthorized tool-call chaining name Agent Tool/API Access Scoping's reachable-set revocation and Agentic Session Timeout and Forced Termination's forced suspension, with investigation starting from Agentic AI Tool-Call and Action Logging (Application/API Logging). An approval gate bypass instead disables the agent's task-scoped credential issuance pending review of why the gate did not fire. The model registry lookup resolves an incident to every serving deployment of the affected model version, not just the endpoint that raised the alert.

### RS-1.2: Incident Response Team Structure and Training

**Design Intent:** The ISSM leads every incident, with the ISSOs and security analysts as the hands-on responders. The CSSP contains what cannot wait for the on-call analyst, using the pre-approved playbooks. The Platform Team, IT Operations, and Fleet Operations act on their own systems at the ISSM's direction. For a model incident, the ML team owns the model and the mission team owns the use case, and both join the response. Every responder trains on KESTREL's own tools and runbooks each year, and the AO funds the CSSP and tooling through the program budget.

**NIST Control Mapping:**

- **IR-2 (full):** the only claim of the control in the framework. Develop Team Training delivers role-based training on assignment, on a defined cycle, and when the system changes.
- **IR-4(11) (full):** the integrated response team itself, cited at the enhancement because its subject is the team rather than the handling of any one incident.
- **Declined:** AT-3 is not claimed, since IR-2 is the purpose-built control here and the Manage pillar's Role-Based Specialized Training holds general role-based training. IR-4(6) and IR-4(7) cover the insider threat dimension, which splits like IR-9(4) does, with the personnel half at the PSO and the detection half at User/Entity Behavior Analytics (UEBA) / Insider Threat Detection.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Identity Platform, Network Infrastructure, Device/Workstation, Application/API, AI/ML System, Industrial Controller/SCADA

**External Dependencies:** The CSSP, under the detection and response split in its service agreement.

**Security Impact:** Moderate

**Activities:**

- **RS-1.2.1: Organize Team Structure**
    - **Description:** Name the response team's roles, the authority each holds to direct containment, notification, or system shutdown, the on-call coverage that keeps every role reachable outside business hours, and the escalation path between them, and record the result in the IRP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-4(11) (full) mapping. Plan coverage per facility and per enclave, since a responder who cannot be admitted to a facility is not deployable to it. Assign decisions such as isolating a production system or notifying outside the program in advance. IR-4(14) is not claimed, and IR-8 is left to the focus area's Incident Response Plan (IRP) outcome.

- **RS-1.2.2: Develop Team Training**
    - **Description:** Build and deliver role-specific incident response training against the program's own systems, runbooks, and reporting deadlines, require it of each responder before they take an on-call rotation, and repeat it on the program's defined cycle and whenever the response procedures materially change.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-2 (full) mapping. Train responders before they join the rotation rather than at the next annual cycle, and revise the material whenever Incident Response Development revises a runbook. IR-2(1) is delivered through the Incident Response Plan Testing and Exercises outcome under IR-3, IR-2(2) is unlikely to be tailored in, and IR-2(3) belongs with the Privacy Compliance capability.

- **RS-1.2.3: AI Incident Escalation Path and Model Owner Accountability**
    - **Description:** Name the model owner as the accountable role for a model implicated in an incident, extend the response team's escalation path to route an AI-specific incident to the Manage pillar's AI/ML Governance Review Board at the severity threshold the focus area's severity model sets, record the external reporting triggers an AI incident carries beyond the program's standing regulatory obligations, and document the escalation path and accountability role in the IRP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, elaborating the escalation content Organize Team Structure names under the outcome's IR-4(11) (full) mapping. It names the model owner role and routes escalation to the AI/ML Governance Review Board, since retiring, retraining, or narrowing a model is that board's decision rather than the incident commander's. Record AI-specific external reporting triggers here, since the board carries the AO's expectations for AI failure modes.

- **RS-1.2.4: Response Capability Resourcing and Management Support**
    - **Description:** Determine the staffing level, on-call coverage capacity, and tooling and platform budget the response capability needs to sustain the team structure's committed coverage and the training program's cadence, secure management's endorsement of that determination as a standing commitment rather than a one-time budget line, and document the resourcing determination and management support commitment in the IRP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation, supplying the resources and management support element IR-8a asks the plan to state. The focus area's Incident Response Plan (IRP) outcome holds IR-8 and draws this activity in. Set staffing and on-call capacity against the roster Organize Team Structure requires and the cadence Develop Team Training sets, and state the tooling budget the runbooks assume. Capture management's endorsement as a standing commitment revisited on the outcome's review cycle.

### RS-1.3: Incident Response Plan Testing and Exercises

**Design Intent:** The response team runs a tabletop twice a year, one with an aircraft or ground segment scenario and one with an AI scenario. It also runs a functional exercise each year with the CSSP, using the real tools. Each exercise's findings become tracked changes to the IRP and runbooks.

**NIST Control Mapping:**

- **IR-3 (full):** the only claim of the control in the framework, since the two exercise activities test the response capability on the program's cycle with discussion-based and functional methods.
- **IR-3(2) (full):** coordinating that testing with the Recovery focus area's Contingency Planning capability and the continuity owners it serves. The contingency side of that relationship stays with the CP family.
- **IR-3(3) (full):** Exercise Findings and Plan Update Tracking uses exercise data to measure effectiveness and improve the process.
- **Declined:** IR-3(1) is not claimed because both exercises are human-led. A program that adds automated response testing would open it.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Security Information and Event Management (SIEM) Platform, Compute, Identity Platform, Network Infrastructure, Device/Workstation, Application/API, Industrial Controller/SCADA

**External Dependencies:** The CSSP, which takes part in the functional exercise.

**Security Impact:** Moderate

**Activities:**

- **RS-1.3.1: Tabletop Exercise Planning and Facilitation**
    - **Description:** Assemble scenario packets from the incident types the program's threat model and detection coverage make most likely, facilitate the discussion-based exercise with the responders and decision-makers who would actually be in the room, and capture as a finding every decision the group could not reach.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's IR-3 (full) mapping. Focus on the decisions the group cannot make, since those are the ones a real incident would stall on. Include the AO's representative, the PSO, and program counsel in at least one scenario per cycle. Draw at least one scenario per cycle from the AI incident taxonomy that Automated Severity Scoring and Escalation maintains, preferring a cross-domain failure such as a prompt injection that escalates into an agentic scope violation.

- **RS-1.3.2: Functional Incident Response Exercise Execution**
    - **Description:** Execute a functional exercise in which responders operate the real tooling against a seeded scenario, and invite the owners of the contingency, disaster recovery, and continuity plans an incident would run alongside so the handoffs between those plans are exercised rather than assumed.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's IR-3 (full) mapping and the whole of its IR-3(2) (full) mapping, which requires the related-plan owners to take part. A functional exercise finds mechanical failures a tabletop cannot, such as revoked permissions, a redesigned console, or a silently failing paging integration. Seed the scenario into a representative environment rather than production. Exercise a control-system segment in simulator or discussion form only, which is why this activity's live execution does not reach Cyber-Physical System (OT/ICS).

- **RS-1.3.3: Exercise Findings and Plan Update Tracking**
    - **Description:** Record each exercise finding as an owned, dated item against the specific runbook, procedure, or IRP section it changes, drive it to closure, and derive from successive exercises the measures that show whether response performance is improving.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-3(3) (full) mapping and part of its IR-3(2) (full) mapping. Give each finding an owner and a date, and keep the resulting measures accurate, consistent, and reproducible. It stays distinct from the Systemic Lessons Learned Process, which runs the same loop over real incidents, though both feed the IRP.

### RS-1.4: Security Contact Information

**Design Intent:** The security contact on every subscription and the tenant is the Security Team's monitored address and the CSSP's operations center, never an individual. The Security Team checks the contacts each quarter.

**NIST Control Mapping:**

- **IR-7(2) (partial):** a populated and maintained security contact record identifies the team to external protection providers. It is partial because the sibling Cyber Defense Service Provider Alignment holds the fuller service agreement and division of responsibilities.
- **Declined:** the IR-7 base is not claimed, since a user help-desk resource differs from the provider-facing contact record kept here. It stays available to the focus area's Incident Response Plan (IRP) outcome.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Cloud Account/Subscription/Tenant Boundary, Serverless/Platform Service

**External Dependencies:** The IL5 cloud provider, whose security team uses these contacts.

**Security Impact:** Low

**Activities:**

- **RS-1.4.1: Cloud-Native Threat Protection Platform Security Contact Configuration**
    - **Description:** Set the security and abuse contact fields in every account, subscription, project, and tenant inside the boundary, and in the threat protection platform itself, to a monitored role address and distribution list the response team actually reads rather than to any individual's mailbox.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the identify-the-team-to-the-provider half of the outcome's IR-7(2) (partial) mapping. Most platforms hold these fields per account, so check every new account rather than setting the value once. Route notices to a monitored distribution list rather than an individual's mailbox.

- **RS-1.4.2: Security Contact Information Review and Update Cadence**
    - **Description:** Review every security contact record the program maintains with an external provider on a defined cycle and on any change to response team membership, and verify by test message that each address still reaches a person.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the maintain-the-relationship half of the outcome's IR-7(2) (partial) mapping. Verify each record with a test message, since a valid record can still route to an empty distribution list. Its scope reaches every external protection provider, including vendors for on-premises and isolated enclaves, which is why the outcome's Deployment Type is broader than the configuration activity.

### RS-1.5: Automated Notification Workflows

**Design Intent:** A declared incident pages the on-call security analyst through the service desk, and the CSSP's operations center is notified at the same time. Severe incidents also page the ISSM and the affected team's lead. The security monitoring platform hands incidents to the service desk through an event stream, not by email.

**NIST Control Mapping:**

- **IR-6 (partial):** the first clause, personnel reporting suspected incidents within a defined period, through the intake path fielded here. The sibling Incident Reporting and External Communications outcome holds the second clause, and the IRP records the period.
- **IR-6(1) (full):** the only claim of the enhancement in the framework. These paths carry both internal notification and transmission of the external reports, so it is claimed once here.
- **Declined:** SI-4(12) stays with the Detection focus area's SIEM Capabilities and the Artificial Intelligence focus area's Production Abuse Monitoring. This outcome routes declared incidents rather than adding a second alerting engine.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Serverless/Platform Service, Security Information and Event Management (SIEM) Platform, Message Queue/Event Stream

**External Dependencies:** The CSSP, under the detection and response split in its service agreement.

**Security Impact:** Moderate

**Activities:**

- **RS-1.5.1: Incident Notification Channel Configuration**
    - **Description:** Configure the channels each responder role and stakeholder is reachable on, including mail, chat, SMS, and paging, bind each channel to the on-call rotation and escalation tier it serves, and set the acknowledgment and re-escalation behavior that applies when a notification goes unanswered.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the whole of the outcome's IR-6 (partial) mapping and part of its IR-6(1) (full) mapping. Build acknowledgment and re-escalation into each channel, since without them it sends a notification rather than a page. Bind each path to a role and rotation rather than to named individuals.

- **RS-1.5.2: Monitoring Platform and Event Streaming Integration**
    - **Description:** Integrate the monitoring, SIEM, and event-streaming platforms with the notification service so that an incident record crossing the program's declaration threshold raises the page on its own, and carry the incident identifier through the message so the responder arrives at the record rather than at a description of it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the core of the outcome's IR-6(1) (full) mapping and is the capability's Automate instance, removing the human relay between a raised incident and a paged responder. The paging threshold comes from the severity scoring the Incident Detection, Analysis, and Investigation capability owns. Build an out-of-band alternate path, which in an isolated enclave cannot be a commercial internet paging service.

### RS-1.6: Incident Reporting and External Communications

**Design Intent:** The ISSM notifies the AO, and the CSSP reports to the DoD reporting chain within the timelines CJCSM 6510.01B sets. If partner data is affected, the foreign disclosure officer notifies the partner nations under their agreements. Incidents involving a vendor's product are coordinated with that vendor. When a performer laptop holding KESTREL source code is involved, the performer also reports under DFARS 252.204-7012.

**NIST Control Mapping:**

- **IR-6 (partial):** the second clause, reporting to designated authorities, paired with the first-clause claim Automated Notification Workflows holds. The AO is the first authority, with expectations set during authorization rather than by published regulation.
- **IR-6(3) (full):** notifying the affected product's provider and other supply chain organizations, a direction nothing else in this focus area covers.
- **IR-4(10) (full):** Vendor and Supply Chain Incident-Handling Coordination coordinates joint investigation, eradication, and patch timelines with an implicated vendor. IR-6(3) covers one-way disclosure instead.
- **IR-4(8) (full):** Cross-Organization Correlation and Incident Information Sharing shares incident information with a cyber defense service provider or ISAC during an active incident. It builds on the IR-7(2) contact relationship from Security Contact Information.
- **Declined:** IR-6(2) goes to Vulnerability and Patch Management. IR-9 stays with Classified Data Spillage Response. IR-4(15) covers public relations, which is not a reporting obligation of a classified program.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Self-Hosted Third-Party Application (COTS), Third-Party Dependency (Embedded Library/Package), Industrial Controller/SCADA

**External Dependencies:** The CSSP and the DoD reporting chain it reports to. The partner nations, under their memoranda of agreement. The performer, under DFARS 252.204-7012. Each vendor, under its support agreement.

**Security Impact:** Moderate

**Activities:**

- **RS-1.6.1: Regulatory/AO Incident Reporting Workflow and Timelines**
    - **Description:** Enumerate every reporting obligation the program carries to its AO, its government reporting authorities, and its contracting customer, attach to each the triggering criteria and the deadline measured from discovery, and record the workflow, the approving authority, and the report template for each in the IRP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-6 (partial) mapping. Record each deadline as measured from discovery, since a program measuring from containment will report late. Name the approving authority for each report alongside its deadline. Revisit the enumeration on the AO's cycle, since obligations change with the authorization and the contract.

- **RS-1.6.2: External Stakeholder and Authority Notification Procedures**
    - **Description:** Define who notifies affected mission partners, product and service providers, and organizations in the program's supply chain, what may be disclosed to each at what classification, and who is authorized to speak for the program, and record the procedures in the IRP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-6(3) (full) mapping. What an uncleared vendor may be told about an incident on a classified system is decided in advance with the PSO and program counsel. The procedure executes against the Contract Security Requirements of the Third-Party and Supply Chain Governance capability. It is Level 2 because the sibling activity's authority-facing workflow meets the mandatory reporting obligation.

- **RS-1.6.3: Vendor and Supply Chain Incident-Handling Coordination**
    - **Description:** Coordinate active incident-handling activities, including joint investigation scoping, eradication and patch timelines, and the exchange of technical findings, with the implicated vendor or supply-chain organization whose product or service was the entry vector or is otherwise involved in the incident.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-4(10) (full) mapping, which asks for joint handling with the provider rather than notification alone. It scopes a shared investigation, agrees an eradication or patch timeline, and exchanges indicators, unlike the one-way IR-6(3) disclosure of External Stakeholder and Authority Notification Procedures. Its results feed Exploited-Vulnerability Closure Verification where the fix comes from the vendor.

- **RS-1.6.4: Cross-Organization Correlation and Incident Information Sharing**
    - **Description:** Establish the criteria, classification handling rules, and channel by which the response team shares and receives incident-specific technical context, including indicators, scope, and technique observations, with the designated cyber defense service provider, an ISAC, or another external correlation partner while an incident is active, and record the procedure in the IRP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-4(8) (full) mapping, sharing incident information externally to learn whether the activity is part of a broader campaign. It builds on the IR-7(2) contact relationship of Security Contact Information and defines what travels over it. What may be shared with an uncleared partner is decided with the PSO, so author it alongside External Stakeholder and Authority Notification Procedures.

### RS-1.7: Cyber Defense Service Provider Alignment

**Design Intent:** The CSSP's service agreement divides the work. The CSSP monitors around the clock, triages, and supplies threat intelligence. The CSSP runs the pre-approved containment playbooks when an incident cannot wait for the Security Team, and the Security Team carries out every other response action inside KESTREL. The security monitoring platform forwards all telemetry to the CSSP. The CSSP's analysts also read that telemetry and the cloud's native threat protection in place through their host pool. The ISSM receives the CSSP's directives and advisories and tracks each one to completion.

**NIST Control Mapping:**

- **IR-7 (full):** the only claim of the base control in the framework. The designated provider is the support resource offering advice and assistance the program's own team lacks.
- **IR-7(2) (partial):** the direct cooperative relationship with the provider. The sibling Security Contact Information holds the contact record, and the two are tracked jointly.
- **IR-7(1) (partial):** the automated push and pull of provider advisories and assistance into incident tracking. It is partial because it serves the response team, while the general user help resource is left to the focus area's Incident Response Plan (IRP) outcome.
- **Declined:** IR-6, IR-6(3), and IR-4(8) are held by Incident Reporting and External Communications. SI-4 stays with the Detection focus area and the boundary security stack, whose telemetry this outcome delivers.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Security Information and Event Management (SIEM) Platform, Network Telemetry/Monitoring Platform, Intrusion Detection/Prevention System (IDPS), Serverless/Platform Service

**External Dependencies:** The CSSP, under the detection and response split in its service agreement.

**Security Impact:** High

**Activities:**

- **RS-1.7.1: Provider Service Agreement and Responsibility Division**
    - **Description:** Execute a written service agreement with the program's designated cyber defense service provider that divides monitoring, analysis, incident handling, and reporting responsibilities between the provider and the program's own response team, and record the division in the Incident Response Plan (IRP).
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-7 (full) and IR-7(2) (partial) mappings. State which events each side watches, who declares an incident, and whose direction prevails during one. The provider's responsibilities are inherited controls, so feed them to the Governance focus area's Inherited Control Validation and its SCTM entries.

- **RS-1.7.2: Telemetry and Sensor Delivery to the Provider**
    - **Description:** Deliver the logs, alerts, and sensor data the service agreement specifies to the provider continuously and in the format it requires, and alert when a feed stops or falls behind.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Monitor feed health as a control, since a silently stopped feed is the most common reason a provider cannot see an attack. Telemetry leaving a classified or isolated segment travels by its approved path, such as a cross domain solution where one is required.

- **RS-1.7.3: Provider Incident Reporting and Directive Handling**
    - **Description:** Report incidents to the provider through the channel and within the timelines the agreement and the program's reporting obligations set, and receive, track, and close the directives, alerts, and findings the provider issues to the program.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Reporting to the provider is one destination of the Incident Reporting and External Communications workflow, and this activity adds the return path. Track provider directives, such as a mandated configuration change or an indicator block, to closure against their deadlines. Raise a directive the program cannot meet with the provider and the AO.

- **RS-1.7.4: Automated Provider Advisory and Assistance Access**
    - **Description:** Integrate the provider's advisory feed and support ticketing interface with the program's incident tracking and notification service so that provider alerts land on the matching incident record automatically and responders can open and follow an assistance request from that record.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity also carries the outcome's IR-7(1) (partial) mapping. It qualifies as Automate because it removes the person who would copy advisories into the incident record or phone for help, covering both push and pull. In an isolated enclave the feed may be a scheduled transfer over the telemetry's approved path.

## RS-2: Incident Detection, Analysis, and Investigation

### RS-2.1: Automated Incident Creation and Enrichment

**Design Intent:** Correlated alerts above the declaration threshold raise an incident record in the service desk automatically. The record carries the asset's owner, team, criticality, and recent changes from the inventory, so the analyst starts with context instead of data entry.

**NIST Control Mapping:**

- **IR-5 (full):** the only claim of the control in the framework. The record raised here, carried through every state change to closure, is the tracking artifact. Production Abuse Monitoring and Network/OT Intrusion and Anomaly Detection both reserve IR-5 for this focus area.
- **IR-5(1) (full):** likewise claimed nowhere else, since the ticket-creation and enrichment automation tracks incidents and collects their information end to end.
- **Declined:** IR-4 is divided among this capability's other outcomes and Incident Preparation's. SI-4(12) stays with the Detection focus area's SIEM Capabilities outcome.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Security Information and Event Management (SIEM) Platform, Self-Hosted Third-Party Application (COTS)

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RS-2.1.1: Automated Incident Ticket Creation from Correlated Detection Alerts**
    - **Description:** Configure the detection platform to open an incident record on its own whenever a correlated alert meets the program's declaration criteria, populating it with the alert, its constituent events, the entities involved, and the discovery timestamp that starts the reporting clocks.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the creation half of the outcome's IR-5 (full) and IR-5(1) (full) mappings, and is tagged Automate because it replaces manual transcription. Capture the discovery timestamp, since every external reporting deadline is measured from it. Set declaration criteria deliberately, since an over-inclusive trigger trains responders to close records unread. For an OT-sourced correlated alert, the criteria also require confirmation from Anomaly Alert Triage and Escalation Workflow that the named engineer adjudicated the anomaly. A correlated alert with no OT-sourced constituent event opens on the criteria alone.

- **RS-2.1.2: Automated Context/Asset Enrichment**
    - **Description:** Enrich each newly raised record automatically with the affected asset's owner, its criticality rating, its classification and enclave, and the incidents previously raised against it, drawing every field from the authoritative inventory rather than from whoever is on call.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the collection and analysis half of the outcome's IR-5(1) (full) mapping. Enrichment is only as good as the Device and Infrastructure focus area's inventory, so treat an empty owner field as an inventory defect. Include prior incident history, which turns repeated minor tickets against one host into a pattern. The criticality field comes from the Asset Criticality and Business Impact Assessment outcome.

- **RS-2.1.3: XDR/SIEM-to-ITSM Integration for Incident Record Creation**
    - **Description:** Integrate the XDR and SIEM platforms with the program's IT service management system so an incident exists under one identifier across all of them, and keep state, ownership, and closure synchronized in both directions rather than in one.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's IR-5 (full) mapping, which needs one authoritative record. Build the integration two-way, since a one-way sync leaves the service management record stuck at its initial severity. Where an enclave cannot reach the enterprise system, its own tracker is the record of authority and reconciliation is a documented manual step.

### RS-2.2: Incident-Scoped Log Analysis and Investigation

**Design Intent:** Analysts investigate in the security monitoring platform's workbench, which holds every telemetry source in one place. Related alerts are folded into one incident, and each investigation's queries and findings are saved with the incident record.

**NIST Control Mapping:**

- **IR-4 (partial):** the detection and analysis phase performed against an already declared incident, split by phase from the slices Endpoint Response and Incident Response Development hold. It is partial because containment, eradication, and recovery sit with Incident Containment, Recovery, and Lessons Learned, and the comparable-and-predictable clause with Automated Severity Scoring and Escalation.
- **AU-12(3) (full):** the only claim of the enhancement in the framework. Responders raise the logging level on selected components within a defined time threshold when an investigation needs more detail.
- **Declined:** AU-7 and AU-7(1) are held by the Detection focus area's SIEM Capabilities outcome, whose platform this investigation uses. AU-6 covers routine audit review, not querying a known incident's scope.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Security Information and Event Management (SIEM) Platform, Compute, Identity Platform, Network Infrastructure, Device/Workstation, Application/API, Industrial Controller/SCADA

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RS-2.2.1: Alert-to-Incident Correlation and Deduplication**
    - **Description:** Set the rules by which related alerts collapse into a single incident, naming the entity, time window, and detection-signature dimensions they are grouped along, and merge an alert that a second platform raised for the same activity into the existing record instead of opening another one.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's IR-4 (partial) mapping, correlating alerts into an incident one level above Detection/Correlation Rule Configuration. Tune grouping in both directions, since fragmenting a campaign across many tickets hides it and merging separate intrusions gives them one scope and one closure.

- **RS-2.2.2: Investigative Log Query and Collection**
    - **Description:** Query the centralized log platform for the entities, time windows, and record classes the incident's scope demands, preserve both the result sets and the queries that produced them with the incident record, and raise the logging level on affected components where the default cannot answer the question.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the whole of the outcome's AU-12(3) (full) mapping and part of its IR-4 (partial) mapping. Preserve each query alongside its result so a finding can be reproduced later. Return the raised logging level when the incident closes, since a permanently verbose source breaks the Log Retention Strategy sizing. On control-system devices, change logging only through the vendor's engineering path with operations concurrence.

- **RS-2.2.3: SIEM-Based Investigation Workbench Usage**
    - **Description:** Establish the working surface responders investigate from, supplying saved query sets for the incident types the program actually sees, event timelines assembled across sources onto one clock, and entity relationship views showing what a compromised account or host reached.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's IR-4 (partial) mapping. It depends on the Detection focus area's Time Synchronization outcome, since clocks that disagree will misorder an adversary's steps. Build saved query sets so a less experienced responder can work a common incident type competently.

### RS-2.3: Evidence Preservation and Forensic Capabilities

**Design Intent:** Evidence collection is automated for cloud resources and data center hosts, capturing disk snapshots, memory, and the related logs. All of it goes to an evidence store in the backup repository under retention lock, with chain of custody recorded. Fleet equipment is imaged only during a maintenance window or after the aircraft has landed. Evidence handling follows the requirements of the DoD reporting chain and any law enforcement referral.

**NIST Control Mapping:**

- **IR-4(12) (partial):** the offline examination of images, memory captures, and artifacts on an isolated workstation against a copy. The other slice, the live remote-shell session, is held by Endpoint Response's Live Response activity.
- **AU-10 (partial):** the collection, access, transfer, and release of evidence, so nobody who handled an item can deny it. The Identity focus area's AI Agent Identities holds the other base slice, and the base is cited because AU-10's enhancements address information review and release rather than evidence custody.
- **Declined:** AU-9, AU-9(2), and AU-11 stay with Audit Log Integrity Protection and Log Retention Strategy, since the evidence repository runs on a legal-hold clock rather than audit retention. SI-12 sits with the Data focus area's Data Management Plan (DMP).

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Device/Workstation, Backup/Archive Repository, Industrial Controller/SCADA

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RS-2.3.1: Evidence Collection Automation**
    - **Description:** Automate the capture of volatile and non-volatile evidence at incident declaration, covering memory, running process and network state, disk images, and the platform-side audit and configuration state of the affected resources, and write each capture into the evidence store with its hash before any remediation step executes.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is tagged Automate because it replaces a manual collection sequence that must run in volatility order before containment, which often loses memory. On endpoints it uses the Device and Infrastructure focus area's Live Response session, and in the cloud a volume snapshot plus a control-plane export. On a running control-system device, collection is manual, vendor-supported, and taken only with operations concurrence.

- **RS-2.3.2: Forensic Analysis Tools Integration**
    - **Description:** Field and integrate the forensic toolchain that examines collected images, memory captures, and artifacts offline, and bind its findings back to the incident record so the analysis and the incident it belongs to do not live in separate systems.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-4(12) (partial) mapping, analyzing malicious code and residual artifacts against a working copy. Isolate the examination environment by construction, since detonating recovered malware is a legitimate step. In a classified program the toolchain must be procured, accredited, and staffed inside the boundary, which drives the one-time cost.

- **RS-2.3.3: Immutable Evidence Storage**
    - **Description:** Stand up the evidence repository under a retention lock that prevents modification and deletion for the duration of the hold, restrict access to named responders under separation from the administrators of the systems the evidence came from, and record a cryptographic hash at ingest that every later verification is checked against.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity supports the outcome's AU-10 (partial) mapping by making custody records and evidence tamper-evident. Keep evidence undeletable by the source system's administrator, and hash each item at ingest. Keep this store separate from the audit log repository and accredit it at the highest classification of evidence it may hold.

- **RS-2.3.4: Compliance and Legal Requirements**
    - **Description:** Determine with program counsel, the PSO, and the AO how long each class of evidence must be held, what triggers a legal hold and who may release one, and what the custody record must capture, maintain that record so every collection, access, transfer, and release of an item is bound to the identity that performed it, and document the retention terms and legal-hold triggers in the IRP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-10 (partial) mapping, binding each custody entry to an authenticated identity. Set default repository retention from the program's longest obligation, since holds are often placed weeks after closure. Release of classified evidence is a classification determination made with the PSO, and the determinations are consolidated into the IRP.

### RS-2.4: Asset Criticality and Business Impact Assessment

**Design Intent:** Each asset's mission criticality comes from its inventory tags and the Risk focus area's business impact analysis. The command link, the ground control stations, and the identity provider rank highest. That criticality feeds directly into each incident's severity.

**NIST Control Mapping:**

- **RA-9 (partial):** the general criticality analysis across systems, services, and data to prioritize incident response. The Artificial Intelligence focus area's robustness outcomes hold the other, ML-scoped slice. RA-9 has no enhancements in SP 800-53 Rev 5.
- **Declined:** CP-2 and CP-2(8) belong to the Recovery focus area's Contingency Planning capability and its contingency plan (CP), though both ratings should draw from one shared asset register. RA-2 stays with the Manage pillar's Security Categorization, which bounds this rating.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Application/API, Identity Platform, Network Infrastructure, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RS-2.4.1: Business Impact Classifications**
    - **Description:** Rate every system, service, and data store in the inventory against a tiered criticality scheme that states for each tier the mission consequence it represents and the response commitment it carries, name an owner accountable for each rating, and record the scheme in the IRP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's RA-9 (partial) mapping. Keep the scheme to three or four tiers and state how few assets belong in the top one. Watch for under-rating of assets that matter indirectly, such as the identity platform, DNS, PKI, and the log pipeline. Review annually against the asset inventory, coordinated with the Recovery focus area's contingency planning owner so both read the same register.

- **RS-2.4.2: Business Impact Scoring Integration into Incident Prioritization**
    - **Description:** Expose the criticality rating as a field the incident platform reads from the asset inventory automatically, and make it an input the severity calculation consumes rather than a note in the record's body a responder is expected to notice.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity joins the sibling's rating, Automated Context/Asset Enrichment, and Severity Scoring Model Definition so criticality actually drives severity. Decide explicitly what an asset missing from the inventory scores, since defaulting it to the lowest tier means untracked systems are never escalated.

### RS-2.5: Automated Severity Scoring and Escalation

**Design Intent:** Severity is computed from asset criticality, data sensitivity, scope, and whether the incident can affect an aircraft. The AI incident taxonomy adds training data poisoning, model theft, jailbreak abuse, AI agent misuse, and a compromised foundation model deployment. Each severity has its own paging and escalation route, and a response metrics dashboard tracks time to triage, contain, and recover.

**NIST Control Mapping:**

- **IR-4 (partial):** the control's final clause, that handling rigor be comparable and predictable across organizational elements, through a severity model applied uniformly. The other partial slices are held by Endpoint Response, Incident Response Development, and Incident-Scoped Log Analysis and Investigation.
- **Declined:** SI-4(12) is already held by Production Abuse Monitoring and the Detection focus area's SIEM Capabilities. IR-6(1) stays with Automated Notification Workflows, which this outcome routes over. IR-3(3) stays with Incident Response Plan Testing and Exercises, since exercise measures differ from live response performance.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Security Information and Event Management (SIEM) Platform, Self-Hosted Third-Party Application (COTS), AI/ML System

**External Dependencies:** None outside the boundary.

**Security Impact:** Low

**Activities:**

- **RS-2.5.1: Severity Scoring Model Definition**
    - **Description:** Define severity as an explicit function of the incident's assessed impact, the criticality of the assets it reaches, and the confidence that the detection is a true positive, fix the tier boundaries that function produces, and record the model, its thresholds, and its override path in the IRP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IR-4 (partial) mapping. Include confidence as an explicit term so the model separates a high-impact certainty from a high-impact guess. Name who may override a computed severity and require the reason on the record. Bind the top tier to the deadlines in Regulatory/AO Incident Reporting Workflow and Timelines, and take the criticality term from Asset Criticality and Business Impact Assessment.

- **RS-2.5.2: AI Incident Type Taxonomy and Severity Mapping**
    - **Description:** Enumerate the AI-specific incident types the program's fielded models can produce, such as adversarial or jailbroken output, data poisoning, prompt injection exploitation, model theft, inference manipulation, PII leakage via model output, adversarial concept drift, agentic scope violation, high-risk-action approval gate bypass, and unauthorized tool-call chaining, then map each to the severity model's tier boundaries, embed the taxonomy in the incident ticketing system so an AI-flagged record classifies consistently regardless of who is on shift, and document the taxonomy and severity mapping in the IRP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries a further instance of the outcome's IR-4 (partial) comparable-and-predictable clause, adding the incident-type term AI failure modes need. Populate each entry from the outcome that actually detects it, such as Data Poisoning Prevention and Detection, Extraction Abuse Monitoring, Model Drift Detection and Alerting, and Agentic AI Tool-Call and Action Logging (Application/API Logging). This activity maps each finding to a severity tier rather than re-detecting it.

- **RS-2.5.3: Automated Escalation Routing and Paging**
    - **Description:** Wire the computed severity tier to the escalation path it selects so a scored record pages the on-call rotation, the response lead, or program leadership without a person deciding each time, and re-escalate automatically when a tier's acknowledgment window passes unanswered.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is tagged Automate because it removes the human relay between a scored incident and the responder. It delivers over the channels Incident Notification Channel Configuration fields, so no IR-6(1) or SI-4(12) claim is opened. Test the path for every tier, and verify it again after any change to the on-call roster or paging vendor.

- **RS-2.5.4: Incident Response Metrics Dashboard**
    - **Description:** Build the view the security organization and program leadership read incident performance from, covering mean time to detect and to respond, open incidents by severity and by age, and adherence to the acknowledgment and reporting commitments each tier carries, and document which metrics are tracked and what each one measures in the IRP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is the capability's Visualize instance, rendering what the program did with incidents rather than the alert queue. Mean time to detect depends on the discovery timestamp captured by Automated Incident Ticket Creation from Correlated Detection Alerts. Show age of open incidents by severity, which exposes what averages hide. These measures feed the systemic lessons learned process and stay separate from the IR-3(3) exercise measures.

## RS-3: Incident Containment, Recovery, and Lessons Learned

### RS-3.1: SOAR Capabilities

**Design Intent:** Playbooks in the security monitoring platform run the program's decided responses as code and update the service desk record at each step. Actions that disrupt production need a Security Team approval inside the playbook. Fully automatic actions are limited to what Endpoint Response allows, namely isolating a host outside production. The CSSP may run the containment playbooks from its host pool, and each run pages the Security Team's on-call at once. The Security Team reviews or reverses each run by the next business day.

**NIST Control Mapping:**

- **IR-4(1) (partial):** program-wide orchestration across the endpoint, identity, network, cloud, and ticketing mechanisms at once. Endpoint Response's Automated Investigation and Response holds the single-agent slice, and the two are tracked jointly.
- **Declined:** no IR-4 base claim is opened, since orchestration executes the phases that other outcomes claim. IR-4(9) covers deploying new capabilities in response to an incident, which nothing here fields.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Identity Platform, Network Infrastructure, Device/Workstation, Security Information and Event Management (SIEM) Platform, Self-Hosted Third-Party Application (COTS)

**External Dependencies:** The CSSP, whose containment role its service agreement defines.

**Security Impact:** Moderate

**Activities:**

- **RS-3.1.1: SOAR Playbook Development and Automation Configuration**
    - **Description:** Encode the program's decided response to each incident type as an ordered sequence of enrichment, containment, and notification actions spanning the endpoint, identity, network, and cloud platforms, and version each playbook alongside the runbook it automates.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the core of the outcome's IR-4(1) (partial) mapping and is the capability's first Automate instance. Build each playbook against an existing runbook, scoped to incident types the environment actually produces. Exercise the set on the functional exercise cycle so API changes do not break it silently. It is Level 3 because responders executing procedures already meet the mandatory handling obligation.

- **RS-3.1.2: SOAR-to-SIEM/Ticketing Integration**
    - **Description:** Connect the orchestration platform to the SIEM it takes its triggers from and to the ticketing system of record it writes back to, so a playbook fires from a correlated alert and every action it took lands in the incident record as an auditable entry.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's IR-4(1) (partial) mapping by supplying the automation's trigger and its record. Do not defer write-back, since an automated containment nobody can reconstruct looks like an outage of unknown cause. Write to the record Automated Incident Creation and Enrichment raises rather than opening a second one.

- **RS-3.1.3: Automated Response Action Approval Workflow**
    - **Description:** Classify every automated response action by the disruption it can cause, let the low-impact ones execute unattended, route the rest to a named approver with the incident context, a decision deadline, and a recorded outcome before the action runs, and document the classification and approval workflow in the IRP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity sets the authorization boundary the outcome's IR-4(1) (partial) mapping depends on, deciding in advance which actions a machine may take unattended. Classify by asset class and consequence rather than by action type. Give every request a deadline and a documented default. Control-system approvals belong to the sibling Human-in-the-Loop Containment outcome.

### RS-3.2: Automated Containment and Isolation Procedures

**Design Intent:** Network containment moves a workload into a quarantine policy at the cloud hub, or into the SDN fabric's quarantine segment in the data center. Identity containment disables the account, revokes its sessions and tokens, and suspends any workload or AI agent identity. Both run from playbooks, and the Security Team approves before either touches production. The CSSP may run them on its own authority when an incident cannot wait for the Security Team. Neither the Security Team's playbooks nor the CSSP's may touch fleet systems.

**NIST Control Mapping:**

- **IR-4 (partial):** the containment phase, under this capability's convention of one phase per base slice. The other slices are held by Endpoint Response, Incident Response Development, Incident-Scoped Log Analysis and Investigation, and Automated Severity Scoring and Escalation.
- **IR-4(2) (full):** the only claim of the enhancement in the framework. Both activities dynamically reconfigure access control lists, firewall and gateway filters, and intrusion prevention parameters.
- **AC-2(3) (partial):** the policy-violation trigger applied to an account an incident has shown is compromised. Account Lifecycle and Identity Data Quality and Application and Service Account Identities hold the other triggers, and the three are tracked jointly.
- **AC-2(13) (full):** unheld elsewhere, disabling the accounts of individuals found to pose significant risk within a defined period. User/Entity Behavior Analytics (UEBA) / Insider Threat Detection supplies the discovery.
- **Declined:** IR-4(5) automatically disables the system itself and stays with Endpoint Response's Device Isolation, while reconfiguring enforcement points around a running system is IR-4(2). AC-12 stays with Continuous Authentication, since this outcome revokes sessions administratively. SC-7 and its enhancements belong to the Network and Environment focus area, whose boundaries this outcome operates.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Segmentation Policy, Network Firewall, Network Access Control (NAC), DNS Infrastructure, Identity Lifecycle and Governance, Human Authentication, Privileged Access Management, Compute, Device/Workstation, Application/API

**External Dependencies:** The CSSP, whose containment role its service agreement defines.

**Security Impact:** High

**Activities:**

- **RS-3.2.1: Network Isolation Automation**
    - **Description:** Implement the network-layer containment actions the program has authorized, namely moving a compromised host into a quarantine segment, revoking its cloud security group membership, and pushing block rules for adversary infrastructure to the firewall, network access control, and DNS enforcement points through their own APIs.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the whole of the outcome's IR-4(2) (full) mapping and part of its IR-4 (partial) containment slice, and is tagged Automate. Act at the switch, firewall, network access control system, and cloud security group, which reaches hosts no agent runs on. Keep management and telemetry paths open in the quarantine segment. Write the reversal path alongside each action.

- **RS-3.2.2: Account and Access Control Automation**
    - **Description:** Disable an account that an incident has established as compromised or whose holder it has identified as a significant risk, revoke its active sessions and refresh tokens, force reauthentication, strip the privileged role assignments an adversary would otherwise retain, and define the reinstatement path each of those actions is reversed through.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-2(3) (partial) and AC-2(13) (full) mappings and the remainder of its IR-4 (partial) and IR-4(2) (full) coverage, and is tagged Automate. Revoke live sessions and refresh tokens along with disabling the account, and strip privileged role assignments too. Define a reinstatement path with an owner.

### RS-3.3: Human-in-the-Loop Containment

**Design Intent:** No containment action may touch a ground control station, the launch and recovery equipment, or a datalink while an aircraft under that station's control is airborne. Such actions wait until Fleet Operations' operations lead approves them or the aircraft has landed. Cutting the ground segment conduit is pre-approved, since it carries only file transfers and cannot affect a flight. The manual runbook covers safe recovery of airborne aircraft, either by handing them to another station or recovering them, before a station is isolated.

**NIST Control Mapping:**

- **IR-4(3) (full):** the only claim of the enhancement in the framework. The classification identifies incident classes, the routing sets who authorizes each action, and the runbook supplies the predefined action, such as fallback to manual mode. Endpoint Response defers containment of non-agentable OT and legacy assets to this path.
- **Declined:** no IR-4 base slice is opened, since Automated Containment and Isolation Procedures holds the containment phase and IR-4(3) fits this scope more precisely. Safety engineering is a systems-engineering discipline outside the SABER's scope.

**Deployment Type:** On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Industrial Controller/SCADA, OT/ICS Zone-Conduit Segmentation (IEC 62443)

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **RS-3.3.1: OT/Safety-Critical Asset Containment-Action Risk Classification**
    - **Description:** Rate every available containment action against each class of safety-critical and process-control asset by the physical and mission consequence of taking it, and record in the IRP which actions may execute unattended, which require an operations approval, and which are prohibited outright.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the identification half of the outcome's IR-4(3) (full) mapping. Perform it with the engineering and operations organizations, who know what de-energizing a segment does. State the prohibited category explicitly, and treat any asset whose classification cannot be established as requiring approval by default.

- **RS-3.3.2: Human Approval Workflow Routing to OT/Plant Operations Personnel**
    - **Description:** Route every containment action the classification marks as requiring approval to the control room or operations authority on shift, carrying the incident context and the specific action requested, and hold the action until that authority answers or the fallback the IRP records applies.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the authorization half of the outcome's IR-4(3) (full) mapping. It routes to whoever holds the process at that moment, a shift role, rather than to the response team's own authority. Deliver requests over a path the control room actually watches. Record in the IRP what happens when no authority answers inside the window.

- **RS-3.3.3: Pre-Approved Manual Containment Runbook**
    - **Description:** Write, for each asset type in the process segment, the manual isolation procedure operations has already agreed to, naming the step sequence, the safe process state each step requires, and the fallback-to-manual-control mode the segment runs in while the isolation holds.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the predefined-action core of the outcome's IR-4(3) (full) mapping, describing fallback-to-manual and orderly degradation for the program's own equipment. Get operations to pre-approve each procedure during planning, not during the incident. Rehearse the set only in the discussion or simulator form Functional Incident Response Exercise Execution reserves for control-system segments. It is Documentation because the deliverable is the countersigned procedure.

### RS-3.4: Eradication and Threat Removal

**Design Intent:** Eradication removes the adversary's persistence, rotates every credential and secret the incident touched, and verifies the exploited weakness is closed before the incident can close. A compromised model version is withdrawn, and the registry blocks any rollback to it. A compromised station or aircraft has its datalink keys replaced.

**NIST Control Mapping:**

- **IR-4 (partial):** the eradication phase under this capability's per-phase convention, disjoint from the containment slice Automated Containment and Isolation Procedures holds.
- **IA-5 (partial):** the event-triggered clause, resetting authenticators after a confirmed compromise. Credential Management and Secrets and Credentials Protection hold the other slices, and the base is cited because no enhancement covers a reset across every authenticator class.
- **Declined:** SI-3 is held by the Device and Infrastructure, Application, and Artificial Intelligence focus areas' scanning mechanisms, which this outcome invokes. SI-2 and RA-5 stay with Vulnerability and Patch Management, the same boundary behind declining IR-6(2).

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Device/Workstation, Application/API, Artifact/Model Registry, Secrets Vault, Identity Platform, Network Infrastructure, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **RS-3.4.1: Malware/Attacker-Artifact Removal and Persistence Eradication**
    - **Description:** Remove from every affected system the adversary's implants, dropped artifacts, and persistence footholds, covering scheduled tasks, services, startup entries, container images, serverless function code, and the identity-side persistence of malicious application registrations and consent grants.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the core of the outcome's IR-4 (partial) eradication slice. Hunt for every persistence mechanism, including identity-side footholds such as a malicious application registration, a consented OAuth grant, or an added federation trust. Rebuild from a known-good image on stated criteria where the compromise reached the operating system's trust boundary. On a control-system device, the equivalent is a vendor-supported reflash in a maintenance window.

- **RS-3.4.2: Post-Compromise Credential and Secret Reset/Rotation**
    - **Description:** Determine from the incident's established scope every credential, token, key, and secret the adversary could have reached, force the reset or rotation of each through the mechanisms the Identity focus area already fields, and verify that no consumer of a rotated secret is still presenting the old one.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5 (partial) mapping and part of its IR-4 (partial) eradication slice. It executes through Secrets and Credentials Protection, Credential Management, and Key Lifecycle Automation, defining only the blast radius, ordering, and verification. Scope by what the adversary could have reached rather than what they were seen using. Order rotation of chained secrets so consumers are updated before the vault credential changes.

- **RS-3.4.3: Exploited-Vulnerability Closure Verification**
    - **Description:** Identify the vulnerability, misconfiguration, or exposed service the intrusion entered through, drive its remediation to closure on every instance in the environment rather than on the compromised host alone, and verify by rescan or test before the affected systems return to service.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's IR-4 (partial) eradication slice. Drive closure across every host the initial access vector exists on, not just the compromised one. Verify by rescan or test rather than by a completed change record. Where no fix exists, record the compensating control against the incident and carry it into the Vulnerability and Patch Management backlog.

### RS-3.5: Classified Data Spillage Response

**Design Intent:** The likeliest spill is classified content arriving through a high-to-low product, or pasted into a language model prompt, which the content filters are tuned to catch. The ISSM traces every copy, including index entries, embeddings, model training snapshots, and backups. The ISSM then suspends access to them and has each one sanitized. The ISSM reports the spill to the AO, the PSO, and the IL6 enclave's owner.

**NIST Control Mapping:**

- **IR-9 (full):** the only claim of the control in the framework, reserved here by Incident Reporting and External Communications. The four activities carry its clauses in turn: identification, isolation, eradication, and responsibility assignment with out-of-band alerting.
- **IR-9(3) (full):** keeping personnel impacted by a spill working while contaminated systems are corrected, through the clean replacements the sanitization activity names.
- **IR-9(4) (partial):** the system-side half, suspending the accounts and access paths that reached the spilled information. The personnel-security half, debriefing and adjudication, is held by the PSO outside the SABER's scope.
- **Declined:** IR-9(1) is withdrawn in Rev 5 and folded into the base. IR-9(2) training would extend Develop Team Training under IR-2 if the AO tailors it in. MP-6 and MP-6(1) stay with Resource Decommissioning Governance and Media Protection Policy and Procedures, which execute any destruction of contaminated media.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Object/File Storage, Backup/Archive Repository, Virtual Machine/Server, Identity Lifecycle and Governance, Segmentation Policy, Cross-Domain/Boundary Transfer

**External Dependencies:** The IL6 enclave's owner, whose release review and security office join any spill traced to a high-to-low product. The PSO, who receives every spill report.

**Security Impact:** High

**Activities:**

- **RS-3.5.1: Spillage Identification and Scope Determination**
    - **Description:** Establish exactly what classified information was introduced, at what classification and under what caveats, and trace every system, mailbox, share, backup, index, and endpoint cache it reached after it arrived.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the identification clauses of the outcome's IR-9 (full) mapping. Trace derived copies, such as search index snippets, later backups, replicas, endpoint caches, and forwarded mail, since each needs its own sanitization. The original classification authority determines the actual classification, and scoping proceeds on the conservative assumption meanwhile. Search using the Data focus area's labeling and classification.

- **RS-3.5.2: Spillage Containment and Access Suspension**
    - **Description:** Isolate every contaminated system and component from further replication, suspend the accounts and access paths that reached the spilled information, and hold both in place until the PSO and the AO authorize release.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the isolation clause of the outcome's IR-9 (full) mapping and the whole of its IR-9(4) (partial) mapping. Stop replication first, including backup jobs, replication targets, and synchronization clients. Suspend rather than delete accounts and mailboxes, preserving the exposure record the PSO needs. Only the PSO and the AO release a suspended system or account.

- **RS-3.5.3: Contaminated Media and System Sanitization**
    - **Description:** Sanitize or destroy every contaminated system, volume, and piece of media by the method the spilled information's classification requires, verify and record each action, and stand up the clean replacements affected personnel keep working from while the corrective action runs.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the eradication clause of the outcome's IR-9 (full) mapping and the whole of its IR-9(3) (full) mapping through clean replacement hardware. Choose the method from the classification and media type together, and expect destruction for high-classification information on flash-backed media. Verify and record every action. Replacement hardware and media destruction drive the one-time cost.

- **RS-3.5.4: Spillage Reporting and Authority Notification**
    - **Description:** Report the spill to the PSO, the ISSM, the AO, and the original classification authority inside the deadline each imposes, using a communication path that does not traverse the contaminated systems, and record in the IRP the roles accountable for spill response and the notification path each uses.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the responsibility-assignment and alerting clauses of the outcome's IR-9 (full) mapping. Report over an out-of-band path, never over the system holding the spill. Spill reporting runs to the PSO and the original classification authority, separate from the IR-6 workflow, and the IRP records both side by side. Name the accountable roles by position.

### RS-3.6: Recovery and Return-to-Operations Validation

**Design Intent:** Restoration uses only backups, images, and model versions from before the earliest confirmed adversary activity, and each source is checked for the incident's indicators before it is used. A recovered system stays under heightened monitoring for 30 days.

**NIST Control Mapping:**

- **IR-4 (partial):** the recovery phase of the first clause and the whole of the second, coordinating incident handling with contingency planning through a verification gate before restoration. The other partial slices are held by its siblings and the earlier capabilities.
- **SI-4 (partial):** the clause requiring monitoring levels to change with risk, which no surface-scoped SI-4 slice covers. The other slices are held across both pillars by monitoring surface.
- **Declined:** CP-2, CP-10, and the rest of the CP family stay with the Recovery focus area, which performs restoration once this outcome approves it. IR-3(2) stays with Incident Preparation, since it covers exercise coordination.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Identity Platform, Network Infrastructure, Device/Workstation, Application/API, Backup/Archive Repository, Security Information and Event Management (SIEM) Platform, Industrial Controller/SCADA

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RS-3.6.1: Pre-Restoration Clean-State Verification**
    - **Description:** Verify before any restoration begins that the backup, image, or rebuild source predates the earliest confirmed adversary activity and carries none of the artifacts the eradication step removed, and gate the Recovery focus area's restoration on that verification rather than letting the two run in parallel.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the coordination clause of the outcome's IR-4 (partial) mapping. Compare restoration sources against the earliest confirmed adversary activity date. Raise a backup retention depth beyond plausible dwell time against the Recovery focus area's backup coverage. Where no clean source exists, settle in advance on rebuilding from a golden image with selective data restoration.

- **RS-3.6.2: Post-Incident Heightened Monitoring**
    - **Description:** Raise the monitoring level on the recovered systems, accounts, and network paths for a defined period after return to service, watching specifically for the indicators this incident produced, and return the level to baseline on a decision recorded against the incident record rather than by drift.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4 (partial) mapping and the recovery-phase portion of its IR-4 (partial) mapping. Promote this incident's indicators to alerting for a stated period, handing durable ones to Indicator of Compromise (IOC) Feed Management. Record the decision to stand down against the incident record. Reinfection inside the window reopens the original incident.

### RS-3.7: Systemic Lessons Learned Process

**Design Intent:** Every high-severity incident and every exercise ends with a lessons-learned review. It produces findings against the detection that missed, the procedure that failed, or the design weakness behind the incident. Each finding becomes a tracked item, and design findings go to the PMO ISSE.

**NIST Control Mapping:**

- **IR-4 (partial):** the third clause, incorporating lessons learned into procedures, training, and testing and implementing the changes. The rest of IR-4 sits with the seven other slices.
- **Declined:** IR-3(3) stays with Incident Response Plan Testing and Exercises, since this loop runs over real incidents and both feed the IRP separately. CA-5 stays partial with STIG Risk Tracking, and a finding that proves to be a control deficiency is entered there.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Security Information and Event Management (SIEM) Platform, Self-Hosted Third-Party Application (COTS)

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **RS-3.7.1: Lessons Learned Framework**
    - **Description:** Define the review that follows an incident, naming which severity tiers trigger one, how soon it convenes, who attends, and the blameless format it runs in, require each review to produce findings against the detection, the procedure, and the architecture rather than against the responders, and document the review framework in the IRP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the incorporation half of the outcome's IR-4 (partial) mapping. Set the review threshold low enough to learn from more than catastrophes, and convene within a set interval. Use a blameless format so responders report runbook defects. Include the performer engineers who own the affected system, keyed to the tiers in Severity Scoring Model Definition.

- **RS-3.7.2: Improvement Implementation Tracking**
    - **Description:** Record every lessons-learned finding as an owned, dated item against the specific runbook, playbook, detection rule, control, or IRP section it changes, drive it to closure on the program's normal work-tracking path, and report closure rate and item age alongside the response measures the preceding capability publishes.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the implement-the-resulting-changes half of the outcome's IR-4 (partial) mapping. Route items onto the engineering organization's own backlog rather than a security-only list. Report closure rate and age into the Incident Response Metrics Dashboard alongside response performance.

## RS-4: Incident Response Planning

### RS-4.1: Incident Response Plan (IRP)

**Design Intent:** The ISSM authors KESTREL's IRP. Fleet Operations writes the OT containment rules, the ML team writes the AI runbooks, and the CSSP confirms the responsibility split. The Configuration Control Board approves the IRP, and it is revised each year and after every exercise or major incident that changes it.

**NIST Control Mapping:**

- **IR-1 (partial):** the incident-response-specific procedures slice. The Manage pillar's Security Policy Framework holds the family-level policy, and IR-1 has no enhancements in SP 800-53 Rev 5.
- **IR-8 (full):** claimed full because IR-8's subject is the plan itself, and the three activities cover IR-8a through IR-8d. The plan elements are drawn from determinations the focus area's other capabilities reached, such as Organize Team Structure and Severity Scoring Model Definition.
- **Declined:** IR-8's one enhancement, IR-8(1), covers breaches of personally identifiable information, which is an AO tailoring decision rather than an assumed element. The IR-7 base is held in full by Cyber Defense Service Provider Alignment.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Identity Platform, Network Infrastructure, Device/Workstation, Application/API, OT/ICS Device, AI/ML System

**External Dependencies:** The CSSP, under the detection and response split in its service agreement.

**Security Impact:** Moderate

**Activities:**

- **RS-4.1.1: IRP Development and Authoring**
    - **Description:** Author the incident response plan, consolidating the team structure and authorities, handling and reporting procedures, reportable-incident definitions, criticality and severity models, evidence and retention terms, OT containment rules, and response measures produced across the focus area's other three capabilities into a single governing document, and mark and store it at the classification and access restriction its content requires.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the plan-development clause of the outcome's IR-8 (full) mapping together with its protection clause, IR-8d. Mark, store, and restrict the plan, since it would help an adversary who obtained it. Author it after the determinations it consolidates exist. IRP Periodic Review and Revision keeps it current afterward.

- **RS-4.1.2: IRP Review and Approval**
    - **Description:** Route the drafted IRP through stakeholder review, secure formal approval from the accountable authority, and distribute the approved plan to the response personnel and organizational elements it names.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries IR-8a.9 and IR-8b of the outcome's mapping. Distribute the approved plan to the people who must use it. Approval fixes the approving roles and the frequency IRP Periodic Review and Revision runs on.

- **RS-4.1.3: IRP Periodic Review and Revision**
    - **Description:** Review the IRP on the cadence its approval fixed and revise it to reflect changes in the response team, the program's reporting obligations, the criticality and severity models, the systems it covers, or problems encountered during an incident, an exercise, or the plan's own execution.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries IR-8c of the outcome's mapping and supersedes the One-Time issuance produced by IRP Development and Authoring. Treat the annual cadence as a floor, and absorb items from Exercise Findings and Plan Update Tracking and Improvement Implementation Tracking as they arrive. A change to team membership or a reporting deadline also triggers revision.
