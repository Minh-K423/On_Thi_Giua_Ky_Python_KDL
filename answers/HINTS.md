# Staged hints: open only the section where you are stuck

Try for about eight minutes before opening a hint. If you need a hint, close it
after reading and implement from understanding. No full application solution is
included, so the core work remains yours.

## R1: cleaning one record

1. Establish the expected keys first. CSV missing values may be None and surplus
   cells may appear under a None key. Validate shape before calling strip.
2. Build a new dictionary; do not change the dictionary you were passed.
3. Normalize identifiers/status first. Convert the three integers inside a narrow
   try/except ValueError and re-raise a useful ValueError if conversion fails.
4. Use explicit bounds, not `if value`, because zero is valid money.
5. For tags: split on `|`, strip/lower each item, discard empty items, make a set,
   then sorted. An intermediate list is clearer than a crowded comprehension.

## R2: loading with an audit trail

Keep three result lists plus a set of seen valid IDs. Open with utf-8-sig and
newline=''. Check DictReader.fieldnames before processing rows. For each numbered
row, normalize in a narrow try block. On ValueError, append an audit dictionary
and continue. Only after successful normalization check seen, then either append
a duplicate audit entry or accept the row and add its ID to seen.

Full fixture: accepted B001-B024; duplicates at file lines 26 and 27; rejected
X001-X008 at lines 28-35. Reasons: invalid integer, zone, empty player, status,
negative snack, invalid completed zero duration, excessive duration, invalid integer.
The exact error wording is free, but a nonempty reason must help a reader.

## R3: billing and conditions

Cancelled -> zero immediately. For a positive duration, rounded-up block count is
`(minutes + block_minutes - 1) // block_minutes`. Alternatively use math.ceil on
the quotient. A 31-minute PC session uses two blocks, not one.

Test classification in a sensible order: settled, urgent, follow_up. Reject invalid
inputs before classifying. Keep computation separate from printing and reading.

## R4: three classes

Create per-object containers in __init__, never directly under class. After
validating duration, assign all fields and set `_tags` to a fresh list. Update
`Booking.created_count`, not `self.created_count`. from_record can unpack a dict
into cls; it does not need to know where the data came from.

valid_duration has no self/cls; be careful that bool is a subclass of int in Python.
The contract intentionally excludes True as one minute, so an exact int type
check is useful here. A property is read without parentheses.

In charge, construct a small normalized dictionary from stored fields and delegate
to charge_for. In due, subtract actual paid and clamp at zero. Shift.add checks
the object type and existing IDs before append; Shift.find can use a for loop
with an early return and return None after the loop.

Use `list(self._bookings)` for a shallow copy. That protects the collection's
membership, not the state of each contained object. Do not deep-copy on every
lookup just to avoid thinking about ownership.

## P1: aggregation and presentation

Write a small helper for the seven aggregate fields, then reuse it for all bookings
and each zone. Initialize totals before looping. Mean minutes uses completed
duration sum / completed count; None for zero count.

Build debt rows only for positive due. A sort key such as `(-due, booking_id)`
handles both order rules in one ascending sort. Slice the first three.
For a key function, either a named def or a short lambda is fine.

Report calls shift.summary and converts results to text; the ledger calculations
already belong elsewhere. Build a list of lines and join them with '\n'. Format
money with commas; format a missing average as N/A rather than formatting None
as a float. Keep any rounding in the presentation layer.

## P2: exports and interaction

Use fresh row dictionaries to replace tag lists with '|'.join(tags) before CSV
writing, leaving in-memory records unchanged. DictWriter writes fieldnames and
writeheader even for an empty list. Use mode='w' for generated outputs. JSON
serialization handles None as null automatically. Use explicit UTF-8.

The menu is a while True loop around input. Catch EOFError only at that input
call if you want clean end-of-input. Match token sequences so wrong arity falls
to help. Use the OR pattern for ['q'] | ['quit']; use a guard for known zone names.
Stop with break. Avoid editing payments, history persistence and extra menus.

## If time is slipping away

At 23:25, switch to tiny.csv to debug totals if necessary. At 00:40, get the
report saved before adding menu refinements. At 01:25, stop coding and do L15-L24.
Use the remaining time to explain the mistakes you actually made; you do not
need to memorize the fictional café's totals for the exam.
