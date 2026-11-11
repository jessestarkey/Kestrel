## Design Intent
KESTREL accepts model weights only in non-executable formats such as safetensors. Every model artifact entering the registry is scanned for embedded code, and pickle-based or code-carrying formats are refused.

## External Dependencies
The publishers of any pretrained checkpoint or framework KESTREL adopts.
