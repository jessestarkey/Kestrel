## Design Intent
Canary credentials sit in every spoke's vault and in the directory, decoy hosts sit in each data center segment, and a decoy dataset sits in each data lake zone. None of them has a legitimate user, and backup and Data Team pipeline jobs are excluded from touching them. Any touch alerts the Security Team and the CSSP at the highest priority, with the decoy's location attached.

## External Dependencies
The CSSP, which receives deception alerts around the clock.
