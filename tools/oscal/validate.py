"""Validate an OSCAL JSON document against NIST's JSON schema.

Usage (from the kestrel repo root, with jsonschema installed):
    python tools/oscal/validate.py tools/oscal/oscal_ssp_schema.json docs/06-ssp/kestrel-ssp.oscal.json

The schema is NIST's OSCAL 1.1.2 SSP schema, from usnistgov/OSCAL's release assets.

NIST's schema uses ECMAScript Unicode classes such as \\p{L}, which Python's re cannot parse,
so each one is translated to an equivalent Python class before validating.
"""
import json
import sys

from jsonschema import Draft7Validator

BS = chr(92)


def translate(r):
    out, inclass, i = '', False, 0
    while i < len(r):
        ch = r[i]
        if ch == BS and r[i + 1:i + 3] == 'p{':
            j = r.index('}', i)
            name = r[i + 3:j]
            if name.startswith('L'):
                body = 'a-zA-Z' + chr(0xC0) + '-' + chr(0xFFFF)
            elif name.startswith('N'):
                body = '0-9'
            else:
                body = BS + 'w'
            out += body if inclass else '[' + body + ']'
            i = j + 1
            continue
        if ch == BS:
            out += r[i:i + 2]
            i += 2
            continue
        if ch == '[':
            inclass = True
        elif ch == ']':
            inclass = False
        out += ch
        i += 1
    return out


def walk(node):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == 'pattern' and isinstance(v, str) and (BS + 'p{') in v:
                node[k] = translate(v)
            else:
                walk(v)
    elif isinstance(node, list):
        for v in node:
            walk(v)


schema = json.load(open(sys.argv[1], encoding='utf-8'))
walk(schema)
doc = json.load(open(sys.argv[2], encoding='utf-8'))
errs = list(Draft7Validator(schema).iter_errors(doc))
print('errors', len(errs))
for e in errs[:15]:
    print(list(e.absolute_path)[:7], e.message[:240])
sys.exit(1 if errs else 0)
