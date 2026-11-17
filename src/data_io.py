"""Read immutable inputs and write reproducible results."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
OUTPUT = ROOT / "output"
FIELDS = ("booking_id", "player", "zone", "minutes", "snack_vnd", "paid_vnd", "status", "tags")


def load_config() -> dict:
    """Read the local UTF-8 configuration. Plumbing supplied."""
    return json.loads((RAW / "config.json").read_text(encoding="utf-8"))


def normalize_row(row: dict) -> dict:
    """Return a new normalized record, or raise ValueError for invalid data.

    TODO R1: Follow README validation rules, in their stated order.
    Keep input unchanged. Tags become a sorted list of unique lowercase strings.
    Missing/unexpected CSV fields are ValueError, not silently ignored.
    """
    raise NotImplementedError("R1: normalize_row")


def load_bookings(path: Path) -> tuple[list[dict], list[dict], list[dict]]:
    """Return (accepted, rejected, duplicates), preserving input order.

    TODO R2: csv.DictReader, utf-8-sig, newline='', enumerate(start=2).
    Check the header against FIELDS (order may vary). Bad header -> ValueError.
    Normalize before deduplication; first VALID occurrence of an ID wins.
    Rejected/duplicate entries: {'line': int, 'booking_id': str, 'reason': str}.
    Catch only ValueError from normalization. Missing files must still raise.
    """
    raise NotImplementedError("R2: load_bookings")


def write_outputs(records: list[dict], rejected: list[dict], duplicates: list[dict],
                  summary: dict, report: str) -> None:
    """Write clean_bookings.csv, rejected.csv, duplicates.csv, summary.json, report.txt.

    TODO P2: Create PROCESSED and OUTPUT using pathlib. CSV tags must be
    joined by '|'; all CSVs need headers, encoding and newline=''.
    Clean records go in PROCESSED; other four files go in OUTPUT.
    Convert no original inputs in place. JSON: ensure_ascii=False, indent=2.
    Re-running replaces generated files; it must not duplicate their rows.
    """
    raise NotImplementedError("P2: write_outputs")
