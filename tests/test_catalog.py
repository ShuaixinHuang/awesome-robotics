import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.check_catalog import ROOT, check_catalog, check_documentation_links


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.text = (ROOT / "README.md").read_text(encoding="utf-8")

    def test_real_catalog_passes_and_counts_every_direction(self):
        counts, errors = check_catalog(self.text)
        self.assertFalse(errors, errors)
        self.assertTrue(all(count > 0 for count in counts.values()))

    def test_missing_anchor_is_reported(self):
        _, errors = check_catalog(self.text.replace('<a id="vla"></a>', ""))
        self.assertTrue(any("#vla" in error for error in errors))

    def test_detached_table_rows_are_reported(self):
        _, errors = check_catalog(
            self.text.replace("\n| **robot-data-diff**", "\n\n| **robot-data-diff**")
        )
        self.assertTrue(any("detached" in error for error in errors))

    def test_added_resource_requires_total_and_navigation_updates(self):
        row = "| **Checker fixture** | Example | [Source](https://example.com) | Test only |\n"
        text = self.text.replace("| **LeLab**", row + "| **LeLab**", 1)
        counts, errors = check_catalog(text)
        original, _ = check_catalog(self.text)
        self.assertEqual(counts["robots"], original["robots"] + 1)
        self.assertTrue(any("Resource total" in error for error in errors))
        self.assertTrue(
            any("Navigation count for #robots" in error for error in errors)
        )

    def test_duplicate_names_and_bad_columns_are_reported(self):
        row = next(
            line for line in self.text.splitlines() if line.startswith("| **LeLab**")
        )
        _, errors = check_catalog(self.text.replace(row, row + "\n" + row))
        self.assertTrue(any("duplicate resource name" in error for error in errors))
        _, errors = check_catalog(
            self.text.replace(row, row[:-1] + " extra | column |")
        )
        self.assertTrue(any("four resource columns" in error for error in errors))


    def test_real_documentation_links_pass(self):
        self.assertEqual(check_documentation_links(ROOT), [])

    def test_relative_markdown_targets_and_anchors_are_checked(self):
        with TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "docs").mkdir()
            (root / "README.md").write_text(
                '<a id="start"></a>\n[Guide](docs/guide.md#missing)\n'
                '[Missing](docs/missing.md)\n[External](https://example.com/page.md)\n',
                encoding="utf-8",
            )
            (root / "docs/guide.md").write_text(
                '[Home](../README.md#start)\n', encoding="utf-8"
            )
            self.assertEqual(
                check_documentation_links(root),
                [
                    "README.md:2: missing explicit anchor in docs/guide.md#missing",
                    "README.md:3: missing Markdown target docs/missing.md",
                ],
            )

    def test_official_source_can_appear_in_description(self):
        row = "| **Fixture** | Example | 见说明 | [Source](https://example.com) |"
        text = self.text.replace("| **LeLab**", row + "\n| **LeLab**", 1)
        _, errors = check_catalog(text)
        self.assertFalse(any("expected a project or source link" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
