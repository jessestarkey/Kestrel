## Design Intent
Prompts and inference logs are scanned for personal information, which is redacted from inputs before they reach a model and from the logs. Inference logs follow the DMP's retention schedule, and the foundation model's provider keeps nothing.

## External Dependencies
The IL5 cloud provider, which keeps no prompts or responses under its provisional authorization.
