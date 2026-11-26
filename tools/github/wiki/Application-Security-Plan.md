> **Notional system.** KESTREL is fictional. This page stands in for a governing plan in KESTREL's self-hosted Confluence. Its names, thresholds, and decisions are invented to show a completed Application Security Plan.

# KESTREL Application Security Plan (ASP)

This plan sets how KESTREL's software is taken in, designed, written, reviewed, released, and protected once it runs. It gathers the Application focus area's standing decisions in one place. The teams that build software and the pipeline that gates it then read the same rules. It carries out the design decisions in the [Application](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/05-application.md) section of the SADD. It names the products that enforce them. The [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/05-application.md) is the record of each product selection, and a substitution there revises this plan.

**NIST Control Mapping:** SA-15 (partial), held through AP-6.1, for the review of the whole secure development process as one package. Each outcome this plan draws from holds its own slice of SA-15.

> **Phasing.** This plan is approved in Phase 1, since its thresholds gate the first releases. Some of its rules govern work that starts later. Adversarial code review, the approved library set, registry cleanup, and vulnerability disclosure start in Phase 2. Runtime protection starts in Phase 4. A rule marked "from Phase 2" or "from Phase 4" takes effect then.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| ASP Version | 0.1 |
| Date | 2026-11-25 |
| Prepared By | PMO ISSE, with the Platform Team for the pipeline sections, reviewed by the Security Team |
| Approved By | Configuration Control Board, chaired by the chief engineer |
| Source SADD Version | 0.8 |
| Source SIP Version | 0.6 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-25 | PMO ISSE | Initial draft for Configuration Control Board review |

---

## Purpose and Scope

This ASP covers every piece of software KESTREL builds or hosts inside its authorization boundary. That includes the mission teams' applications, the Data Team's ingest code, and the Platform Team's automation. It also covers the AI use cases and agents, and the COTS products KESTREL runs itself. It does not cover the provider services KESTREL inherits, though a new one still enters through Section 1. Remediation deadlines for flaws found after release belong to the Vulnerability and Patch Management Plan (VPMP). Model-specific testing belongs to the AI/ML Security Plan (AISP).

Certification to Field's Branch Protection Compliance Report (`AP-4.1`) and the Unified Vulnerability Dashboard (`AP-5.6`) check practice against this plan. Their findings feed the Splunk dashboards the owning teams and the PMO ISSE work from.

---

## 1. Application Intake and Onboarding

*Traces to AP-1.2.1 and AP-1.2.2.*

**One way in.** Every new application, service, agent, or COTS product enters through one intake request in Jira. So does a major addition to an existing one, such as a new external interface or a new data source. The request comes before design starts or a purchase is made. The PMO ISSE approves it before any work begins.

**What the request records.**

- What the software is for, and whether it is built or bought
- The owning team and its product owner
- The spoke or host it will run on
- The payload vendor terms it falls under, if any
- The expected delivery date

**The fixed questions.** Every requesting team answers the same questions at intake.

- **Data.** Will it handle CUI, payload vendor A or B data, mission imagery and signals, export-controlled technical data, or personal information?
- **Exposure.** Who can reach it: KESTREL staff only, mission partners, the internet through the access point, or the IL6 enclave?
- **Reach.** Can it send anything to an aircraft, a station, or a datalink?
- **Agents.** Can an AI agent call it, or is it an agent itself?

The answers set the threat model's rigor under Section 2 and decide whether Section 4's review applies. A wrong answer found later reopens the intake.

**What intake starts.** An approved request opens the threat model and the security impact analysis (`GV-5.11`). It also registers the application in Jira Service Management Assets, and nothing deploys without that record (`AP-4.7`).

---

## 2. Security Requirements and Threat Modeling

*Traces to AP-1.3.2 and AP-1.4.1.*

**Where the requirements come from.** The PMO ISSE derives them from the CCSD's control set. OWASP ASVS 5.0 Level 2 is the reference. Level 3 applies to anything partner-facing, internet-reachable, or callable by an agent. Each requirement enters the team's backlog as an acceptance criterion with a test that proves it. A product owner accepts no story until its security tests pass.

**The standing requirements.**

| Area | Requirement | How it is tested |
|---|---|---|
| Authentication | Users sign in only through Entra ID or Active Directory with a CAC or ECA credential. No application keeps its own accounts or passwords. | A request without a valid token is refused |
| Authorization | Access is denied by default and checked on the server for every object, scoped to the caller's team. | A test account for each role reaches only its own team's objects |
| Sessions | A session ends after 15 minutes idle and 8 hours in all. Sign-out ends it on the server. | A token used after either limit is refused |
| Input | Every input is checked on the server against a schema, and anything outside it is rejected. | Fuzzed and malformed inputs are rejected without an error trace |
| Output | Output is encoded for where it is shown. Errors show users a generic message, and detail goes only to the logs. | DAST finds no injection or reflected content |
| Logging | Sign-ins, access decisions, privileged actions, and data exports are logged to Splunk with the user, action, object, and result. | Each event appears in Splunk during the test |
| Cryptography | Only FIPS 140-3 validated modules through the platform libraries, with TLS 1.2 or later. No team writes its own cryptography. | SAST finds no unapproved algorithm or library |

**The methodology.** KESTREL threat-models with Threagile, using the program's custom image. That image adds IL5 rules and a risk engine that cites MITRE ATLAS for AI. Each model is YAML in the GitLab threat model repository. It is built from the program's modular templates and shared asset libraries, never from a blank page. A team starts by reusing the closest existing model for the same kind of architecture.

**What a model contains.**

- The technical assets and the data assets they hold
- The trust boundaries and the communication links that cross them
- The risks the image finds, each with its mitigation or acceptance
- For an AI use case or agent, its models, tools, and the data each tool can reach

**Rigor.** Anything partner-facing, internet-reachable, able to act on aircraft, or callable by an agent gets the full model. Anything else may model only its data flows and trust boundaries, from a template.

**The design gate.** The PMO ISSE reviews each model before building starts. Findings use Threagile's own scale, from Low to Critical, as the risk charter sets out.

| Severity | What the gate requires |
|---|---|
| Critical or High | Mitigated in the design, or accepted under Risk Acceptance Process (`RK-1.4`), before building starts |
| Elevated | A mitigation with an owner and a date, tracked in Jira |
| Medium or Low | Tracked by the owning team |

An accepted risk joins the Architecture Risk Tracking register (`AP-5.1`). A change that adds an interface, data flow, external connection, or agent tool makes the model stale. The pipeline catches it at merge (`AP-2.20`).

---

## 3. Secure Coding and Dependency Standards

*Traces to AP-2.2.1, AP-2.8.2, and AP-2.8.3.*

**Approved languages.**

| Language | Use |
|---|---|
| Go | New services and the Platform Team's automation |
| Rust | New services that parse untrusted or vendor-format data |
| Python | Machine learning, data pipelines, and agents |
| TypeScript | Web front ends |
| C or C++ | Only where a vendor SDK requires it, and always fuzzed (`AP-3.6`) |
| Java | Only where a vendor SDK requires it |

New services use a memory-safe language. A new service in C or C++ needs the PMO ISSE's approval, recorded at intake.

**Prohibited.**

- Evaluating or executing untrusted input, such as `eval` or a shell command built from it
- SQL or queries built by string concatenation
- Loading a pickled or serialized model or object from outside the program, unless ModelScan has passed it (`AI-4.7`)
- Turning off certificate or hostname checking
- MD5 or SHA-1 for any security purpose
- Secrets in code, configuration, or pipeline variables
- Rust `unsafe` blocks without a comment giving the reason and a Section 4 review

**Required patterns.** The first version takes its patterns from ASVS and the Application Security and Development STIG. Each annual review adds the flaw classes SAST and the penetration tests find most often in KESTREL's code.

**Build hardening.** The pipeline templates apply the compiler and packaging settings, such as position-independent executables and stack protection for C and C++. A build that drops them fails.

**Licenses.** The dependency review gate (`AP-2.8`) checks every component's license against this policy.

| Decision | Licenses |
|---|---|
| Accepted | MIT, BSD, Apache 2.0, ISC, Python Software Foundation, MPL 2.0 |
| Reviewed by program counsel | LGPL, EPL, the GPL family, and any source-available license, such as BUSL |
| Refused | AGPL and SSPL in anything KESTREL serves, and any component with no license or an unknown one |

**Provenance.** A component may be used only when it meets all of these.

- It resolves through Artifactory from that ecosystem's approved upstream (`AP-2.7`).
- Its release is at least 14 days old, so a malicious release has time to be caught.
- It has no known malicious version, as Xray reports.
- Its name does not imitate a reserved KESTREL name or a popular package.

Xray and GitLab Dependency Scanning check these at every merge request. A component that fails cannot merge without an exception under Risk Acceptance Process (`RK-1.4`). The exception records the reason, the compensating measure, and a review date.

---

## 4. Adversarial Code Review

*Traces to AP-2.10.1 and AP-2.10.2. From Phase 2.*

**Which changes need it.** A change needs adversarial review when it touches any of these.

- Authentication, authorization, or session handling
- Cryptography or key use
- Partner release logic
- The code that keeps payload vendor A and B data apart
- Any tool an AI agent can call, or an agent's instructions and tool configuration
- A new trust boundary or external interface, as the threat model shows

GitLab code owners mark these paths. The Security Team's approval is then a required check, so the merge button stays unavailable until it is given.

**Who reviews.** A Security Team member who holds the team's reviewer designation. The designation follows three reviews done alongside a designated reviewer. The reviewer is never from the authoring team.

**What the reviewer tries.** The reviewer reads the change as an attacker would. They try to bypass the control it implements, chain it with known weaknesses, and abuse logic the scanners cannot see. For an agent tool, they also try to make the agent misuse it. Any AI-assisted analysis runs on a model hosted in ML Prod.

**The record.** The review note on the merge request lists the attack paths tried, the findings, and how each was settled. A finding left open becomes a ticket with the VPMP's deadline. Code the coding agent wrote gets the same review as any other change.

---

## 5. Release Risk and Registry Hygiene

*Traces to AP-4.5.1 and AP-5.4.1.*

**Conditions that block outright.** A release cannot proceed while any of these hold.

- An open Critical finding from any scanner
- An open High finding from SAST, dependency, container, or DAST scanning
- A verified secret in the code or its history
- A missing signature, provenance attestation, or SBOM
- A failed runtime baseline check in stage (appendix)

**The score.** Every other open finding adds points. Each scanner's severity is first mapped onto one scale, from Critical to Low.

| Finding | Points |
|---|---|
| High from IaC, API fuzzing, or ASD STIG checks | 8 |
| Medium from any scanner | 3 |
| Low from any scanner | 1 |

Points double for anything partner-facing, internet-reachable, or callable by an agent, as intake recorded.

**The threshold.** A release scoring 20 or less carries Very Low residual risk and proceeds on the pipeline's evidence. Every release is CCSD row 10, so a release scoring above 20 goes to the PMO ISSE. The PMO ISSE sends it back, or approves it once fixes or compensating measures bring it back to Very Low. Anything still above Very Low goes to the AO under Risk Acceptance Process (`RK-1.4`). Open findings in a release that proceeds become tickets with the VPMP's deadlines.

**Registry retention, from Phase 2.** Artifactory keeps these images:

- Every fielded release
- The certified release before it, for rollback (`AP-4.6`)
- Every release baselined to the IL6 enclave

Candidate builds are kept for 90 days, and dev/test images for 30. A weekly job deletes any image past its window that no running deployment, tagged release, or rollback target references. A monthly report shows where the registry departs from these rules.

---

## 6. Runtime Protection and Vulnerability Disclosure

*Traces to AP-5.9.2 and AP-5.10.1.*

**RASP policy, from Phase 4.** Contrast Protect instruments the analyst portal, the signals workbench, the partner API, and the LLM analyst assistant's front end. Each starts in monitor mode. It moves to blocking after 30 days without an unexplained false positive, with the Security Team's approval.

| Treatment | Detection classes |
|---|---|
| Blocked | SQL and command injection, path traversal, unsafe deserialization, expression language injection, XML external entities |
| Logged and reported | Cross-site scripting, method tampering, and probing that matches no rule |
| Suppressed | None today. A suppression needs the Security Team's approval and is reviewed each quarter. |

Every event goes to Splunk. No application deviates from this default yet. A deviation is recorded here with its reason.

**Vulnerability disclosure, from Phase 2.** KESTREL's internet-reachable endpoints are enrolled in the DoD Vulnerability Disclosure Program, which DC3 runs.

- **Scope.** The endpoints behind the access point, up to the sign-in page. Every role needs a CAC or ECA credential, so nothing past sign-in is in scope. The PMO ISSE confirms this scope with DC3 at enrollment.
- **Allowed testing.** What the DoD program's policy permits. Denial of service, social engineering, and physical testing are never allowed.
- **Response times.** DC3 acknowledges each report and sets disclosure timing. The Security Team triages each relayed report within 3 business days, and the fix follows the VPMP's deadlines.
- **Intake.** DC3 relays reports to the Security Team's monitored Jira queue, which the Security Team lead owns. Each report is tracked to closure like a penetration test finding.

---

## Appendix: Reference Catalogs and Configuration Baselines

Each item below is living data that the pipeline or a team consults, kept where its tool reads it.

**Approved Component and Paved-Road Template Catalog** *(AP-2.2.2, from Phase 2)*: Two parts, held in GitLab.

- **Products.** The open-source and source-available products the Security Implementation Plan selects, such as PyRIT, promptfoo, and Threagile. The Security Team admits each one after checking its license, provenance, and maintenance. It also checks for any call outside the boundary. Remote features and telemetry must be turned off, as with promptfoo and SonarQube for IDE. Each product is mirrored through Artifactory. Program counsel confirms a source-available license first. The supply chain risk management plan's review applies too.
- **Libraries and templates.** The vetted libraries for each approved language, plus one service template per language. Each template comes with Entra ID sign-in, the platform cryptography libraries, schema input validation, and Splunk logging already wired in. Every new service starts from one.

**Runtime Configuration Baseline** *(AP-4.4.1)*: A versioned baseline kept with each release in GitLab and checked by Gatekeeper and Conftest in stage. Its defaults are these:

- **Identity:** a workload identity per service, with no shared or long-lived credential
- **Privileges:** a non-root user, dropped capabilities, and a read-only filesystem
- **Limits:** resource limits set
- **Interfaces:** only the interfaces the threat model lists exposed
- **Transport:** TLS 1.2 or later
- **Response headers:** CSP `default-src 'self'` with no third-party sources, HSTS, `X-Content-Type-Options: nosniff`, and `frame-ancestors 'none'`
- **Cookies:** Secure, HttpOnly, and SameSite=Strict
- **CORS:** only the origins listed in the baseline
- **Logging and diagnostics:** logging to Splunk, with debug endpoints and stack traces turned off

---

## Approval

**Approved By:** Pending. The Configuration Control Board reviews version 0.1 in Phase 1, after the Security Team's review.

**Circulated To:** the Platform Team, the mission teams, the Data Team, the ML Team, the Security Team, and the CSSP.

**Approval Date:** Pending.

---

## Periodic Review and Revision

**Review Cadence:** Annually, as a floor. The first review falls in Phase 2.

**Revision Triggers:**
- A change to the coding standard, the approved languages, or the component catalog
- A change to a release threshold or the scoring model
- A new kind of application, such as the first agent with tools that reach the fleet
- A change to the application threat landscape, such as a new class of attack on agents
- A change to a governing requirement
- A material finding from the Branch Protection Compliance Report or the Unified Vulnerability Dashboard showing practice no longer matches this plan
- A product substitution recorded in the Security Implementation Plan, for any product this document names
