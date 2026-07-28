# 📋 Lab02 Cheat Sheet — Decisions, Loops, Functions & Files

**The Cozy Bean · M1-W1-Lab02 · Apeiron AI Training Academy**

*Everything from Lab02 on one page. Print it and keep it next to [Lab01's cheat sheet](../Lab01/CHEATSHEET.md) — you need both.*

---

## Running things

```text
python scripts/04_morning_checklist.py     # Windows and Mac, same command
py scripts/04_morning_checklist.py         # Windows fallback
python3 scripts/04_morning_checklist.py    # Mac fallback
pwd                                        # which folder am I standing in?
ls                                         # what is in here? (must show data/)
```

> ⚠️ **Always run from your `Lab02` folder** (`AperionAI/Module1/Week1/Lab02`). File paths like `data/orders.txt` are relative to where you are standing.
> **Ctrl+C** stops a runaway program.

---

## Decisions

```python
if cups >= 10:
    print("Big order -- free cookie!")
elif cups >= 5:
    print("Medium order -- thank you!")
else:
    print("Small order -- enjoy!")
```

- The colon `:` promises an indented block.
- **The FIRST True condition wins** — the rest are never checked.
- Put the most specific rule first, or it becomes unreachable.
- One `=` fills a jar; two `==` asks a question.

---

## Indentation IS the grammar

```python
if True:
    print("inside the if")     # 4 spaces = belongs to the if
print("outside the if")        # no spaces = runs regardless
```

| Error | Cause |
|---|---|
| `IndentationError: expected an indented block after 'if' statement on line 1` | you forgot to indent after the colon |
| `IndentationError: unindent does not match any outer indentation level` | mixed tabs and spaces, or uneven indents |

**Use 4 spaces. Never mix tabs and spaces.**

---

## Loops

**Over a list** — once per item:

```python
for customer in ["Sara", "Ben"]:
    print("Now serving:", customer)
```

**A fixed number of times** — `range(5)` gives 0,1,2,3,4:

```python
for i in range(5):
    print("Stamp number:", i)      # use i + 1 to count like a human
```

**Until something changes** — when you do not know how many:

```python
cups = 0
while cups < 5:
    print(cups)
    cups += 1        # SOMETHING must move towards False, or it never ends
```

**Stopping early:**

```python
for customer in queue:
    if customer == "Aisha":
        break        # leaves the loop immediately
    print("Served:", customer)
```

| Use | When |
|---|---|
| `for` | you know what you are looping over |
| `while` | you only know when to stop |
| `break` | you need to leave early |

`count += 1` means "add 1 to count". Also works: `-=`, `*=`.

---

## Functions — laminated recipe cards

```python
def greet_customer(name):          # name is the PARAMETER (the blank)
    print("Good morning,", name)

greet_customer("Sara")             # CALLING it. Writing it does nothing.
```

**Handing a value back:**

```python
def latte_price(cups):
    return cups * 3.50

two = latte_price(2)               # 7.0, caught in a jar
print(latte_price(5))              # 17.5, used straight away
```

| | Does |
|---|---|
| `print` | shows it on screen; then it is gone |
| `return` | hands the value back so you can **store and reuse** it |

More than one blank is fine: `def add_numbers(a, b): return a + b`

---

## Built-in functions (they came with Python)

```python
print(...)          # show something
len(my_list)        # how many items
type(value)         # what kind of thing
max(3.5, 2.75)      # the biggest
range(5)            # 0,1,2,3,4
```

> ⚠️ Never name a variable `max`, `len`, `type`, `list`, `str` or `print` — it hides the built-in.

---

## Files — the order notebook

**Writing** (`with` closes it for you):

```python
with open("data/report.txt", "w") as f:
    f.write("Cups sold: 63\n")      # the \n is NOT optional
```

**Reading, line by line** — the usual way:

```python
file = open("data/orders.txt", "r")
for line in file:
    print(line.strip())             # strip trims the invisible newline
file.close()
```

**The three modes:**

| Mode | Means | Careful |
|---|---|---|
| `"r"` | read (default) | look, do not touch |
| `"w"` | write | ⚠️ **ERASES the file first** |
| `"a"` | append | adds to the end, keeps what is there |

**The four ways to read:**

| Method | Hands back |
|---|---|
| `f.read()` | the whole file as one piece of text |
| `f.readline()` | the next single line |
| `f.readlines()` | a list of all the lines |
| `for line in f` | one line at a time — **the usual choice** |

> 🐛 **The classic bug:** `.write()` adds nothing you did not ask for. Three writes with no `\n` become one smooshed line. `print` starts new lines for you; `.write()` never does.

---

## Splitting and joining

```python
"latte with oat milk".split()        # ['latte', 'with', 'oat', 'milk']
"latte,3.50".split(",")              # ['latte', '3.50']   <- still TEXT!
float("3.50")                        # 3.5                 <- now a number

", ".join(["latte", "muffin"])       # 'latte, muffin'     <- glue goes FIRST
```

**The standard file-parsing recipe:**

```python
for line in open("data/menu_prices.txt", "r"):
    parts = line.strip().split(",")      # strip FIRST, then split
    name = parts[0]
    price = float(parts[1])              # convert before doing maths
```

---

## Errors you have met in this lab

| Error | Means | Typical cause |
|---|---|---|
| `IndentationError` | spacing is wrong | forgot to indent after a colon |
| `FileNotFoundError` | no such file here | **running from the wrong folder** |
| `SyntaxError` | grammar typo | `=` instead of `==` in an `if` |
| `TypeError` | wrong kind of thing | doing maths on a piece that is still text |

> **Read the LAST line of an error first.** For `FileNotFoundError`, check `pwd` before anything else.

---

## 🚀 Bonus — beyond class

```python
name = input("Customer name? ")     # pauses and waits; hands back TEXT
print(f"Total: ${price:.2f}")       # money with 2 decimals -> $4.00
```
