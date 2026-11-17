## Design Intent
Keep break-glass accounts for the cloud tenant, the directory, and the ground segment. The two cloud accounts use different phishing-resistant methods. The directory and station accounts are console-only passwords under CCSD tailoring action 6, still pending AO approval. If the AO declines it, those accounts use offline smart cards held in the same seals. Logon is limited to named consoles, any use alerts the Security Team and the CSSP, and each password rotates after use. Directory sessions end after four hours, and station sessions once no aircraft under the station is airborne. A station's alert is raised locally and queued until its conduit returns.

## External Dependencies
None outside the boundary.
