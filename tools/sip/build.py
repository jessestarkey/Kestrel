"""Build the KESTREL Security Implementation Plan in docs/04-sip/.

Usage (from the kestrel repo root):
    python tools/sip/build.py [--framework PATH]

Scoping comes from tools/saberlib.py, so the plan carries exactly the SADD's
in-scope outcomes. Product, team, phase, and dependency choices come from
selections.py and catalog.py. Activity metadata is carried from the SABER.
"""
import argparse, collections, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
import saberlib as S
from saberlib import REPO, PILLAR, parse, scope
from catalog import PRODUCTS, CONTRACTS, GOV, OSS
from selections import CAP, OUT, PINS, NA, RERATE, ONE, SHARED, STRICT, EXCEPT

ap = argparse.ArgumentParser()
ap.add_argument('--framework', default=os.path.join(os.path.dirname(REPO), 'security-framework'))
args = ap.parse_args()
S.init(args.framework)
DOCS = os.path.join(REPO, 'docs', '04-sip')
SADD = '../03-sadd'

# Phase -> (name, start, end, funding status)
PHASES = {
    1: ('Foundation', '2027-01-01', '2027-06-30', 'Funded (FY27 base)'),
    2: ('Protect and Operate', '2027-07-01', '2027-12-31', 'Funded (FY27 and FY28 base)'),
    3: ('Mission, AI, and Fleet', '2028-01-01', '2028-06-30', 'Pending approval (FY28 RDT&E and O&M)'),
    4: ('Maturity', '2028-07-01', '2028-12-31', 'Unfunded (FY28 and FY29 requests)'),
}
# Fiscal years each phase spans. The federal fiscal year starts on 1 October.
FY = {1: ['FY27'], 2: ['FY27', 'FY28'], 3: ['FY28'], 4: ['FY28', 'FY29']}
# Work due by the ATO decision must be ready two months early, so the SCA can assess it.
ASSESS_READY = '2028-04-30'
SEC6 = 'index.md#6-contracting-and-procurement-cross-references'


def funding(team, fys):
    if 'SCA' in team or team.startswith('Program Office'):
        line = 'program management'
    elif team.startswith('Fleet Operations'):
        line = 'RDT&E, fleet integration'
    elif any(t in team for t in ('ML Team', 'Mission', 'Data Team')):
        line = 'RDT&E, mission and ML'
    else:
        line = 'O&M, platform and security operations'
    return f"{' and '.join(fys)} {line}"


def contracting(keys):
    ids, gov, oss = [], False, False
    for k in keys:
        c = PRODUCTS[k][1]
        if c == GOV:
            gov = True
        elif c == OSS:
            oss = True
        elif c not in ids:
            ids.append(c)
    parts = [f'[{c}]({SEC6})' for c in ids]
    extra = [x for x, f in (('government-furnished', gov), ('open source', oss)) if f]
    if not parts:
        return 'None. ' + ' and '.join(extra).capitalize() + ', so no new contract is needed.'
    s = ', '.join(parts)
    return s + (f", plus {' and '.join(extra)} components" if extra else '')


def level(a):
    m = re.match(r'Level (\d)', ' '.join(a['f'].get('Maturity Model', [''])))
    return int(m.group(1)) if m else None


def cell(a, f):
    v = ' '.join(a['f'].get(f, [''])).strip()
    if f == 'Maturity Model':
        v = re.sub(r'\s*\(.*\)$', '', v)
    return v


ACT_COLS = ['Control Type', 'Cross-Cutting Discipline', 'Maturity Model', 'ConMon Activity',
            'Level of Effort', 'Cost', 'Time Estimation']
os.makedirs(DOCS, exist_ok=True)
inherited = collections.defaultdict(list)
used_na = set(); used_pins = set(); act_count = collections.Counter()
starts = {}; dep_refs = {}
stats = []; contract_use = collections.defaultdict(list); phase_count = collections.Counter()
phase_fa = collections.defaultdict(collections.Counter); warnings = []
for fname in sorted(os.listdir(S.FW)):
    m = re.match(r'(0[2-9]|1[0-3])-saber-(.+)\.md$', fname)
    if not m:
        continue
    pillar = PILLAR[m.group(1)]
    fa, caps = parse(os.path.join(S.FW, fname))
    code = fa.split(':')[0].strip()
    sadd_file = f'{SADD}/{m.group(1)}-{m.group(2)}.md'
    body = [f'# {fa}', '',
            f'*KESTREL Security Implementation Plan, Section 4 ({pillar}). Each record implements the outcome of the same ID in the '
            f'[SADD]({sadd_file}), which holds its design intent and control mapping. See the [index](index.md) for the phases, '
            'issue tracker mapping, and contracts. Activity-level metadata is carried from the SABER.*', '']
    n = acts = 0
    for cap in caps:
        cid = cap['title'].split(':')[0].strip()
        recs = []
        for o in cap['outcomes']:
            ok, *_ = scope(o)
            if not ok:
                continue
            oid, ot = [x.strip() for x in o['title'].split(':', 1)]
            sel = dict(CAP[cid]); sel.update(OUT.get(oid, {}))
            # Tailoring copied from the capability usually describes a sibling, not this outcome.
            if sel['tailoring'] == CAP[cid]['tailoring'] and sel['tailoring'] != ONE and oid not in SHARED:
                inherited[code].append(oid)
            # Each activity takes a phase from its maturity level: Level 1 keeps the
            # outcome's base phase, Level 2 waits for Phase 2 at the earliest, and
            # Level 3 waits for Phase 4. A pin in selections.PINS overrides that.
            base = sel['phase']
            aph = {}
            for a in o['acts']:
                aid = a['title'].split(':')[0].strip()
                if aid in NA:
                    used_na.add(aid); continue
                lv = level(a)
                p = {1: base, 2: max(base, 2), 3: 4}.get(lv, base)
                if aid in PINS:
                    p = PINS[aid][0]; used_pins.add(aid)
                if lv == 1 and p > 3:
                    sys.exit(f'{aid} is Maturity Level 1, required for ATO, but lands in Phase {p}')
                aph[aid] = p
                act_count[p] += 1
            phase = min(aph.values())
            starts[oid] = phase; dep_refs[oid] = re.findall(r'\b([A-Z]{2}-\d+(?:\.\d+)?)\b', sel['deps'])
            recs.append((o, oid, ot, sel, phase, aph))
        if not recs:
            continue
        body += [f"## {cap['title']}", '']
        for o, oid, ot, sel, phase, aph in recs:
            n += 1; phase_count[phase] += 1; phase_fa[phase][code] += 1
            for k in sel['tools']:
                c = PRODUCTS[k][1]
                if c not in (GOV, OSS) and oid not in contract_use[c]:
                    contract_use[c].append(oid)
            pname = PHASES[phase][0]
            # A record whose fleet slice waits for Phase 3 stays open through it, via 'through'.
            last = max(max(aph.values()), sel.get('through', 0)); end = ASSESS_READY if last == 3 else PHASES[last][2]
            span = f'Phase {phase}, {pname}' + (f', with work through Phase {last}' if last > phase else '')
            fys = sorted({y for p in list(aph.values()) + [last] for y in FY[p]})
            body += [f'### {oid}: {ot}', '',
                     f"**Selected Tool / Product / Service:** {', '.join(PRODUCTS[k][0] for k in sel['tools'])}", '',
                     f"**Environment-Specific Tailoring:** {sel['tailoring']}", '',
                     f"**Accountable Team:** {sel['team']}", '',
                     f"**Dependencies:** {sel['deps']}", '',
                     f"**Funding Line:** {funding(sel['team'], fys)}", '',
                     f'**Rollout Phase:** {span}', '',
                     f'**Target Date / Sprint:** {end}', '',
                     f"**Contracting / Procurement Reference:** {contracting(sel['tools'])}", '',
                     '**Status:** Not Started', '',
                     '**Activity-Level Metadata:**', '',
                     '| Activity | Phase | ' + ' | '.join(ACT_COLS) + ' |', '|---|---|' + '---|' * len(ACT_COLS)]
            for a in o['acts']:
                acts += 1
                aid = a['title'].split(':')[0].strip()
                if aid in NA:
                    body.append(f"| {a['title']} | N/A | " + ' | '.join(cell(a, f) for f in ACT_COLS) + ' |'); continue
                pin = ' (pinned)' if aid in PINS else ''
                rr = RERATE.get(aid, ({}, ''))[0]
                cells = [f'{rr[f]} (re-rated)' if f in rr else cell(a, f) for f in ACT_COLS]
                body.append(f"| {a['title']} | {aph[aid]}{pin} | " + ' | '.join(cells) + ' |')
            pinned = [aid for aid in aph if aid in PINS]
            if pinned:
                body += ['', '**Pinned:** ' + ' '.join(f'{aid}: {PINS[aid][1]}' for aid in pinned)]
            rerated = [aid for aid in aph if aid in RERATE]
            if rerated:
                body += ['', '**Re-rated:** ' + ' '.join(f'{aid}: {RERATE[aid][1]}' for aid in rerated)]
            exc = [aid for aid in aph if aid in EXCEPT]
            if exc:
                body += ['', '**Exception:** ' + ' '.join(f'{aid}: {EXCEPT[aid]}' for aid in exc)]
            na = [a['title'].split(':')[0].strip() for a in o['acts'] if a['title'].split(':')[0].strip() in NA]
            if na:
                body += ['', '**Not applicable:** ' + ' '.join(f'{aid}: {NA[aid]}' for aid in na)]
            body.append('')
    out = f'{m.group(1)}-{m.group(2)}.md'
    open(os.path.join(DOCS, out), 'w', encoding='utf-8', newline='\n').write('\n'.join(body))
    stats.append((pillar, fa, code, out, n, acts))
    print(f'{out:36} records {n:3} activities {acts:4}')

# Index
src = open(os.path.join(HERE, 'index.src.md'), encoding='utf-8').read()
codes = [s[2] for s in stats]
ph = ['| Phase | Target Timeframe | Dependencies Satisfied / Rationale | Funding Status | Major Outcomes in This Phase |',
      '|---|---|---|---|---|']
RATIONALE = {
    1: 'Builds what everything else assumes, namely the landing zone and hubs, identity and privileged access, keys and PKI, the pipeline, logging into the security monitoring platform, and the governance bodies and core plans.',
    2: 'Needs Phase 1 identity, keys, pipeline, and logging. Hardens and watches the estate, adds application security gates, data protection, backup and recovery, detection content, and incident response, and brings AI governance up before any AI build.',
    3: 'Needs Phase 2 gates and detection. Builds the AI lifecycle controls, model serving guardrails, and the fleet and ground segment controls, and ends with the SCA assessment and the ATO decision.',
    4: 'Needs a fielded system to tune against. Adds the Level 3 maturity outcomes, such as deception, breach and attack simulation, RASP, and post-quantum migration planning.',
}
for p, (name, start, end, fund) in PHASES.items():
    major = ', '.join(f'{c} ({phase_fa[p][c]})' for c in codes if phase_fa[p][c])
    ph.append(f'| Phase {p}, {name} | {start} to {end} | {RATIONALE[p]} | {fund} | '
              f'{act_count[p]} activities. {phase_count[p]} records start here: {major} |')
status = ['| Pillar | Focus Area | Records | Activities |', '|---|---|---|---|']
for pillar, fa, code, out, n, acts in stats:
    status.append(f'| {pillar} | [{fa}]({out}) | {n} | {acts} |')
status.append(f"| | **Total** | **{sum(s[4] for s in stats)}** | **{sum(s[5] for s in stats)}** |")
c6 = ['| Contract | Selected Product / Service | Required Contract Clause(s) | Source | Status | Records |', '|---|---|---|---|---|---|']
for cid, (veh, clauses, srcx, st) in CONTRACTS.items():
    c6.append(f'| {cid} | {veh} | {clauses} | {srcx} | {st} | {len(contract_use[cid])} |')
gf = sorted({PRODUCTS[k][0] for k in PRODUCTS if PRODUCTS[k][1] == GOV})
os_ = sorted({PRODUCTS[k][0] for k in PRODUCTS if PRODUCTS[k][1] == OSS}, key=str.lower)
src = (src.replace('{{PHASES}}', '\n'.join(ph)).replace('{{STATUS}}', '\n'.join(status))
          .replace('{{CONTRACTS}}', '\n'.join(c6)).replace('{{GOV}}', ', '.join(gf))
          .replace('{{OSS}}', ', '.join(os_)).replace('{{NREC}}', str(sum(s[4] for s in stats))))
open(os.path.join(DOCS, 'index.md'), 'w', encoding='utf-8', newline='\n').write(src)
unused = [c for c in CONTRACTS if not contract_use[c]]
print(f"{sum(phase_count.values())} records by starting phase: {dict(sorted(phase_count.items()))}")
print(f"activities by phase: {dict(sorted(act_count.items()))}")
print(f'{len(used_pins)} pins used')
if set(NA) - used_na:
    sys.exit(f'Not-applicable entries that match no in-scope activity: {sorted(set(NA) - used_na)}')
if set(PINS) - used_pins:
    sys.exit(f'Pins that match no in-scope activity: {sorted(set(PINS) - used_pins)}')
if unused:
    print('Contracts no record uses:', unused)

# Every dependency must start no later than the outcome that relies on it. A
# reference to a capability, such as AI-5, means every in-scope outcome in it.
late, missing = [], []
for oid, refs in dep_refs.items():
    for r in refs:
        targets = [r] if r in starts else [o for o in starts if o.startswith(r + '.')]
        if not targets:
            missing.append(f'{oid} -> {r}')
        late += [f'{oid} (Phase {starts[oid]}) depends on {t} (Phase {starts[t]})' for t in targets if starts[t] > starts[oid]]
for c, ids in inherited.items():
    if c in STRICT:
        sys.exit(f'{c} records still carry their capability tailoring: {ids}. Write their own in OUT or list them in SHARED.')
print('Records still carrying capability tailoring, by unreviewed focus area: ' + ', '.join(f'{c} {len(v)}' for c, v in inherited.items()))
if missing:
    sys.exit('Dependencies on outcomes that are not in scope: ' + ', '.join(missing))
if late:
    sys.exit('Dependencies scheduled after the outcomes that rely on them:\n  ' + '\n  '.join(late))
print(f'{sum(len(v) for v in dep_refs.values())} dependency references, all scheduled in order')
