# CP: Contingency Planning

## CP-1

The program manager will issue the contingency planning policy as part of KESTREL's system security policy. The Contingency Plan will hold the procedures. The Configuration Control Board will approve both, and each will be reviewed at least once a year.

## CP-2

The Platform Team will write the Contingency Plan, with Fleet Operations writing the fleet and ground segment sections. It names the essential functions and their recovery objectives, and the roster with a backup for every role. It also sets the restoration order, the backup policy, the manual fallbacks, and the alternate site arrangements. The ISSM reviews it, and the Configuration Control Board approves it. A printed copy is kept at each site, so it can be read when the identity provider is down.

## CP-2(1)

The plan will be coordinated with the related plans and parties. These are the Incident Response Plan, the parent organization's continuity of operations and occupant emergency plans, the alternate site's operator, and the CSSP. The record of that coordination is kept with the plan.

## CP-2(2)

Capacity will be planned for a contingency. The alternate site holds warm standbys sized for Tier 1. Recovery spokes in US Gov Arizona are sized to take Tier 2 if the data center is lost.

## CP-2(3)

Essential functions will be resumed within each tier's recovery time objective: 4 hours for Tier 1, 24 hours for Tier 2, and 7 days for Tier 3. The program manager approves those objectives from the business impact analysis.

## CP-2(5)

Essential functions will continue through a disruption. The fleet keeps flying from the ground control stations with local smart card sign-in, and aircraft keep their recordings until the data lake returns. Analysts work from the last delivered products, and mission planning reverts to manual if the planning agent is unavailable.

## CP-2(8)

The plan will name the critical assets behind each essential function, taken from the business impact analysis. Examples are the identity provider, the PKI and HSMs, the signing path, and the ground segment's configuration.

## CP-3

Everyone with a contingency role will be trained when they take the role, after a system change, and each year. That includes the operators, the restore operators, and the Tier 0 administrators.

## CP-3(1)

Training will include simulated events. Fleet drills on degraded operations start when the fleet integrates in Phase 3.

## CP-4

The plan will be tested. Each quarter the Platform Team restores a sample from every tier and measures the result against its objectives, and production traffic fails between the data center's two circuits. A failover exercise runs each year, and a tier that misses its objective is raised to the AO.

## CP-4(1)

The yearly failover exercise will be coordinated with the owners of related plans, including the Incident Response Plan's owner and the CSSP.

## CP-4(2)

The yearly failover exercise will run at the alternate site, proving its standbys, its circuit, and its readiness to take the workload.

## CP-6

The alternate site will store a copy of every backup, and immutable Blob storage in US Gov Arizona will store a second copy. No single site or region holds every copy.

## CP-6(1)

The alternate site will be a parent organization facility in a different region from the data center, far enough away that no regional event reaches both.

## CP-6(2)

Backups will be replicated to the alternate storage sites often enough to meet each tier's recovery point objective.

## CP-6(3)

Events that could leave the alternate site unreachable will be planned for: a regional DISN outage, the parent organization's own emergency, or a travel restriction. In each case, Tier 2 restores into recovery spokes in US Gov Arizona, managed from the cloud.

## CP-7

The alternate site will serve as the alternate processing site, holding warm standbys for Tier 1, including domain controllers, an issuing certificate authority, and CyberArk. Tier 1 services run there within their 4-hour recovery time, and Tier 2 services restore into the recovery spokes in US Gov Arizona.

## CP-7(1)

The alternate processing site will be far enough from the data center that no regional event reaches both.

## CP-7(2)

The same accessibility plans that cover the alternate storage site will cover processing, with US Gov Arizona as the fallback when the alternate site cannot be reached.

## CP-7(3)

The facility agreement will give KESTREL priority access to the alternate site in an area-wide emergency, and it names who may activate the site.

## CP-7(4)

The alternate site will be kept ready for use. Its standbys stay warm, a second HSM holds the escrowed keys, and a copy of every backup and two privileged access workstations are staged there.

## CP-8

Each of the data center's two circuits will come from a different carrier, and the alternate site will have a third. All three ride DISN, whose transport KESTREL inherits. Production traffic fails between the data center's circuits each quarter.

## CP-8(1)

Every carrier agreement will carry priority restoration of service.

## CP-8(2)

No single point of failure will be able to cut the data center off. Each circuit runs on its own path, through its own building entry, to a different meet-me point.

## CP-8(3)

The data center's two circuits will come from different carriers, so the loss of one carrier does not take both.

## CP-8(4)

Every carrier agreement will require the carrier to keep a contingency plan of its own.

## CP-9

Backups will follow three tiers set from the business impact analysis. Tier 1 is replicated continuously with a daily full backup, Tier 2 is backed up daily, and Tier 3 weekly. Azure Backup protects cloud services, and Veeam protects the data center. Services that cannot be backed up directly are exported on schedule, and fleet equipment is captured with the manufacturers' tools in maintenance windows. Every resource is bound to its tier's policy when it is created.

## CP-9(1)

Backup jobs will be checked for reliability and integrity. Job results reach Splunk, a failure alerts the backup operators, and a sample is test-restored each week.

## CP-9(2)

A sample from every tier will be restored each quarter, rotating so every Tier 1 system is restored at least once a year. The registry restore re-verifies every signature.

## CP-9(3)

Backups of critical information, such as the identity provider and the PKI, will be stored separately from the systems they protect. They sit in locked storage at the alternate site and in the second region. HSM key backups go only to the alternate site's HSM.

## CP-9(5)

Backup copies will be transferred to the alternate site and to the second IL5 region often enough to meet each tier's recovery point.

## CP-9(8)

Each Veeam backup set will be encrypted under its own key rooted in the nShield HSMs, and Azure Backup vaults use customer-managed keys in Key Vault Premium.

## CP-10

Systems will be restored to a known state: their last backup from before the disruption, or before the compromise if an incident caused it. A restored system returns to service only after its image and configuration match their signed baselines, a compliance scan passes, and its logs reach Splunk. The restoration order is agreed in advance.

## CP-10(2)

Point-in-time restore will recover database transactions to within each tier's recovery point.

## CP-10(4)

Services will be restorable from a known-good image within set times. Every production spoke keeps the previous certified release ready to roll back to, and each model endpoint can return to its previous certified version in minutes. Rollback is rehearsed before each model is certified.
