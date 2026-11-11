import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import check_list  # noqa: E402
import next_plan  # noqa: E402
import render_readme  # noqa: E402
from common import ROOT, load_entries, load_prompts, load_warnings  # noqa: E402


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

    def test_warning_files_have_caution_box_and_marks(self):
        for lang in ("en", "zh"):
            text = render_readme.render_warning(lang)
            self.assertIn("> [!CAUTION]", text)
            items = [l for l in text.splitlines() if l.startswith("- ") and "](https://github.com/" in l]
            self.assertEqual(len(items), len(load_warnings()["entries"]))
            self.assertTrue(all(l.startswith("- ⚠️ ") for l in items))

    def test_no_warning_images_stored_in_repo(self):
        stored = {p.name for p in (ROOT / "docs" / "images").iterdir()}
        for e in load_warnings()["entries"]:
            img = e.get("image")
            if img:
                self.assertTrue(img["src"].startswith("https://"))
                self.assertNotIn(img["src"].rsplit("/", 1)[-1], stored)
        self.assertFalse(any(n.startswith("warning") for n in stored))

    def test_no_download_or_install_steps_in_warnings(self):
        for e in load_warnings()["entries"]:
            for k in ("en", "zh"):
                self.assertIsNone(check_list.INSTALL_WORDS.search(e[k]), e["repo"])
            self.assertNotIn("/releases", e["url"])
        bad = copy.deepcopy(load_warnings())
        self.assertIsNotNone(check_list.INSTALL_WORDS.search("Download the setup.exe and install it"))
        self.assertIsNotNone(check_list.INSTALL_WORDS.search("解压后输入密码"))

    def test_warning_keywords_exempt_but_main_list_not(self):
        errs = []
        check_list.check_entries(load_entries(), errs)
        self.assertEqual(errs, [])
        self.assertTrue(any(check_list.BANNED.search(e["repo"]) for e in load_warnings()["entries"]))

    def test_readmes_link_to_warning_list(self):
        self.assertIn("WARNING.md", render_readme.render("en"))
        self.assertIn("WARNING.zh-CN.md", render_readme.render("zh"))

    def test_plan_check(self):
        self.assertEqual(next_plan.check(next_plan.TEMPLATE), [])
        self.assertIn("## Goal", next_plan.check("# empty"))


if __name__ == "__main__":
    unittest.main()
