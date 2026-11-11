## Design Intent
One policy engine decides data access from user and data attributes, namely team, payload vendor rights, role, partner nation, and the record's labels. Its enforcement points are every application and partner-facing API, each data lake zone, and the report index's retrieval. KESTREL holds no classified compartments, so the payload vendor split is enforced like a compartment, and flows between zones are allowed only where F18 permits. Policy changes are tested against a fixed set of access cases before deployment.

## External Dependencies
The payload vendors, whose data rights terms the vendor attributes encode.
