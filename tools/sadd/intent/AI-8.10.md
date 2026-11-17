## Design Intent
Every system prompt is kept in its use case's repository and versioned with the release. Changes are reviewed like code, signed off by the ISSO, and deployed only through the pipeline. Each change passes an injection-hardening review, and a prompt that fails it cannot deploy. A change that alters a prompt's role or limits triggers re-testing against jailbreak and injection. Every prompt is audited against its approved version each year.

## External Dependencies
None outside the boundary.
