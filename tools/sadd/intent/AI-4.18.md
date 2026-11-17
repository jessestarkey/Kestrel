## Design Intent
Each model's certification sets an approved envelope for retraining, including hyperparameter ranges. A run whose hyperparameters change outside that envelope alerts the ML Team and the PMO ISSE, and its output needs full Certification to Field. Edge models never use the envelope fast path.

## External Dependencies
None outside the boundary.
