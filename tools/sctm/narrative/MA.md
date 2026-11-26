# MA: Maintenance

## MA-1

The program manager will issue the maintenance policy as part of KESTREL's system security policy. The Configuration Management Plan's maintenance section, written by IT Operations, will hold the procedures. The Configuration Control Board will approve both, and each will be reviewed at least once a year.

## MA-2

On-premises hardware maintenance will be scheduled in Jira Service Management, escorted, and recorded. The owning team's lead approves it, and Tier 0 maintenance also needs the Platform Team lead. Failed drives stay on site for sanitization. From Phase 3, fleet maintenance runs only in each operating site's weekly window, never while an aircraft under its stations is airborne. After maintenance, a compliance scan confirms the component still meets its baseline.

## MA-2(2)

Maintenance will be scheduled, tracked, and recorded in Jira Service Management, so each maintenance action and its change share one record.

## MA-3

The Security Team will approve the diagnostic tools that maintenance may use. Each tool is scanned at the media intake station before use.

## MA-3(1)

Maintenance tools will be inspected before use, both those KESTREL holds and those a vendor brings, to confirm they are approved and unmodified.

## MA-3(2)

Media carrying diagnostic or test programs will be scanned for malicious code at the media intake station before it is used on any KESTREL system.

## MA-3(3)

Maintenance equipment will not leave with KESTREL information on it. Failed drives stay on site, and any other component leaving the facility first has its storage sanitized with Blancco, or removed and kept. HSMs are zeroized before they ship.

## MA-4

Vendor engineers will perform remote maintenance only from the dedicated vendor host pool in Azure Virtual Desktop. They sign in with ECA Medium Hardware credentials, and only for an open Jira Service Management case. CyberArk brokers and records each session, which lasts at most eight hours and ends when the case closes.

## MA-4(3)

Remote maintenance will run from systems KESTREL controls. Vendor sessions start in the vendor host pool, which is built to KESTREL's own VDI baseline, rather than from the vendor's device.

## MA-5

Only authorized people will perform maintenance. KESTREL's own staff do most of it. A vendor engineer working on site is escorted at all times, and one working remotely is limited to the brokered session for their case.

## MA-5(1)

Vendor engineers without KESTREL access will be escorted on site at all times by an authorized KESTREL staff member. They work only on the equipment in their case.

## MA-6

Support agreements will set replacement times for the HSMs, identity servers, and hub firewalls. Spares cover the mission's tolerance for downtime, including spare stations and aircraft for the fleet.
