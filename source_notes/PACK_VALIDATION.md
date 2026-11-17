# Practice-pack validation

Prepared 2026-11-17. This records checks of the supplied assignment materials,
not a claim that the learner's unfinished application already works.

- All eight original PDFs were extracted and read (389 PDF pages). Three object
  model/composition pages were additionally rendered and visually inspected.
- All seven supplied Python source files compile without syntax errors.
- The 34-row fixture has its intended UTF-8 BOM, Unicode names, quoted comma,
  two duplicate rows and eight intentionally invalid rows.
- Expected results were independently cross-checked using per-zone started-block
  counts (PC 19, CONSOLE 16, VR 15), snack totals (50,000 / 45,000 / 60,000 VND),
  payments and the seven nonzero outstanding balances.
- Total completed minutes are 1,338 over 21 completed bookings. Charges are
  1,250,000 VND, paid 1,100,000 VND, outstanding 150,000 VND.
- All 24 prediction exercises have matching answer sections. Source links in
  the Markdown files resolve to local files.
- The billing checker was smoke-tested against the supplied starter. It imports
  and runs, then reports the intentional R3 NotImplementedError TODOs. These are
  expected unfinished-exercise errors, not passing application tests.
- Report rendering, exports and interaction remain learner tasks; inspect them
  using the manual finish checks in README after implementation.

Original slides and the existing StudentsPerformance.csv were not edited.
