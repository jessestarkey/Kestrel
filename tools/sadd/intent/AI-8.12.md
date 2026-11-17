## Design Intent
Onboard models run in the aircraft's trusted execution environment, stored encrypted with keys only its crypto module can use. They are zeroized on tamper or crash detection, or on command while the link holds. Otherwise the weights stay encrypted, so a captured aircraft yields neither usable weights nor keys.

## External Dependencies
The aircraft manufacturer, which supplies the onboard trusted execution environment and crypto module.
