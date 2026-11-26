# SSP Build

KESTREL's System Security Plan in [`docs/06-ssp/`](../../docs/06-ssp/index.md) is generated, as a page per focus area and as OSCAL. Sources generate both outputs, and neither output is edited by hand, so the two cannot drift apart.

- **`build.py`** writes the SSP pages and `kestrel-ssp.oscal.json`. It imports the [SCTM build](../sctm/README.md) for the control rows, so KESTREL keeps one OSCAL system security plan.
- **`index.src.md`** holds the hand-written sections, such as Distribution and Approval, with placeholders for the generated ones.
- **`status.json`** is a snapshot of the project board's statuses, which sets each outcome's status.
- **`narrative/`** holds a file per outcome stating what was actually built, once its work is Done. See its [README](narrative/README.md).

## Where each part comes from

| SSP part | Source |
|---|---|
| Section 2, System Identification | `docs/01-system-description.md`, which stays the source until SSP 1.0 |
| Sections 3 and 4, categorization and baseline | `docs/02-ccsd.md`, read through the SCTM build |
| Each outcome's related controls | Its NIST Control Mapping in the SADD |
| Each outcome's status | `status.json`. Planned while none of its work is Done, Partially Does once some is, and Currently Does when its story is Done. |
| Each outcome's narrative | `narrative/<ID>.md` if it exists, otherwise its schedule in the Security Implementation Plan |
| Configuration Detail | The trace lines in each governing plan's wiki source, under `tools/github/wiki/` |
| Source SIP Record | The outcome's record in `docs/04-sip/` |

## Running it

From the kestrel repository root:

```
python tools/github/issues.py status
python tools/ssp/build.py
python tools/oscal/validate.py tools/oscal/oscal_ssp_schema.json docs/06-ssp/kestrel-ssp.oscal.json
```

The first command needs the GitHub CLI and refreshes `status.json`. Skip it to rebuild from the committed snapshot. The validator needs the `jsonschema` package. Commit the snapshot with the SSP, so every status change traces to a board state in git.

Rebuild after any change to the system description, the CCSD, the SADD, the Security Implementation Plan, a governing plan's trace lines, a narrative, or the board.
