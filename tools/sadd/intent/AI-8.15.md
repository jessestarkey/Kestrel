## Design Intent
AI agents keep working memory for one session only, and it is discarded when the session ends. No agent writes persistent memory today, so nothing it reads in one task can steer a later one. An agent that needs memory across sessions must first be approved by the AI/ML Governance Review Board, with its scopes and retention recorded in the AISP. Its memory is then scoped per user, labeled with its source, and screened when stored and when recalled. Neither the mission-planning agent nor the coding agent keeps any.

## External Dependencies
None outside the boundary.
