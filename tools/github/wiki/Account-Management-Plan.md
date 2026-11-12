> **Notional system.** KESTREL is fictional. This page stands in for a governing plan in KESTREL's self-hosted Confluence. Its names, thresholds, and decisions are invented to show a completed Account Management Plan.

# KESTREL Account Management Plan (AMP)

This plan consolidates KESTREL's identity assurance levels, authentication and session rules, credential rotation, account lifecycle, access reviews, privileged access, emergency access, and vendor access into one governing document. It is the procedures half of the access control policy pairing, beneath the system security policy the program manager issues under Security Policy Framework (`GV-1.1`). It carries out the design decisions in the [Identity section of the SADD](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/02-identity.md) without naming the products that enforce them, which the [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/02-identity.md) does.

**NIST Control Mapping:** AC-1 (partial), held through ID-5.1. AMP Compliance Verification (ID-5.2) holds CA-7 (partial) for checking the running configuration against this plan.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| AMP Version | 0.1 |
| Date | 2026-11-11 |
| Prepared By | KESTREL ISSM, with the Platform Team's Tier 0 administrators and IT Operations |
| Approved By | Configuration Control Board, chaired by the chief engineer |
| Source SADD Version | 0.2 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-11 | KESTREL ISSM | Initial draft for Configuration Control Board review |

---

## Purpose and Scope

This AMP governs every identity inside KESTREL's authorization boundary, namely the people who use and run it, its workloads and service accounts, its AI agents, and its aircraft, stations, and launch equipment. It covers the IL5 cloud, the mission data center, the alternate site, and the UAS fleet. It does not govern the performer's laptops or the parent organization's devices, which their owners manage, though it sets the conditions those devices must meet to connect.

---

## 1. Identity Proofing and Population Management

*Traces to ID-1.1.1 and ID-1.1.6.*

| Population | Identity Assurance Level | How proofing is met | Why this level |
|---|---|---|---|
| Government and performer staff, including analysts, developers, data scientists, IT Operations, the Security Team, and the Program Office | IAL3 | Bound to the in-person proofing behind each person's CAC | Every role reads CUI, and most can change what KESTREL fields |
| UAS operators and Tier 0 and Tier 1 administrators | IAL3, plus sponsor approval for the role | CAC binding, and the PSO confirms the investigation the role requires | They can command aircraft or change the boundary |
| CSSP analysts and penetration testers | IAL3 | CAC binding, with sponsorship tied to the service agreement or the engagement | They reach KESTREL from outside its parent organization |
| Coalition partner users | IAL2 | Partner PKI or External Certificate Authority credential, with a named KESTREL sponsor | They see only products released to their own nation |
| Vendor support engineers | IAL2 | External Certificate Authority credential, sponsored per support case | Their access is bound to one case and one maintenance window |

An identity is re-proofed when any of the following occurs:

- The person moves into an operator role or a Tier 0 or Tier 1 role.
- The person's CAC, partner credential, or ECA credential is reissued, rather than renewed on the same identity record.
- The person returns after more than 12 months without a KESTREL account.
- A partner nation's agreement is renewed, which re-proofs every user from that nation.
- The person's name or citizenship record changes.

---

## 2. Authentication Policy

*Traces to ID-2.1.1, ID-2.1.4, ID-2.1.5, ID-2.1.6, ID-2.1.8, and ID-2.2.3.*

**Primary authenticators.** Every person authenticates with a hardware certificate, namely the CAC for DoD staff, performers, the CSSP, and penetration testers, and a partner PKI or ECA certificate for partners and vendors. No user role has a password path. FIPS 140-3 validated FIDO2 hardware keys are used only for break-glass accounts, under Section 11.

**Step-up.** A fresh certificate authentication is required to activate any Tier 0 or Tier 1 role, to approve a release to a partner nation, to approve an AI agent's action that affects a flight, and to approve a change in the Configuration Control Board's queue.

**Fallback when a CAC is unavailable.** A user whose CAC is lost or broken may receive a temporary FIDO2 hardware key from IT Operations, after in-person identity verification against the CAC record. It is valid for 14 days, grants no privileged role, and is revoked as soon as the replacement CAC is issued.

**Degraded revocation checking.** If the revocation service cannot be reached, services accept a cached response for up to 24 hours and then deny. Ground control stations validate against a locally cached revocation list refreshed at every maintenance window, so revocation outages never block an operator in flight.

**OT and legacy systems.** Ground control stations authenticate operators with a local smart card check, because the enterprise sign-in flow cannot be relied on during flight. Their compensating controls are the station's controlled operating area and the physical presence of the operator, as CCSD tailoring action 2 records. Launch and recovery equipment accepts maintenance access only through the brokered vendor path in Section 12.

**Invalid attempts.**

| Population | Limit | Counted over | Result |
|---|---|---|---|
| Users | 5 failed sign-ins | 15 minutes | Locked for 30 minutes |
| Privileged role activation | 3 failed attempts | 15 minutes | Locked until IT Operations unlocks it after verifying the person |
| Partner users | 5 failed sign-ins | 15 minutes | Locked for 60 minutes, and the sponsor is told |

The CAC itself locks after three incorrect PINs, which only a card issuance office can reset. Every sign-in screen masks the PIN, and every failure message says only that sign-in failed, never which factor was wrong.

---

## 3. Credential and Secret Rotation

*Traces to ID-1.5.4, ID-3.6.2, ID-3.7.4, and ID-3.7.5.*

| Credential | Cadence | Also rotated |
|---|---|---|
| The directory's Kerberos ticket-granting account key | Every 180 days, twice in succession | At once after any suspected Tier 0 compromise |
| Local administrator passwords on servers and workstations | Every 30 days, managed automatically | After every use |
| Service accounts of the directory, its cloud synchronization, and the certificate authorities | Every 90 days, or automatically where the account type allows | After any change in who administers them |
| Vaulted non-person secrets in production spokes | Every 30 days | At once on suspected exposure |
| Vaulted non-person secrets in dev/test spokes | Every 90 days | At once on suspected exposure |

OT and legacy devices that can hold a certificate get a constrained lifecycle. Certificates are valid for two years, enrolled with the manufacturer's tool during a maintenance window, and renewed in the window falling 60 days before expiry. Rotation of those certificates, of vendor gateway credentials, and of any credential remediated on fleet equipment rides the next maintenance window rather than a continuous cadence. Datalink keys are rotated as the KMP sets.

---

## 4. Account Lifecycle

*Traces to ID-1.8.3, ID-3.2.1, ID-3.3.1, and ID-2.4.1.*

**Dormancy.** An account with no sign-in for 35 days is disabled, and one dormant for 90 days is removed. Dormancy is checked daily. Privileged role eligibility lapses after 35 days without an activation.

**Departures.** A departure signal from the parent organization's or the performer's personnel system disables the account within 24 hours, across every segment including the ground control stations. Partner accounts end with their sponsor's agreement.

**Service accounts.** A service account is created only where workload identity cannot be used, through a service desk request naming its owner, purpose, scope, and expiry. The Platform Team lead and an ISSO both approve it.

**AI agents.** Every AI agent is registered as its own identity after the AI/ML Governance Review Board approves its use case. Registration records the owning team, the use case, every tool and data scope the agent may use, the human role that approves its actions, and a review date no more than one year out. The mission-planning agent is the first.

**Baseline access.** A new identity receives only the right to sign in and to reach the training and rules of behavior pages. Everything else comes from a role in Section 5, after training and the rules of behavior acknowledgment are complete.

---

## 5. Role-Based Access Control (RBAC/GBAC) Model

*Traces to ID-2.4.2 to ID-2.4.4 and ID-4.1.1 to ID-4.1.3, for the policy these activities embed. The role lists they produce are in the Appendix.*

KESTREL uses group-based access control. Permissions are granted to groups, and a person or workload gains access only through group membership, never through a one-off grant. Every role is built to the least privilege its function needs, whether the platform ships it or KESTREL defines it.

Team membership is part of every role, so a role never spans two mission teams' payload vendor data. A platform-shipped role that grants broader access than its tier warrants, such as a tenant-wide owner or contributor role, is disabled for daily use rather than adopted.

---

## 6. Access Review

*Traces to ID-1.9.1.*

| Campaign | Covers | Cadence | Reviewer |
|---|---|---|---|
| Privileged | Tier 0 and Tier 1 eligibility, and break-glass custodians | Quarterly | ISSM, with the Platform Team lead |
| Operators | Operator roles and approval rights for AI agent actions | Quarterly | Fleet Operations' operations lead |
| Partners | Every partner user | Quarterly | Each user's KESTREL sponsor |
| External parties | CSSP analysts, penetration testers, and vendor engineers | Quarterly | The sponsor named in each agreement or case |
| Team members | Analysts, developers, data scientists, and data engineers | Semiannually | Each team's product owner |
| Workloads and agents | Service accounts, workload identities, and AI agents | Semiannually | Each owning team lead |

A completed review certifies that each person or workload still needs the access, holds the right role, and has had unused entitlements removed. Access a reviewer has not confirmed within 14 days of the campaign's close is removed.

---

## 7. Session and Risk-Based Access

*Traces to ID-2.5.2, ID-2.6.1, ID-2.6.5, ID-2.6.7, ID-2.6.8, and ID-3.3.8.*

**Access decisions.**

| Condition | Result |
|---|---|
| A performer laptop that is not reporting as compliant | Deny |
| A partner session from outside that nation's expected networks | Step up, and deny if it persists |
| High sign-in risk from identity threat detection | Deny, and alert the Security Team |
| An operator signed in at a station they are not badged into | Deny, and alert the Security Team |
| Medium sign-in risk on a privileged activation | Step up |

**Session risk.** Each session's risk score rises with impossible travel, a changed device or network, token reuse from another device, and access to another team's data. A score above the high threshold ends the session and revokes its tokens.

**Lifetimes.**

| Session | Maximum | Idle timeout |
|---|---|---|
| User sessions, direct or through single sign-on | 8 hours | 15 minutes |
| VDI sessions | 8 hours | 15 minutes |
| Tier 1 activation | 4 hours | 15 minutes |
| Tier 0 activation | 1 hour | 10 minutes |

Access tokens last one hour. Refresh tokens are bound to the device that received them and are revoked when the session's risk rises.

**AI agent sessions.** Each agent task runs in a session lasting no more than 30 minutes. A task that calls a tool outside its registered scope, or that tries to reach anything able to task an aircraft, is suspended at once and an ISSO is alerted.

**Device lock and concurrent sessions.** Every KESTREL device locks after 15 minutes of inactivity, except a ground control station whose aircraft is airborne, as CCSD tailoring action 2 records. A user may hold three concurrent sessions, and a privileged role one.

---

## 8. SSO and Federation

*Traces to ID-2.3.1.*

KESTREL federates its applications with OIDC, using SAML only for COTS products that support nothing else. Every application joins single sign-on at intake, before it is first deployed. One sign-on covers the mission applications, such as the analyst portal, the signals workbench, and the LLM analyst assistant. Administrative consoles never share that session and always require their own fresh authentication.

---

## 9. Developer Secrets Workflow

*Traces to ID-3.6.3.*

Every developer's laptop runs the pre-commit secret scanning hooks the performer agreement requires. Developers fetch any secret they need for local testing from their own team's dev/test vault, using their own identity, and never keep secrets in local files. The pipeline templates and service scaffolds read secrets from the vault by workload identity, so no code ever needs a secret written into it.

---

## 10. Privileged Access Management

*Traces to ID-4.2.1, ID-4.3.2, ID-4.4.4, ID-4.5.1, and ID-4.5.5.*

**Tier model.**

| Tier | Covers |
|---|---|
| Tier 0 | The directory and identity provider, its cloud synchronization, the PKI and HSMs, the privileged access platform, and the cloud tenant-owner roles |
| Tier 1 | The cloud hub and spokes, every cluster, the data center and alternate site servers, the network fabric, and the security monitoring platform |
| Tier 2 | VDI desktops, the privileged access workstations as devices, and ground control station workstations |

Tier 0 roles may be activated only by the Platform Team's named Tier 0 administrators, from the privileged access workstations, for up to one hour. Tier 1 roles may be activated by each team's named administrators for that team's own systems, from the platform VDI host pool, for up to four hours. No privilege is standing.

**OT maintenance windows.** Each operating site has a weekly maintenance window for its ground control stations and launch equipment, scheduled by Fleet Operations and never held while an aircraft under that site's stations is airborne. Each window opens against a change record the Configuration Control Board has approved, and the device credential rotation in Section 3 rides the same window. Work that runs past the window stops until Fleet Operations' operations lead and an ISSO approve an extension.

**Two-person actions.**

| Action | Second person |
|---|---|
| HSM key generation, backup, and destruction | Present |
| Root and issuing certificate authority operations | Present |
| Retrieving break-glass credentials | Present, as the second custodian |
| Deleting audit records or shortening log retention | Approves |
| Deleting backups or changing backup retention | Approves |
| Expanding an AI agent's tool or data scope | Approves |

---

## 11. Emergency Access

*Traces to ID-4.6.5.*

KESTREL keeps break-glass accounts for the directory, the cloud tenant, and the ground segment, sealed in the data center with a second sealed set at the alternate site. Each set is exercised once a quarter by a planned use of the [Break-Glass Account Retrieval](Break-Glass-Account-Retrieval) runbook. Every credential is rotated after every real or test use, and each test's result is recorded.

---

## 12. Third-Party and Vendor Access

*Traces to ID-4.7.1.*

Vendor support access exists only for an open support case in the service desk. The lead of the team that owns the system sponsors it and decides which engineer may connect, which systems are in scope, and when access ends. Access ends when the case closes, or after eight hours, whichever comes first. Fleet vendors connect only within a maintenance window. Every vendor session is brokered and recorded.

---

## Appendix: Reference Catalogs and Configuration Data

These are maintained as data in the identity provider and the privileged access platform, and the location of each export is given here rather than its contents.

**Status Taxonomy and Marking Convention** *(ID-1.1.4)*: Directory attributes mark each identity as government, performer, partner with its nation code, CSSP, penetration tester, or vendor. Display names carry the matching prefix.

**Approved External Certificate Authorities** *(ID-1.2.1)*: The DoD-approved ECA providers and the partner PKIs named in each partner nation's memorandum of agreement, held in the identity provider's trust store.

**Assurance-Level-to-Resource-Sensitivity Mapping** *(ID-2.1.2)*:

| Resource sensitivity | Authenticator assurance |
|---|---|
| Key material and Tier 0 | AAL3 hardware certificate, fresh at activation, from a privileged access workstation |
| Mission data, releases, and Tier 1 | AAL3 hardware certificate |
| Shared reports and training content | AAL3 hardware certificate, or AAL2 for partners on released products only |

**Entitlement Catalog** *(ID-1.7.1)*: One access package per role in each team, exported quarterly from the identity provider for the access reviews.

**Non-Privileged Role Catalog / GBAC Baseline** *(ID-2.4.2 to ID-2.4.4)*: One group per role per team, such as imagery analyst for Mission Team 1 or signals analyst for Mission Team 2, exported from the identity provider.

**Approved Client Application Certificates** *(ID-3.4.2)*: The program PKI's issuing authorities, and the workload certificates each service accepts, held in the certificate management service.

**Privileged Role Catalog / GBAC Baseline** *(ID-4.1.1 to ID-4.1.3)*: One eligible group per tier and administrative surface, exported from the identity provider and the privileged access platform.

---

## Compliance Verification Cross-Reference

AMP Compliance Verification (ID-5.2) compares the identity provider's and the privileged access platform's running configuration with this plan each month.

**AMP-to-Configuration Reconciliation record location:** The security monitoring platform's identity posture dashboard, with each month's variance report attached to the ID-5.2 story in the tracker.

**Open compliance findings tracker:** The tracker, with each finding that cannot close within 30 days carried into the POA&M.

---

## Approval

**Approved By:** Pending. The Configuration Control Board reviews version 0.1.

**Circulated To:** the Platform Team, IT Operations, Fleet Operations, every team lead, the PSO, and the CSSP.

**Approval Date:** Pending.

---

## Periodic Review and Revision

**Review Cadence:** Annually, as a floor.

**Revision Triggers:**
- A change to the identity provider, the privileged access platform, or the cloud tenant's identity settings
- A new identity population, such as a new partner nation, payload vendor, or AI agent
- A change to an account-management procedure
- A change to a governing requirement
- A material finding from AMP Compliance Verification (ID-5.2) that cannot close without changing this plan
