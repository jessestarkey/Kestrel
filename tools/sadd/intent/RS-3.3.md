## Design Intent
No containment action may touch a ground control station, the launch and recovery equipment, or a datalink while an aircraft under that station's control is airborne. Such actions wait until the operations lead or the shift lead at that site approves them, or the aircraft has landed. The aircraft's lost-link procedure is the fallback, using the same airborne window as CCSD tailoring action 2. Fleet Operations may cut an operating site's conduit at the data center side, and the site's services keep working. Cutting it holds any flight plans queued on F34, so it needs the operations lead's concurrence while a plan is pending. It also blinds OT monitoring, so the IRP limits how long it lasts. The manual runbook covers safe recovery of airborne aircraft before a station is isolated.

## External Dependencies
None outside the boundary.
