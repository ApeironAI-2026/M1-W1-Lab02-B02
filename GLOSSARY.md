# 📖 Lab02 Glossary — every word, one plain sentence

**The Cozy Bean · M1-W1-Lab02 · Apeiron AI Training Academy**

*Lab01's words (variable, list, string, casting…) are in [Lab01's glossary](../Lab01/GLOSSARY.md) and still apply. These are the new ones.*

---

## The story words

| Story | Python | Meaning |
|---|---|---|
| the barista's decision rule | **`if` / `elif` / `else`** | choosing which code to run based on a question |
| indented sub-steps on a recipe card | **indentation** | the spaces that tell Python which lines belong together |
| serving everyone in the queue | **`for` loop** | doing the same thing once per item |
| restocking until the shelf is full | **`while` loop** | repeating until a condition stops being true |
| the fire alarm | **`break`** | leaving a loop immediately |
| a laminated recipe card | **function** | instructions written once and used many times |
| the blank on the card | **parameter** | the value you fill in each time you use the function |
| the drink handed over the counter | **`return`** | the value a function hands back to you |
| the appliances that came with the shop | **built-in functions** | tools Python provides for free |
| the morning opening checklist | **script** | a `.py` file that runs top to bottom, the same way every time |
| the order notebook | **file** | text saved on disk that outlives your program |
| tearing an order slip into pieces | **`split()`** | breaking text into a list of parts |
| stapling the pieces back | **`join()`** | gluing a list of parts into one piece of text |

---

## A–Z

**`a` mode** — opening a file in **append** mode: new text is added to the end and what was already there is kept.

**append (files)** — adding to the end of a file rather than replacing it. See `a` mode. *(Not the same as a list's `.append()`, though the idea is identical.)*

**block** — a group of lines that belong together, marked by being indented the same amount. Every colon `:` introduces one.

**`break`** — a keyword that leaves the loop it is inside immediately, skipping whatever items remain.

**built-in function** — a function Python provides for free, with nothing to install or write: `print()`, `len()`, `type()`, `range()`, `max()`.

**call** — to actually use a function, by writing its name with brackets: `greet_customer("Sara")`. Defining a function does nothing until you call it.

**`.close()`** — a file method that shuts a file you opened by hand. Not needed when you use `with open(...)`, which closes it for you.

**colon (`:`)** — the punctuation ending an `if`, `for`, `while` or `def` line. It means "an indented block follows".

**condition** — the True/False question an `if` or `while` asks.

**`def`** — the keyword that begins a function definition ("define").

**`elif`** — short for "else if". Another condition checked only when every condition above it was False.

**`else`** — the catch-all branch that runs when no condition above it was True.

**`FileNotFoundError`** — the error you get when Python cannot find the file you asked for. **Nearly always means you are running from the wrong folder.**

**`float()` on a token** — converting a piece of text from a split into a real number, so it can be used in maths.

**`for` loop** — a loop that runs once for each item in a list (or each number in a `range`).

**function** — a named block of instructions you write once and use as often as you like.

**`if`** — the keyword that starts a decision: the indented block below it runs only when its condition is True.

**indentation** — the spaces at the start of a line. In Python this is **grammar, not decoration** — it is how Python knows which lines belong to which block. Use 4 spaces.

**`IndentationError`** — the error you get when indentation is missing, uneven, or mixes tabs with spaces.

**infinite loop** — a `while` loop whose condition never becomes False, so it runs forever. Press **Ctrl+C** to stop it.

**`join()`** — a string method that glues a list of pieces into one piece of text, with the text in front used as the glue: `", ".join(parts)`.

**mode** — the second thing you pass to `open()`, saying what you intend to do: `"r"` read, `"w"` write, `"a"` append.

**`open()`** — the built-in function that opens a file and hands back a file object you can read from or write to.

**parameter** — the name in a function's brackets, standing for a value that will be supplied when it is called. The blank on the recipe card.

**`+=`** — shorthand for "add this to what is already there". `count += 1` means `count = count + 1`.

**`.read()`** — a file method handing back the entire file as one piece of text.

**`.readline()`** — a file method handing back the next single line.

**`.readlines()`** — a file method handing back a list of all the lines in the file.

**`return`** — the keyword that hands a value back from a function to whoever called it, so it can be stored and used.

**`.strip()`** — a string method that trims whitespace (including the invisible newline) off both ends of a piece of text.

**`split()`** — a string method that breaks text into a list of pieces: at spaces by default, or at whatever you pass in, such as `.split(",")`.

**`\n`** — the newline character: two characters you type that mean "start a new line here". `.write()` needs it; `print()` adds one automatically.

**`while` loop** — a loop that keeps repeating as long as its condition stays True, checking again before each round.

**`with open(...) as f:`** — the tidy way to open a file: it closes automatically when the indented block ends, so you cannot forget.

**`w` mode** — opening a file in **write** mode. ⚠️ This **erases** anything already in the file before writing.

---

## 🚀 Bonus words (beyond class — only if you did the bonus bits)

**`input()`** — a function that pauses the program, waits for you to type something and press Enter, then hands back what you typed as text.

**`:.2f`** — a formatting instruction inside an f-string meaning "show exactly two digits after the decimal point", used to make numbers look like money.
