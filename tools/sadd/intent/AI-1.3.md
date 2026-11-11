## Design Intent
Each model choice is recorded with the criteria it was assessed against, namely the publisher's security practice, licensing, the serialization format, and fitness for the mission. Foundation models come only from the cloud provider's IL5-authorized catalog. Every detection and embedding model starts from a pretrained checkpoint on the approved catalog or is trained from scratch, and each choice records the risks the program accepted.

## External Dependencies
The IL5 cloud provider, which hosts each foundation model deployment inside KESTREL's tenant under its provisional authorization. The publishers of any pretrained checkpoint or framework KESTREL adopts.
