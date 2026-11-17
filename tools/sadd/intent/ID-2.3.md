## Design Intent
Federate every cloud user-facing application and administrative console with the cloud identity service, from the analyst portal and the LLM analyst assistant to the cloud administrative consoles. Data center applications federate with the on-premises directory instead, so they keep working if the circuits fail. One sign-on covers the mission applications, while administrative consoles require fresh authentication. Partner systems reach the partner API with mutual TLS under Server and Services Authentication (`ID-3.4`), not through single sign-on.

## External Dependencies
The IL5 cloud provider's identity service, inherited under its provisional authorization.
