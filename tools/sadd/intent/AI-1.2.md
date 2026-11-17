## Design Intent
Incidental imagery of people is the only personal information in KESTREL's collection. Training sets keep it only where a detection task needs it, and no model is trained to identify individuals. The AISP sets a recall threshold for the person-detection model as a privacy requirement, since its misses decide what reaches dev/test data. The privacy officer approves each new training set's handling, and removing a record later means retraining rather than editing the weights.

## External Dependencies
None outside the boundary.
