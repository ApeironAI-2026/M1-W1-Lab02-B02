# ☕ M1-W1-Lab02 — The Cozy Bean Gets Busy

### Decisions, Loops, Recipe Cards & the Order Notebook
**Apeiron AI Training Academy** · *"Boundless Possibilities, Infinite Potential"*

| | |
|---|---|
| **Module** | M1: AI/ML Fundamentals |
| **Week** | Week 1 |
| **Lab** | Lab02 — The Cozy Bean Gets Busy |
| **Duration** | **≈ 3 hours 45 minutes** of lab work (setup not counted) |
| **Difficulty** | ⭐ Absolute Beginner — continues directly from Lab01 |

> 🛋️ **Split this across two or three sittings.** A natural break is after Cluster C (recipe cards), when you have decisions, loops and functions under your belt and file work is still ahead.

### What you learned in class (and will now make your own)

`if` / `elif` / `else` · why indentation is the grammar · `for` loops · `range()` · `while` loops · `break` · functions with `def`, parameters and `return` · built-in functions · running `.py` files from a terminal · writing files · reading files · file modes `r`/`w`/`a` · `split()` and `join()` · two capstone exercises from class

---

## 1. ☕ The Story

Three weeks have gone by, and something wonderful and slightly terrifying has happened: **The Cozy Bean got popular.**

There is a queue out of the door by 8 a.m. The wobbly third table has a permanent occupant who writes novels. You have hired three baristas — **Sara**, **Ben** and **Aisha** — and last Tuesday you charged someone the wrong price twice because you were making four drinks and answering the phone.

That is the moment every small business hits: the point where doing everything *personally* stops working. You cannot stand at the till deciding each individual price. You cannot greet each customer with a separately typed sentence. And you certainly cannot remember Tuesday's takings on Wednesday.

So this week you stop *doing* and start **writing things down that do themselves**:

- **Rules** the baristas follow without asking you — `if` a customer orders 10 or more cups, they get a free cookie.
- **Loops** that handle the whole queue, whether it is four people or four hundred, without you writing a line per person.
- **Recipe cards** — write the latte recipe once, laminate it, use it forever.
- An **order notebook** the shop writes to at closing and reads back the next morning. Your shop gets a memory.

In Lab01 you taught Python what your shop *has*. This week you teach it what your shop *does*.

### Why this matters in real life (and in AI/ML)

- **Every model is a very large decision rule.** The `if` / `elif` chain you write in STEP 3 is the same shape as the final decision a trained classifier makes — just with fewer branches and better manners.
- **Training a model is a loop.** "For each example, look, adjust, repeat" is a `for` loop. The one you write in STEP 4 is that loop, with a shorter queue.
- **Every dataset you ever load is a file being read.** `for line in file` is where all data work genuinely begins, before any library gets involved.

### ✅ Success Criteria — what you will be able to produce

- `python scripts/01_decision_rules.py` — rules that pick their own answer
- `python scripts/02_serving_the_line.py` — a whole queue served by four lines of code
- `python scripts/03_recipe_cards.py` — functions you wrote, called more than once
- `python scripts/04_morning_checklist.py` — a real opening checklist you could genuinely use
- `python scripts/05_order_notebook.py` — files your program writes and reads back
- `python scripts/06_order_slips.py` — an order slip torn into pieces and priced
- …plus eight practice problems, **including two capstones** rebuilt from the class exercises.

---

## 2. 🎯 Learning Objectives

By the end of this lab you will be able to:

1. Make a program choose between paths with `if`, `elif` and `else`.
2. Explain why **indentation is Python's grammar**, and fix an `IndentationError`.
3. Repeat work with a `for` loop, over both a list and a `range()`.
4. Use a `while` loop when you do not know the number of repeats in advance, and stop early with `break`.
5. Write your own **functions** with `def`, hand them **parameters**, and get answers back with `return`.
6. Recognise the **built-in functions** you have been using all along.
7. Run a `.py` script from a terminal on Windows or Mac, and say how a script differs from a notebook.
8. **Write** to a file and **read** it back, using the right mode — and explain why `\n` matters.
9. Tear a line of text into pieces with `split()`, convert those pieces, and staple them back with `join()`.
10. Complete both capstones: find the biggest order of the day, and report every barista's shift hours.

---

## 3. 🔧 Before You Start

> ### ⚡ Already cloned and set up? Then you are two clicks away.
>
> 1. **File → Open Folder…** and choose your **`Lab02`** folder (the one holding this document, at `AperionAI/Module1/Week1/Lab02`).
> 2. **Terminal → New Terminal.**
>
> That is it — skip to the walkthrough.
>
> **Not cloned this lab yet?** This is a **separate repo** from Lab01. The [README](README.md#1--get-this-repo-onto-your-computer) shows you how: click the GitHub Classroom link from Google Classroom, copy your own repo address, and clone it into `AperionAI/Module1/Week1/Lab02` — right next to `Lab01`.
>
> **Never done the Python/VS Code setup at all?** [Lab01's setup section](../Lab01/README.md#2--set-up-python-and-vs-code) walks you through installing Python, opening VS Code and a terminal, and saving files. Do that once, then come back here.

### 3.1 Two things are different in this lab

**① There is a `data/` folder now.** It ships with three small text files:

| File | What it holds |
|---|---|
| `data/orders.txt` | the day's orders, one per line |
| `data/shift_hours.txt` | each barista's id, name and five days of hours |
| `data/menu_prices.txt` | drink names and prices, comma-separated |

You never create these — they are already there. Some scripts will *add* new files to that folder (`sample.txt`, `sample_fixed.txt`, `end_of_day.txt`, `my_report.txt`). That is Python creating them for you, and it is safe to run those scripts as many times as you like.

**② Being in the right folder now really matters.** In Lab01 a wrong folder meant "file not found". Here, your scripts open files by a path written relative to the lab folder — `open("data/orders.txt")` means *"the data folder, in the room I am standing in"*. Stand in the wrong room and there is no `data` folder to find.

### 3.2 Confirm you are in the right room

```text
pwd
```

The answer must end in **`Week1/Lab02`** — Windows shows it with backslashes, `...\Week1\Lab02`. Then check the furniture:

```text
ls
```

You should see at least `README.md`, `M1-W1-Lab02.md`, `CHEATSHEET.md`, `GLOSSARY.md`, `data`, `scripts`, `practice` and `solutions`. **If you cannot see `data`, you are in the wrong room** — use **File → Open Folder** on your `Lab02` folder and open a fresh terminal.

Now try it for real:

```text
python scripts/04_morning_checklist.py
```

```text
=== THE COZY BEAN -- OPENING CHECKLIST ===
1 - Unlock the front door
2 - Switch on the coffee machine
3 - Put the OPEN sign up
4 - Count the float in the till
5 - Bake the first tray of muffins
Muffin tray: full. Good to open!
=== Ready to open. Have a lovely day. ===
```

> ### ⚠️ The unsaved-file trap, again
>
> **Changed the code but the output didn't change? You probably didn't save — look for the dot on the file tab, press Ctrl+S / Cmd+S, and rerun.**
>
> It catches everyone. Check it first, every time.

### 3.3 "If you see this error, do this"

| What you see | What it means | What to do |
|---|---|---|
| `FileNotFoundError: [Errno 2] No such file or directory: 'data/orders.txt'` | **You are running from the wrong folder.** Python looked for a `data` folder in the room it is standing in and found none. | Type `pwd`. Does it end in `Lab02`? If not, **File → Open Folder** on your `Lab02` folder, then **Terminal → New Terminal**. Confirm with `ls` that you can see `data`. |
| `IndentationError` | Spacing at the start of a line is wrong. | See STEP 2 — this one gets a whole lesson. |
| `'python' is not recognized…` | Windows cannot find Python. | Try `py scripts/04_morning_checklist.py`. |
| `command not found: python` (Mac) | Mac calls it `python3`. | Use `python3 scripts/04_morning_checklist.py`. |
| Program seems frozen, cursor blinking | It is one of the 🚀 bonus scripts, waiting for you to type. | Type an answer, press Enter. That pause is the program being polite. |
| Output did not change after an edit | The file was never saved. | Ctrl+S / Cmd+S, rerun. |

---

## 4. 📖 Guided Walkthrough

Seventeen steps in six groups. Same rhythm as Lab01: read the STEP, run the script, compare to the 📺 block, do the 🎤 tweak.

---

## ☕ Cluster A — Barista Decision Rules

*Script for this cluster:* **`scripts/01_decision_rules.py`**

Your baristas need rules they can follow without asking you. That is all an `if` statement is.

---

### STEP 1 — The first rule: if / else

▶ *In your script:* Section 1 of `scripts/01_decision_rules.py`

🎯 **Objective:** Make a program choose between two paths.

☕ **Story moment:** The oat milk has run out. Ben does not need to phone you about it — he needs a rule: *if there is no oat milk, offer almond; otherwise, make the oat latte.* You are about to write your first rule that the shop follows on its own.

🧠 **The idea in plain English:** `if` asks a True/False question. The **indented** lines below it run **only** when the answer is True. `else` catches every other case. Note the colon `:` at the end of the `if` line — that colon means *"here comes the block."*

💻 **The code:**

```python
oat_milk_left = 0

if oat_milk_left == 0:
    print("Sorry, we're out of oat milk today -- almond instead?")
else:
    print("One oat latte coming right up!")
```

📺 **Expected output:**

```text
Sorry, we're out of oat milk today -- almond instead?
```

⚠️ **Common mistake:** Writing `=` instead of `==`. `if oat_milk_left = 0:` is a `SyntaxError` — one `=` fills a jar, two `==` asks a question. Python catches this one for you, which is a small mercy.

✅ **Verify:** One line — the "out of oat milk" one. Only **one** branch ever runs; that is the point of a decision.

🎤 **Try it yourself (30 seconds):** Change `oat_milk_left` to `5`, save, rerun. The other line prints instead. Same code, different world.

> 📌 **You saw this in class:**
>
> ```python
> age = 20
>
> if age < 18:
>     print("You are a minor")
> elif age < 65:
>     print("You are an adult")
> else:
>     print("You are a senior")
> ```
>
> ```text
> You are an adult
> ```

---

### STEP 2 — Indentation IS the grammar

▶ *In your script:* Section 2 of `scripts/01_decision_rules.py`

🎯 **Objective:** Understand why the spaces at the start of a line are part of the language — and fix the error when they are wrong.

☕ **Story moment:** Look at any recipe card in your shop. Under "if they want it iced", the sub-steps are indented underneath. The indent is what tells you which steps belong to that decision. Python uses the exact same convention — except Python is not being tidy, it is *reading* those spaces.

🧠 **The idea in plain English:** Most languages use curly brackets to say what belongs together. **Python uses indentation.** Those 4 spaces are not decoration — they are how Python knows which lines belong to the `if`. Get them wrong and Python genuinely cannot understand you, so it stops.

💻 **The broken code** (commented out in your script so it still runs):

```python
if oat_milk_left == 0:
print("out of oat milk")
```

📺 **Expected output** — a real error, captured by running exactly this:

```text
  File "your_file.py", line 2
    print("out of oat milk")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 1
```

**Translated into plain English:** *"You promised me a block with that colon, then gave me a line that is not indented. I do not know what belongs to the `if`."* Notice how specific it is: it even names the line the `if` was on.

**The fix** is simply to indent it:

```python
if oat_milk_left == 0:
    print("out of oat milk")
```

⚠️ **Common mistake:** Mixing tabs and spaces. They look identical on screen and Python treats them differently, producing `IndentationError: unindent does not match any outer indentation level` — an error that seems mad because the code *looks* right. **Use 4 spaces, always.** VS Code does this automatically when you press Tab.

✅ **Verify:** Your script runs clean with those lines commented out. Uncomment them to meet the error, then comment them back.

🎤 **Try it yourself (30 seconds):** In a scratch copy, take a working `if` and delete the 4 spaces in front of its indented line. Save, run, read the error, put them back. Deliberately breaking things is how you stop fearing them.

---

### STEP 3 — A chain of rules with elif

▶ *In your script:* Section 3 of `scripts/01_decision_rules.py`

🎯 **Objective:** Chain several conditions, and learn that the **first True one wins**.

☕ **Story moment:** Orders are not just big or small — there is a middle. Big orders get a cookie, medium orders get a warm thank-you, small orders get a smile. Three outcomes, one rule sheet, checked top to bottom.

🧠 **The idea in plain English:** `elif` is short for *"else, if"*. Python checks each condition in order from the top and **stops at the very first one that is True** — every condition after it is skipped entirely, even if it would also be True. That is the single most important thing to know about chains.

💻 **The code:**

```python
cups = 9

if cups >= 10:
    print("Big order -- free cookie!")
elif cups >= 5:
    print("Medium order -- thank you!")
else:
    print("Small order -- enjoy!")
```

📺 **Expected output:**

```text
Medium order -- thank you!
```

⚠️ **Common mistake:** Putting the rules in the wrong order. If you check `cups >= 5` first, an order of 12 cups matches it and prints "Medium" — the free-cookie line becomes unreachable and nobody ever gets a cookie. **Most specific rule first.**

✅ **Verify:** Exactly one line. Nine cups is not ≥ 10, but it is ≥ 5.

🎤 **Try it yourself (30 seconds):** Set `cups = 12`, then `cups = 2`. Predict each answer before running it.

> 📌 **You saw this in class** — and this is the quiz your instructor asked. Here **all three** conditions are True (90 > 50, 90 > 40, 90 > 30). Which line prints?
>
> ```python
> x = 90
>
> if x > 50:
>     print("Condition 1 is True")
> elif x > 40:
>     print("Condition 2 is True")
> elif x > 30:
>     print("Condition 3 is True")
> else:
>     print("None are True")
> ```
>
> ```text
> Condition 1 is True
> ```
>
> **Only the first one.** Once a condition matches, Python leaves the chain entirely — it never even looks at the rest.

---

### 🧠 Quick Quiz #1 — answer from memory, before peeking

*(Answers are in the **Answer Key** at the end. No scrolling ahead.)*

**Q1.** In the `x = 90` chain above, more than one condition is True. Which line prints?

- A) The first True one only
- B) The last True one only
- C) Every True one runs
- D) None of them run

**Q2.** You forget to indent the line under an `if`. Which error appears?

- A) `SyntaxError`
- B) `NameError`
- C) `TypeError`
- D) `IndentationError`

**Q3.** In the class age example, with `age = 70`, what prints?

- A) `You are a minor`
- B) `You are a senior`
- C) `You are an adult`
- D) Nothing prints

---

## ☕ Cluster B — Serving the Line

*Script for this cluster:* **`scripts/02_serving_the_line.py`**

Four customers or four hundred — you are about to write code that does not care which.

---

### STEP 4 — Serve everyone with a for loop

▶ *In your script:* Section 1 of `scripts/02_serving_the_line.py`

🎯 **Objective:** Do the same thing to every item in a list.

☕ **Story moment:** Yesterday you greeted each customer with a separately typed line of code. Four customers, four lines. But what happens when there are forty? You need to say *"do this for each person in the queue"* — once.

🧠 **The idea in plain English:** A **for loop** takes each item in a list, one at a time, and runs the indented block once per item. The name right after `for` is a jar you invent — it holds the current item, refilled each time round. Same colon, same indentation as `if`.

💻 **The code:**

```python
queue = ["Sara", "Ben", "Aisha", "Marcus"]

for customer in queue:
    print("Now serving:", customer)
```

📺 **Expected output:**

```text
Now serving: Sara
Now serving: Ben
Now serving: Aisha
Now serving: Marcus
```

⚠️ **Common mistake:** Forgetting the indent on the loop body. An un-indented line is *outside* the loop, so it runs once at the end instead of once per customer — and no error appears to warn you. If a line prints once when you expected four, check your spaces.

✅ **Verify:** Four lines, one per customer, in queue order. **Three lines of code served four customers** — and the same three would serve four hundred.

🎤 **Try it yourself (30 seconds):** Add two more names to the queue. Rerun. You did not touch the loop, and it handled them anyway. That is the whole idea.

> 📌 **You saw this in class:**
>
> ```python
> fruits = ["apple", "banana", "orange", "mango"]
>
> for fruit in fruits:
>     print(fruit)
> ```
>
> ```text
> apple
> banana
> orange
> mango
> ```

---

### STEP 5 — Counting with range

▶ *In your script:* Section 2 of `scripts/02_serving_the_line.py`

🎯 **Objective:** Loop a fixed number of times.

☕ **Story moment:** The loyalty cards need five stamp boxes printed on them. There is no list of stamps to walk through — you just need to do something *five times*.

🧠 **The idea in plain English:** `range(5)` hands the loop the numbers **0, 1, 2, 3, 4** — starting at 0, stopping **before** 5. It is the same tool you met in Lab01 STEP 23, now doing what it was built for.

💻 **The code:**

```python
for i in range(5):
    print("Stamp number:", i)
```

📺 **Expected output:**

```text
Stamp number: 0
Stamp number: 1
Stamp number: 2
Stamp number: 3
Stamp number: 4
```

⚠️ **Common mistake:** Expecting it to count 1 to 5. It counts **0 to 4** — five numbers, starting at zero. When customers need to see 1–5, print `i + 1`.

✅ **Verify:** Five lines, numbered 0 through 4.

🎤 **Try it yourself (30 seconds):** Change it to `print("Stamp number:", i + 1)` so it counts the way a customer would.

---

### STEP 6 — Restocking with a while loop

▶ *In your script:* Section 3 of `scripts/02_serving_the_line.py`

🎯 **Objective:** Repeat until a condition stops being true.

☕ **Story moment:** You are restocking cups. How many trips to the storeroom will it take? You genuinely do not know — it depends what is on the shelf already. You cannot say "do this 4 times". You can only say: **keep going until the shelf is full.**

🧠 **The idea in plain English:** A `for` loop needs to know its list up front. A `while` loop just keeps repeating **as long as its question stays True**, checking again before each round. Use `for` when you know how many; use `while` when you know only when to stop.

The other essential piece: `count += 1` is shorthand for *"add one to this jar"*. **Something inside the loop must move the question towards False**, or the loop never ends.

💻 **The code:**

```python
cups_on_shelf = 0

while cups_on_shelf < 5:
    print("Restocking... cups on shelf:", cups_on_shelf)
    cups_on_shelf += 1

print("Shelf is full!")
```

📺 **Expected output:**

```text
Restocking... cups on shelf: 0
Restocking... cups on shelf: 1
Restocking... cups on shelf: 2
Restocking... cups on shelf: 3
Restocking... cups on shelf: 4
Shelf is full!
```

⚠️ **Common mistake:** Forgetting the `+= 1`. Then `cups_on_shelf` stays 0 forever, the question stays True forever, and your program prints until you stop it. This is called an **infinite loop**, and everybody writes one eventually. **Press Ctrl+C in the terminal to stop a runaway program.** Write that shortcut on your hand.

✅ **Verify:** Five restocking lines (0 to 4), then "Shelf is full!" once. It printed 5 times because the question turned False when the count reached 5.

🎤 **Try it yourself (30 seconds):** Change `< 5` to `< 3`. Predict how many lines you get before running it.

> 📌 **You saw this in class** — the same counter pattern, `count = 0` and `while count < 5`, running exactly **5** times.

---

### STEP 7 — The fire alarm (break)

▶ *In your script:* Section 4 of `scripts/02_serving_the_line.py`

🎯 **Objective:** Leave a loop early.

☕ **Story moment:** You are halfway down the queue when the fire alarm goes off. You do not finish serving the line. You stop, immediately, wherever you are.

🧠 **The idea in plain English:** `break` leaves the loop the instant it runs, no matter how many items are left. It almost always sits inside an `if`, because you need something to decide *when* to stop.

💻 **The code:**

```python
queue = ["Sara", "Ben", "Aisha", "Marcus"]

for customer in queue:
    if customer == "Aisha":
        print("FIRE ALARM -- everybody out!")
        break
    print("Served:", customer)
```

📺 **Expected output:**

```text
Served: Sara
Served: Ben
FIRE ALARM -- everybody out!
```

⚠️ **Common mistake:** Expecting Aisha to be served before the alarm. Look at the order: the `if` is checked *first*, so when Aisha comes up the alarm fires and `break` leaves immediately — the `print("Served:", ...)` line below never runs for her, and Marcus is never reached at all.

✅ **Verify:** Two served, then the alarm. Marcus does not appear — proof the loop really did stop early.

🎤 **Try it yourself (30 seconds):** Change `"Aisha"` to `"Marcus"`. Now three people get served before the alarm. Where a `break` sits changes everything.

---

### 🧠 Quick Quiz #2 — answer from memory, before peeking

**Q1.** `count = 0`, then `while count < 5:` with `count += 1` inside. How many times does the body run?

- A) `4`
- B) `5`
- C) `6`
- D) forever

**Q2.** What is the first number `for i in range(5)` gives you?

- A) `0`
- B) `1`
- C) `5`
- D) `-1`

**Q3.** What does `break` do?

- A) Skips to the next item in the loop
- B) Restarts the loop from the start
- C) Leaves the loop immediately
- D) Pauses the loop for a second

---

## ☕ Cluster C — Laminated Recipe Cards

*Script for this cluster:* **`scripts/03_recipe_cards.py`**

The most powerful idea in the lab: write it once, use it forever.

---

### STEP 8 — Write the card once, use it twice

▶ *In your script:* Section 1 of `scripts/03_recipe_cards.py`

🎯 **Objective:** Define a function with a parameter and call it more than once.

☕ **Story moment:** You are training Sara and Ben. Rather than explaining the greeting to each of them separately every morning, you write it on a card, laminate it, and hang it by the till. The card says: *"Good morning, [customer name]! What can I get you?"* — with a blank to fill in.

🧠 **The idea in plain English:** A **function** is a named block of instructions you write once and use as often as you like. `def` starts the card, then the name, then brackets holding the **parameter** — the blank on the card that gets filled in each time you use it. The indented lines are the instructions. Nothing happens when you *write* the card; it only runs when you **call** it by name.

💻 **The code:**

```python
def greet_customer(name):
    print("Good morning,", name + "! What can I get you?")

greet_customer("Sara")
greet_customer("Ben")
```

📺 **Expected output:**

```text
Good morning, Sara! What can I get you?
Good morning, Ben! What can I get you?
```

⚠️ **Common mistake:** Writing the card and never calling it. If your function definition produces no output, check you actually called it afterwards — writing a recipe is not the same as cooking.

✅ **Verify:** Two greetings, different names, **one** copy of the instructions. Change the wording on the card and both greetings change together — that is the payoff.

🎤 **Try it yourself (30 seconds):** Add `greet_customer("Aisha")`. One new line, no new instructions.

> 📌 **You saw this in class:**
>
> ```python
> def greet(name):
>     print("Hello", name)
>
> greet("Debela")
> greet("Memar")
> ```
>
> ```text
> Hello Debela
> Hello Memar
> ```

---

### STEP 9 — A card that hands something back

▶ *In your script:* Section 2 of `scripts/03_recipe_cards.py`

🎯 **Objective:** Use `return` and store the result.

☕ **Story moment:** The greeting card just *says* something. But a pricing card is different — you hand it a number of cups and it hands **a price back to you**, which you then put in the till, add to a total, or print on a receipt. It gives you something to hold.

🧠 **The idea in plain English:** `return` hands a value **back** to whoever called the function, instead of printing it. That is the crucial difference:

- **`print`** puts something on the screen. It is gone once you have read it.
- **`return`** hands a value back so you can **store it and use it later**.

💻 **The code:**

```python
def latte_price(cups):
    return cups * 3.50

two_lattes = latte_price(2)      # caught in a jar
print("Two lattes cost:", two_lattes)
print("Five lattes cost:", latte_price(5))
```

📺 **Expected output:**

```text
Two lattes cost: 7.0
Five lattes cost: 17.5
```

⚠️ **Common mistake:** Using `print` inside the function where you meant `return`. A function that prints looks like it works — until you try `total = latte_price(2) + latte_price(3)` and everything falls apart, because it handed back nothing. **If you need the answer later, `return` it.**

✅ **Verify:** `7.0` and `17.5`. The first was stored in a jar before printing; the second went straight into `print`. Both work.

🎤 **Try it yourself (30 seconds):** Add `print("Ten lattes cost:", latte_price(10))`. Then try storing two calls and adding them: `big = latte_price(2) + latte_price(3)`.

> 📌 **You saw this in class:**
>
> ```python
> def add_numbers(a, b):
>     return a + b
>
> result = add_numbers(5, 7)
> print("Result:", result)
> ```
>
> ```text
> Result: 12
> ```
>
> Two parameters this time — a card can have as many blanks as it needs.

---

### STEP 10 — The appliances that came with the shop

▶ *In your script:* Section 3 of `scripts/03_recipe_cards.py`

🎯 **Objective:** Recognise the built-in functions you have used all along.

☕ **Story moment:** When you took over the lease, the shop came with a fridge, an oven and a dishwasher already installed. You never bought them; you just started using them. Python is the same — and you have been using its appliances since your very first line.

🧠 **The idea in plain English:** A **built-in function** comes with Python. Nothing to install, nothing to write. You have already used five of them without noticing.

| Built-in | What it does | You met it in |
|---|---|---|
| `print()` | shows something on screen | Lab01 STEP 1 |
| `len()` | how many items | Lab01 STEP 20 |
| `type()` | what kind of thing is this | Lab01 STEP 6 |
| `range()` | a run of numbers | Lab01 STEP 23, and STEP 5 here |
| `max()` | the biggest of several values | right now |

💻 **The code:**

```python
todays_orders = ["latte", "espresso", "muffin"]

print(len(todays_orders))
print(type(todays_orders))
print(max(3.50, 2.75, 4.25))
print(list(range(3)))
```

📺 **Expected output:**

```text
3
<class 'list'>
4.25
[0, 1, 2]
```

⚠️ **Common mistake:** Naming your own jar after a built-in. Write `max = 10` and you have covered the appliance with a tea towel — `max(...)` then fails for the rest of the program. Avoid `max`, `len`, `type`, `list`, `print` and `str` as variable names.

✅ **Verify:** `3`, the type, `4.25`, and the range list.

🎤 **Try it yourself (30 seconds):** Find the priciest thing on your menu: `print(max(3.50, 2.75, 2.25, 4.00))`.

---

### 🧠 Quick Quiz #3 — answer from memory, before peeking

**Q1.** What is the difference between `return` and `print`?

- A) `return` hands a value back to be used; `print` only shows it
- B) `print` hands a value back to be used; `return` only shows it
- C) They do exactly the same thing
- D) `return` only works inside a loop

**Q2.** `greet("Debela")` then `greet("Memar")` — what prints?

- A) `Hello Debela` only, then nothing
- B) `Hello Memar` only, then nothing
- C) Nothing, as the card is only written
- D) `Hello Debela` then `Hello Memar`

**Q3.** Which of these are built-in functions: `len`, `latte`, `max`?

- A) `len` and `latte`
- B) `len` and `max`
- C) `latte` and `max`
- D) All three of them

---

## ☕ Cluster D — The Morning Checklist

*Script for this cluster:* **`scripts/04_morning_checklist.py`**

---

### STEP 11 — Notebook vs script, and running your shop

▶ *In your script:* the whole of `scripts/04_morning_checklist.py`

🎯 **Objective:** Understand what a `.py` script is for, and run one from a terminal.

☕ **Story moment:** There are two ways to work in your shop. Standing at the counter tasting a new blend, adjusting as you go — that is a **notebook**. And the laminated opening checklist you run through identically every single morning, in order, without thinking — that is a **script**.

🧠 **The idea in plain English:** A **notebook** (`.ipynb`) runs in cells you can execute in any order, showing results as you go. Wonderful for exploring. A **script** (`.py`) is one file that runs top to bottom, every time, in one command — which is how real programs actually ship. Two differences to hold on to:

1. A script **only shows what you `print()`**. A notebook chats back; a script does not.
2. A script always runs **in order, from the top**, so it does the same thing every time.

💻 **How to run it** — identical on Windows and Mac:

```text
python scripts/04_morning_checklist.py
```

*(Windows fallback if `python` is not recognised: `py scripts/04_morning_checklist.py`. Mac fallback: `python3 …`.)*

📺 **Expected output:**

```text
=== THE COZY BEAN -- OPENING CHECKLIST ===
1 - Unlock the front door
2 - Switch on the coffee machine
3 - Put the OPEN sign up
4 - Count the float in the till
5 - Bake the first tray of muffins
Muffin tray: full. Good to open!
=== Ready to open. Have a lovely day. ===
```

Look at what is inside that file: a **list**, a **for loop**, a counter, and an **if/else**. Everything you have learned, doing one useful job. This is a real program.

⚠️ **Common mistake:** Running `python 04_morning_checklist.py` without the `scripts/` part. Python looks in the room you are standing in, finds no such file, and says so. The path has to say which folder.

✅ **Verify:** Seven lines, numbered checklist, muffin verdict, sign-off.

🎤 **Try it yourself (30 seconds):** Add your own job to the `opening_jobs` list — `"Put fresh flowers on table three"`. Save, rerun. It is numbered automatically, because the counter does not care how long the list is.

---

### 🧠 Quick Quiz #4 — answer from memory, before peeking

**Q1.** Which one do you rerun every morning with a single `python file.py` command?

- A) The notebook
- B) The script

**Q2.** You run a script from the wrong folder and it tries to open `data/orders.txt`. Which error appears?

- A) `IndentationError`
- B) `TypeError`
- C) `NameError`
- D) `FileNotFoundError`

---

## ☕ Cluster E — The Order Notebook

*Script for this cluster:* **`scripts/05_order_notebook.py`**

Right now your shop forgets everything the moment the program ends. Time to give it a memory.

---

### STEP 12 — Writing the notebook

▶ *In your script:* Section 1 of `scripts/05_order_notebook.py`

🎯 **Objective:** Write lines into a file.

☕ **Story moment:** Closing time. You total up the day and write it in the shop's notebook, so that tomorrow-you — and the accountant, eventually — can read what happened today.

🧠 **The idea in plain English:** `open(name, "w")` opens a file for **writing**. `.write()` puts text into it. And `with open(...) as f:` is the tidy way: it closes the file automatically when the indented block ends, so you cannot forget.

> ⚠️ **`"w"` means a FRESH page.** If the file already exists, its contents are **erased** before writing. It does not add to the end. (For adding, see STEP 15.)

💻 **The code:**

```python
with open("data/end_of_day.txt", "w") as report:
    report.write("THE COZY BEAN -- END OF DAY\n")
    report.write("Cups sold: 63\n")
    report.write("Muffins sold: 24\n")

print("Report written to data/end_of_day.txt")
```

📺 **Expected output:**

```text
Report written to data/end_of_day.txt
```

Now look in your `data/` folder in the VS Code Explorer — **`end_of_day.txt` has appeared**. Click it. Your program made that.

⚠️ **Common mistake:** Expecting `.write()` to print something. It does not — it puts text in a **file**, not on your screen. Silence here is success.

✅ **Verify:** One confirmation line on screen, and a new file in `data/` containing three lines.

🎤 **Try it yourself (30 seconds):** Add a fourth line — `report.write("Best seller: latte\n")` — save, rerun, and open the file again.

---

### STEP 13 — The famous missing-`\n` bug 🐛

▶ *In your script:* Section 2 of `scripts/05_order_notebook.py`

🎯 **Objective:** See what happens without `\n`, and understand why it matters.

☕ **Story moment:** Ben writes three orders in the notebook without lifting his pen between them. Tomorrow morning nobody can tell where one order ends and the next begins. It is all one long word.

🧠 **The idea in plain English:** `.write()` puts down **exactly** what you give it and nothing more. It does **not** start a new line for you (unlike `print`, which always does). `\n` is the special code meaning *"start a new line here"*. Two characters, enormous consequences.

💻 **The code** — three writes, no `\n` anywhere:

```python
with open("data/sample.txt", "w") as f:
    f.write("Python")
    f.write("Machine Learning")
    f.write("AI Fundamentals")

file = open("data/sample.txt", "r")
print(file.read())
file.close()
```

📺 **Expected output:**

```text
PythonMachine LearningAI Fundamentals
```

There it is — three separate writes, one smooshed line. Nothing errored. Nothing warned you. The file is simply wrong.

**And the fix:**

```python
with open("data/sample_fixed.txt", "w") as f:
    f.write("Python\n")
    f.write("Machine Learning\n")
    f.write("AI Fundamentals\n")

print(open("data/sample_fixed.txt", "r").read())
```

```text
Python
Machine Learning
AI Fundamentals

```

*(That extra blank line at the end is honest: the file's last line ends with `\n`, and `print` adds a line break of its own. Nothing is wrong — it is worth noticing so it never confuses you.)*

⚠️ **Common mistake:** Assuming `.write()` behaves like `print()`. It is the most common file-writing bug there is, and now you have met it on purpose.

✅ **Verify:** One smooshed line, then three clean ones. Open both files in VS Code and compare them.

🎤 **Try it yourself (30 seconds):** Open `data/sample.txt` in VS Code. One line. Then open `data/sample_fixed.txt`. Three. Same three writes.

> 📌 **You saw this in class:** this exact demo — `sample.txt` written with three `f.write()` calls and no newlines, reading back as `PythonMachine LearningAI Fundamentals`. Your instructor left the bug in on purpose. Now you know why.

---

### STEP 14 — Reading yesterday's notebook

▶ *In your script:* Section 3 of `scripts/05_order_notebook.py`

🎯 **Objective:** Read a file line by line, and tidy each line.

☕ **Story moment:** It is tomorrow morning. The notebook is on the counter and you want to walk through yesterday's orders, one at a time.

🧠 **The idea in plain English:** Open with mode `"r"` for **reading**, then loop with `for line in file:` — the template from class. Each line still carries its invisible `\n` on the end, so `.strip()` trims the whitespace off both ends. If you opened the file by hand (without `with`), close it with `.close()` when you are done.

💻 **The code:**

```python
file = open("data/orders.txt", "r")

for line in file:
    print("Order:", line.strip())

file.close()
```

📺 **Expected output:**

```text
Order: latte with oat milk
Order: espresso
Order: large hot chocolate with extra marshmallows and cream
Order: cappuccino and a blueberry muffin
Order: tea
```

⚠️ **Common mistake:** Forgetting `.strip()`. Every line then carries its `\n`, `print` adds another, and your output comes out double-spaced. If you see mysterious blank lines between everything — that is this.

✅ **Verify:** Five orders, single-spaced, each prefixed `Order:`.

🎤 **Try it yourself (30 seconds):** Remove `.strip()`, save, rerun and watch the double-spacing appear. Then put it back.

---

### STEP 15 — Three ways to read, and the three modes

▶ *In your script:* Section 4 of `scripts/05_order_notebook.py`

🎯 **Objective:** Choose between `.read()`, `.readline()` and `.readlines()`, and know the file modes.

☕ **Story moment:** Sometimes you want the whole notebook photocopied. Sometimes just the top line. Sometimes a list of pages to flick through. Different jobs, different tools.

🧠 **The idea in plain English:**

| Method | Hands you back | Use it when |
|---|---|---|
| `.read()` | the **whole file** as one piece of text | you want everything at once |
| `.readline()` | just the **next single line** | you only need the first line |
| `.readlines()` | a **list** of all the lines | you want to count them or index them |
| `for line in file` | one line at a time | **the usual choice** — kind to big files |

And the three modes you pass to `open()`:

| Mode | Means | Careful |
|---|---|---|
| `"r"` | **read** — look, do not touch | the default |
| `"w"` | **write** — start a fresh page | ⚠️ **erases the file first!** |
| `"a"` | **append** — add to the end | keeps what is already there |

💻 **The code:**

```python
file = open("data/orders.txt", "r")
print(file.readline().strip())   # just the first line
file.close()

file = open("data/orders.txt", "r")
print(len(file.readlines()))     # how many lines in total
file.close()
```

📺 **Expected output:**

```text
latte with oat milk
5
```

**And appending** — adding to the end without erasing:

```python
with open("data/end_of_day.txt", "a") as report:
    report.write("Signed: Sara\n")

print(open("data/end_of_day.txt", "r").read())
```

```text
THE COZY BEAN -- END OF DAY
Cups sold: 63
Muffins sold: 24
Signed: Sara

```

⚠️ **Common mistake:** Reaching for `"w"` when you meant `"a"`. Opening your carefully built report in `"w"` mode wipes it instantly, with no warning and no undo. **When a file matters, check the mode twice.**

✅ **Verify:** The first order, then `5`, then the four-line report with Sara's signature added.

🎤 **Try it yourself (30 seconds):** Run the append snippet twice. Two signatures. Now you can *feel* the difference between `"a"` and `"w"`.

---

### 🧠 Quick Quiz #5 — answer from memory, before peeking

**Q1.** You open an existing file in `"w"` mode. What happens to what was in it?

- A) It is kept, and new text goes on the end
- B) It is kept, and new text goes at the start
- C) It is erased before anything is written
- D) Python refuses and raises an error

**Q2.** In class, three lines were written with no `\n`. What did the file contain?

- A) One line with all three joined together
- B) Three separate lines
- C) An empty file
- D) Three lines with blanks between them

**Q3.** What does `.readlines()` hand you back?

- A) The whole file as one piece of text
- B) A list of all the lines
- C) The next single line
- D) The number of lines

---

## ☕ Cluster F — Tearing Up Order Slips

*Script for this cluster:* **`scripts/06_order_slips.py`**

A line from a file arrives as one long piece of text. Usually you need its pieces.

---

### STEP 16 — Tearing a slip into pieces

▶ *In your script:* Section 1 of `scripts/06_order_slips.py`

🎯 **Objective:** Break text apart with `.split()` and convert the pieces.

☕ **Story moment:** The order slip says `latte,3.50` — a drink and a price, stuck together on one slip. Before you can add that price to the day's total, you have to tear the slip along the comma.

🧠 **The idea in plain English:** `.split()` with empty brackets breaks text wherever there are spaces, handing back a **list** of pieces. `.split(",")` breaks it at commas instead. One catch worth remembering: **the pieces are still text**, so a price needs `float()` before it can do maths — exactly the paper-label lesson from Lab01, arriving again in a new outfit.

💻 **The code:**

```python
slip = "latte with oat milk"
pieces = slip.split()
print(pieces)
print(len(pieces))

line = "latte,3.50"
parts = line.split(",")
print(parts)

drink = parts[0]
price = float(parts[1])       # text -> real number
print(drink, "costs", price * 2, "for two")
```

📺 **Expected output:**

```text
['latte', 'with', 'oat', 'milk']
4
['latte', '3.50']
latte costs 7.0 for two
```

⚠️ **Common mistake:** Doing maths on the piece without `float()`. `parts[1] * 2` gives `'3.503.50'` — because multiplying *text* repeats it, exactly as in Lab01. No error, just a nonsense total.

✅ **Verify:** Four pieces, the count, two pieces, then `7.0`.

🎤 **Try it yourself (30 seconds):** Split `"cappuccino and a blueberry muffin"` and print `len()` of the result.

**Reading the whole price list** — every line from a real file, torn and converted:

```python
total = 0.0
for line in open("data/menu_prices.txt", "r"):
    parts = line.strip().split(",")
    print(parts[0], "->", float(parts[1]))
    total += float(parts[1])

print("One of everything costs:", total)
```

```text
latte -> 3.5
espresso -> 2.75
muffin -> 2.25
cappuccino -> 4.0
One of everything costs: 12.5
```

Notice `.strip()` **before** `.split(",")` — otherwise the last piece on each line carries a `\n`, and `float()` would be working with something untidy. Strip first, then split. That order becomes a habit.

---

### STEP 17 — Stapling the pieces back together

▶ *In your script:* Section 2 of `scripts/06_order_slips.py`

🎯 **Objective:** Join a list of pieces into one piece of text.

☕ **Story moment:** For the customer's receipt you want the order written out neatly: *latte, muffin, tea* — one tidy line, commas between.

🧠 **The idea in plain English:** `join()` is the exact opposite of `split()`. It reads a little backwards at first: the text you put **in front** is the glue that goes **between** the pieces.

💻 **The code:**

```python
order_parts = ["latte", "muffin", "tea"]

print(", ".join(order_parts))
print(" + ".join(order_parts))
```

📺 **Expected output:**

```text
latte, muffin, tea
latte + muffin + tea
```

⚠️ **Common mistake:** Writing it the other way round — `order_parts.join(", ")`. The glue goes first: `glue.join(list)`. Also, every piece must be text; a list with a number in it needs `str()` first.

✅ **Verify:** Two lines, same three words, different glue.

🎤 **Try it yourself (30 seconds):** Try `" and ".join(order_parts)`. Suddenly it reads like a sentence.

---

### 🧠 Quick Quiz #6 — answer from memory, before peeking

**Q1.** What does `"latte,3.50".split(",")` hand back?

- A) `['latte,3.50']`
- B) `['latte', '3.50']`
- C) `('latte', 3.50)`
- D) `'latte 3.50'`

**Q2.** What does `float("3.50")` hand back?

- A) The text `'3.50'`
- B) The number `3`
- C) The number `3.5`
- D) An error

---

> ## 🚀 Bonus — beyond class: the interactive till
>
> *Script:* **`scripts/07_bonus_interactive_till.py`**
>
> Nothing else in this lab depends on this. It is here because it is the most satisfying twenty lines you will write all week: Lab01's `input()` plus this lab's `if`/`elif` and functions, adding up to a till that genuinely takes an order.
>
> ```python
> def price_for(size):
>     if size == "small":
>         return 3.00
>     elif size == "medium":
>         return 3.50
>     elif size == "large":
>         return 4.00
>     else:
>         return 3.50
> ```
>
> Run it with `python scripts/07_bonus_interactive_till.py` and answer the three questions. Here is a run where the answers typed were `Ben`, `Cappuccino`, `Large`:
>
> ```text
> Customer name? Which drink? Size (small / medium / large)? --- THE COZY BEAN ---
> Ben: one large cappuccino
> Total: $4.00
> Thank you, see you tomorrow!
> ```
>
> *(The three questions appear on one line in this transcript because the answers were piped in rather than typed. When you run it yourself, each question waits politely on its own line.)*
>
> **The program STOPS and waits for you to type. That blinking cursor is your turn, not a freeze.**

---

## 5. 🏋️ Practice Problems

Eight core problems, ramping from a single rule to the two capstones from class. Then one bonus.

**How practice works:** one problem per file in `practice/`; run just the one you want with `python practice/p01_rush_hour_rules.py`. Every file's header repeats the task **and the exact expected output**. Every file runs as-is before you touch it. Answers are in `solutions/` — **open them only after a genuine attempt.**

| # | File | Story task | You will practise |
|---|---|---|---|
| p01 | `p01_rush_hour_rules.py` | Price orders by size, tested on three real orders. | `if` / `elif` / `else` |
| p02 | `p02_stamp_cards.py` | Punch five loyalty stamps, numbered the way customers count. | `for`, `range()` |
| p03 | `p03_restock_counter.py` | Restock the shelf until it is full — or until the trays run out. | `while`, `break` |
| p04 | `p04_recipe_card.py` | Write two pricing cards and use each of them twice. | `def`, parameters, `return` |
| p05 | `p05_end_of_day_report.py` | Write the day's report to a file, then read it back to prove it worked. | writing files, `\n` |
| p06 | `p06_read_the_notebook.py` | Read the order notebook and print it as a numbered list. | reading files, `.strip()` |
| **p07** | `p07_capstone_biggest_order.py` | **CAPSTONE A** — a function that finds the biggest order of the day. | functions + file reading |
| **p08** | `p08_capstone_shift_hours.py` | **CAPSTONE B** — every barista's total and average daily hours. | files + `split()` + `float()` |
| 🚀 p09 | `p09_bonus_order_taker.py` | **Bonus:** a till that takes a typed order and prices it. | `input()` + `if`/`elif` |

### 🏔️ About the two capstones

These are the exercises straight from your class session, rebuilt inside the shop. They are the hardest things in this lab, and finishing them means you have genuinely learned Week 1.

- **Capstone A — The Biggest Order of the Day.** In class this was `input_stats` / `longest_line`: a function that reads a file and reports its longest line. In the shop it becomes the closing-time prize for the day's biggest order. Same recipe card, new apron.
- **Capstone B — Barista Shift Hours.** In class this was `hours.txt`, with Suzy, Brad and Jenn. Here it is your three baristas in `data/shift_hours.txt`, and the output keeps the exact shape used in class: `<name> ID <id> worked <total> hours: <avg> / day`. Everybody works exactly five days.

---

## 6. 📚 Cheat Sheet & Glossary

- **[CHEATSHEET.md](CHEATSHEET.md)** — all of Lab02's syntax on one page: decisions, loops, functions, file modes, split and join. Print it.
- **[GLOSSARY.md](GLOSSARY.md)** — every technical word in this lab, one plain sentence each.

*(Lab01's [cheat sheet](../Lab01/CHEATSHEET.md) and [glossary](../Lab01/GLOSSARY.md) still apply — variables, types and lists are used constantly here.)*

---

## 7. 🤔 Reflection (2 minutes — please actually do this)

1. **Which one felt most like something you already do by hand?** Rules, loops, or recipe cards? Why that one?
2. **What is still fuzzy?** Name the one thing you would ask an instructor sitting beside you. Write it down — it is your first question next session.
3. **What would you automate next?** Think of one repetitive thing in your own week. Would it be a rule, a loop, or a recipe card?

---

## 8. ✅ Answer Key

*No peeking until you have answered. Sixteen questions in total.*

### Quiz #1

| Q | Answer | Why |
|---|---|---|
| 1 | **A** — the first True one only | Python stops at the first match and leaves the chain; the rest are never even checked. |
| 2 | **D** — `IndentationError` | The colon promises an indented block, so Python objects when none arrives. |
| 3 | **B** — `You are a senior` | 70 is not under 18 and not under 65, so both tests fail and `else` catches it. |

### Quiz #2

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — `5` | It runs for counts 0, 1, 2, 3, 4; at 5 the question turns False and the loop ends. |
| 2 | **A** — `0` | `range` starts at 0 and stops before the number you give it. |
| 3 | **C** — leaves the loop immediately | Remaining items are skipped entirely. |

### Quiz #3

| Q | Answer | Why |
|---|---|---|
| 1 | **A** — `return` hands a value back to be used | `print` only displays; the value cannot be stored or reused. |
| 2 | **D** — `Hello Debela` then `Hello Memar` | One card, called twice with different ingredients. |
| 3 | **B** — `len` and `max` | `latte` is just a word from our story, not a Python function. |

### Quiz #4

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — the script | A `.py` file runs top to bottom in one command, identically every time. |
| 2 | **D** — `FileNotFoundError` | The path `data/orders.txt` is looked for inside the folder you are standing in. |

### Quiz #5

| Q | Answer | Why |
|---|---|---|
| 1 | **C** — it is erased before anything is written | `"w"` means a fresh page. Use `"a"` to add to the end instead. |
| 2 | **A** — one line with all three joined together | `.write()` adds nothing you did not ask for, so with no `\n` everything runs together. |
| 3 | **B** — a list of all the lines | Which is why `len(file.readlines())` counts them. |

### Quiz #6

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — `['latte', '3.50']` | `split` hands back a list of pieces, and they are still text. |
| 2 | **C** — the number `3.5` | `float()` converts text into a real number; Python drops the unneeded trailing zero. |

---

## 9. ➡️ What's Next

You now have the complete toolkit of a working programmer: values, containers, decisions, repetition, functions, and files. That is genuinely most of what day-to-day code is made of.

**Next session** you start organising bigger programs — putting these pieces together into something with real structure, and taking the first steps toward the data work that AI and machine learning are built on. Every dataset you will ever load starts as `for line in file`, and you can already write that.

The Cozy Bean is dreaming of a second branch. ☕

---

*Apeiron AI Training Academy · Module 1: AI/ML Fundamentals · Week 1 · Lab02*
*"Boundless Possibilities, Infinite Potential"*
