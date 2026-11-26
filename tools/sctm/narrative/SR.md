# SR: Supply Chain Risk Management

## SR-1

The program manager will issue the supply chain risk management policy as part of KESTREL's system security policy. The Supply Chain Risk Management Plan will hold the procedures. The Configuration Control Board will approve both, and each will be reviewed at least once a year.

## SR-2

The supply chain lead will write the Supply Chain Risk Management Plan with the SCRM team. It covers vendor assessment and tiering, contract security requirements, the supply chain risk assessment and dependency map, sourcing and inspection, and component disposal. The ISSM and the PMO ISSE review it, the Configuration Control Board approves it, and it is revised each year and whenever a Tier 1 supplier changes.

## SR-2(1)

A standing SCRM team, chaired by the supply chain lead, will meet each month and whenever a Tier 1 supplier changes. Its members include the contracting officer, program legal counsel, the PMO ISSE, the ISSM, and the leads who receive hardware for the data center and the fleet.

## SR-3

Components will enter KESTREL only through controlled paths. Builds resolve packages only through Artifactory, which draws each ecosystem from its approved upstream. Every dependency change is reviewed for vulnerabilities, license terms, and package health before it can merge. Every software supplier delivers an SBOM with each release, which is loaded into Dependency-Track and monitored for new flaws.

## SR-5

KESTREL will buy hardware only from manufacturers and authorized resellers, and its contracts will carry clause sets matched to each supplier's risk. Sole-source or obsolete parts bought elsewhere need the SCRM team's approval, a stricter inspection, and a risk acceptance.

## SR-6

Every commercial supplier will answer KESTREL's security questionnaire before contract award, including questions on ownership and foreign influence. Suppliers are tiered by what they can reach, and Tier 1 suppliers are reassessed every year. Model publishers, dataset sources, and the foundation model provider are assessed against the AISP's criteria as well.

## SR-8

Contracts will require suppliers to notify KESTREL of a compromise or a failed audit, as a clause in the clause library's software and Tier 1 clause sets.

## SR-9

Hardware will be inspected for tampering when it arrives and again when it returns from vendor service. Inspectors check packaging and seals, markings, serial and lot numbers, and physical characteristics against a known-good unit.

## SR-9(1)

Tamper resistance and detection will apply at more than one stage of the lifecycle. Suppliers' own controls are assessed before award, hardware is inspected at receipt and after service, and stations and avionics are rescanned each year.

## SR-10

The Platform Team will inspect data center hardware at receipt from Phase 1, and Fleet Operations will inspect fleet equipment from Phase 3. Each item is also inspected again when it returns from vendor service.

## SR-11

Firmware will come only from the manufacturer or its authorized channel, and its signature will be verified before installation. Unsigned firmware is checked against the manufacturer's published hash. Each verified version is recorded against its device in Jira Service Management Assets. A suspect counterfeit part is quarantined and reported to its source, to GIDEP, to the contracting officer, and to the ISSM.

## SR-11(1)

The staff who receive and inspect hardware, in the Platform Team and Fleet Operations, will be trained to recognize counterfeit indicators.

## SR-11(2)

Components sent out for service or repair will be inspected again when they return, before they are reinstalled, and their firmware is verified as on first receipt.

## SR-11(3)

Ground control stations and aircraft avionics will be rescanned for counterfeit parts each year, at a maintenance window, focusing on parts that entered through vendor service channels. CCSD tailoring action 4 added this control.

## SR-12

Retired components will be disposed of so that nobody can recover them. Drives are purged on site with Blancco to NIST SP 800-88, verified, and shredded. HSMs and datalink crypto modules are zeroized and then destroyed. A retired model's weights and derived embeddings are deleted, and its copies are removed from every aircraft. Each disposal is recorded with its method and a certificate of destruction.
