# IR: Incident Response

## IR-1

The program manager will issue the incident response policy as part of KESTREL's system security policy. The Incident Response Plan will hold the procedures. The Configuration Control Board will approve both, and each will be reviewed at least once a year.

## IR-2

Everyone with an incident response role will be trained on KESTREL's runbooks when they take the role and each year after. That covers the Security Team, the Platform Team, IT Operations, the Data Team, and Fleet Operations.

## IR-2(1)

Training will include simulated incidents, so responders practice the runbooks rather than only reading them.

## IR-2(2)

Training will run in the exercise environment, which mirrors production's tools without touching production.

## IR-2(3)

Training on responding to a breach of personal information will come from the DoD component privacy program, which KESTREL inherits.

## IR-3

The IRP will be tested twice a year by tabletop exercise, one with an aircraft or ground segment scenario and one with an AI scenario. From Phase 3, a functional exercise each year uses the real tools with the CSSP. Each exercise's findings are tracked, and the IRP is updated from them.

## IR-3(2)

Exercises will be coordinated with the owners of related plans. The yearly functional exercise includes the Contingency Plan's owners and the CSSP, and it rehearses the handoff from incident response to recovery.

## IR-4

Incidents will be handled through preparation, detection and analysis, containment, eradication, and recovery, as the IRP sets out. The ISSM leads each one in Jira Service Management, and owning teams act on their own systems at the ISSM's direction. The CSSP triages around the clock and contains what cannot wait through pre-approved playbooks. Fleet containment is manual, and nothing acts on an aircraft in flight.

## IR-4(1)

Incident handling will be automated where it is safe. Splunk SOAR enriches incidents, opens and updates their records, and runs containment playbooks that can take only listed actions. Accounts are disabled and sessions revoked automatically, and non-production hosts are isolated automatically.

## IR-4(4)

Information from every incident will be correlated in Splunk Enterprise Security and Defender XDR, so related events across hosts, identities, and the network are seen as one incident.

## IR-4(11)

One integrated incident response team will handle every incident. The ISSM leads it, with the Security Team, the CSSP, and the owning teams' responders working from the same runbooks and the same record.

## IR-5

Every incident will be tracked in its Jira Service Management record, from declaration to closure, with its actions, findings, and evidence.

## IR-5(1)

Correlated alerts above the declaration threshold will open an incident record automatically. Each record collects the affected asset's owner, team, criticality, and recent changes as the incident proceeds.

## IR-6

Incidents will be reported on the IRP's time limits. The ISSM notifies the AO, and the CSSP reports up the DoD reporting chain under CJCSM 6510.01B. The foreign disclosure officer notifies partner nations, the privacy officer reports breaches of personal information, and the performer reports incidents on its own laptops to DC3.

## IR-6(1)

A declared incident will notify the CSSP's operations center and page the on-call analyst automatically. If the service desk or the circuits are down, Splunk pages directly, sending only an incident ID and severity.

## IR-6(3)

Incidents that involve a supplier's product will be coordinated with that supplier, under the notification terms in its contract.

## IR-7

The CSSP will provide incident response support around the clock under its service agreement, including triage and pre-approved containment. The ISSM tracks each CSSP directive to completion.

## IR-7(1)

Splunk will forward all telemetry to the CSSP automatically, so its analysts have the same information as the Security Team, and a stalled feed raises an alert.

## IR-8

The ISSM will have an interim IRP approved in Phase 1 for the interim authorization to test, covering declaration, reporting to the CSSP, and who acts. The full IRP, with its runbooks, follows in Phase 2. It is revised each year and after each exercise.

## IR-8(1)

The IRP will cover breaches of personal information, including the privacy officer's reporting duty and the notice owed to the people affected.
