## Design Intent
Key rotation is automated on the KMP's cadence for every key class, and datalink keys rotate on Fleet Operations' schedule. The hierarchy runs from HSM-held root keys to the cloud's customer-managed keys. Keys whose loss would destroy data, such as backup keys, are escrowed in the HSMs under split knowledge.

## External Dependencies
The IL5 cloud provider, whose HSM-backed key management service holds the cloud keys under its provisional authorization.
