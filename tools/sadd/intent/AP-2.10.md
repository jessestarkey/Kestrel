## Design Intent
High-risk changes get a second review by a designated security reviewer from outside the authoring team. High-risk means authentication and authorization, cryptography, partner release logic, enforcement of the payload vendor split, and any tool an AI agent can call. The reviewer reads the change as an attacker would, and their approval is a required check on the merge.

## External Dependencies
None outside the boundary.
