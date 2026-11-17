## Design Intent
Key rotation is automated on the KMP's cadence for every key class, and datalink keys rotate on Fleet Operations' schedule. Cloud keys imported from the HSMs rotate by a scheduled re-import, and they are available in the second IL5 region used for recovery. Keys whose loss would destroy data, such as backup keys, are escrowed in the alternate site's HSM under split knowledge. Recovering an escrowed key needs the ISSM's and a Tier 0 administrator's approval.

## External Dependencies
The IL5 cloud provider, whose HSM-backed key management service holds the cloud keys under its provisional authorization.
