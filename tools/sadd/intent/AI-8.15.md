## Design Intent
AI agents keep working memory for one session only, unless the AI/ML Governance Review Board approves persistent memory for one. The AISP then records its scopes and retention. An agent whose actions can reach the fleet never keeps persistent memory, since a poisoned entry would steer later drafts toward a station. The mission-planning agent is that case. An approved agent's memory is scoped per repository or per user, never shared across teams, and expires after a set period. Each write comes from an explicit user request or an entry the user approves. It carries a label naming its source, author, time, and trust level, with an integrity check verified on recall. Content is screened for embedded instructions when stored and when recalled. A write that comes from processed content alone is blocked and raises an alert. The coding agent is today's case, keeping notes per repository and per developer.

## External Dependencies
None outside the boundary.
