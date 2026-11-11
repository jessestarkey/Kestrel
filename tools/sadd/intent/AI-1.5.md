## Design Intent
Every pretrained checkpoint is checked against its publisher's signature or published digest when it enters the model registry, and it is refused if either fails. Each foundation model deployment records the exact version the cloud provider serves. A version KESTREL did not approve raises an alert.

## External Dependencies
The IL5 cloud provider, which hosts each foundation model deployment inside KESTREL's tenant under its provisional authorization. The publishers of any pretrained checkpoint or framework KESTREL adopts.
