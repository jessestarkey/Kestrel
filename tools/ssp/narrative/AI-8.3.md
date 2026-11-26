Each foundation model will be an Azure OpenAI deployment in KESTREL's own tenant, with customer-managed keys, reached only by private endpoint and workload identity. Prompts carry report excerpts but never raw collection. Azure Government stores no prompts for abuse monitoring, which the ISSM confirms with the provider each year.

A dev/test deployment in ML Dev/Test pins the same model version and is reached from stage over F27. When the provider changes or retires a version, the new one is re-tested before any use case moves to it.
