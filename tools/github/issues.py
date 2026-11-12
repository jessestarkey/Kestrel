"""Load one focus area of the KESTREL Security Implementation Plan into GitHub.

The repository's Issues stand in for a self-hosted Jira, and a GitHub Project
stands in for its board. The hierarchy follows the plan's Section 5:
focus area -> initiative, capability -> epic, outcome -> story,
activity -> sub-task, joined as GitHub sub-issues.

Usage (from the kestrel repo root):
    python tools/github/issues.py plan  ID    # write the local plan, create nothing
    python tools/github/issues.py apply ID    # create what the state file lacks

`plan` writes tools/github/out/<code>-plan.json and prints a summary.
`apply` creates labels, milestones, issues, sub-issue links, and project items,
recording each in tools/github/state/<code>.json so a re-run never duplicates.
"""
import json, os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))
import saberlib as S

OWNER, NAME = 'jessestarkey', 'Kestrel'
GH = r'C:\Program Files\GitHub CLI\gh.exe' if os.name == 'nt' else 'gh'
BLOB = f'https://github.com/{OWNER}/{NAME}/blob/main'
FRAMEWORK = os.path.join(os.path.dirname(REPO_ROOT), 'security-framework')
FILES = {'ID': ('02', 'identity'), 'DI': ('03', 'device-and-infrastructure'), 'NE': ('04', 'network-and-environment'),
         'AP': ('05', 'application'), 'AI': ('06', 'artificial-intelligence'), 'DA': ('07', 'data'),
         'DE': ('08', 'detection'), 'RS': ('09', 'response'), 'RC': ('10', 'recovery'),
         'GV': ('11', 'governance'), 'RK': ('12', 'risk'), 'CO': ('13', 'compliance')}
# Target dates for sub-tasks. Phase 3 work is due two months before the ATO decision, for SCA assessment.
TARGET = {1: '2027-06-30', 2: '2027-12-31', 3: '2028-04-30', 4: '2028-12-31'}
PHASE_START = {1: '2027-01-01', 2: '2027-07-01', 3: '2028-01-01', 4: '2028-07-01'}
PHASES = {1: ('Phase 1: Foundation', '2027-06-30'), 2: ('Phase 2: Protect and Operate', '2027-12-31'),
          3: ('Phase 3: Mission, AI, and Fleet', '2028-06-30'), 4: ('Phase 4: Maturity', '2028-12-31')}
def note(kind):
    return (f'> **Notional system.** KESTREL is fictional. This issue stands in for {kind} in a self-hosted Jira, '
            'generated from the Security Implementation Plan.')
# Stories whose work lives in a wiki page, the stand-in for Confluence.
WIKI = {'ID-4.6': ('Break-Glass Account Retrieval runbook', 'Break-Glass-Account-Retrieval'),
        'ID-5.1': ('Account Management Plan', 'Account-Management-Plan')}
TYPE_LABELS = {'initiative': ('type: initiative', '5319e7'), 'epic': ('type: epic', '1d76db'),
               'story': ('type: story', '0e8a16'), 'sub-task': ('type: sub-task', 'c5def5')}


def slug(heading):
    s = heading.strip().lower()
    s = re.sub(r'[^\w\- ]', '', s)
    return s.replace(' ', '-')


def narrative(text, start_pat, stop_pat):
    """Return the prose between a heading and the next heading of interest."""
    m = re.search(start_pat, text, re.M)
    if not m:
        return ''
    rest = text[m.end():]
    n = re.search(stop_pat, rest, re.M)
    body = rest[:n.start()] if n else rest
    paras = [p.strip() for p in body.strip().split('\n\n') if p.strip() and not p.lstrip().startswith(('```', '%%', '|'))]
    return '\n\n'.join(paras)


def sip_records(path):
    """Parse the plan's records: outcome ID -> fields and activity rows."""
    text = open(path, encoding='utf-8').read()
    recs = {}
    for blk in re.split(r'\n### ', text)[1:]:
        head, _, rest = blk.partition('\n')
        oid = head.split(':')[0].strip()
        f = dict(re.findall(r'^\*\*([^*]+):\*\* (.*)$', rest, re.M))
        rows = {}
        for line in rest.splitlines():
            m = re.match(r'^\| ([A-Z]{2}-[\d.]+): [^|]+ \| (\d|N/A)( \(pinned\))? \| (.+) \|$', line)
            if m:
                cells = [c.strip().replace(' (re-rated)', '') for c in m.group(4).split(' | ')]
                rows[m.group(1)] = {'phase': None if m.group(2) == 'N/A' else int(m.group(2)),
                                    'pinned': bool(m.group(3)), 'cells': cells}
        pin = re.search(r'^\*\*Pinned:\*\* (.*)$', rest, re.M)
        na = re.search(r'^\*\*Not applicable:\*\* (.*)$', rest, re.M)
        na = dict(re.findall(r'([A-Z]{2}-[\d.]+): (.*?)(?= [A-Z]{2}-[\d.]+: |$)', na.group(1))) if na else {}
        recs[oid] = {'title': head, 'fields': f, 'rows': rows, 'pinned': pin.group(1) if pin else '', 'na': na}
    return recs


COLS = ['Control Type', 'Cross-Cutting Discipline', 'Maturity Model', 'ConMon Activity',
        'Level of Effort', 'Cost', 'Time Estimation']


def build_plan(code):
    num, name = FILES[code]
    S.init(FRAMEWORK)
    fw_path = os.path.join(S.FW, f'{num}-saber-{name}.md')
    fw_text = open(fw_path, encoding='utf-8').read()
    fa, caps = S.parse(fw_path)
    sip_file = f'docs/04-sip/{num}-{name}.md'
    sadd_file = f'docs/03-sadd/{num}-{name}.md'
    recs = sip_records(os.path.join(REPO_ROOT, sip_file))
    issues = []
    fa_intro = narrative(fw_text, r'^# ' + re.escape(fa) + r'\s*$', r'^## ')
    init_key = code
    issues.append({'key': init_key, 'type': 'initiative', 'parent': None, 'phase': None,
                   'title': f'{fa}',
                   'body': f"{note('an initiative')}\n\n{fa_intro}"
                           f'\n\n**SADD:** [{sadd_file}]({BLOB}/{sadd_file})  \n'
                           f'**Security Implementation Plan:** [{sip_file}]({BLOB}/{sip_file})\n'})
    for cap in caps:
        cid = cap['title'].split(':')[0].strip()
        ins = [o for o in cap['outcomes'] if o['title'].split(':')[0].strip() in recs]
        if not ins:
            continue
        cap_intro = narrative(fw_text, r'^## ' + re.escape(cap['title']) + r'\s*$', r'^###? ')
        cap_phase = min(min(r['phase'] for r in recs[o['title'].split(':')[0].strip()]['rows'].values() if r['phase']) for o in ins)
        issues.append({'key': cid, 'type': 'epic', 'parent': init_key, 'phase': cap_phase, 'title': cap['title'],
                       'body': f"{note('an epic')}\n\n{cap_intro}"
                               f'\n\n**Stories:** {len(ins)}, one per in-scope SADD outcome.\n'})
        for o in ins:
            oid, ot = [x.strip() for x in o['title'].split(':', 1)]
            r = recs[oid]; f = r['fields']
            phase = min(x['phase'] for x in r['rows'].values() if x['phase'])
            lines = [note('a story'), '',
                     f"**SADD outcome:** [{oid}: {ot}]({BLOB}/{sadd_file}#{slug(o['title'])}), which holds the design intent and control mapping.  ",
                     f"**Plan record:** [{oid}]({BLOB}/{sip_file}#{slug(o['title'])})", '',
                     '| Field | Value |', '|---|---|']
            for k in ['Selected Tool / Product / Service', 'Environment-Specific Tailoring', 'Accountable Team',
                      'Dependencies', 'Funding Line', 'Rollout Phase', 'Target Date / Sprint',
                      'Contracting / Procurement Reference']:
                v = f.get(k, '').replace('](index.md', f']({BLOB}/docs/04-sip/index.md')
                lines.append(f'| {k} | {v} |')
            if oid in WIKI:
                t, page = WIKI[oid]
                lines += ['', f'**Wiki:** [{t}](https://github.com/{OWNER}/{NAME}/wiki/{page})']
            lines += ['', '**Done when** every sub-task is closed and the SSP records what was built against this outcome.']
            if r['pinned']:
                lines += ['', f"**Pinned activities:** {r['pinned']}"]
            issues.append({'key': oid, 'type': 'story', 'parent': cid, 'phase': phase,
                           'deps': re.findall(r'\b([A-Z]{2}-\d+(?:\.\d+)?)\b', f.get('Dependencies', '')),
                           'title': f'{oid}: {ot}', 'body': '\n'.join(lines) + '\n',
                           'fields': {'Outcome ID': oid, 'Team': f.get('Accountable Team', ''),
                                      'Target Date': f.get('Target Date / Sprint', '')}})
            for a in o['acts']:
                aid, at = [x.strip() for x in a['title'].split(':', 1)]
                row = r['rows'][aid]
                meta = dict(zip(COLS, row['cells']))
                desc = ' '.join(a['f'].get('Description', []))
                guide = ' '.join(a['f'].get('Supplemental Guidance', []))
                body = [note('a sub-task'), '', desc]
                if guide:
                    body += ['', f'**Supplemental Guidance:** {guide}']
                if row['phase'] is None:
                    phase_line = f"**Not applicable:** {r['na'].get(aid, 'Does not apply to KESTREL.')} Closed as not planned."
                else:
                    phase_line = f"**Phase:** {PHASES[row['phase']][0]}{' (pinned, see the parent story)' if row['pinned'] else ''}"
                body += ['', phase_line, '', '| Field | Value |', '|---|---|'] + [f'| {k} | {v} |' for k, v in meta.items()]
                fields = {'Outcome ID': oid, **meta}
                if row['phase']:
                    fields['Target Date'] = TARGET[row['phase']]
                issues.append({'key': aid, 'type': 'sub-task', 'parent': oid, 'phase': row['phase'],
                               'state': 'open' if row['phase'] else 'closed',
                               'title': f'{aid}: {at}', 'body': '\n'.join(body) + '\n', 'fields': fields})
    # Start dates for the roadmap view, and spans for the epics and the initiative.
    for it in issues:
        if it['phase']:
            it.setdefault('fields', {})['Start Date'] = PHASE_START[it['phase']]
    for it in issues:
        if it['type'] in ('epic', 'initiative'):
            kids = [k for k in issues if k['parent'] == it['key']] if it['type'] == 'epic' else \
                   [k for k in issues if k['type'] == 'story']
            f = it.setdefault('fields', {})
            f['Start Date'] = min(k['fields']['Start Date'] for k in kids if 'Start Date' in k['fields'])
            f['Target Date'] = max(k['fields']['Target Date'] for k in kids if 'Target Date' in k['fields'])
    return issues


# ---------- GitHub calls ----------

def gh(*args, input=None, ok_fail=False):
    for attempt in range(6):
        p = subprocess.run([GH, *args], input=input, capture_output=True, text=True, encoding='utf-8')
        if p.returncode == 0:
            return p.stdout
        err = p.stderr
        if ok_fail:
            return None
        if 'rate limit' in err.lower() or 'abuse' in err.lower() or 'HTTP 403' in err or 'HTTP 429' in err:
            wait = 60 * (attempt + 1)
            print(f'  rate limited, waiting {wait}s'); time.sleep(wait); continue
        if 'Something went wrong' in err or 'HTTP 502' in err or 'HTTP 503' in err or 'HTTP 504' in err:
            wait = 10 * (attempt + 1)
            print(f'  GitHub server error, retrying in {wait}s'); time.sleep(wait); continue
        raise RuntimeError(f"gh {' '.join(args[:3])} failed: {err.strip()}")
    raise RuntimeError('gave up after repeated rate limits')


def api(method, path, fields=None):
    args = ['api', '-X', method, path, '-H', 'Accept: application/vnd.github+json']
    body = json.dumps(fields) if fields is not None else None
    if body:
        args += ['--input', '-']
    return json.loads(gh(*args, input=body) or 'null')


def graphql(query, **vars):
    payload = json.dumps({'query': query, 'variables': vars})
    out = json.loads(gh('api', 'graphql', '--input', '-', input=payload))
    if out.get('errors'):
        raise RuntimeError(out['errors'])
    return out['data']


def apply(code, issues):
    state_path = os.path.join(HERE, 'state', f'{code}.json')
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    st = json.load(open(state_path)) if os.path.exists(state_path) else {'issues': {}, 'links': [], 'items': {}, 'fields_set': []}

    def save():
        json.dump(st, open(state_path, 'w'), indent=1)

    repo = f'/repos/{OWNER}/{NAME}'
    # Labels
    have = {l['name'] for l in api('GET', f'{repo}/labels?per_page=100')}
    want = [v for v in TYPE_LABELS.values()] + [(f'phase: {p}', 'fbca04') for p in PHASES] + [(f'focus area: {code}', 'bfd4f2'), ('notional', 'ededed')]
    for n, c in want:
        if n not in have:
            api('POST', f'{repo}/labels', {'name': n, 'color': c})
    # Milestones
    ms = {m['title']: m['number'] for m in api('GET', f'{repo}/milestones?state=all&per_page=100')}
    for p, (t, due) in PHASES.items():
        if t not in ms:
            ms[t] = api('POST', f'{repo}/milestones', {'title': t, 'due_on': f'{due}T23:59:59Z',
                                                       'description': 'Rollout phase from the KESTREL Security Implementation Plan. Stands in for a Jira fix version.'})['number']
    # Issues
    for i, it in enumerate(issues):
        if it['key'] in st['issues']:
            continue
        labels = [TYPE_LABELS[it['type']][0], f'focus area: {code}', 'notional'] + ([f"phase: {it['phase']}"] if it['phase'] else [])
        data = {'title': it['title'], 'body': it['body'], 'labels': labels}
        if it['phase']:
            data['milestone'] = ms[PHASES[it['phase']][0]]
        made = api('POST', f'{repo}/issues', data)
        st['issues'][it['key']] = {'number': made['number'], 'id': made['id'], 'node': made['node_id']}
        save(); print(f"  #{made['number']} {it['title'][:70]}"); time.sleep(1.2)
    # Sub-issue links
    for it in issues:
        if not it['parent'] or it['key'] in st['links']:
            continue
        parent = st['issues'][it['parent']]['number']
        api('POST', f'{repo}/issues/{parent}/sub_issues', {'sub_issue_id': st['issues'][it['key']]['id']})
        st['links'].append(it['key']); save(); time.sleep(0.8)
    print(f"issues {len(st['issues'])}, sub-issue links {len(st['links'])}")
    about(st, save)
    sync(code, issues, st, save)
    project(code, issues, st, save)
    dependencies(issues, st, save)


def labels_for(code, it):
    return sorted([TYPE_LABELS[it['type']][0], f'focus area: {code}', 'notional'] + ([f"phase: {it['phase']}"] if it['phase'] else []))


def sync(code, issues, st, save):
    """Bring existing issues in line with the plan, and re-set project fields where the phase moved."""
    repo = f'/repos/{OWNER}/{NAME}'
    have, page = {}, 1
    while True:
        batch = api('GET', f'{repo}/issues?state=all&per_page=100&page={page}&labels=' + f'focus area: {code}'.replace(' ', '%20'))
        if not batch:
            break
        have.update({i['number']: i for i in batch}); page += 1
    ms = {m['title']: m['number'] for m in api('GET', f'{repo}/milestones?state=all&per_page=100')}
    changed = 0
    for it in issues:
        cur = have.get(st['issues'][it['key']]['number'])
        if cur is None:
            continue
        want_labels = labels_for(code, it)
        want_ms = PHASES[it['phase']][0] if it['phase'] else None
        cur_ms = cur['milestone']['title'] if cur['milestone'] else None
        moved = sorted(l['name'] for l in cur['labels']) != want_labels or cur_ms != want_ms or cur['state'] != it.get('state', 'open')
        if cur['title'] != it['title'] or (cur['body'] or '').replace('\r\n', '\n') != it['body'] or moved:
            data = {'title': it['title'], 'body': it['body'], 'labels': want_labels, 'state': it.get('state', 'open'),
                    **({'state_reason': 'not_planned'} if it.get('state') == 'closed' else {}),
                    'milestone': ms[want_ms] if want_ms else None}
            api('PATCH', f"{repo}/issues/{cur['number']}", data); changed += 1
            if moved:
                for lst in ('fields_set', 'dates_set'):
                    if it['key'] in st.get(lst, []):
                        st[lst].remove(it['key'])
            save(); print(f"  synced {it['key']}{' (phase moved)' if moved else ''}"); time.sleep(0.8)
    print(f'issues synced with the plan: {changed}')


def dependencies(issues, st, save):
    """Mark each story blocked by the outcomes, or whole capabilities, its plan record depends on."""
    repo = f'/repos/{OWNER}/{NAME}'
    done = st.setdefault('deps', []); skipped = set()
    wanted = {f"{it['key']}<-{ref}" for it in issues for ref in it.get('deps', [])}
    for link in [l for l in done if l not in wanted]:
        key, ref = link.split('<-')
        api('DELETE', f"{repo}/issues/{st['issues'][key]['number']}/dependencies/blocked_by/{st['issues'][ref]['id']}")
        done.remove(link); save(); print(f'  removed {key} blocked by {ref}'); time.sleep(0.8)
    for it in issues:
        for ref in it.get('deps', []):
            link = f"{it['key']}<-{ref}"
            if link in done:
                continue
            if ref not in st['issues']:
                skipped.add(ref); continue
            api('POST', f"{repo}/issues/{st['issues'][it['key']]['number']}/dependencies/blocked_by",
                {'issue_id': st['issues'][ref]['id']})
            done.append(link); save(); print(f'  {it["key"]} blocked by {ref}'); time.sleep(0.8)
    print(f"dependency links {len(done)}" + (f", not loaded on GitHub: {', '.join(sorted(skipped))}" if skipped else ''))


ABOUT = """<p align="center"><img src="https://raw.githubusercontent.com/jessestarkey/Kestrel/main/docs/assets/kestrel-mark.svg" alt="KESTREL logo, a hovering kestrel inside a reticle" width="160"></p>

> **Notional system.** KESTREL is fictional. Nothing in this repository describes a real program, real data, or a real authorization.

This repository shows a PMO ISSE applying the [SABER](https://github.com/jessestarkey/saber-framework) to a notional system. For the demonstration, three GitHub features stand in for KESTREL's self-hosted tools inside its authorization boundary:

| KESTREL's tool | Stood in for by | What it holds here |
|---|---|---|
| Jira Software Data Center | GitHub Issues with sub-issues | The Security Implementation Plan's work, as initiative, epic, story, and sub-task |
| Jira plans and boards | The [KESTREL Implementation](https://github.com/users/jessestarkey/projects/3) project | The same issues with the plan's phase, team, and activity metadata as fields |
| Confluence Data Center | This repository's wiki | Governing plans and runbooks the stories point to |
| GitLab Ultimate | This repository's code and docs | Source, infrastructure as code, and the configuration-controlled documents |

Only the Identity focus area is loaded. Every issue is generated from the plan's records by `tools/github/issues.py`, so the tracker and the documents always agree. Phases are milestones, standing in for Jira fix versions.
"""


def about(st, save):
    if 'ABOUT' in st['issues']:
        return
    made = api('POST', f'/repos/{OWNER}/{NAME}/issues', {'title': 'About this demonstration: GitHub standing in for Jira and Confluence',
                                                         'body': ABOUT, 'labels': ['notional']})
    st['issues']['ABOUT'] = {'number': made['number'], 'id': made['id'], 'node': made['node_id']}; save()
    graphql('mutation($id:ID!){pinIssue(input:{issueId:$id}){issue{number}}}', id=made['node_id'])
    print(f"  pinned #{made['number']} About this demonstration")


SELECTS = ['Level', 'Phase', 'Team', 'Control Type', 'Cross-Cutting Discipline', 'Maturity Model',
           'ConMon Activity', 'Level of Effort', 'Time Estimation']
TEXTS = ['Outcome ID', 'Cost']
DATES = ['Start Date', 'Target Date']


def values(it):
    v = {'Level': it['type'].title(), **{k: x for k, x in it.get('fields', {}).items() if x}}
    if it['phase']:
        v['Phase'] = PHASES[it['phase']][0]
    return v


def project(code, issues, st, save):
    title = 'KESTREL Implementation'
    if 'project' not in st:
        owner = graphql('query{viewer{id}}')['viewer']['id']
        repo_id = graphql('query($o:String!,$n:String!){repository(owner:$o,name:$n){id}}', o=OWNER, n=NAME)['repository']['id']
        p = graphql('mutation($o:ID!,$t:String!){createProjectV2(input:{ownerId:$o,title:$t}){projectV2{id number url}}}',
                    o=owner, t=title)['createProjectV2']['projectV2']
        graphql('mutation($p:ID!,$r:ID!){linkProjectV2ToRepository(input:{projectId:$p,repositoryId:$r}){repository{id}}}',
                p=p['id'], r=repo_id)
        graphql('mutation($p:ID!,$d:String!,$r:String!){updateProjectV2(input:{projectId:$p,shortDescription:$d,readme:$r,public:true}){projectV2{id}}}',
                p=p['id'], d='Stands in for KESTREL\'s Jira board. Notional system.', r=ABOUT)
        st['project'] = {'id': p['id'], 'number': p['number'], 'url': p['url'], 'fields': {}}; save()
        print(f"  project {p['url']}")
    pid = st['project']['id']; fields = st['project']['fields']
    # Fields, with every option the plan needs
    opts = {k: [] for k in SELECTS}
    for it in issues:
        for k, x in values(it).items():
            if k in opts and x not in opts[k]:
                opts[k].append(x)
    for k in SELECTS + TEXTS + DATES:
        if k in fields:
            continue
        dtype = 'SINGLE_SELECT' if k in SELECTS else 'DATE' if k in DATES else 'TEXT'
        args = {'p': pid, 'n': k, 'd': dtype}
        q = 'mutation($p:ID!,$n:String!,$d:ProjectV2CustomFieldType!'
        if dtype == 'SINGLE_SELECT':
            q += ',$o:[ProjectV2SingleSelectFieldOptionInput!]'
            args['o'] = [{'name': x, 'color': 'GRAY', 'description': ''} for x in sorted(opts[k])]
            q += '){createProjectV2Field(input:{projectId:$p,name:$n,dataType:$d,singleSelectOptions:$o})'
        else:
            q += '){createProjectV2Field(input:{projectId:$p,name:$n,dataType:$d})'
        q += '{projectV2Field{... on ProjectV2Field{id} ... on ProjectV2SingleSelectField{id options{id name}}}}}'
        f = graphql(q, **args)['createProjectV2Field']['projectV2Field']
        fields[k] = {'id': f['id'], 'options': {o['name']: o['id'] for o in f.get('options', [])}}; save()
    status = graphql('query($p:ID!){node(id:$p){... on ProjectV2{field(name:"Status"){... on ProjectV2SingleSelectField{id options{id name}}}}}}', p=pid)
    sf = status['node']['field']; todo = next(o['id'] for o in sf['options'] if o['name'] == 'Todo')
    # Items and their values
    for it in issues:
        key = it['key']
        if key not in st['items']:
            node = st['issues'][key]['node']
            item = graphql('mutation($p:ID!,$c:ID!){addProjectV2ItemById(input:{projectId:$p,contentId:$c}){item{id}}}',
                           p=pid, c=node)['addProjectV2ItemById']['item']['id']
            st['items'][key] = item; save(); time.sleep(0.5)
        if key in st['fields_set']:
            continue
        sets = [(sf['id'], {'singleSelectOptionId': todo})]
        for k, x in values(it).items():
            f = fields[k]
            if k in SELECTS:
                sets.append((f['id'], {'singleSelectOptionId': f['options'][x]}))
            elif k in DATES:
                sets.append((f['id'], {'date': x}))
            else:
                sets.append((f['id'], {'text': x}))
        for k in ('Phase', 'Start Date', 'Target Date'):
            if k not in values(it) and k in fields:
                graphql('mutation($p:ID!,$i:ID!,$f:ID!){clearProjectV2ItemFieldValue(input:{projectId:$p,itemId:$i,fieldId:$f}){projectV2Item{id}}}',
                        p=pid, i=st['items'][key], f=fields[k]['id'])
        for fid, val in sets:
            graphql('mutation($p:ID!,$i:ID!,$f:ID!,$v:ProjectV2FieldValue!){updateProjectV2ItemFieldValue(input:{projectId:$p,itemId:$i,fieldId:$f,value:$v}){projectV2Item{id}}}',
                    p=pid, i=st['items'][key], f=fid, v=val)
            time.sleep(0.3)
        st['fields_set'].append(key); st.setdefault('dates_set', []).append(key); save()
        print(f"  project item {key}")
    # Items loaded before Start Date existed get both dates set here.
    done = st.setdefault('dates_set', [])
    for it in issues:
        if it['key'] in done or 'Start Date' not in it.get('fields', {}):
            continue
        for k in DATES:
            graphql('mutation($p:ID!,$i:ID!,$f:ID!,$v:ProjectV2FieldValue!){updateProjectV2ItemFieldValue(input:{projectId:$p,itemId:$i,fieldId:$f,value:$v}){projectV2Item{id}}}',
                    p=pid, i=st['items'][it['key']], f=fields[k]['id'], v={'date': it['fields'][k]})
            time.sleep(0.3)
        done.append(it['key']); save()
        print(f"  dates {it['key']}")
    print(f"project items {len(st['items'])}, with fields {len(st['fields_set'])}, with dates {len(done)}")


if __name__ == '__main__':
    mode, code = sys.argv[1], sys.argv[2].upper()
    issues = build_plan(code)
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    out = os.path.join(HERE, 'out', f'{code}-plan.json')
    json.dump(issues, open(out, 'w', encoding='utf-8'), indent=1)
    counts = {t: sum(1 for i in issues if i['type'] == t) for t in TYPE_LABELS}
    print(f'{code}: {len(issues)} issues {counts}, written to {os.path.relpath(out, REPO_ROOT)}')
    if mode == 'apply':
        apply(code, issues)
