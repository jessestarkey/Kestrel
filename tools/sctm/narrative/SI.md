# SI: System and Information Integrity

## SI-1

The program manager will issue the system and information integrity policy as part of KESTREL's system security policy. The Vulnerability and Patch Management Plan will hold the flaw remediation procedures. The Configuration Control Board will approve both, and each will be reviewed at least once a year.

## SI-2

Flaws will be found and fixed on the VPMP's deadlines, which are shorter for the DMZ, Tier 0, and the fleet. ACAS scans every host from Phase 1, and Dependency-Track checks every fielded release's SBOM daily. Patches move through dev, test, and stage before production, and container images are rebuilt rather than patched. Fleet patches must be validated by the manufacturer and tried on a spare.

## SI-2(2)

Splunk and Jira Service Management will track every finding's remediation status automatically against its deadline, and report findings past their deadline in each continuous monitoring cycle.

## SI-3

Malicious code protection will run at every entry point. Defender for Endpoint runs on every server, workstation, and VDI desktop, and Defender for Containers protects every cluster. ClamAV scans every package and image the mirror fetches and every build artifact. ModelScan checks every model file before it can load.

## SI-4

KESTREL will monitor itself in every location. Splunk Enterprise Security correlates telemetry from endpoints, identity, the network, the cloud, data services, the models, and the ground segment. The CSSP monitors the same telemetry around the clock under its service agreement. Monitoring is tightened after an incident and around any asset that cannot be patched.

## SI-4(2)

Monitoring will use automated tools for real-time analysis. These are Defender for Cloud and Defender for Identity for their services, Defender for Endpoint on hosts, and Splunk Enterprise Security correlation across them.

## SI-4(4)

Inbound and outbound traffic will be monitored at the hubs and at each ground segment conduit. On the conduit, the firewall parses the command and control protocol and blocks any command a station is not approved to send.

## SI-4(5)

Systems will raise alerts when indicators of compromise appear. These include EDR detections, sign-in risk, unusual data access, deviations on the ground segment, and spoofing or jamming of navigation signals.

## SI-4(10)

Both hubs will decrypt outbound TLS for inspection. Mutual TLS between workload identities is exempt, since decrypting it would break the identity it carries.

## SI-4(12)

Splunk will alert the Security Team automatically on events that need attention, such as model-serving abuse that spans several endpoints.

## SI-4(14)

From Phase 2, Bastille sensors will detect rogue access points and unauthorized radios at the data center and the alternate site. They extend to each operating site in Phase 3.

## SI-4(20)

CyberArk will record every privileged session and let reviewers watch it live and end it. User activity monitoring covers privileged users in particular.

## SI-4(22)

The pipeline will compare observed reachability with the registered ports, protocols, and services on every change, so an unauthorized network service is found.

## SI-5

The Security Team will receive security alerts and directives, such as IAVM notices and CYBERCOM tasking orders, through the CSSP. Each directive opens a Jira ticket, and its remediation is tracked against the directive's own compliance date. The CSSP's indicators arrive with a confidence tier and an expiry.

## SI-5(1)

Advisories and indicators from the CSSP will arrive automatically, as STIX over TAXII.

## SI-6

Security functions will be checked to confirm they still work. Boot integrity attestation and file integrity monitoring verify hosts, and canary prompts with known answers run daily against every fielded model to confirm its guardrails have not changed.

## SI-7

Software and information will be protected against unauthorized change. Tamper protection keeps the EDR agent running, and exploit protection guards every host. The applications serve only their own client code, with content security policies blocking anything else.

## SI-7(1)

Integrity checks will run wherever a change would matter. File integrity monitoring covers Tier 0, and training environments check their own hashes before each run. Training data, recalled agent memory, and retrieved documents are checked before they are used. The retraining pipeline is compared with its certified version each week.

## SI-7(2)

File integrity monitoring will alert the Security Team on any integrity violation it finds.

## SI-7(5)

An integrity violation will trigger an automatic response where it is safe to do so. A training batch that fails its screens is blocked from the training zone, and a host that fails integrity checks is flagged for response.

## SI-7(7)

Integrity violations will feed incident response directly, raising alerts in Splunk that open incident records under the IRP.

## SI-7(15)

Code will be authenticated before it is installed or run. Release images and packages are signed with Cosign, and only signed images with a Certification to Field attestation are admitted to production. Pretrained checkpoints are checked against their publisher's signature or digest, and reference and trained models are signed. Firmware is verified against its manufacturer's signature or published hash.

## SI-10

Inputs will be validated before they are used. The WAF and API Management check each request against its schema, and the model endpoints check type, size, and format before LLM Guard screens prompts for injection. Training labels and retraining records are validated for schema, ranges, and floods.

## SI-11

Applications will show users a generic error and send diagnostic detail only to logs that authorized staff can read.

## SI-12

Information will be kept only as long as the DMP's retention schedule allows, then disposed of as it sets out. Registry images and model versions expire on the ASP's and the AISP's schedules, and agent memory entries expire after 180 days. Evidence is kept in immutable storage for as long as its rules require.

## SI-12(1)

Personal information will be limited to what each purpose needs. Presidio redacts personal information from inference logs, and the DMP's minimization rules cover every other record.

## SI-12(2)

Test, training, and research data will hold no identifying text, and no imagery of people unless the AISP's privacy requirements allow it.

## SI-12(3)

Information will be disposed of with the method the DMP sets for each kind. Drives are purged on site with Blancco, HSMs are zeroized, and cloud media is sanitized by the provider.

## SI-16

Memory will be protected from unauthorized code execution. Exploit protection applies data execution prevention and address space randomization on every host, and virtualization-based security isolates credential stores. The pipeline applies compiler hardening settings to every build.

## SI-18

The Privacy Impact Assessment will set how the accuracy of personal information is maintained. Account records are synchronized against the authoritative source.

## SI-18(4)

The privacy officer will handle requests from individuals to correct their personal information.

## SI-19

Personal information will be removed or masked before data is used for testing, training, or release. Presidio removes identifying text, and people in imagery are blurred or cropped, by a Data Team reviewer until the person-detection model is certified. The privacy officer approves each technique.
