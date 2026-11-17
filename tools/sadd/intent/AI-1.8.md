## Design Intent
No KESTREL model may command an aircraft, its flight controls, or its payload. Onboard detection models only cue the operator. The mission-planning agent's drafts take effect only after an operator approves them in the planning queue, the only path to a station (F34). The AI/ML Governance Review Board enforces this at intake, and agent tool scoping enforces it technically. Before an onboard model or the agent is fielded, and each year after, it gets an OT-adjacent AI risk assessment. That assessment combines its threat model, robustness requirements, and a safety-impact determination from the program's airworthiness and systems-safety authority. High findings go to the board and the ISSO.

## External Dependencies
The program's airworthiness and systems-safety authority, which makes the safety-impact determination.
