# Prediction lab: check only after attempting

These are explanation targets, not a solution to the application TODOs.

**L01.** Python is the language; CPython is an implementation; an environment is
an interpreter plus installed packages/versions. CPython compiles source to
bytecode and executes it; cached bytecode is generated, not hand-edited.
REPL: quick expressions; script: repeatable workflow; IPython: enhanced interactive
inspection; notebook: code/output/prose with execution state. `python -m pip`
selects that interpreter's pip. executable is the binary; prefix identifies its
environment root. venv isolates Python packages, conda manages environments and
non-Python dependencies too, uv is another environment/package workflow tool.
Pinned versions record dependencies; raw/processed separation preserves provenance.
NumPy: arrays/numerics; pandas: tables; re: patterns; Matplotlib/seaborn: plots;
SciPy: scientific/statistical routines; scikit-learn: ML; requests: HTTP;
BeautifulSoup: HTML parsing; sqlite3: SQL; Git: versioning; Ruff: lint/format.
Most are roadmap introductions, not algorithms taught in these eight decks.

**L02.** Old cell-2 output stays 20. Running it again, or restarting and running
all, prints `tenten`. REPL displays expression values; scripts need print. A
docstring is runtime-accessible documentation; comments are source annotations.
Main guards separate direct execution from import. Format example:
`print(f"Paid\t{40000:,} VND\nShare {0.75:.1%}", end="\n")`.
`print(f"{'VR':<8}", f"{63.714:.2f}", sep=" | ")`.

**L03.** `(True, False)`; `(3, -3, 2, 4)`; `(True, True, False, False)`;
`(3.5, 3, 1, 512, (3,1))`; False; ValueError. Compare approximate numeric
results with math.isclose. float('8.5') is valid if a decimal is allowed; truncating
it is not acceptable validation for integer minutes. Reassignment rebinds a name;
it does not turn the original integer into a string. int has arbitrary precision
subject to available resources; floats approximate many decimal fractions.

**L04.** `True False True`, then `['solo','ranked'] ['solo']`. The dictionary
copy is new but its tag list is shared; deep copy separates the nested state.
List += prints `[1,2]`; string += prints `a` through the original name.
Flat containers of immutable values need only shallow copies; deep copy traverses
nested state and costs extra work. Equality compares values for these built-ins;
identity compares objects. Use `is None` for the missing-value sentinel.

**L05.** First `['solo']`, then `['solo','ranked']`. The default is evaluated
once when def executes. Use tags=None and create [] when None. For an independent
flat copy even when supplied, use `tags = [] if tags is None else list(tags)`.
If mutation is intended, retain the supplied list and document that side effect.

**L06.** Prints cheap, follow_up, missing, 99. The nonempty string in the first
condition is truthy; use membership. Test the urgent bound before the weaker bound.
Use `paid is not None`. A bare match name captures rather than compares; use a
literal, qualified constant, or guard. Patterns include `case ['find', code]:`,
`case ['q'] | ['quit']:`, `case ['zone', z] if z in rates:`, `case _:`.
Use if for simple inequalities or conditions involving unrelated expressions.

**L07.** `[8,9,4,7]`, `[('A',10),('B',20)]`, `[5,3,1]`, then `0 0` and `1 0`.
Removal shifts remaining elements; a fresh filter `[v for v in values if v>=5]`
does not skip them. continue advances the current loop; break exits that loop.
zip silently stops at the shorter input. The terminating loop starts n=1 and
updates n*=3 while n<=100, ending at 243. Two nested loops of sizes m,n may do
m*n iterations; do not call one faster without measuring.

**L08.** Count: start 0; accumulate: start 0; filter: fresh list; maximum: first
record or a None sentinel; groups: dictionary of lists or totals/counts. Maximum
is B with -3, not zero. Empty maxima/means can return None by contract. An
initializer inside the loop discards previous progress. Inputs, output shape,
state and pattern are the four design questions before writing the loop.

**L09.** `('B001','WARN',(1,2),True,{'line':4})`. The three invalid calls raise
TypeError for a required positional first argument, duplicate label values, and
missing first, respectively. Because **details exists, first= would be collected
there, but it still does not supply the positional-only first parameter.
`audit(*args, **options)` unpacks both collections. f(1,'a') is TypeError;
f(1,title='a') is valid; f(x=1,2) is SyntaxError. A misspelled keyword without a
**kwargs catch-all is TypeError. Read positional-only, ordinary/default,
var-positional, keyword-only and var-keyword parameters in their declared order.

**L10.** UnboundLocalError: assignment makes count local throughout bump, so the
right-hand read precedes a local value. Use `def bump(count): return count+1`
and `count=bump(count)`. Lookup is Local, Enclosing, Global, Built-in; the nearest
defined label wins. Shadowing sum resolves to an integer, causing TypeError when
called. Annotations do not enforce runtime types. append mutates the shared
object; it does not rebind the caller's variable.

**L11.** `repr(s)` is `' VR|solo '`, slice is `VR`, final character is a space,
membership True; find/count give `2 3`; startswith/replace give `True DC`;
tuple becomes `([1,2],'VR')`. Both indexed assignments fail with TypeError, but
mutating the list stored inside a tuple is allowed. append/insert/remove/sort
mutate and return None; pop removes and returns an element. sorted returns a new
list. Missing dict indexing raises KeyError; get supplies a default. keys,
values, items are views. Intersection is {'ranked'}, union contains all three,
difference is {'solo'}; printed set ordering is not guaranteed.
Examples: `[t.upper() for t in tags]`, `{t for t in tags}`,
`{t:len(t) for t in tags}`. Duplicate dict keys keep their last assigned value.

**L12.** Prints 40000 inside bill, then None. `return 40000` enables composition
with other calculations. Multiple return values form one tuple, unpacked by the
caller. Parsing/normalization and accounting should return results; export and
print intentionally have side effects. The import forms bind a module, a named
member, and a module alias. A main guard prevents a demo running during import.

**L13.** ValueError, ValueError, ZeroDivisionError, IndexError, KeyError,
NameError, TypeError, FileNotFoundError, UnicodeDecodeError, typically
PermissionError, AttributeError, IndentationError, SyntaxError, respectively.
Read the traceback's final type/message, then its file/line. Catch normalization
ValueError at the row boundary and retain the rejected row's number/reason.
Broad catches hide programming mistakes. cwd is where execution starts; __file__
anchors to the module's location. r reads, w truncates/replaces, a appends. with
closes on normal exit and exceptions. Iterating lines avoids loading an entire
large text file. JSON and the tiny config can reasonably be read at once.

**L14.** utf-8-sig strips the BOM; csv handles quoted commas. newline='' lets csv
handle line endings consistently. `raw=path.read_bytes(); obj=json.loads(raw.decode('utf-8'))`.
Date serialization raises TypeError; date.isoformat() returns a JSON-compatible
string. dumps/loads operate on strings; dump/load operate on file objects.
`ễ` is one character and three UTF-8 bytes. encode: text to bytes; decode: bytes
to text. ensure_ascii=False preserves readable Unicode in serialized text;
indent=2 only affects presentation. JSON does not preserve arbitrary Python objects.

**L15.** `2 1 2 3`. The earlier print arguments were evaluated before x.bump()
incremented state. z aliases x; y is independent. Bound instance methods supply
self automatically; the class attribute is a function needing an explicit object.
__new__ creates; __init__ initializes and returns None. Returning a non-None value
from __init__ causes TypeError. A normal class without custom equality uses
identity-based equality. Names like self are conventions, not keywords.

**L16.** `8 5 5`; `1 0 0 ['seen']`; then `5`. Before deletion, vars(a) contains
visits=1 and limit=8, but not class-owned tags. Afterwards limit disappears.
Initialize self.tags=[] for each object. Update Desk.visits for a shared counter.
self.visits += 1 reads the class integer then assigns an instance integer;
append changes the existing shared list. Booking.created_count counts successful
constructions, not unique accepted rows or objects currently in one Shift.

**L17.** charge needs self; from_record receives cls; valid_duration receives no
implicit object. cls(...) preserves the called class for alternative constructors.
A method with no self slot called through an instance raises TypeError because
an object is supplied automatically. Annotations alone do not validate values.

**L18.** Initial output 10. paid() -> TypeError; assigning paid -> AttributeError;
__pin -> AttributeError; _Wallet__pin -> 'demo'; direct _paid assignment succeeds
and bypasses validation; assigning pay's result makes w None (when independently
starting with the original wallet). `_` is a convention; `__` mangles the name
to reduce accidental collisions, not to secure information. Properties can compute
fresh results on each read without exposing a setter.

**L19.** 1, then Changed. The list copy is separate, the booking is shared.
Reports holding the same Shift observe its current state. A Shift has many
Bookings; a Report uses one Shift. Independent parallel lists can lose alignment
when only one changes. A global registry mixes shifts and cannot own each shift's
label/invariants. Deeper containers can ask their immediate children for totals.

**L20.** After -8 and -3: n=2, total=-11, min=-8, max=-3, mean=-5.5.
Initialize extrema to None and special-case the first add. A MeanModel stores
mean_ in fit; fit returns self for chaining. Guard an empty training list with
ValueError; predict before fit should raise a clear error (or AttributeError in
the minimal slide pattern). predict repeats mean_ n times. This revises a
stateful class and a library interface, not a predictive model's validity.

**L21.** Mean of means =60; correct overall mean=(30*1+90*3)/4=75. Empty overall
count gives None. For [0,2,3]: any=True, all=False, sum=5, min=0, max=3,
reversed=[3,2,0]; abs(-3)=3; pow(2,3)=8; round(2.5)=2. max with a key function
returns the original element with the largest key. Sorted set output has a
defined order. Sum per-booking due, not total charges minus total payments when
overpayments are allowed.

**L22.** greet returns the global Binh; use self.player. A misspelled attribute
silently creates a second field; fix the spelling and use vars to inspect.
sort returns None; call it without assigning, or use sorted. VIPGuest lacks
player; reading it raises AttributeError. Parent initialization (for example
super().__init__(player)) establishes inherited state. Overriding replaces a
method for the subtype. Containment models the Shift relationship. This brief
inheritance preview does not imply a requirement to learn the absent Bài 9 tonight.

**L23.** An HTML sharing/login page is not the raw file, even with successful
transport. The supplied slides distinguish GitHub raw links from blob pages and
discuss Drive public access/download links with confirmation limitations.
Treat those as lecture examples rather than a guarantee that any particular URL
works now. Cache a snapshot locally, retain source/date, and inspect content before
parsing. Never store secret-bearing URLs in source. pd.read_csv can read a URL;
shape gives rows/columns and head previews initial rows. This assignment exercises
the decode/parse/cache concepts locally, without external dependencies.

**L24.** Explain your own implementation, not a memorized answer. Tariffs belong
in config; formatting in Report; row validation in normalize_row. Shift length
comes from contained bookings, independent of a process-wide construction count.
The standalone code on Bài 3 PDF page 10 prints `True` for id(a)==id(b), then
`False False` for a==c and a is c. The slide prints True False for the second
line, inconsistent with the displayed a=[1,2,3]. An earlier append would make
value equality true, but that append is absent from this standalone snippet.
Trust a fresh trace and the actual code rather than importing invisible state.
