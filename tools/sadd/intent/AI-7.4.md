## Design Intent
Retraining signal is accepted only from authenticated sources. Analyst corrections are bound to the analyst's identity and the inference session they correct. Federated updates are authenticated by each aircraft's device identity. Products released from the IL6 enclave are treated as untrusted input, so they pass the same checks as everything else.

## External Dependencies
The IL6 enclave's owner, whose release review approves every product returned high to low.
