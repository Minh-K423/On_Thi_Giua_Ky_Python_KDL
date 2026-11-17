"""Recreate the fictional practice inputs. Standard library only.

Run only when intentionally resetting data/raw; never run during analysis.
All people, bookings and business rules are synthetic, created 2026-11-17.
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
FIELDS = ["booking_id", "player", "zone", "minutes", "snack_vnd", "paid_vnd", "status", "tags"]


def main():
    """Write deterministic fixtures without network access or randomness."""
    RAW.mkdir(parents=True, exist_ok=True)
    rows = [
        ["B001", " Nguyễn An ", " pc ", "60", "10000", "40000", " completed ", "solo|student"],
        ["B002", "Trần Bình", "CONSOLE", "90", "15000", "60000", "completed", "party|student"],
        ["B003", "Lê Chi", "VR", "30", "0", "30000", "completed", "first_visit"],
        ["B004", "Phạm Dũng", "PC", "31", "5000", "20000", "completed", "solo"],
        ["B005", "Hoàng Hà", "CONSOLE", "60", "0", "45000", "completed", "party"],
        ["B006", "Võ Minh", "VR", "45", "20000", "80000", "completed", "party|first_visit"],
        ["B007", "Đỗ Lan", "PC", "120", "10000", "70000", "completed", "student|ranked"],
        ["B008", "Bùi Khang", "CONSOLE", "30", "5000", "0", "completed", "party"],
        ["B009", "Mai Linh", "VR", "60", "10000", "60000", "completed", "first_visit"],
        ["B010", "Alex, Jr.", "PC", "15", "0", "15000", "completed", "solo|tourist"],
        ["B011", "Ngọc Anh", "CONSOLE", "61", "10000", "77500", "completed", "party"],
        ["B012", "Quốc Bảo", "VR", "90", "15000", "100000", "completed", "ranked"],
        ["B013", "Tú Uyên", "PC", "180", "20000", "110000", "completed", "ranked|student"],
        ["B014", "Gia Huy", "CONSOLE", "120", "0", "90000", "completed", "party|ranked"],
        ["B015", "Thảo Vy", "VR", "31", "0", "0", "completed", "first_visit"],
        ["B016", "Hải Đăng", "PC", "30", "5000", "20000", "completed", "solo"],
        ["B017", "Khánh Ngân", "CONSOLE", "45", "5000", "40000", "completed", "party|student"],
        ["B018", "Thiên Phúc", "VR", "120", "10000", "130000", "completed", "ranked"],
        ["B019", "Minh Châu", "PC", "90", "0", "45000", "completed", "student"],
        ["B020", "Tuấn Kiệt", "CONSOLE", "15", "10000", "32500", "completed", "party"],
        ["B021", "Yến Nhi", "VR", "15", "5000", "35000", "completed", "tourist|first_visit"],
        ["B022", "Đức Long", "PC", "0", "0", "0", "cancelled", ""],
        ["B023", "Bảo Trân", "CONSOLE", "0", "0", "0", "cancelled", "party"],
        ["B024", "Anh Thư", "VR", "0", "0", "0", "cancelled", "first_visit"],
    ]
    rows += [list(rows[0]), list(rows[9])]
    rows += [
        ["X001", "Bad minutes", "PC", "sixty", "0", "0", "completed", ""],
        ["X002", "Bad zone", "ARCADE", "30", "0", "0", "completed", ""],
        ["X003", "   ", "PC", "30", "0", "0", "completed", ""],
        ["X004", "Bad status", "PC", "30", "0", "0", "pending", ""],
        ["X005", "Negative snack", "PC", "30", "-1", "0", "completed", ""],
        ["X006", "Zero play", "VR", "0", "0", "0", "completed", ""],
        ["X007", "Too long", "CONSOLE", "301", "0", "0", "completed", ""],
        ["X008", "Non-finite", "PC", "NaN", "0", "0", "completed", ""],
    ]
    with (RAW / "bookings.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(FIELDS)
        writer.writerows(rows)
    # Tiny, independently hand-checkable case: 2 completed + 1 cancelled.
    with (RAW / "tiny.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(FIELDS)
        writer.writerows([rows[0], rows[3], rows[21]])
    config = {
        "title": "NightShift - Game Cafe Closing Report",
        "shift_date": "2026-11-17",
        "block_minutes": 30,
        "rates_vnd": {"PC": 15000, "CONSOLE": 22500, "VR": 30000},
        "alert_threshold_vnd": 20000,
        "metadata": {"currency": "VND", "synthetic": True, "notes": ["Ôn tập Python", "Offline only"]},
    }
    (RAW / "config.json").write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (RAW / "api_snapshot.json").write_text(json.dumps({"source": "fictional cached API", "promotions": [{"zone": "PC", "label": "Đêm luyện rank"}]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (RAW / "fake_download.html").write_text('<!doctype html><html><body>Sign in to view this file.</body></html>\n', encoding="utf-8")
    (RAW / "commands.txt").write_text('summary\nfind B004\nfind UNKNOWN\nzone VR\nzone PC extra\nquit\n', encoding="utf-8")
    print(f"Created {len(rows)} booking rows and supporting fixtures in {RAW}")


if __name__ == "__main__":
    main()
