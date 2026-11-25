"""Curated SCTM dispositions for KESTREL.

The build computes most of each row from the CCSD and the SADD. This file holds what only a
person can decide: which provider covers part of a control, which selected controls do not
apply, and which unclaimed controls an outcome already meets.
"""

# Providers KESTREL inherits from, each validated under Inherited Control Validation (GV-5.12).
PROVIDERS = {
    'azure': ('Azure Government', 'its IL5 provisional authorization, in both US Gov regions'),
    'disa': ('DISA', 'the Boundary Cloud Access Point, the internet access points, and DISN'),
    'pki': ('DoD PKI', 'CAC issuance and the DoD certificate authorities'),
    'cssp': ('the CSSP', 'its service agreement'),
    'cds': ('the cross domain service provider', 'the enterprise cross domain solution and its accreditation'),
    'parent': ('the parent organization', 'its enterprise security program, including the PSO and the alternate site facility'),
    'dod': ('DoD enterprise services', 'DoD issuances and JKO training'),
    'privacy': ('the DoD component privacy office', 'the component privacy program and its DoD-wide SORNs'),
}

# Provider portions. A key is a control ID or a two-letter family. A claimed control with a
# provider portion is Hybrid, and an unclaimed one is Inherited.
INHERITED = {
    'PE': (['azure', 'parent'], 'Physical protection of the cloud regions by Azure Government, and of the data center, the alternate site, and the operating sites under the PSO'),
    'PS': (['parent'], 'Personnel security under the PSO'),
    'PM-3': (['parent'], 'Security and privacy resourcing at the enterprise level'),
    'PM-8': (['dod'], 'Critical infrastructure planning at the department level'),
    'PM-13': (['dod'], 'The DoD cyber workforce program under DoDM 8140.03'),
    'PM-20': (['privacy'], 'Privacy program information published by the component'),
    'PM-20(1)': (['privacy'], 'Privacy policies on the component websites'),
    'PM-21': (['privacy'], 'Accounting of disclosures under the component privacy program'),
    'PM-24': (['privacy'], 'The component Data Integrity Board'),
    'PM-25': (['privacy'], 'Component policy minimizing PII in testing, training, and research'),
    'PM-26': (['privacy'], 'Complaint management under the component privacy program'),
    'PM-27': (['privacy'], 'Privacy reporting by the component'),
    'PT-4': (['privacy'], 'Consent mechanisms under the component privacy program'),
    'PT-6': (['privacy'], 'The DoD-wide SORNs covering user and service desk records'),
    'PT-6(1)': (['privacy'], 'Routine use review of the DoD-wide SORNs'),
    'PT-6(2)': (['privacy'], 'Exemption rules of the DoD-wide SORNs'),
    'IR-2(3)': (['privacy'], 'Breach response training under the component privacy program'),
    'IA-12(4)': (['pki'], 'In-person identity evidence validation at CAC issuance'),
    'AT-2': (['dod'], 'DoD cyber awareness and CUI training content on JKO'),
    'AT-3': (['dod'], 'DoD role-based training content on JKO'),
    'IA-5(2)': (['pki'], 'The DoD and External Certificate Authority trust anchors'),
    'SC-17': (['pki'], 'DoD PKI server certificates for user-facing edge services'),
    'SC-5': (['disa'], 'Network-layer flood absorption at the internet access points and the Boundary Cloud Access Point'),
    'SC-7': (['disa'], 'Boundary protection at the Boundary Cloud Access Point'),
    'SC-7(4)': (['disa'], 'Managed external telecommunications through the Boundary Cloud Access Point'),
    'CP-8': (['disa'], 'DISN transport for the circuits, with priority restoration'),
    'IR-4': (['cssp'], 'Around-the-clock triage and pre-approved containment'),
    'IR-6': (['cssp'], 'Reporting to the DoD reporting chain under CJCSM 6510.01B'),
    'SI-4': (['cssp'], 'Around-the-clock monitoring of forwarded telemetry'),
    'AU-6': (['cssp'], 'Review and analysis of forwarded telemetry'),
    'AC-4(8)': (['cds'], 'Guard filtering by the cross domain solution'),
    'AC-4(12)': (['cds'], 'Data type identifiers enforced by the cross domain solution'),
    'AC-4(15)': (['cds'], 'Detection of unsanctioned information by the guard'),
    'AC-4(17)': (['cds'], 'Domain authentication by the cross domain solution'),
    'AC-4(26)': (['cds'], 'Audit of filtering actions by the cross domain solution'),
    'AC-4(31)': (['cds'], 'Failed content transfer handling by the guard'),
    'MA-2': (['azure'], 'Maintenance of the cloud hardware'),
    'MA-4': (['azure'], 'Nonlocal maintenance of the cloud hardware'),
    'MA-5': (['azure'], 'Maintenance personnel for the cloud hardware'),
    'MA-6': (['azure'], 'Timely maintenance of the cloud hardware'),
    'MP-6': (['azure'], 'Sanitization of cloud storage media'),
}

# Selected controls that do not apply to KESTREL, with the reason.
NOT_APPLICABLE = {
    'AC-18(4)': 'KESTREL has no wireless LAN, and users cannot configure the datalinks.',
    'AC-19': 'KESTREL has no mobile devices, and its workstations never travel.',
    'AC-19(5)': 'KESTREL has no mobile devices, and its workstations never travel.',
    'PT-7(1)': 'KESTREL collects no Social Security numbers. Accounts key on the CAC DoD ID number.',
    'PT-8': 'KESTREL runs no computer matching program.',
}

# Unclaimed controls an outcome already meets. Each is a gap only in the SADD's mapping, and
# goes to the SADD's gap register for a claim.
MET_UNCLAIMED = {
    'AC-2(11)': ('ID-2.5', 'Conditional access sets the usage conditions on each account.'),
    'AC-3(14)': ('CO-4.2', 'The privacy officer handles individual access requests.'),
    'AC-4(4)': ('NE-2.4', 'Both hubs decrypt outbound TLS for inspection.'),
    'AU-3(1)': ('DE-2.1', 'Logging adds the detail each source class needs.'),
    'AU-3(3)': ('DE-2.4', 'Application logs limit the personal information they record.'),
    'AU-5(2)': ('DE-3.1', 'A silent log source alerts within the hour.'),
    'AU-6(5)': ('DE-3.1', 'Splunk correlates scan, performance, and log data.'),
    'AU-6(6)': ('ID-1.10', 'Physical and logical access events are correlated.'),
    'CA-3(6)': ('GV-5.6', 'The interconnection agreements authorize each transfer, still to be confirmed.'),
    'CM-3(6)': ('DA-3.13', 'Cryptographic changes go through the KMP and the Configuration Control Board.'),
    'CP-10(2)': ('RC-1.2', 'Point-in-time restore recovers transactions within each tier\'s recovery point.'),
    'IR-2(1)': ('RS-1.2', 'Responders train on simulated incidents.'),
    'IR-2(2)': ('RS-1.2', 'Training runs in the exercise environment.'),
    'IR-8(1)': ('RS-4.1', 'The IRP covers breaches of personal information.'),
    'MA-2(2)': ('DI-2.4', 'Maintenance is scheduled and recorded in Jira Service Management.'),
    'MA-4(3)': ('ID-4.7', 'Vendor sessions run from the vendor host pool, built to KESTREL\'s baseline.'),
    'MA-5(1)': ('DI-2.4', 'Uncleared vendor engineers are escorted at all times.'),
    'MP-6(3)': ('DI-5.1', 'The media intake station scans media before use.'),
    'PL-9': ('NE-1.1', 'Policy as code is defined once and deployed everywhere.'),
    'PT-5': ('CO-4.2', 'The account request form carries the Privacy Act statement.'),
    'PT-5(2)': ('CO-4.2', 'The Privacy Act statement is given where data is collected.'),
    'PT-7': ('CO-4.2', 'The PIA identifies any special category of personal information.'),
    'PT-7(2)': ('CO-1.1', 'Intelligence oversight bars collection on First Amendment activity.'),
    'SA-4(1)': ('GV-3.2', 'A contract clause requiring functional properties of security controls belongs in the contract security requirements, still to be confirmed.'),
    'SA-4(2)': ('GV-3.2', 'A contract clause requiring design and implementation information belongs in the contract security requirements, still to be confirmed.'),
    'SA-4(5)': ('GV-3.2', 'A contract clause requiring delivery in a secure configuration belongs in the contract security requirements, still to be confirmed.'),
    'SA-8(33)': ('AI-1.2', 'Privacy requirements minimize personal data by design.'),
    'SA-9(2)': ('GV-3.2', 'A contract clause requiring each external service to identify its functions, ports, and protocols belongs in the contract security requirements, still to be confirmed.'),
    'SA-16': ('GV-3.2', 'A contract clause requiring developer-provided training belongs in the contract security requirements, still to be confirmed.'),
    'SA-21': ('GV-3.2', 'A contract clause requiring screening of developers belongs in the contract security requirements, still to be confirmed.'),
    'SC-7(24)': ('DA-1.5', 'Data loss prevention watches personal information at the boundary.'),
    'SI-4(10)': ('NE-2.4', 'Both hubs decrypt outbound TLS for inspection.'),
    'SI-4(20)': ('DE-1.9', 'User activity monitoring covers privileged users.'),
    'SI-5(1)': ('RK-2.3', 'CSSP advisories arrive automatically as STIX over TAXII.'),
    'SI-7(2)': ('DI-5.4', 'File integrity monitoring alerts on violations.'),
    'SI-18': ('CO-4.2', 'The PIA sets how personal data accuracy is maintained.'),
    'SI-18(4)': ('CO-4.2', 'The privacy officer handles correction requests.'),
    'SR-9(1)': ('GV-3.4', 'Supplier assessments cover multiple stages of the supply chain, still to be confirmed.'),
}

# Controls whose only owners are narrow outcomes. The SADD's gap register asks the SCTM not to
# read them as system-wide, so each row carries this note until a system-wide owner is named.
NARROW = {'SI-7(5)', 'SI-6', 'SC-4', 'CM-6(2)', 'SA-5', 'AC-3', 'MP-8', 'SI-19(3)'}
