"""Build KESTREL's Security Controls Traceability Matrix (SCTM).

Reads:
  - tools/sctm/data/*.json: NIST's OSCAL High and privacy baselines, a notional stand-in for
    the CNSSI 1253 High/High/Moderate selection the CCSD names
  - docs/02-ccsd.md: the information types (Section 2), their impact values (Section 3), and the
    tailoring actions (Section 7)
  - docs/03-sadd/control-coverage.md: every control the SADD's outcomes claim
  - tools/sctm/dispositions.py: provider portions, not-applicable controls, and unclaimed
    controls an outcome already meets

Writes:
  - docs/05-sctm/index.md: the matrix a person reads

The SSP build (tools/ssp/build.py) imports this module for the same rows, and writes them
into KESTREL's one OSCAL system security plan, docs/06-ssp/kestrel-ssp.oscal.json.

Run from the repository root: python tools/sctm/build.py
"""
import glob
import json
import os
import re
import sys
import uuid
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dispositions import PROVIDERS, INHERITED, NOT_APPLICABLE, MET_UNCLAIMED, NARROW  # noqa: E402

VERSION, DATE = '0.4', '2026-11-26'
SOURCES = {'CCSD': '1.0, with 1.1 pending', 'SADD': '0.10', 'SIP': '0.9'}
DATA = os.path.join(ROOT, 'tools', 'sctm', 'data')
OUT = os.path.join(ROOT, 'docs', '05-sctm')
BASE_URL = 'https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/'
HIGH = 'NIST_SP-800-53_rev5_HIGH-baseline_profile.json'
PRIVACY = 'NIST_SP-800-53_rev5_PRIVACY-baseline_profile.json'
NS = 'https://github.com/jessestarkey/Kestrel/ns/sctm'
UUID_NS = uuid.UUID('6f1d4c2a-9b7e-4e1f-8a35-2c0d5e7b9a41')
FAMILIES = ['AC', 'AT', 'AU', 'CA', 'CM', 'CP', 'IA', 'IR', 'MA', 'MP', 'PE', 'PL', 'PM', 'PS',
            'PT', 'RA', 'SA', 'SC', 'SI', 'SR']
CHAPTERS = {'ID': '02-identity', 'DI': '03-device-and-infrastructure', 'NE': '04-network-and-environment',
            'AP': '05-application', 'AI': '06-artificial-intelligence', 'DA': '07-data', 'DE': '08-detection',
            'RS': '09-response', 'RC': '10-recovery', 'GV': '11-governance', 'RK': '12-risk', 'CO': '13-compliance'}


def uid(*parts):
    return str(uuid.uuid5(UUID_NS, '/'.join(parts)))


def from_oscal(i):
    m = re.fullmatch(r'([a-z]{2})-(\d+)(?:\.(\d+))?', i)
    return f"{m[1].upper()}-{m[2]}" + (f"({m[3]})" if m[3] else '')


def to_oscal(c):
    m = re.fullmatch(r'([A-Z]{2})-(\d+)(?:\((\d+)\))?', c)
    return f"{m[1].lower()}-{m[2]}" + (f".{m[3]}" if m[3] else '')


def key(c):
    m = re.fullmatch(r'([A-Z]{2})-(\d+)(?:\((\d+)\))?', c)
    return (FAMILIES.index(m[1]), int(m[2]), int(m[3] or 0))


def base(c):
    return c.split('(')[0]


def baseline(name):
    d = json.load(open(os.path.join(DATA, name), encoding='utf-8'))
    return [from_oscal(i) for imp in d['profile']['imports']
            for inc in imp.get('include-controls', []) for i in inc.get('with-ids', [])]


def section(text, heading):
    i = text.index(heading)
    j = text.find('\n## ', i + len(heading))
    return text[i:j if j > 0 else len(text)]


def rows(block):
    out = []
    for line in block.splitlines():
        if line.startswith('| ') and not line.startswith('|---'):
            out.append([c.strip() for c in line.strip().strip('|').split('|')])
    return out[1:]


def unbold(s):
    return s.replace('**', '').strip()


# Sources
ccsd = open(os.path.join(ROOT, 'docs', '02-ccsd.md'), encoding='utf-8').read()
actions = OrderedDict()
for r in rows(section(ccsd, '## 7. Tailoring Actions')):
    if r[0].isdigit():
        actions[r[1]] = {'n': int(r[0]), 'action': r[2], 'decision': r[-1]}
types = {}
for r in rows(section(ccsd, '## 2.')):
    if r[0].isdigit():
        types[int(r[0])] = {'title': r[1], 'id': r[2].split(',')[0].strip()}
for r in rows(section(ccsd, '## 3.')):
    if r[0].isdigit() and int(r[0]) in types:
        types[int(r[0])].update(c=unbold(r[2]), i=unbold(r[3]), a=unbold(r[4]))

claims = {}
for line in open(os.path.join(ROOT, 'docs', '03-sadd', 'control-coverage.md'), encoding='utf-8'):
    m = re.match(r'\| ([A-Z]{2}-\d+(?:\(\d+\))?) \| (Full|Partial) \| ([^|]+) \|', line)
    if m:
        claims[m[1]] = (m[2], [o.strip() for o in m[3].split(',')])

high, privacy = baseline(HIGH), baseline(PRIVACY)
removed = {c for c, a in actions.items() if a['action'] == 'Removed'}
added = {c for c, a in actions.items() if a['action'] == 'Added'}
selected = (set(high) | set(privacy) | added)
removed_all = {c for c in selected if base(c) in removed or c in removed} | removed
selected -= removed_all


def tailoring(c):
    a = actions.get(c)
    if a:
        d = a['decision']
        pending = ', proposed' if d.startswith('Pending') else (', approved with conditions' if d.startswith('Modified') else '')
        return f"Action {a['n']}: {a['action'].lower()}{pending}"
    if base(c) in actions and actions[base(c)]['action'] == 'Removed':
        return f"Removed with its base, action {actions[base(c)]['n']}"
    return ''


# Rows
matrix = []
for c in sorted(selected | removed_all, key=key):
    row = {'control': c, 'tailoring': tailoring(c), 'claim': claims.get(c), 'providers': [], 'portion': '',
           'note': '', 'gap': None}
    prov = INHERITED.get(c) or INHERITED.get(c[:2])
    if prov:
        row['providers'], row['portion'] = prov
    if c in removed_all:
        row['designation'] = 'Removed'
    elif c in NOT_APPLICABLE:
        row['designation'], row['note'] = 'Not applicable', NOT_APPLICABLE[c]
    elif c in claims:
        row['designation'] = 'Hybrid' if prov else 'System-Specific'
    elif c in MET_UNCLAIMED:
        o, why = MET_UNCLAIMED[c]
        row['designation'] = 'Hybrid' if prov else 'System-Specific'
        row['note'] = f"Held by {o}, which does not claim it. {why}"
        row['gap'] = ('met', o)
    elif prov:
        row['designation'] = 'Inherited'
    else:
        row['designation'] = 'Unassigned'
        row['note'] = 'No outcome or provider holds it.'
        row['gap'] = ('open', None)
    if c in NARROW and c in claims:
        row['note'] = (row['note'] + ' ' if row['note'] else '') + 'Its only owners are narrow outcomes. A system-wide owner is still to be named.'
        row['gap'] = ('narrow', None)
    matrix.append(row)
beyond = sorted(set(claims) - selected - removed_all, key=key)


def outcomes(row):
    if not row['claim']:
        return 'None'
    return f"{', '.join(row['claim'][1])} ({row['claim'][0]})"


def providers(row):
    return ', '.join(PROVIDERS[p][0] for p in row['providers'])


def cell(s):
    return s.replace('|', '\\|')


# Control names, each outcome's claim sentences, and each outcome's build status
TITLES = json.load(open(os.path.join(DATA, 'control-titles.json'), encoding='utf-8'))['titles']
FAMILY_NAMES = {'AC': 'Access Control', 'AT': 'Awareness and Training', 'AU': 'Audit and Accountability',
                'CA': 'Assessment, Authorization, and Monitoring', 'CM': 'Configuration Management',
                'CP': 'Contingency Planning', 'IA': 'Identification and Authentication', 'IR': 'Incident Response',
                'MA': 'Maintenance', 'MP': 'Media Protection', 'PE': 'Physical and Environmental Protection',
                'PL': 'Planning', 'PM': 'Program Management', 'PS': 'Personnel Security',
                'PT': 'PII Processing and Transparency', 'RA': 'Risk Assessment', 'SA': 'System and Services Acquisition',
                'SC': 'System and Communications Protection', 'SI': 'System and Information Integrity',
                'SR': 'Supply Chain Risk Management'}


def slug(heading):
    s = re.sub(r'[^\w\- ]', '', heading.strip().lower())
    return s.replace(' ', '-')


OUTCOME = {}      # outcome ID -> (title, SADD chapter file), for the links into the SSP
for code, chapter in CHAPTERS.items():
    path = os.path.join(ROOT, 'docs', '03-sadd', chapter + '.md')
    if not os.path.exists(path):
        continue
    for blk in re.split(r'\n### ', open(path, encoding='utf-8').read())[1:]:
        head, _, _ = blk.partition('\n')
        oid, _, title = head.partition(': ')
        OUTCOME[oid.strip()] = (title.strip(), chapter + '.md')

_status_path = os.path.join(ROOT, 'tools', 'ssp', 'status.json')
BOARD = json.load(open(_status_path, encoding='utf-8'))['status'] if os.path.exists(_status_path) else {}


def built(oid):
    """How far an outcome is built, from the board snapshot."""
    if BOARD.get(oid) == 'Done':
        return 'done'
    if any(k.startswith(oid + '.') and v == 'Done' for k, v in BOARD.items()):
        return 'partial'
    return 'planned'


def impl_status(row):
    d = row['designation']
    if d in ('Removed', 'Not applicable', 'Inherited'):
        return d
    if d == 'Unassigned':
        return 'No owner'
    oids = row['claim'][1] if row['claim'] else [row['gap'][1]] if row['gap'] and row['gap'][1] else []
    states = [built(o) for o in oids]
    if states and all(s == 'done' for s in states):
        return 'Implemented'
    if any(s != 'planned' for s in states):
        return 'Partially implemented'
    return 'Planned'


def sentence(s):
    s = s.strip()
    return s[0].upper() + s[1:] if s else s


WRITTEN = {}      # control -> its implementation narrative, from tools/sctm/narrative/<family>.md
for path in sorted(glob.glob(os.path.join(ROOT, 'tools', 'sctm', 'narrative', '[A-Z][A-Z].md'))):
    for blk in re.split(r'\n## ', open(path, encoding='utf-8').read())[1:]:
        cid, _, text = blk.partition('\n')
        WRITTEN[cid.strip()] = ' '.join(p.strip() for p in text.strip().split('\n\n'))


def tailoring_note(t):
    m = re.match(r'Action (\d+): (.+?)(, proposed|, approved with conditions)?$', t)
    if m:
        state = {', proposed': ", pending the AO's approval",
                 ', approved with conditions': ', approved by the AO with conditions'}
        return f"CCSD tailoring action {m.group(1)} ({m.group(2).lower()}) applies{state.get(m.group(3), '')}."
    m = re.match(r'Removed with its base, action (\d+)', t)
    return f'CCSD tailoring action {m.group(1)} removed it with its base control.' if m else ''


def narrative(row):
    """How KESTREL meets one control, in plain implementation terms, then where the SSP tells it."""
    parts = []
    c, d = row['control'], row['designation']
    if d == 'Removed':
        a = actions.get(c)
        return f"CCSD tailoring action {a['n']} removed it." if a else tailoring_note(row['tailoring'])
    if c in WRITTEN:
        parts.append(WRITTEN[c])
    elif d not in ('Inherited', 'Not applicable', 'Unassigned'):
        parts.append('*Implementation narrative not yet written.*')
    if row['portion'] and not (d == 'Inherited' and c in WRITTEN):
        names = [PROVIDERS[p][0] for p in row['providers']]
        who = names[0] if len(names) == 1 else ', '.join(names[:-1]) + ' and ' + names[-1]
        parts.append(f"**Inherited from {who}:** {sentence(row['portion'])}.")
    if d == 'Not applicable':
        parts.append(row['note'])
    elif d == 'Unassigned':
        parts.append('Nothing in the design implements it yet, and it is tracked as a gap.')
    elif row['gap'] and row['gap'][0] == 'met':
        parts.append('The design meets it, but the SADD does not yet claim it, so it is tracked as a gap.')
    elif row['gap'] and row['gap'][0] == 'narrow':
        parts.append('A system-wide owner is still to be named, and it is tracked as a gap.')
    if row['tailoring']:
        parts.append(tailoring_note(row['tailoring']))
    oids = [o for o in (row['claim'][1] if row['claim'] else []) if o in OUTCOME]
    if oids:
        links = [f"[{o}](../06-ssp/{OUTCOME[o][1]}#{slug(o + ': ' + OUTCOME[o][0])})" for o in oids]
        parts.append('The SSP describes ' + ('it' if len(links) == 1 else 'them') + ' under ' + ', '.join(links) + '.')
    return ' '.join(parts)


# Page
def main():
    counts = Counter(r['designation'] for r in matrix if r['designation'] != 'Removed')
    gaps_met = [r for r in matrix if r['gap'] and r['gap'][0] == 'met']
    gaps_open = [r for r in matrix if r['gap'] and r['gap'][0] == 'open']
    gaps_narrow = [r for r in matrix if r['gap'] and r['gap'][0] == 'narrow']
    in_set = [r for r in matrix if r['designation'] != 'Removed']
    L = []
    L += ['> **Notional system.** KESTREL is fictional. Its control selection uses NIST\'s published baselines as a stand-in, as Control Set explains.', '',
          '# KESTREL Security Controls Traceability Matrix (SCTM)', '',
          '*Generated by `tools/sctm/build.py` from the CCSD, the SADD, and the curated dispositions in `tools/sctm/dispositions.py`. Edit those, not this page.*', '',
          'This matrix carries every control in KESTREL\'s approved set to the SADD outcomes that implement it, the providers it inherits from, and where its evidence is kept. '
          "The same rows are kept as OSCAL in KESTREL's system security plan, [`kestrel-ssp.oscal.json`](../06-ssp/kestrel-ssp.oscal.json), under SCTM Automation via Machine-Readable Format (OSCAL) (`GV-5.9.4`).", '',
          '---', '', '## Document Control', '', '| Field | Value |', '|---|---|',
          '| Program / System Name | KESTREL |', f'| SCTM Version | {VERSION} |', f'| Date | {DATE} |',
          '| Prepared By | KESTREL ISSM, with the PMO ISSE |',
          f"| Source CCSD Version | {SOURCES['CCSD']} |", f"| Source SADD Version | {SOURCES['SADD']} |", f"| Source SIP Version | {SOURCES['SIP']} |",
          '| SSP Validation | Built from the same sources as the SSP, so the two agree by construction. Each submission still checks them against each other. |',
          '| Classification / Handling | CUI |', '', '### Version History', '',
          '| Version | Date | Author | Description of Changes |', '|---|---|---|---|',
          '| 0.1 | 2026-11-25 | KESTREL ISSM | Initial matrix, built against the SADD before SSP validation |',
          f'| 0.2 | {DATE} | KESTREL ISSM | Recast as a checklist by control family, with control names, implementation status from the board, and a narrative per control. The OSCAL moved into the SSP. |',
          f'| 0.3 | {DATE} | KESTREL ISSM | Wrote an implementation narrative for every control KESTREL implements in whole or in part |',
          f'| 0.4 | {DATE} | KESTREL ISSM | Moved the 21 held-but-unclaimed controls to their new SABER v2.0 claims, and recorded MP-6(3) as not applicable |', '',
          '---', '', '## Control Set', '',
          f'The CCSD selects KESTREL\'s controls from the CNSSI 1253 columns for High confidentiality, High integrity, and Moderate availability. '
          f'This notional example does not reproduce those columns. It uses NIST\'s OSCAL [High baseline]({BASE_URL}{HIGH}) and [privacy baseline]({BASE_URL}{PRIVACY}) as a stand-in. '
          f'The CCSD\'s tailoring actions then apply. SI-8 is removed with its enhancements, and SR-11(3) and SA-9(5) are added.', '',
          f'That gives {len(in_set)} controls in the set. The cloud, OT, and IL5 overlays would add rows a real selection carries, and this stand-in omits them.', '',
          '---', '', '## How to Read Each Row', '',
          '- **Control ID** and **Control Name** come from NIST SP 800-53 Rev 5.',
          '- **Designation** is System-Specific when KESTREL implements the whole control, Inherited when a provider does, and Hybrid when both do.',
          "- **Implementation Status** comes from the project board, through the SSP's status snapshot. A control is Planned until its outcomes' work starts reaching Done, Partially implemented once some has, and Implemented when every claiming outcome is done. A Hybrid control's status is KESTREL's own part, since the provider's part is already in place.",
          "- **Narrative** says how KESTREL meets the control, naming the products and where they run, in future tense until the work is built. It then gives any provider's part and any CCSD tailoring. Its last sentence links to the part of the [SSP](../06-ssp/index.md) that tells the whole story, and each linked entry closes with its [Security Implementation Plan](../04-sip/index.md) record.",
          '- **Evidence** for every row is kept in the program evidence repository under `evidence/<family>/<control>/`, under Compliance Evidence Collection and Retention (`CO-1.3`). Nothing is collected yet.', '',
          '---', '', '## Summary', '', '| Designation | Controls |', '|---|---|']
    for d in ['System-Specific', 'Hybrid', 'Inherited', 'Not applicable', 'Unassigned']:
        L.append(f'| {d} | {counts.get(d, 0)} |')
    L += [f'| **Total** | **{len(in_set)}** |', '',
          f'The SADD claims {sum(1 for r in in_set if r["claim"])} of these controls. It also claims {len(beyond)} controls outside the set, listed at the end.', '',
          '---', '', '## Gaps for the SADD\'s Gap Register', '',
          'These rows go to the SADD\'s gap register (Section 9) for disposition.', '',
          f'**Held but unclaimed ({len(gaps_met)}).** An outcome already does this, or is where it belongs, but its mapping does not claim the control. Each needs a claim added to the outcome, or a recorded reason it stays unclaimed.', '',
          ]
    if gaps_met:
        L += ['| Control | Held By | How |', '|---|---|---|']
    for r in gaps_met:
        o, why = MET_UNCLAIMED[r['control']]
        L.append(f"| {r['control']} | {o} | {cell(why)} |")
    if not gaps_met:
        L.append('- None')
    L += ['', f'**No owner ({len(gaps_open)}).** No outcome or provider holds these.', '']
    L += [f"- {r['control']}" for r in gaps_open] or ['- None']
    L += ['', f'**Narrow owners ({len(gaps_narrow)}).** These rest only on narrow outcomes. The SCTM does not read them as system-wide, and each still needs a system-wide owner named.', '']
    L += [f"- {r['control']}: {outcomes(r)}" for r in gaps_narrow] or ['- None']
    L += ['', '---', '', '## Matrix', '']
    for fam in FAMILIES:
        fr = [r for r in matrix if r['control'].startswith(fam + '-')]
        if not fr:
            continue
        L += [f'### {fam}: {FAMILY_NAMES[fam]}', '',
              '| Control ID | Control Name | Designation | Implementation Status | Narrative |', '|---|---|---|---|---|']
        for r in fr:
            L.append(f"| {r['control']} | {cell(TITLES.get(r['control'], ''))} | {r['designation']} | "
                     f"{impl_status(r)} | {cell(narrative(r))} |")
        L.append('')
    L += ['---', '', '## Claimed Beyond the Set', '',
          f'The SADD claims these {len(beyond)} controls, though the set does not select them. They are design choices beyond the baseline, and the SCTM tracks them so a later selection change finds them.', '',
          ', '.join(beyond), '']
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, 'index.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L))
    print(f"SCTM: {len(in_set)} controls, {dict(counts)}; gaps met {len(gaps_met)}, open {len(gaps_open)}, narrow {len(gaps_narrow)}; beyond {len(beyond)}")


if __name__ == '__main__':
    main()
