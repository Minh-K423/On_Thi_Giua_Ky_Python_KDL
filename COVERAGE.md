# Source-to-practice map

All eight supplied PDF files were read: **52 + 61 + 43 + 44 + 53 + 41 + 46 + 49 =
389 PDF pages**. Page numbers below are **PDF viewer pages**, starting at 1, not
necessarily the printed slide numbers. Bài 1 has repeated overlay pages, so its
printed slide numbering diverges from its PDF page numbering.

Implementation = build it in R/P tasks; prediction = trace/debug in L exercises;
recall = explain or recognize an introductory topic. Every taught topic is
assigned one of these. This does not claim equal depth, full exam prediction, or
coverage of subjects merely announced for future weeks.

## Bài 1 — ecosystem and workflow

Source: [Bai01_He_sinh_thai_Python.pdf](../Bai01_He_sinh_thai_Python.pdf)

| PDF pages | Topic | Where / evidence |
|---|---|---|
| 4-8 | Course goals, prediction-first, measurement before optimization, reproducibility, assessment policy | R0; lab protocol; L07; practice work is preparation, not an exam-time aid |
| 10-13 | Python as glue, language vs implementation vs environment, CPython bytecode, Python version, ecosystem roles | L01 recall |
| 15-19 | REPL, scripts, __main__, python -m, IPython help/magics, notebook | R0; L01-L02; explain `%timeit`, `%pwd`, `len?` as IPython features, not ordinary Python syntax |
| 21-28 | venv creation/activation, sys paths, interpreter mismatch, pip, freeze, pinned requirements, conda/uv | R0; L01 |
| 30-32 | Notebook strengths, stale state, Restart and Run All, reusable code in .py | L02; core in src |
| 34-36 | raw/processed/notebooks/src/tests/figures layout, README, repeatable outputs | Project layout, P2; explain why unused notebooks/figures folders need not be created tonight |
| 38-41 | Naming, imports, indentation, line width, Ruff format/check | R0; L02; inspect your completed code |
| 43-47 | Version-aware official docs, help/type/dir, / and * in signatures | L01; L09; R3-R4 |
| 49-52 | Summary and environment practical | R0 and reproducibility check |

Roadmap topics (arrays, pandas analysis, regex cleaning, plots, API/HTML/SQL,
simulation/bootstrap, machine learning, evaluation and data ethics) are introduced
as later weeks, not taught in these eight PDFs. L01 recognizes the tools; the
project does not invent an unseen NumPy/ML syllabus. Offline help is enough for
tonight; no online lookup is required to use this pack.

## Bài 2 — basic syntax

Source: [Bai02_Cu_phap_co_ban.pdf](../Bai02_Cu_phap_co_ban.pdf)

| PDF pages | Topic | Where / evidence |
|---|---|---|
| 4-7 | End-to-end file-to-report program; grouping and averages | Whole project; tiny fixture |
| 9-12 | Interactive vs script output, print sep/end, comments/indentation, traceback reading | L02; L13; P1 |
| 14-20 | Assignment, +=, swapping/unpacking, names, types, int/float/bool/str, arithmetic precedence, logical comparisons, conversion | R1/R3; L03/L09; manually trace `a,b=b,a` |
| 22-26 | Quotes, triple strings, escapes, concatenation/repetition, length, indexing/slicing, string methods, f-string formats | R1/P1; L02/L11 |
| 28-34 | if/elif/else, for/range, accumulators, unpacking, while termination, break/continue | R2/R3/P2; L06-L08 |
| 36-44 | list/tuple/dict/set properties and operations, indexing/mutation, sums/sorting, missing keys, set algebra, group/count | R1/P1; L04/L11/L21 |
| 46-50 | Built-ins, function definition, scope, return vs print, defaults, named arguments, tuple return | R1-R3; L09-L12/L21 |
| 52-56 | input always str, formatting, text read/write, modes, with, specific exceptions, math/random/import | P2; L13-L14; extra prompt below |
| 58-61 | Common errors, iteration exercises, aliasing preview | L04/L13; starter contracts |

Small recall prompts: `math.sqrt(16)`, `floor(7.8)`, `ceil(7.2)` give 4.0, 7, 8.
`random.Random(2026)` supplies repeatable pseudorandom draws for a fixed workflow;
why is a recorded seed useful? This dataset is deterministic without randomness.
Identify that standard-library imports require no pip installation. Swap two
variables using tuple unpacking and explain right-hand evaluation before assignment.

## Bài 3 — object model and copying

Source: [Bai03_Bien_va_mo_hinh_doi_tuong.pdf](../Bai03_Bien_va_mo_hinh_doi_tuong.pdf)

| PDF pages | Topic | Where / evidence |
|---|---|---|
| 4-12 | Names reference objects, assignment, id/is/==, sentinel comparison, naming | L04/L15/L24; R4 |
| 14-20 | Types/conversion, truncation, false values, numeric strings, float precision/isclose, ties-to-even round | R1/R3; L03; checker comparisons |
| 22-27 | Immutable strings, strip/split/replace/upper, comprehensions, f-strings and formats | R1/P1; L02/L11 |
| 29-33 | Mutable vs immutable, +=, aliases, caller-visible mutation | L04/L05/L10 |
| 35-39 | Assignment vs shallow copy vs deep copy; nested sharing and cost | R4; L04/L19 |
| 41-43 | Silent bugs and mutation during iteration preview | L03/L04/L07 |

**Verified correction:** PDF page 10 displays a=[1,2,3], c=[1,2,3,4], but lists
`True False` for a==c, a is c. For that displayed standalone code the correct
second output is **False False**. The first id comparison is True. L24 explicitly
revises this; do not memorize the inconsistent output.

## Bài 4 — branching and loops

Source: [Bai04_Re_nhanh_va_vong_lap.pdf](../Bai04_Re_nhanh_va_vong_lap.pdf)

| PDF pages | Topic | Where / evidence |
|---|---|---|
| 4-5, 34, 43 | Unsafe removal during traversal; build a new filtered list | L07; R2 |
| 8-13 | Comparisons, and/or/not, chained bounds, ordered elif, truth vs missing, faulty or | R1/R3; L06 |
| 15-19 | match literals, OR patterns, guards, sequence patterns, capture-name trap; version requirement | P2; L06 |
| 21-25 | Iterable traversal, range endpoints/step, enumerate, zip truncation, dict views | R2/P1; L07/L11 |
| 27-31 | while condition progress, interrupting runaway loops, break/continue, nested-loop cost | P2; L07; Ctrl+C is the terminal escape from an accidental infinite loop |
| 33-37 | Count, accumulate, filter, labeled extrema, group | R3/P1; L08 |
| 39-44 | Translate specification to iterable/output/state/pattern; group totals/counts | R3/P1; L08/L21 |

## Bài 5 — functions

Source: [Bai05_Ham.pdf](../Bai05_Ham.pdf)

| PDF pages | Topic | Where / evidence |
|---|---|---|
| 4-10 | Decomposition, def/return/early exit, implicit None, tuple returns | R1-R3; L12 |
| 12-22 | Positional/default/keyword arguments, call errors, /, *, *args, **kwargs and unpacking | R3; L09; Booking.from_record |
| 23-25 | Mutable defaults created once; None sentinel repair | R4; L05 |
| 27-33 | Reading globals, local rebinding/UnboundLocalError, avoiding global, mutation, LEGB, built-in shadowing | L10; R1/R3 purity |
| 32 | Built-in groups: aggregation/conversion/traversal/numbers/introspection/I/O | L03/L11/L15/L21 and project |
| 35-36 | Docstrings, annotations not runtime enforcement | R1-R4; L02/L10 |
| 38-45 | Verb-based decomposition, input/output contracts, single-purpose functions, over-fragmentation | Starter design; L08/L12/L24 |
| 47-53 | Modules, import forms/aliases, avoid import *, __name__, review | Supplied main; L02/L12 |

## Bài 6 — files and transformation

Source: [Bai06_Tep_va_bien_doi_du_lieu.pdf](../Bai06_Tep_va_bien_doi_du_lieu.pdf)

| PDF pages | Topic | Where / evidence |
|---|---|---|
| 4-10 | Real data pitfalls, pathlib operations, bytes/Unicode, UTF-8/BOM/wrong encoding | R1/R2; L13-L14 |
| 12-16 | Text I/O, context manager, streaming, CSV quoting/reader/DictReader/writer, newline='', types | R2/P2; L14 |
| 18-21 | Missing/locked/misdecoded files, narrow try/except, row-level error logs, avoid broad catches | R2/P2; L13; errors are not silently converted to empty success |
| 23-25 | Nested JSON, dumps/loads, ensure_ascii/indent, unsupported dates and ISO text | Config/P2; L14 |
| 27-31 | Mapping/filtering list comprehensions, set/dict comprehensions, reversed lookup, readability | R1/P1; L11/L14; invert `{zone:rate}` only when values are unique |
| 33-37 | pandas URL read, shape/head, GitHub raw vs HTML, urllib bytes/decode/JSON, Drive access, cache/provenance/no secrets | L23 offline interpretation; local snapshot for actual decoding |
| 39-41 | End-to-end data pipeline and silent pitfalls | Whole project |

The network section is **covered as recall and local simulation**, not a live
download. This respects the local-data constraint and avoids depending on a link,
network connection, or package setup during the night. It does not claim to have
tested current GitHub/Drive service behavior.

## Bài 7 — classes and instances

Source: [Bai07_Lop_va_doi_tuong.pdf](../Bai07_Lop_va_doi_tuong.pdf)

| PDF pages | Topic | Where / evidence |
|---|---|---|
| 4-8 | Tuple positional ambiguity, dict typo keys, data+behavior, class/object/attribute/method | R4; L15/L22 |
| 10-18 | Class/pass, creating instances, dynamic attributes, __init__, vars, self identity, __new__ distinction, normalization | R4; L15 |
| 19, 21-28 | Default lists, instance methods/calls, self convention/binding, missing self, implicit None, typos | R4; L05/L15/L17/L22 |
| 30-35 | List of objects, sort/max by key, lookup dict, independent vs aliased objects, print evaluation order | R4/P1; L15/L19/L21 |
| 37-39 | Specification to stateful RunningStats, incremental extrema/mean, multiple instances | L20 sketch and trace |
| 40-42 | Configuration vs learned attributes, fit/predict shape, trailing _, chaining self, pre-fit error, naming/docstrings | L20 |
| 44-46 | Summary and shared-class-list preview | L16 |

## Bài 8 — attributes and composition

Source: [Bai08_Thuoc_tinh_va_quan_he.pdf](../Bai08_Thuoc_tinh_va_quan_he.pdf)

| PDF pages | Topic | Where / evidence |
|---|---|---|
| 4-15 | Class vs instance data, shared mutables, constants/counters, lookup, shadowing/deletion, read/write asymmetry | R4; L16 |
| 17-18 | classmethod alternate constructor, cls; staticmethod utility vs instance self | R4; L17 |
| 20-24 | public/_internal/__mangled, property vs call/setter error, validation and raise | R4; L18 |
| 26-33 | Parallel-list risks, global registry limitations, contains-many, forwarding work, shallow output copies | Shift/Report; L19 |
| 34-39 | Contains-one geometry, multilevel containment/weighted totals, shared third objects, shopping-cart analogy, uses vs contains | L19/L21; extra prompt below |
| 41-45 | Report separation, cooperative classes, alternate presentation, lookup/count/capacity | P1/P2; L24; extra prompt below |
| 43, 49 | Brief override/parent-initialization preview of next lesson | L22 recognition only |
| 47-48 | All attribute/composition syntax and silent traps | R4; L16-L19/L22 |

Extra two-minute oral prompts: adapt the Shift relationship to a cart containing
items; adapt it to a segment containing two Point objects (0,0) and (3,4), whose
length is 5. For a Café containing multiple Shifts, ask each Shift for its totals
instead of accessing every internal list directly. How would add enforce a class
capacity limit? Answer: check current length before append, reject when full;
direct mutation of an internal `_bookings` list can bypass that convention.

## Scope and accuracy notes

- There are no Bài 9+ files here. Inheritance is only previewed; advanced
  polymorphism, special methods and a full data-science stack are not new core tasks.
- The source snippets sometimes rely on surrounding state or omit edge guards.
  The project explicitly specifies empty averages, cancelled rows, overpayment,
  duplicate handling, and invalid integers so your result is unambiguous.
- `_internal` does not make access impossible. Read-only properties and method
  validation guide the public API; neither turns Python objects into secure storage.
- Text extraction is searchable but can lose indentation, arrows or diagram
  placement. The original PDFs remain the authority for the displayed content;
  a fresh Python trace checks whether a displayed result follows from its code.
