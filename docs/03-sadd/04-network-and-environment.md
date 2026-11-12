# NE: Network and Environment

*KESTREL SADD, Section 5 (Protect). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## NE-1: Network Management and Segmentation

### NE-1.1: Network Centralization and Standardization

**Design Intent:** Both hubs and the SDN controller take their rules and routes from one rule base, defined once as policy as code in the Platform Team's repository and deployed to each side by the pipeline. A rule change is a pull request with a second reviewer, and changes to the shared rule base go to the Configuration Control Board. The pipeline compares each hub's running policy with the repository and alerts on any difference.

**NIST Control Mapping:**

- **CM-2 (partial):** an independent slice scoped to network infrastructure. Firewall Standardization and Routing Management documents the approved firewall and routing baseline, and Centralized Policy Enforcement applies it centrally. Baseline Configuration Standards holds CM-2 for the compute, storage, and platform-service asset classes.
- **CM-3 (partial):** carried by Network Resource Configuration Governance, which approves changes to network resource configuration. Asset Lifecycle Change Control holds the compute, storage, and platform-service scope, and both defer standing oversight to the Manage pillar's Configuration Control Board.
- **CM-6(1) (partial):** carried by Firewall/Routing Configuration Drift Detection and Alerting, which automatically scans live firewall and routing configuration against the documented baseline. The compute, storage, platform-service, and end-user-device slices belong to other outcomes.
- **Declined:** SI-4 is not claimed because network telemetry collection and the posture dashboard belong to Network Telemetry and Security Posture Visualization.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Routing/Switching Fabric, Network Firewall

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **NE-1.1.1: Centralized Policy Enforcement**
    - **Description:** Stand up and operate the central control point that applies firewall, routing, and segmentation policy uniformly across the network estate from a single management plane rather than through per-device configuration.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the central apply-and-maintain dimension of the outcome's CM-2 (partial) mapping for network infrastructure. It enforces the baseline Firewall Standardization and Routing Management defines. It is a standing platform rather than a pipeline scan or gate, so it is not tagged Automate.

- **NE-1.1.2: Firewall Standardization and Routing Management**
    - **Description:** Define the approved firewall ruleset and routing configuration baseline that network devices must conform to as the network-infrastructure standard the enforcement and drift-detection layers measure against, and document the baseline in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the define-and-document dimension of the outcome's CM-2 (partial) mapping. It is Documentation because its output is the recorded standard that Centralized Policy Enforcement applies and Firewall/Routing Configuration Drift Detection and Alerting verifies. It is event-driven, revised when the approved configuration changes.

- **NE-1.1.3: Network Resource Configuration Governance**
    - **Description:** Establish the governance process that routes every change to network resource configuration through documented review and approval before it is applied, and document the process in the CMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-3 (partial) claim, scoped to network resource configuration, and documents its process in the CMP. It is event-driven because approvals happen per change request. It is also the change-control gate for network device patches, which Vulnerability and Patch Management relies on for its SI-2 (partial) claim, though remediation SLAs stay with that outcome.

- **NE-1.1.4: Firewall/Routing Configuration Drift Detection and Alerting**
    - **Description:** Continuously scan live firewall and routing configuration against the documented approved baseline and raise an alert whenever a network device's configuration has drifted from that baseline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the verify dimension of the outcome's CM-6(1) (partial) mapping for network infrastructure. It is tagged Automate because tool-driven scanning replaces manual device-by-device inspection. Its drift results surface on the Network Security Posture Dashboard, and it checks against the baseline Firewall Standardization and Routing Management maintains.

### NE-1.2: Network Infrastructure Device Hardening

**Design Intent:** Hardening baselines come from the DISA STIGs for the SDN switches and controller, both hubs' firewalls, the alternate site firewall, and the ground segment network's switches. Management interfaces sit only on the out-of-band network and accept only administrators coming through the privileged access platform. The cloud and data center run dual-stack, with every hub rule written for both address families. The ground segment stays IPv4 only and drops IPv6 at its conduit.

**NIST Control Mapping:**

- **CM-6 (partial):** claimed at the base for the configuration of the network device itself, which Network Device Hardening Baseline Definition documents and the two implementation activities apply. Other CM-6 claims cover other asset classes, such as Baseboard Management Controller (BMC) Hardening. The base is cited because switches and routers are configured through their own management interfaces rather than the automated pipeline CM-6(1) describes.
- **Declined:** CM-7 is not claimed, since Insecure Services and Protocols holds CM-7(1) for disabling nonsecure protocols and the Ports, Protocols, and Services Matrix (PPSM) holds CM-7(3).

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Routing/Switching Fabric, Wireless/RF Infrastructure, Load Balancer/Reverse Proxy/API Gateway

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider hardens the network devices beneath the cloud hub and the managed load balancers in the DMZ.

**Security Impact:** High

**Activities:**

- **NE-1.2.1: Network Device Hardening Baseline Definition**
    - **Description:** Derive a documented hardening baseline for each network device class from the benchmark and STIG content Device and Infrastructure's Configuration Frameworks activity already adopts, and record each baseline together with its approved deviations in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the establish-and-document dimension of the outcome's CM-6 (partial) mapping. It reuses the framework selection from Configuration Frameworks and extends it to routers, switches, wireless controllers, and load balancers. It is Documentation, and event-driven because baselines are reissued as benchmark and STIG releases land.

- **NE-1.2.2: Device Management Plane Hardening**
    - **Description:** Apply the hardened baseline to each device's management plane by binding administrative authentication to the program's central authentication service, restricting management reachability to the out-of-band network and its authorized source addresses, enforcing SNMPv3 and encrypted administrative transport, authenticating interior routing-protocol adjacencies, and setting idle-session timeouts.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the implement dimension of the outcome's CM-6 (partial) mapping for who can administer a device and over what path. Its reachability restriction depends on Out-of-Band Management Network Isolation, so build the two together. Interior routing adjacency authentication is treated as a device setting here, since Routing Protocol and Control Plane Protection holds the external control plane under SC-7(4).

- **NE-1.2.3: IPv6 and Dual-Stack Disposition**
    - **Description:** Decide for each network segment whether IPv6 is enabled or disabled, switch the address family off wherever the mission does not require it, extend the program's filtering, logging, and first-hop protections to IPv6 at parity with IPv4 wherever it is enabled, and record the disposition in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the implement dimension of the outcome's CM-6 (partial) mapping for the address-family setting. Most devices enable IPv6 by default, so a program writing only IPv4 rules often runs an unfiltered second address family. Where IPv6 is enabled, first-hop protections, boundary rules, and flow logging must reach it, and IPv6-in-IPv4 tunneling stays blocked unless registered in the PPSM baseline.

### NE-1.3: Insecure Services and Protocols

**Design Intent:** Flow telemetry from both hubs and the SDN fabric is checked for cleartext and obsolete protocols, such as Telnet, FTP, SMBv1, unsigned LDAP, and TLS below 1.2. Each one found is disabled. The payload processing workstation stays connected past its replacement date only if the AO re-dates CCSD tailoring action 3. If its operating system then cannot negotiate current TLS, its transfer to the data lake is the one registered exception, confined to its single conduit.

**NIST Control Mapping:**

- **CM-7(1) (partial):** Insecure Protocol Discovery reviews for nonsecure protocols from the network side, and Insecure Services and Protocols Disabling disables or removes them. The enhancement fits the identify-and-disable work better than the CM-7 base. Unapproved Service Usage Monitoring and Alerting holds the host-side slice, and Runtime API Inventory and Governance and others hold the rest.
- **Declined:** the CM-7 base stays with the Device and Infrastructure outcomes, such as Policy Service Restrictions, whose policy this outcome enforces. SI-4(22) stays with Ports, Protocols, and Services Matrix (PPSM), which finds unauthorized services rather than insecure ones. SC-8 belongs to the Data focus area's encryption outcomes. RA-7 is not claimed, since retained protocols use the existing risk-acceptance workflow.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Network Infrastructure, Compute, Device/Workstation, OT/ICS Device, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **NE-1.3.1: Insecure Protocol Discovery**
    - **Description:** Locate every place a cleartext or cryptographically obsolete protocol is still in use by analyzing the program's network telemetry and running targeted scans across the estate, and record each finding with its endpoints, its owning system, and the secure protocol that should replace it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the review-and-identify dimension of the outcome's CM-7(1) (partial) mapping. It works from the network, so devices no host agent can reach are still caught by the protocols they speak. It uses the Centralized Network Telemetry and Analytics Platform rather than new collection, and it scans OT segments passively only.

- **NE-1.3.2: Insecure Services and Protocols Disabling**
    - **Description:** Turn off each discovered insecure service and protocol in the host, service, and network-device configuration once its traffic has been moved onto the secure replacement, and confirm by re-scan that the protocol no longer answers anywhere it was found.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the disable-or-remove dimension of the outcome's CM-7(1) (partial) mapping. Its applicability is narrower than the outcome's Deployment Type, since OT equipment that cannot turn off an insecure protocol passes to Compensating Controls Implementation. It is event-driven because retirements proceed per finding with each system owner.

- **NE-1.3.3: Compensating Controls Implementation**
    - **Description:** Constrain each insecure protocol that a legacy system cannot be moved off to a dedicated segment and its named peers, carry it inside an encrypted tunnel wherever the endpoints permit one, raise monitoring on it, and register the retained protocol as a bounded, approved exception in the PPSM baseline.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it inherits AC-4 and SC-7(5) enforcement from Network Micro Segmentation and transmission protection from the Data focus area's encryption outcomes. Register each retained insecure protocol in the existing PPSM baseline, so the recertification cycle keeps it visible.

### NE-1.4: Network Macro Segmentation

**Design Intent:** The macro segments are the cloud's ten spokes, the data center's SDN segments, and the ground segment's OT zone. The data center's segments match the cloud's teams, with one segment per mission team's data lake zone. The DMZ, the VDI spoke, and Tier 0 are the high-risk classes, each isolated in its own segment. The data center's BMCs, SDN controller management, and HSM management sit on an out-of-band network reachable only from the privileged access workstations.

**NIST Control Mapping:**

- **SC-7 (partial):** claimed at the base because Network Topology Design and Subnet Allocation and Segmentation Plan establish the overall boundary architecture before any enhancement's mechanism applies. The other SC-7 claims in this focus area, such as Network Micro Segmentation's, hold the enhancement level.
- **SC-7(13) (partial):** carried by Out-of-Band Management Network Isolation, which places management and support components on a physically separate subnetwork with a managed interface. It is partial because the enhancement also reaches defensive-analysis and forensics infrastructure, which the Operate pillar sites unless the program hosts it locally.
- **SC-7(21) (partial):** claimed for High-Risk Workload Isolation, which separates mission-differentiated workload classes into distinct subnetworks. Micro-segmentation isolates through flow rules instead, so it maps to AC-4 and SC-7(5). IT/OT Zone and Conduit Segmentation (IEC 62443) and Secrets Vault Network Security Hardening hold other independent slices.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Segmentation Policy, Compute

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **NE-1.4.1: Network Topology Design**
    - **Description:** Design the program's overall segmented network topology, defining the macro-level boundaries and managed interfaces that separate broad system classes, and record it as the architecture the subnet allocation and downstream micro-segmentation build within.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the design dimension of the outcome's SC-7 (partial) mapping. It produces the macro architecture that the other activities build on. It is event-driven, revised when the network architecture changes.

- **NE-1.4.2: High-Risk Workload Isolation**
    - **Description:** Isolate high-risk workload classes, such as internet-facing services, administrative planes, and sensitive data stores, into their own macro boundary so they cannot be reached from lower-trust segments except through an enforced managed interface.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7(21) (partial) mapping. Separating a high-risk workload class into its own distinct subnetwork matches the enhancement more precisely than SC-7's general intent. It is event-driven as high-risk classes are identified.

- **NE-1.4.3: Subnet Allocation and Segmentation Plan**
    - **Description:** Allocate the subnets and network segments that realize the topology design, and document the allocation scheme and its segment-to-boundary assignments in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the define-and-document dimension of the outcome's SC-7 (partial) mapping. Document the allocation in the CMP alongside the network configuration baseline rather than a new plan. It is Documentation and event-driven, updated when the topology changes.

- **NE-1.4.4: Out-of-Band Management Network Isolation**
    - **Description:** Build a dedicated management network that carries device administration, console, and infrastructure-monitoring traffic on paths physically separate from the production data planes, reachable only through a managed interface with its own authentication and authorization and with no route to any production segment.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7(13) (partial) mapping. It keeps an adversary on a production segment from reaching the control surface of the devices enforcing it. Build it alongside Device Management Plane Hardening, and use Secure Remote Access to broker access across its managed interface. In cloud, the equivalent is a dedicated management virtual network with no peering to workload spokes.

### NE-1.5: Network Micro Segmentation

**Design Intent:** Each team maps the flows its workloads need, and those flows become allow rules on workload security groups, with everything else denied. Inside each cluster, Kubernetes network policies deny traffic between namespaces by default. Flow logs feed the security monitoring platform, which flags rules nothing has used for 90 days. The penetration testers try to cross the vendor split and the dev/test to prod deny at every engagement.

**NIST Control Mapping:**

- **AC-4 (partial):** Communication Requirements Mapping defines the approved workload flows, and Allow and Deny Rules enforce them. The base is cited because general flow enforcement fits better than any narrower enhancement. IT/OT Zone and Conduit Segmentation holds the OT conduit slice.
- **SC-7(5) (partial):** claimed for Allow and Deny Rules, whose deny-by-default, allow-by-exception posture is exactly this enhancement. IT/OT Zone and Conduit Segmentation holds the OT conduit slice.
- **Declined:** SC-7(21) belongs to High-Risk Workload Isolation, while micro-segmentation isolates through AC-4 and SC-7(5). CM-6(1) stays with Firewall/Routing Configuration Drift Detection and Alerting. CA-8 is held by the Application focus area's Penetration Testing outcome. Security grouping is a construct rather than a control, and flow-log monitoring uses the existing SI-4 telemetry platform.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Segmentation Policy, Application/API

**External Dependencies:** The penetration testing provider, which tests segmentation and exfiltration paths under each engagement's rules of engagement.

**Security Impact:** Moderate

**Activities:**

- **NE-1.5.1: Communication Requirements Mapping**
    - **Description:** Map the workload-to-workload and application-to-application communication each system legitimately requires as the approved-flow baseline the allow and deny rules are derived from, and document the baseline in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the define dimension of the outcome's AC-4 (partial) mapping. It is Documentation because its output is the approved-flow baseline that Allow and Deny Rules enforce. It is event-driven, revised as applications and their dependencies change.

- **NE-1.5.2: Allow and Deny Rules**
    - **Description:** Express the approved communication baseline as allow and deny rules applied at workload granularity with a default-deny posture, permitting only the flows the mapping authorized and denying all others.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the enforcement dimension of the outcome's AC-4 (partial) mapping and its SC-7(5) (partial) claim. It enforces the approved flows from a deny-by-default posture, using the groups Workload/Application-Based Security Grouping provides. It is standing enforcement, so it is not tagged Automate.

- **NE-1.5.3: Workload/Application-Based Security Grouping**
    - **Description:** Group workloads and applications into security groups by role, sensitivity, or application tier so the allow and deny rules can be written against stable group identities rather than individual addresses.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it is the grouping construct the Allow and Deny Rules are written against. It is Level 2 because it improves the manageability of mandatory enforcement rather than meeting it. It is event-driven as workloads are added or reclassified.

- **NE-1.5.4: Flow Logs Monitoring and Optimization**
    - **Description:** Monitor the segmentation flow logs to confirm traffic conforms to the allow and deny model and to identify unused or over-permissive rules, feeding rule tightening back into the ruleset.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it uses the existing Centralized Network Telemetry and Analytics Platform. Its analysis surfaces unused or over-permissive rules to refine the AC-4 ruleset. It is tagged Automate and sits at Level 2, tightening mandatory enforcement rather than meeting it.

- **NE-1.5.5: Security Group and Firewall Rule Drift Detection**
    - **Description:** Compare the security group, network security group, and host-level firewall rules deployed across the estate against the approved-flow baseline on a continuous automated cycle, and alert on any rule that permits a flow the baseline does not authorize or that has been widened beyond the peers and ports it was approved for.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it verifies the approved-flow baseline rather than opening a second CM-6(1) claim. A security group can match the device baseline and still permit a flow no one approved, which is why this check exists. It is tagged Automate and sits at Level 2, keeping enforcement from eroding.

- **NE-1.5.6: Segmentation Enforcement Validation and Exfiltration Testing**
    - **Description:** Test on a recurring cycle that the segmentation actually enforces as designed by attempting lateral movement between segments that should not reach one another and simulated data egress along paths the boundary should refuse, and drive every boundary that does not hold into remediation.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it validates the AC-4 and SC-7(5) enforcement and the macro boundaries. CA-8 stays with the Application focus area's Penetration Testing outcome, so this is a repeatable confirmation that named segments stay unreachable. Record findings as rule and topology defects. It is Process at Level 2 and is not tagged Automate.

### NE-1.6: IT/OT Zone and Conduit Segmentation (IEC 62443)

**Design Intent:** The ground segment has four zones, namely aircraft and datalinks, ground control stations, launch and recovery, and the payload processing workstation. The station and aircraft zones carry security level target 3, and the others carry 2. One conduit joins the ground segment to the data center through an IT/OT DMZ, where recordings and model packages are staged so that no session spans IT and OT. The passive sensors watch every zone-to-zone flow, and the penetration testers validate the zones on spares.

**NIST Control Mapping:**

- **SC-7 (partial):** claimed at the base for the zone-and-conduit architecture Zone and Conduit Model Definition establishes, alongside Network Macro Segmentation's IT claim. IT/OT Demilitarized Zone extends the same claim to the IT/OT interface.
- **SC-7(21) (partial):** grouping OT assets into criticality-differentiated zones is the isolation the enhancement describes. This is an independent OT-scoped claim, while High-Risk Workload Isolation holds the IT slice.
- **AC-4 (partial):** claimed for Conduit Access Control and Allow-Listing, which enforces approved zone-to-zone flows. Network Micro Segmentation holds the IT workload slice.
- **SC-7(5) (partial):** claimed for the same activity, since conduit allow-listing denies all unauthorized zone-to-zone traffic by default. IT/OT Demilitarized Zone extends it to the IT/OT interface, and Network Micro Segmentation holds the IT slice. IEC 62443 unifies isolation and flow control, which the framework splits across two outcomes for IT.
- **Declined:** SI-4 is not reopened for Zone-to-Zone Data Flow Monitoring, since its passive feed comes from OT/Legacy Passive Monitoring, which holds SI-4(13) and SI-4(5).

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** OT/ICS Device, OT/ICS Zone-Conduit Segmentation (IEC 62443)

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **NE-1.6.1: Zone and Conduit Model Definition**
    - **Description:** Group the program's OT and legacy assets into criticality-based security zones, define the conduits that carry the authorized communication between those zones, and document the resulting zone-and-conduit model in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7 (partial) base claim and its SC-7(21) (partial) claim for criticality-based zone isolation. Document it in the CMP alongside the network segmentation records. It is Documentation, and event-driven as the OT architecture changes.

- **NE-1.6.2: Security Level Target (SL-T) Assignment**
    - **Description:** Assign each defined security zone its target security level following IEC 62443-3-2, derived from the consequence of a compromise in that zone and the threat the program expects it to withstand, and record each target alongside the zone's entry in the zone-and-conduit model.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since the target sizes the SC-7(21) isolation and SC-7(5) conduit posture its siblings claim. It draws on the Manage pillar's risk assessment and gives the reference the achieved security level is measured against. It is Documentation at Level 2.

- **NE-1.6.3: Conduit Access Control and Allow-Listing**
    - **Description:** Enforce allow-listed communication through each conduit so that only the explicitly authorized zone-to-zone flows are permitted and all other traffic between zones is denied by default.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-4 (partial) mapping, enforcing approved zone-to-zone flows through the conduits, and its SC-7(5) (partial) mapping, permitting them only by explicit exception. It is the OT counterpart of Allow and Deny Rules. It is standing, continuous enforcement, so it is not tagged Automate.

- **NE-1.6.4: IT/OT Demilitarized Zone**
    - **Description:** Stand up a dedicated demilitarized zone between the IT and OT estates that terminates every IT-to-OT and OT-to-IT conduit, hosts the data historian replicas, patch and update repositories, jump hosts, and protocol brokers both sides need to reach, and permits no flow from one estate into the other unless a component inside it brokers that flow.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the boundary-architecture dimension of the outcome's SC-7 (partial) base mapping and the deny-by-default dimension of its SC-7(5) (partial) mapping at the IT/OT interface. Every conduit terminates on a broker or replica in the demilitarized zone, so no session started on the IT side reaches a controller. Use Unidirectional Gateways where nothing may return, and this zone for bidirectional needs such as patching, historian queries, and engineering access.

- **NE-1.6.5: Zone-to-Zone Data Flow Monitoring**
    - **Description:** Passively observe the traffic traversing zone conduits to confirm it conforms to the allow-listed model and to surface anomalous or unauthorized zone-to-zone flows for operator investigation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since its passive feed comes from OT/Legacy Passive Monitoring rather than the active Centralized Network Telemetry and Analytics Platform. It is tagged Automate because tool-driven flow analysis against the allow-listed model replaces manual inspection. It is Level 2, tightening the enforcement Conduit Access Control and Allow-Listing provides.

- **NE-1.6.6: Zone Segmentation Enforcement Validation**
    - **Description:** Validate automatically that traffic cannot cross zone boundaries except through the authorized conduits by testing the enforced segmentation against the documented zone-and-conduit model, and flag any boundary that does not hold as designed.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it validates the SC-7, SC-7(21), AC-4, and SC-7(5) boundaries its siblings establish. It is tagged Automate because tool-driven segmentation testing replaces manual probing. It is Level 2, adding assurance that mandatory enforcement holds.

### NE-1.7: Network Access Control (NAC/802.1X)

**Design Intent:** Every wired port in the data center, at the alternate site, and at the operating sites requires 802.1X, with device certificates from the program PKI. Posture checks gate admission for the privileged access workstations and servers. Ground control stations and launch equipment that cannot run a supplicant are admitted by registered hardware address to their own zone only. A device that fails is quarantined, and the Security Team is alerted. Each operating site keeps admitting devices while it is cut off from the data center.

**NIST Control Mapping:**

- **IA-3 (partial):** 802.1X Port-Based Authentication Deployment authenticates a device before it connects, with posture criteria from NAC Device Compliance/Posture Policy Definition and a fallback in OT and Legacy Device Network Admission. The base is cited because the EAP method is not fixed, so IA-3(1) is not guaranteed. OT/Legacy Device Identity Controls holds the rest, and the two are tracked jointly.
- **SC-7(20) (partial):** claimed for Rogue Device Detection and Quarantine, which moves a device that fails authentication or posture checks into an isolated segment. That is the enhancement's dynamic isolation, and no other outcome claims it.
- **Declined:** IA-3(1) is held by OT/Legacy Device Identity Controls for gateway-proxied device authentication. The SC-7 base is already held elsewhere in this focus area. CM-8(3) gains no slice, since quarantine findings route into the existing discovery process as Unmanaged/Rogue Device Discovery does.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Device/Workstation, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **NE-1.7.1: 802.1X Port-Based Authentication Deployment**
    - **Description:** Deploy 802.1X port-based authentication across the wired network so that each device is uniquely identified and authenticated at the switch port before it is granted any network connectivity.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Extensive
    - **Cost:** One-Time: Extensive; Recurring: Moderate
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries the mechanism dimension of the outcome's IA-3 (partial) mapping, authenticating devices before they connect. Effort, cost, and timeline are rated at the top of each scale because a full wired rollout touches every switch port and every device behind one. Printers, cameras, and badge readers that cannot run a supplicant need individually justified and registered MAC authentication bypass exceptions.

- **NE-1.7.2: NAC Device Compliance/Posture Policy Definition**
    - **Description:** Define the device compliance and posture policy that the NAC admission decision applies alongside authentication, covering the patch level, endpoint-protection state, and configuration criteria a device must satisfy, and document it in the CMP as the admission standard the enforcement points are configured against.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the policy dimension of the outcome's IA-3 (partial) mapping, setting the posture criteria NAC admission applies on top of 802.1X. It is Documentation, while the NAC platform enforces the standard. It is event-driven as the compliance baseline changes.

- **NE-1.7.3: OT and Legacy Device Network Admission**
    - **Description:** Admit devices that cannot run an 802.1X supplicant through a registered fallback path that authorizes each port by its device's verified network-layer identity, places the admitted device directly into the zone its zone-and-conduit assignment gives it, and denies any port whose device does not match a registered profile.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the admission-decision dimension of the outcome's IA-3 (partial) mapping for devices 802.1X cannot reach. It takes identity verification from OT/Legacy Device Identity Controls and adds the port enforcement point. Since address-based admission is spoofable, bind each device to a specific port where the switch supports it, place it in a zone that assumes impersonation, and record it as a bounded exception. Effort is High because each profile is built by hand.

- **NE-1.7.4: Rogue Device Detection and Quarantine**
    - **Description:** Detect devices that fail 802.1X authentication or NAC posture checking at the admission layer and automatically quarantine them into a restricted or isolated segment until they are remediated or authorized.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7(20) (partial) mapping by isolating a device that fails authentication or posture at the moment of detection. It adds no CM-8(3) slice and routes findings into the existing discovery process, complementing Unmanaged/Rogue Device Discovery. It is tagged Automate and sits at Level 2, strengthening containment of admission failures.

### NE-1.8: Wireless Network Access Control

**Design Intent:** The command and payload datalinks are KESTREL's only authorized wireless. No wireless LAN exists in the data center or at the operating sites, and embedded radios are disabled on every server, workstation, and station. WPA2/3-Enterprise therefore has nothing to authenticate today. Wireless sensors at the data center and each operating site look for rogue access points and alert the Security Team.

**NIST Control Mapping:**

- **AC-18 (partial):** carried by Wireless Access Policy and Authorization, which sets configuration and connection requirements for each wireless type and authorizes it before use. That spans 802.11, point-to-point links, and embedded radios such as Bluetooth, which the enhancement's mechanism does not address. The other activities here hold the enhancements.
- **AC-18(1) (partial):** claimed for Wireless Network Authentication (WPA2/3-Enterprise), whose authentication and encryption are exactly the enhancement's mechanism. It is partial alongside the outcome's base and AC-18(3) claims.
- **AC-18(3) (partial):** claimed for the policy activity's rule that components without a wireless use case carry no enabled radio. It is partial because the asset-class baselines from Baseline Configuration Standards apply the actual disable.
- **SI-4(14) (full):** claimed for Rogue Access Point Detection, since the enhancement names a wireless intrusion detection system outright. No other outcome claims it, and no SI-4 base claim covers the radio-frequency environment.
- **Declined:** AC-18(4) is answered by the Identity focus area's privilege controls. AC-18(5) covers antenna siting and power, which belong to physical and facility security.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Wireless/RF Infrastructure, Device/Workstation, OT/ICS Device

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **NE-1.8.1: Wireless Access Policy and Authorization**
    - **Description:** Enumerate every type of wireless access the program permits with the configuration requirements, connection requirements, and implementation guidance governing each, authorize each type before any connection of that type is allowed, require that embedded radios be disabled on components not authorized to use them, and record the resulting wireless policy in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-18 (partial) base mapping and its AC-18(3) (partial) mapping. Its scope includes embedded radios in printers, sensors, management controllers, and OT devices, which programs most often fail to govern. The asset-class baselines apply the disable, and Rogue Access Point Detection finds radios that appear anyway. It is Documentation and event-driven as the wireless footprint changes.

- **NE-1.8.2: Wireless Network Authentication (WPA2/3-Enterprise)**
    - **Description:** Authenticate wireless network access through WPA2 or WPA3-Enterprise so that devices and users joining over wireless are authenticated via 802.1X/EAP and their traffic is encrypted, rather than admitted through a shared pre-shared key.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-18(1) (partial) mapping. It extends the 802.1X admission model to wireless, using per-user enterprise authentication instead of a shared pre-shared key.

- **NE-1.8.3: Rogue Access Point Detection**
    - **Description:** Deploy wireless intrusion detection sensors and RF spectrum monitoring across the program's facilities to identify unauthorized access points attached to the wired network, ad hoc and peer-to-peer wireless networks, and evil-twin beacons impersonating the program's own SSIDs, and alert on each detection so the transmitter can be located and removed.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(14) (full) mapping. It finds rogue access points and evil twins, which never present themselves to the wired admission layer and so bypass 802.1X entirely. It adds no CM-8(3) slice, since findings route into the existing discovery process. It is tagged Automate and sits at Level 2, closing the path that bypasses mandatory admission.

## NE-2: Network Boundary Security

### NE-2.1: Private Connectivity

**Design Intent:** Every provider-managed service, including the foundation model, the spoke vaults, and the portal database, is reached only through a private endpoint in its own spoke, with public access disabled. Configuration checks alert if public access returns. The dedicated circuit terminates on the cloud hub and the data center hub. The carrier path is not trusted, so traffic crosses the circuit inside encrypted tunnels between the hubs. Its routing sessions are authenticated, and prefix filters accept only KESTREL's own address ranges.

**NIST Control Mapping:**

- **SC-7(4) (partial):** a private endpoint is the managed interface for an externally reached service, which Private Network Endpoint Deployment builds and Public Network Access Disablement makes the only path. Dedicated Private Circuit Connectivity covers the external telecommunication service, and Routing Protocol and Control Plane Protection covers the enhancement's control plane parts, such as route origin authorization. It is partial because exception review runs through the PPSM baseline, and Authorized Cloud Access Point Integration holds a further slice.
- **Declined:** SC-8 is not claimed for routing-update authentication, since transmission protection is the Data focus area's. Private Network Endpoint Monitoring uses the existing SI-4 telemetry platform rather than a new citation.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Private Connectivity/Dedicated Circuit, Routing/Switching Fabric, Serverless/Platform Service, Storage/Database

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider supplies the private endpoint service and the dedicated circuit's cloud side.

**Security Impact:** Moderate

**Activities:**

- **NE-2.1.1: Private Network Endpoint Deployment**
    - **Description:** Deploy a private endpoint for each in-scope PaaS, serverless, and provider-managed service, projecting the service into the program's private address space so it is reachable over the internal network rather than a public address.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the managed-interface dimension of the outcome's SC-7(4) (partial) mapping. It projects each external service into the program's address space, and Public Network Access Disablement makes that the only path. It is event-driven as services are onboarded.

- **NE-2.1.2: Public Network Access Disablement (private-only enforcement)**
    - **Description:** Disable the public network access setting on each service that has a private endpoint so that the endpoint becomes the only ingress path and the service rejects all connections arriving over its public address.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the traffic-flow-policy dimension of the outcome's SC-7(4) (partial) mapping by removing the public path. Where a service can be private-only, disable public access here. Where public reachability must remain, Service Native Firewall Configurations constrains it under SC-7(11).

- **NE-2.1.3: Private Network Endpoint Monitoring**
    - **Description:** Monitor the deployed private endpoints for connection health, DNS resolution correctness, and any regression that would re-expose a service to the public network, surfacing deviations for investigation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it uses the existing Centralized Network Telemetry and Analytics Platform. It confirms the private-only posture continues to hold. It is tagged Automate and sits at Level 2, guarding against silent regression.

- **NE-2.1.4: Dedicated Private Circuit Connectivity**
    - **Description:** Terminate the dedicated circuit joining the program's on-premises estate to its cloud and partner environments on a managed interface at each end, establish the traffic flow policy that interface enforces, and route the program's cross-environment traffic over that circuit rather than over an internet path.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries the external-telecommunications-service dimension of the outcome's SC-7(4) (partial) mapping, since a dedicated circuit is that service and its termination is the managed interface. Cost is High because the circuit is billed as standing capacity, and the timeline is Long-term because of carrier lead times. A dedicated circuit is private but not encrypted, so the Data focus area's transmission protection still applies.

- **NE-2.1.5: Routing Protocol and Control Plane Protection**
    - **Description:** Protect the routing control plane the program's external and hybrid connectivity runs on by authenticating every external routing adjacency, filtering accepted and advertised prefixes against an explicit list with a maximum-prefix limit, publishing route origin authorizations for the address space the program holds, and validating route origin on the announcements it accepts where the upstream supports it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the control plane dimension of the outcome's SC-7(4) (partial) mapping through adjacency authentication, prefix filtering, published route origin authorizations, and origin validation. An accepted bogus announcement can move traffic onto someone else's path without touching a firewall rule. Route origin authorizations apply only where the program holds its own address space, so the activity narrows to adjacency authentication and prefix filtering otherwise.

### NE-2.2: Platform Service Network Integration

**Design Intent:** Managed services that support it are injected into their spoke's subnets, so their traffic follows the hub's routes and inspection. Edge listeners exist only in the DMZ. Mission team services publish only internal listeners, which the DMZ's edge services reach through the cloud hub. The Platform Team reviews internal connections each quarter and removes any that no longer match a documented flow.

**NIST Control Mapping:**

- **CA-9 (partial):** claimed for Service Virtual Network Deployments, which authorizes and documents each managed service's connection into the program's network as an internal connection. Internal Connection Review and Termination holds the rest, namely termination and periodic review.
- **CM-7 (partial):** claimed at the base because Service Communication Configuration and Load Balancer and Edge Listener Configuration permit only the functions, ports, and protocols each service or listener needs. No enhancement fits this scoping better than the base. The Device and Infrastructure focus area and Secure Remote Access hold other disjoint CM-7 slices.
- **Declined:** Neither CA-9 activity reaches CA-3, which the Manage pillar holds full. CA-9(1) is the provisioning-time gate Device and Infrastructure owns. SA-9(2) places a disclosure duty on the provider rather than the program. SC-7(11) belongs to Service Native Firewall Configurations, no SC-7 claim is made, and AC-4 and SC-7(5) stay with Network Micro Segmentation.

**Deployment Type:** Cloud, Hybrid

**Affected Components:** Serverless/Platform Service, Storage/Database, Load Balancer/Reverse Proxy/API Gateway

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.

**Security Impact:** Moderate

**Activities:**

- **NE-2.2.1: Service Virtual Network Deployments**
    - **Description:** Inject or delegate each in-scope PaaS and serverless service into its designated virtual network and subnet, and document the resulting internal connection's interface characteristics and permitted information flows.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's CA-9 (partial) mapping by authorizing and documenting each managed service's connection as an internal connection. It is event-driven as services are onboarded.

- **NE-2.2.2: Service Communication Configuration**
    - **Description:** Configure how each network-integrated service communicates, identifying and permitting only the functions, ports, protocols, and destinations the service requires and recording them alongside the service's network integration.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-7 (partial) mapping by permitting each integrated service only the functions, ports, protocols, and destinations it needs. SA-9(2) is not cited because it obliges the provider to disclose needs, not the program to restrict them. It is event-driven as service dependencies change.

- **NE-2.2.3: Load Balancer and Edge Listener Configuration**
    - **Description:** Configure each load balancer, application gateway, and edge listener in the program's request path to expose only the listeners, ports, and protocol versions its application requires, terminate TLS under the cryptographic standard the program's transmission-protection policy sets, redirect or refuse cleartext, and forward only to the health-checked backend pool the application declares.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the request-path-edge dimension of the outcome's CM-7 (partial) mapping. It applies the Data focus area's TLS standard at the listener without claiming SC-8. The listener's own surface is where a forgotten cleartext port or legacy protocol survives every inspection layer, so Web Application Firewall and Network Firewall do not cover it.

- **NE-2.2.4: Internal Connection Review and Termination**
    - **Description:** Review the continued need for every authorized internal connection on a defined cycle with the system owner it serves, terminate the connections that no longer carry a required flow or whose defined termination conditions have been met, and update the authorization record accordingly.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the terminate-and-review dimensions of the outcome's CA-9 (partial) mapping. It retires integrations that outlived their workload, which the PPSM recertification does not reach since it covers boundary-crossing services only. It is Process because the system owner confirms continued need. Periodic (Annual) is a baseline the AO may shorten for higher-risk integrations.

### NE-2.3: Service Native Firewall Configurations

**Design Intent:** Every platform service has its resource firewall on, such as the spoke vaults, the database services, the feedback endpoints' queues, and each foundation model deployment. Each admits only its own spoke's private endpoint and the workloads that need it. No KESTREL platform service is reachable over a public address, so no public allow-list exists.

**NIST Control Mapping:**

- **SC-7 (partial):** claimed at the base for Service Native Firewall Capability Enablement, which turns on the boundary protection each cloud service exposes at its own edge. It sits alongside the network-topology and OT-zone SC-7 claims other outcomes hold.
- **SC-7(11) (partial):** claimed for Service Firewall Rules and Service Public Access Allow-List Configuration, which permit incoming traffic only from authorized sources. It is partial, shared by those two activities. Private Connectivity removes public access where possible, while this outcome constrains it where it must remain.

**Deployment Type:** Cloud, Hybrid

**Affected Components:** Service-Native/Resource-Level Firewall, Database Service, Object/File Storage, Secrets Vault, Message Queue/Event Stream, Serverless/Platform Service

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.

**Security Impact:** Moderate

**Activities:**

- **NE-2.3.1: Service Native Firewall Capability Enablement**
    - **Description:** Enable the native firewall capability on each in-scope cloud service so the service enforces a default-deny boundary at its own resource edge before any allow rules are added.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7 (partial) base claim by enabling the service-edge boundary that the rules and allow-list then constrain. It is event-driven as services are onboarded.

- **NE-2.3.2: Service Firewall Rules**
    - **Description:** Author the native firewall rules for each service that define which networks, private endpoints, and trusted service identities may reach it, denying every source not explicitly permitted.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's SC-7(11) (partial) mapping by defining the authorized sources and destinations for each service firewall from a default-deny base. It is standing enforcement, so it is not tagged Automate.

- **NE-2.3.3: Service Public Access Allow-List Configuration**
    - **Description:** Pin the public reachability of any service that must remain reachable over public addresses to an explicit allow-list of authorized source IP ranges, remove any open-to-the-internet access, and document each retained public exception.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the residual-public-access portion of the outcome's SC-7(11) (partial) mapping by pinning retained public reachability to enumerated sources. Public Network Access Disablement removes public access where possible, so the two do not overlap. It is event-driven as authorized sources change.

### NE-2.4: Network Firewall

**Design Intent:** The cloud hub's next-generation firewall sits at the center of the ten spokes, each peered only to the hub. Custom routes send every spoke's traffic, east-west and outbound, through it. The data center hub is a redundant appliance pair in front of the SDN fabric. Outbound web traffic is limited to an allow-list of update and package sources, all reached through the package mirror. Both hubs inspect outbound TLS. East-west flows already protected by mutual TLS between workload identities are exempt from decryption.

**NIST Control Mapping:**

- **SC-7(3) (partial):** the hub-and-spoke topology reduces external and inter-spoke connections to one managed access point, where the firewall controls traffic. On-Premises Perimeter Firewall Deployment holds the same claim for each physical site. The enhancement fits this mechanism exactly, and citing it avoids a fourth SC-7 base claim.
- **SC-7(8) (partial):** claimed for HTTP/HTTPS Traffic URL Filtering, which routes outbound web traffic through the firewall's filtering proxy to permit or deny by URL and category. Authorized Cloud Access Point Integration holds the cloud enclave's slice.
- **SC-7(10) (partial):** claimed for TLS Inspection Advanced Filtering, which decrypts outbound TLS to inspect for policy violations and exfiltration. Training Cluster Network Segmentation and Egress Control holds a disjoint slice for training-cluster egress.
- **Declined:** SC-8 is not claimed, since TLS inspection terminates encryption rather than protecting it. The peering and routing activities only force traffic to the SC-7(3) access point. CM-2 and CM-6(1) stay with Network Centralization and Standardization, whose baseline the firewall policies build on.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Network Firewall, Routing/Switching Fabric

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider supplies the virtual machines and networking the cloud hub's firewalls run on.

**Security Impact:** High

**Activities:**

- **NE-2.4.1: Hub and Spoke Cloud Network Topology**
    - **Description:** Design a hub-and-spoke topology in which a central hub network hosts the shared firewall and security services and each workload spoke connects only through that hub, consolidating the program's external and inter-spoke connections to a single managed access point, and record the design in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the design dimension of the outcome's SC-7(3) (partial) mapping by establishing the single managed access point. Document it in the CMP with the network topology records. It is Documentation and event-driven as the architecture changes.

- **NE-2.4.2: Spoke Cloud Network Peering**
    - **Description:** Peer each workload spoke network to the hub so that spoke traffic transits the hub rather than reaching external or peer destinations directly, realizing the hub-and-spoke topology as concrete network peerings.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it is the plumbing that realizes the hub-and-spoke design. It is event-driven as spokes are onboarded.

- **NE-2.4.3: Custom Routing Configuration**
    - **Description:** Configure user-defined routes that force all spoke egress, ingress, and inter-spoke traffic through the hub firewall, leaving no path that bypasses the inspecting boundary.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it steers traffic to the SC-7(3) access point and the SC-7(8) filtering proxy. Without it, the hub firewall could be bypassed. It is event-driven as spokes and destinations change.

- **NE-2.4.4: Cloud-Native Firewall Deployment**
    - **Description:** Deploy the cloud-native firewall in the hub so that a managed, scalable boundary component sits at the consolidated access point and inspects every flow the routing steers to it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the enforcement dimension of the outcome's SC-7(3) (partial) mapping by placing the firewall at the managed access point. Recurring cost is High because a premium cloud firewall bills on inspected throughput, which becomes the whole estate's traffic volume.

- **NE-2.4.5: On-Premises Perimeter Firewall Deployment**
    - **Description:** Stand a redundant physical or virtual firewall pair at each on-premises and enclave perimeter, cable and route the site so that every flow leaving or entering the perimeter transits that pair with no alternate path around it, and fail the pair over without dropping the boundary.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7(3) (partial) mapping in the on-premises and isolated estate, consolidating each site's external connections through physical topology and routing. In a disconnected enclave, it enforces the perimeters between mission segments, laboratories, and authorized peer enclaves. Its rules come from Firewall Policies and Filtering Rules, and device settings from Network Infrastructure Device Hardening. One-time cost is High because the pair is bought per site.

- **NE-2.4.6: Firewall Policies and Filtering Rules**
    - **Description:** Author the firewall's network and application rule collections that permit only the approved source, destination, port, and protocol combinations and deny all other traffic at the hub boundary, and document the resulting rule set in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the traffic-control dimension of the outcome's SC-7(3) (partial) mapping by defining what may cross the access point. It builds on the approved baseline from Firewall Standardization and Routing Management rather than re-claiming CM-2. It is standing enforcement, so it is not tagged Automate.

- **NE-2.4.7: HTTP/HTTPS Traffic URL Filtering**
    - **Description:** Route outbound HTTP and HTTPS traffic through the firewall's filtering proxy and permit or deny each request by URL and site category, blocking access to disallowed and known-malicious web destinations.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7(8) (partial) mapping by filtering egress web traffic by URL and category at the managed interface. It is Level 2, strengthening the mandatory boundary control in Firewall Policies and Filtering Rules.

- **NE-2.4.8: TLS Inspection Advanced Filtering**
    - **Description:** Terminate and decrypt outbound TLS at the firewall, inspect the plaintext for policy violations and data exfiltration, and re-encrypt before forwarding, so that content filtering is not blind to encrypted traffic.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7(10) (partial) mapping by decrypting TLS so the firewall can inspect for exfiltration before re-encrypting. SC-8 is not claimed because it terminates encryption. It is Level 2, strengthening the boundary control in Firewall Policies and Filtering Rules.

### NE-2.5: DDoS Protection

**Design Intent:** The DMZ holds no cloud provider public addresses. Its DoD-registered addresses are reached only through DISA's internet access points and the Boundary Cloud Access Point, which absorb network-layer floods upstream. The DMZ's edge services add request-rate limits for every user-facing application. The cloud hub rate-limits each spoke, so a runaway workload cannot flood the hub or ML Prod's endpoints. DDoS alerts go to the security monitoring platform.

**NIST Control Mapping:**

- **SC-5 (partial):** claimed at the base for Application Layer DDoS Protection against request floods, which no capacity-focused enhancement matches. API Abuse Protection and the Web Application Firewall's Bot Management and Request Rate Limiting hold the other two slices, split by mechanism.
- **SC-5(1) (partial):** claimed for Outbound and Internal Flood Containment, which restricts a compromised host from flooding other systems. It is partial because containment bounds rate and reach rather than removing the ability, and it covers only attack classes a network control can act on.
- **SC-5(2) (partial):** claimed for Network Layer DDoS Protection, since absorbing layer-3 and layer-4 floods through capacity, bandwidth, and redundancy is this enhancement's mechanism, a partial claim alongside the outcome's other SC-5 slices.
- **SC-5(3) (partial):** claimed for DDoS Protection Monitoring and Alerts, which detects denial-of-service indicators in both directions and watches utilization headroom. Link-Anomaly and Jamming-Indicator Monitoring and Alerting holds the RF link slice.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** DDoS Protection, Application/API

**External Dependencies:** The Boundary Cloud Access Point, which absorbs network-layer floods before they reach KESTREL. The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization, supplies the edge services' rate limiting.

**Security Impact:** Moderate

**Activities:**

- **NE-2.5.1: Network Layer DDoS Protection**
    - **Description:** Enable network-layer (layer 3 and 4) DDoS protection on the program's public-facing address space and load balancers, sized with the capacity, bandwidth headroom, and redundancy to absorb volumetric floods without exhausting the protected services.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-5(2) (partial) mapping by absorbing volumetric floods through capacity, bandwidth, and redundancy. Its applicability is narrower than the outcome's Deployment Type, since an isolated enclave with no public address space relies on its own architectural headroom. It is tagged Automate because the managed service detects and mitigates attacks automatically.

- **NE-2.5.2: Application Layer DDoS Protection**
    - **Description:** Engage application-layer DDoS protection on the program's HTTP and HTTPS endpoints to detect and rate-limit request-flood attacks that mimic legitimate traffic and would exhaust application resources below the volumetric threshold.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-5 (partial) base mapping by protecting application endpoints against request floods the network-layer mechanism misses. It is tagged Automate because it detects and rate-limits anomalous requests automatically. It is Level 2, strengthening the mandatory volumetric protection against lower-rate attacks.

- **NE-2.5.3: DDoS Protection Monitoring and Alerts**
    - **Description:** Monitor the DDoS mitigation service and the program's own network telemetry for inbound attack detections, protected-resource utilization, and signs of a denial-of-service condition arising inside the environment, such as internal resource exhaustion, broadcast and multicast storms, or a program host generating flood traffic toward an internal or external target, and alert operators on each so the response and availability impact can be tracked through to mitigation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-5(3) (partial) mapping. Its detection is bidirectional, covering internal exhaustion, broadcast storms, and outbound floods alongside inbound detections, which gives it value in isolated environments. Alerts feed the Network Security Posture Dashboard. It is tagged Automate and sits at Level 2.

- **NE-2.5.4: Outbound and Internal Flood Containment**
    - **Description:** Bound what the program's own hosts and segments can emit by applying egress rate limits and per-source connection ceilings at the boundary, enabling broadcast, multicast, and unknown-unicast storm control on access switches, and blocking spoofed source addresses at every point where the program's traffic leaves a segment.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-5(1) (partial) mapping by restricting a compromised host or insider from flooding other systems. It is the enforcement counterpart to the outbound indicators DDoS Protection Monitoring and Alerts detects, and in an isolated enclave the threat is almost entirely internal. Source-address filtering keeps the program's network from being used for reflected or amplified attacks. It is Level 2, covering the direction the inbound mitigations do not.

### NE-2.6: Web Application Firewall

**Design Intent:** The WAF in the DMZ's edge services fronts every user-facing application in blocking mode, with managed rules plus custom rules for each application. Today those are the identity-aware access proxy, the analyst portal, the signals workbench, and the partner API. Every partner-facing API is checked against its published schema and rate-limited per partner. Nothing on premises faces users directly, so no on-premises reverse-proxy WAF is needed.

**NIST Control Mapping:**

- **SI-10 (partial):** a web application firewall checks the validity of request headers, query strings, cookies, and body at the network edge and rejects malicious or malformed inputs. Other slices are held by API Security Testing and others, split by lifecycle position and input class. The base is cited because SI-10(1) through SI-10(4) do not describe a WAF policy.
- **SI-10(5) (partial):** carried by API Protection Policy and Schema Validation, which holds requests to the operations, parameters, types, and ranges the interface specification declares and refuses unregistered clients. Single Sign on (SSO) and three Artificial Intelligence focus area outcomes hold other input-class slices.
- **SI-10(6) (partial):** carried by WAF Policy Configurations and Custom Rules, whose OWASP core rule set and custom rules reject SQL injection, cross-site scripting, and other injection classes. The Application focus area's API Security Testing holds the other slice.
- **SC-5 (partial):** claimed for Bot Management and Request Rate Limiting, which bounds unauthenticated automated clients that are abusive by rate rather than content, such as credential stuffing and scraping. DDoS Protection and API Abuse Protection hold the other two slices.
- **CM-7(1) (partial):** claimed for API Gateway Runtime Policy Enforcement, which refuses to route any interface absent from the runtime inventory. Runtime API Inventory and Governance identifies those routes and decides their disposition, so the two are assessed as a pair. Insecure Services and Protocols holds a disjoint slice.
- **Declined:** SC-5(2) and SC-5(3) belong to DDoS Protection. The SC-7 base is already held at three scopes in this focus area, and SC-7(5) and SC-7(8) are held by Network Micro Segmentation and Network Firewall. SI-3 stays with the Device and Infrastructure focus area's host anti-malware. WAF Service Selection and WAF Policy and Service Endpoint Associations only deploy and attach the mechanism.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Web Application Firewall, Load Balancer/Reverse Proxy/API Gateway, First-Party/Custom Application Code, Self-Hosted Third-Party Application (COTS), API/Interface Contract

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider supplies the WAF service.

**Security Impact:** Moderate

**Activities:**

- **NE-2.6.1: WAF Service Selection**
    - **Description:** Select and deploy the web application firewall service appropriate to each web-facing application's fronting resource (application gateway, load balancer, or content-delivery edge), so a policy-enforcement point exists in the request path ahead of the application.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it stands up the enforcement point the rule set then populates. It is event-driven as web-facing applications are onboarded.

- **NE-2.6.2: WAF Policy Configurations and Custom Rules**
    - **Description:** Configure the managed rule sets, namely the provider's OWASP core rule set and known-exploit signatures, and author any application-specific custom rules so the WAF inspects each HTTP and HTTPS request and blocks SQL injection, cross-site scripting, and other application-layer exploit payloads, then document the resulting rule set and policy configuration in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries both of the outcome's SI-10 (partial) and SI-10(6) (partial) mappings. The base covers validity checks across every request component, and the enhancement covers the injection-prevention subset. It is standing enforcement, so it is not tagged Automate.

- **NE-2.6.3: WAF Policy Mode**
    - **Description:** Set each WAF policy to prevention mode, which actively blocks, once its rules have been tuned, and use detection-only mode solely as a temporary tuning stage so that in steady state malicious requests are rejected rather than merely logged.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the enforcement dimension of the outcome's SI-10 (partial) and SI-10(6) (partial) mappings, deciding whether failed inputs are blocked or only logged. An injection rule left in detection-only mode prevents nothing. It is event-driven as rules move from tuning into enforcement.

- **NE-2.6.4: WAF Policy and Service Endpoint Associations**
    - **Description:** Associate each configured WAF policy with the specific front-facing service endpoints it protects, such as application gateway listeners, front-door routes, or load-balancer frontends, so every web-facing entry point is bound to an enforcing policy and none is left uncovered.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since it binds the SI-10 policy to endpoints in the request path. Without it, a configured policy inspects no traffic. It is event-driven as endpoints are onboarded.

- **NE-2.6.5: On-Premises Reverse-Proxy WAF Deployment**
    - **Description:** Place a reverse proxy running the program's web application firewall rule engine in front of each web application hosted on infrastructure the program owns, terminate client connections there so no request reaches the application server directly, and load it with the same rule content and blocking mode the provider-edge policies carry.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-10 (partial) and SI-10(6) (partial) mappings in the on-premises and disconnected estate. An enclave's internal web applications and consoles are reachable by any host there, so an adversary with a foothold attacks them directly. Use the same rule sets WAF Policy Configurations and Custom Rules maintains, and update signatures through the program's existing offline path.

- **NE-2.6.6: Bot Management and Request Rate Limiting**
    - **Description:** Classify the automated clients reaching each web application through the WAF's bot signatures, client fingerprinting, and challenge mechanisms, permit the automation the mission depends on through an explicit allow-list, and apply per-client and per-endpoint request rate ceilings that throttle or block the credential-stuffing, scraping, and enumeration traffic the rest of it generates.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-5 (partial) mapping as the third disjoint slice of that base control. A credential-stuffing run sends well-formed requests at volumes no capacity control notices, so rate and client classification stop it rather than payload inspection. Allow-list search indexing, monitoring probes, and partner integrations before tuning. It is tagged Automate and sits at Level 2.

- **NE-2.6.7: API Protection Policy and Schema Validation**
    - **Description:** Load each exposed API's schema into the WAF as an API protection policy, reject requests whose operation, path, parameters, types, or value ranges fall outside what that schema declares, restrict the interface to its registered client population, enable the API-specific rule content covering broken object-level authorization, mass assignment, and the other abuse patterns generic web rules do not carry, and document the resulting API protection policy in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-10(5) (partial) mapping and is this outcome's one true allow-list, refusing anything the schema does not permit. An inaccurate schema is a defect for the Application focus area's API outcomes to fix, not a reason to relax the policy. It also contributes to the SI-10 (partial) and SI-10(6) (partial) claims. Undocumented APIs are refused by API Gateway Runtime Policy Enforcement instead.

- **NE-2.6.8: API Gateway Runtime Policy Enforcement**
    - **Description:** Admit only the routes recorded in the runtime interface inventory the Application focus area's Runtime API Inventory and Governance maintains, apply each record's authentication, authorization, and rate-limiting policy to the traffic admitted, and refuse traffic to any route with no record.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-7(1) (partial) mapping as the enforcement half of the obligation Runtime API Inventory and Governance identifies. Roll out in report mode first to find legitimate routes the inventory is missing, since default-deny against an incomplete inventory takes production down. Express policies through Policy-as-Code Evaluation rather than gateway-specific configuration. It is Level 2 and tagged Automate, since the gateway evaluates every request.

### NE-2.7: Secure Remote Access

**Design Intent:** Performers reach KESTREL only through the identity-aware access proxy for developer tools and the VDI brokers for desktops. Neither offers a network tunnel, so no laptop joins KESTREL's network and split tunneling cannot occur. The VDI desktops reach management ports only during an approved just-in-time window, or through the privileged access platform's session hosts. Sessions end after 15 idle minutes, and the Security Team can end any session at once. Recorded sessions and broker logs go to the security monitoring platform.

**NIST Control Mapping:**

- **AC-17 (partial):** claimed at the base for Virtual Desktop Isolation and Browser Based Access, each an authorized remote-access type whose restrictions and configuration are set before connections are allowed. Narrower access outcomes elsewhere defer to this general fabric, and the other activities here hold its enhancements.
- **AC-17(1) (partial):** claimed for Virtual Desktop Monitoring and Alerting, which monitors and controls remote sessions automatically. Access Process for Third-Party Support holds the disjoint slice for vendor support sessions.
- **AC-17(2) (partial):** claimed for Remote Access Key Management, which manages the keys and certificates behind encrypted remote sessions.
- **AC-17(3) (partial):** claimed for Private Remote Access, which routes all remote access through a private broker instead of public RDP or SSH. Authorized Cloud Access Point Integration holds the cloud enclave's management-path slice.
- **AC-17(9) (full):** claimed for Remote Session Disconnect Capability, since building the capability and fixing the period is the whole enhancement.
- **SC-7(7) (full):** claimed for Split Tunneling Prevention, which sets the prohibition and its enumerated exception conditions. Its subject is the remote device's connectivity, so it does not reopen the SC-7 base.
- **CM-7 (partial):** claimed at the base for JIT Network Port Access, whose time-bound opening and closing of a host port is a distinct least-functionality dimension. Policy Service Restrictions and Service Communication Configuration hold other disjoint CM-7 slices.
- **SC-10 (full):** carried by Idle Network Connection Termination, which ends a session's network connection at its close or after inactivity. No other outcome claims it.
- **Declined:** AC-17(4) is not claimed, since Privileged Credential Vaulting and Session Brokering governs privileged remote actions.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Remote Access/VPN Gateway, Virtual Desktop Infrastructure (VDI), Virtual Machine/Server, Identity Platform

**External Dependencies:** The performer, whose CMMC Level 2 laptops originate these sessions under the interconnection agreement.

**Security Impact:** High

**Activities:**

- **NE-2.7.1: Private Remote Access**
    - **Description:** Stand up a private remote-access broker, such as a bastion or private-link-fronted jump service, as the single managed access control point for administrative and remote-worker access, and remove any publicly exposed RDP or SSH so no internal system is reachable directly from the internet.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-17(3) (partial) mapping by funneling remote access through a managed access control point instead of public listeners. It is a standing broker, so it is not tagged Automate.

- **NE-2.7.2: JIT Network Port Access**
    - **Description:** Implement time-bound, just-in-time opening of specific host ports and services only when an authenticated, approved request requires them, closing them automatically when the access window expires, and document the JIT eligibility and approval criteria in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's CM-7 (partial) claim at the base, keeping host ports closed by default and opening one only for an approved session. It differs from the standing service policy in Policy Service Restrictions and opens no AC-17 claim. It is Level 2, and it is the one activity here that also applies inside an isolated enclave. It is tagged Automate because the broker grants and revokes ports automatically.

- **NE-2.7.3: Remote Access Key Management**
    - **Description:** Manage the SSH keys, client certificates, and other credentials that authenticate remote-access sessions, enrolling them into the program's secret store and binding their generation, rotation, and revocation to the Key Management Plan (KMP).
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-17(2) (partial) mapping by keeping remote-session keys and certificates managed rather than static or shared. Document algorithms, rotation intervals, and revocation triggers in the KMP. It is event-driven as operators and access paths change.

- **NE-2.7.4: Virtual Desktop Isolation**
    - **Description:** Provision a virtual desktop infrastructure (VDI) tier that remote operators connect into, so the internal network is reached only from the managed virtual desktop and never directly from the operator's own potentially untrusted endpoint, and document its usage restrictions and connection requirements as an authorized remote-access type.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Extensive; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AC-17 (partial) base mapping by establishing the isolated virtual desktop as an authorized remote-access type. Its cost is the highest in this outcome because the tier is sized to concurrent sessions and carries ongoing per-seat licensing. It is event-driven as the remote-workforce footprint changes.

- **NE-2.7.5: Browser Based Access**
    - **Description:** Offer a clientless, browser-based access option for lower-assurance or unmanaged-endpoint scenarios where a full VDI or installed client is not warranted, and document its permitted scope and connection requirements as a separate authorized remote-access type.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's AC-17 (partial) base mapping as a second authorized remote-access type, mediated entirely through the browser. It is Level 2, extending coverage where a full virtual desktop does not fit. It is event-driven as access needs change.

- **NE-2.7.6: Virtual Desktop Monitoring and Alerting**
    - **Description:** Monitor the remote-access and virtual-desktop sessions for connection activity, anomalous behavior, and policy violations, and alert operators so active remote sessions are observable while under way and reviewable afterward.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-17(1) (partial) mapping as the general remote-session monitoring fabric the Identity focus area's vendor-session monitoring defers to. It is tagged Automate and sits at Level 2, adding assurance over mandatory access mediation.

- **NE-2.7.7: Split Tunneling Prevention**
    - **Description:** Prevent a remote device from holding a connection into the program's environment and a route to any other network at the same time, enforcing full-tunnel routing on every remote-access client, and permit an exception only where a specific split is securely provisioned under safeguards documented in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7(7) (full) mapping. A split-tunneled endpoint bridges the program's environment and a network the program does not control, bypassing every boundary control. Where an exception is required, such as local printing, enumerate the permitted destinations rather than writing a general exclusion.

- **NE-2.7.8: Remote Session Disconnect Capability**
    - **Description:** Build and exercise the capability to disconnect or disable remote access, for a single session or for the whole remote-access path at once, within the time period the program defines, and document that period together with the roles authorized to invoke the disconnect in the IRP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-17(9) (full) mapping and is the enforcement end of Virtual Desktop Monitoring and Alerting. Build it to cut a single session and the entire remote-access path when the broker is implicated. Document it in the IRP, and test it annually. It is a human decision, so it is not tagged Automate.

- **NE-2.7.9: Idle Network Connection Termination**
    - **Description:** Terminate the network connection behind a remote or management session when the session ends or after a defined period of inactivity, at the gateway or broker that terminates the connection rather than relying on the client to close it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-10 (full) mapping. It closes abandoned VPN or management tunnels whose application session has ended, which neither on-demand disconnect nor the Identity focus area's session termination covers.

### NE-2.8: Telemetry, Tracking, and Command (TT&C) Link Security

**Design Intent:** KESTREL's equivalent of a TT&C link is the aircraft datalinks, so CCSDS SDLS itself does not apply. The command uplink is authenticated and encrypted, so an aircraft executes only commands from a KESTREL ground control station. The telemetry and payload downlink is encrypted and integrity-protected. The keys are CCSD row 13's key material, held in the HSMs and the datalink crypto modules. Stations alert operators to link anomalies and jamming indicators, and those alerts also reach the Security Team.

**NIST Control Mapping:**

- **IA-3(1) (partial):** claimed for Command Uplink Authentication and Encryption and Telemetry Downlink Authentication and Integrity Protection, since CCSDS SDLS cryptographically authenticates ground and spacecraft to each other before accepting frames. OT/Legacy Device Identity Controls holds the terrestrial slice, split by channel.
- **SC-8 (partial), SC-8(1) (partial):** claimed for the uplink and downlink confidentiality and integrity that SDLS authenticated encryption provides. The Data focus area's TLS Encryption Enforcement and Secure File Transfer and Management Protocols hold the other two slices, split by channel.
- **SC-5(3) (partial):** claimed for Link-Anomaly and Jamming-Indicator Monitoring and Alerting, which watches ground receiver signal-quality telemetry for jamming or spoofing patterns. DDoS Protection holds the network-layer slice. Physical anti-jam engineering belongs to the Program Protection Plan, and no SABER outcome performs it.
- **SC-40 (partial):** the framework's only claim of the control. The uplink and downlink activities defeat imitative and spoofed signals, and Link-Anomaly and Jamming-Indicator Monitoring and Alerting detects interference. It is partial because spread spectrum and frequency hopping belong to the radio design.
- **Declined:** the IA-3 base adds nothing beyond the enhancement. SC-8(2) is unneeded, since protection is re-established after an outage, and SC-8(3) and SC-8(4) are not implemented anywhere. SC-5(1), SC-5(2), and the SC-5 base do not fit RF interference, which SC-5(3) already covers. AC-17 stays with Secure Remote Access for ground segment operator access. SC-12, SC-13, and SC-28(3) belong to the Data focus area's Cryptographic Management capability.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** OT/ICS Device, Network Infrastructure, Cryptographic Hardware/HSM

**External Dependencies:** The aircraft and datalink manufacturers, who supply the datalink crypto modules.

**Security Impact:** High

**Activities:**

- **NE-2.8.1: Command Uplink Authentication and Encryption (CCSDS SDLS)**
    - **Description:** Deploy the CCSDS Space Data Link Security Protocol on the command uplink so the spacecraft cryptographically authenticates each command frame's origin and rejects any frame not authenticated as arriving from an authorized ground segment, and encrypt the uplink's content under the algorithm baseline the Cryptographic Management capability approves.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries the ground-to-spacecraft dimension of the outcome's IA-3(1) (partial) mapping and the uplink half of its SC-8 and SC-8(1) (partial) mappings. A spacecraft that executes any frame on its command frequency is commandable by anyone who can reach it. Effort, cost, and timeline are at the top of the scales because the keys and frame logic are built into flight software before launch, so a late start means a costly retrofit.

- **NE-2.8.2: Telemetry Downlink Authentication and Integrity Protection (CCSDS SDLS)**
    - **Description:** Apply the CCSDS Space Data Link Security Protocol to the telemetry downlink so ground authenticates each telemetry frame as genuinely sourced from its own spacecraft and detects any frame altered or injected in transit, and encrypt downlink content whose sensitivity warrants confidentiality under the same approved algorithm baseline the uplink uses.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries the spacecraft-to-ground dimension of the outcome's IA-3(1) (partial) mapping and the downlink half of its SC-8 and SC-8(1) (partial) mappings. A spoofed downlink feeds false data into health monitoring and orbit determination, which can push operators into a harmful command decision. It shares the uplink's cost profile because both are engineered as one SDLS implementation.

- **NE-2.8.3: Link-Anomaly and Jamming-Indicator Monitoring and Alerting**
    - **Description:** Monitor the ground receiver's signal-quality telemetry, including carrier lock status, bit error rate, signal-to-noise ratio, and frame-acceptance and frame-reject counts, for the degradation pattern a jamming, spoofing, or interference event produces, and alert operators when an indicator crosses its defined threshold so a link-availability event is investigated as a potential security incident rather than dismissed as routine RF variation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-5(3) (partial) mapping by monitoring ground receiver signal-quality indicators and alerting on a link denial-of-service condition. It detects rather than defeats jamming, turning a degraded link into a tracked security event with an owner. It is tagged Automate and sits at Level 2.

### NE-2.10: Cross Domain Solution (CDS) Transfer Procedures

**Design Intent:** KESTREL uses the enterprise cross domain solution a DoD cross domain service provider operates, and that provider owns product selection and accreditation. Low-to-high baselines need Certification to Field approval before the transfer gateway stages them. High-to-low products pass the enclave's release review and then KESTREL's own content checks. The provider's transfer logs and the gateway's logs both go to the security monitoring platform. Manual media transfer across the domains is prohibited.

**NIST Control Mapping:**

- **SC-46 (partial):** claimed for CDS Transfer Request and Approval Workflow, which operates the accredited CDS as the policy enforcement mechanism between security domains. SC-46 has no enhancements, and no other outcome claims it.
- **SC-7(22) (partial):** the CDS's high-side and low-side interfaces terminate in separate subnets dedicated to each domain, never bridged. It is held as a partial claim at the outcome level because no activity performs the placement, though CDS Accreditation and Periodic Reassessment confirms it.
- **AC-4(8) (partial):** carried by Content Inspection/Filtering Prior to Transfer, which inspects transfer content against security policy filters and blocks or quarantines failures. The other AC-4 enhancements here complete the filter.
- **AC-4(12) (partial):** claimed for Policy-Based Automated Transfer Release, which bases release on verified data type identifiers such as file signatures rather than filenames. No other outcome claims it, and it decides whether a human must be asked rather than whether content passes.
- **AC-4(15) (partial):** carried by the same inspection activity, whose dirty-word and classification-marking checks look for unsanctioned information, one partial slice of the filter.
- **AC-4(17) (partial):** carried by that activity, binding each filter decision to the source and destination domains the request workflow validates, another partial slice of the filter.
- **AC-4(26) (partial):** claimed for Transfer Audit Logging and Review, which records and audits filtering actions and results for cross-domain transfers.
- **AC-4(31) (partial):** carried by the inspection activity, whose block, strip, and quarantine outcomes keep failed content out of the receiving domain, a partial slice of the filter. None of these claims reopens the AC-4 base or the AC-4(21) diode claim.
- **Declined:** AC-4(14) is not claimed, since the accredited product's own filter definitions fix the format specifications. CDS Accreditation and Periodic Reassessment and CDS Product Selection and Baseline List Compliance carry no citation, since authorization evidence for the SC-46 mechanism belongs in the traceability artifact. SA-4 stays with the Manage pillar and the Application focus area. CA-2(1) is assessment evidence rather than a design-intent control.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Cross-Domain/Boundary Transfer, Application/API, Storage/Database

**External Dependencies:** The enterprise cross domain service provider, under the interconnection agreement covering both directions. The IL6 enclave's owner, whose release review approves every high-to-low product.

**Security Impact:** High

**Activities:**

- **NE-2.10.1: CDS Product Selection and Baseline List Compliance**
    - **Description:** Select the cross domain solution from the National Cross Domain Strategy and Management Office (NCDSMO) Cross Domain Baseline List, engage that office at the point the requirement is identified rather than at accreditation, confirm the selected product and the program's intended configuration satisfy the current Raise the Bar (RTB) design requirements, and schedule the Lab-Based Security Assessment (LBSA) the product and its configuration must pass.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Low
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since product selection and laboratory assessment are authorization evidence. A program must choose from the national cross domain authority's baseline list and pass a laboratory assessment before its own accreditation, which sets this outcome's schedule. Engage early, because a requirement found after the architecture is fixed often forces rework. Its Long-term estimate reflects the authority's calendar.

- **NE-2.10.2: CDS Transfer Request and Approval Workflow**
    - **Description:** Route every cross-domain transfer through a request-and-approval workflow in which a human authority validates the requester, the data, and the destination domain against the transfer policy and authorizes the transfer before the CDS releases it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-46 (partial) mapping by operating the accredited CDS as the authorization gate every transfer must pass. It is Process and not tagged Automate, because cross-domain release requires human review.

- **NE-2.10.3: Policy-Based Automated Transfer Release**
    - **Description:** Define the release rules the guard applies without human intervention for each high-volume or continuous transfer flow that a per-transfer human queue cannot absorb, expressed as verified data type identifiers, structural conformance to an enumerated format, source and destination pairing, and the marking the content carries, and route every transfer that falls outside those rules into the human approval workflow as an exception.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-4(12) (partial) mapping. Per-transfer human approval cannot keep up with streamed telemetry, replicated feeds, or continuous log egress. Write rules as a narrow allow-list on a named source and destination pair, route everything else to the human workflow, and expect the accreditation authority to assess the rule set. Filtering and auditing still apply to every release. It is tagged Automate at Level 2.

- **NE-2.10.4: Content Inspection/Filtering Prior to Transfer**
    - **Description:** Inspect and filter each transfer's content against the domain's transfer policy, including format checks, dirty-word and classification-marking filters, and structure validation, for the uniquely identified and authenticated source and destination domain pair before release, and block, strip, or quarantine any content that fails a filter so that it never reaches the receiving focus area.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Extensive; Recurring: Moderate
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries four of the outcome's AC-4-family mappings: AC-4(8) (partial) for policy filters, AC-4(15) (partial) for dirty-word and marking checks, AC-4(17) (partial) for authenticated source and destination binding, and AC-4(31) (partial) for keeping failed content out. An accredited product delivers the filtering, so cost is a program-level acquisition, and the timeline follows accreditation. The filters narrow human review rather than replace it, so it is not tagged Automate.

- **NE-2.10.5: Transfer Audit Logging and Review**
    - **Description:** Record every transfer's filtering actions, results, and disposition in a tamper-evident audit log, and review those logs on a defined cadence to detect policy violations, filter failures, and attempted unauthorized transfers.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-4(26) (partial) mapping. Filtering actions are captured automatically, and periodic human review detects violations and filter failures. It is not tagged Automate because that review is human.

- **NE-2.10.6: CDS Accreditation and Periodic Reassessment**
    - **Description:** Accredit the cross domain solution product against the governing cross-domain and connection-approval requirements before it enters operation, and reassess and reaccredit it on the mandated recurring cycle to confirm the CDS remains authorized and effective.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since accreditation is assessment of the SC-46 mechanism and belongs in the traceability artifact. It confirms the outcome's SC-7(22) (partial) subnet separation as part of connection approval. It is Process, repeated annually within the authorization period.

- **NE-2.10.7: Manual Cross-Domain Media Transfer**
    - **Description:** Govern every transfer between classification levels that does not pass through the accredited cross domain product by an approved manual procedure performed by appointed, trained transfer agents, requiring a second agent's review of every transfer to a lower classification, scanning and verifying content on a dedicated transfer system, and logging each transfer with its media, content, agents, and approval.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent citation. The Data focus area's Media Protection Policy and Procedures holds MP-5 and MP-8 for media handling and downgrading. DoD and intelligence community programs often call these agents data transfer agents and the procedure assured file transfer. Use the transfer log to find recurring flows that should move onto the accredited product. A downgrade that skips the second agent's review is a spillage, handled through the Response focus area's spillage response.

### NE-2.11: Industrial Protocol Filtering (DPI)

**Design Intent:** The ground segment firewall parses the command and control protocol the ground control stations use with the launch and recovery equipment. It allows only the commands each station is approved to send. The conduit to the data center carries file transfer for recordings and model packages and nothing else, so any control protocol traffic there is blocked and alerted. Fleet Operations and the Security Team tune the rules after each maintenance window.

**NIST Control Mapping:**

- **SC-7(17) (partial):** the enhancement names deep packet inspection that verifies application-layer protocol adherence, which industrial protocol inspection does. Protocol-Aware DPI Deployment provides the engine, Allowed Function Code/Command Allow-Listing sets the specification, and Unauthorized Command Blocking and Alerting enforces it. No other outcome claims it, and the SC-7 base is not reopened.
- **SC-7(18) (partial):** claimed for the deployment activity's per-point failure disposition, decided and recorded with the process owner. It is partial because a conduit whose loss would endanger the process fails open with compensating monitoring.
- **SI-4(4) (partial):** the function-code allow-list sets the criteria for unauthorized traffic, DPI Rule Tuning and False-Positive Management refines them, and Unauthorized Command Blocking and Alerting monitors and alerts against them. The other SI-4 claims elsewhere do not address traffic criteria.
- **Declined:** the AC-4 base stays with the segmentation outcomes that admit flows to a conduit. AC-4(8), AC-4(21), and AC-4(26) stay with Cross Domain Solution (CDS) Transfer Procedures and Unidirectional Gateways, while this outcome judges commands inside permitted flows.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Industrial Controller/SCADA

**External Dependencies:** The ground equipment manufacturers, who document the command sets their equipment accepts.

**Security Impact:** Moderate

**Activities:**

- **NE-2.11.1: Protocol-Aware DPI Deployment**
    - **Description:** Deploy inline deep packet inspection at each IT/OT conduit and boundary point carrying industrial traffic, loaded with parsers for the specific protocols in use so that every flow can be decoded and evaluated at the application layer rather than by address and port alone.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** This activity carries the mechanism dimension of the outcome's SC-7(17) (partial) mapping and its SC-7(18) (partial) mapping. Decide each inspection point's fail-open or fail-closed disposition with the process owner and record it in the CMP, since the safe failure mode depends on the process behind it. The timeline is Long-term because each insertion is negotiated against plant outage windows.

- **NE-2.11.2: Allowed Function Code/Command Allow-Listing**
    - **Description:** Enumerate per protocol and per source the function codes and commands each communicating party is sanctioned to issue, for example supervisory polling reads without the write, program-download, and device-mode codes, then permit only those and record the resulting allow-list in the CMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the specification dimension of the outcome's SC-7(17) (partial) mapping and the criteria half of its SI-4(4) (partial) mapping. Derive the sanctioned command set with the control and process engineers, and document it in the CMP. It is Documentation and event-driven as control logic and procedures change.

- **NE-2.11.3: Unauthorized Command Blocking and Alerting**
    - **Description:** Configure the inspection to drop any industrial protocol command falling outside the allow-list and to alert both the security operations team and the control-room operators, so an unsanctioned write, program download, or device-mode change is stopped at the conduit and surfaced while it is happening.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the enforcement dimension of the outcome's SC-7(17) (partial) mapping and the monitoring-and-alert dimension of its SI-4(4) (partial) mapping. It is tagged Automate because the engine decides at line rate. Route alerts to control-room operators as well as security operations, since only they can judge the physical consequence.

- **NE-2.11.4: DPI Rule Tuning and False-Positive Management**
    - **Description:** Review the blocks and alerts the inspection produces against observed legitimate process behavior, refine the rules to eliminate false positives without widening the sanctioned command scope, and record each tuning decision in the CMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the criteria-refinement dimension of the outcome's SI-4(4) (partial) mapping. Because a false positive can halt a physical process, run new rules in detection-only mode before blocking, and fix persistent noise rather than tolerate it. It is Level 2 and not tagged Automate, since tuning needs engineering judgment.

### NE-2.12: Ports, Protocols, and Services Matrix (PPSM)

**Design Intent:** Every port, protocol, and service crossing KESTREL's boundary is registered in the DoD PPSM registry and aligned to its Category Assurance List entry. These include the Boundary Cloud Access Point flows, the CSSP feed, the cross domain transfers, and the partner API. The approved baseline is the same policy-as-code rule base the hubs run, so the pipeline checks the deployed rules against the registration on every change. The Security Team recertifies the registration each year.

**NIST Control Mapping:**

- **CM-7(3) (partial):** the DoD PPSM process, with its CAL categories and per-boundary registration, is the registration requirement the enhancement names. Its registration, approval, and oversight dimensions are shared by the three PPSM activities. The CM-7 base is held elsewhere for what runs on hosts or services, while this outcome governs what crosses a boundary.
- **SI-4(22) (partial):** claimed for Boundary Enforcement Validation Against PPSM, which detects and alerts on unauthorized services reachable at a boundary. No other outcome claims it.
- **Declined:** CM-7(1) stays with Unapproved Service Usage Monitoring and Alerting and Insecure Services and Protocols, since recertification is registration oversight. The boundary controls this outcome records stay with the enforcement outcomes. CM-2 stays with Network Centralization and Standardization, and the CM-7 base with Platform Service Network Integration.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Network Infrastructure, Application/API, Compute, OT/ICS Device

**External Dependencies:** DISA's PPSM program, which maintains the registry and the Category Assurance List.

**Security Impact:** Moderate

**Activities:**

- **NE-2.12.1: PPSM Registration and CAL (category assurance list) Alignment**
    - **Description:** Register every port, protocol, and service that crosses a program boundary, record each entry's CAL assurance category together with the mitigation or configuration that category requires, and remediate or retire any entry the CAL restricts or prohibits in the program's usage context.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the registration dimension of the outcome's CM-7(3) (partial) mapping. It is Process, performed against the enterprise PPSM authority. It is event-driven as boundary crossings are added, changed, or retired.

- **NE-2.12.2: PPS Baseline Documentation and Approval**
    - **Description:** Publish the approved PPS baseline listing each registered port, protocol, and service with its boundary, its mission justification, and its approving authority, route it through the program's approval chain, and maintain it in the CMP as the authoritative statement of what may cross.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the approved-baseline dimension of the outcome's CM-7(3) (partial) mapping. Document it in the CMP. It governs what devices may expose across a boundary, while the CM-2 baseline governs how they are configured. It is event-driven as registrations change.

- **NE-2.12.3: Boundary Enforcement Validation Against PPSM**
    - **Description:** Compare the rules actually deployed on the program's firewalls, gateways, and service-edge policies against the approved PPS baseline on a continuous automated cycle, and alert on any port, protocol, or service found reachable at a boundary that the matrix does not authorize.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(22) (partial) mapping. It is tagged Automate because it compares what is actually reachable against the registered entries across every boundary device. Unlike Firewall/Routing Configuration Drift Detection and Alerting, it catches an unregistered service even on a correctly configured device.

- **NE-2.12.4: PPSM Periodic Review and Recertification**
    - **Description:** Revalidate every PPSM entry on the mandated cycle with its owning system or mission stakeholder, confirming the port, protocol, or service remains required, still satisfies its CAL category's mitigation, and still carries current approval, and remove the entries no longer justified.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the oversight dimension of the outcome's CM-7(3) (partial) mapping by retiring entries that no longer reflect the mission. It is not a CM-7(1) claim. It needs a stakeholder to confirm each entry, so it is not tagged Automate. Periodic (Annual) is a baseline the AO may shorten for higher-risk boundaries.

### NE-2.13: Authorized Cloud Access Point Integration

**Design Intent:** Every inbound flow from outside KESTREL's own sites reaches it only through the Boundary Cloud Access Point and then the cloud hub. That includes analysts, partners, performers, and the CSSP. The mission-owner stack behind it is the cloud hub's firewall and intrusion prevention, followed by the DMZ's edge services and WAF. Administration uses its own path through the VDI brokers and the privileged access workstations. KESTREL was registered with the access point's operator before it accepted traffic. DISA also approved the dedicated circuits to the data center and the alternate site as a direct connection.

**NIST Control Mapping:**

- **SC-7(4) (partial):** the designated access point is the enclave's only external interface, with its traffic flow policy and documented exceptions. Private Connectivity holds a disjoint slice.
- **SC-7(8) (partial):** the mission owner's boundary stack routes enclave traffic through authenticated proxies at the access point's inner edge. Network Firewall holds the slice for the program's own perimeter.
- **AC-17(3) (partial):** remote administration reaches the enclave through a dedicated management access control point. Secure Remote Access holds the other remote access paths.
- **SC-2 (partial):** Segregated Management Path keeps administration off the mission traffic path. Privileged Access Workstations and Administrative Tiering holds the device and tier slice.
- **Declined:** SC-7(5) and SC-7(21) stay with the segmentation outcomes. Provider and access point operator controls are inherited and verified by Inherited Control Validation.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Network Firewall, Load Balancer/Reverse Proxy/API Gateway, Web Application Firewall, Intrusion Detection/Prevention System (IDPS), Private Connectivity/Dedicated Circuit, Remote Access/VPN Gateway

**External Dependencies:** The Boundary Cloud Access Point, which DoD operates and which approves KESTREL's connection.

**Security Impact:** High

**Activities:**

- **NE-2.13.1: Designated Access Point Routing Enforcement**
    - **Description:** Configure the enclave's routing so every flow to and from external networks traverses the designated access point, and detect and remove any route, public address, or provider-native internet path that would let traffic bypass it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7(4) (partial) mapping. In cloud, a direct internet path is usually a convenience configuration, such as a public address on one resource. Check for it in the Device and Infrastructure configuration baselines and in the Security Impact Analysis (SIA) of any routing change.

- **NE-2.13.2: Mission-Owner Boundary Security Stack**
    - **Description:** Deploy the mission owner's boundary security stack between the access point and the workloads, covering traffic inspection, application-layer filtering, proxying of outbound traffic, and intrusion detection, and feed its telemetry to the program's monitoring and to its designated cyber defense service provider.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-7(8) (partial) mapping. It places the firewall, WAF, and intrusion detection functions defined elsewhere at the access point's inner edge rather than redefining them. Send its telemetry to both the program's detection and the provider from Cyber Defense Service Provider Alignment.

- **NE-2.13.3: Segregated Management Path**
    - **Description:** Administer the enclave only through a dedicated management path that is logically separate from the mission traffic path and reached through a managed access control point, and refuse administrative access arriving by any other route.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-17(3) (partial) and SC-2 (partial) mappings. Keeping management off the mission path means a compromised workload does not expose the enclave's administrative console. Privileged Credential Vaulting and Session Brokering still brokers and records the privileged sessions.

- **NE-2.13.4: Access Point Registration and Connection Approval**
    - **Description:** Register the enclave with the designated access point's operator, obtain the connection approval its authorization framework requires before the enclave accepts traffic, and keep the registration current as the enclave's addressing, services, and impact level change.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The access point operator enforces connection approval, and the lead time belongs on the schedule before the enclave is built. When the enclave's exposure changes, update the registration and the Ports, Protocols, and Services Matrix (PPSM) together, as flagged by the Security Impact Analysis (SIA).

## NE-3: Network Visibility

### NE-3.1: Network Telemetry and Security Posture Visualization

**Design Intent:** Cloud flow logs, the SDN fabric's flow telemetry, both hubs' logs, and the ground segment sensors all report to the security monitoring platform. Its network posture dashboard shows segmentation coverage, hub rule health, and DDoS and WAF alerts. The Platform Team, the Security Team, and the CSSP all read the same dashboard.

**NIST Control Mapping:**

- **SI-4 (partial):** claimed at the base for Centralized Network Telemetry and Analytics Platform, which establishes central network monitoring rather than a specific detection function. Other monitoring surfaces, such as Endpoint Detection, hold other slices, and the IDPS outcome holds SI-4(1). The dashboard presents posture other outcomes produce, so it adds no citation.
- **Declined:** AU-12 is not claimed, since the Operate pillar's Network Security Logging claims the records this platform carries.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Network Telemetry/Monitoring Platform

**External Dependencies:** The CSSP, which receives the same network telemetry by forwarding.

**Security Impact:** Moderate

**Activities:**

- **NE-3.1.1: Centralized Network Telemetry and Analytics Platform**
    - **Description:** Deploy the platform that centrally collects and analyzes network telemetry, namely flow logs, device logs, and traffic metadata, across the network estate as the program's network-monitoring capability.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is where the outcome's SI-4 (partial) mapping lands, cited at the base because it establishes the monitoring capability itself. The Operate pillar's SIEM and Detection focus area perform the analytics and response on top of it.

- **NE-3.1.2: Network Security Posture Dashboard**
    - **Description:** Build and maintain a dashboard that surfaces the program's network security posture, including segmentation coverage, firewall rule health, and DDoS/WAF alert status, as a single view for the PMO ISSE and network owners.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is tagged Visualize because it presents posture from drift detection, segmentation, DDoS Protection, and Web Application Firewall rather than producing it, so it claims none of their controls. Effort is Moderate because those inputs arrive on different schemas from cloud and on-premises sources and must be normalized. It is Level 2.

### NE-3.2: IDPS

**Design Intent:** Intrusion prevention runs on both hubs, blocking at the DMZ's inbound paths, the circuit, and the ground segment conduit. East-west rules between spokes start in alert mode and move to blocking as the Security Team tunes them. Rule sets cover the exposure KESTREL actually has, namely web applications, the partner API, identity services, and the protocols crossing the conduit.

**NIST Control Mapping:**

- **SI-4(1) (partial):** Cloud-Native Firewall Advanced Threat Protection Deployment connects each hub firewall's detection engine into the central telemetry platform, giving one correlated view. IDPS Signature Rules Selection and Signature Fine-Tuning configure its content. No other outcome claims SI-4(1), and Unpatchable/Legacy Asset Compensating Controls inherits this apparatus for virtual patching.
- **SI-4(7) (partial):** claimed for IDPS Mode Configuration, since deny mode drops a malicious session and reports it automatically. Endpoint Detection holds the disjoint host-process slice.
- **Declined:** SI-4(13) belongs to OT/Legacy Passive Monitoring's baseline profiling. No SC-7 claim is made, since the tier rides the existing hub firewall at the SC-7(3) access point. SI-3 stays with the Device and Infrastructure focus area's host anti-malware.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Intrusion Detection/Prevention System (IDPS), Network Firewall

**External Dependencies:** The CSSP, which supplies signatures and indicators drawn from its threat intelligence.

**Security Impact:** Moderate

**Activities:**

- **NE-3.2.1: Cloud-Native Firewall Advanced Threat Protection Deployment**
    - **Description:** License and activate the cloud-native firewall's advanced threat protection tier on each hub firewall so the existing boundary gains a signature-based intrusion detection and prevention engine, and connect its detections into the program's central network telemetry platform.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the mechanism dimension of the outcome's SI-4(1) (partial) mapping by linking each firewall's detection engine into one correlated view. The tier is a licensed add-on, so cost is recurring license and throughput charges. Review throughput before enabling deep inspection on an existing boundary.

- **NE-3.2.2: On-Premises IDPS Sensor Deployment**
    - **Description:** Deploy intrusion detection and prevention sensors at the program's own perimeters and at the interior segment boundaries whose traffic warrants inspection, position each one inline or on a tap according to whether the boundary can tolerate an inline failure, and connect every sensor's detections into the program's central network telemetry platform.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(1) (partial) mapping in the on-premises and disconnected estate, where independent sensors must be connected into one system-wide capability. Decide inline or tap per boundary, since an inline sensor's failure on mission traffic becomes an outage. Size coverage against the segmentation model, because interior boundaries are where lateral movement shows.

- **NE-3.2.3: IDPS Signature Rules Selection**
    - **Description:** Select the signature rule sets the engine evaluates traffic against, scoping them to the operating systems, application protocols, and threat classes the program actually exposes, and record the enabled set as the detection content the boundary is held to.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the configuration dimension of the outcome's SI-4(1) (partial) mapping. Scope rule sets to the deployed technology stack, since signatures for platforms the program does not run only add noise. It is event-driven as exposure and vendor content change.

- **NE-3.2.4: IDPS Mode Configuration**
    - **Description:** Decide per rule set whether a signature match is alerted or dropped, promoting rule sets into deny mode once their alert behavior is understood, so that in steady state a matching session is blocked and reported rather than only recorded.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(7) (partial) mapping, turning a signature match into an automated session drop. It is tagged Automate because the engine decides at line rate. Keep noisy rule sets in alert until Signature Fine-Tuning settles them, and record the promotion path and any alert-only rule sets in the CMP.

- **NE-3.2.5: Signature Fine-Tuning**
    - **Description:** Work through the engine's alert output on a recurring cycle, suppressing or narrowing the signatures that fire on known-good application behavior without surrendering coverage of the underlying threat class, and record each tuning decision in the CMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the keep-it-accurate dimension of the outcome's SI-4(1) (partial) mapping. Scope suppressions to the specific source, destination, or application rather than the signature globally, so tuning does not turn coverage off. It is Level 2 and not tagged Automate, since tuning is engineering judgment.

### NE-3.3: Trusted DNS Service

**Design Intent:** The cloud DNS resolvers and the data center DNS are KESTREL's only recursive resolvers, and hosts are allowed no other. Outbound queries are filtered by policy, and the resolvers validate DNSSEC. KESTREL's public names, one for each user-facing application, are hosted in the cloud provider's DNS service and signed. Resolver traffic across the circuit stays inside its encryption.

**NIST Control Mapping:**

- **SC-20 (partial):** claimed for Managed DNS Hosted Domains, which returns signed authoritative data and publishes delegation-signer records for the chain of trust. The base is cited because SC-20(2) covers internal queries, which Private DNS Service holds.
- **SC-21 (partial):** claimed for Secure DNS Deployment Guidelines, which has the resolver verify origin and integrity on responses. SC-21(1) was withdrawn into the base, and it is partial alongside the sibling SC-20 and SC-22 claims.
- **SC-22 (partial):** claimed for Managed DNS Service Selection, which provisions resolution redundantly and separates authoritative from recursive roles. SC-22 has no enhancements, and Custom DNS for Restricted Resolution holds the enclave slice.
- **Declined:** Managed DNS Firewall Rules opens no control, since DNS Advanced Protection owns malicious-domain blocking and Network Firewall holds SC-7(8). SI-4 is left to DNS Advanced Protection, the IDPS SI-4(1) view, and the Operate pillar. SC-8 is the Data focus area's, and Insecure Services and Protocols finds remaining cleartext resolution.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** DNS Infrastructure, Compute, Device/Workstation, Application/API

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization. The provider hosts KESTREL's public zone.

**Security Impact:** Moderate

**Activities:**

- **NE-3.3.1: Managed DNS Service Selection**
    - **Description:** Select the managed DNS service the program's resolution will run on, provision it redundantly across availability zones or regions, separate the externally-reachable authoritative role from the internal recursive-resolution role so that publicly answerable servers hold no internal-only records, and record the resulting resolution architecture in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-22 (partial) mapping. Redundant provisioning removes the single point of failure, and internal-only records stay in Private DNS Service's private zones rather than public ones. Document the architecture in the CMP. It is event-driven as the DNS footprint changes.

- **NE-3.3.2: Managed DNS Firewall Rules**
    - **Description:** Author the DNS firewall rule set that decides which focus areas the resolver will answer for, permitting the destinations the mission requires, denying the domain categories and named destinations program policy prohibits, and logging every allow and deny decision for review.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries no independent control citation, since DNS Advanced Protection owns malicious-domain blocking and Network Firewall holds SC-7(8). SC-7(5) is not reopened because a resolver works from policy lists rather than deny-by-default. It is standing enforcement, so it is not tagged Automate.

- **NE-3.3.3: Managed DNS Hosted Domains**
    - **Description:** Host the focus areas the program owns as authoritative zones on the managed service, sign each zone so its responses carry data origin authentication and integrity verification artifacts, and publish the delegation-signer records that let a resolver verify the chain of trust from the parent focus area into any child zone.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-20 (partial) mapping by signing hosted zones and publishing delegation-signer records. The Key Management Plan (KMP) governs zone-signing keys. It is event-driven as zones and delegations change.

- **NE-3.3.4: Secure DNS Deployment Guidelines**
    - **Description:** Enable signature validation on the program's recursive resolvers so every response accepted from an authoritative source is origin-authenticated and integrity-verified, require encrypted resolver transport on the paths that support it, prohibit hosts from bypassing the approved resolver, and record the resulting secure-DNS deployment standard in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-21 (partial) mapping through resolver validation of authoritative responses. Encrypted transport is the Data focus area's, not an SC-8 claim here. The bypass prohibition keeps hosts from sidestepping the SC-20 and SC-22 posture through an unapproved resolver.

### NE-3.4: Private DNS Service

**Design Intent:** Each spoke's private zone holds its internal names, and the private endpoint zones resolve every managed service to its endpoint. Each side's resolvers forward the other side's names across the circuit, so a circuit outage leaves local resolution working. Each operating site resolves only its own names and the IT/OT DMZ, through a local resolver pair, so a lost conduit leaves resolution working.

**NIST Control Mapping:**

- **SC-20(2) (partial):** this outcome is the program's internal authoritative source, through private resolution zones and private-endpoint zones. It is partial because managed private zones often cannot be signed, so integrity rests on being resolvable only inside the program's networks. Record any residual gap through the existing risk-acceptance workflow.
- **SC-22 (partial):** claimed for Custom DNS for Restricted Resolution, which builds redundancy from local resolvers in an enclave with no upstream. Managed DNS Service Selection holds the disjoint connected-estate slice.
- **Declined:** the SC-20 base stays with Trusted DNS Service for external queries. Private Connectivity's SC-7(4) claim is inherited, not reopened, since resolution only steers clients to its interface. SI-4 belongs to DNS Advanced Protection and IDPS.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** DNS Infrastructure, Compute, Storage/Database, Application/API

**External Dependencies:** The IL5 cloud provider, whose controls KESTREL inherits under its provisional authorization.

**Security Impact:** Moderate

**Activities:**

- **NE-3.4.1: Managed Private DNS for Private Resolution**
    - **Description:** Provision the managed private DNS zones that hold the program's internal-only records and link each zone to the virtual networks permitted to resolve it, so internal names are answered from inside the program's own networks and are never published to the public hierarchy.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the internal-zone dimension of the outcome's SC-20(2) (partial) mapping, scoping each zone to the networks entitled to it. Its applicability is narrower than the outcome's Deployment Type, since managed private zones are cloud and hybrid constructs. It is event-driven as namespaces and networks are onboarded.

- **NE-3.4.2: Managed Private DNS for Private Endpoints**
    - **Description:** Wire each private endpoint into its provider-specific private DNS zone and bind that zone to the resolving networks, so a platform service fronted by a private endpoint resolves to the endpoint's private address rather than to the service's public one.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the private-endpoint dimension of the outcome's SC-20(2) (partial) mapping and completes Private Connectivity's SC-7(4) claim without reopening it, since resolution is what sends clients to the endpoint. Private Network Endpoint Monitoring watches the posture set here. Its applicability is narrower than the outcome's Deployment Type, limited to cloud and hybrid.

- **NE-3.4.3: Custom DNS for Restricted Resolution**
    - **Description:** Build the custom resolver configuration for enclaves that can reach no public or cloud-managed resolver, standing up redundant local resolvers with internal root hints and conditional forwarders, denying any upstream path off the enclave, and documenting the resulting resolution architecture in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-22 (partial) mapping for an enclave with no reachable upstream. Redundant local resolvers give fault tolerance, and internal root hints make the internal role the only one. Document the architecture in the CMP. It is event-driven as the enclave namespace changes.

### NE-3.5: DNS Advanced Protection

**Design Intent:** Both sides' resolvers block known-malicious, newly registered, and algorithmically generated domains using a threat feed. Query logs go to the security monitoring platform, where analytics look for tunneling, beaconing, and exfiltration. Records are checked continuously against the asset inventory, so a record pointing at a removed resource is caught before someone else can claim the address.

**NIST Control Mapping:**

- **SI-4 (partial):** claimed at the base for the resolution layer. Managed DNS Threat Protection matches queries against attack indicators, and Dangling DNS Records Detection watches the program's zones for decommissioning residue. No enhancement describes resolver-level refusal, and no other SI-4 claimant observes name resolution.
- **SI-4(18) (partial):** claimed for Malicious DNS Activity Monitoring, since a resolver watching for tunneling and data in query names is interior analysis of a covert exfiltration channel. Data Loss Prevention (DLP) and Monitoring holds the disjoint egress-content slice.
- **Declined:** Both sibling DNS outcomes decline SI-4 so this one can claim it. SC-7(10) is not reopened, since DNS tunnels never form the TLS session it inspects. SC-20, SC-21, SC-22, and SC-20(2) stay with the sibling DNS outcomes. SI-4(7) does not fit preventive list-based blocking and is held elsewhere. SI-4(24) belongs to Endpoint Detection, and SI-4(1) to IDPS. CM-8 stays with Resource Decommissioning Governance, which Dangling DNS Records Detection feeds.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** DNS Infrastructure, Compute, Device/Workstation, Application/API

**External Dependencies:** A commercial threat feed service, pulled by zone transfer with no query data sent back. The CSSP, whose indicators load as a local policy zone.

**Security Impact:** Low

**Activities:**

- **NE-3.5.1: Managed DNS Threat Protection**
    - **Description:** Subscribe the program's resolvers to a managed DNS threat-protection feed and configure it to refuse resolution for the domains that feed classifies as known-malicious, newly-registered, or algorithmically generated, returning a sinkhole response rather than a silent failure so every blocked attempt stays attributable to the host that made it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the mechanism dimension of the outcome's SI-4 (partial) mapping by putting a detection decision in front of every query. It is tagged Automate because the feed updates continuously without manual curation. Sinkhole blocked queries so the host, domain, and time are preserved for investigation. Record the exception path for newly registered domains, and every exception granted, in the CMP.

- **NE-3.5.2: Malicious DNS Activity Monitoring**
    - **Description:** Analyze the resolvers' query telemetry for the behavioral signatures of DNS abuse, such as high-entropy or oversized labels, unusual record types, excessive subdomain cardinality beneath a single parent, and fixed-interval query rhythms, and raise an alert into the program's central network telemetry platform on each detection of tunneling, beaconing, or exfiltration.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(18) (partial) mapping, treating the resolver as the interior point and DNS tunneling as the covert channel. It is tagged Automate because query analysis at volume needs tools. Detections go to the Centralized Network Telemetry and Analytics Platform for Operate pillar triage. Suppress noisy detections for content delivery or telemetry services to the specific parent focus area only.

- **NE-3.5.3: Dangling DNS Records Detection**
    - **Description:** Reconcile every record in the program's authoritative and private zones against the resource it resolves to on a continuous cycle, and flag each alias, CNAME, or address record whose target has been deprovisioned or released so the record is retired before someone else can claim that target and answer for the program's name.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the attack-surface dimension of the outcome's SI-4 (partial) mapping and opens no inventory control. Route findings to Resource Decommissioning Governance under its CM-8 (partial) claim. A record pointing at a released resource lets whoever claims that name serve content or obtain a certificate under the program's subdomain. It is tagged Automate and sits at Level 2.

### NE-3.7: External Attack Surface Management

**Design Intent:** The Security Team watches KESTREL's public names and addresses continuously from outside, and it reviews what it finds against the inventory each month. KESTREL's source code is held on performer laptops, so the Security Team also watches public code hosting and paste sites for its code, secrets, and credentials. Each finding opens a service desk ticket to the owning team.

**NIST Control Mapping:**

- **RA-5(4) (full):** the two discovery activities determine what is discoverable from outside, and Exposure Finding Remediation Tracking drives the corrective actions. No other outcome claims it. The RA-5 base is held for inside-out scanning of known assets, while this outcome finds what those scans never targeted.
- **AU-13 (partial), AU-13(1) (partial):** claimed for Leaked Credential and Exposed Secret Monitoring, which watches external public sites with automated mechanisms. It is the external counterpart Secrets and Credentials Detection anticipated. Both are partial because credentials are only one class of disclosed information.
- **Declined:** CM-8(3) and CM-8 are not claimed, since unrecorded assets feed Asset Management's discovery process and resources that should be retired go to Resource Decommissioning Governance.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Storage/Database, Application/API, Network Infrastructure, Identity Platform

**External Dependencies:** The CSSP, which reports external exposures and leaked credentials it sees in its threat intelligence.

**Security Impact:** High

**Activities:**

- **NE-3.7.1: Internet-Facing Asset and Exposure Discovery**
    - **Description:** Continuously enumerate, from outside the program's own networks, the domains, subdomains, address ranges, certificates, and exposed services attributable to the program, and reconcile that outside-in view against the authoritative inventory so that anything present externally but unrecorded internally is investigated.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the discoverable-information half of the outcome's RA-5(4) (full) mapping. Attribution is the hard part, since any asset under a program domain, certificate, or address block belongs to the program whether recorded or not. Feed unrecorded components to Asset Inventory and Discovery, and retired-but-reachable ones to Resource Decommissioning Governance. It is tagged Automate and sits at Level 2.

- **NE-3.7.2: Shadow IT and Unsanctioned Cloud Resource Discovery**
    - **Description:** Identify the cloud subscriptions, tenants, storage buckets, and internet-facing services that were stood up outside the program's approved provisioning path, and bring each either under the program's inventory and governance or into decommissioning.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity contributes to the discoverable-information half of the outcome's RA-5(4) (full) mapping for infrastructure. SaaS Application Discovery and Security Posture Management (CASB) finds applications from identity telemetry, while this finds compute and storage no provisioning workflow touched. Route governed resources through Secure Resource Provisioning and unneeded ones to Secure Decommissioning Procedures. It is tagged Automate and sits at Level 2.

- **NE-3.7.3: Leaked Credential and Exposed Secret Monitoring**
    - **Description:** Monitor the external sources where organizational credentials and secrets surface after a leak, such as paste sites, breach and combolist dumps, public code repositories, and criminal marketplaces, for material attributable to the program, and drive every confirmed exposure into immediate revocation and rotation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-13 (partial) and AU-13(1) (partial) mappings. It is the external counterpart to Secrets Exposure Monitoring, which watches internal surfaces. Remediation runs through the Identity focus area's account controls and Secrets and Credentials Protection, so no IA-5 claim is opened. Recurring cost is Moderate because this is usually a subscription service.

- **NE-3.7.4: Exposure Finding Remediation Tracking**
    - **Description:** Track every exposure this outcome surfaces from discovery through closure by assigning it an owner, a corrective action, and a due date drawn from the remediation service levels the VPMP sets, and escalate the findings that pass it.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the corrective-action half of the outcome's RA-5(4) (full) mapping. Measure against the timeframes in the Vulnerability and Patch Management Plan (VPMP), and disposition exposures that miss them through Exception and Risk Acceptance Workflow under its RA-7 (partial) claim. It is Process and not tagged Automate.

### NE-3.8: OT/Legacy Passive Monitoring

**Design Intent:** The ground segment's passive sensors build a profile of normal traffic for each zone, and deviations alert Fleet Operations and the Security Team. The sensors never act on traffic or devices. Each maintenance window that changes equipment ends with a re-profiling, so the new configuration becomes the baseline.

**NIST Control Mapping:**

- **SI-4(13) (partial):** Passive Network Baseline Profiling develops traffic profiles, Anomaly Detection Rule/Model Tuning uses them to tune monitoring, and Baseline Re-Profiling After Authorized Change keeps them current. GNSS/PNT Spoofing and Jamming Detection holds the PNT slice.
- **SI-4(5) (partial):** claimed for Anomaly Alerting and Operator Notification, which alerts personnel without an automated response. SI-4(7) would require terminating the event, which could itself cause a safety consequence on a live process. Endpoint Detection's EDR Passive/Audit Mode and others hold slices for other system classes.
- **Declined:** SI-4(7) is held elsewhere and would act on a live process. The SI-4 base is not reopened, the same discipline Network Firewall applies to SC-7. SI-4(11) covers outbound traffic at external interfaces rather than interior OT conversations. SI-4(4) stays with Industrial Protocol Filtering (DPI), which enforces inline. CM-6 stays with OT Baseline Configuration Drift Detection, and CM-8 and CM-8(3) with OT/Legacy Passive Protocol-Aware Discovery. AU-6 does not fit an alert raised at detection. This outcome feeds Zone-to-Zone Data Flow Monitoring.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** OT/ICS Device, OT/ICS Passive Network Monitoring, Device/Workstation

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **NE-3.8.1: Passive Network Baseline Profiling**
    - **Description:** Observe each OT and legacy segment from the passive taps already listening to it across a full operational cycle, and develop a profile of the traffic and event patterns that segment normally exhibits, covering its conversing pairs, protocols and function codes, message rates, and periodicity.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the analyze-and-develop dimensions of the outcome's SI-4(13) (partial) mapping. Span a full operational cycle, including shift changes and scheduled maintenance, or a legitimate quarterly pattern will alert every time it recurs. Reuse the existing taps and stay strictly read-only, since active scanning can crash this equipment. It is tagged Automate.

- **NE-3.8.2: Anomaly Detection Rule/Model Tuning**
    - **Description:** Tune the passive monitoring platform's detection rules and statistical models against the developed profile so that departure from the learned normal is what registers as an anomaly, and record each tuning decision and its sensitivity setting in the CMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the third part of the outcome's SI-4(13) (partial) mapping, using the profiles to tune monitoring. It sits at Level 2 because the control is outside the Moderate baseline, but an untuned profile detects nothing, so a program relying on this detection treats tuning as mandatory. Set sensitivity with control engineers, since operators ignore a console that cries wolf.

- **NE-3.8.3: Anomaly Alerting and Operator Notification**
    - **Description:** Alert the control-room operators and the security operations team whenever observed traffic departs from the profiled baseline, carrying the deviating conversation and its process context in the alert, and take no automated action against the traffic, the device, or the process.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(5) (partial) mapping, which ends at notification. No session is dropped, no port shut, and no device isolated. Route alerts to control-room operators as well as security operations, since only they can tell an intrusion from an unrecorded process adjustment. It is tagged Automate for alert generation only.

- **NE-3.8.4: Baseline Re-Profiling After Authorized Change**
    - **Description:** Re-develop the affected segment's profile after each authorized change to the process, control logic, or device population, triggered by the approved change record itself, so that the new normal becomes the baseline instead of a standing source of false anomalies.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the re-development dimension of the outcome's SI-4(13) (partial) mapping. Trigger re-profiling only from an approved CMP change record, never from alert noise, or the profile may absorb an intrusion into normal. It is event-driven and Level 2.

### NE-3.9: GNSS/PNT Spoofing and Jamming Detection

**Design Intent:** Each aircraft's GNSS receiver reports signal and solution quality, which is profiled per aircraft and compared with its inertial navigation. Each station compares its GNSS timing with a local holdover reference. It also checks against the data center's time source whenever the conduit is up. Indicators of spoofing or jamming alert the operator at the station during flight and reach the Security Team through the security monitoring platform.

**NIST Control Mapping:**

- **SI-4(13) (partial):** PNT Signal Profiling and Spoofing/Jamming Indicator Detection profiles receiver-reported metrics such as satellite geometry, carrier-to-noise ratio, and gain control. Cross-Source PNT Consistency Validation profiles divergence from an independent inertial reference. OT/Legacy Passive Monitoring holds the separate OT traffic slice.
- **SI-4(5) (partial):** claimed for Spoofing/Jamming Alerting and Operator Notification, which alerts personnel without a response obligation. Endpoint Detection's EDR Passive/Audit Mode and others hold slices for other system classes.
- **Declined:** SI-4(7) is not claimed, since an automated receiver reset or source switchover in flight could cause the harm monitoring exists to prevent. SC-5 does not fit external RF jamming, which SI-4(5) already captures. SA-8 belongs to the platform's design-time engineering. SC-45, SC-45(1), and SC-45(2) stay with Time Synchronization, which trusts its source rather than testing it. CP-12 belongs to whatever outcome builds a PNT-loss safe mode. Anti-spoofing hardware, like SR-9(1) anti-tamper work, is out of scope.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Industrial Controller/SCADA, OT/ICS Passive Network Monitoring, Network Telemetry/Monitoring Platform, Device/Workstation

**External Dependencies:** The aircraft manufacturer, whose receivers report the signal quality data this profiling uses.

**Security Impact:** High

**Activities:**

- **NE-3.9.1: PNT Signal Profiling and Spoofing/Jamming Indicator Detection**
    - **Description:** Observe each platform's GNSS receiver-reported signal and solution-quality metrics (satellite count and geometry, carrier-to-noise ratios, automatic gain control level, and position, velocity, and clock-bias jump magnitude) across normal operation, develop a profile of what those metrics look like when the signal is genuine, and tune detection thresholds so a departure consistent with spoofing or jamming registers as an indicator.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the profile-and-tune dimensions of the outcome's SI-4(13) (partial) mapping for receiver output. It reads only the receiver's standard status interface and never reconfigures it. Effort is High and the timeline Medium-term because profiling spans varied receivers across a fleet. It is tagged Automate.

- **NE-3.9.2: Cross-Source PNT Consistency Validation**
    - **Description:** Continuously compare the GNSS-derived position, velocity, and time against the platform's independent onboard reference, such as an inertial navigation system or other non-GNSS sensor, and flag divergence beyond the tolerance the platform's own navigation error model predicts as an additional spoofing or jamming indicator.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the second slice of the outcome's SI-4(13) (partial) mapping for cross-sensor consistency. It is Level 2 because it needs an independent reference sensor, which is a platform design decision. Read the tolerance from the platform's navigation error model rather than deriving it. DOT and DHS/CISA PNT guidance inform the independent-reference concept.

- **NE-3.9.3: Spoofing/Jamming Alerting and Operator Notification**
    - **Description:** Alert the platform operator and any integrated platform contingency system the moment either the signal-profile check or the cross-source consistency check departs from its baseline, carrying the deviating metric and its magnitude in the alert, and take no automated action against the receiver, the antenna, or the navigation system.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(5) (partial) mapping, alerting a person and any integrated contingency system without commanding the receiver or navigation system. It is tagged Automate for alert generation only. Where the platform implements a degraded-navigation mode, validate its readiness the way Rollback/Kill-Switch Readiness Check does.

## Scoped Out

These outcomes drop out of KESTREL's design, each for the reason given.

| Outcome | Reason |
|---|---|
| NE-2.9: Unidirectional Gateways | Out of scope by design. The ground segment conduit carries traffic both ways, namely recordings out (F3) and certified edge models in (F6), so a firewalled conduit with protocol inspection protects it instead of a data diode. |
| NE-3.6: Native Email Messaging Service | Out of scope. KESTREL runs no email service, and the AO approved removing SI-8 (CCSD tailoring action 1). |
