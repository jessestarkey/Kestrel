## Design Intent
The training platform's job, dataset, and registry interfaces are tested from their schemas for authorization flaws. One check confirms that a pipeline identity cannot mount a snapshot or write a namespace that is not its own.

## External Dependencies
None outside the boundary.
