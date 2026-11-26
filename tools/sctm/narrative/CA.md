# CA: Assessment, Authorization, and Monitoring

## CA-1

The program manager will issue the assessment, authorization, and monitoring policy as part of KESTREL's system security policy. The Continuous Monitoring Plan will hold the procedures. The AO approves the Continuous Monitoring Plan, and both are reviewed at least once a year.

## CA-2

The SCA will assess KESTREL's controls under a Security Assessment Plan written from the SCTM, starting on 2028-07-31. The assessment covers the cloud, the data center, the alternate site, the fleet through spares and the simulator, and each model through its evidence annex. Inherited controls are assessed by reviewing each provider's package. After authorization, controls are reassessed on the Continuous Monitoring Plan's calendar.

## CA-2(1)

Assessments will be performed by the SCA, who is independent of the teams that build and run KESTREL.

## CA-2(2)

Specialized assessments will add depth where it matters: penetration testing each year, AI red teaming of each new use case, and adversary emulation from Phase 4.

## CA-3

Each information exchange with an outside system will rest on a signed agreement, stored in Confluence and recorded in eMASS. The CSSP and access point agreements are signed in Phase 1, and partner nation agreements before each partner's first release. Each is reviewed every year and whenever its connection changes.

## CA-3(6)

Each transfer across the cross domain solution will be authorized. Low-to-high baselines need Certification to Field approval before they are staged, and high-to-low products need the IL6 enclave's release review. The interconnection agreements authorize each type of transfer.

## CA-5

POA&M items will live in eMASS from Phase 1, covering the conditions of the interim authorization to test, assessment findings, missed remediation deadlines, and open STIG findings. Milestones are reviewed each month and reported to the AO each quarter, and an ISSO closes an item only after verifying the fix.

## CA-6

The AO will grant an interim authorization to test in Phase 1. It covers the spare aircraft and the simulator, the access point and CSSP connections, and the prior collection. The ATO decision is due on 2028-09-30, on the full package the ISSM submits in eMASS. After that, the authorization is kept current through ongoing authorization, with agreed reauthorization triggers and a status report to the AO each quarter.

## CA-7

KESTREL will be monitored continuously under the Continuous Monitoring Plan. Each check has a frequency and an owner, and its results reach the Splunk posture dashboard and eMASS. The checks range from account reconciliation, vulnerability and application findings, and backup health to model drift and re-testing. The ISSM reports to the AO each quarter.

## CA-7(1)

The SCA will perform the independent portion of continuous monitoring, reassessing controls on the calendar the Continuous Monitoring Plan sets.

## CA-7(4)

Risk monitoring will cover accepted risks as well as open findings. Accepted design risks and risk acceptances carry review dates, and the steering committee reviews the risk register each month.

## CA-8

Independent penetration testers will test all of KESTREL each year, and the paths reachable from outside every six months, starting in Phase 2. They also test after a major change. Fleet systems are tested on spares or the simulator, and each finding becomes a POA&M item retested before it closes.

## CA-8(1)

The penetration testing provider will be independent of the performer, under its own contract and rules of engagement. The ISSM scopes each test, so the people who designed a control do not scope its check.

## CA-9

Internal connections between KESTREL's components will be documented and reviewed. Managed services connect only inside their spoke's subnets, through the hub's routes and inspection. Each quarter, the Platform Team removes any internal connection that no longer matches a documented flow.
