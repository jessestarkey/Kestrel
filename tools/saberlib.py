"""Shared SABER parsing and KESTREL scoping for the SADD and SIP builds.

Both builds call init() with the SABER repository root, then use parse() and
scope() so every document scopes outcomes the same way.
"""
import os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYSDESC = os.path.join(REPO, 'docs', '01-system-description.md')
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


FW = TPL = None
PARENTS = {}; ALLSUB = set(); TABLES = set(); FOOT = set()


def init(framework_root):
    """Point the module at a SABER checkout and compute KESTREL's footprint."""
    global FW, TPL, PARENTS, ALLSUB, TABLES, FOOT
    FW = os.path.join(framework_root, 'framework')
    TPL = os.path.join(framework_root, 'templates', 'SADD-TEMPLATE.md')
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
        if len(c) >= 6 and c[-3] and c[-3] != 'Deployment Type' and not c[-3].startswith(':--') \
                and all(d.strip() in DEPLOY + ['Air-Gapped/Isolated'] for d in c[-3].split(',')):
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


