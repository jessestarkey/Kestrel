## Design Intent
Retraining signal is accepted only from authenticated sources. Analyst corrections are bound to the analyst's identity and the inference session they correct. Federated updates are authenticated by each aircraft's device identity, and onboard training computes them against a copy, so the certified model an aircraft runs never changes in flight. IL6 releases are untrusted input and pass the same checks as everything else.

## External Dependencies
The IL6 enclave's owner, whose release review approves every product returned high to low.
