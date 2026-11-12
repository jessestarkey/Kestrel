# ID: Identity

*KESTREL SADD, Section 5 (Protect). See the [index](index.md) for the document-wide sections. Outcome metadata and activity fields are carried from the SABER unchanged. Design Intent and External Dependencies are written for KESTREL.*

## ID-1: Identity Platform and Management

### ID-1.1: Identity Proofing and Enrollment

**Design Intent:** Proof every person before KESTREL issues an account, at the assurance level the AMP sets for each population. DoD users are proofed through their CAC issuance, so KESTREL binds them to that record rather than re-proofing them. Operators and platform administrators sit at the highest assurance level, since they can command aircraft or change the boundary.

**NIST Control Mapping:**

- **IA-12 (full):** Identity Assurance Level Determination, Sponsor/Nomination and Identity Verification, and Binding to Authoritative Source deliver the base proofing requirement jointly.
- **IA-12(1) (full):** Sponsor/Nomination and Identity Verification makes an authorized sponsor a condition of registration.
- **IA-12(2) (partial):** This claim narrows to the identity-evidence collection step of Sponsor/Nomination and Identity Verification.
- **IA-12(3) (partial):** This claim narrows to the identity-evidence validation step of the same activity.
- **IA-4 (partial):** only the identifier-assignment portion of this outcome, Binding to Authoritative Source, exercises this control.
- **IA-4(4) (full):** Contractor and Foreign National Identifier Marking marks each identifier with the subject's contractor, foreign national, or non-organizational status.
- **AC-2(1) (partial):** Provisioning-on-Enrollment Automation automates creating the baseline account when enrollment completes. Account Lifecycle and Identity Data Quality holds the rest of the account lifecycle.
- **IA-12(5) (full):** Address Confirmation sends a registration code or notice of proofing to the address of record out of band.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Identity Lifecycle and Governance

**External Dependencies:** DoD PKI CAC issuance, which proofs DoD users before they reach KESTREL.

**Security Impact:** High

**Activities:**

- **ID-1.1.1: Identity Assurance Level Determination**
    - **Description:** Determine the Identity Assurance Level (IAL1, IAL2, or IAL3) each identity population requires from the consequences of an identity-proofing failure for that population, following the digital identity risk assessment NIST SP 800-63 prescribes, and document the determination criteria in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The IAL sets how rigorously the program proves who a subject is, while the AAL sets how strongly that subject authenticates. Assurance-Level-to-Resource-Sensitivity Mapping selects the AAL separately, and both values are recorded side by side in the AMP.

- **ID-1.1.2: Sponsor/Nomination and Identity Verification**
    - **Description:** Verify each subject's claimed identity through an authorized sponsor or nomination together with corroborating evidence commensurate with the assigned assurance level.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)

- **ID-1.1.3: Binding to Authoritative Source**
    - **Description:** Bind each vetted identity to the program's authoritative system of record so that every downstream credential and entitlement derives from a single trusted anchor.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is tagged Automate because binding runs as a tool-enforced integration with the authoritative source. If a program binds manually, remove the tag and set Control Type to Process. Authoritative Source Synchronization keeps the anchor current after enrollment.

- **ID-1.1.4: Contractor and Foreign National Identifier Marking**
    - **Description:** Mark each individual's identifier with the status characteristics the program must be able to distinguish, such as contractor, foreign national, and non-organizational user, at the moment the identity is bound to the authoritative source, and document the status taxonomy and its marking convention in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-4(4) (full) mapping. The marking is an attribute on the authoritative record, so it propagates through Authoritative Source Synchronization with every other attribute. Access reviews, external-user scoping, and releasability decisions all depend on it, and a status change is one of the Re-Proofing Triggers conditions.

- **ID-1.1.5: Provisioning-on-Enrollment Automation**
    - **Description:** Automatically create and enable a subject's baseline account and access the moment enrollment completes its assurance determination, verification, and binding steps, without waiting on manual account setup.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity mirrors Deprovisioning-on-Termination Automation on the joiner side. It provisions baseline access only, while Identities and Entitlements Lifecycle assigns entitlements beyond that baseline.

- **ID-1.1.6: Re-Proofing Triggers**
    - **Description:** Define the events and time-based conditions that trigger re-proofing of an identity, such as a role change, an elevation of access sensitivity, or a credential lifecycle milestone, and document them in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is Level 1 because sustained assurance is inseparable from the initial proofing decision. Downgrade it to Level 2 if the AO accepts one-time proofing. When a trigger fires, re-proofing re-runs the existing proofing and binding activities rather than a separate one.

- **ID-1.1.7: Address Confirmation**
    - **Description:** Confirm each subject's address of record by delivering a registration code or notice of proofing to that address through a channel separate from the proofing session, and document the confirmation channels and code validity period in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-12(5) (full) mapping. Remote proofing requires the subject to return the code before enrollment completes, while in-person proofing sends a notice instead. The address always comes from the authoritative source, never from details the subject supplies in the same session.

### ID-1.2: External PKI Trust and Sponsorship

**Design Intent:** Admit vendor support engineers on External Certificate Authority credentials from the first build, and coalition partners on ECA or federated partner PKI credentials once they onboard, each under a named KESTREL sponsor. Partner identities map only to partner API roles and vendor identities only to their support cases, and every external credential is revocation-checked at each session. The trust list names each partner nation's issuing authorities, and adding a partner nation is a CCSD revision trigger.

**NIST Control Mapping:**

- **IA-8 (full):** The outcome satisfies non-organizational-user authentication broadly, across both PIV and non-PIV partner-agency credentials.
- **IA-8(1) (partial):** This claim covers specifically the PIV/CAC federation case named in this outcome's description.
- **IA-8(2) (partial):** External PKI Trust Chain Management and Partner Identity Provider Federation Trust Management maintain the list of accepted external issuers. The rest, the compliance criteria, comes from Phishing-Resistant Authenticator Selection (PIV/CAC/FIDO2).
- **IA-8(4) (full):** Partner Identity Provider Federation Trust Management fixes the identity management profiles for interoperating with mission partners. SSO Protocol Configuration Hardening covers organizational users separately under SI-10.
- **IA-8(5) (full):** External PKI Trust Chain Management sets the acceptable anchors, including the Federal PKI bridge, and External Credential Validation and Revocation Checking verifies credentials against them.
- **IA-12(6) (full):** External User Sponsorship and Local Identity Binding accepts the external issuer's proofing at the level Identity Assurance Level Determination sets.
- **IA-5(2) (partial):** This outcome holds only the external-issuer side of PKI authentication. Credential Status Checking (OCSP/CRL) holds the internal PIV/CAC side, and Certificate-Based Credentials holds the non-person-entity side.
- **AC-2 (partial):** Only the external-user slice of account management lives here, and no AC-2 enhancement fits sponsored external accounts. Account Lifecycle and Identity Data Quality holds the rest.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** PKI/Certificate Authority, External/Federated Trust

**External Dependencies:** DoD PKI, External Certificate Authorities, and each partner nation's PKI or identity provider, under the memoranda of agreement listed in the system description.

**Security Impact:** High

**Activities:**

- **ID-1.2.1: External PKI Trust Chain Management**
    - **Description:** Establish and maintain the set of trusted external certificate authorities and cross-certification paths, such as the Federal PKI bridge or partner-agency roots, against which externally issued credentials are validated.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-8(2) (partial) mapping and the policy half of its IA-8(5) (full) mapping. It decides which external credentials may be presented before External Credential Validation and Revocation Checking verifies any. In an Air-Gapped/Isolated deployment, anchors come from offline-distributed trust material.

- **ID-1.2.2: External Credential Validation and Revocation Checking**
    - **Description:** Validate externally issued credentials at authentication time by verifying the certificate path to a trusted anchor and confirming revocation status against the issuer's OCSP responder or CRL.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-8(5) (full) mapping together with External PKI Trust Chain Management. It mirrors Credential Status Checking (OCSP/CRL) for externally issued credentials. In an Air-Gapped/Isolated deployment, it falls back to offline CRLs or cached revocation data, as PIV-Denied and Degraded-Connectivity Fallback defines.

- **ID-1.2.3: Partner Identity Provider Federation Trust Management**
    - **Description:** Establish each mission-partner federation trust by exchanging and pinning the partner identity provider's metadata, scheduling its signing-certificate rollover ahead of expiry, transforming the partner's asserted claims into the program's own attribute namespace, and filtering out any claim the partner is not authorized to assert about its own subjects.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-8(4) (full) mapping and contributes to its IA-8(2) (partial) one. It decides whose assertions the program believes, while External PKI Trust Chain Management decides whose certificates it validates. Partner claims are mapped into a program namespace and anything outside the agreed set is dropped, since a passed-through role claim lets the partner grant access. Signing-certificate rollover is scheduled because an expired partner certificate is the most common way a federation breaks. It does not apply in an Air-Gapped/Isolated deployment, which has no connectivity to a partner identity provider.

- **ID-1.2.4: External User Sponsorship and Local Identity Binding**
    - **Description:** Require an authorized local sponsor to vouch for each external user and bind the externally authenticated identity to a local identity record in the program's identity platform.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-12(6) (full) mapping. It accepts the external issuer's proofing under local sponsorship, at the assurance level Identity Assurance Level Determination sets, and binds the result to the authoritative source.

- **ID-1.2.5: External User Access Authorization Mapping**
    - **Description:** Map each sponsored external user to a constrained set of roles and entitlements appropriate to the partner relationship, applying least privilege more conservatively than for internal users.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** External roles come from the same role and group model as Non-Privileged Access Control. This activity governs which of those roles an external user may hold and how tightly they are scoped.

- **ID-1.2.6: External User Access Review and Revocation**
    - **Description:** Review external users' access on a defined cadence and promptly revoke local identity bindings and entitlements when the sponsoring relationship or partner engagement ends.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** External-user reviews use the Access Reviews campaign machinery, but monthly rather than quarterly and with sponsor re-attestation, since the program does not administer these subjects directly.

### ID-1.3: Centralized Identity Platform

**Design Intent:** The on-premises identity provider and directory in the mission data center is KESTREL's one identity system of record. It serves the IL5 cloud over the dedicated circuit, so identity keeps working for the data center and the fleet if the cloud is unreachable. Separate administrative units keep each team's identities apart, along with partner, operator, and platform administrator identities.

**NIST Control Mapping:**

- **IA-2 (full):** mapped at the base-control level as the platform's core purpose, identifying and authenticating organizational users.
- **AC-2 (partial):** This outcome provides the platform accounts live on, not the account lifecycle. The rest is held by Account Lifecycle and Identity Data Quality and Access Reviews.
- **Declined:** IA-2(1), IA-2(2), and related multi-factor and authenticator-strength enhancements are tailored downstream under User Authentication Controls rather than claimed at platform stand-up.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Directory/Platform Core Infrastructure

**External Dependencies:** None outside the boundary. The identity provider is program-owned.

**Security Impact:** High

**Activities:**

- **ID-1.3.1: Identity Platform Adoption**
    - **Description:** Select and stand up the program's centralized identity platform as the authoritative system of record, consolidating existing fragmented identity stores onto it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Extensive
    - **Cost:** One-Time: High; Recurring: High
    - **Time Estimation:** Long-term (6+ months)
    - **Supplemental Guidance:** Identity Platform Threat Detection and Hardening handles hardening after adoption. Level of Effort is Extensive because consolidating identity stores reaches every system that consumes identity. Recurring Cost is High because the platform license is a standing line item.

- **ID-1.3.2: Identity Organization and Segmentation Strategy**
    - **Description:** Define how identities, tenants, organizational units, and administrative boundaries are structured within the platform to enforce least privilege, delegated administration, and blast-radius containment.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)

### ID-1.4: Identity Platform Threat Detection and Hardening

**Design Intent:** Treat the identity provider as the asset whose loss would hand an adversary the command link, and watch it accordingly. Identity threat detection feeds the security monitoring platform, and the provider is hardened to its DISA STIG.

**NIST Control Mapping:**

- **SI-4(2) (partial):** Identity Platform Protection Tool Deployment analyzes identity-platform activity for compromise in real time. It is partial because it covers only the identity-platform slice, alongside Platform-Native Threat Detection and others.
- **CM-6 (partial):** Identity Platform Protection Tool Hardening applies the platform's baseline manually, so the base control fits rather than CM-6(1). Directory and Tier 0 Infrastructure Hardening holds the separate on-premises slice.
- **Declined:** AC-3(12) belongs to Application Consent Control (OAuth/SaaS) under Third-Party Application and SaaS Access Governance, which owns the admin-consent gate.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Directory/Platform Core Infrastructure

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **ID-1.4.1: Identity Platform Protection Tool Deployment**
    - **Description:** Deploy identity threat detection and response tooling that monitors the identity platform for compromise indicators such as anomalous sign-ins, token theft, consent-grant abuse, and privilege-escalation attempts.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Session Risk Scoring and the Adaptive, Risk-Based Access Control outcome consume this tooling's risk signals and turn them into access-time enforcement.

- **ID-1.4.2: Identity Platform Protection Tool Hardening**
    - **Description:** Harden the identity platform's own configuration against a recognized secure-configuration baseline, covering its authentication and token policies, administrative role assignments, legacy-protocol disablement, and tenant security defaults.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity delivers the hardening Identity Platform Adoption defers to this outcome, scoped to the platform's tenant-level settings. Directory and Tier 0 Infrastructure Hardening covers the on-premises directory, CA, and synchronization servers, so a hybrid program applies two baselines to two systems.

### ID-1.5: Directory and Tier 0 Infrastructure Hardening

**Design Intent:** Harden the directory, its domain controllers, and the PKI's issuing certificate authorities as Tier 0. The root certificate authority and its keys sit in the HSMs that hold CCSD row 13's key material, so this outcome protects KESTREL's one High confidentiality type directly. Directory synchronization to the cloud runs only over the dedicated circuit.

**NIST Control Mapping:**

- **CM-6 (partial):** Directory Service Configuration Hardening, Certificate Authority Infrastructure Hardening, and Hybrid Identity Synchronization Infrastructure Hardening apply identity-role settings on top of the inherited host baseline. Identity Platform Threat Detection and Hardening holds the separate tenant-level slice.
- **IA-5 (partial):** Tier 0 and Local Administrator Credential Rotation refreshes tier 0 key material and service-account authenticators on a defined period. Credential Management holds the person-entity slice, and Eradication and Threat Removal holds compromise-triggered refresh.
- **Declined:** CM-7(1) belongs to Insecure Services and Protocols, while this outcome only makes the directory refuse legacy protocols. AC-6 is not claimed, since the delegation constraints are a directory setting CM-6 already covers rather than AC-6 privilege right-sizing. SC-17 stays with Server and Services Authentication and the Data focus area's certificate outcomes, since this outcome hardens the CA host rather than certificate policy.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Directory/Platform Core Infrastructure, PKI/Certificate Authority, Virtual Machine/Server, Cryptographic Hardware/HSM, Device/Workstation

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **ID-1.5.1: Directory Service Configuration Hardening**
    - **Description:** Harden the directory and its domain controllers against the program's recognized configuration baseline by requiring LDAP signing and channel binding, refusing legacy authentication protocols and cipher suites, removing or constraining Kerberos delegation on every account that does not demonstrably require it, restoring and protecting the permissions AdminSDHolder propagates, and enabling SID filtering on every directory trust.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the greater part of the outcome's CM-6 (partial) mapping. Each setting closes a path that defeats other controls, namely unconstrained delegation, relayed authentication over unsigned LDAP, and trusts without SID filtering. It is Event-Driven because the settings are revisited when topology, trusts, or forest functional level change.

- **ID-1.5.2: Certificate Authority Infrastructure Hardening**
    - **Description:** Constrain the certificate authority that issues the program's credentials by keeping its root offline, protecting issuing-CA key material in a hardware security module, restricting who may enroll or act as an enrollment agent, and reviewing every certificate template for enrollment permissions and subject-name settings that would let a requester obtain a certificate naming an identity other than its own.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's CM-6 (partial) mapping. It covers the CA as a tier 0 host and its enrollment configuration, while the Data focus area owns certificate policy and lifecycle. Template review matters most, since a template that lets a requester supply its own subject name mints valid privileged certificates. The HSM draws on the Data focus area's key management infrastructure.

- **ID-1.5.3: Hybrid Identity Synchronization Infrastructure Hardening**
    - **Description:** Treat the servers that synchronize an on-premises directory to a cloud identity provider, along with the connector and agent accounts they run under, as tier 0 assets by restricting administrative access to them at the directory's own tier, removing the standing directory permissions the connector does not require, and monitoring them for the credential-extraction attempts their two-sided access invites.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's CM-6 (partial) mapping. The synchronization server holds working credentials for both sides of a hybrid estate, so its compromise defeats the tier separation Tiered Credential Isolation Enforcement maintains. Its monitoring reuses Identity Platform Protection Tool Deployment telemetry, so it opens no SI-4 claim. It applies only in a Hybrid deployment, narrower than the outcome's union.

- **ID-1.5.4: Tier 0 and Local Administrator Credential Rotation**
    - **Description:** Rotate the tier 0 credentials whose compromise would otherwise survive remediation by rotating the directory's krbtgt key twice with at least one full replication interval between rotations, refreshing directory, connector, and certificate-authority service-account credentials on a defined cadence, and randomizing each host's local administrator password to a unique value retrieved from a protected store, and document the rotation cadences in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the whole of the outcome's IA-5 (partial) mapping. The krbtgt key is rotated twice, a replication interval apart, because one rotation leaves the old key valid. Unique local administrator passwords close the lateral path that crosses no tier boundary, and they are retrieved from the vault Privileged Credential Vaulting and Session Brokering governs where one exists. ConMon Activity records the semi-annual krbtgt and service-account rotation.

### ID-1.6: Third-Party Application and SaaS Access Governance

**Design Intent:** KESTREL admits no third-party OAuth or SaaS application to its identities by default. A foundation model the cloud provider hosts inside KESTREL's tenant receives no delegated user access, so it is not a third-party application in this outcome's sense. Discovery runs against IL5 production egress to catch any other service in use.

**NIST Control Mapping:**

- **AC-3(12) (partial):** Application Consent Control (OAuth/SaaS) is a direct instance, since applications declare delegated access, the platform blocks unverified ones, and expansion needs fresh approval. Application Control holds the endpoint half through CM-7(5).
- **SI-4(2) (partial):** The broker's continuous analysis of which SaaS applications organizational identities reach is a disjoint slice, alongside Identity Platform Threat Detection and Hardening's platform slice.
- **Declined:** CM-6 covers baselines on systems the program operates, while SaaS posture findings go to the tenant's owner for remediation.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** External/Federated Trust

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-1.6.1: Application Consent Control (OAuth/SaaS)**
    - **Description:** Govern which third-party OAuth and SaaS applications may obtain delegated access to organizational identities and data by requiring administrative consent and restricting or blocking unverified or over-permissioned applications.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-3(12) (partial) mapping, realizing all three clauses at the OAuth consent gate. It requires an application to declare its delegated access, blocks unverified or over-permissioned grants, and requires fresh approval before scope expands. SaaS Application Discovery and Security Posture Management (CASB) instead finds what is already in use.

- **ID-1.6.2: SaaS Application Discovery and Security Posture Management (CASB)**
    - **Description:** Deploy a cloud access security broker to discover which sanctioned and unsanctioned SaaS applications organizational identities are actually signing in to and moving data through, and to assess and drive remediation of the security posture of the SaaS tenants the program depends on.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4(2) (partial) mapping. The broker continuously analyzes which applications organizational identities reach and what data moves through them, one hop beyond the platform. Unlike Application Consent Control (OAuth/SaaS), it finds what is already in use and judges each tenant's configuration. It is Level 3 because the mandatory identity-platform protections sit under Identity Platform Threat Detection and Hardening.

### ID-1.7: Identities and Entitlements Lifecycle

**Design Intent:** Build entitlements as bundles for each user role in the system description, scoped to the team that role belongs to. Analysts get their own mission team's raw collection and detections, and every team gets the shared reports. IT Operations provisions accounts, but the approval comes from the requester's product owner or team lead, so no one approves and provisions the same access. Approving an AI agent's actions is an entitlement in the bundle of the role that approves them, so each approval can be reviewed rather than reached by anyone. Today that is the operator bundle, which approves the mission-planning agent's drafts.

**NIST Control Mapping:**

- **AC-2 (partial):** This outcome owns the entitlement-management and workflow slice of account management. Account Lifecycle and Identity Data Quality and Centralized Identity Platform hold the rest.
- **AC-2(6) (partial):** Permissions Management continuously analyzes and right-sizes effective permissions (CIEM). Access Reviews holds the periodic recertification of the same entitlements.
- **AC-6 (partial):** Permissions Management right-sizes effective permissions, including cloud entitlements. Non-Privileged Access Control holds the default-deny floor.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Storage/Database, Identity Lifecycle and Governance

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-1.7.1: Entitlement Management**
    - **Description:** Establish and maintain the catalog of entitlements that identities can hold, such as access packages, resource roles, and group memberships, bundling raw permissions into governable, assignable units.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Entitlements are built on the role and group model that Non-Privileged Access Control and Privileged Access Control define. This activity packages those roles and groups without redefining them.

- **ID-1.7.2: Entitlement Lifecycle Workflows**
    - **Description:** Implement the request, approval, and change workflows through which identities acquire, modify, and relinquish entitlements over time, routing approvals to accountable resource owners.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** These workflows govern standing, longer-lived entitlement changes. The Just in Time Access outcome's Activation Workflows handle time-bound elevation of privileged entitlements separately, outside this standing-access request path.

- **ID-1.7.3: Permissions Management**
    - **Description:** Continuously analyze and right-size the effective permissions granted to identities, including cloud infrastructure entitlements (CIEM), removing unused and excessive privileges to enforce least privilege.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-2(6) and AC-6 (partial) mappings. It right-sizes human and effective permissions, while Cloud Workload Identity Permissions, Service Account Least Privilege, and Agent Tool/API Access Scoping cover non-person identities. Just in Time Access shares the AC-2(6) claim through time-bound activation. In an Air-Gapped/Isolated deployment, only the on-premises analysis applies, not CIEM.

### ID-1.8: Account Lifecycle and Identity Data Quality

**Design Intent:** Synchronize accounts against the identity provider and deprovision a departing user's access across every segment, including the ground control stations. Partner accounts expire with their sponsor's agreement, and accounts dormant past the AMP's threshold are disabled.

**NIST Control Mapping:**

- **AC-2(1) (partial):** Authoritative Source Synchronization continuously and automatically synchronizes account attributes against the authoritative source. It stays partial, since this outcome owns only the data-quality and hygiene slice of account management.
- **AC-2(3) (partial):** This outcome automates two of the four disabling conditions, accounts no longer tied to a user and inactive accounts, for human accounts only. Policy-violation disabling stays a human decision, and other outcomes hold the non-person and expired conditions.
- **IA-4 (partial):** This outcome owns only the duplicate-identity slice. Binding to Authoritative Source holds the identifier-assignment slice.
- **Declined:** AC-2(4) covers auditing account actions, which the Operate pillar's Identity Change Tracking holds as AC-2(4) partial, so claiming it here would double-count.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Identity Lifecycle and Governance

**External Dependencies:** The parent organization's personnel system and the performer's, which signal departures. Performer departures follow the timeline in the interconnection agreement.

**Security Impact:** Moderate

**Activities:**

- **ID-1.8.1: Authoritative Source Synchronization**
    - **Description:** Continuously synchronize identity records and account attributes against the program's authoritative system of record so that every account reflects the current state of its subject after enrollment.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Binding to Authoritative Source sets the initial anchor, and this activity keeps it current for the life of the account. It also feeds Deprovisioning-on-Termination Automation, since a recorded termination drives deprovisioning.

- **ID-1.8.2: Deprovisioning-on-Termination Automation**
    - **Description:** Automatically disable and revoke a subject's accounts and access the moment a termination or separation is recorded in the authoritative source, without waiting on manual ticket-driven offboarding.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity handles the clean case where a termination is recorded upstream. Orphaned and Dormant Account Remediation catches the accounts that slip past it.

- **ID-1.8.3: Orphaned and Dormant Account Remediation**
    - **Description:** Define the inactivity threshold and detection cadence at which an account is considered dormant and document them in the AMP, then detect accounts with no valid owner or no recent activity against that threshold and disable or remove them on that cadence to shrink the standing attack surface of unused credentials.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Monthly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is the safety net beneath Deprovisioning-on-Termination Automation, finding accounts never cleanly deprovisioned by scanning for absent ownership and inactivity.

- **ID-1.8.4: Duplicate Identity Detection and Reconciliation**
    - **Description:** Detect multiple accounts or identifiers that resolve to the same real-world subject and reconcile them to a single authoritative identity so that entitlements and audit trails are not fragmented across duplicates.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Tool-driven detection carries the outcome's IA-4 (partial) mapping. Reconciliation is a human decision, so this activity is not tagged Automate.

- **ID-1.8.5: Identity/Access Posture Dashboard**
    - **Description:** Provide a dashboard that surfaces identity and access posture metrics, such as entitlement sprawl, access review completion, and orphaned and dormant account counts, for the PMO ISSE and program leadership.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Visualize
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This dashboard aggregates signals from several outcomes, such as Access Reviews and Identities and Entitlements Lifecycle, without performing remediation itself.

### ID-1.9: Access Reviews

**Design Intent:** Recertify access on the AMP's cadence, reviewing operator, platform administrator, and partner access more often than analyst access. Partner reviews include each sponsor, and operator reviews include the operations lead.

**NIST Control Mapping:**

- **AC-6(7) (full):** this outcome is a direct implementation of periodic privilege recertification.
- **AC-2 (partial):** Only the review sub-requirement lives here, and other outcomes own the rest. The base control is cited because AC-6(7) carries recertification.
- **AC-2(7) (partial):** Privileged entitlement campaigns and Access Review Outcome Actions monitor privileged role assignments and revoke inappropriate ones. Privileged Access Control holds the role-based clause, and Identity Change Tracking holds real-time change monitoring.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Identity Lifecycle and Governance

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-1.9.1: Access Review Scope and Objectives**
    - **Description:** Define which identities, entitlements, and resources each review campaign covers and what the review is intended to certify, and document the scope and objectives in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)

- **ID-1.9.2: Access Review Assignments**
    - **Description:** Assign each in-scope entitlement to the accountable reviewer best positioned to judge whether the access remains warranted, typically the resource owner or the subject's manager.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)

- **ID-1.9.3: Access Review Setup**
    - **Description:** Stand up each review campaign in the access review tooling, loading its scope, reviewers, cadence, and decision options so that reviewers can be presented with the access to certify.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)

- **ID-1.9.4: Access Review Evaluations**
    - **Description:** Have assigned reviewers evaluate each entitlement in the campaign and record an explicit keep-or-revoke decision with justification for the access being certified.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)

- **ID-1.9.5: Access Review Outcome Actions**
    - **Description:** Act on each review decision by revoking or adjusting the entitlements flagged for removal and confirming the changes were applied, closing the loop on the campaign.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Revocations run through the request-and-change path Entitlement Lifecycle Workflows establishes, so a review-driven removal is applied and audited like any other change.

- **ID-1.9.6: Automated Access Review Campaign Generation and Reminders**
    - **Description:** Automatically generate recurring review campaigns from defined scope and reviewer assignments and send reviewers escalating reminders until their evaluations are complete.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity automates recurring Access Review Setup and follow-through on Access Review Assignments. Its completion rates feed the Identity/Access Posture Dashboard.

### ID-1.10: Physical and Logical Access Convergence

**Design Intent:** Correlate badge events at the mission data center and the ground control station sites with logical sign-ins, so an operator signed in at a station but not badged into that site raises an alert. The physical access control systems belong to the PSO, and at the alternate site to the parent organization's facility, so KESTREL consumes their events and drives badge provisioning from its account lifecycle rather than running them.

**NIST Control Mapping:**

- **PE-3 (partial):** This outcome owns only the identity-platform integration slice, binding physical credentials to identity records and correlating physical with logical activity. The PSO holds the physical access program, and PE-3's enhancements govern those operations.
- **PE-2 (partial):** This claim covers the same integration slice as PE-3, while the rest stays with the PSO. PE-2's enhancements likewise govern physical operations this outcome does not own.
- **AC-2 (partial):** This outcome extends the account lifecycle to badge and physical credentials. Account Lifecycle and Identity Data Quality holds the general machinery.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Directory/Platform Core Infrastructure, Identity Lifecycle and Governance, OT/ICS Device

**External Dependencies:** The PSO's physical access control systems at the data center and each operating site, and the parent organization's facility access control system at the alternate site, under the facility agreement.

**Security Impact:** Low

**Activities:**

- **ID-1.10.1: PACS-to-Identity Platform Integration**
    - **Description:** Integrate the physical access control system with the centralized identity platform so that badge credentials and physical-access authorizations derive from the same authoritative identity records as logical access.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This integration builds on the platform that Identity Platform Adoption, under Centralized Identity Platform, stands up. It connects PACS into that authoritative platform rather than establishing a parallel physical-identity store.

- **ID-1.10.2: Physical Access Provisioning and Deprovisioning**
    - **Description:** Provision and deprovision badge credentials and physical-access rights through the same account lifecycle that governs logical accounts, so that physical access is granted and revoked in lockstep with logical access.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is tagged Automate because it extends Deprovisioning-on-Termination Automation to physical credentials. A recorded separation disables the badge on the same signal that disables logical accounts.

- **ID-1.10.3: Physical-Logical Access Correlation**
    - **Description:** Correlate physical-presence events from the PACS against logical-access activity to detect anomalies where the two disagree, such as a logical session from an account whose badge shows the subject off-site.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 3 (Optimal, best practice beyond minimum ATO requirements)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** A physical-logical mismatch strongly indicates a shared, stolen, or spoofed credential. The Adaptive, Risk-Based Access Control outcome can consume this signal for access-time enforcement.

- **ID-1.10.4: Physical Access Reconciliation and Audit**
    - **Description:** Reconcile PACS-held physical-access assignments against authoritative identity records on a defined cadence and audit for badge credentials that no longer map to a valid, currently-authorized identity.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity does for badges what Orphaned and Dormant Account Remediation does for logical accounts. It catches badges that outlived their authorization because a separation never reached the PACS.

## ID-2: User Identity Protection

### ID-2.1: User Authentication Controls

**Design Intent:** Require CAC or partner PKI certificates for every person, with no password path for any user role. Ground control stations cannot use the enterprise sign-in flow during flight, so they authenticate operators with a local smart card check and rely on the compensating physical controls the CCSD recorded for AC-11.

**NIST Control Mapping:**

- **AC-8 (full):** System Use Notification Banner Configuration carries this claim. Rules of Behavior and Acceptable Use Policy names this outcome as AC-8's home, since the banner is a technical setting rather than the PL-4 document.
- **IA-2(1) (full):** mandating phishing-resistant authenticators for privileged accounts implements multi-factor authentication for that class, as Centralized Identity Platform defers here.
- **IA-2(2) (full):** the same mandate applied to non-privileged accounts.
- **IA-2(8) (partial):** the mandated phishing-resistant authenticators resist replay, while the residual password fallback does not, which keeps this partial. Session and token replay after login falls under SC-23 in Continuous Authentication.
- **IA-2(12) (partial):** this outcome governs acceptance of internally issued PIV/CAC and derived PIV. Credential Management holds issuance, and External PKI Trust and Sponsorship holds other-agency PIV.
- **IA-5(1) (partial):** only the residual fallback slice of password-based authentication lives here, in the Password Security activity, consistent with the zero-trust phishing-resistant-first posture that minimizes password use.
- **AC-7 (full), IA-6 (full):** Logon Attempt Limits and Authentication Feedback limits invalid logon attempts and obscures authentication feedback.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Human Authentication, Device/Workstation, OT/ICS Device

**External Dependencies:** DoD PKI and External Certificate Authorities for the certificates themselves.

**Security Impact:** High

**Activities:**

- **ID-2.1.1: Phishing-Resistant Authenticator Selection (PIV/CAC/FIDO2)**
    - **Description:** Select and mandate phishing-resistant authenticators (PIV, CAC, and FIDO2/WebAuthn) as the program's primary authentication mechanism, and document the approved authenticator types and their permitted use in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The outcome's IA-2(1)/IA-2(2) full mappings rest on this decision. Credential Management issues the selected authenticators, and Centralized Identity Platform enforces them at access time.

- **ID-2.1.2: Assurance-Level-to-Resource-Sensitivity Mapping**
    - **Description:** Determine the authenticator assurance level (AAL1/AAL2/AAL3) and phishing-resistant authenticator strength each resource-sensitivity tier requires at access time from the consequences of an authentication failure at that tier, selecting it on its own risk assessment rather than deriving it from the identity assurance level, and document the mapping in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The AAL is selected on its own risk assessment rather than translated from the IAL, since SP 800-63 separates IAL, AAL, and FAL. Both are recorded together in the AMP beneath the AO-tailored, DoD/STIG-derived baseline. The phishing-resistant-first posture puts the practical floor at AAL2 or above.

- **ID-2.1.3: Derived/Mobile Credentials**
    - **Description:** Issue and manage derived PIV credentials for mobile and other form factors that cannot accept a physical PIV/CAC card, binding each derived credential to the subject's already-proofed identity per NIST SP 800-157.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Derived credentials build on the identity already proofed under Identity Proofing and Enrollment, extending phishing-resistant authentication to mobile devices. They do not apply in an Air-Gapped/Isolated deployment.

- **ID-2.1.4: Fallback/Step-Up Authenticator Policy**
    - **Description:** Define the policy governing when a weaker fallback authenticator may be used in place of the primary phishing-resistant authenticator and when a stronger step-up authenticator is required for sensitive actions, and document it in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity defines the policy only, and Step-Up Re-Authentication Triggers enforces it at access time. Fallback to weaker authenticators is allowed only where no phishing-resistant option exists.

- **ID-2.1.5: Password Security**
    - **Description:** Establish password composition, screening against breached-password lists, and lifecycle requirements per NIST SP 800-63B for the residual cases where a password must serve as a fallback authenticator, and document them in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity holds the outcome's IA-5(1) (partial) mapping, since passwords survive only as a fallback. Requirements follow NIST SP 800-63B, favoring length and breached-list screening over forced rotation.

- **ID-2.1.6: OT/Legacy Authentication Compensating Controls**
    - **Description:** Define compensating authentication controls for legacy and OT systems that cannot support phishing-resistant authenticators, such as gateway-mediated authentication, network-enforced access restrictions, and monitored shared-credential handling, and document them in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity covers how operators authenticate to legacy and OT systems that cannot present a phishing-resistant authenticator. Its compensating controls lean on OT/Legacy Device Identity Controls and IT/OT zone-and-conduit segmentation. It is the sole reason Cyber-Physical System (OT/ICS) appears in the outcome's Deployment Type.

- **ID-2.1.7: System Use Notification Banner Configuration**
    - **Description:** Configure the system to display a system use notification banner that follows the standard DoD banner language pattern rather than program-specific wording and states the absence of privacy expectations, consent to monitoring, and the consequences of unauthorized use, and require explicit acknowledgment before access is granted.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Immediate (less than one sprint)
    - **Supplemental Guidance:** This activity carries the outcome's AC-8 (full) mapping. Rules of Behavior and Acceptable Use Policy declines AC-8, since the banner is a technical setting rather than part of the rules document. It is event-driven because the text changes only when policy or legal review changes the required language.

- **ID-2.1.8: Logon Attempt Limits and Authentication Feedback**
    - **Description:** Limit consecutive invalid logon attempts within a defined window, lock the account or delay further attempts once the limit is reached, and obscure authentication feedback so entered secrets are masked and failure messages do not reveal which factor was wrong.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-7 (full) and IA-6 (full) mappings. A smart card PIN is still guessable, so lockout still matters. The threshold balances guessing resistance against deliberate lockout of users, so it is set per population in the AMP. OT/Legacy Authentication Compensating Controls covers devices that cannot lock out.

### ID-2.2: Credential Management

**Design Intent:** KESTREL validates CACs and partner certificates but does not issue them. It issues and revokes only its own device and workload certificates from the program PKI, and it runs the revocation checking every external credential passes. The NSS PKI tokens this outcome names belong to the IL6 enclave, not to KESTREL.

**NIST Control Mapping:**

- **IA-5 (partial):** This outcome owns only the person-entity PKI slice, namely PIV/CAC issuance, renewal, and revocation. Password Security and Non-Person Entity Identity Protection hold the other slices.
- **IA-5(2) (partial):** This outcome covers only the internal PIV/CAC side, validating paths to the program's own anchor and checking its own OCSP/CRL. External PKI Trust and Sponsorship holds the external-issuer side.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Human Authentication, PKI/Certificate Authority, Device/Workstation

**External Dependencies:** DoD PKI and External Certificate Authorities for issuance and revocation of user credentials.

**Security Impact:** High

**Activities:**

- **ID-2.2.1: PIV/CAC Credential Issuance**
    - **Description:** Issue and provision the PIV, CAC, and FIDO2 authenticators selected by Phishing-Resistant Authenticator Selection to identities already proofed and bound under Identity Proofing and Enrollment, without re-proofing the subject.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity issues the physical PIV/CAC and FIDO2 authenticators Phishing-Resistant Authenticator Selection selects. It issues to identities Identity Proofing and Enrollment already established, while Derived/Mobile Credentials covers mobile form factors.

- **ID-2.2.2: Credential Revocation and Renewal**
    - **Description:** Revoke a subject's credentials on separation, loss, or compromise and renew or re-key them before expiration so that every active PIV/CAC remains valid and every credential no longer entitled to trust is promptly rendered untrusted.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Revocation on separation acts on the same termination signal as Deprovisioning-on-Termination Automation. Credential Status Checking (OCSP/CRL) then publishes and queries the resulting revocation state.

- **ID-2.2.3: PIV-Denied and Degraded-Connectivity Fallback**
    - **Description:** Define the fallback authentication procedures that apply when PIV/CAC issuance or validation infrastructure is unavailable or connectivity to revocation services is degraded, and document them in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Unlike Fallback/Step-Up Authenticator Policy, this activity covers the case where PIV/CAC infrastructure or revocation connectivity itself fails, using locally cached revocation data as IA-5(2) permits. It matters most in Air-Gapped/Isolated and intermittently connected deployments.

- **ID-2.2.4: Credential Status Checking (OCSP/CRL)**
    - **Description:** Stand up and operate the internal OCSP responder or CRL distribution point that publishes PIV/CAC revocation status, and validate internally issued PIV/CAC at authentication time by constructing the certificate path to the program's trust anchor and confirming revocation status against it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity operates the internal-issuer side of the outcome's IA-5(2) (partial) mapping, mirroring External Credential Validation and Revocation Checking. A credential revoked under Credential Revocation and Renewal stops authenticating at the next status check.

- **ID-2.2.5: National Security Systems PKI Hardware Token Management**
    - **Description:** Coordinate the issuance, PIN reset, renewal, and revocation of National Security Systems (NSS) PKI hardware tokens, such as SIPRNet tokens, for every user of a SECRET or higher network through the NSS PKI registration authority process CNSSI 1300 governs, and document the token sponsorship and return procedures in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity extends the outcome's IA-5 (partial) mapping to classified networks PIV and CAC do not reach. The NSS PKI is a separate hierarchy, so the program sponsors users to its registration authority and owns local token accountability. A lost or unreturned token is reported to the issuing authority the same day. It is Level 2, but mandatory for any program with users on SECRET or higher networks.

### ID-2.3: Single Sign on (SSO)

**Design Intent:** Federate every user-facing application and administrative console behind the identity provider, from the analyst portal and the LLM analyst assistant to the partner API. One sign-on covers the mission applications, while administrative consoles require their own fresh authentication.

**NIST Control Mapping:**

- **IA-2(10) (full):** SSO Planning defines the set of accounts and services, and SSO Configuration integrates each application so a subject authenticates once.
- **SI-10 (partial):** SSO Protocol Configuration Hardening validates each assertion's signature, audience, recipient, nonce, and validity window, and rejects structural manipulation. It is partial because other outcomes hold SI-10 for other input classes.
- **SI-10(5) (partial):** The same activity restricts those inputs to trusted sources and formats through redirect URI and issuer allowlists and a fixed protocol profile. It is partial on the same footing as SI-10.
- **Declined:** IA-2 and its authenticator-strength enhancements are already claimed by Centralized Identity Platform and User Authentication Controls, and SSO only federates IA-2 authentication. IA-2(10) is distinct, since it covers the SSO capability itself.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Directory/Platform Core Infrastructure, Human Authentication, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-2.3.1: SSO Planning**
    - **Description:** Select the federation protocols (SAML/OIDC), define the application onboarding strategy, and determine the session-sharing scope for SSO, and document them in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is the scoping half of the outcome's IA-2(10) (full) mapping, with SSO Configuration as the delivery half. It presumes Centralized Identity Platform is the identity provider. Session and Token Lifetime Policy governs the lifetime of the sessions scoped here.

- **ID-2.3.2: SSO Configuration**
    - **Description:** Integrate each in-scope application against the centralized identity platform using the selected federation protocol so that users authenticate once and receive federated access to the onboarded applications.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity, with SSO Planning, delivers the outcome's IA-2(10) (full) mapping by federating applications against the platform. It inherits IA-2 authentication and its phishing-resistant enforcement rather than re-satisfying them. SSO Protocol Configuration Hardening hardens the protocol settings for each relationship.

- **ID-2.3.3: SSO Protocol Configuration Hardening**
    - **Description:** Harden the federation protocol configuration on the identity platform and on each onboarded application by pinning the signature algorithms and keys an assertion must verify against, validating its audience, recipient, in-response-to, nonce, and validity window on every consumption, allowlisting exact redirect URIs and accepted issuers, requiring proof key for code exchange on every authorization-code flow, and refusing unsolicited identity-provider-initiated assertions.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries both of the outcome's SI-10 (partial) and SI-10(5) (partial) mappings. Without it, a correctly planned federation can still honor an assertion the platform never issued, turning one compromised application into access as any user. Each check closes a different gap, namely algorithm and key pinning, audience and recipient checks, and in-response-to and nonce correlation. A consuming library that cannot resist signature wrapping needs replacing. It is Level 1, unlike its siblings, because a program that stands up SSO cannot leave the federation unhardened.

### ID-2.4: Non-Privileged Access Control

**Design Intent:** Define the non-privileged roles once in the identity provider, and default every new identity to no access. Team membership is part of every role, so an analyst in one mission team cannot reach another team's payload vendor data. Partners see only products released to their own nation.

**NIST Control Mapping:**

- **AC-3(7) (partial):** The non-privileged roles and group-based baseline are a role-based access control policy. Privileged Access Control holds the privileged half.
- **AC-6 (partial):** Default Permissions sets the least-privilege baseline for non-privileged identities, alongside other least-privilege claims such as Identities and Entitlements Lifecycle's right-sizing.
- **AC-14 (full):** Unauthenticated Action Inventory identifies and justifies each action permitted without authentication.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Identity Lifecycle and Governance

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **ID-2.4.1: Default Permissions**
    - **Description:** Define the minimal baseline set of permissions every non-privileged identity receives by default before any role is assigned, holding that baseline to least privilege, and document it in the AMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This baseline is the least-privilege floor for the outcome's AC-6 (partial) mapping. An identity with no role reaches only what every program member needs, so all further access is an explicit role grant. Control Type is Documentation because the deliverable is the determination, recorded in the AMP.

- **ID-2.4.2: Platform-Defined Non-Privileged Roles**
    - **Description:** Catalog and adopt the out-of-the-box non-privileged roles the identity platform ships, mapping each to the program's access needs and disabling those that grant more than a non-privileged identity should hold, and document the resulting catalog in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Adopting the platform's built-in roles first keeps the model close to the vendor's supported baseline. Custom Non-Privileged Roles extends it only where a genuine access need has no platform-provided equivalent.

- **ID-2.4.3: Custom Non-Privileged Roles**
    - **Description:** Design and build program-defined non-privileged roles for the access needs the platform's built-in roles do not cover, scoping each to the minimum permissions its function requires, and document the resulting catalog in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Custom roles are built only where Platform-Defined Non-Privileged Roles leaves a genuine gap, and each is held to least privilege so it does not become a broad catch-all role that erodes the model.

- **ID-2.4.4: Non-Privileged Group Access Control (GBAC) Baseline**
    - **Description:** Define the group-based access control baseline that ties the platform-defined and custom non-privileged roles to resource access, establishing the standard groups, their role assignments, and the resources each group reaches, and document the resulting baseline in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This baseline binds roles to resources through groups and carries the group-membership half of the outcome's AC-3(7) (partial) mapping. Entitlement Management packages these same groups for assignment.

- **ID-2.4.5: Unauthenticated Action Inventory**
    - **Description:** Identify every action a user can perform on the system without identifying or authenticating, document the justification for each, and remove any that lacks one.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-14 (full) mapping. In most classified programs the inventory is nearly empty, namely the banner, the logon screen, and perhaps an emergency function. It catches endpoints exposed anonymously without anyone deciding they should be.

### ID-2.5: Adaptive, Risk-Based Access Control

**Design Intent:** Evaluate each request against identity, device posture, network origin, and risk before granting access. Performer users reach the identity-aware proxy and the admin VDI pool only from laptops that report as compliant at that moment. Partner sessions that arrive from outside their nation's expected networks are stepped up or denied. Identity threat detection feeds the policy engine. The physical-logical correlation raises alerts in the security monitoring platform instead, since stations check sign-ins locally.

**NIST Control Mapping:**

- **AC-3(13) (partial):** the policy engine enforces access on subject, device, location, and risk attributes at request time. The Data focus area's Attribute-Based Data and Application Access Enforcement (ABAC) holds the data and application layers.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Human Authentication, Application/API

**External Dependencies:** The Boundary Cloud Access Point, which supplies the network-origin signal for inbound sessions. The performer's device management, which supplies each laptop's compliance signal.

**Security Impact:** Moderate

**Activities:**

- **ID-2.5.1: Adaptive, Risk-Based Access Tool Deployment**
    - **Description:** Deploy the adaptive access policy engine, a conditional-access or equivalent decision service, that evaluates identity, device, location, and risk-score signals at the moment access is requested and renders an allow, deny, or step-up-authentication decision.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** The engine consumes identity risk signals from Identity Platform Protection Tool Deployment and anomaly signals from Physical-Logical Access Correlation. Adaptive, Risk-Based Access Policy Definition defines the policies it evaluates.

- **ID-2.5.2: Adaptive, Risk-Based Access Policy Definition**
    - **Description:** Define the risk-based access policies the engine enforces, namely the risk thresholds, signal combinations, and resource-sensitivity conditions that map to an allow, deny, or step-up-authentication outcome, and document them in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity delivers the outcome's AC-3(13) (partial) mapping by defining the conditions the engine evaluates. Its step-up decisions invoke Fallback/Step-Up Authenticator Policy, while Continuous Authentication handles mid-session risk.

### ID-2.6: Continuous Authentication

**Design Intent:** Re-evaluate every portal, assistant, and administrative session while it runs, and revoke a session when risk becomes severe. Device lock applies to every KESTREL device except a ground control station whose aircraft is airborne, the exception the AO approved in CCSD tailoring action 2.

**NIST Control Mapping:**

- **AC-12 (partial):** Session/Token Revocation on Risk Change and Session and Token Lifetime Policy terminate sessions on risk or elapsed time, and Continuous Access Evaluation carries termination to the resource. Agentic Session Timeout and Forced Termination holds the AI agent population.
- **IA-11 (full):** Step-Up Re-Authentication Triggers and the lifetime-driven re-authentication of Session and Token Lifetime Policy require re-authentication under defined circumstances.
- **SC-23 (partial):** Session and Token Lifetime Policy limits how long a captured token stays useful, and Token Binding and Proof-of-Possession makes it useless away from its client. Application and network session mechanisms hold the rest.
- **IA-10 (full):** Step-Up Re-Authentication Triggers requires re-proof at a stronger authenticator under the risk circumstances session scoring defines.
- **AC-11 (full), AC-11(1) (full):** Device Lock locks after inactivity or on request, holds the lock until re-authentication, and conceals the display.
- **AC-10 (full):** the only claim of the control in the framework, carried by Concurrent Session Limits, which limits the number of concurrent sessions per account and account type.
- **AC-2(5) (partial):** Session and Token Lifetime Policy logs users out after inactivity. Rules of Behavior and Acceptable Use Policy holds the user's duty to log out before an absence.
- **Declined:** No SC-23 enhancement fits better than the base SC-23. SC-23(1) covers logout invalidation, SC-23(3) identifier randomness, and SC-23(5) permitted certificate authorities.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Human Authentication, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-2.6.1: Session Risk Scoring**
    - **Description:** Continuously compute a per-session risk score for each already-active session from ongoing signals, including the identity threat signals produced by Identity Platform Protection Tool Deployment, device posture, and behavioral and location changes, and document the scoring inputs and thresholds in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is the scoring engine the other three activities act on. It reuses Identity Platform Protection Tool Deployment's risk signals during the session, not only at access time. Moderate risk fires Step-Up Re-Authentication Triggers, and severe risk fires Session/Token Revocation on Risk Change.

- **ID-2.6.2: Step-Up Re-Authentication Triggers**
    - **Description:** Configure the identity platform to force step-up re-authentication when a session's risk score crosses a defined mid-session threshold, requiring the subject to re-prove at the authenticator strength set by Fallback/Step-Up Authenticator Policy.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity executes Fallback/Step-Up Authenticator Policy mid-session, as Adaptive, Risk-Based Access Policy Definition does at access time. It is the lower-severity response, demanding re-proof rather than ending the session.

- **ID-2.6.3: Session/Token Revocation on Risk Change**
    - **Description:** Configure the identity platform to automatically revoke an active session and invalidate its issued tokens when its risk score crosses a severity threshold beyond which step-up re-authentication is no longer sufficient, forcing a full new authentication.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity kills a session in progress when Session Risk Scoring reports severe risk, the higher-severity response compared with Step-Up Re-Authentication Triggers. It contributes to the outcome's AC-12 (partial) mapping alongside Session and Token Lifetime Policy. Continuous Access Evaluation makes the invalidation take effect at applications already holding a token.

- **ID-2.6.4: Continuous Access Evaluation**
    - **Description:** Establish the critical-event and session-revocation signalling path between the identity platform and its onboarded applications so that an application re-evaluates an already-issued access token against current risk, device, and account state within seconds of a change, rather than honoring that token until its next expiry.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity closes the gap between a revocation decision and its effect, since an issued access token stays valid until it expires. It contributes to the outcome's AC-12 (partial) mapping by carrying termination to the resource, which lets Session and Token Lifetime Policy set lifetimes on accepted risk. It is tagged Automate because re-evaluation is an always-on machine-to-machine exchange. Applications that do not support the signalling protocol fall back to the shortest lifetime the program will bear.

- **ID-2.6.5: Session and Token Lifetime Policy**
    - **Description:** Define the maximum session lifetime, idle-timeout, and token and refresh-token rotation requirements that govern both direct platform sessions and the SSO-established sessions Single Sign on (SSO) creates, and document them in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-23 (partial) mapping, the lifetime-and-idle half of its AC-12 (partial) mapping, and its AC-2(5) (partial) mapping through the idle timeout. Its lifetimes govern both SSO and direct platform sessions. They are also the compensating position wherever Token Binding and Proof-of-Possession cannot be applied.

- **ID-2.6.6: Token Binding and Proof-of-Possession**
    - **Description:** Issue session and refresh tokens as proof-of-possession artifacts cryptographically bound to a key the client holds, whether by a client-held key demonstrated at each use, a mutual-TLS-bound certificate, or a device-bound refresh token, so that a token captured in transit or lifted off a compromised host cannot be replayed from anywhere else.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-23 (partial) mapping alongside Session and Token Lifetime Policy. It answers token theft by adversary-in-the-middle proxies and infostealers, which bypass phishing-resistant authentication by stealing the resulting session artifact. Binding makes the token useless without the key it was bound to. Where an application cannot bind, the shortest bearable lifetime plus Continuous Access Evaluation compensates, and unbound applications are tracked as residual risk.

- **ID-2.6.7: Device Lock**
    - **Description:** Lock each device after the period of inactivity the AMP defines and on the user's request, conceal the display's contents while it is locked, and require the user to re-authenticate before the lock is released.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-11 (full) and AC-11(1) (full) mappings. Device lock is not session termination, since the session resumes on re-authentication. The authorization framework sets the inactivity period, and device baselines enforce it so users cannot lengthen it.

- **ID-2.6.8: Concurrent Session Limits**
    - **Description:** Limit the number of concurrent sessions each account may hold to the limits the AMP sets, with a tighter limit for privileged accounts, and alert when an account exceeds it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-10 (full) mapping. It is Level 2 because AC-10 is High-baseline only, and it is mandatory where the program's baseline is High. A second concurrent session is a simple indicator of a shared or stolen credential, so the alert matters as much as the limit.

## ID-3: Non-Person Entity Identity Protection

### ID-3.1: Cloud Workload Identities

**Design Intent:** Give every IL5 workload the managed Kubernetes service's native workload identity, so services read the data lake zones, the report index, and ML Prod's model endpoints without a stored secret. Each workload's identity is scoped to its own spoke and team. Static credentials found in the cloud spokes are removed once native identity replaces them.

**NIST Control Mapping:**

- **IA-9 (partial):** The base is cited because Rev 5 withdrew IA-9's enhancements into it. This outcome covers only the cloud-native workload slice, while Application and Service Account Identities and Server and Services Authentication hold the rest.
- **AC-6 (partial):** Cloud Workload Identity Permissions right-sizes workload identity permissions, alongside the other non-person and human right-sizing activities.
- **IA-5(7) (partial):** Native/Local Credential Elimination removes static authenticators embedded in code and configuration. Secrets and Credentials Detection, Secrets and Credentials Protection, and outcomes in the Application and Artificial Intelligence focus areas hold the other surfaces.

**Deployment Type:** Cloud, Hybrid

**Affected Components:** Compute, Cloud Workload/Native Platform Identity, Application/API

**External Dependencies:** The IL5 cloud provider's workload identity mechanism, inherited under its provisional authorization.

**Security Impact:** Moderate

**Activities:**

- **ID-3.1.1: Cloud Workload Identity Selection**
    - **Description:** Select and adopt the cloud provider's native workload identity mechanism, such as managed identities or IAM roles for compute, as the program's primary non-person identity model for every cloud workload the platform can natively identify.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The rest of the outcome builds on this decision. Workloads the platform cannot natively identify fall back to the managed and vaulted path Application and Service Account Identities owns.

- **ID-3.1.2: Cloud Workload Identity Permissions**
    - **Description:** Continuously scope and right-size the permissions granted to each workload identity, removing unused and excessive entitlements so that a workload holds only the access its function requires.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity owns the workload slice of the outcome's AC-6 (partial) mapping by continuously pruning cloud IAM entitlements. Service Account Least Privilege, Agent Tool/API Access Scoping, and Permissions Management right-size the other identity types.

- **ID-3.1.3: Cloud Workload Identity Code Authentication Integration**
    - **Description:** Integrate application code to obtain its identity and access tokens at runtime from the native workload identity mechanism, through the platform's identity SDK or instance metadata endpoint, rather than reading an embedded or configured credential.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Once code authenticates through the selected mechanism, Native/Local Credential Elimination can remove the embedded credential. Where instance metadata is the retrieval path, require IMDSv2 or the equivalent session-token mode, set the hop limit to 1, and disable the legacy endpoint after migration. Server-side request forgery against instance metadata is the standard way this credential is stolen.

- **ID-3.1.4: Native/Local Credential Elimination**
    - **Description:** Find and remove the embedded, static, and locally stored credentials, such as API keys, connection strings, and passwords, that native workload identity has rendered unnecessary, and confirm each workload authenticates solely through its platform identity.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(7) (partial) mapping. It removes the embedded credentials Secrets and Credentials Detection finds once Cloud Workload Identity Code Authentication Integration provides a credential-free path. Credentials that cannot be eliminated move into the vault Secrets and Credentials Protection owns.

### ID-3.2: Application and Service Account Identities

**Design Intent:** Use governed service accounts only where native identity is not available, namely the data center's services and connections that cross the dedicated circuit. Each has a named owner and certificate-based authentication from the program PKI.

**NIST Control Mapping:**

- **IA-9 (partial):** The base is cited since Rev 5 withdrew its enhancements. This outcome owns the service-account slice, while Cloud Workload Identities and Server and Services Authentication hold the rest.
- **AC-6 (partial):** Service Account Least Privilege right-sizes service-account permissions, alongside the other right-sizing activities Permissions Management names.
- **IA-5(2) (partial):** Certificate-Based Credentials makes PKI-backed authentication the preferred service-account credential. Secrets and Credentials Protection holds the residual client-secret path, and Credential Management and External PKI Trust and Sponsorship hold the person-entity slices.
- **AC-2(3) (partial):** Non-Person Entity Account Recertification disables non-person identities that lost an owner or purpose. This slice is tracked jointly with the human one in Account Lifecycle and Identity Data Quality, since termination signals and dormancy scans never fire for non-person accounts.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Application and Service Account Identity, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-3.2.1: Service Account Creation**
    - **Description:** Provision service accounts only through a governed request-and-approval process rather than ad hoc, giving each a named owner, a defined purpose, and a lifecycle bound to that purpose, and document the provisioning process in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This governed-provisioning decision is the service-account counterpart to Cloud Workload Identity Selection. Service Account Least Privilege then right-sizes these accounts, and Certificate-Based Credentials or Client Secret Fallback credentials them.

- **ID-3.2.2: Service Account Least Privilege**
    - **Description:** Continuously review and trim the entitlements each service account holds, revoking those left unused or exceeding its function so the account retains only the access it genuinely needs.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity delivers the service-account portion of the outcome's AC-6 (partial) mapping by trimming entitlements to each account's function. Cloud Workload Identity Permissions and Agent Tool/API Access Scoping cover the other non-person identity types.

- **ID-3.2.3: Certificate-Based Credentials**
    - **Description:** Configure service accounts to authenticate with certificate-based credentials wherever the platform and application support them, in preference to shared client secrets, as the strongest available authenticator for this fallback path.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(2) (partial) mapping, making certificate authentication the preferred service-account credential. The Data focus area's key management owns certificate issuance, and Client Secret Fallback covers cases where certificates cannot be used.

- **ID-3.2.4: Client Secret Fallback**
    - **Description:** Where certificate-based authentication is not possible, issue the service account a client secret and store it in the secrets vault through NPE Credential Vault Integration (Secrets and Credentials Protection) rather than leaving it in application configuration or source.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This residual path applies only when Certificate-Based Credentials cannot be used. NPE Credential Vault Integration and Automated Secret Rotation vaults and rotates the secret, and code reads it at runtime.

- **ID-3.2.5: Service Account Code Authentication Integration**
    - **Description:** Integrate application code to obtain the service account's credential from its certificate store or the secrets vault at runtime, rather than reading an embedded or hard-coded secret from configuration or source.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is the fallback-path pair of Cloud Workload Identity Code Authentication Integration. It wires code to the certificate store or vaulted secret, keeping the credential out of configuration and source.

- **ID-3.2.6: Non-Person Entity Account Recertification**
    - **Description:** Re-attest every service account, workload identity, and agent identity on a defined cadence against a named, currently employed owner and a still-valid business purpose, and disable those failing either test rather than waiting for them to fall dormant.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-2(3) (partial) mapping. Termination signals, dormancy scans, and manager attestation all miss non-person accounts, since no separation is recorded and automated callers never go idle. Ownership comes from Service Account Creation, Agent Identity Registration, and Resource Tagging and Ownership Strategy, so one review covers all three non-person populations. Unlike Service Account Least Privilege, it asks whether an account should exist at all.

### ID-3.3: AI Agent Identities

**Design Intent:** Register every AI agent as its own identity, scoped to the data and tools its approved use case needs. No agent identity can reach a tool that tasks an aircraft or changes a system without a named human role approving the action first. The mission-planning agent is the first, scoped to reading mission data and drafting plans, so an operator's approval stays the only path from a draft to a flight.

**NIST Control Mapping:**

- **AC-6 (partial):** Agent Tool/API Access Scoping right-sizes which tools, APIs, and data sources an agent may invoke. It joins the focus area's other right-sizing activities, while other outcomes hold the rest of the control.
- **AU-10 (partial):** This partial claim covers Delegated Authority Attribution, which binds each agent action to the principal that invoked it, as the base control's process-acting-for-an-individual wording describes. AU-10's enhancements address data producers, custody, and reviewers instead.
- **AC-3(2) (partial):** High-Risk Action Human Approval Gate requires a human approver before an agent executes defined high-risk actions. The broader enforcement is held by other outcomes.
- **AC-12 (partial):** Agentic Session Timeout and Forced Termination bounds agent sessions and forces termination or re-authorization. Continuous Authentication holds the human session population, and the two are tracked jointly.
- **SA-9 (partial):** This claim covers admitting external tool-providing servers to an agent's reachable set and monitoring their declared catalogs. Such servers assert their own callable actions at connection time, a risk distinct from a conventional API. Four other outcomes, including Contract Security Requirements, hold the other provider populations.
- **Declined:** IA-9 is already satisfied by the base identity from Cloud Workload Identities or Application and Service Account Identities. AC-6 stays with Agent Tool/API Access Scoping. SI-15 and AC-4 belong to Agentic Tool-Call/Action Output Validation.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, AI Agent Identity, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-3.3.1: Agent Identity Registration**
    - **Description:** Provision each AI agent as its own governed non-person identity, never a person account or a shared generic service account, recording its owning team, purpose, underlying model, and the tools and data sources it is authorized to reach, and document the registration process in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Registration names the agent as its own identity, the agent analog of Service Account Creation and Cloud Workload Identity Selection. It carries no control citation, since the agent authenticates through the base credential those outcomes own. Its approval is also the re-approval path for material scope changes. Model Registration and Inventory Logging is a separate record for the model version the agent runs on.

- **ID-3.3.2: Task-Scoped Credential Issuance**
    - **Description:** Issue each agent short-lived, task- or session-scoped credentials sized to the job at hand rather than a standing broad role, so that a manipulated or misbehaving agent's blast radius is bounded to that session.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries no independent citation and does not join the AC-2(6) tracking, which covers time-bound human elevation. Its per-task credential is sized against Agent Tool/API Access Scoping and gated by High-Risk Action Human Approval Gate. ConMon Activity is Continuous because issuance mints and expires a credential per task.

- **ID-3.3.3: External Tool-Provider Registration and Approval**
    - **Description:** Register each external tool-providing server an agent may connect to as its own reviewed entry, recording its operator, the tool catalog and data access it declares, and the residency and trust terms it is held to, and block an agent from adding a server's tools to its reachable set until that entry is approved.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-9 (partial) mapping for the admission element. A tool-providing server declares its own catalog at connection time, and the agent reads that declaration as context, so an unreviewed server is an unreviewed input to the agent's reasoning. It is Level 1 because Agent Tool/API Access Scoping presupposes that servers have cleared this gate.

- **ID-3.3.4: Agent Tool/API Access Scoping**
    - **Description:** Continuously right-size which tools, APIs, and data sources each agent identity may invoke, removing unused and excessive tool grants so that an agent can reach only the capabilities its task requires.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity contributes the agent-scoping quarter of the outcome's AC-6 (partial) mapping by right-sizing the tools, APIs, and data sources an agent may invoke. It governs what an agent draws from servers External Tool-Provider Registration and Approval already admitted. Right-sizing only removes reach, and any scope growth routes back through the approval Agent Identity Registration recorded.

- **ID-3.3.5: Tool-Provider Catalog Drift Detection**
    - **Description:** Record a hash or signed baseline of each admitted server's declared tool catalog, names, descriptions, and parameter schemas at approval time, compare it against what the server presents on each connection, and hold any changed entry out of the agent's reachable set until it clears re-review.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's SA-9 (partial) mapping for the ongoing-monitoring element, applied to a tool catalog. An admitted server's operator can later change a tool, widen a parameter, or embed an instruction in a description without tripping any credential control. Comparison runs against the declaration, while Agentic Tool-Call/Action Output Validation watches call behavior.

- **ID-3.3.6: Delegated Authority Attribution**
    - **Description:** Bind every agent action back to the human or system principal that invoked it through an on-behalf-of chain, so that each action is attributable to an accountable party rather than to the agent alone.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity owns the outcome's AU-10 (partial) mapping, cited at the base level because AU-10's definition covers a process acting on behalf of an individual. It is partial because the Detection focus area's Application/API Logging captures and retains the records. This activity owns only binding each agent action to its invoking principal.

- **ID-3.3.7: High-Risk Action Human Approval Gate**
    - **Description:** Require a human-in-the-loop approval before an agent executes any action in a defined set of high-risk or irreversible operations, rather than permitting fully autonomous execution.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-3(2) (partial) mapping. Unlike Just in Time Access, which governs human elevation, it requires a human approver before an agent runs defined high-risk or irreversible actions. It is partial because dual authorization applies only to those enumerated actions.

- **ID-3.3.8: Agentic Session Timeout and Forced Termination**
    - **Description:** Define a maximum session duration per agentic deployment, automatically terminate any session that exceeds it, suspend a session and alert the ISSO if its action sequence approaches a prohibited action boundary before the duration limit is reached, require human re-authorization logged with the authorizing individual and timestamp before a suspended or timed-out session resumes, and document the duration limits and boundary-approach thresholds in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-12 (partial) mapping, bounding how long an agent session runs even if its credential is re-minted. It also suspends a session whose actions approach a prohibited action in Agent Identity Registration's scope record, routing to the High-Risk Action Human Approval Gate decision point. Thresholds are reviewed annually and adjusted from red team findings.

### ID-3.4: Server and Services Authentication

**Design Intent:** Require mutual TLS between every KESTREL service, with certificates from the program PKI. This includes traffic across the dedicated circuit and the feedback endpoints that accept released products from the IL6 enclave.

**NIST Control Mapping:**

- **IA-9 (partial):** The base is cited since Rev 5 withdrew its enhancements. This outcome owns server-to-server authentication, while Cloud Workload Identities and Application and Service Account Identities hold the rest.
- **SC-17 (partial):** Client Application Certificate Trust selects the trust anchors each service accepts. The rest, issuance and revocation, sits with the Data focus area's Certificate Policies and Integration and Certificate Lifecycle and Revocation.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Network Infrastructure, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **ID-3.4.1: TLS Authentication for Services**
    - **Description:** Configure each service endpoint to present a valid server certificate and require TLS for all inbound connections, so that clients can cryptographically authenticate the service they are connecting to.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity provides the server-side half of the outcome's IA-9 (partial) authentication. Mutual TLS adds client-side proof, and channel encryption is a network-pillar concern.

- **ID-3.4.2: Client Application Certificate Trust**
    - **Description:** Define and configure the set of trust anchors and client certificates each service will accept, so that only approved client applications can authenticate to it, and document the trust configuration in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SC-17 (partial) mapping by restricting each service to approved trust anchors. The Data focus area's key management owns certificate issuance and lifecycle.

- **ID-3.4.3: Mutual TLS**
    - **Description:** Enforce mutual TLS on service-to-service connections so that both endpoints present and validate certificates against the trust established by Client Application Certificate Trust, authenticating each other before exchanging data.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is the fullest expression of the outcome's IA-9 (partial) mapping. It makes both endpoints prove their identity, so service trust rests on cryptographic identity rather than network reachability.

### ID-3.5: Secrets and Credentials Detection

**Design Intent:** Scan the source repository, pipeline logs, container images, and object storage for exposed secrets on every build and on a schedule. A finding in a release candidate fails Certification to Field.

**NIST Control Mapping:**

- **IA-5(7) (partial):** Agentless Scanning detects embedded static authenticators. Native/Local Credential Elimination holds removal, and Secrets and Credentials Protection holds protection.
- **SI-4 (partial):** no SI-4 enhancement fits secrets-exposure monitoring better than the base. It covers only the secrets-exposure slice, while other focus areas hold the rest of system monitoring.
- **Declined:** AU-13 covers external public sites, while Secrets Exposure Monitoring watches internal systems, so SI-4 fits instead.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Compute, Object/File Storage, Artifact/Model Registry, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-3.5.1: Agentless Scanning**
    - **Description:** Deploy tool-driven, agentless scanning that inspects source code, repositories, and configuration for embedded secrets and credentials without requiring an installed agent on each system, flagging every exposure for remediation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(7) (partial) mapping and is the scanning source Native/Local Credential Elimination draws on. Its agentless, pipeline-integrated model covers source and repositories without an agent on every system.

- **ID-3.5.2: Secrets Exposure Monitoring**
    - **Description:** Monitor the non-code surfaces where secrets leak incidentally, namely chat and collaboration tools, ticketing systems, logs, object storage, and container images, for exposed credentials, distinct from the source and repository surfaces Agentless Scanning covers.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Moderate
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's SI-4 (partial) mapping for surfaces Agentless Scanning does not reach, such as chat, tickets, logs, object stores, and container images. It is not tagged Automate because it adds detection coverage rather than replacing a manual step.

### ID-3.6: Secrets and Credentials Protection

**Design Intent:** Hold every non-person secret in its own spoke's secrets vault and rotate it automatically, so no vault holds another team's secrets. CCSD row 13's datalink and root signing keys stay in the HSMs instead, since their High confidentiality calls for hardware protection a software vault does not give.

**NIST Control Mapping:**

- **IA-5(6) (partial):** NPE Credential Vault Integration vaults non-person authenticators, Automated Secret Rotation refreshes them, and Secrets Continuous Monitoring confirms protection holds. Outcomes in the Application and Artificial Intelligence focus areas hold the other slices.
- **IA-5(7) (partial):** Vaulting and the developer workflow keep secrets out of source and configuration. Secrets and Credentials Detection holds detection, and Native/Local Credential Elimination holds removal.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Compute, Application and Service Account Identity, Application/API

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-3.6.1: NPE Credential Vault Integration**
    - **Description:** Integrate non-person-entity credentials, such as service-account client secrets, API keys, connection strings, and machine certificates, into the secrets vault so every NPE secret is stored in and retrieved from the vault rather than held in application configuration or source.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's IA-5(6) and IA-5(7) (partial) mappings. It wires NPE credentials into the vault, including Client Secret Fallback secrets, while the Data focus area owns the vault and HSM infrastructure.

- **ID-3.6.2: Automated Secret Rotation**
    - **Description:** Automatically rotate vaulted non-person-entity secrets on a defined cadence and on demand after suspected exposure, updating both the stored credential and its consumers without manual intervention, and document the rotation cadence in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's IA-5(6) (partial) mapping by keeping each authenticator short-lived. It also rotates the client secrets Client Secret Fallback issues.

- **ID-3.6.3: Developer Workflow for Secrets**
    - **Description:** Establish the developer workflow that keeps secrets out of code from the start, including pre-commit scanning hooks, local secret retrieval from the vault instead of local files, and guardrails that remove any need to hardcode a secret, and document the workflow in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity keeps secrets from being hardcoded in the first place, while Agentless Scanning catches what slips through. Its pre-commit hooks are a local guardrail, not the authoritative pipeline scan. Control Type is Process because the deliverable is a documented developer practice.

- **ID-3.6.4: Secrets Continuous Monitoring**
    - **Description:** Continuously monitor how non-person entities consume and rotate vaulted secrets by verifying that rotation occurs on schedule, that secrets are retrieved from the vault as intended, and that access patterns are not anomalous, distinct from the Data focus area's monitoring of the vault infrastructure itself.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity reinforces the outcome's IA-5(6) (partial) posture by confirming rotation runs on cadence and secrets are consumed as intended. The Data focus area's Secrets Vault Protection and Monitoring watches the vault itself, not how non-person entities use it.

### ID-3.7: OT/Legacy Device Identity Controls

**Design Intent:** Remove vendor-default credentials from the aircraft, ground control stations, and launch and recovery equipment before they field. Each aircraft and station authenticates with its device identity on the datalinks, and equipment that cannot authenticate itself is identified by its zone and conduit placement.

**NIST Control Mapping:**

- **IA-3 (partial):** Network-Based Device Identity Verification identifies OT and legacy devices by network signals and zone placement, and Gateway-Based Credential Proxying covers devices with no credential. Network Access Control (NAC/802.1X) holds modern endpoints.
- **IA-3(1) (partial):** Gateway-Based Credential Proxying and Constrained-Device Certificate Lifecycle Management provide cryptographic authentication indirectly. Most OT devices rely on non-cryptographic network signals instead, which keeps this partial.
- **IA-5 (partial):** Default Credential Remediation replaces default authenticators, and Credential Rotation via Maintenance Windows rotates them. Credential Management and Secrets and Credentials Protection hold the other slices.

**Deployment Type:** On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** OT/ICS Device, Network Infrastructure, OT/Legacy Device Identity

**External Dependencies:** The aircraft and ground station vendors, whose devices must accept program-issued identities.

**Security Impact:** Moderate

**Activities:**

- **ID-3.7.1: Default Credential Remediation**
    - **Description:** Inventory the OT and legacy devices that ship with vendor-default or well-known credentials, replace each default credential with a unique managed one, and record the remediated devices and any that cannot be changed.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries part of the outcome's IA-5 (partial) mapping by replacing vendor-default credentials. Gateway-Based Credential Proxying fronts devices whose defaults cannot change, and Credential Rotation via Maintenance Windows rotates the new credentials.

- **ID-3.7.2: Network-Based Device Identity Verification**
    - **Description:** Verify the identity of OT and legacy devices that cannot present a modern credential through network-layer signals, namely MAC address, traffic and protocol fingerprinting, and switch-port binding, anchored to each device's assigned zone and conduit within the network and environment focus area's IT/OT segmentation.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-3 (partial) mapping, inferring identity from network signals and zone-and-conduit placement when a device cannot present a credential. OT/Legacy Authentication Compensating Controls leans on it.

- **ID-3.7.3: Gateway-Based Credential Proxying**
    - **Description:** Where a device cannot authenticate on its own at all, place a gateway or protocol-translation proxy in front of it that holds and presents a managed credential to the identity platform on the device's behalf, so the device is reachable only through the authenticated gateway.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-3(1) (partial) mapping and contributes to its IA-3 (partial) mapping. The gateway authenticates cryptographically on the device's behalf and confines it behind an authenticated chokepoint, covering devices the other activities cannot reach.

- **ID-3.7.4: Constrained-Device Certificate Lifecycle Management**
    - **Description:** For OT and legacy devices that can support lightweight certificates but not the full enterprise PKI lifecycle, manage a constrained certificate lifecycle adapted to their compute and operational limits, with longer validity, simplified enrollment, and maintenance-window renewal, coordinating issuance with the Data focus area's key management and documenting the adapted lifecycle in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's IA-3(1) (partial) mapping for devices that can hold a lightweight certificate but cannot complete enterprise PKI enrollment. It adapts the Data focus area's certificate infrastructure to constrained hardware.

- **ID-3.7.5: Credential Rotation via Maintenance Windows**
    - **Description:** Schedule rotation of OT devices' remediated credentials, gateway credentials, and constrained certificates to align with planned maintenance windows rather than a continuous cadence, since many OT devices cannot have credentials rotated live without disrupting an operational process, and document the rotation schedule in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the remainder of the outcome's IA-5 (partial) mapping. Unlike Automated Secret Rotation, rotation here is window-bound and not tagged Automate, since live rotation would disrupt the process. It shares planned windows with OT/Legacy Scheduled Maintenance-Window Access.

## ID-4: Privileged Access Management

### ID-4.1: Privileged Access Control

**Design Intent:** Define privileged roles for each administrative surface, namely the cloud hub, each spoke, the cluster control planes, the data center, the alternate site, the PKI and HSMs, and the ground segment. A team's administrators can administer only that team's spokes, and Tier 0 roles go only to the Platform Team's named Tier 0 administrators. The Security Team and the CSSP get read and audit roles, never the administrative roles they check. The CSSP's only action right is running the pre-approved containment playbooks. No single role spans the HSMs and the cloud tenants, and the cloud tenant-owner roles are separate from day-to-day cloud administration so they can be held to the privileged access workstations.

**NIST Control Mapping:**

- **AC-3(7) (partial):** The privileged roles and their group-based baseline form the elevated half of a role-based access control policy. Non-Privileged Access Control holds the non-privileged half.
- **AC-6(5) (full):** the privileged role set and GBAC baseline restrict privileged accounts to organization-defined roles. Just in Time Access handles on-demand granting under AC-2(6).
- **AC-2(7) (partial):** cited for the first clause, administering privileged accounts under a role-based scheme. Access Reviews and the Operate pillar's Identity Change Tracking hold the rest.
- **AC-6(10) (partial):** privileged functions are reachable only through the privileged roles and groups defined here. Secure Compute Baselines holds host-level enforcement.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Privileged Access Management

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **ID-4.1.1: Platform-Defined Privileged Roles**
    - **Description:** Catalog and adopt the out-of-the-box privileged roles the identity platform ships, mapping each to the program's administrative needs and disabling those that grant broader elevation than any role legitimately requires, and document the resulting catalog in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Adopting built-in privileged roles first keeps the model close to the vendor baseline. Custom Privileged Roles extends it only where no platform role fits.

- **ID-4.1.2: Custom Privileged Roles**
    - **Description:** Design and build program-defined privileged roles for the administrative needs the platform's built-in privileged roles do not cover, scoping each to the minimum elevated permissions its function requires, and document the resulting catalog in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Custom privileged roles fill only genuine gaps and stay least-privilege, so none becomes a broad standing administrator role that undermines AC-6(5).

- **ID-4.1.3: Privileged Group Access Control (GBAC) Baseline**
    - **Description:** Define the group-based access control baseline that ties the platform-defined and custom privileged roles to the resources they administer, establishing the standard privileged groups, their role assignments, and the resources each group reaches, and document the resulting baseline in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This baseline binds privileged roles to resources through groups and carries the group-membership half of the outcome's AC-3(7) (partial) mapping. With the role definitions, it delivers the outcome's AC-6(5) (full) restriction. It also carries the outcome's AC-6(10) (partial) mapping, since accounts outside these groups hold no privileged function.

### ID-4.2: Privileged Access Workstations and Administrative Tiering

**Design Intent:** Administer Tier 0, which holds the identity provider, PKI, and HSMs, only from the physical privileged access workstations in the mission data center and at the alternate site. The cloud tenant-owner roles, which can change a tenant's own security and identity settings, are restricted to the same workstations. Other Tier 1 work runs from the Platform Team's host pool in the VDI spoke, reached from performer laptops. The CSSP's analysts get their own host pool. It reads the security monitoring platform and the cloud's native threat protection and runs the pre-approved containment playbooks, but grants no administrative access. Developers hold no privileged roles, so they need neither path.

**NIST Control Mapping:**

- **AC-6(2) (full):** an upper-tier credential cannot log on to the tier 2 workstation used for email and browsing, so nonsecurity work needs the separate non-privileged account.
- **AC-6(3) (partial):** Privileged Access Workstation Deployment and Hardening allows privileged network commands only from dedicated administrative workstations. The rest, documenting each need, is held by the AMP and SSP.
- **SC-2 (partial):** Administrative Tier Model Definition and Privileged Access Workstation Deployment and Hardening confine management functions to dedicated workstations and tiers. Authorized Cloud Access Point Integration holds the cloud management path.
- **Declined:** AC-6(5) stays with Privileged Access Control, which decides which roles hold elevated capability rather than where they are used. CM-2, CM-6, and CM-7 stay with Secure Compute Baselines and Endpoint Security, which produce and defend the PAW image.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Privileged Access Management, Privileged Access Workstation (PAW), Compute

**External Dependencies:** The performer, whose CMMC Level 2 laptops are the origin for Tier 1 sessions. The CSSP, whose analysts use their own host pool under its service agreement.

**Security Impact:** High

**Activities:**

- **ID-4.2.1: Administrative Tier Model Definition**
    - **Description:** Define the program's administrative tier model by assigning every system, service, and privileged role to a tier according to the blast radius of what it controls, with identity and directory control planes at tier 0, servers and enterprise applications at tier 1, and end-user workstations and devices at tier 2, and document the model and its tier assignments in the AMP.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** The tier assignment is the precondition the other activities enforce, made over the roles Privileged Access Control already defined. The identity platform, directory, PAM tooling, and CA sit at tier 0 because their compromise is recoverable only by rebuilding trust. Backup Coverage Strategy uses this assignment to place the identity fabric in its highest consequence tier.

- **ID-4.2.2: Privileged Access Workstation Deployment and Hardening**
    - **Description:** Issue dedicated privileged access workstations built from a restricted hardened image with email, general web browsing, and unapproved applications removed, and make them the only origin from which tier 0 and tier 1 administration is permitted.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: High; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-6(3) (partial) mapping by restricting privileged commands to hardened administrative devices. The image is a restricted profile of Secure Compute Baselines, so no configuration-management control is re-claimed. It is Level 2 because AC-6(2) credential separation is the mandatory floor, and High effort because every upper-tier administrator needs a dedicated workstation.

- **ID-4.2.3: Tiered Credential Isolation Enforcement**
    - **Description:** Enforce logon-restriction policy in the identity platform and on the systems themselves so that a credential belonging to one administrative tier cannot authenticate to a system in another, giving an administrator who works across tiers a separate account for each and never exposing an upper-tier credential on a lower-tier host.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-6(2) (full) mapping by denying upper-tier credentials any logon path to lower-tier systems, and the reverse. It prevents credential theft by reuse, where a tier 0 credential is left on a compromised workstation. It is High effort because per-tier accounts reach every administrator's workflow and every system's logon rights.

- **ID-4.2.4: Tiering Compliance Monitoring and Violation Alerting**
    - **Description:** Monitor sign-in and authentication telemetry for logons that cross a tier boundary or that reach an upper-tier system from a device that is not a privileged access workstation, and alert on each so the exposure can be dispositioned and the affected credential rotated.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity verifies that the outcome's AC-6(2) separation and AC-6(3) origin restriction hold, without a citation of its own. It reuses the sign-in telemetry of Identity Platform Protection Tool Deployment, and AC-2(7) does not fit because it watches where credentials are used. A violation is a credential-exposure event, so the upper-tier credential is rotated. It is Level 2 because it assures controls that are already mandatory.

### ID-4.3: Just in Time Access

**Design Intent:** Make every cloud, data center, and ground segment privilege eligible rather than standing, activated through the privileged access platform for a bounded window. Tier 1 elevation happens inside an admin VDI session, so the resulting credentials and tokens never reach the performer laptop. Activation for the PKI and HSMs needs a second approver.

**NIST Control Mapping:**

- **AC-2(6) (partial):** Time-bound activation and automatic expiration of privileged roles are runtime privilege changes. OT/Legacy Scheduled Maintenance-Window Access and Permissions Management hold the other shares.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Privileged Access Management

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-4.3.1: Privileged Access Management Tool Deployment**
    - **Description:** Deploy the privileged access management (PAM) or privileged identity management capability, whether a dedicated PAM platform or the identity platform's built-in privileged identity management feature, that enforces time-bound eligibility, activation, and expiration of privileged roles.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: High
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity stands up the mechanism the rest of the outcome configures, on the role model Privileged Access Control defines. Recurring Cost is a range, namely Moderate where the existing identity platform provides it and High where a dedicated PAM platform is procured.

- **ID-4.3.2: Time-Bound Role Eligibility Configuration**
    - **Description:** Configure in the PAM tool which identities are eligible to activate which privileged roles and the maximum activation duration each role permits, and document the eligibility and duration policy in the AMP.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Eligibility lets an identity activate a role without holding it, so no privileged role is held continuously. The maximum activation duration set here is the ceiling Automatic Expiration enforces.

- **ID-4.3.3: Activation Workflows**
    - **Description:** Configure the on-demand activation workflow through which an eligible identity elevates a privileged role for a bounded window, requiring justification, any required approval, and step-up authentication at activation time.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activation path owns time-bound privileged elevation, separate from Entitlement Lifecycle Workflows. With Automatic Expiration, it carries the runtime core of the outcome's AC-2(6) (partial) mapping. Step-up at activation reuses the User Authentication Controls authenticator policy.

- **ID-4.3.4: Automatic Expiration**
    - **Description:** Configure the PAM tool to automatically deactivate an elevated privileged role at the end of its activation window without manual revocation, returning the identity to its non-elevated default state.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Tool-enforced expiration makes elevation genuinely time-bound, replacing manual deactivation, so it is tagged Automate. With Activation Workflows, it carries the runtime core of the outcome's AC-2(6) (partial) mapping, enforcing the duration Time-Bound Role Eligibility Configuration sets.

### ID-4.4: Privileged Credential Vaulting and Session Brokering

**Design Intent:** Vault the built-in administrative accounts on the HSMs, network appliances, hypervisors, and out-of-band controllers, and broker and record every session that uses one.

**NIST Control Mapping:**

- **IA-5(6) (partial):** Vaulting, session injection, and rotation on return protect appliance and hypervisor administrative credentials. Secrets and Credentials Protection and outcomes in the Application and Artificial Intelligence focus areas hold the other populations.
- **AC-2(9) (partial):** The vault's release conditions govern when a shared account may be used. Emergency Access and OT/Legacy Authentication Compensating Controls cover the other shared-credential populations, which an AO tailoring this enhancement should confirm.
- **IA-2(5) (partial):** the administrator authenticates individually to the broker before the shared credential is injected. It is partial on the same population basis as AC-2(9).
- **AC-3(2) (partial):** Two-Person Integrity for Designated Privileged Actions gates dual authorization at the broker, alongside the agent and safety-critical slices other outcomes hold.
- **AU-14 (partial):** Privileged Session Recording and Monitoring records session content for the privileged sessions this outcome brokers. User Activity Monitoring holds the general user population, and legal-counsel consultation is handled in the AMP.
- **AU-14(3) (partial):** cited for a reviewer's ability to watch and end a privileged session in progress. It is partial on the same basis as AU-14.
- **AC-17(4) (partial):** recorded commands give remote privileged access its assessable evidence, with justifying needs recorded in the AMP. Secure Remote Access holds the network path.
- **Declined:** AC-6(3) stays with Privileged Access Workstation Deployment and Hardening, which restricts origin devices. AC-17(3) stays with Private Remote Access, since this broker sits on an internal path. AC-2(6) does not fit, since a checkout releases a credential rather than changing a standing account's privilege.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Privileged Access Management, Virtual Machine/Server, Network Infrastructure, Database Service

**External Dependencies:** None outside the boundary.

**Security Impact:** High

**Activities:**

- **ID-4.4.1: Privileged Credential Vaulting and Checkout**
    - **Description:** Bring every privileged account that cannot be role-activated under the privileged access management vault, including appliance and network-device administrative accounts, database engine superuser accounts, hypervisor and out-of-band management accounts, and standalone local administrator accounts, and release each credential only on a justified, approved, time-bound checkout that rotates it automatically on return.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-5(6) (partial) mapping and its AC-2(9) (partial) mapping. Rotation on return confines each credential value to one attributable checkout. It covers accounts Time-Bound Role Eligibility Configuration cannot reach, using the vault Privileged Access Management Tool Deployment stands up.

- **ID-4.4.2: Privileged Session Brokering**
    - **Description:** Route every privileged session to a vaulted account through the privileged access management broker, so the credential is injected into the connection by the broker and never reaches the administrator's workstation, clipboard, or terminal history.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** High
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's IA-2(5) (partial) mapping and completes its IA-5(6) (partial) one. The administrator authenticates to the broker with their own phishing-resistant authenticator, and the broker presents the shared credential to the target. A credential the administrator never sees cannot be cached or scraped from their workstation. It is Level 2 because vaulting and checkout already meet the mandatory obligation.

- **ID-4.4.3: Privileged Session Recording and Monitoring**
    - **Description:** Record each brokered privileged session, capturing the commands and keystrokes issued and the screen content displayed, retain the recordings under the program's audit retention requirements, and give authorized reviewers the ability to watch a session in progress and terminate it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Moderate
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AU-14 (partial) mapping for recording and its AU-14(3) (partial) mapping for real-time viewing and intervention. The checkout shows who held the credential, and the recording shows what they did. Retention and integrity draw on the Operate pillar's Log Retention Strategy and Audit Log Integrity Protection. This activity also carries the outcome's AC-17(4) (partial) mapping, so record remote privileged access needs and their rationale in the AMP.

- **ID-4.4.4: Two-Person Integrity for Designated Privileged Actions**
    - **Description:** Designate in the AMP the privileged actions the program's authorizing authority requires two authorized individuals to perform, such as security configuration changes, deletion or alteration of audit records, and cryptographic key operations, and enforce a second individual's approval or concurrent presence at the broker before each executes.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-3(2) (partial) mapping. It is Level 2, but mandatory where the authorizing authority requires two-person integrity, as in special access programs and some top secret environments. Keep the authority's list of designated actions short enough to enforce. The broker ensures the second individual authenticates separately and is not the requester.

### ID-4.5: OT/Legacy Scheduled Maintenance-Window Access

**Design Intent:** Grant ground control station and launch equipment maintenance access only within scheduled maintenance windows, never while an aircraft under that station's control is airborne. Model packages also load only in these windows, which ties this outcome to the edge release path in flow F6.

**NIST Control Mapping:**

- **AC-2(2) (partial):** Time-Bound Account Enablement and Automatic Disablement enables the temporary maintenance account for a window and disables it at the close. Emergency Access and Access Process for Third-Party Support hold the other temporary-account populations.
- **AC-2(6) (partial):** Scheduled, window-bound enablement gives OT and legacy systems bounded privilege where live elevation is impossible. It is tracked jointly with Just in Time Access and Permissions Management.
- **MA-2 (partial):** The maintenance activities schedule, approve, monitor, and review OT and legacy maintenance and verify account disablement afterward. Controlled Maintenance and Support and the PSO hold the rest, namely the off-site dimension, and post-maintenance verification reaches only this outcome's access controls.
- **MA-3(1) (partial):** cited for inspecting the maintenance tool itself for unauthorized modification. Controlled Maintenance and Support holds the IT estate's tools.
- **MA-3(2) (partial):** cited for checking a technician's media and diagnostic programs for malicious code before connection. It is partial on the same basis as MA-3(1).
- **MA-5 (partial):** Window-Bound Access Request and Approval authorizes maintenance personnel per window, and Post-Maintenance Access Review and Audit verifies they stayed in scope. The PSO holds the rest, principally escorting uncleared personnel.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** OT/ICS Device, Virtual Machine/Server, OT/Legacy Device Identity, Privileged Access Management

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-4.5.1: Maintenance Window Scheduling and Change Coordination**
    - **Description:** Establish the recurring schedule of maintenance windows for OT and legacy systems, coordinate each window with the change-management process and with the device-credential rotation that rides the same windows, and document the window schedule in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is the scheduling foundation the other activities attach to. Scheduling maintenance against change management is the first half of the outcome's MA-2 (partial) mapping. It shares outages with Credential Rotation via Maintenance Windows so the process is disrupted only once.

- **ID-4.5.2: Window-Bound Access Request and Approval**
    - **Description:** Require each person needing maintenance access to request it against a specific scheduled window, and route that request through documented approval that authorizes who may perform maintenance in that window and on which systems.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the authorization half of the outcome's MA-5 (partial) mapping, paralleling Activation Workflows for live elevation.

- **ID-4.5.3: Time-Bound Account Enablement and Automatic Disablement**
    - **Description:** Enable the maintenance account only at the start of its approved window and disable it automatically at the window's close, so no maintenance account remains active and usable outside a scheduled, approved window.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the core of the outcome's AC-2(6) (partial) mapping and the whole of its AC-2(2) (partial) mapping. It does for OT and legacy systems what Automatic Expiration does for live PAM roles. ConMon Activity is Continuous because, while windows are event-driven, enforcement runs always-on against them.

- **ID-4.5.4: Maintenance Session Monitoring and Recording**
    - **Description:** Monitor and record the privileged actions taken during each maintenance session through session logging or recording of commands and changes, so activity performed within a window is observable and reviewable after the fact.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** Session monitoring is the compensating assurance that work stayed in scope, since OT systems cannot enforce fine-grained authorization. Post-Maintenance Access Review and Audit reviews its records, which draw on AU-3 and AC-17 logging controls owned elsewhere.

- **ID-4.5.5: Window Extension and Escalation Process**
    - **Description:** Define the re-approval path for maintenance that legitimately runs past its scheduled window, requiring an explicit extension approval or escalation rather than letting the window's access silently continue, and document the process in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** An extension is a fresh approved decision, so an overrun cannot quietly defeat Time-Bound Account Enablement and Automatic Disablement. It parallels re-requesting activation under Just in Time Access.

- **ID-4.5.6: Post-Maintenance Access Review and Audit**
    - **Description:** After each window closes, review the recorded session activity against what was requested and approved, confirm the maintenance account was disabled on schedule, and document any deviation for follow-up.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity contributes to the outcome's MA-5 (partial) mapping by verifying that only authorized personnel acted in scope, and to its AC-2(6) and AC-2(2) (partial) mappings by confirming the account did not persist. It also carries the records-and-verification half of the MA-2 (partial) mapping. Discrepancies feed back into scheduling and approval.

- **ID-4.5.7: Maintenance Tool and Diagnostic Equipment Inspection**
    - **Description:** Inspect every maintenance laptop, programming device, and diagnostic tool brought to an OT or legacy system for improper or unauthorized modification, and scan the media and diagnostic software it carries for malicious code, before any of it is connected to equipment inside the window.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's MA-3(1) (partial) and MA-3(2) (partial) mappings, inspecting the tool for modification and its media for malicious code. It is the entry control the pattern otherwise lacks, since nothing else examines what a technician brings. It is Process and event-driven because people perform it at each arrival, and results are kept with the window's approval package.

### ID-4.6: Emergency Access

**Design Intent:** Keep break-glass accounts for the cloud tenant, the directory, and the ground segment. The two cloud accounts use different phishing-resistant methods. The directory set holds a domain account, each domain controller's Directory Services Restore Mode password, and a local administrator for each privileged access workstation, and every station has its own local account. All of those are console-only passwords under CCSD tailoring action 6, since their recovery cannot depend on the PKI or the directory they may be recovering. Cloud and directory sets are sealed in the data center and at the alternate site, and each station's account at its operating site, since an identity outage must never stop operators from recovering an airborne aircraft.

**NIST Control Mapping:**

- **AC-2(2) (partial):** This outcome owns the emergency population, with minimal provisioning, platform-independent authentication, time-boxed activation, and testing. OT/Legacy Scheduled Maintenance-Window Access and Access Process for Third-Party Support hold the rest, the temporary population.
- **AC-2(12) (partial):** Emergency Account Monitoring and Alerting treats any break-glass use as atypical. The Operate pillar's UEBA and the Data focus area's DLP hold the other monitored populations.
- **CP-13 (partial):** break-glass access is the alternative mechanism for access control when the identity platform is unavailable. It is partial because it covers only that one security function.
- **Declined:** IA-2(1) and IA-2(2) stay with User Authentication Controls, whose policy these accounts reuse.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Privileged Access Management, Virtual Machine/Server

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-4.6.1: Emergency Access Account Creation**
    - **Description:** Provision the minimal set of break-glass emergency accounts, seal their credentials under split-knowledge, out-of-band custody whose retrieval path does not depend on the primary identity platform, such as a hardware token or printed credential held in a safe under two-person control or a vault instance authenticating against an independent local path, and record each account's purpose, custodians, sealed-custody arrangement, and retrieval procedure.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Keep the population as small as possible, and hold every credential under split knowledge. The sealing mechanism must not depend on the identity platform, or the break-glass path fails in the outage it exists for. Use a physical safe under two-person control or a vault with an independent emergency retrieval path. Emergency Account Testing and Maintenance Procedures reseals the credentials after every use.

- **ID-4.6.2: Emergency Account Authentication Protections**
    - **Description:** Enforce phishing-resistant multi-factor authentication on every emergency account using the same authenticator-strength policy required of standing privileged accounts, selecting an authenticator that does not depend on the centralized identity platform being reachable.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity reuses the User Authentication Controls phishing-resistant policy rather than re-mapping IA-2(1)/IA-2(2). The authenticator must verify without the identity platform, such as an offline-capable hardware token, so an outage does not disable the second factor.

- **ID-4.6.3: Emergency Session Scope and Time-Boxing**
    - **Description:** Constrain each activated emergency account to a restricted permission scope and a time-boxed session that deactivates automatically at its bound, and exclude these accounts from conditional-access and adaptive policy evaluation, so break-glass access grants only the capability the emergency requires while staying usable when the policy engine itself is down.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity is the automatic-deactivation core of the outcome's AC-2(2) (partial) mapping, keeping an activated account scoped and time-limited. Excluding these accounts from adaptive policy is deliberate, since that engine depends on the platform whose outage the path must survive. Minimal population, sealed custody, platform-independent authentication, alerting on every use, and post-use rotation compensate for the exemption.

- **ID-4.6.4: Emergency Account Monitoring and Alerting**
    - **Description:** Generate a real-time, high-priority alert on any authentication or activation of an emergency account and route it to security operations, so that every break-glass use is surfaced immediately as an exceptional, reviewable event.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** Any break-glass use is atypical by design, which carries the outcome's AC-2(12) (partial) mapping. Organization-wide account-usage monitoring stays with the Operate pillar, and this activity draws on AU-6 logging owned elsewhere.

- **ID-4.6.5: Emergency Account Testing and Maintenance Procedures**
    - **Description:** Periodically exercise each emergency account and its documented break-glass procedure to confirm the credentials still function and the path is executable, rotate the credentials after every real or test use, document the test cadence in the AMP, and record the results of each test.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Semi-Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity guards against a break-glass path that fails because nobody tested it, while keeping tests exceptional. Rotate credentials after every real or test use and reseal them into the custody Emergency Access Account Creation establishes.

### ID-4.7: Access Process for Third-Party Support

**Design Intent:** Approve each vendor support session per support case, broker and record it, and end it when the case closes. Ground control station and payload vendors connect only within maintenance windows.

**NIST Control Mapping:**

- **MA-4 (partial):** Vendor Support Access Approval and Vendor Support Approval Workflows approve nonlocal maintenance, and Vendor Support Access Monitoring and Audit Logging monitors and records it. User Authentication Controls holds the strong-authentication obligation, which keeps this partial.
- **MA-4(1) (partial):** Vendor Support Access Monitoring and Audit Logging logs each session for anomaly review. The rest, the review itself, sits with the Operate pillar's detection capabilities.
- **AC-2(2) (partial):** Vendor Engagement Automatic Deactivation disables the engagement's temporary access at its approved bound. Emergency Access and OT/Legacy Scheduled Maintenance-Window Access hold the other populations.
- **PS-7 (partial):** This outcome sets and monitors per-engagement access requirements for vendor personnel. The PSO holds the broader external-personnel program.
- **AC-17(1) (partial):** Vendor Support Access Monitoring and Audit Logging monitors and controls vendor remote sessions. Virtual Desktop Monitoring and Alerting holds general remote sessions as a separate partial.
- **Declined:** AC-6(6) prohibits privileged access by non-organizational users, while this outcome grants it under AO tailoring. Its per-case approval, bounded scope, and recorded session are the compensating design that tailoring rests on.

**Deployment Type:** Cloud, On-Premises, Hybrid, Cyber-Physical System (OT/ICS)

**Affected Components:** Privileged Access Management

**External Dependencies:** Ground control station, payload, and launch equipment vendors, under their support agreements.

**Security Impact:** Moderate

**Activities:**

- **ID-4.7.1: Vendor Support Access Approval**
    - **Description:** Require each vendor support engagement to be requested against a specific, open support case and routed to an authorized sponsor or approver who determines the vendor engineer's eligibility, the systems in scope, and the time bound of the access, and document the vendor-support access policy in the AMP.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the per-engagement half of the outcome's PS-7 (partial) mapping and the approval obligation of its MA-4 (partial) mapping. An authorized local sponsor accepts accountability for each case. Unlike External User Sponsorship and Local Identity Binding, it authorizes one time-bound engagement rather than a standing identity.

- **ID-4.7.2: Vendor Support Approval Workflows**
    - **Description:** Configure the approval-routing workflow that carries a vendor support request through the required reviewers and any escalation path, and that fixes the access scope and duration each level of approval is permitted to grant.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity routes requests to the approvers and bounds what they may grant, paralleling Window-Bound Access Request and Approval. It contributes to the outcome's PS-7 (partial) and MA-4 (partial) mappings by making this path the only way vendor access is granted.

- **ID-4.7.3: Vendor Support Access Monitoring and Audit Logging**
    - **Description:** Monitor and record the vendor's session activity for the duration of the engagement and retain an audit trail of the access that was granted and the actions taken under it, so external support activity inside the environment is observable while active and reviewable afterward.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-17(1) (partial) and MA-4(1) (partial) mappings and the monitoring obligations of its MA-4 and PS-7 mappings. It draws on AC-17, AU-3, and AU-6 controls owned elsewhere. In an Air-Gapped/Isolated deployment, the vendor works on site under escort, and the escort's record goes into the same audit trail.

- **ID-4.7.4: Vendor Engagement Automatic Deactivation**
    - **Description:** Disable each vendor engagement's access automatically when the time bound its approval fixed elapses or the support case that justified it closes, without waiting on a sponsor or administrator to remember to revoke it.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Continuous
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity carries the outcome's AC-2(2) (partial) mapping and closes the termination obligation of its MA-4 (partial) mapping. An unenforced duration leaves an external party with access that outlives its case. It is tagged Automate because tool-enforced deactivation replaces the sponsor remembering to revoke, and its ConMon Activity is Continuous because enforcement runs always-on.

## ID-5: Account Management Planning

### ID-5.1: Account Management Plan (AMP)

**Design Intent:** Write one AMP covering every KESTREL identity population, including partners, AI agents, and OT devices. It records the assurance levels, the role bundles, the maintenance-window rules, and the ground control station session lock exception.

**NIST Control Mapping:**

- **AC-1 (partial):** this outcome operationalizes the account-management slice of access-control policy, while other focus areas hold the rest. AC-1 has no enhancements.
- **IA-1 (partial):** The AMP holds the procedures half through its authenticator, assurance-level, and session procedures. Security Policy Framework holds the policy tier.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Identity Platform

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-5.1.1: AMP Development and Authoring**
    - **Description:** Author the Account Management Plan, consolidating the assurance-level criteria, authenticator policy, service-account and OT credential-rotation procedures, and privileged-elevation eligibility produced across the focus area's four capabilities into a single governing document.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** One-Time
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity compiles determinations from all four Identity capabilities, such as Identity Assurance Level Determination and Phishing-Resistant Authenticator Selection (PIV/CAC/FIDO2). It depends on those determinations rather than defining them. AMP Periodic Review and Revision keeps it current.

- **ID-5.1.2: AMP Review and Approval**
    - **Description:** Route the drafted AMP through stakeholder review and secure formal approval from the accountable authority before it takes effect.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)

- **ID-5.1.3: AMP Periodic Review and Revision**
    - **Description:** Review the AMP on a defined cadence and revise it to reflect changes in the identity platform, account-management procedures, or governing requirements.
    - **Control Type:** Documentation
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 1 (Mandatory, required for ATO)
    - **ConMon Activity:** Periodic (Annual)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity supersedes the One-Time issuance produced by AMP Development and Authoring, keeping the plan current as the determinations it consolidates across the focus area's four capabilities change over time.

### ID-5.2: AMP Compliance Verification

**Design Intent:** Audit the identity provider, the privileged access platform, and the ground segment's account settings against the AMP, and report drift to the ISSM.

**NIST Control Mapping:**

- **CA-7 (partial):** This outcome verifies that AMP determinations hold in the live identity platform and PAM tool. The Operate pillar's ConMon capabilities hold the rest, namely organization-wide monitoring, and supply the telemetry consumed here.

**Deployment Type:** Cloud, On-Premises, Hybrid

**Affected Components:** Identity Platform

**External Dependencies:** None outside the boundary.

**Security Impact:** Moderate

**Activities:**

- **ID-5.2.1: AMP-to-Configuration Reconciliation**
    - **Description:** Compare live identity-platform, PAM tool, and account-management configuration against the determinations the AMP documents, such as assurance-level criteria, authenticator policy, role eligibility and duration, and credential-rotation cadence, and produce a variance report identifying where implementation has drifted from the written plan.
    - **Control Type:** Technical
    - **Cross-Cutting Discipline:** Automate
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Quarterly)
    - **Level of Effort:** Moderate
    - **Cost:** One-Time: Moderate; Recurring: Low
    - **Time Estimation:** Medium-term (3–6 months)
    - **Supplemental Guidance:** This activity is tagged Automate because a tool-driven reconciliation replaces manual document-by-document comparison of the AMP against live configuration. It runs on a repeatable cadence.

- **ID-5.2.2: AMP Compliance Finding Remediation and Escalation**
    - **Description:** Track each variance AMP-to-Configuration Reconciliation identifies through to remediation, and escalate findings that remain unresolved past a defined threshold to the accountable authority for risk acceptance or corrective action.
    - **Control Type:** Process
    - **Cross-Cutting Discipline:** None
    - **Maturity Model:** Level 2 (Recommended, strengthens ATO posture)
    - **ConMon Activity:** Periodic (Event-Driven)
    - **Level of Effort:** Low
    - **Cost:** One-Time: Low; Recurring: Low
    - **Time Estimation:** Short-term (1–3 months)
    - **Supplemental Guidance:** This activity owns each variance from detection through remediation or documented risk acceptance, closing the loop AMP-to-Configuration Reconciliation opens. It is event-driven because its only trigger is a variance from the quarterly reconciliation.
