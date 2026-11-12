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
sys.path.insert(0, os.path.dirname(HERE))
import saberlib as S
from saberlib import (REPO, DEPLOY, PROSE, DESIGN, MANUAL_OUT, PILLAR, ACT_FIELDS,
                      split_items, bullets, parse, scope)

ap = argparse.ArgumentParser()
ap.add_argument('--framework', default=os.path.join(os.path.dirname(REPO), 'security-framework'))
args = ap.parse_args()
S.init(args.framework)
FW, PARENTS, TABLES, FOOT = S.FW, S.PARENTS, S.TABLES, S.FOOT
OUT = os.path.join(REPO, 'docs', '03-sadd')
INTENT = os.path.join(HERE, 'intent')


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
