## Design Intent
Source code lives on performer laptops, so secret scanning runs at all four points. Pre-commit hooks run on the laptops, push protection runs at the repository, the pipeline scans every build, and scheduled scans cover full history. A secret found in history is rotated first and removed second.

## External Dependencies
The performer, which under the interconnection agreement equips the laptops its developers use for KESTREL work. Its developers run the pre-commit hooks.
