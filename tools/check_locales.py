#!/usr/bin/env python3
"""Require complete localizations and reject silent source-text drift."""
import hashlib
import json
import re
from common import ROOT, load_entries
from render_readme import LOCALES, locale_data, render, render_catalog, license_summary

def source_digest():
    data = load_entries()
    source = {
        'entries': {e['id']: {key: e.get(key) for key in ('en','name','category','license','license_source','url')} for e in data['entries']},
        'categories': {c['id']: c['en'] for c in data['categories']},
        'licenses': {e['license']: license_summary(e['license'], 'en') for e in data['entries']},
        'notes': {e['id']: e['link_note']['en'] for e in data['entries'] if e.get('link_note')},
        'ui': locale_data('en')['ui'],
    }
    return hashlib.sha256(json.dumps(source, sort_keys=True, ensure_ascii=False).encode()).hexdigest()

def validate_locale(lang, loc):
    data = load_entries()
    errors = []
    expected = {'entries': {e['id'] for e in data['entries']}, 'categories': {c['id'] for c in data['categories']}, 'license_summaries': {e['license'] for e in data['entries']}, 'link_notes': {e['id'] for e in data['entries'] if e.get('link_note')}, 'ui': set(locale_data('en')['ui'])}
    for key, ids in expected.items():
        values = loc.get(key)
        if not isinstance(values, dict) or set(values) != ids:
            errors.append(f'{lang}: {key} keys do not match source')
            continue
        for item, value in values.items():
            if not value or (isinstance(value,str) and re.search(r'\bTODO\b|\bTBD\b|TRANSLATE_ME',value)):
                errors.append(f'{lang}: incomplete {key}/{item}')
    ui = loc.get('ui', {})
    source_ui = locale_data('en')['ui']
    for key, original in source_ui.items():
        translated = ui.get(key)
        pairs = zip(original, translated) if isinstance(original,list) and isinstance(translated,list) else [(original,translated)]
        if isinstance(original,list) and (not isinstance(translated,list) or len(original)!=len(translated)):
            errors.append(f'{lang}: {key} list length/type differs')
            continue
        for src,dst in pairs:
            if not isinstance(dst,str) or not dst.strip():
                errors.append(f'{lang}: invalid ui/{key}')
            elif isinstance(src,str) and set(re.findall(r'\{\w+\}',src)) != set(re.findall(r'\{\w+\}',dst)):
                errors.append(f'{lang}: placeholder mismatch ui/{key}')
    for key in ('entries','license_summaries','link_notes'):
        for item,value in loc.get(key,{}).items():
            if isinstance(value,str) and ('\n' in value or re.search(r'(?<!\\)\|',value)):
                errors.append(f'{lang}: unsafe table text {key}/{item}')
    script = {'ja': r'[\u3040-\u30ff]', 'ko': r'[\uac00-\ud7af]', 'zh-TW': r'[\u4e00-\u9fff]'}[lang]
    for field in ('entries', 'categories', 'license_summaries', 'link_notes'):
        for eid, value in loc.get(field,{}).items():
            if not isinstance(value,str) or not re.search(r'[\u3040-\u30ff\u4e00-\u9fff]' if lang=='ja' and field=='categories' else script,value): errors.append(f'{lang}: untranslated {field}/{eid}')
    for key in ('intro','back','hero_caption','browse','contribute_label','sort_note','mobile','expand','identity','source','missing','list_scope','unknown_heat','cols'):
        if not re.search(script,ui.get(key,'')): errors.append(f'{lang}: untranslated ui/{key}')
    for key in ('expand',):
        if '{count}' not in loc.get('ui',{}).get(key,''): errors.append(f'{lang}: missing count template')
    if loc.get('source_sha256') != source_digest(): errors.append(f'{lang}: source changed; review translations and refresh source_sha256')
    return errors

def main():
    errors=[]
    for lang in ('zh-TW','ja','ko'):
        try: errors += validate_locale(lang,locale_data(lang))
        except (OSError,ValueError) as exc: errors.append(str(exc))
    if not errors:
        data=load_entries(); urls={e['url'] for e in data['entries']}
        for lang, (_, suffix) in LOCALES.items():
            for text in (render(lang),render_catalog(lang)):
                found=re.findall(r'^\| \[[^\]]+\]\((https://[^)]+)\)<br>',text,re.M)
                if len(found)!=len(urls) or set(found)!=urls: errors.append(f'{lang}: catalog coverage differs')
                for _, other in LOCALES.values():
                    if other != suffix and f'{other}.md)' not in text: errors.append(f'{lang}: missing language navigation {other}')
    print('\n'.join(errors) if errors else 'Five-language coverage and source-drift checks passed.')
    return bool(errors)
if __name__=='__main__': raise SystemExit(main())
