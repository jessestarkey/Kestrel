## Design Intent
Every API with a published schema is tested from that schema in stage, including authorization tests for each role and partner. Today those are the partner API, the feedback endpoints, and the model endpoints the mission teams call. Business logic tests cover the multi-step approvals, namely the foreign disclosure officer's partner release and the operator's approval of agent drafts. They also try cross-team object access across the payload vendor split.

## External Dependencies
None outside the boundary.
