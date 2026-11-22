import unittest

from scripts.check_catalog import ROOT, check_catalog


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


if __name__ == "__main__":
    unittest.main()
