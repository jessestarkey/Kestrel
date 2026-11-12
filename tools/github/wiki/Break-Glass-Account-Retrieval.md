> **Notional system.** KESTREL is fictional. This page stands in for a runbook in KESTREL's self-hosted Confluence.

# Break-Glass Account Retrieval

| Field | Value |
|---|---|
| Executes | ID-4.6: Emergency Access Accounts, under the [Account Management Plan](Account-Management-Plan) |
| Owner | Platform Team (Tier 0 administrators) |
| Reviewed by | ISSM |
| Version | 0.1 draft |

## Purpose

This runbook restores administrative access when KESTREL's normal identity path has failed, such as the identity provider being down, a Conditional Access change locking out every administrator, or the cloud tenant refusing all privileged sign-ins. It is for recovering access, not for routine work, and every use is an incident.

## The accounts

| Account set | Where it works | Authenticator | Why it exists |
|---|---|---|---|
| Directory break-glass | Active Directory in the data center and the alternate site | YubiKey 5 FIPS with PIN | Recovers the identity system of record and Tier 0 |
| Cloud tenant break-glass, two accounts | Entra ID and the Azure Government tenant | YubiKey 5 FIPS (FIDO2) with PIN | Recovers the tenant if Entra policy or synchronization fails |
| Ground segment break-glass | The ground control stations and the ground segment network | YubiKey 5 FIPS with PIN, verified locally | Lets operators recover airborne aircraft if identity is down |

Each authenticator verifies without reaching the identity provider, so an identity outage cannot disable the account meant to fix it. The cloud tenant accounts are excluded from Conditional Access for the same reason.

## Custody

- The hardware keys sit in one safe in the data center's Tier 0 room, and their PINs sit in sealed envelopes in a second safe. No single person can open both.
- A second sealed set is held the same way at the alternate site, so losing the data center does not lose break-glass access.
- Custodians are named in the AMP. One is a Platform Team Tier 0 administrator and the other an ISSO.
- Every opening of either safe is written in the custody log inside it, with the date, time, both custodians, and the reason.

## When to use it

Use break-glass only when normal privileged access through the privileged access platform and PIM has failed. The person declaring the emergency must get authorization first:

| Account set | Who authorizes | If they cannot be reached |
|---|---|---|
| Directory or cloud tenant | ISSM | Program manager |
| Ground segment, with an aircraft airborne | Fleet Operations' operations lead, at once | Act first, and notify the ISSM within 15 minutes |

## Steps

1. **Declare.** Open a Severity 1 incident in the service desk. If the service desk is down, call the Security Team's on-call number and record the incident afterward.
2. **Retrieve.** Both custodians open their safes together, sign the custody log, and hand over the key and PIN envelope for only the account set needed.
3. **Sign in** from a privileged access workstation for the directory or cloud tenant, or at the affected station's console for the ground segment.
4. **Confirm the alert.** Every break-glass sign-in pages the Security Team and the CSSP through the security monitoring platform. If no page arrives within five minutes, report it in the incident, since monitoring is also impaired.
5. **Do only the recovery.** Restore normal access and nothing else. Do not change other configuration, and write each action in the incident record as it is taken.
6. **End the session** within four hours. If recovery needs longer, the authorizer renews the authorization and the incident records it.

## After every use

1. Rotate the account's credential and replace its PIN.
2. Reseal the key and PIN in their safes, with both custodians signing the log.
3. The Security Team reviews the session recording and the incident record within two business days.
4. Any gap the use exposed becomes a tracked item, and if the runbook was wrong, this page is updated.

## Testing

Each account set is tested on the AMP's schedule, once a quarter, by a planned use of this runbook outside an emergency. A test follows every step above, including the alert check, rotation, and resealing, and its result is recorded against story ID-4.6 in the tracker.
