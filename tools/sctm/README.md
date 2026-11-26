# SCTM Build

KESTREL's Security Controls Traceability Matrix in [`docs/05-sctm/`](../../docs/05-sctm/index.md) is generated from the CCSD, the SADD, and hand-written dispositions in this folder.

- **`build.py`** writes the matrix page. The [SSP build](../ssp/README.md) imports it and carries the same rows into KESTREL's one OSCAL system security plan, `docs/06-ssp/kestrel-ssp.oscal.json`.
- **`dispositions.py`** holds the choices only a person can make. These are the providers KESTREL inherits from and what each covers, the selected controls that do not apply, and the unclaimed controls an outcome already holds.
- **`data/`** holds NIST's OSCAL High and privacy baseline profiles. They stand in for the CNSSI 1253 selection the CCSD names, which this notional example does not reproduce.

## Running it

From the kestrel repository root, after the SADD is built:

```
python tools/sctm/build.py
```

The build reports the controls in the set, the count of each designation, and the gaps it found.

## What the build decides

- **The set.** The NIST baselines, plus controls the CCSD's tailoring actions add, minus those it removes. A removed control takes its enhancements with it.
- **Designation.** A claimed control is System-Specific, or Hybrid when a provider covers part of it. An unclaimed control is Inherited when a provider covers it. A control in neither is Unassigned, and `NOT_APPLICABLE` overrides both.
- **Gaps.** An unclaimed control an outcome already holds, a control nobody holds, and a control resting only on narrow outcomes are each listed for the SADD's gap register.

Rebuild after any change to the CCSD's tailoring, the SADD's mapping, or the dispositions, then rebuild the SSP so its OSCAL carries the change.
