# RA: Risk Assessment

## RA-1

The program manager will issue the risk assessment policy as part of KESTREL's system security policy. The Risk Management Program Charter and the Vulnerability and Patch Management Plan will hold the procedures. The Configuration Control Board will approve them, and each will be reviewed at least once a year.

## RA-2

KESTREL will be categorized High for confidentiality and integrity, and Moderate for availability, by CNSSI 1253's high-water mark over the CCSD's 18 information types. The AO concurred in the categorization on 2026-08-28, and it is reassessed with every CCSD revision.

## RA-3

Risk will be assessed with one method, based on NIST SP 800-30, and recorded in one register. Risks come from threat models, release and model certification scores, the AI threat assessment, and the SCA's assessment. The SCA's Risk Assessment Report goes to the AO before the ATO decision, and the register is reviewed each month.

## RA-3(1)

Supply chain risk will be assessed each year for every Tier 1 supplier and the components KESTREL depends on most, including the foundation model's publisher. Single points of supply and countries of origin are recorded, and model choices record the supplier risks accepted.

## RA-5

Every host will be scanned for vulnerabilities by ACAS in every location, on a continuously updated feed. Containers are scanned before they are pushed and rescanned in the registry. Dependencies are reviewed at every merge request and matched daily against new disclosures after release. Applications get DAST in stage, and models are re-tested against new attacks each quarter. Findings are fixed on the VPMP's deadlines.

## RA-5(2)

ACAS's vulnerability feed will update continuously, and Dependency-Track and Xray pull new vulnerability data as it is published.

## RA-5(4)

Tenable Attack Surface Management will watch KESTREL's public names and services from outside, and GitGuardian will watch public sources for KESTREL's code and credentials. The Security Team reviews the findings each month.

## RA-5(5)

Vulnerability scans will run authenticated. Scan credentials for Tier 0 are vaulted in CyberArk and used only from a Tier 0 scanner.

## RA-5(11)

KESTREL's internet-reachable endpoints will be enrolled in the DoD Vulnerability Disclosure Program, which DC3 runs. The Security Team triages each relayed report and tracks it to closure like a penetration test finding.

## RA-7

Each risk will get a recorded response: fix it, compensate for it, or accept it under the risk acceptance process. Release and model scores route anything outside their thresholds to the PMO ISSE. Anything above Very Low in the flight safety and key material rows goes to the AO. Assets that cannot be patched get a fixed set of compensating controls. Accepted design risks are tracked in their own register.

## RA-8

The Privacy Impact Assessment, on DD Form 2930, will be approved in Phase 1, before user and service desk records and the prior collection imagery arrive. A new collection, sensor, AI use case, or partner release triggers a reassessment.

## RA-9

A criticality analysis will identify the components the mission depends on most. Each asset's criticality comes from the business impact analysis and its inventory tags. The command link, the stations, the identity provider, the HSMs and PKI, and the signing and registry path rank highest. Each model's robustness requirements reflect how much the mission relies on its output.
