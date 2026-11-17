## Design Intent
Aircraft, stations, and payloads are bought only from their manufacturers, and data center hardware and HSMs only from authorized resellers. Everything is inspected for tampering and counterfeit parts at receipt and on return from vendor service. Stations and aircraft avionics are rescanned for counterfeit components at a fixed interval, under CCSD tailoring action 4. Suspect parts are quarantined and reported to the source and to GIDEP. Firmware is accepted only with a valid manufacturer signature, or a published hash where it is unsigned, and each verified version is recorded in the inventory. Retired components are sanitized, verified, and recorded before disposal.

## External Dependencies
The aircraft, ground equipment, and data center hardware manufacturers and their authorized resellers.
