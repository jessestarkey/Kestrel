# SADD Build

The KESTREL SADD in [`docs/03-sadd/`](../../docs/03-sadd/index.md) is part generated and part hand-written. This folder holds both halves and the script that joins them.

- **`build.py`** reads the SABER framework and KESTREL's system description, decides which outcomes are in scope, and writes the SADD files.
- **`intent/`** holds the hand-written text, one file per outcome, named by outcome ID (for example `ID-1.1.md`). Each file has a `## Design Intent` section and a `## External Dependencies` section.
- **`index.src.md`** is the source of the SADD's index. The build fills in its footprint checklist, Section 5 status table, control count, and Automate and Visualize counts.

## Running it

From the kestrel repository root, with the SABER repository checked out beside it:

```
python tools/sadd/build.py
```

Pass `--framework PATH` if the SABER repository is somewhere else. The build writes a focus area's file only once every in-scope outcome in it has an intent file, and it reports how many are still missing.

## What the build decides

- **Scope.** An outcome is in scope when at least one of its deployment types and at least one of its affected components are in KESTREL's footprint. The footprint is the system description's component tables plus the `PROSE` and `DESIGN` sets in `build.py`. `MANUAL_OUT` removes outcomes that tailoring or a design decision rules out, each with its reason.
- **Carried fields.** NIST Control Mapping, Security Impact, and every activity field are copied from the SABER unchanged. Deployment Type and Affected Components are narrowed to KESTREL's footprint.
- **Section 7.** The control coverage table is built from every in-scope outcome, written or not, since the mappings come from the SABER.

Rebuild after any change to the system description, the intent files, or the SABER version KESTREL is aligned to.
