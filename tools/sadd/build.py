"""Build the KESTREL SADD in docs/03-sadd/ from the SABER framework.

Usage (from the kestrel repo root):
    python tools/sadd/build.py [--framework PATH]

PATH is the SABER repository root, defaulting to ../security-framework.
The script writes:
  - one Section 5 file per focus area, but only once every in-scope outcome
    in that focus area has a hand-written file in tools/sadd/intent/
  - docs/03-sadd/control-coverage.md (Section 7), from every in-scope outcome
  - docs/03-sadd/index.md, from tools/sadd/index.src.md with its generated parts filled in
"""
import argparse, collections, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
ap = argparse.ArgumentParser()
ap.add_argument('--framework', default=os.path.join(os.path.dirname(REPO), 'security-framework'))
args = ap.parse_args()
FW = os.path.join(args.framework, 'framework')
TPL = os.path.join(args.framework, 'templates', 'SADD-TEMPLATE.md')
SYSDESC = os.path.join(REPO, 'docs', '01-system-description.md')
OUT = os.path.join(REPO, 'docs', '03-sadd')
INTENT = os.path.join(HERE, 'intent')

DEPLOY = ['Cloud', 'On-Premises', 'Hybrid', 'Cyber-Physical System (OT/ICS)']

# Footprint values the system description's prose evidences, beyond its component tables.
PROSE = {
    'Cloud Account/Subscription/Tenant Boundary', 'Cloud Workload/Native Platform Identity',
    'Application and Service Account Identity', 'Identity Lifecycle and Governance',
    'External/Federated Trust', 'Third-Party Dependency (Embedded Library/Package)',
    'Base/Pretrained Model',
}
# Footprint values this design introduces.
DESIGN = set()

MANUAL_OUT = {
    'DI-4.1': "Out of scope. KESTREL owns no laptops, desktops, or mobile devices. Performers reach it from their own CMMC Level 2 laptops and the program office from the parent organization's managed devices, and each owner enforces its own devices' compliance.",
    'NE-2.9': 'Out of scope by design. The ground segment conduit carries traffic both ways, namely recordings out (F3) and certified edge models in (F6), so a firewalled conduit with protocol inspection protects it instead of a data diode.',
    'NE-3.6': 'Out of scope. KESTREL runs no email service, and the AO approved removing SI-8 (CCSD tailoring action 1).',
}
PILLAR = {'02': 'Protect', '03': 'Protect', '04': 'Protect', '05': 'Protect', '06': 'Protect', '07': 'Protect',
          '08': 'Operate', '09': 'Operate', '10': 'Operate', '11': 'Manage', '12': 'Manage', '13': 'Manage'}
ACT_FIELDS = ['Control Type', 'Cross-Cutting Discipline', 'Maturity Model', 'ConMon Activity',
              'Level of Effort', 'Cost', 'Time Estimation']


def split_items(title):
    return [x.strip() for x in re.split(r',(?![^(]*\))', title) if x.strip()]


# Parent category -> sub-values, from the SADD template's footprint checklist.
PARENTS = {}
cur = None
for l in open(TPL, encoding='utf-8'):
    m = re.match(r'^- \[ \] \*\*(.+?)\*\*', l)
    if m:
        cur = m.group(1); PARENTS[cur] = []; continue
    m = re.match(r'^\s+- \[ \] (.+?)\s*$', l)
    if m and cur:
        PARENTS[cur].append(m.group(1))
PARENTS = {k: v for k, v in PARENTS.items() if v}
ALLSUB = {s for v in PARENTS.values() for s in v}

# Component-table values, read from the system description.
TABLES = set()
for l in open(SYSDESC, encoding='utf-8'):
    c = [x.strip() for x in l.split('|')]
    # Component tables end with Deployment Type and Affected Components, with or without a Spoke column.
    if len(c) >= 6 and c[-3] and c[-3] != 'Deployment Type' and not c[-3].startswith(':--')             and all(d.strip() in DEPLOY + ['Air-Gapped/Isolated'] for d in c[-3].split(',')):
        TABLES |= set(split_items(c[-2]))
FOOT = TABLES | PROSE | DESIGN
bad = FOOT - ALLSUB
if bad:
    sys.exit(f'Footprint values not in the SABER taxonomy: {sorted(bad)}')


def bullets(lines):
    out = []
    for l in lines:
        m = re.match(r'^- \*\*(.+?):\*\*\s*(.*)$', l)
        if m:
            out.append((m.group(1), m.group(2)))
    return out


def parse(path):
    lines = open(path, encoding='utf-8').read().replace('\r\n', '\n').split('\n')
    fa = None; caps = []; cap = out = act = None; field = None
    for l in lines:
        if l.startswith('# '):
            fa = l[2:].strip(); continue
        if l.startswith('## '):
            cap = {'title': l[3:].strip(), 'outcomes': []}; caps.append(cap)
            out = act = None; field = None; continue
        if l.startswith('### '):
            out = {'title': l[4:].strip(), 'f': {}, 'acts': []}; cap['outcomes'].append(out)
            act = None; field = None; continue
        if l.startswith('#### '):
            act = {'title': l[5:].strip(), 'f': {}}; out['acts'].append(act); field = None; continue
        m = re.match(r'^\*\*([A-Za-z \-/]+):\*\*\s*(.*)$', l)
        if m and (out or act):
            field = m.group(1); tgt = act if act else out
            tgt['f'][field] = [m.group(2)] if m.group(2) else []
            continue
        if field and (out or act) and l.strip():
            (act if act else out)['f'][field].append(l)
    return fa, caps


def scope(o):
    oid = o['title'].split(':')[0]
    if oid in MANUAL_OUT:
        return False, MANUAL_OUT[oid], [], []
    dep = []
    for t, txt in bullets(o['f'].get('Deployment Type', [])):
        if not txt.lower().startswith('omitted'):
            dep += [d for d in split_items(t) if d in DEPLOY]
    dep = [d for d in DEPLOY if d in dep]
    comps = []
    for t, _ in bullets(o['f'].get('Affected Components', [])):
        for c in split_items(t):
            if c in FOOT or (c in PARENTS and any(s in FOOT for s in PARENTS[c])):
                comps.append(c)
    comps = list(dict.fromkeys(comps))
    if not dep:
        return False, 'Out of scope. It applies only to deployment types KESTREL does not field.', dep, comps
    if not comps:
        return False, "Out of scope. None of its affected components are in KESTREL's footprint.", dep, comps
    return True, None, dep, comps


def intent(oid):
    p = os.path.join(INTENT, oid + '.md')
    if not os.path.exists(p):
        return None
    s = open(p, encoding='utf-8').read()
    di = re.search(r'## Design Intent\n(.*?)(?=\n## |\Z)', s, re.S).group(1).strip()
    ed = re.search(r'## External Dependencies\n(.*?)(?=\n## |\Z)', s, re.S).group(1).strip()
    return di, ed


def render(fname, pillar):
    fa, caps = parse(os.path.join(FW, fname))
    st = {'in': 0, 'out': 0, 'acts': 0, 'A': 0, 'V': 0, 'missing': []}
    claims = []; out_rows = []
    body = [f'# {fa}', '',
            f'*KESTREL SADD, Section 5 ({pillar}). See the [index](index.md) for the document-wide sections. '
            'Outcome metadata and activity fields are carried from the SABER unchanged. '
            'Design Intent and External Dependencies are written for KESTREL.*', '']
    for cap in caps:
        ins = []
        for o in cap['outcomes']:
            ok, why, dep, comps = scope(o)
            oid, ot = [x.strip() for x in o['title'].split(':', 1)]
            if ok:
                ins.append((o, oid, ot, dep, comps))
            else:
                st['out'] += 1; out_rows.append((oid, ot, why))
        if not ins:
            continue
        body += [f"## {cap['title']}", '']
        for o, oid, ot, dep, comps in ins:
            st['in'] += 1
            it = intent(oid)
            if it is None:
                st['missing'].append(oid); it = ('`[pending]`', '`[pending]`')
            sec = (o['f'].get('Security Impact') or [''])[0]
            lvl = re.match(r'(High|Moderate|Low)', sec)
            body += [f'### {oid}: {ot}', '', f'**Design Intent:** {it[0]}', '', '**NIST Control Mapping:**', '']
            body += [l for l in o['f'].get('NIST Control Mapping', []) if l.startswith('- ')]
            for t, _ in bullets(o['f'].get('NIST Control Mapping', [])):
                if t == 'Declined':
                    continue
                for c in re.split(r',\s*(?=[A-Z]{2}-)', t):
                    mm = re.match(r'([A-Z]{2}-\d+(?:\(\d+\))?)\s*\((full|partial)\)', c.strip())
                    if mm:
                        claims.append((mm.group(1), mm.group(2), oid, pillar, fa))
            body += ['', f"**Deployment Type:** {', '.join(dep)}", '',
                     f"**Affected Components:** {', '.join(comps)}", '',
                     f'**External Dependencies:** {it[1]}', '',
                     f"**Security Impact:** {lvl.group(1) if lvl else sec}", '', '**Activities:**', '']
            for a in o['acts']:
                st['acts'] += 1
                aid, at = [x.strip() for x in a['title'].split(':', 1)]
                ccd = ' '.join(a['f'].get('Cross-Cutting Discipline', ['']))
                st['A'] += ccd == 'Automate'; st['V'] += ccd == 'Visualize'
                body.append(f'- **{aid}: {at}**')
                body.append(f"    - **Description:** {' '.join(a['f'].get('Description', []))}")
                for f in ACT_FIELDS:
                    body.append(f"    - **{f}:** {' '.join(a['f'].get(f, ['']))}")
                if a['f'].get('Supplemental Guidance'):
                    body.append(f"    - **Supplemental Guidance:** {' '.join(a['f']['Supplemental Guidance'])}")
                body.append('')
    if out_rows:
        body += ['## Scoped Out', '', "These outcomes drop out of KESTREL's design, each for the reason given.", '',
                 '| Outcome | Reason |', '|---|---|']
        body += [f'| {i}: {t} | {w} |' for i, t, w in out_rows]
        body.append('')
    return fa, '\n'.join(body), st, claims


def ctrl_key(k):
    m = re.match(r'([A-Z]{2})-(\d+)(?:\((\d+)\))?', k)
    return (m.group(1), int(m.group(2)), int(m.group(3) or 0))


os.makedirs(OUT, exist_ok=True)
stats = []; allclaims = []
for fname in sorted(os.listdir(FW)):
    m = re.match(r'(0[2-9]|1[0-3])-saber-(.+)\.md$', fname)
    if not m:
        continue
    pillar = PILLAR[m.group(1)]
    fa, text, st, claims = render(fname, pillar)
    outname = f'{m.group(1)}-{m.group(2)}.md'
    written = not st['missing']
    if written:
        open(os.path.join(OUT, outname), 'w', encoding='utf-8', newline='\n').write(text)
    stats.append((pillar, fa, outname, st, written)); allclaims += claims
    print(f"{outname:36} in {st['in']:3} out {st['out']:2} acts {st['acts']:4} "
          f"{'written' if written else 'pending (%d outcomes need intent)' % len(st['missing'])}")

# Section 7
d = collections.defaultdict(lambda: {'fp': set(), 'o': [], 'pf': []})
for cid, fp, oid, pil, fa in allclaims:
    e = d[cid]; e['fp'].add(fp)
    if oid not in e['o']:
        e['o'].append(oid)
    lab = f"{pil} / {fa.split(': ', 1)[1]}"
    if lab not in e['pf']:
        e['pf'].append(lab)
cov = ['# KESTREL SADD: Control Mapping Coverage Summary', '',
       "*KESTREL SADD, Section 7. Generated from the NIST Control Mapping of every outcome in KESTREL's design, "
       'so it changes only when an outcome is scoped in or out.*', '',
       'Each row is one control or enhancement claimed by at least one in-scope outcome. **Full** means at least one '
       'outcome claims the whole control, and **Partial** means the claims are shared slices that together make up the '
       'design intent. The SCTM is built from this table once the SADD is approved.', '',
       '| Control ID | Full / Partial | Owning Outcome(s) | Pillar / Focus Area |', '|---|---|---|---|']
for k in sorted(d, key=ctrl_key):
    e = d[k]
    cov.append(f"| {k} | {'Full' if 'full' in e['fp'] else 'Partial'} | {', '.join(e['o'])} | {', '.join(e['pf'])} |")
open(os.path.join(OUT, 'control-coverage.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(cov) + '\n')

# Index
fp = []
for p, subs in PARENTS.items():
    fp.append(f"- [{'x' if any(s in FOOT for s in subs) else ' '}] **{p}**")
    for s in subs:
        mark = ' ‡' if s in DESIGN else (' †' if s in PROSE and s not in TABLES else '')
        fp.append(f"    - [{'x' if s in FOOT else ' '}] {s}{mark}")
status = ['| Pillar | Focus Area | Outcomes In / Out | Activities | Status |', '|---|---|---|---|---|']
av = ['| Focus Area | Automate Activities | Visualize Activities |', '|---|---|---|']
ta = tv = 0
for pillar, fa, outname, st, written in stats:
    name = f'[{fa}]({outname})' if written else fa
    status.append(f"| {pillar} | {name} | {st['in']} / {st['out']} | {st['acts']} | {'Written' if written else 'Pending'} |")
    av.append(f"| {fa} | {st['A']} | {st['V']} |"); ta += st['A']; tv += st['V']
av.append(f'| **Total** | **{ta}** | **{tv}** |')
src = open(os.path.join(HERE, 'index.src.md'), encoding='utf-8').read()
src = (src.replace('{{FOOTPRINT}}', '\n'.join(fp)).replace('{{STATUS}}', '\n'.join(status))
       .replace('{{AVROWS}}', '\n'.join(av)).replace('{{NCTRL}}', str(len(d))))
if '{{' in src:
    sys.exit('Unfilled placeholder in index.src.md')
open(os.path.join(OUT, 'index.md'), 'w', encoding='utf-8', newline='\n').write(src)
print(f'{len(d)} controls claimed, {ta} Automate and {tv} Visualize activities')
