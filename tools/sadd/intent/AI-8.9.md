## Design Intent
Inputs and outputs of every language model use case are filtered against KESTREL's use policy. The filter also detects classification markings above what KESTREL may hold, so a possible spill is blocked and reported at once.

## External Dependencies
The IL5 cloud provider, which hosts each foundation model deployment inside KESTREL's tenant under its provisional authorization. The provider supplies the in-tenant content filters.
