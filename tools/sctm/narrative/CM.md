# CM: Configuration Management

## CM-1

The program manager will issue the configuration management policy as part of KESTREL's system security policy. The Configuration Management Plan (CMP) will hold the procedures that carry it out. The Configuration Control Board will approve both, and each will be reviewed at least once a year.

## CM-2

KESTREL's baselines will come from DISA STIGs and SRGs, with the Cloud Computing SRG's IL5 requirements in the cloud. They are held as code. Landing zone modules define the cloud's hub and spokes, and Packer images define servers and VDI desktops. Containers start from Iron Bank base images, managed services follow Azure Policy initiatives, and Ansible roles carry the baselines on premises. Fleet equipment follows each manufacturer's hardening guidance, and each release carries a versioned runtime baseline.

## CM-2(2)

Baselines will be kept current and accurate by the same automation that applies them. The landing zone modules, Packer images, and Ansible roles live in GitLab. A change to a baseline is therefore a reviewed merge request, and every new build picks it up. Training environments pin their dependencies and image digests, and each run checks its environment against the approved baseline before it starts. System prompts are versioned with each release in the same way.

## CM-2(3)

Previous configurations will be kept so a change can be rolled back. GitLab keeps the full history of every baseline and policy as code. Artifactory keeps every fielded release and the certified release before it, and the model registry keeps each model's prior certified version. Backups keep each system's configuration as part of its tier's backup policy.

## CM-2(7)

The privileged access workstations are KESTREL's only endpoints that stay outside the VDI pools, and none of them travels. They are enrolled in Configuration Manager in the Tier 0 enclave and held to a dedicated compliance policy. KESTREL has no mobile devices, so no travel configuration is needed.

## CM-3

Every change will have a change record. For anything defined as code, that is the merged GitLab merge request, approved by a second reviewer. Jira Service Management holds the record for everything else, including fleet changes. System prompts change only through the pipeline, reviewed like code. Changes to the shared firewall rule base, the identity provider, or an interconnection go to the Configuration Control Board, which the chief engineer chairs. Emergency changes run through CyberArk and are reviewed within two business days.

## CM-3(1)

GitLab will enforce change control automatically. Protected branches block a merge until its required approvals and checks pass. Code owners mark sensitive paths, such as pipeline definitions, infrastructure as code, admission policy, and agent configuration. A change to one needs extra approval and raises an alert in Splunk. Open Policy Agent rejects changes that break policy in the pipeline and at cluster admission. Privileged changes to training configuration alert the ML Team and the Security Team.

## CM-3(2)

Changes will be tested before they reach production. Cloud changes go first to the owning team's stage cluster. Tier 0 and data center changes go to the alternate site's standby or a lab, and a change with neither records an exception and gets extra checking afterward. A compliance scan after the change closes its record.

## CM-3(4)

Security sits on the change path itself. A change to a sensitive repository path needs the Platform Team's and the Security Team's approval beyond the team's own reviewer. The PMO ISSE and the ISSM are members of the Configuration Control Board.

## CM-3(6)

Changes to cryptographic mechanisms, such as algorithms, key lengths, and certificate profiles, will go through the Key Management Plan and the Configuration Control Board.

## CM-4

Each change will carry a security impact note, answering what it touches, whether it changes a boundary or an identity's access, and which controls it affects. Every note feeds a Security Impact Analysis, which the ISSM runs against what the authorization was granted on. A significant change goes to the SCA and the AO before it is made. A change to a system prompt's role or limits also triggers jailbreak and injection testing.

## CM-4(1)

Changes will be analyzed in separate environments before production. Each team has its own dev, test, and stage clusters, with stage carrying production's configuration. On-premises and Tier 0 changes are tried on the alternate site's standby or in a lab.

## CM-4(2)

After a change is made, the controls its impact analysis identified will be checked again. The check confirms each control is implemented correctly, operating as intended, and meeting its requirements. The results are recorded on the Security Impact Analysis record.

## CM-5

Only approved people and pipelines will be able to change production. Each team's pipeline identity reaches only its own repositories and dev/test spoke. Only the release identity, on a separate protected runner, can deploy to production, and it is unlocked only by Certification to Field's approval. Protected branches require a second reviewer and signed commits, with no administrator bypass. Training identities write only to their own run's output.

## CM-5(1)

GitLab will enforce those restrictions and record each one. Every review, approval, dismissal, and override streams to Splunk, where Platform Team administrators cannot change it. Each approval is checked against the approver's entitlement in Entra ID Governance at the time it was given.

## CM-6

Each class of asset will be configured to its baseline's settings. Domain controllers, certificate authorities, and sync servers follow their DISA STIGs. Containers must run as non-root with a read-only filesystem, dropped capabilities, and resource limits. Fleet equipment follows its manufacturer's hardening guide. Each deviation from a STIG is recorded with its reason and approved through change control.

## CM-6(1)

Settings will be applied and checked automatically. OpenTofu and Ansible apply them, Azure Policy and Conftest check infrastructure as code before it deploys, and Gatekeeper rejects non-compliant workloads at admission. Azure Machine Configuration, Defender for Cloud CSPM, and ACAS STIG audits then check running systems continuously, and results feed compliance dashboards in Splunk.

## CM-6(2)

When an unauthorized change is found, KESTREL will respond automatically where it can do so safely. A privileged access workstation that drifts loses Tier 0 sign-in until Configuration Manager restores it. A change to a training hyperparameter outside its approved range alerts the ML Team, and a retraining pipeline that fails its integrity check halts. Firewall policy that drifts from its repository is reverted within one business day.

## CM-7

Every asset will run only the services its function needs. Images are built minimal, managed services expose only private endpoints, and the CMP lists the ports, protocols, and services each asset type may use. Host firewalls and the shared firewall rule base deny everything else.

## CM-7(1)

What runs will be reviewed against what is allowed. ACAS scans and Defender for Cloud CSPM look for services outside the CMP's list. Network flows and firewall rules are reviewed against the approved flow map, and API Management reports any API endpoint that answers but was never registered.

## CM-7(2)

App Control for Business on Windows and fapolicyd on Red Hat Enterprise Linux will block any program that is not on the allow-list. They run in audit mode during Phase 2 and enforce by Phase 3.

## CM-7(5)

Software will run by exception only. The allow-lists name the programs each class of host may run, and everything else is denied. To add a program, a team asks through Jira Service Management and the Security Team reviews the request. The Platform Team then adds it to the signed policy through a merge request.

## CM-8

Jira Service Management Assets will be KESTREL's one inventory. Azure Resource Graph feeds it for the cloud, Defender for Endpoint for on-premises hosts, and the Cisco APIC for the data center network. Passive sensors and Fleet Operations' records feed the fleet. Each application and each certified model version is registered too, and so are third-party products once their supplier assessment passes.

## CM-8(1)

The inventory will change when components do. Provisioning and decommissioning update it as part of the same change, and a deployment to production fails unless its application is registered. Each certified model version is registered when it is certified.

## CM-8(2)

The inventory will be maintained automatically from the cloud's resource inventory, the endpoint agents, and the SDN controller. A deployment inventory in Splunk compares what is running with what was certified, and the model registry reports its own state each month.

## CM-8(3)

Unauthorized components will be detected automatically. A subscription created outside the landing zone alerts, and so does a device the Cisco APIC does not recognize. Passive sensors flag unknown devices on the ground segment. Anything running in production that was never certified is flagged, and the model registry admits only models from approved sources.

## CM-8(4)

Every asset will carry tags naming its owning team, segment, environment, data classification, mission criticality, and end-of-support date. The pipeline rejects an untagged cloud resource, and Fleet Operations tags fleet equipment when it is received.

## CM-9

The Platform Team will write the Configuration Management Plan, with Fleet Operations writing the OT and legacy sections and IT Operations the maintenance sections. The Security Team reviews it, and the Configuration Control Board approves it. It is revised each year and after any significant change, such as a new spoke or interconnection.

## CM-10

KESTREL will track the license terms of every licensed product, including the foundation model's terms, in Jira Service Management Assets. Peer-to-peer file sharing software is prohibited.

## CM-11

Users will not be able to install software. Allow-listing on every host blocks anything not on the approved list, and new software reaches a host only through the request and merge process described for CM-7(5).

## CM-12

KESTREL will know where its information lives. The Data Team labels every record at ingest, and OpenMetadata catalogs every data store and classifies databases and structured files by their content. The catalog is checked against the CCSD's information types.

## CM-12(1)

OpenMetadata will scan the data stores automatically over a read-only identity, so the record of where information lives stays current without manual surveys.
