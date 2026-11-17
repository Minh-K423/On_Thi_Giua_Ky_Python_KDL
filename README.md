# NightShift: close a game café before sunrise

**Your mission:** build a small Python program that turns a messy night of PC,
console and VR bookings into a trustworthy closing report. Find the unpaid bills,
compare the three zones, and leave clean data that tomorrow's manager can reuse.

This is a **practice assignment for you to implement**, with data, starter code,
checks, and separate hints. The core TODOs are intentionally unsolved.
Aim for a working terminal program and an explanation of its behavior by 02:00.

Designed from all eight supplied PDFs (389 PDF pages), for **21:00 on November 17
to 02:00 on November 18, 2026, Vietnam time**. It assumes you have already seen the
lessons and are revising, rather than learning all eight for the first time.
There are 205 minutes of concept-focused work, 85 of product-focused work and a
10-minute break: approximately **71% school / 29% practical** of study time.

## Start here

1. Read this brief, then inspect `data/raw/tiny.csv` and `config.json`.
2. Work through R1-R4, then P1-P2, in the schedule below.
3. Write predictions before running the exercises in `EXAM_LAB.md`.
4. Use `COVERAGE.md` to locate the exact source pages for a weak topic.
5. Consult `answers/HINTS.md` only after about eight minutes stuck on one task.
   `answers/LAB_ANSWERS.md` is for checking explanations after attempting them.

All paths and all runtime data stay inside this `NightShift` folder, itself inside
`PYython_slide`. The original slides and `StudentsPerformance.csv` are unchanged.
The data here is newly invented, not a real café's records. No external service,
download, API key, account, payment processing, or package installation is needed.

## The finished product

From a terminal opened in `NightShift`:

```powershell
python -m src.main
```

The program reads 34 CSV records, accepts 24, rejects 8, and logs 2 duplicates.
It prints a closing report, writes five output files, then offers a small menu:

```text
NIGHTSHIFT | 2026-11-17
Accepted: 24 | Completed: 21 | Cancelled: 3
Charges: 1,250,000 VND | Paid: 1,100,000 VND | Due: 150,000 VND
Mean completed session: 63.71 minutes

Zone       Completed       Charges          Paid           Due
PC                 7       335,000       320,000        15,000
CONSOLE            7       405,000       345,000        60,000
VR                 7       510,000       435,000        75,000

Follow up first:
1. B015  Thảo Vy       60,000 VND
2. B008  Bùi Khang     27,500 VND
3. B002  Trần Bình     22,500 VND

> find B004
B004 | Phạm Dũng | PC | charge 35,000 | paid 20,000 | due 15,000
> zone VR
8 bookings | 7 completed | 510,000 VND charges | 75,000 VND due
> q
```

Exact spacing and wording are your choice; the amounts and meanings must agree.
**Business conclusion:** VR has the largest charges and outstanding balance in
this fictional shift. This is descriptive, not a forecast or a causal finding.

| Output you create | Contents |
|---|---|
| `data/processed/clean_bookings.csv` | 24 normalized records, same eight columns |
| `output/rejected.csv` | 8 rows: line, booking_id, reason |
| `output/duplicates.csv` | 2 rows with the same audit columns |
| `output/summary.json` | Machine-readable totals; schema in `answers/expected_summary.json` |
| `output/report.txt` | Human-readable report matching the terminal report |

Do not copy the expected JSON into your program. Calculate it from the input.
Running twice must produce the same results without appending duplicate records.

## The five-hour schedule

| Time | Work | Finish line |
|---|---|---|
| 21:00-21:15 | R0: environment + L01-L02 | Explain interpreter, venv, imports and notebook state |
| 21:15-21:55 | R1-R2: normalize and load | `python check.py parsing` passes |
| 21:55-22:30 | R3: billing functions + hand tracing | `python check.py billing` passes; explain 30 vs 31 minutes |
| 22:30-22:40 | Break | Leave the screen |
| 22:40-23:25 | R4: Booking + Shift | `python check.py models` passes |
| 23:25-00:05 | P1: summarize + Report | `python check.py summary` passes; readable report |
| 00:05-00:40 | R5: L03-L14 | Predictions, explanations, smallest fixes |
| 00:40-01:25 | P2: exports + command loop | Five outputs; valid/invalid menu commands work |
| 01:25-02:00 | R6: L15-L24 + final recall | Explain the remaining OOP/file traps without notes |

**Hard stop:** at 01:25, switch to recall even if the interface is unfinished.
If behind, use the hints and drop menu polish; preserve parsing, billing, class
state and the exam exercises. Do not add a GUI, database, machine learning,
web server, inheritance framework, charts, or installation troubleshooting tonight.
A single report from `tiny.csv` plus explanations is the fallback finish line;
full completion is the five files and working menu above. The time estimate is a
target, not a promise of mastering every slide in one night.

## R0: environment and workflow (Bài 1)

Use your working Python first; the core requires Python 3.11 or newer. From this
folder, the following creates an isolated environment locally if you want to
practice the course workflow. Activation is optional; direct interpreter paths
avoid PowerShell execution-policy distractions.

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.prefix)"
.\.venv\Scripts\python.exe -m pip --version
.\.venv\Scripts\python.exe check.py billing
```

If you use this venv, replace `python` in subsequent commands with
`.\.venv\Scripts\python.exe`, or activate it with `.\.venv\Scripts\Activate.ps1`.
`requirements.txt` intentionally has no third-party dependencies. Explain
`python -m pip freeze`, pinned versions, and `python -m pip install -r requirements.txt`;
you need not install the ecosystem libraries merely mentioned in the slides.
If Ruff is already available, run `python -m ruff check src` and
`python -m ruff format src`; otherwise apply the course's naming/import/indentation
rules manually. Finish L01-L02. Record your interpreter version in `revision_notes.md`.

## Data dictionary and exact rules

The CSV is UTF-8 **with a BOM**, includes a quoted comma in `Alex, Jr.`, and contains
Vietnamese names. Use `csv.DictReader`, not `split(',')`. Every CSV cell initially
arrives as text. The fixture has no embedded newlines, so the enumerated record
numbers starting at 2 also match physical file lines.

| Field | Normalize / validate |
|---|---|
| booking_id | Strip and uppercase; must be nonempty. Do not restrict to B-prefix: X IDs are intentionally tested for other errors. |
| player | Strip ends; preserve spelling, accents and case; must be nonempty. |
| zone | Strip and uppercase; only PC, CONSOLE, VR. |
| minutes | Parse with `int(text.strip())`; do not use int(float(...)). |
| snack_vnd | Parse as int; must be >= 0. Zero is valid. |
| paid_vnd | Parse as int; must be >= 0. Zero is valid. |
| status | Strip and lowercase; only completed or cancelled. |
| tags | Split this cell on `|`, strip/lowercase each item, discard blanks, remove duplicates, sort; empty becomes `[]`. |

Validation order: (1) exact field set and nonmissing string cells, (2) normalize
text and require ID/player, (3) allowed zone/status, (4) parse the three integers,
(5) nonnegative money, (6) duration and cancellation rules. Raise `ValueError` with
a useful reason for the first failure. Unexpected extra/missing CSV columns are
invalid; a bad header stops loading immediately. `TypeError` and misspelled
programming names must not vanish behind a broad exception handler.

Completed bookings require **1 <= minutes <= 300**. Cancelled bookings require
**minutes == snack_vnd == paid_vnd == 0**. No refunds or deposits are modeled.
Reject decimal strings, NaN, infinity and missing numbers; do not invent values.

Normalize and validate **before** deduplication. Keep the first valid row for each
normalized ID; later valid occurrences go into `duplicates`, even if other fields
differ. An invalid occurrence is rejected and does not reserve its ID. Preserve
input order in all three lists. Never edit the source CSV.

Pricing: each **started 30-minute block** costs PC 15,000, CONSOLE 22,500, VR 30,000
VND. These rates are supplied in `config.json` and must be passed to calculations.
For a completed booking, charge = rounded-up block count * rate + snacks.
Cancelled bookings have charge 0. Outstanding = `max(charge - paid, 0)`.
Overpayment is allowed: report actual money paid and zero outstanding; it is not
a negative debt. Hence total charges minus total paid is not generally total due.
All money stays integer VND. Float averages are compared using `math.isclose`.

## R1-R3: functions and structured data (Bài 2-6)

Implement TODOs in `src/data_io.py` and `src/analysis.py`.

- `normalize_row(row) -> dict`: fresh normalized record, without changing input.
- `load_bookings(path) -> (accepted, rejected, duplicates)`: lists of dicts.
  Audit dictionaries use `line` (int), `booking_id` (normalized when available),
  and a nonempty explanatory `reason`. Never catch a missing file as empty data.
- `charge_for(record, rates, /, *, block_minutes=30) -> int`: pure billing function.
  `record` and `rates` are positional-only; block size is keyword-only. Assume
  validated records, known rates and a positive integer block size.
- `balance_band(due, *, threshold=20000) -> str`: settled for 0, urgent for
  due >= threshold, otherwise follow_up. Reject due < 0 or threshold <= 0.

First write a loop by hand for each of the five patterns: count completed, sum
payments, filter unpaid, find largest debt with its ID, group by zone. Keep those
small attempts in `revision_notes.md`; reuse their logic in P1. Explain the empty
case before computing a maximum or average. Use a list, dict, set and tuple
purposefully. Refactor one simple transformation into each of a list, set and
dict comprehension. `key=` may take a named function; lambda is not required.

Tiny fixture, calculated by hand: B001 costs 40,000, B004 costs 35,000, B022 costs
0. Totals: 3 bookings, 2 completed, 1 cancelled, 75,000 charged, 60,000 paid,
15,000 due, completed mean 45.5 minutes. Explain why 0 is different from None.

## R4: model state and relationships (Bài 7-8)

Implement the contracts in `src/models.py`:

```text
Report --uses--> Shift --contains many--> Booking
                      --asks-----------> each Booking for its bill
```

`Booking` stores one normalized record. `_tags` is private by convention and copied
on input/output. A caller-supplied list must not become its internal list.
`MAX_MINUTES` is a class constant; `created_count` is a shared diagnostic counter,
not the number of active bookings. It counts successful constructions in this
Python process, including test fixtures, so never use it in the closing report.

`from_record` is a classmethod using `cls`; `valid_duration` is a staticmethod;
`charge`, `due` and `tags` are instance methods; `is_completed` is a read-only
property. Input records are already validated; the constructor additionally
checks duration, but does not need to repeat the whole CSV validator.

`Shift` owns its own list and prevents duplicate IDs. `add` returns None;
`find` returns the Booking or None. `bookings()` returns a **shallow** list copy:
clearing it cannot empty the Shift, but editing a contained object is visible.
`Report` asks Shift for its summary and formats it; it does not repeat billing logic.

Before moving on, create two shifts and two bookings. Modify one and predict what
the other sees. Explain `booking.charge(rates)` as
`Booking.charge(booking, rates)`; inspect `vars`, `type`, `isinstance`, `dir`, `help`.

## P1: useful analytics and presentation

Implement `summarize` and `Report.render`. Top-level totals and each `by_zone` entry
have `bookings`, `completed`, `cancelled`, `charges_vnd`, `paid_vnd`, `due_vnd`, and
`mean_minutes`. A mean uses **completed bookings only**, and is None when empty.
Keep unrounded floats in JSON; round only for display. Include all three zones.
`top_due` is a list of up to three dictionaries with `booking_id`, `player`,
`due_vnd`, sorted by descending due and then ascending ID, excluding settled rows.
For an empty Shift, all counts/totals are zero, averages None, and top_due empty.

Avoid taking the average of zone averages: combine totals and completed counts.
Use `enumerate(start=1)` to rank debtors, and an f-string table. Include a one-line
conclusion about which zone needs attention. This report is the favored final output.

## P2: finish the tool

Implement `write_outputs` and `command_loop`. Use a `while` loop and sequence
`match` patterns for `summary`, `find ID`, `zone NAME`, `quit` or `q`.
Handle malformed/unknown commands by printing help and continuing. The supplied
`commands.txt` is a manual test script, not another parser you must build.

Run all checks, then run the app twice:

```powershell
python check.py all
python -m src.main
```

Enter `summary`, `find B004`, `find UNKNOWN`, `zone VR`, `zone PC extra`, then `q`.
Check that Unicode names survive the round trip, all CSV files reopen correctly,
raw files are unchanged, and outputs overwrite cleanly. `check.py` covers core
contracts and totals; it does not grade report aesthetics or interactive behavior.

## How to mark your own work (100 points)

| Revision: 70 | Practical: 30 |
|---|---|
| Environment and reproducibility: 5 | Correct overall + zone report: 10 |
| Types, strings, collections, copies: 15 | Useful ranking + command menu: 10 |
| Branching, loops, function signatures and scope: 15 | Clean exports + audit trail + repeatable run: 10 |
| Files, encodings, errors, JSON and transformations: 15 | |
| OOP, attributes, properties, composition: 20 | |

Award revision points only when you can explain the behavior, not merely when a
check passes. For each missed lab, write one sentence explaining the cause and
one minimal repair. At 02:00, close your notes and explain: alias vs copy;
None vs zero; return vs print; mutable defaults; class vs instance state;
self vs cls; property vs method; shallow copy of objects; CSV vs split;
and how this program stays reproducible.

## Files supplied vs work remaining

- Supplied and ready: input fixtures, data generator, contracts, path setup,
  config loader, main orchestration, checker, known totals, labs and hints.
- Your work: function/class TODOs, report, exports, menu, and prediction answers.
- `source_notes/`: searchable extraction of every source page plus three rendered
  diagram pages used when reviewing the material. Extracted code may lose
  indentation; consult the original PDF before copying an example.
- `tools/generate_data.py`: optional deterministic fixture reset. It overwrites
  only these synthetic inputs; do not run it during normal analysis.

Full topic-to-exercise mapping, including ecosystem introductions and next-lesson
previews, is in `COVERAGE.md`. Full syllabus coverage here means **every taught
topic is encountered through implementation, prediction, or recall**, not that
every topic receives a substantial new feature or equal practice time.
