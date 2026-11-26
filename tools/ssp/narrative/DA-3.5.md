Keys that Key Vault generates will rotate automatically on the KMP's cadence. Imported keys cannot rotate in place, so an approaching expiry triggers an nShield job that generates, wraps, and imports the replacement. Datalink keys rotate on Fleet Operations' schedule. Every cloud key is also available in the second IL5 region, so recovery never waits on one.

Keys whose loss would destroy data, such as backup keys, are escrowed in the alternate site's HSM under split knowledge. Recovering an escrowed key needs approval from both the ISSM and a Tier 0 administrator.
