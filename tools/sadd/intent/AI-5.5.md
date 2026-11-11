## Design Intent
Each detection model is tested on out-of-distribution inputs, such as new weather, terrain, sensor faults, and emitter types it was not trained on. The test checks that it lowers its confidence rather than answering wrongly with high confidence.

## External Dependencies
None outside the boundary.
