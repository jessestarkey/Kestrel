# SA: System and Services Acquisition

## SA-1

The program manager will issue the acquisition policy as part of KESTREL's system security policy. The Supply Chain Risk Management Plan will hold the acquisition procedures, including the contract security requirements. The Configuration Control Board will approve both, and each will be reviewed at least once a year.

## SA-2

Security will be planned and funded as part of each capability. The PMO ISSE turns the CCSD's controls into requirements that enter each team's backlog. The program managers hold a dedicated application security budget line, which funds closing the gaps the PMO ISSE finds.

## SA-3

KESTREL will manage development through one lifecycle with security built into each stage. Every application, AI use case, and COTS product enters through intake, is threat-modeled before it is built, and is tested and certified before it is fielded. Roles for each stage are set in the ASP and the AISP.

## SA-4

Each acquisition will state the security functions the product must provide, the evidence the supplier must deliver, and the supplier's configuration and supply chain duties. The PMO ISSE writes these requirements from the SADD, and the supply chain lead draws the contract terms from the clause library the SCRM plan sets out. Model selection records the security criteria each model and publisher was assessed against.

## SA-4(1)

Contracts will require suppliers to describe the functional properties of the security controls their products provide, as a clause in the Supply Chain Risk Management Plan's clause library.

## SA-4(2)

Contracts will require suppliers to provide design and implementation information for the security controls in their products, as a clause in the clause library.

## SA-4(5)

Contracts will require suppliers to deliver their products in a secure configuration, with that configuration documented, as a clause in the clause library.

## SA-4(9)

Contracts will require suppliers to identify the functions, ports, protocols, and services their products use. That information feeds KESTREL's PPSM registration and the CMP's list of permitted services.

## SA-4(10)

Products that handle PIV credentials, such as CAC readers and the identity platform, will be bought only from the products approved for FIPS 201 use.

## SA-5

Documentation for each certified model will be generated from its validation results. The pipeline produces a model card stating the model's intended use, tested limits, known failure modes, and retraining envelope. The PMO ISSE checks it against its evidence before certification. Administrator and user documentation for other components comes from their suppliers under their contracts.

## SA-8

Security engineering principles will be applied as requirements are derived. The PMO ISSE turns the SADD's design principles, such as least privilege, deny by default, and separation of the payload vendor data, into testable requirements for each application.

## SA-8(33)

KESTREL will collect and keep only the personal information its mission needs. Incidental imagery of people is the only personal information in the collection, and training sets keep it only where a detection task requires it. The DMP sets the minimization rules, and the AISP sets the privacy requirements for models.

## SA-9

External services will be held to security requirements through their contracts and authorizations. Azure Government is relied on through its IL5 authorization, which the inherited control check confirms each year. The foundation model runs as a deployment inside KESTREL's own tenant, reached only by private endpoint. Applications call no external service outside the boundary except Purview Information Protection in the Microsoft 365 DoD tenant.

## SA-9(2)

Each external service will identify the functions, ports, protocols, and services it uses, as a clause in the clause library. KESTREL registers each one in the DoD PPSM registry.

## SA-9(5)

Processing and storage will stay in United States regions inside the cloud provider's IL5 authorization. CCSD tailoring action 5 records that location as a parameter, covering the foundation model service and KESTREL's Microsoft 365 DoD tenant.

## SA-10

Changes to the pipeline itself will be controlled. Every team's pipeline extends the Platform Team's templates, and an unapproved change to a pipeline definition stops the run and alerts the Platform Team and the Security Team. From Phase 2, the templates are signed and verified before each job. Training code and its configuration are versioned and reviewed the same way.

## SA-11

Every application and model will be tested before it is fielded. GitLab DAST scans each candidate application build in stage with a test account for each role. Models are tested for jailbreaks, prompt injection, adversarial evasion, data poisoning, and out-of-distribution inputs, against thresholds the AISP sets for each assurance level.

## SA-15

KESTREL will set its development processes, standards, and tools in the ASP and the AISP. These cover the threat modeling method, the secure coding standard, the policy-as-code gates, the approved component catalogs, and the model optimization techniques. Both plans are reviewed as a whole each year.

## SA-15(3)

A criticality analysis will identify the components and suppliers KESTREL's essential functions depend on. The supply chain lead maps those dependencies each year, flagging single sources and concentrations, and the contract terms for each supplier follow from that analysis.

## SA-16

Contracts will require suppliers of critical components to provide training on their security functions, as a clause in the clause library.

## SA-17

Each application's security architecture will follow the SADD's design, and its threat model will document how the application meets it. The PMO ISSE checks both at the design gate before building starts.

## SA-21

Contracts will require suppliers to screen the developers who work on KESTREL's components, as a clause in the clause library.

## SA-22

Each asset's end of support will be forecast at least 12 months ahead, so it can be replaced in time. An asset kept past its end of support needs an exception, with its compensating controls and a replacement date. The payload processing workstation is the known case, replaced by 2027-09-30, and it connects only if the AO re-dates CCSD tailoring action 3.
