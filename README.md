# KESTREL: The SABER Applied

KESTREL is a **notional system** built to show the SABER (Security Architecture and Baseline Engineering Reference) applied in practice. It follows a PMO ISSE through the whole path the SABER is designed to support: categorizing a system, tailoring the framework to it, producing a Security Architecture and Design Document (SADD), and carrying that design into an issue-tracker Implementation Plan.

> **KESTREL is fictional.** It is not a real program, it holds no real data, and any resemblance to an actual system is coincidental. Its architecture is realistic so that every SABER decision made against it is a decision a real program would face, but nothing here describes an operational capability.

## Why a notional system

The SABER is a framework: it defines outcomes, activities, control mappings, and metadata, but it deliberately stops short of any one program's design. A framework that only exists in the abstract is hard to evaluate. KESTREL gives it something concrete to act on, chosen so that most of the SABER applies and the parts that get tailored out are excluded for a stated reason, not because the example was too small to need them.

## The system

KESTREL is a hybrid ISR (intelligence, surveillance, and reconnaissance) analytics platform. A fleet of unmanned aircraft collects sensor data and runs onboard detection models. An IL5 cloud and on-premises backend trains and improves those models, manages the mission data, and serves applications to operators, analysts, and coalition partners.

| Segment | What it hosts |
| :--- | :--- |
| **IL5 development and test** | CI/CD pipelines, the model training cluster, experimentation environments. Not reachable from outside the program. |
| **IL5 production** | The externally accessible applications: the analyst portal, the partner API, the LLM analyst assistant with retrieval over mission reports, and the feedback endpoints that supply retraining data. |
| **On-premises mission data center** | The authoritative mission data lake, PKI and HSMs, the identity provider, and the security operations center. |
| **UAS fleet** | Aircraft, ground control stations, and launch and recovery equipment (OT/ICS), each aircraft running an onboard detection model and contributing federated model updates. |

```mermaid
flowchart LR
    subgraph USERS["Users"]
        direction TB
        OPS["UAS operators"]
        ANL["Analysts"]
        PART["Coalition partners"]
    end

    subgraph IL5["IL5 Gov Cloud"]
        direction TB
        DEV["Dev/test<br/>CI/CD, training, experimentation"]
        PROD["Production<br/>analyst portal, partner API,<br/>LLM assistant, feedback endpoints"]
        DEV -->|"CtF, continuous"| PROD
    end

    subgraph ONPREM["On-Premises Mission Data Center"]
        direction TB
        LAKE["Mission data lake"]
        PKI["PKI, HSMs, identity provider"]
        SOC["Security operations center"]
    end

    subgraph FLEET["UAS Fleet (OT/ICS)"]
        direction TB
        GCS["Ground control stations"]
        UAS["Aircraft with<br/>onboard detection model"]
        GCS --- UAS
    end

    CDS{{"Cross-domain solution"}}
    CLASS["Classified enclave<br/>disconnected tools and models"]

    ANL --> PROD
    PART --> PROD
    OPS --> GCS
    PROD <--> LAKE
    UAS -->|"sensor data, federated updates"| LAKE
    LAKE --> DEV
    DEV -->|"certified models, baseline release"| GCS
    PROD -->|"CtF, periodic baseline"| CDS --> CLASS
    CLASS -->|"released products, high to low"| CDS --> PROD
```

### Users

- **UAS operators** are privileged, mission-critical users working from ground control stations and the operator side of the portal.
- **Analysts** use the IL5 portal and the LLM assistant, and submit corrections that feed retraining.
- **Coalition partners** reach the partner API with federated or External Certificate Authority PKI credentials under program sponsorship.

There is no anonymous or general-public access. IL5 holds controlled unclassified and unclassified national security information, so "external" here means authenticated, sponsored users from outside the program team, entering through the DoD cloud access boundary rather than directly from the internet.

## How KESTREL exercises the SABER

| Pillar | Focus Area | Why KESTREL needs it |
| :--- | :--- | :--- |
| Protect | Identity | DoD users, coalition partners with external PKI, workload and pipeline identities, an agentic mission-planning assistant, and privileged operators with OT maintenance-window access. |
| Protect | Device and Infrastructure | Cloud workloads, on-premises servers, HSMs, ground control stations, and the aircraft themselves. |
| Protect | Network and Environment | Segmentation between dev/test and production, an externally exposed production boundary, the hybrid circuit to the data center, two-way cross domain transfer, and OT network isolation. |
| Protect | Application | The analyst portal and partner API, shipped continuously through Certification to Field to IL5 production and as periodic baselines to the IL6 enclave. |
| Protect | Artificial Intelligence | The full model lifecycle: training, Continuous Training from analyst feedback and federated fleet updates, cloud and edge serving, RAG, a vendor-hosted foundation model, an agentic assistant, and safety-critical AI on aircraft. |
| Protect | Data | Mission data classification, provenance, and lineage, key management, and incidental PII captured in imagery. |
| Operate | Detection, Response, Recovery | An externally exposed production environment and a fielded fleet give the SOC real telemetry, real incidents, and real recovery requirements across four deployment types. |
| Manage | Governance, Risk, Compliance | One authorization package at IL5, risk acceptance at the certification gate, and continuous monitoring spanning cloud, on-premises, hybrid, and OT environments. |

Two parts of the SABER are especially well exercised:

- **Both release cadences.** IL5 production receives continuous per-build releases, while the aircraft and the IL6 enclave receive periodic baselines. Both pass through the same Certification to Field gate, which is the case that gate was designed to cover.
- **Continuous Training as a real loop.** Analyst corrections and federated fleet updates flow back into retraining, so the feedback authentication, skew detection, and drift monitoring outcomes all have real inputs to act on.

### Tailored out

Enterprise email and collaboration remain outside the SABER's scope and are not modeled here. KESTREL also stops at IL5. It exchanges data with an IL6 enclave through a two-way cross domain solution, but that enclave is a separate system and its design is not modeled. Any other outcome KESTREL does not need is tailored out in the SADD with its reason recorded, rather than silently omitted.

## Planned contents

The repository will grow along the same path a PMO ISSE follows:

1. **System description** ([01-system-description.md](01-system-description.md)): authorization boundary, components, data flows, users, and interconnections.
2. **Security categorization:** FIPS 199 and CNSSI 1253 categorization and the resulting control baseline.
3. **Tailoring and SADD:** which SABER outcomes apply, which are tailored out and why, and the populated metadata for KESTREL's environments.
4. **Implementation Plan:** epics, stories, and tasks derived from the tailored outcomes, ready to load into an issue tracker.
5. **Plan-type deliverables:** KESTREL-specific instances of the SABER's governing plans (AMP, CMP, KMP, IRP, CP, AISP, and others) where a worked example is useful.

The system description is written. The rest follow in order.

## Relationship to the SABER

KESTREL is built against **SABER v1.3**, maintained in the separate [saber-framework](https://github.com/jessestarkey/saber-framework) repository. When this repository cites a SABER outcome or activity, it uses the SABER's own ID and name (for example, `AI-6.5: Deployment Risk Threshold Evaluation`). If the SABER changes, this repository records which version it was last aligned to rather than silently drifting.

As in the SABER itself, mapping KESTREL's design to NIST SP 800-53 controls reflects design intent, not compliance evidence. Implementation narratives, assessment results, and control status would live in a program's separately maintained requirements traceability artifact, which a notional system does not have.
