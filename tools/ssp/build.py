"""Build KESTREL's System Security Plan (SSP), as a page and as OSCAL.

Reads:
  - tools/ssp/index.src.md: the hand-written sections, with placeholders for the rest
  - docs/01-system-description.md: Section 2, System Identification
  - docs/02-ccsd.md: Sections 3 and 4, through the SCTM build
  - docs/03-sadd/NN-*.md: each outcome's controls and the capability headings
  - docs/04-sip/NN-*.md: each in-scope outcome's record, phase, and target
  - tools/github/wiki/*.md: each governing plan's trace lines, for Configuration Detail
  - tools/ssp/status.json: the board snapshot, from `python tools/github/issues.py status`
  - tools/ssp/narrative/<ID>.md: what was actually built, once an outcome has work Done
  - tools/sctm/build.py, imported for the control rows and designations

Writes:
  - docs/06-ssp/index.md and one file per focus area
  - docs/06-ssp/kestrel-ssp.oscal.json, KESTREL's one OSCAL system security plan

Run from the repository root: python tools/ssp/build.py
Then validate: python tools/oscal/validate.py tools/oscal/oscal_ssp_schema.json docs/06-ssp/kestrel-ssp.oscal.json
"""
import glob
import importlib.util
import json
import os
import re
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.join(ROOT, 'tools', 'ssp')
OUT = os.path.join(ROOT, 'docs', '06-ssp')
WIKI_SRC = os.path.join(ROOT, 'tools', 'github', 'wiki')
WIKI_URL = 'https://github.com/jessestarkey/Kestrel/wiki'
VERSION, DATE = '0.2', '2026-11-26'
STATUSES = ['Planned', 'Partially Does', 'Currently Does', 'Does Not']


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sctm = load('sctm_build', os.path.join(ROOT, 'tools', 'sctm', 'build.py'))
issues = load('issues', os.path.join(ROOT, 'tools', 'github', 'issues.py'))
SOURCES = sctm.SOURCES
uid, slug = sctm.uid, issues.slug


def ns_prop(name, value):
    return {'name': name, 'ns': sctm.NS, 'value': value}


def shift(block, by=1):
    """Push every markdown heading in a block down by `by` levels."""
    return re.sub(r'^(#+) ', lambda m: '#' * (len(m.group(1)) + by) + ' ', block, flags=re.M)


def md_section(text, heading, level=2):
    """The body under a heading, up to the next heading at the same level or higher."""
    i = text.index(heading + '\n')
    rest = text[i + len(heading) + 1:]
    m = re.search(r'^#{1,%d} ' % level, rest, re.M)
    return rest[:m.start()] if m else rest


# Sources
status = json.load(open(os.path.join(HERE, 'status.json'), encoding='utf-8'))
board = status['status']

sadd, caps, order = {}, {}, []
for path in sorted(glob.glob(os.path.join(ROOT, 'docs', '03-sadd', '[0-9][0-9]-*.md'))):
    text = open(path, encoding='utf-8').read()
    for m in re.finditer(r'^## ([A-Z]{2}-\d+): (.+)$', text, re.M):
        caps[m.group(1)] = m.group(2).strip()
    for blk in re.split(r'\n### ', text)[1:]:
        head, _, body = blk.partition('\n')
        oid, _, title = head.partition(': ')
        mapping = body.split('**NIST Control Mapping:**', 1)
        ctrls = []
        if len(mapping) == 2:
            for line in mapping[1].split('\n\n**', 1)[0].splitlines():
                m = re.match(r'- \*\*([A-Z]{2}-\d+(?:\(\d+\))?) \(', line)
                if m:
                    ctrls.append(m.group(1))
        sadd[oid.strip()] = {'title': title.strip(), 'controls': ctrls}

sip, chapters = OrderedDict(), OrderedDict()
for path in sorted(glob.glob(os.path.join(ROOT, 'docs', '04-sip', '[0-9][0-9]-*.md'))):
    name = os.path.basename(path)
    recs = issues.sip_records(path)
    text = open(path, encoding='utf-8').read()
    fa = re.search(r'^# ([A-Z]{2}): (.+)$', text, re.M)
    chapters[name] = {'code': fa.group(1), 'title': fa.group(2).strip(), 'outcomes': []}
    for oid, r in recs.items():
        if not re.fullmatch(r'[A-Z]{2}-\d+\.\d+', oid):
            continue
        r['file'] = name
        sip[oid] = r
        chapters[name]['outcomes'].append(oid)

# Plan sections, from each wiki page's trace lines
plans = {}
for path in sorted(glob.glob(os.path.join(WIKI_SRC, '*.md'))):
    page = os.path.basename(path)[:-3]
    if page in ('Home', '_Sidebar') or page.startswith('SIA-'):
        continue
    text = open(path, encoding='utf-8').read()
    h1 = re.search(r'^# KESTREL (.+)$', text, re.M)
    if not h1:
        continue
    title = h1.group(1).strip()
    short = re.search(r'\(([A-Za-z/]+)\)$', title)
    short = short.group(1) if short else title
    heading = None
    for line in text.splitlines():
        if line.startswith('## '):
            heading = line[3:].strip()
            continue
        ids = []
        if line.startswith('*Traces to '):
            ids = re.findall(r'[A-Z]{2}-\d+(?:\.\d+)*', line)
        elif heading and heading.startswith('Appendix'):
            ids = re.findall(r'\*\(([A-Z]{2}-\d+\.\d+\.\d+)', line)
        for i in ids:
            label = 'its appendix' if heading.startswith('Appendix') else 'Section ' + heading.split('.')[0]
            plans.setdefault(i, []).append((short, title, page, heading, label))


def config_detail(oid):
    """Where an outcome's specifics live, as a fragment for the citation line."""
    seen, out = set(), []
    hits = [h for i, hs in plans.items() if i == oid or i.startswith(oid + '.') for h in hs]
    if oid in issues.WIKI:
        # An outcome whose own work is the page, such as a plan, is "published as" it. An outcome
        # that is one section of a compendium already gets its section links below instead.
        t, page = issues.WIKI[oid]
        if not any(h[2] == page for h in hits):
            out.append(f'Published as the [{t}]({WIKI_URL}/{page}).')
    by_plan = OrderedDict()
    for short, title, page, heading, label in hits:
        key = (short, page, heading)
        if key in seen:
            continue
        seen.add(key)
        by_plan.setdefault((short, page), []).append(f'[{label}]({WIKI_URL}/{page}#{slug(heading)})')
    parts = [f"the {s}, {' and '.join(ls)}" for (s, _), ls in by_plan.items()]
    if parts:
        out.append('Details: ' + (parts[0] if len(parts) == 1 else '; '.join(parts[:-1]) + '; and ' + parts[-1]) + '.')
    return ' '.join(out)


def outcome_status(oid, rec):
    narrative = os.path.join(HERE, 'narrative', f'{oid}.md')
    text = open(narrative, encoding='utf-8').read().strip() if os.path.exists(narrative) else ''
    override = re.match(r'\*\*Status:\*\* (.+)\n+', text)
    if override:
        text = text[override.end():].strip()
    acts = [a for a, r in rec['rows'].items() if r['phase']]
    done = [a for a in acts if board.get(a) == 'Done']
    if override:
        st = override.group(1).strip()
    elif board.get(oid) == 'Done':
        st = 'Currently Does'
    elif done:
        st = 'Partially Does'
    else:
        st = 'Planned'
    return st, text, done


def planned_text(oid, rec, st, done):
    f = rec['fields']
    rollout = f.get('Rollout Phase', '')
    phase = rollout.split(',')[0]
    last = re.search(r'with work through (Phase \d)', rollout)
    when = f'from {phase}, running through {last.group(1)}' if last else f'in {phase}'
    target = f.get('Target Date / Sprint', '')
    if st == 'Planned':
        return (f'*This narrative is not yet written. The Security Implementation Plan schedules the outcome {when}, '
                f'with a target of {target}.*')
    return (f"*This narrative is not yet written. Done so far: {', '.join(done)}. "
            f'The rest is scheduled in the Security Implementation Plan, with a target of {target}.*')


def capability_opening(cap):
    path = os.path.join(HERE, 'narrative', f'{cap}.md')
    return open(path, encoding='utf-8').read().strip() if os.path.exists(path) else ''


# Section 6, one file per focus area
results = {}
fa_rows = []
for name, ch in chapters.items():
    L = [f"# {ch['code']}: {ch['title']}", '',
         '*Generated by `tools/ssp/build.py`. Edit its sources, not this page.*', '']
    cap = None
    counts = Counter()
    for oid in ch['outcomes']:
        rec = sip[oid]
        c = oid.split('.')[0]
        if c != cap:
            cap = c
            L += [f'## {c}: {caps.get(c, "")}', '']
            opening = capability_opening(c)
            if opening:
                L += [opening, '']
        st, text, done = outcome_status(oid, rec)
        counts[st] += 1
        results[oid] = st
        title = sadd.get(oid, {}).get('title') or rec['title'].partition(': ')[2]
        ctrls = sadd.get(oid, {}).get('controls', [])
        L += [f'### {oid}: {title}', '', text or planned_text(oid, rec, st, done), '']
        cite = [f'**{st}.**',
                f"Controls: {', '.join(ctrls)}." if ctrls else 'Controls: none, as the SADD declines a mapping.',
                f"SIP record: [{oid}](../04-sip/{name}#{slug(rec['title'])}).",
                config_detail(oid)]
        L += ['<sub>' + ' '.join(x for x in cite if x) + '</sub>', '']
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(L))
    fa_rows.append(f"| [{ch['code']}: {ch['title']}]({name}) | {len(ch['outcomes'])} | "
                   + ' | '.join(str(counts.get(s, 0)) for s in STATUSES) + ' |')
total = Counter(results.values())
fa_rows.append(f'| **Total** | **{len(results)}** | ' + ' | '.join(f'**{total.get(s, 0)}**' for s in STATUSES) + ' |')

# Section 2, from the System Description
sysdesc = open(os.path.join(ROOT, 'docs', '01-system-description.md'), encoding='utf-8').read()
S2 = ['## 2. System Identification', '',
      '*Carried from the [System Description](../01-system-description.md), which stays the source until this plan reaches version 1.0.*', '',
      '### Authorization Boundary', '', md_section(sysdesc, '## Authorization Boundary').strip(), '',
      '### Inherited Services', '',
      'The SCTM records inheritance control by control, and Inherited Control Validation (`GV-5.12`) confirms each provider still delivers it.', '',
      '| Provider | What KESTREL Inherits | Basis |', '|---|---|---|']
for p, (n, d) in sctm.PROVIDERS.items():
    fams = sorted({k for k, (ps, _) in sctm.INHERITED.items() if p in ps})
    S2.append(f"| {n[0].upper() + n[1:]} | {', '.join(fams)} | {d[0].upper() + d[1:]} |")
S2 += ['', '### Component Inventory', '', shift(md_section(sysdesc, '## Components').strip(), 1), '',
       '### Operational Context', '', shift(md_section(sysdesc, '## Mission and Purpose').strip()), '',
       '#### Teams', '', shift(md_section(sysdesc, '## Teams').strip(), 1), '',
       '### Data Flows', '', md_section(sysdesc, '## Data Flows').strip(), '',
       '### Users and Roles', '', shift(md_section(sysdesc, '## Users and Roles').strip(), 1), '',
       '### Interconnections and External Dependencies', '', md_section(sysdesc, '## Interconnections and External Dependencies').strip(), '',
       '### Assumptions and Exclusions', '', md_section(sysdesc, '## Assumptions and Exclusions').strip(), '',
       '### Security Role Holders', '',
       'This notional example names roles rather than people. A real SSP names each holder and how to reach them.', '',
       '| Role | Holder |', '|---|---|',
       '| Authorizing Official (AO) | The KESTREL AO |',
       "| ISSM | The performer's ISSM, under an appointment letter |",
       "| ISSOs | The Security Team's ISSOs |",
       '| System Owner | The KESTREL program manager |',
       "| PMO ISSE | The program office's ISSE |",
       '| Security Control Assessor | The SCA the AO designates |']

# Sections 3 and 4, from the CCSD
ccsd = sctm.ccsd
cat = md_section(ccsd, '## 4. System-Level Categorization (carried in)')
levels = {r[0]: sctm.unbold(r[1]) for r in sctm.rows(cat)}
concur = re.search(r'\*\*AO concurrence:\*\* (.+)', cat).group(1).strip()
rationale = [p for p in cat.split('\n\n') if p.strip() and not p.lstrip().startswith(('>', '|', '**'))]
S3 = ['## 3. Information Types and Categorization', '',
      '*Carried from the [CCSD](../02-ccsd.md), Sections 2 to 4. Security Categorization (`GV-5.5`) changes these, never this page.*', '',
      '| # | Information Type | Confidentiality | Integrity | Availability |', '|---|---|---|---|---|']
S3 += [f"| {n} | {t['title']} | {t['c']} | {t['i']} | {t['a']} |" for n, t in sorted(sctm.types.items())]
S3 += ['', '**System-level impact:**', '',
       '| Confidentiality | Integrity | Availability |', '|---|---|---|',
       f"| {levels['Confidentiality']} | {levels['Integrity']} | {levels['Availability']} |", '',
       '**Categorization rationale:** ' + ' '.join(p.strip() for p in rationale), '',
       f'**AO concurrence on categorization:** {concur}']
base = md_section(ccsd, '## 5. Baseline Selection').strip()
over = md_section(ccsd, '## 6. Overlays and Cloud Impact-Level Requirements').strip()
S4 = ['## 4. Baseline and Overlays in Force', '',
      '*Carried from the [CCSD](../02-ccsd.md), Sections 5 to 7. Nothing is re-tailored here.*', '',
      '### Baseline', '', shift(base, 2), '', '### Overlays and Cloud Requirements', '', shift(over, 2), '',
      '### Tailoring Actions', '',
      '| Action | Control | Change | AO Decision |', '|---|---|---|---|']
for c, a in sorted(sctm.actions.items(), key=lambda kv: kv[1]['n']):
    S4.append(f"| {a['n']} | {c} | {a['action']} | {sctm.cell(a['decision'])} |")
in_set = [r for r in sctm.matrix if r['designation'] != 'Removed']
S4 += ['', f"The [SCTM](../05-sctm/index.md) carries the resulting {len(in_set)} controls, "
       "with each one's System-Specific, Hybrid, or Inherited designation."]

summary = (f"{len(results)} in-scope outcomes: " + ', '.join(f'{total.get(s, 0)} {s.lower()}' for s in STATUSES if total.get(s, 0))
           + f". The board snapshot was taken on {status['taken']}.")
page = open(os.path.join(HERE, 'index.src.md'), encoding='utf-8').read()
for k, v in {'VERSION': VERSION, 'DATE': DATE, 'CCSD': SOURCES['CCSD'], 'SADD': SOURCES['SADD'], 'SIP': SOURCES['SIP'],
             'SNAPSHOT': f"{status['taken']}, from the project board", 'STATUS_SUMMARY': summary,
             'SECTION2': '\n'.join(S2), 'SECTION3': '\n'.join(S3), 'SECTION4': '\n'.join(S4),
             'FA_TABLE': '\n'.join(fa_rows), 'AO_CONCURRENCE': concur}.items():
    page = page.replace('{{' + k + '}}', v)
assert '{{' not in page, re.findall(r'\{\{\w+\}\}', page)
open(os.path.join(OUT, 'index.md'), 'w', encoding='utf-8', newline='\n').write(page)

# OSCAL: one system security plan, carrying the SCTM's rows and each outcome's status
LEVEL = {'Low': 'fips-199-low', 'Moderate': 'fips-199-moderate', 'High': 'fips-199-high'}
STATE = {'Planned': 'planned', 'Partially Does': 'partial', 'Currently Does': 'implemented', 'Does Not': 'planned'}
this = uid('component', 'this-system')
comp = {p: uid('component', p) for p in sctm.PROVIDERS}


def control_state(oids):
    sts = [results.get(o, 'Planned') for o in oids]
    if sts and all(s == 'Currently Does' for s in sts):
        return 'implemented'
    if any(s in ('Currently Does', 'Partially Does') for s in sts):
        return 'partial'
    return 'planned'


reqs = []
for r in in_set:
    c = r['control']
    by = []
    if r['designation'] == 'Not applicable':
        by.append({'component-uuid': this, 'uuid': uid('by', c, 'this'), 'description': r['note'],
                   'implementation-status': {'state': 'not-applicable'}})
    elif r['designation'] != 'Inherited':
        if r['claim']:
            oids = r['claim'][1]
            desc = ('Implemented through ' + ', '.join(f"{o} ({results.get(o, 'not in scope')})" for o in oids)
                    + ". Each outcome's entry in the SSP states what is built.")
            state = control_state(oids)
        else:
            desc, state = r['note'] or 'No implementation yet.', 'planned'
        by.append({'component-uuid': this, 'uuid': uid('by', c, 'this'), 'description': desc,
                   'implementation-status': {'state': state}})
    for p in r['providers']:
        by.append({'component-uuid': comp[p], 'uuid': uid('by', c, p),
                   'description': f"{r['portion']}, under {sctm.PROVIDERS[p][1]}. Validated under GV-5.12.",
                   'implementation-status': {'state': 'implemented'}})
    req = {'uuid': uid('req', c), 'control-id': sctm.to_oscal(c),
           'props': [ns_prop('designation', r['designation'].lower().replace(' ', '-'))],
           'links': [{'href': f"evidence/{c[:2]}/{c}/", 'rel': 'evidence'}],
           'by-components': by}
    if r['claim']:
        req['props'].append(ns_prop('sadd-outcomes', ' '.join(r['claim'][1])))
        req['props'].append(ns_prop('sadd-claim', r['claim'][0].lower()))
    if r['tailoring']:
        req['props'].append(ns_prop('tailoring', r['tailoring']))
    if r['gap']:
        req['props'].append(ns_prop('gap', r['gap'][0]))
    if r['note']:
        req['remarks'] = r['note']
    reqs.append(req)

info = [{'uuid': uid('info', str(n)), 'title': t['title'], 'description': f'CCSD information type {n}.',
         'categorizations': [{'system': 'https://doi.org/10.6028/NIST.SP.800-60v2r1', 'information-type-ids': [t['id']]}],
         'confidentiality-impact': {'base': LEVEL[t['c']]}, 'integrity-impact': {'base': LEVEL[t['i']]},
         'availability-impact': {'base': LEVEL[t['a']]}} for n, t in sorted(sctm.types.items())]


def table(block):
    return [r for r in sctm.rows(block) if r and not r[0].startswith(':')]


components = [{'uuid': this, 'type': 'this-system', 'title': 'KESTREL',
               'description': "KESTREL's own implementation, as the SADD designs it and the SSP records it.",
               'status': {'state': 'under-development'}}]
components += [{'uuid': comp[p], 'type': 'service', 'title': n, 'description': f'Provides {d}.',
                'status': {'state': 'operational'}} for p, (n, d) in sctm.PROVIDERS.items()]
for r in table(md_section(sysdesc, '## Components')):
    if len(r) >= 4:
        components.append({'uuid': uid('component', r[0]), 'type': 'service', 'title': r[0], 'description': r[1],
                           'props': [ns_prop('deployment-type', r[2])], 'status': {'state': 'under-development'}})
for r in table(md_section(sysdesc, '## Interconnections and External Dependencies')):
    components.append({'uuid': uid('interconnection', r[0]), 'type': 'interconnection', 'title': r[0],
                       'description': f'Connects to {r[1][0].lower() + r[1][1:]}. Basis: {r[2]}', 'status': {'state': 'under-development'}})
users = [{'uuid': uid('user', r[0]), 'title': r[0], 'description': r[1]}
         for r in table(md_section(sysdesc, '### People', level=3))]
boundary = md_section(sysdesc, '## Authorization Boundary').strip().split('\n\n')[0]

ssp = {'system-security-plan': {
    'uuid': uid('ssp', 'kestrel'),
    'metadata': {'title': 'KESTREL System Security Plan', 'last-modified': f'{DATE}T00:00:00Z',
                 'version': VERSION, 'oscal-version': '1.1.2',
                 'props': [ns_prop('source-ccsd', SOURCES['CCSD']), ns_prop('source-sadd', SOURCES['SADD']),
                           ns_prop('source-sip', SOURCES['SIP']), ns_prop('board-snapshot', status['taken'])],
                 'remarks': "Notional. KESTREL is fictional, and NIST's High and privacy baselines stand in for its CNSSI 1253 selection. Generated by tools/ssp/build.py."},
    'import-profile': {'href': sctm.BASE_URL + sctm.HIGH},
    'system-characteristics': {
        'system-ids': [{'identifier-type': 'https://ietf.org/rfc/rfc4122', 'id': uid('system', 'kestrel')}],
        'system-name': 'KESTREL',
        'description': 'An unmanned aircraft ISR system with IL5 cloud, on-premises, and fleet segments.',
        'security-sensitivity-level': LEVEL[max(levels.values(), key=['Low', 'Moderate', 'High'].index)],
        'system-information': {'information-types': info},
        'security-impact-level': {'security-objective-confidentiality': LEVEL[levels['Confidentiality']],
                                  'security-objective-integrity': LEVEL[levels['Integrity']],
                                  'security-objective-availability': LEVEL[levels['Availability']]},
        'status': {'state': 'under-development'},
        'authorization-boundary': {'description': boundary}},
    'system-implementation': {'users': users, 'components': components},
    'control-implementation': {
        'description': 'Every control in the stand-in set, carried to its SADD outcomes and their status, its providers, and its evidence location.',
        'implemented-requirements': reqs}}}
json.dump(ssp, open(os.path.join(OUT, 'kestrel-ssp.oscal.json'), 'w', encoding='utf-8', newline='\n'), indent=2)
print(f"SSP: {len(results)} outcomes {dict(total)}; {len(reqs)} controls; {len(components)} components; {len(users)} user roles; "
      f"{sum(1 for o in results if config_detail(o))} outcomes with plan pointers")
