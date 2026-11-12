import hashlib
import json
import re
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from common import load_entries
from render_readme import discovery_data, LOCALES, render, render_catalog, render_llms, anchor, locale_data


def source_digest(spec):
    return hashlib.sha256(json.dumps({'en': spec['locales']['en'], 'routes': spec['routes']}, ensure_ascii=False, sort_keys=True).encode()).hexdigest()

class DiscoveryTests(unittest.TestCase):
    def test_metadata_limits_and_relevance(self):
        d = discovery_data()
        self.assertEqual(d['repository'], 'jammyfu/awesome-game-assets')
        self.assertLessEqual(len(d['description']), 350)
        self.assertLessEqual(len(d['topics']), 20)
        self.assertEqual(len(d['topics']), len(set(d['topics'])))
        for topic in d['topics']:
            self.assertRegex(topic, r'^[a-z0-9][a-z0-9-]{0,49}$')
        self.assertIsNone(d['homepage'])
        self.assertNotIn('verified license', d['description'])

    def test_localized_discovery_is_reviewed_and_complete(self):
        d = discovery_data()
        self.assertEqual(set(d['locales']), set(LOCALES))
        expected = set(d['locales']['en'])
        for lang, loc in d['locales'].items():
            self.assertEqual(set(loc), expected)
            self.assertEqual(len(loc['route_labels']), len(d['routes']))
            self.assertEqual(len(loc['faq']), 4)
            self.assertEqual(set(re.findall(r'\{\w+\}',loc['summary'])), {'{entries}', '{categories}'})
            self.assertTrue(all(q.strip() and a.strip() for q,a in loc['faq']))
            if lang != 'en':
                self.assertNotEqual(loc['faq'], d['locales']['en']['faq'])
                self.assertEqual(d['reviewed_source_sha256'][lang], source_digest(d))

    def test_all_reader_route_anchors_exist(self):
        d = discovery_data()
        for lang in LOCALES:
            text = render(lang)
            for category in d['routes']:
                title = locale_data(lang)['categories'][category]
                self.assertIn(f'(#{anchor(title)})',text)
                self.assertIn(f'## {title}\n',text)
            self.assertIn(str(len(load_entries()['entries'])),text)
            for q,a in d['locales'][lang]['faq']:
                self.assertIn(q,text)
                self.assertIn(a,render_catalog(lang))

    def test_llms_full_language_coverage_and_absolute_links(self):
        text = render_llms()
        for _, suffix in LOCALES.values():
            self.assertIn(f'https://github.com/jammyfu/awesome-game-assets/blob/main/README{suffix}.md',text)
            self.assertIn(f'https://github.com/jammyfu/awesome-game-assets/blob/main/docs/catalog{suffix}.md',text)
        self.assertNotIn('bilingual',text)
        self.assertIn('non-commercial',text)
        self.assertIn('does not guarantee',text)
        self.assertIn('does not relicense',text)
        for url in re.findall(r'\]\(([^)]+)\)',text):
            self.assertTrue(url.startswith('https://'))

    def test_no_new_dropped_or_reordered_entries(self):
        data = load_entries()
        for lang in LOCALES:
            text = render(lang)
            rows = re.findall(r'^\| \[([^\]]+)\]\((https://[^)]+)\)<br>',text,re.M)
            self.assertEqual(len(rows),len(data['entries']))
            expected = []
            for category in data['categories']:
                group = [e for e in data['entries'] if e['category'] == category['id']]
                group.sort(key=lambda e: (e.get('popularity',{}).get('value') is None, -(e.get('popularity',{}).get('value') or 0)))
                expected.extend(group)
            self.assertEqual([u for _,u in rows], [e['url'] for e in expected])
            for entry in expected:
                image = entry['image']
                if image['type'] == 'original' and image.get('display_status') == 'verified':
                    self.assertIn(f'src="{image["src"]}"', text)
            self.assertEqual(text.count('<details>'),sum(sum(e['category']==c['id'] for e in expected)>15 for c in data['categories']))
