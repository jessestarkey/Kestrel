## Design Intent
The cryptographic inventory records every place KESTREL relies on quantum-vulnerable public-key cryptography, with the program PKI, the datalinks, and code signing first. The transition plan follows the CNSA 2.0 timelines, and every new design must let algorithms change without redesign.

## External Dependencies
The aircraft and datalink manufacturers, who supply the datalink crypto modules. Their roadmaps set when the datalinks can move to quantum-resistant algorithms.
