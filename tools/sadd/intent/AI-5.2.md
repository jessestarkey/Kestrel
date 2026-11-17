## Design Intent
Every language model use case is tested for prompt injection through each path content reaches it. For the LLM analyst assistant, that includes injected instructions planted in mission reports and in products released from the IL6 enclave. For AI agents, it includes injected instructions in tool responses. For AI-assisted alert triage, it includes attacker-written content in the logs and alerts F32 carries. Each successful injection is tracked to a fix that constrains it, and the test is re-run before the finding closes.

## External Dependencies
None outside the boundary.
