# AU: Audit and Accountability

## AU-1

The program manager will issue the audit and accountability policy as part of KESTREL's system security policy. The Security Team's logging procedures will carry it out. The Configuration Control Board will approve both, and each will be reviewed at least once a year.

## AU-2

KESTREL will log the events that matter to its security. These include sign-ins and their risk, access decisions, privileged actions, configuration changes, data access and export, release events, agent tool calls, and the events from every security tool. The Security Team confirms each event class is present and reviews the list each year.

## AU-3

Each audit record will say what happened, when and where, its source, its outcome, and the identity behind it. A shared logging library gives each team's application the same record structure, and COTS output is normalized when it reaches Splunk.

## AU-3(1)

Records will carry the extra detail each source class needs. Examples are the parameters and approval of each agent tool call, and the object and partner behind each data release.

## AU-3(3)

Application logs will limit the personal information they record to what an investigation needs, and Presidio redacts personal information from inference logs.

## AU-4

Splunk will be sized to hold 12 months of searchable security logs, with StorageGRID holding 18 more. The Security Team monitors capacity, and storage warnings reach the logging administrators before space runs out.

## AU-5

A failure in logging will alert the Security Team. Splunk tracks every source's expected volume, and a source that goes silent or a pipeline that stops raises an alert.

## AU-5(1)

Splunk will warn the logging administrators when its storage approaches a set threshold, in time to add capacity before records are lost.

## AU-5(2)

A silent log source will raise a real-time alert within the hour, so a gap in logging is caught quickly.

## AU-6

The Security Team will review and analyze audit records in Splunk Enterprise Security, and report findings to the ISSM. The CSSP monitors the same telemetry around the clock under its service agreement, reading it through its own host pool.

## AU-6(1)

Review, analysis, and reporting will be integrated with response. Splunk SOAR enriches each alert, opens its ticket, and notifies the right people, so review flows directly into incident handling.

## AU-6(3)

Splunk will correlate records across every repository, from the cloud and the data center to the alternate site and the ground segment. One event can then be followed across all of them.

## AU-6(5)

Splunk will analyze audit records together with vulnerability scan results, performance data, and other monitoring, so a detection draws on all of them at once.

## AU-6(6)

Badge events from the physical access control systems will be correlated with sign-ins. An operator signed in at a station without having badged into that site raises an alert.

## AU-7

Splunk will reduce and report on audit records on demand, with searches, dashboards, and reports that leave the original records unchanged.

## AU-7(1)

Splunk will process audit records automatically, filtering and correlating them by the fields an analyst chooses, such as user, asset, or time window.

## AU-8

Every record will carry a time stamp from a shared reference. On-premises hosts take time from GNSS-disciplined SyncServer time servers, checked against DoD's authoritative time service, and cloud workloads use the provider's time service. Splunk alerts on drift between the two.

## AU-9

Audit records will be protected from change and deletion. Splunk writes each record to a StorageGRID bucket under S3 Object Lock in compliance mode, and no role holds the capability to delete logs. Break-glass access through CyberArk raises an alert.

## AU-9(2)

Audit records will be stored on a separate system from the components they describe. Splunk and its StorageGRID archive sit apart from the systems being logged, and all telemetry is also forwarded to the CSSP.

## AU-9(3)

Audit records will be protected cryptographically. Splunk hashes each batch it writes, GitLab's audit stream is hashed in batches, and the provenance ledger's entries are hash-chained and signed, so any alteration is detectable.

## AU-9(4)

Only named Security Team members will hold the logging administrator role. Platform Team administrators cannot change the audit records of the systems they run.

## AU-10

Actions will be bound to the people behind them. Each AI agent action records the principal who invoked it, so no one can deny an action taken on their behalf. Incident evidence is tracked through its collection, access, transfer, and release, so no one who handled an item can deny it.

## AU-11

Security logs will be kept searchable for 12 months and archived for 18 more, 30 months in all. Alert and investigation records are kept for 3 years, and longer where a case or POA&M item requires it. Incident evidence follows the IRP's retention terms.

## AU-12

Every component will generate audit records, with logging turned on when it is created. Cloud resources log through Azure Monitor diagnostic settings, and on-premises systems through Splunk forwarders. Applications log through the shared library, and the ground segment through the IT/OT DMZ. Azure Policy and a Splunk source check flag any component missing its logging.

## AU-12(1)

Splunk will assemble a system-wide audit trail, ordered by the shared time reference, and stitch each connection together across the circuits.

## AU-12(3)

During an investigation, authorized Security Team members will be able to change which events a component logs, or raise its detail, without stopping it. Each such change is itself recorded.
