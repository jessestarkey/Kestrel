> **Notional system.** KESTREL is fictional. This page stands in for a governing plan in KESTREL's self-hosted Confluence. Its names, thresholds, and decisions are invented to show a completed Key Management Plan.

# KESTREL Key Management Plan (KMP)

This plan governs the algorithms, keys, certificates, and vaults that protect KESTREL's data. The Data Management Plan (DMP) says what each class of data needs, and this plan says how the cryptography delivers it. It carries out the design decisions in the [Data section of the SADD](https://github.com/jessestarkey/Kestrel/blob/main/docs/03-sadd/07-data.md) and names the products that enforce them. The [Security Implementation Plan](https://github.com/jessestarkey/Kestrel/blob/main/docs/04-sip/07-data.md) is the record of each product selection, and a substitution there revises this plan.

**NIST Control Mapping:** SC-1 (partial), held through DA-3.13.

> **CNSA 2.0 transition.** This plan is approved in Phase 1. The cryptographic inventory finishes in Phase 2, and the PMO ISSE then adds the full transition sequence to Section 1. Until then, Section 1 records the order and the deadlines already known.

---

## Document Control

| Field | Value |
|---|---|
| Program / System Name | KESTREL |
| KMP Version | 0.1 |
| Date | 2026-11-25 |
| Prepared By | The Platform Team's Tier 0 administrators, with Fleet Operations for the datalink key procedures, reviewed by the Security Team |
| Approved By | Configuration Control Board, chaired by the chief engineer |
| Source SADD Version | 0.5 |
| Source SIP Version | 0.3 |
| Classification / Handling | CUI |

### Version History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 0.1 | 2026-11-25 | KESTREL Tier 0 administrators | Initial draft for Configuration Control Board review |

---

## Purpose and Scope

This KMP covers every key, certificate, and secret KESTREL generates, holds, or trusts. That includes the cloud's Key Vaults, the nShield HSMs, the program PKI, and the datalink crypto modules in the aircraft and stations. It also covers the trust KESTREL places in DoD PKI and External Certificate Authorities. CCSD row 13, the command link and root signing key material, is KESTREL's only High confidentiality information type. Most of this plan's strictest rules exist to protect it.

KESTREL protects no classified information. NSA-approved Type 1 cryptography sits on the IL6 side, owned by the enclave and the cross domain service provider. This plan therefore names no Type 1 or CSfC use.

---

## 1. TLS and Algorithm Baselines

*Traces to DA-2.2.1, DA-3.1.2, and DA-3.2.2.*

**Modules.** KESTREL uses only FIPS 140-3 validated modules. The nShield HSMs and the datalink crypto modules must be validated at Level 3.

**Algorithms.** KESTREL is a national security system, so it uses the CNSA algorithms CNSSP 15 requires.

| Use | Approved | Notes |
|---|---|---|
| Data at rest | AES-256 | GCM or XTS mode, as the storage service supports |
| Data in transit | TLS, with the suites below | Inside IPsec tunnels in FIPS-CC mode on the circuits |
| Key establishment | ECDH on P-384, or RSA-3072 or larger | ML-KEM-1024 as products support it |
| Digital signatures | ECDSA on P-384, or RSA-3072 or larger | ML-DSA-87, LMS, or XMSS as products support them |
| Hashing | SHA-384 or SHA-512 | |
| Customer-managed and imported keys | RSA-3072 or larger, or P-384 | Generated in the nShield HSMs |

**TLS.** Every service KESTREL terminates accepts only TLS 1.2 or later, and prefers TLS 1.3. That covers Application Gateway, the Istio mesh, and the Palo Alto firewalls.

| Version | Permitted suites |
|---|---|
| TLS 1.3 | TLS_AES_256_GCM_SHA384 |
| TLS 1.2 | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 and TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 |

Key exchange uses P-384, and certificates sign with ECDSA on P-384 or RSA-3072 or larger. Service-to-service connections use mutual TLS with program PKI certificates. User-facing edge services present DoD PKI server certificates. Corelight flags plaintext attempts on premises, and the firewalls block and log them.

**Provider endpoints.** A provider-managed endpoint presents the provider's certificates under its own minimum TLS setting. Azure Policy enforces TLS 1.2 as that minimum. Where a provider's suites fall outside the table, the cryptographic inventory records them, and the ISSM tracks them as a known exception.

**Exceptions.** A service that cannot meet this baseline needs an exception under the exception process (`GV-2.2`). The exception names the service, the gap, the compensating measure, and an end date. Scans of code, configuration, and traffic with Keyfactor and ACAS flag any use outside the baseline.

**CNSA 2.0 transition.** The cryptographic inventory records every use of quantum-vulnerable public-key cryptography. The transition follows this order:

1. Code signing and firmware signing, which must use CNSA 2.0 exclusively by 2030. That covers the Key Vault release signing keys and the fleet signing key.
2. The program PKI's roots and issuing authorities.
3. The datalinks, gated by the datalink crypto modules' manufacturer.
4. Network equipment, such as the Palo Alto firewalls and the IPsec tunnels, as vendors ship support.
5. TLS on KESTREL's own services, then provider endpoints as the provider supports them.

Every contract signed from 2027-01-01 requires CNSA 2.0 support, or an NSA-approved exception or AO waiver. Every new design must let its algorithms change without redesign. The PMO ISSE adds the dated sequence and each step's vendor dependency in Phase 2.

---

## 2. Key Ownership and Vault Infrastructure

*Traces to DA-2.5.1, DA-3.1.4, and DA-3.3.2.*

**Key ownership.** KESTREL owns and controls the keys for every store holding mission data, models, or backups.

| Data | Key ownership |
|---|---|
| Mission data, models, and lineage (CCSD rows 1 to 8) | Customer-managed, imported from the nShield HSMs |
| Code, releases, and configuration (rows 9 to 11) | Customer-managed, imported from the nShield HSMs |
| Credentials and security configuration (row 12) | Customer-managed, in each spoke's Key Vault |
| Command link and root signing key material (row 13) | Held only in the nShield HSMs and the datalink crypto modules, never in the cloud |
| Telemetry, identity, maintenance, and service desk records (rows 14 to 16 and 18) | Customer-managed, imported from the nShield HSMs |
| Backup and archive copies (row 17) | Customer-managed, with each backup set's key escrowed under Section 3 |
| Synthetic or sanitized dev/test data | Platform-managed keys allowed, but never in ML Dev/Test |

A customer-managed key must be available in the second IL5 region, so recovery never waits on it. Key administration is separate from key use, as Section 5 sets out.

**Vault tiers.**

| Tier | Product | Holds | Why this tier |
|---|---|---|---|
| Cloud keys | Azure Key Vault Premium, one per spoke | Customer-managed keys, the pipeline's release and dev/test signing keys, and each spoke's secrets | HSM-backed keys validated at FIPS 140-3 Level 3, inside each spoke's own boundary |
| Root keys | nShield HSMs in the data center | The root certificate authority, the issuing authorities, the fleet signing key, and the datalink key material | FIPS 140-3 Level 3, under KESTREL's own security world |
| Standby | nShield HSM at the alternate site | Backups of the root keys and escrowed keys | Survives the loss of the data center |

Key Vault Premium's throughput covers KESTREL's peak, which is training runs unwrapping data keys. The Platform Team checks throttling in Splunk each quarter. The HSMs run as a pair in the data center, so one can fail without stopping signing or issuance.

---

## 3. Key Lifecycle Management

*Traces to DA-3.5.1, DA-3.5.2, and DA-3.5.4.*

**Rotation.** Key Vault rotates the keys it generates on this cadence. Imported keys cannot rotate in place, so near expiry a Key Vault event triggers an nShield job. The job generates, wraps, and imports the replacement.

| Key | Rotates every | Notes |
|---|---|---|
| Customer-managed keys for rows 1 to 12 and 14 to 18 | 1 year | Re-imported from the HSMs |
| Pipeline release signing key | 1 year | Old signatures stay valid against the retired key's certificate |
| Fleet signing key | 2 years | Aircraft take the new key's certificate in a maintenance window first |
| Datalink traffic keys | 30 days, on Fleet Operations' schedule | Superseded fleet-wide at once when an aircraft is lost |
| Datalink key-encryption keys | 1 year | Loaded by key loader in a maintenance window |
| Backup set keys | With each backup set | Escrowed, never rotated in place |
| Root certificate authority | 20-year certificate, rekeyed at 10 years | Only in the nShield HSMs |
| Issuing authorities | 5-year certificate, rekeyed at 2.5 years | Only in the nShield HSMs |

**Key hierarchy.** The nShield security world protects every key the HSMs hold. Root keys sign the issuing authorities. Key-encryption keys, generated in the HSMs, are imported into each spoke's Key Vault. Those keys wrap the data-encryption keys each storage service uses. A data-encryption key never wraps another key, and no key-encryption key ever leaves an HSM-backed tier in the clear.

**Bring your own key.** The nShield HSMs are KESTREL's only source of externally generated key material. A key is generated there, wrapped under Key Vault's key exchange key, and imported. KESTREL accepts no key generated by a vendor or by software.

**Row 13 keys.** Row 13 keys never exist in the clear outside an HSM, a datalink crypto module, or a key loader in transit. Loaders are accounted for in Assets and zeroized after each fill. Backups reach the alternate site's HSM over F19 only as security-world blobs, unusable outside an HSM. HSM administration needs two people, and every HSM operation is logged to Splunk.

**Escrow and recovery.** Keys whose loss would destroy data are escrowed in the alternate site's HSM under split knowledge. Backup set keys are the main case. Recovering one needs a quorum of two of the four administrator cards. The ISSM and a Tier 0 administrator must both approve it first, on a Jira Service Management record. A recovery is allowed only when the operational key is lost, destroyed, or unusable, and the Security Team is told at once. Destroying a backup set's key sanitizes the set, as the IRP's spill procedure uses.

---

## 4. Certificate Management

*Traces to DA-3.7.1 and DA-3.9.3.*

**Issuers.** Active Directory Certificate Services issues KESTREL's device, workload, and code-signing certificates under the HSM-held root. Keyfactor Command distributes them and keeps the inventory. The PMO ISSE confirms the root's approval under DoDI 8520.02. User, partner, and edge server certificates come from DoD PKI and External Certificate Authorities, whose trust anchors the identity provider holds.

**Profiles.**

| Purpose | Validity | Key usage | Subject alternative names | Renewal |
|---|---|---|---|---|
| Workload and service TLS | 90 days | Digital signature, server and client authentication | DNS names in KESTREL's own zones only | cert-manager, 30 days ahead |
| Mesh workload identity | 24 hours | Digital signature, client and server authentication | The workload's SPIFFE ID only | istiod, automatic |
| Device, for 802.1X | 1 year | Digital signature, client authentication | The device's Assets record name | Automatic enrollment |
| Aircraft and station | 2 years | Digital signature, client authentication | The tail number or station ID | In a maintenance window |
| Code signing | 1 year | Digital signature, code signing | None | Manual, with a second Tier 0 approver |
| Break-glass | 1 year, under the dedicated break-glass CA | Digital signature, smart card logon | The break-glass account only | Manual, under the AMP |

Every profile uses ECDSA on P-384 or RSA-3072 or larger. No profile allows wildcard names. Keyfactor and Splunk alert on approaching expiry or on any issuance nobody requested.

**Revocation.** A certificate is revoked on compromise, decommissioning, or a change of role. The owning team, the Security Team, or the ISSM may request a revocation. A Tier 0 administrator authorizes each one. The updated revocation list and OCSP responses publish within one hour. The dedicated break-glass CA's revocation list has a seven-day validity, as the AMP sets out.

An aircraft declared lost has its device certificates revoked at once. Every datalink key it shared is superseded fleet-wide from the nShield HSMs by key loader. Stations refresh their cached revocation list daily and before each flight.

---

## 5. Secrets Vault Access

*Traces to DA-3.10.1.*

**Roles.** Key administrators, key users, and key auditors are separate roles, and no identity holds two of them.

| Role | Who holds it | May | May not |
|---|---|---|---|
| Key administrator | Tier 0 administrators, activated just in time through Entra PIM | Create, rotate, and set policy on keys and secrets | Read a secret's value, or use a key to encrypt, decrypt, or sign |
| Key user | Workload identities, and Fleet Operations' key loading staff | Read the specific secrets, or use the specific keys, their function needs | Change, export, or delete anything |
| Key auditor | The Security Team | Read vault configuration and every operation log | Read secrets, or use or change keys |

**Workloads.** Each spoke's Key Vault grants each workload identity only the secrets and keys it needs, named one by one. No workload holds access to a whole vault.

**People.** No person holds standing vault access. A Tier 0 administrator activates access just in time inside an admin VDI session, under Just in Time Access (`ID-4.3`).

**Guarding the guards.** Keys are created non-exportable. Every vault has soft delete and purge protection on, so no one person can purge a vault or key. Changing a key service's access policy needs a second Tier 0 approver and alerts the Security Team. A key operation by any identity outside its role also alerts the Security Team, through Defender for Key Vault and Splunk.

---

## Approval

**Approved By:** Pending. The Configuration Control Board reviews version 0.1 in Phase 1.

**Circulated To:** the Platform Team, Fleet Operations, the Security Team, the Data Team, the ML Team, and every team lead whose services draw keys or certificates.

**Approval Date:** Pending.

---

## Periodic Review and Revision

**Review Cadence:** Annually, as a floor.

**Revision Triggers:**
- A change to the approved algorithm baseline
- A change to a key tier, the HSMs, or the program PKI
- A CNSA 2.0 transition milestone, including the cryptographic inventory's completion in Phase 2
- A lost aircraft or a key compromise that tested this plan
- A change to a governing requirement, such as CNSSP 15
- A product substitution recorded in the Security Implementation Plan, for any product this document names
