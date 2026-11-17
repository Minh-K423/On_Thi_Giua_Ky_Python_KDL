# NightShift prediction lab

Write **output or exception type, reason, smallest repair** before running a
snippet. Each snippet is independent unless stated otherwise. Use a scratch
`revision_notes.md` or `scratch.py` here. Do not paste intentionally broken code
into the main application. Spend roughly 2-3 minutes per numbered exercise;
unfinished explanations are more valuable to revisit than extra interface polish.

## L01 — Explain your environment (during R0)

In one sentence each, distinguish Python, CPython and an environment; explain
bytecode and `__pycache__`. Match REPL, script, IPython and Jupyter to a use case.
Why `python -m pip`? What do `sys.executable` and `sys.prefix` tell you? Explain
venv/pip vs conda vs uv, version pinning, and why raw data is kept separately.

Assign each name its role, without installing it: NumPy, pandas, re, Matplotlib,
seaborn, SciPy, scikit-learn, requests, BeautifulSoup, sqlite3, Git, Ruff.
Explain why these introductions are not a demand to build a machine-learning
system tonight. Locate the version of your interpreter, then inspect
`help(str.split)` and `dir(str)` locally.

## L02 — Notebook state and readable scripts (during R0)

Notebook: execute cell 1 `x = 10`, cell 2 `print(x * 2)`, then change and execute
cell 1 to `x = 'ten'`, leaving cell 2 untouched. What is displayed? What happens
after Restart and Run All? Why can an output be stale without an exception?

Explain the difference between entering `2 + 2` in a REPL and in a `.py` file.
Write a two-line f-string receipt using `\n`, `\t`, `sep`, `end`, `:.2f`, `:,`,
`:.1%`, and one alignment width. Use 4-space indentation, snake_case, CapWords,
UPPER_CASE constants, grouped imports and a short docstring. Distinguish a comment
from a docstring. Explain the role of `if __name__ == '__main__'`.

## L03 — Numbers, types and truth

Predict each expression independently:

```python
"9" > "31", 9 > 31
int(3.9), int(-3.9), round(2.5), round(3.5)
bool("0"), bool([0]), bool([]), bool(None)
7 / 2, 7 // 2, 7 % 2, 2 ** 3 ** 2, divmod(7, 2)
0.1 + 0.2 == 0.3
int("8.5")
```

Repair the last two appropriately for a numeric analysis. Why would converting
`"8.5"` through float be the **wrong** repair for NightShift's integer minutes?
Does `x = 1; x = 'one'` change the type of the integer object or rebind the name?

## L04 — Three copies and two meanings of equality

```python
import copy
a = {"tags": ["solo"]}
b = a
c = a.copy()
d = copy.deepcopy(a)
b["tags"].append("ranked")
print(a == c, a is c, a["tags"] is c["tags"])
print(c["tags"], d["tags"])
```

Now predict separately: `x=[1]; y=x; y += [2]; print(x)` and
`x='a'; y=x; y += 'b'; print(x)`. Which operation mutates, which rebinds?
When is `.copy()` sufficient? What extra work does `deepcopy` do?

## L05 — Mutable default vs caller-owned data

```python
def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags

print(add_tag("solo"))
print(add_tag("ranked"))
```

Repair the default. Then distinguish two valid APIs: one intentionally modifies
a caller's supplied list, the other always returns an independent flat list.
Why does using `None` fix defaults but not automatically copy supplied lists?

## L06 — Conditions and match traps

Predict these independent snippets and repair the surprising ones:

```python
zone = "VR"
if zone == "PC" or "CONSOLE":
    print("cheap")

due = 25000
if due > 0:
    print("follow_up")
elif due >= 20000:
    print("urgent")

paid = 0
print("known" if paid else "missing")

LIMIT = 300
match 99:
    case LIMIT:
        print(LIMIT)
```

Write one sequence match for `['find', 'B004']`, an alternative pattern for
`q`/`quit`, a guarded pattern, and a wildcard. When is if clearer than match?

## L07 — Loop mechanics

```python
values = [8, 3, 9, 2, 4, 7]
for value in values:
    if value < 5:
        values.remove(value)
print(values)
print(list(zip(["A", "B", "C"], [10, 20])))
print(list(range(5, 0, -2)))
for i in range(2):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

Repair the deletion loop using a fresh list. Explain continue vs break, the
shortest-input rule of zip, and why break only exits the inner loop. Show a
terminating while loop which raises 1 by factors of 3 until it exceeds 100.

## L08 — Five patterns from a sentence

For `[('A', 'PC', -8), ('B', 'VR', -3), ('C', 'PC', -5)]`, write pseudocode for
counting, accumulating, filtering, finding the largest value **with its ID**, and
grouping by zone. What breaks if the largest-value accumulator starts at zero?
What should your function return for no records? Why initialize outside the loop?
Before coding, state: input iterable, output shape, remembered state, loop pattern.

## L09 — Read the whole signature

```python
def audit(first, /, label="INFO", *items, urgent=False, **details):
    return first, label, items, urgent, details

print(audit("B001", "WARN", 1, 2, urgent=True, line=4))
```

Which calls fail, and how: `audit(first='B001')`,
`audit('B001', 'WARN', label='INFO')`, `audit()`?
Explain `*args` as a tuple and `**kwargs` as a dictionary. Demonstrate unpacking
`args=('B001','WARN')` and `options={'urgent':True}` into a call.
For `def f(x, *, title=''): ...`, classify `f(1, 'a')`, `f(1, title='a')`, and
`f(x=1, 2)` (the last must be analyzed on paper, not pasted into a working file).

## L10 — LEGB and annotation limits

```python
count = 0
def bump():
    count = count + 1
bump()
```

Explain the exception; repair using parameters and return, without global.
Then trace a nested function reading `label` when local, enclosing and global
versions exist. Why does `sum=10; sum([1,2])` fail? Does `def f(x: int) -> int:
return x` prevent `f('hello')`? Why can list.append affect a caller even without
global or return? Explain rebinding separately from mutation.

## L11 — Strings and containers speed round

```python
s = " VR|solo "
s.strip()
print(repr(s), s[1:3], s[-1], "solo" in s)
print("banana".find("na"), "banana".count("a"))
print("B001".startswith("B"), "PC".replace("P", "D"))
t = ([1], "VR")
t[0].append(2)
print(t)
```

Which of `s[0]='x'` and `t[1]='PC'` fails? Why can a tuple contain a mutable list?
Try list append/insert/remove/pop on a scratch list; explain their mutation and
return behavior. Contrast `sorted(values)` with `values.sort()`.
For `d={'PC':2}`, contrast `d['VR']`, `d.get('VR',0)`, `d.keys()`, `d.values()` and
`d.items()`. Predict `{'solo','ranked'} & {'ranked','party'}`, union, and difference.
Give a list, set and dict comprehension for the tags `['solo','party','solo']`.

## L12 — Return, modules and decomposition

```python
def bill():
    print(40000)

result = bill()
print(result)
```

Repair it so another function can add tax, without printing during calculation.
Explain `return low, high, mean` and tuple unpacking. Split “read data, clean it,
sum debts, print table” into functions with input/output contracts. Which functions
should mutate? Compare `import src.analysis`, `from src.analysis import charge_for`,
and `import statistics as st`; explain why star-imports obscure names.

## L13 — Read the exception, preserve the evidence

Match these examples to exception types and a useful response:

```text
float('absent')        int('8.5')         1 / 0
[][0]                 {}['zone']        unknown_name
'paid: ' + 20         a missing file    invalid UTF-8 bytes
writing a locked file                  a missing object attribute
an unindented body after if             a missing colon after if
```

Why is `except: pass` dangerous around `row['paidd_vnd']`? Where should R2 catch
ValueError? Why should a misspelled dictionary key still be visible? Explain
Path.cwd vs a path anchored to `__file__`. Inspect Path.name/stem/suffix/parent,
exists and mkdir. Contrast read/read_text, line iteration, r/w/a and automatic
closing by with. Do not actually lock files or modify raw data for this exercise.

## L14 — CSV, JSON and encodings

Use `data/raw/bookings.csv`: explain why the first header needs utf-8-sig and
why `Alex, Jr.` defeats split(','). Why use newline='' for csv? Convert the local
`api_snapshot.json` from bytes to text to a Python object using explicit UTF-8.
Then serialize it with ensure_ascii=False and indent=2 to a scratch output here.

Predict `json.dumps({'day': date(2026, 11, 17)})` after importing date/json.
Repair it with an ISO date string. What are dumps/loads vs dump/load?
Predict `len('ễ')` vs `len('ễ'.encode('utf-8'))`; distinguish encode from decode.
Write one list, one set and one dict comprehension from accepted bookings.
Explain why complex nested comprehensions can be less readable than loops.

## L15 — self and object construction

```python
class Counter:
    def __init__(self):
        self.n = 0
    def bump(self):
        self.n += 1
        return self.n

x = Counter()
y = Counter()
z = x
x.bump()
z.bump()
y.bump()
print(x.n, y.n, z.n, x.bump())
```

Rewrite a bound call as `Counter.bump(x)`. Inspect type(x.bump) vs
type(Counter.bump), vars(x), and isinstance. Does __init__ create the object or
initialize it? What does it return? Explain the illustrative two steps
`object.__new__(Counter)` then `Counter.__init__(obj)`. Why is self a convention,
not a keyword? Why do distinct plain class instances usually compare unequal?

## L16 — Class attributes: read and write differ

```python
class Desk:
    limit = 3
    visits = 0
    tags = []
    def visit(self):
        self.visits += 1
        self.tags.append("seen")

a, b = Desk(), Desk()
a.visit()
a.limit = 8
Desk.limit = 5
print(a.limit, b.limit, Desk.limit)
print(a.visits, b.visits, Desk.visits, b.tags)
del a.limit
print(a.limit)
```

Repair the shared list and the shared counter separately. Explain why += on an
integer and append on a shared list have different effects here. Which attributes
appear in vars(a)? How does this relate to Booking.created_count?

## L17 — Three method kinds

Using Booking, name one method that needs self, one that needs cls, and one that
needs neither. Show the implicit argument for each call. Why return cls(...) from
from_record rather than hard-coding Booking(...)? What happens if a normal
instance method is defined with zero parameters? Does type information validate
the values automatically? Demonstrate two independent objects.

## L18 — Encapsulation and property traps

```python
class Wallet:
    def __init__(self):
        self._paid = 0
        self.__pin = "demo"
    @property
    def paid(self):
        return self._paid
    def pay(self, amount):
        if amount < 0:
            raise ValueError("negative payment")
        self._paid += amount

w = Wallet()
w.pay(10)
print(w.paid)
```

Analyze independently: `w.paid()`, `w.paid=99`, `w.__pin`, `w._Wallet__pin`,
`w._paid=-1`, and `w=w.pay(5)`. Which are errors, which bypass a convention?
Why does `_name` not enforce privacy? Why is name mangling not security?

## L19 — Composition and shallow boundaries

After implementing R4:

```python
shift = Shift("A")
booking = Booking.from_record(record)  # record is a valid normalized dict
shift.add(booking)
copy_of_list = shift.bookings()
copy_of_list.clear()
print(len(shift.bookings()))
shift.bookings()[0].player = "Changed"
print(booking.player)
```

Explain contains-many vs contains-one vs uses. If two Report objects receive the
same Shift, what happens when a booking changes? Draw references rather than boxes
holding duplicated data. Why can parallel ID/minutes lists silently become
misaligned? Why is a global list of all bookings not a substitute for a Shift?

## L20 — State over time, and fit/predict

Sketch a RunningStats with n, total, minimum, maximum, add(x), mean(). Empty mean
and extrema are None; adding -8 then -3 gives what? Why is zero a bad initial
maximum? Sketch a MeanModel with fit(values) storing mean_ and returning self,
then predict(n) repeating mean_. What if predict is called before fit, or fit
gets an empty list? Contrast fit returning self with Shift.add returning None.
No scikit-learn package is needed: this is its interface shape, not ML training.

## L21 — Aggregation and built-ins

Zone A has one session lasting 30 minutes. Zone B has three lasting 90 minutes
each. Compare the average of zone means to the overall session mean. Write the
correct weighted formula. Explain the empty case and the need for counts.
For `[0, 2, 3]`, predict any/all, sum/min/max, list(reversed(...)), abs(-3),
pow(2,3), and round(2.5). Use max(..., key=...) to recover a booking, not just a
number. Explain why sorting a set before displaying it makes results reproducible.

## L22 — Four silent OOP bugs and the inheritance preview

Find the smallest repair for each:

```python
# A: global name accidentally hides a missing self
player = "Binh"
class Guest:
    def __init__(self, player):
        self.player = player
    def greet(self):
        return player

# B: typo creates a new attribute
guest = Guest("An")
guest.palyer = "Chi"

# C: mutation method result assigned back
numbers = [3, 1]
numbers = numbers.sort()

# D: next-lesson preview from the end of Bài 8
class VIPGuest(Guest):
    def __init__(self, player, badge):
        self.badge = badge
```

What happens when reading VIPGuest('An','gold').player? What does calling the
parent initializer fix? Explain overriding a report method, and why a Shift
**has bookings**, rather than **is a Booking**. This is recognition only;
inheritance/polymorphism in depth are announced for the next, unsupplied lesson.

## L23 — Review network ingestion without going online

Read the supplied `fake_download.html` locally. Why might a browser share link
return this instead of CSV? Describe the slide's GitHub blob-page vs raw-file
distinction and Drive sharing/download-link idea, including login/confirmation
pages. A successful download does not prove the content is your dataset.

On paper, trace `if not path.exists(): path.write_bytes(fetch(url))`, then a local
read. State how to record source/date and keep keys out of source. Explain
urllib's bytes + decode + json.loads, and pandas.read_csv(URL), shape and head
at the recognition level used in Bài 6. Use the supplied local snapshot for any
actual decoding; no connection or download is necessary for this assignment.

## L24 — Defend your finished program

Without opening code, explain the route from raw row to bill to report, and where
each validation happens. Name one mutation that is intended and one that must
not occur. Explain one case where shallow copying suffices and one where it
does not. Why can test code construct 100 Bookings without the shift count being
100? Where would you change the tariff, report formatting, or CSV validation?

Finally, inspect `Bai03_Bien_va_mo_hinh_doi_tuong.pdf`, PDF page 10: the shown code
has `a=[1,2,3]`, `b=a`, `c=[1,2,3,4]`, then prints `a==c, a is c`. Predict the
actual output. Is the printed answer on that slide consistent with this standalone
code? Test a fresh snippet rather than inheriting an earlier slide's hidden state.
