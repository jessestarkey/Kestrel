> **Notional system.** KESTREL is fictional. This page stands in for a runbook in KESTREL's self-hosted Confluence.

# Break-Glass Account Retrieval

| Field | Value |
|---|---|
| Executes | ID-4.6: Emergency Access, under the [Account Management Plan](Account-Management-Plan) |
| Owner | Platform Team (Tier 0 administrators) |
| Reviewed by | ISSM |
| Version | 0.1 draft |

## Purpose

This runbook restores administrative access when KESTREL's normal identity path has failed, such as the identity provider being down, a Conditional Access change locking out every administrator, or the cloud tenant refusing all privileged sign-ins. It is for recovering access, not for routine work, and every use is an incident.

## The accounts

| Account set | Where it works | Authenticator | Why it exists |
|---|---|---|---|
| Cloud tenant break-glass, two accounts | Entra ID and the Azure Government tenant | One FIDO2 key, and one certificate on a YubiKey's smart card applet, each with a PIN | Recovers the tenant if Entra policy, synchronization, or one sign-in method fails |
| Directory break-glass | Active Directory, only at a domain controller or privileged access workstation console in the data center or the alternate site | Long random password | Recovers the identity system of record and Tier 0, including when the PKI itself has failed |
| Ground segment break-glass | One station's console at each operating site | Long random password | Lets operators recover airborne aircraft if a station's smart card check fails |

The two cloud accounts use different methods, so the failure of one method cannot lock out both, and both are excluded from Conditional Access. The directory and ground segment accounts use passwords so that their recovery never depends on the PKI or identity provider being fixed. That is a tailored exception to the phishing-resistant MFA requirement, which the [Account Management Plan](Account-Management-Plan) records with its compensating controls.

## Custody

- The cloud keys sit in one safe in the data center's Tier 0 room, and their PINs sit in sealed envelopes in a second safe. The directory password is split in two halves, one sealed in each safe. No single person can open both.
- A second sealed set of the cloud and directory credentials is held the same way at the alternate site, so losing the data center does not lose break-glass access.
- Each operating site seals its ground segment password in two halves, in two safes at that site, so recovery happens where the aircraft is.
- Custodians are named in AMP Section 11. At the data center and the alternate site, one safe's custodian is a Platform Team Tier 0 administrator and the other's an ISSO. At an operating site, they are Fleet Operations' site lead and the operations lead. Each has a named alternate.
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
3. **Sign in** from a privileged access workstation for the cloud tenant, at a domain controller or privileged access workstation console for the directory, or at the affected station's console for the ground segment. Use the data center or the alternate site, whichever is still running.
4. **Confirm the alert.** Every break-glass sign-in pages the Security Team and the CSSP through the security monitoring platform. If no page arrives within five minutes, report it in the incident, since monitoring is also impaired.
5. **Do only the recovery.** Restore normal access and nothing else. Do not change other configuration, and write each action in the incident record as it is taken.
6. **End the session** within four hours. If recovery needs longer, the authorizer renews the authorization and the incident records it.

## After every use

1. Rotate the account's password, or reissue the key and replace its PIN.
2. Reseal the key and PIN in their safes, with both custodians signing the log.
3. The Security Team reviews the session recording and the incident record within two business days.
4. Any gap the use exposed becomes a tracked item, and if the runbook was wrong, this page is updated.

## Testing

Each account set is tested on the AMP's schedule, once a quarter, by a planned use of this runbook outside an emergency. A test follows every step above, including the alert check, rotation, and resealing, and its result is recorded against story ID-4.6 in the tracker.
