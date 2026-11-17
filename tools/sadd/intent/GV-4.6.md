## Design Intent
The board receives each AI supplier risk finding and decides its treatment. Findings come from model selection, label integrity, foundation model dependency governance, and vendor assessment. Each AI supplier is tiered, and any acceptance of supplier risk routes through Risk Acceptance Process (`RK-1.4`). Each foundation model and other vendor-delivered model is registered in the inventory once its risk is treated.

## External Dependencies
The cloud provider, the foundation model's publisher, and the publishers of pretrained checkpoints.
