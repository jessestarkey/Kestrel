## Design Intent
Onboard models run in the aircraft's trusted execution environment, stored encrypted with keys held in its crypto module. They are zeroized if the aircraft detects tampering or is declared lost. An aircraft that might be captured therefore yields neither usable weights nor keys.

## External Dependencies
The aircraft manufacturer, which supplies the onboard trusted execution environment and crypto module.
