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
  - docs/05-sctm/kestrel-sctm.oscal.json: the same rows as an OSCAL system security plan

Run from the repository root: python tools/sctm/build.py
"""
import json
import os
import re
import sys
import uuid
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dispositions import PROVIDERS, INHERITED, NOT_APPLICABLE, MET_UNCLAIMED, NARROW  # noqa: E402

VERSION, DATE = '0.1', '2026-11-25'
SOURCES = {'CCSD': '1.0, with 1.1 pending', 'SADD': '0.9', 'SIP': '0.8'}
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


# Page
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
      'The same rows are kept as OSCAL in [`kestrel-sctm.oscal.json`](kestrel-sctm.oscal.json), under SCTM Automation via Machine-Readable Format (OSCAL) (`GV-5.9.4`).', '',
      '---', '', '## Document Control', '', '| Field | Value |', '|---|---|',
      '| Program / System Name | KESTREL |', f'| SCTM Version | {VERSION} |', f'| Date | {DATE} |',
      '| Prepared By | KESTREL ISSM, with the PMO ISSE |',
      f"| Source CCSD Version | {SOURCES['CCSD']} |", f"| Source SADD Version | {SOURCES['SADD']} |", f"| Source SIP Version | {SOURCES['SIP']} |",
      '| SSP Validation | Pending. The SSP is drafted in Phase 1, and the matrix is validated against it before each submission. |',
      '| Classification / Handling | CUI |', '', '### Version History', '',
      '| Version | Date | Author | Description of Changes |', '|---|---|---|---|',
      f'| 0.1 | {DATE} | KESTREL ISSM | Initial matrix, built against the SADD before SSP validation |', '',
      '---', '', '## Control Set', '',
      f'The CCSD selects KESTREL\'s controls from the CNSSI 1253 columns for High confidentiality, High integrity, and Moderate availability. '
      f'This notional example does not reproduce those columns. It uses NIST\'s OSCAL [High baseline]({BASE_URL}{HIGH}) and [privacy baseline]({BASE_URL}{PRIVACY}) as a stand-in. '
      f'The CCSD\'s tailoring actions then apply. SI-8 is removed with its enhancements, and SR-11(3) and SA-9(5) are added.', '',
      f'That gives {len(in_set)} controls in the set. The cloud, OT, and IL5 overlays would add rows a real selection carries, and this stand-in omits them.', '',
      '---', '', '## How to Read Each Row', '',
      '- **Tailoring** names the CCSD action that changed the control, if any.',
      '- **Designation** is System-Specific when KESTREL implements the whole control, Inherited when a provider does, and Hybrid when both do. Not applicable and Unassigned rows are explained in Notes.',
      '- **SADD Outcomes** lists the outcomes that claim the control, and whether their claims are full or partial. Each outcome\'s implementation is its record in the [Security Implementation Plan](../04-sip/index.md) until the SSP states it.',
      '- **Provider** names who covers the inherited portion, validated under Inherited Control Validation (`GV-5.12`).',
      '- **Evidence** for every row is kept in the program evidence repository under `evidence/<family>/<control>/`, under Compliance Evidence Collection and Retention (`CO-1.3`). Nothing is collected yet.', '',
      '---', '', '## Summary', '', '| Designation | Controls |', '|---|---|']
for d in ['System-Specific', 'Hybrid', 'Inherited', 'Not applicable', 'Unassigned']:
    L.append(f'| {d} | {counts.get(d, 0)} |')
L += [f'| **Total** | **{len(in_set)}** |', '',
      f'The SADD claims {sum(1 for r in in_set if r["claim"])} of these controls. It also claims {len(beyond)} controls outside the set, listed at the end.', '',
      '---', '', '## Gaps for the SADD\'s Gap Register', '',
      'These rows go to the SADD\'s gap register (Section 9) for disposition.', '',
      f'**Held but unclaimed ({len(gaps_met)}).** An outcome already does this, or is where it belongs, but its mapping does not claim the control. Each needs a claim added to the outcome, or a recorded reason it stays unclaimed.', '',
      '| Control | Held By | How |', '|---|---|---|']
for r in gaps_met:
    o, why = MET_UNCLAIMED[r['control']]
    L.append(f"| {r['control']} | {o} | {cell(why)} |")
L += ['', f'**No owner ({len(gaps_open)}).** No outcome or provider holds these.', '']
L += [f"- {r['control']}" for r in gaps_open] or ['- None']
L += ['', f'**Narrow owners ({len(gaps_narrow)}).** These rest only on narrow outcomes. The SCTM does not read them as system-wide, and each still needs a system-wide owner named.', '']
L += [f"- {r['control']}: {outcomes(r)}" for r in gaps_narrow] or ['- None']
L += ['', '---', '', '## Matrix', '']
for fam in FAMILIES:
    fr = [r for r in matrix if r['control'].startswith(fam + '-')]
    if not fr:
        continue
    L += [f'### {fam}', '', '| Control | Tailoring | Designation | SADD Outcomes | Provider | Notes |', '|---|---|---|---|---|---|']
    for r in fr:
        note = r['note']
        if r['portion']:
            note = (f"{r['portion']}." + (' ' + note if note else ''))
        L.append(f"| {r['control']} | {r['tailoring']} | {r['designation']} | {outcomes(r)} | {providers(r)} | {cell(note)} |")
    L.append('')
L += ['---', '', '## Claimed Beyond the Set', '',
      f'The SADD claims these {len(beyond)} controls, though the set does not select them. They are design choices beyond the baseline, and the SCTM tracks them so a later selection change finds them.', '',
      ', '.join(beyond), '']
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, 'index.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L))

# OSCAL
LEVEL = {'Low': 'fips-199-low', 'Moderate': 'fips-199-moderate', 'High': 'fips-199-high'}
this = uid('component', 'this-system')
comp = {p: uid('component', p) for p in PROVIDERS}
STATE = {'System-Specific': 'planned', 'Hybrid': 'planned', 'Inherited': 'implemented',
         'Not applicable': 'not-applicable', 'Unassigned': 'planned'}


def prop(name, value):
    return {'name': name, 'ns': NS, 'value': value}


reqs = []
for r in in_set:
    c = r['control']
    by = []
    if r['designation'] != 'Inherited':
        desc = (f"Implemented by {outcomes(r)}, as each outcome's SIP record describes." if r['claim']
                else r['note'] or 'No implementation yet.')
        by.append({'component-uuid': this, 'uuid': uid('by', c, 'this'), 'description': desc,
                   'implementation-status': {'state': STATE[r['designation']]}})
    for p in r['providers']:
        by.append({'component-uuid': comp[p], 'uuid': uid('by', c, p),
                   'description': f"{r['portion']}, under {PROVIDERS[p][1]}. Validated under GV-5.12.",
                   'implementation-status': {'state': 'implemented'}})
    req = {'uuid': uid('req', c), 'control-id': to_oscal(c),
           'props': [prop('designation', r['designation'].lower().replace(' ', '-'))],
           'links': [{'href': f"evidence/{c[:2]}/{c}/", 'rel': 'evidence'}],
           'by-components': by}
    if r['claim']:
        req['props'].append(prop('sadd-outcomes', ' '.join(r['claim'][1])))
        req['props'].append(prop('sadd-claim', r['claim'][0].lower()))
    if r['tailoring']:
        req['props'].append(prop('tailoring', r['tailoring']))
    if r['gap']:
        req['props'].append(prop('gap', r['gap'][0]))
    if r['note']:
        req['remarks'] = r['note']
    reqs.append(req)

info = []
for n, t in sorted(types.items()):
    info.append({'uuid': uid('info', str(n)), 'title': t['title'],
                 'description': f"CCSD information type {n}.",
                 'categorizations': [{'system': 'https://doi.org/10.6028/NIST.SP.800-60v2r1', 'information-type-ids': [t['id']]}],
                 'confidentiality-impact': {'base': LEVEL[t['c']]}, 'integrity-impact': {'base': LEVEL[t['i']]},
                 'availability-impact': {'base': LEVEL[t['a']]}})
ssp = {'system-security-plan': {
    'uuid': uid('ssp', 'kestrel'),
    'metadata': {'title': 'KESTREL Security Controls Traceability Matrix', 'last-modified': f'{DATE}T00:00:00Z',
                 'version': VERSION, 'oscal-version': '1.1.2',
                 'props': [prop('source-ccsd', SOURCES['CCSD']), prop('source-sadd', SOURCES['SADD']), prop('source-sip', SOURCES['SIP'])],
                 'remarks': 'Notional. KESTREL is fictional, and NIST\'s High and privacy baselines stand in for its CNSSI 1253 selection. Generated by tools/sctm/build.py.'},
    'import-profile': {'href': BASE_URL + HIGH},
    'system-characteristics': {
        'system-ids': [{'identifier-type': 'https://ietf.org/rfc/rfc4122', 'id': uid('system', 'kestrel')}],
        'system-name': 'KESTREL',
        'description': 'An unmanned aircraft ISR system with IL5 cloud, on-premises, and fleet segments.',
        'security-sensitivity-level': 'fips-199-high',
        'system-information': {'information-types': info},
        'security-impact-level': {'security-objective-confidentiality': 'fips-199-high',
                                  'security-objective-integrity': 'fips-199-high',
                                  'security-objective-availability': 'fips-199-moderate'},
        'status': {'state': 'under-development'},
        'authorization-boundary': {'description': 'The IL5 cloud hub and spokes, the mission data center, the alternate site, the IT/OT DMZ, and the UAS fleet and ground segment, as the System Description draws them.'}},
    'system-implementation': {
        'users': [{'uuid': uid('user', 'issm'), 'title': 'ISSM', 'description': 'Maintains this matrix.'}],
        'components': [{'uuid': this, 'type': 'this-system', 'title': 'KESTREL',
                        'description': 'KESTREL\'s own implementation, as the SADD and SIP define it.',
                        'status': {'state': 'under-development'}}] +
                      [{'uuid': comp[p], 'type': 'service', 'title': n, 'description': f"Provides {d}.",
                        'status': {'state': 'operational'}} for p, (n, d) in PROVIDERS.items()]},
    'control-implementation': {
        'description': 'Every control in the stand-in set, carried to its SADD outcomes, providers, and evidence location.',
        'implemented-requirements': reqs}}}
json.dump(ssp, open(os.path.join(OUT, 'kestrel-sctm.oscal.json'), 'w', encoding='utf-8', newline='\n'), indent=2)
print(f"SCTM: {len(in_set)} controls, {dict(counts)}; gaps met {len(gaps_met)}, open {len(gaps_open)}, narrow {len(gaps_narrow)}; beyond {len(beyond)}")
