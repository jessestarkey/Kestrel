# Security Implementation Plan Build

The KESTREL Security Implementation Plan in [`docs/04-sip/`](../../docs/04-sip/index.md) is generated from the SABER and from hand-written selections in this folder.

- **`build.py`** writes one record per in-scope SADD outcome, one file per focus area, and fills the index from `index.src.md`.
- **`selections.py`** holds the hand-written choices. `CAP` sets the products, accountable team, rollout phase, dependencies, and tailoring for every outcome in a capability, and `OUT` overrides any of them for one outcome.
- **`catalog.py`** names every selected product and the contract vehicle it is bought under. Section 6 of the plan is built from it.
- **`index.src.md`** is the source of the plan's index.

Scoping comes from [`../saberlib.py`](../saberlib.py), which the SADD build also uses, so the plan always covers exactly the SADD's in-scope outcomes.

## Running it

From the kestrel repository root, with the SABER repository checked out beside it:

```
python tools/sip/build.py
```

The build reports records and activities per phase. It stops if a Maturity Level 1 activity lands after Phase 3, since Level 1 work is due by the ATO decision, or if a pin matches no in-scope activity. It also lists any contract no record uses.

## What the build decides

- **Phase.** Each activity gets its own phase. Maturity Level 1 keeps the capability's phase, set in `CAP` or `OUT`, Level 2 waits for Phase 2 at the earliest, and Level 3 waits for Phase 4. `PINS` moves an activity earlier, with the reason it records. A record starts in the phase of its earliest activity.
- **Funding line.** The fiscal years come from the phases its activities fall in, and the line comes from the accountable team.
- **Activity metadata.** The seven activity-level fields are copied from the SABER unchanged.

Rebuild after any change to the SADD's scope, the selections, or the catalog.
