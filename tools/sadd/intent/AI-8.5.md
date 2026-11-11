## Design Intent
Every inference request is validated against its endpoint's input schema, types, and size limits before it reaches a model. That covers image dimensions and formats for the detection models, and prompt length for language model use cases.

## External Dependencies
None outside the boundary.
