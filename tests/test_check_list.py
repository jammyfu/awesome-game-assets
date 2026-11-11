import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import check_list  # noqa: E402
import next_plan  # noqa: E402
import render_readme  # noqa: E402
from common import load_entries, load_prompts  # noqa: E402


class ListTests(unittest.TestCase):
    def setUp(self):
        self.data = load_entries()

    def test_real_list_passes(self):
        self.assertEqual(check_list.run(), [])

    def test_required_seed_entries_present(self):
        urls = {e["url"] for e in self.data["entries"]}
        self.assertIn("https://github.com/jammyfu/open-game-skills", urls)
        self.assertIn("https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS", urls)

    def test_missing_license_fails(self):
        d = copy.deepcopy(self.data)
        d["entries"][0]["license"] = ""
        errs = []
        check_list.check_entries(d, errs)
        self.assertTrue(any("missing license" in e for e in errs))

    def test_missing_use_fails(self):
        d = copy.deepcopy(self.data)
        d["entries"][0]["zh"] = ""
        errs = []
        check_list.check_entries(d, errs)
        self.assertTrue(any("missing zh" in e for e in errs))

    def test_duplicate_link_fails(self):
        d = copy.deepcopy(self.data)
        dup = copy.deepcopy(d["entries"][0])
        dup["id"] = "dup"
        dup["url"] = dup["url"] + "/"
        d["entries"].append(dup)
        errs = []
        check_list.check_entries(d, errs)
        self.assertTrue(any("duplicate link" in e for e in errs))

    def test_duplicate_link_www_and_fragment(self):
        self.assertEqual(check_list.norm("https://www.Example.com/a/#x"), check_list.norm("https://example.com/a"))

    def test_via_must_be_credited(self):
        d = copy.deepcopy(self.data)
        d["entries"][0]["via"] = ["someone/unknown-list"]
        errs = []
        check_list.check_credits(d, errs)
        self.assertTrue(any("not in credits" in e for e in errs))

    def test_credits_section_rendered(self):
        for lang in ("en", "zh"):
            text = render_readme.render(lang)
            for c in self.data["credits"]:
                self.assertIn(c["url"], text)

    def test_banned_keyword_fails(self):
        d = copy.deepcopy(self.data)
        d["entries"][0]["name"] = "Pro Activator"
        errs = []
        check_list.check_entries(d, errs)
        self.assertTrue(any("banned keyword" in e for e in errs))

    def test_other_language_fails(self):
        d = copy.deepcopy(self.data)
        d["entries"][0]["zh"] = "素材 アセット"
        errs = []
        check_list.check_entries(d, errs)
        self.assertTrue(any("only English and Chinese" in e for e in errs))

    def test_generated_image_needs_prompt(self):
        p = copy.deepcopy(load_prompts())
        p["images"].pop(next(iter(p["images"])))
        errs = []
        check_list.check_images(self.data, p, errs)
        self.assertTrue(any("no prompt" in e or "without prompt" in e for e in errs))

    def test_original_image_needs_credit(self):
        d = copy.deepcopy(self.data)
        for e in d["entries"]:
            if e["image"]["type"] == "original":
                e["image"]["source"] = ""
                break
        errs = []
        check_list.check_images(d, load_prompts(), errs)
        self.assertTrue(any("source credit" in e for e in errs))

    def test_telemetry_pattern_detected(self):
        self.assertIsNotNone(check_list.TELEMETRY.search('<script src="https://www.googletagmanager.com/gtag/js">'))
        self.assertIsNotNone(check_list.TELEMETRY.search("https://plausible.io/js/script.js"))

    def test_readmes_parity(self):
        en = render_readme.render("en")
        zh = render_readme.render("zh")
        self.assertEqual(len(check_list.readme_urls(en)), len(self.data["entries"]))
        self.assertEqual(check_list.readme_urls(en), check_list.readme_urls(zh))

    def test_every_category_has_cover_prompt(self):
        prompts = load_prompts()["images"]
        for c in self.data["categories"]:
            self.assertIn(c["cover"], prompts)

    def test_plan_check(self):
        self.assertEqual(next_plan.check(next_plan.TEMPLATE), [])
        self.assertIn("## Goal", next_plan.check("# empty"))


if __name__ == "__main__":
    unittest.main()
