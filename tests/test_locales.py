import copy
import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from check_locales import validate_locale,source_digest
from render_readme import locale_data,LOCALES,render,render_catalog

class LocaleTests(unittest.TestCase):
    def test_complete_locales(self):
        for lang in ('zh-TW','ja','ko'):
            self.assertEqual(validate_locale(lang,locale_data(lang)),[])
    def test_missing_translation_fails(self):
        d=copy.deepcopy(locale_data('ja'));d['entries'].pop(next(iter(d['entries'])))
        self.assertTrue(validate_locale('ja',d))
    def test_english_fallback_fails(self):
        d=copy.deepcopy(locale_data('ko'));d['entries'][next(iter(d['entries']))]='An English fallback.'
        self.assertTrue(validate_locale('ko',d))
    def test_stale_source_hash_fails(self):
        d=copy.deepcopy(locale_data('zh-TW'));d['source_sha256']='old'
        self.assertTrue(validate_locale('zh-TW',d))
    def test_navigation_and_local_catalog_links(self):
        for lang,(_,suffix) in LOCALES.items():
            r=render(lang); c=render_catalog(lang)
            self.assertIn(f'(../README{suffix}.md)',c)
            for code,(_,other) in LOCALES.items():
                if code!=lang:
                    self.assertIn(f'(README{other}.md)',r)
                    self.assertIn(f'(catalog{other}.md)',c)
    def test_template_missing_fails(self):
        d=copy.deepcopy(locale_data('ja'));d['ui']['expand']='More'
        self.assertTrue(validate_locale('ja',d))

    def test_rules_placeholder_and_empty_fail(self):
        d=copy.deepcopy(locale_data('ja'));d['ui']['rules'][3]=''
        self.assertTrue(validate_locale('ja',d))
    def test_table_breaker_fails(self):
        d=copy.deepcopy(locale_data('ko'));d['entries'][next(iter(d['entries']))]='소재 | 추가 열'
        self.assertTrue(validate_locale('ko',d))
