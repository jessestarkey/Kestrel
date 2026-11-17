## Design Intent
Incidental imagery of people is blurred or cropped out of training data unless the detection task needs it. The ML Team's person-detection model finds it once certified, and until then a Data Team reviewer blurs or crops by hand. Training sets carry no analyst names or other personal fields, and raw stores in the ML training zone are readable only by the Data Team. The provenance record notes which technique each release used.

## External Dependencies
None outside the boundary.
