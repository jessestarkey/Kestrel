## Design Intent
Every retraining record is validated against its schema, value ranges, and label vocabulary before it joins a snapshot. Each submitter's correction rate is checked for floods. Federated updates are bounded in size and combined by a robust aggregation method, so one aircraft's update cannot dominate a round.

## External Dependencies
None outside the boundary.
