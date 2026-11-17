"""Contract checks for the learner's implementation; standard library only.

Usage: python check.py parsing|billing|models|summary|all
Unfinished starter code is expected to report NotImplementedError.
"""

import copy
import csv
import io
import json
import math
import sys
import unittest
from unittest.mock import patch

from src.analysis import balance_band, charge_for, summarize
from src.data_io import RAW, ROOT, load_bookings, load_config, normalize_row
from src.models import Booking, Shift

RATES = load_config()["rates_vnd"]


def raw_row(**changes):
    row = dict(booking_id=" b001 ", player=" Nguyễn An ", zone=" pc ",
               minutes="60", snack_vnd="10000", paid_vnd="40000",
               status=" Completed ", tags=" student |solo|STUDENT||")
    row.update(changes)
    return row


def clean_row(**changes):
    row = dict(booking_id="B001", player="Nguyễn An", zone="PC",
               minutes=60, snack_vnd=10000, paid_vnd=40000,
               status="completed", tags=["solo", "student"])
    row.update(changes)
    return row


class Parsing(unittest.TestCase):
    def test_normalization_does_not_mutate(self):
        row = raw_row()
        before = copy.deepcopy(row)
        self.assertEqual(normalize_row(row), clean_row())
        self.assertEqual(row, before)

    def test_invalid_inputs(self):
        for changes in [dict(minutes="NaN"), dict(minutes="inf"),
                        dict(minutes="1.5"), dict(minutes=""), dict(minutes="301"),
                        dict(minutes="0"), dict(zone="ARCADE"), dict(player=" "),
                        dict(paid_vnd="-1"), dict(status="pending"),
                        dict(snack_vnd="-1"), dict(booking_id="")]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                normalize_row(raw_row(**changes))
        row = raw_row()
        del row["minutes"]
        with self.assertRaises(ValueError):
            normalize_row(row)

    def test_zero_and_cancelled(self):
        self.assertEqual(normalize_row(raw_row(paid_vnd="0"))["paid_vnd"], 0)
        valid = raw_row(status="cancelled", minutes="0", snack_vnd="0", paid_vnd="0")
        self.assertEqual(normalize_row(valid)["minutes"], 0)
        for key in ["minutes", "snack_vnd", "paid_vnd"]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                normalize_row({**valid, key: "1"})

    def test_full_fixture_and_audit(self):
        valid, rejected, duplicates = load_bookings(RAW / "bookings.csv")
        self.assertEqual((len(valid), len(rejected), len(duplicates)), (24, 8, 2))
        self.assertEqual(valid[9]["player"], "Alex, Jr.")
        self.assertEqual(valid[0], clean_row())
        self.assertEqual([r["line"] for r in rejected], list(range(28, 36)))
        self.assertEqual([r["line"] for r in duplicates], [26, 27])
        for entry in rejected + duplicates:
            self.assertEqual(set(entry), {"line", "booking_id", "reason"})
            self.assertTrue(entry["reason"])

    def test_bad_header_and_missing_file(self):
        with patch("pathlib.Path.open", return_value=io.StringIO("id,player\nB1,An\n")):
            with self.assertRaises(ValueError):
                load_bookings(RAW / "mock.csv")
        with self.assertRaises(FileNotFoundError):
            load_bookings(RAW / "intentionally_missing.csv")

    def test_first_valid_id_wins(self):
        buf = io.StringIO(newline="")
        writer = csv.DictWriter(buf, fieldnames=list(raw_row()))
        writer.writeheader()
        writer.writerows([raw_row(minutes="bad"), raw_row(), raw_row(player="Other")])
        buf.seek(0)
        with patch("pathlib.Path.open", return_value=buf):
            valid, rejected, duplicates = load_bookings(RAW / "mock.csv")
        self.assertEqual([len(valid), len(rejected), len(duplicates)], [1, 1, 1])
        self.assertEqual(valid[0]["player"], "Nguyễn An")
        self.assertEqual(duplicates[0]["line"], 4)


class Billing(unittest.TestCase):
    def test_started_blocks_and_boundaries(self):
        for minutes, expected in [(1, 15000), (30, 15000), (31, 30000),
                                  (60, 30000), (61, 45000), (300, 150000)]:
            with self.subTest(minutes=minutes):
                self.assertEqual(charge_for(clean_row(minutes=minutes, snack_vnd=0), RATES), expected)
        self.assertEqual(charge_for(clean_row(), RATES), 40000)
        self.assertEqual(charge_for(clean_row(minutes=31, snack_vnd=0), RATES, block_minutes=60), 15000)

    def test_cancelled_and_purity(self):
        row = clean_row(minutes=0, snack_vnd=0, paid_vnd=0, status="cancelled")
        before = copy.deepcopy((row, RATES))
        self.assertEqual(charge_for(row, RATES), 0)
        self.assertEqual((row, RATES), before)

    def test_bands_and_signature(self):
        for due, expected in [(0, "settled"), (1, "follow_up"),
                              (19999, "follow_up"), (20000, "urgent")]:
            self.assertEqual(balance_band(due), expected)
        self.assertEqual(balance_band(100, threshold=100), "urgent")
        with self.assertRaises(ValueError):
            balance_band(-1)
        with self.assertRaises(ValueError):
            balance_band(1, threshold=0)
        with self.assertRaises(TypeError):
            charge_for(clean_row(), RATES, 30)
        with self.assertRaises(TypeError):
            charge_for(record=clean_row(), rates=RATES)


class Models(unittest.TestCase):
    def test_methods_property_and_counter(self):
        start = Booking.created_count
        b = Booking.from_record(clean_row())
        self.assertEqual(Booking.created_count, start + 1)
        self.assertEqual(b.charge(RATES), Booking.charge(b, RATES))
        self.assertEqual(b.charge(RATES), 40000)
        self.assertTrue(b.is_completed)
        with self.assertRaises(AttributeError):
            b.is_completed = False
        self.assertEqual(Booking.from_record(clean_row(paid_vnd=999999)).due(RATES), 0)

    def test_duration_and_tag_ownership(self):
        self.assertTrue(Booking.valid_duration(300, "completed"))
        self.assertTrue(Booking.valid_duration(0, "cancelled"))
        for minutes, status in [(True, "completed"), (1.5, "completed"),
                                (0, "completed"), (301, "completed"), (1, "other")]:
            self.assertFalse(Booking.valid_duration(minutes, status))
        before = Booking.created_count
        with self.assertRaises(ValueError):
            Booking.from_record(clean_row(minutes=301))
        self.assertEqual(Booking.created_count, before)
        record = clean_row()
        b = Booking.from_record(record)
        record["tags"].append("outside")
        b.tags().clear()
        self.assertEqual(b.tags(), ["solo", "student"])
        a = Booking(**{**clean_row(), "tags": None})
        c = Booking(**{**clean_row(booking_id="B002"), "tags": None})
        self.assertIsNot(a._tags, c._tags)

    def test_shift_independence_copy_and_lookup(self):
        a, b = Shift("A"), Shift("B")
        item = Booking.from_record(clean_row())
        self.assertIsNone(a.add(item))
        self.assertEqual(b.bookings(), [])
        self.assertIs(a.find("B001"), item)
        self.assertIsNone(a.find("MISSING"))
        a.bookings().clear()
        self.assertEqual(len(a.bookings()), 1)
        a.bookings()[0].player = "Changed"
        self.assertEqual(a.find("B001").player, "Changed")
        with self.assertRaises(ValueError):
            a.add(Booking.from_record(clean_row()))
        with self.assertRaises(TypeError):
            a.add({})


class Summary(unittest.TestCase):
    def test_full_known_totals(self):
        records, _, _ = load_bookings(RAW / "bookings.csv")
        items = [Booking.from_record(r) for r in records]
        before = copy.deepcopy([vars(b) for b in items])
        got = summarize(items, RATES)
        expected = json.loads((ROOT / "answers" / "expected_summary.json").read_text(encoding="utf-8"))
        self.assert_nested(got, expected)
        self.assertEqual([vars(b) for b in items], before)

    def assert_nested(self, got, expected):
        if isinstance(expected, dict):
            self.assertEqual(set(got), set(expected))
            for key in expected:
                self.assert_nested(got[key], expected[key])
        elif isinstance(expected, list):
            self.assertEqual(len(got), len(expected))
            for a, b in zip(got, expected):
                self.assert_nested(a, b)
        elif isinstance(expected, float):
            self.assertTrue(math.isclose(got, expected, rel_tol=1e-9))
        else:
            self.assertEqual(got, expected)

    def test_empty_and_weighted_mean(self):
        empty = summarize([], RATES)
        self.assertEqual(empty["bookings"], 0)
        self.assertEqual(empty["top_due"], [])
        self.assertIsNone(empty["mean_minutes"])
        for zone in RATES:
            self.assertIsNone(empty["by_zone"][zone]["mean_minutes"])
            self.assertEqual(empty["by_zone"][zone]["due_vnd"], 0)
        items = [Booking.from_record(clean_row(minutes=30)),
                 Booking.from_record(clean_row(booking_id="B002", minutes=90)),
                 Booking.from_record(clean_row(booking_id="B003", zone="VR", minutes=180))]
        self.assertEqual(summarize(items, RATES)["mean_minutes"], 100)

    def test_ties_and_overpayment(self):
        items = [Booking.from_record(clean_row(booking_id=k, paid_vnd=0))
                 for k in ["B003", "B001", "B002", "B004"]]
        got = summarize(items, RATES)
        self.assertEqual([r["booking_id"] for r in got["top_due"]], ["B001", "B002", "B003"])
        items = [Booking.from_record(clean_row(booking_id="B001", paid_vnd=50000)),
                 Booking.from_record(clean_row(booking_id="B002", paid_vnd=0))]
        got = summarize(items, RATES)
        self.assertEqual((got["charges_vnd"], got["paid_vnd"], got["due_vnd"]), (80000, 50000, 40000))


if __name__ == "__main__":
    groups = {"parsing": Parsing, "billing": Billing, "models": Models, "summary": Summary}
    selected = sys.argv[1] if len(sys.argv) > 1 else "all"
    if selected not in (*groups, "all"):
        raise SystemExit("Choose parsing, billing, models, summary, or all")
    print("Starter TODO failures are expected until you implement that stage.")
    suite = unittest.TestSuite()
    for name, case in groups.items():
        if selected in (name, "all"):
            suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(case))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
