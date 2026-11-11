## Design Intent
Each foundation model is a CSP-hosted deployment inside KESTREL's boundary, reached by private endpoint with provider-side prompt logging disabled. Prompts may carry report excerpts at IL5 but never raw collection. Each deployment pins its model version, and a version change or deprecation notice triggers re-testing before the use case moves to it.

## External Dependencies
The IL5 cloud provider, which hosts each foundation model deployment inside KESTREL's tenant under its provisional authorization. The model's publisher, whose versions and deprecations the provider passes on.
