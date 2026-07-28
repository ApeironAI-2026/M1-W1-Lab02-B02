# ☕ M1-W1-Lab02 — The Cozy Bean Gets Busy

**Apeiron AI Training Academy** · *"Boundless Possibilities, Infinite Potential"*

| | |
|---|---|
| **Module** | M1: AI/ML Fundamentals |
| **Week** | Week 1 |
| **Lab** | Lab02 — The Cozy Bean Gets Busy |
| **Topic** | `if`/`elif`/`else`, `for` and `while` loops, functions, running scripts, reading and writing files, `split()`/`join()` |
| **Duration** | **≈ 1 hour** of lab work (setup not counted) |
| **Difficulty** | ⭐ Absolute Beginner — continues directly from Lab01 |

Three weeks on, the shop got popular. This week you stop *doing* everything personally and start writing things down that do themselves: **rules**, **loops**, **recipe cards** (functions), and an **order notebook** your shop reads back the next morning.

**Start here → [`M1-W1-Lab02.md`](M1-W1-Lab02.md)** — the full lab, 20 steps, plus two capstone exercises.

> 📎 **Do [Lab01 — Opening Week](https://github.com/ApeironAI-2026/M1-W1-Lab01-B02) first.** This lab assumes variables, types, lists and dictionaries. Its GitHub Classroom link is in Google Classroom alongside this one.

---

## 1. 📥 Get this repo onto your computer

You reached this repo by clicking the **GitHub Classroom link posted in Google Classroom**. That link made **your own private copy** of the lab — the URL has your GitHub username in it. This is the copy you clone.

### 1.1 Where to put it

This is a **separate repo** from Lab01, so it gets its own folder — a sibling of `Lab01`, right next to it:

```text
AperionAI/
└── Module1/
    ├── Week1/
    │   ├── Lab01/      ← already cloned
    │   └── Lab02/      ← this repo goes here
    ├── Week2/
    │   ├── Lab01/
    │   └── Lab02/
    └── Week3/
        ├── Lab01/
        └── Lab02/
```

Keeping the names exactly `Lab01` and `Lab02` matters for one small, pleasant reason: the links between the two labs' cheat sheets and glossaries then work, because each one knows where the other lives.

### 1.2 Copy your repo's address

1. On this repo's page on GitHub, click the green **`< > Code`** button.
2. Make sure the **HTTPS** tab is selected.
3. Click the 📋 copy icon.

You now have something like `https://github.com/ApeironAI-2026/M1-W1-Lab02-B02-<your-username>.git` on your clipboard. **Use your own address**, not a classmate's.

### 1.3 Clone it into `Week1/Lab02`

In a terminal — **PowerShell** on Windows, **Terminal** on Mac — run these one at a time, replacing `PASTE-YOUR-REPO-URL-HERE` with what you copied:

**Windows (PowerShell):**

```text
cd ~\AperionAI\Module1\Week1
git clone PASTE-YOUR-REPO-URL-HERE Lab02
cd Lab02
```

**Mac / Linux:**

```text
cd ~/AperionAI/Module1/Week1
git clone PASTE-YOUR-REPO-URL-HERE Lab02
cd Lab02
```

That last word — `Lab02` — is what names the folder. Leave it off and git names the folder after the repo instead (`M1-W1-Lab02-B02-your-username`), which breaks the tidy layout above.

> **Folder `Week1` does not exist yet?** You have not cloned Lab01. Create it first — `mkdir -Force ~\AperionAI\Module1\Week1` on Windows, `mkdir -p ~/AperionAI/Module1/Week1` on Mac — then clone.
>
> **No git?** Install from [git-scm.com/downloads](https://git-scm.com/downloads) and reopen your terminal. Or use **`< > Code` → Download ZIP**, unzip, rename the folder to `Lab02` and place it next to `Lab01`.

### 1.4 Check you landed in the right place

```text
pwd
ls
```

`pwd` must end in **`Week1/Lab02`**. `ls` must show `README.md`, `M1-W1-Lab02.md`, `CHEATSHEET.md`, `GLOSSARY.md`, **`data`**, `scripts`, `practice` and `solutions`.

**If you cannot see `data`, stop and fix it before doing anything else.** Being in the right folder matters more in this lab than it did in Lab01: your scripts open files by a path written relative to the lab folder — `open("data/orders.txt")` means *"the `data` folder, in the room I am standing in"*. Stand in the wrong room and there is no `data` folder to find.

---

## 2. 🔧 Open it and run something

**Already set up from Lab01? Then you are two clicks away:**

1. VS Code → **File → Open Folder…** → choose your **`Lab02`** folder.
2. **Terminal → New Terminal.**

**Never done the setup?** [Lab01's README](https://github.com/ApeironAI-2026/M1-W1-Lab01-B02#2--set-up-python-and-vs-code) covers installing Python, getting VS Code, and saving files. Do that once, then come back here.

**Now run something real:**

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

Seven lines like that means everything is wired up. Open [`M1-W1-Lab02.md`](M1-W1-Lab02.md) and begin.

> 💡 Reading the lab in VS Code? Open `M1-W1-Lab02.md` and press **Ctrl+Shift+V** (Mac: **Cmd+Shift+V**) for a formatted preview alongside your code.

---

## 3. 📂 What is in this repo

| Path | What it is |
|---|---|
| [`M1-W1-Lab02.md`](M1-W1-Lab02.md) | **The lab.** 20 steps, 6 clusters, quizzes, two capstones, answer key. |
| [`CHEATSHEET.md`](CHEATSHEET.md) | Lab02 syntax on one page. Keep it next to Lab01's — you need both. |
| [`GLOSSARY.md`](GLOSSARY.md) | The new words for this lab, in plain English. |
| `data/` | Three small text files that **ship with the repo** — see below. |
| `scripts/` | Seven runnable scripts, one per cluster. |
| `practice/` | Nine practice problems, including the two capstones. **Your code goes here.** |
| `solutions/` | Worked solutions. Have a real go first. |

### About the `data/` folder

| File | What it holds |
|---|---|
| `data/orders.txt` | the day's orders, one per line |
| `data/shift_hours.txt` | each barista's id, name and five days of hours |
| `data/menu_prices.txt` | drink names and prices, comma-separated |

You never create these — they are already there. Some scripts will *add* new files to `data/` (`sample.txt`, `sample_fixed.txt`, `end_of_day.txt`, `my_report.txt`). That is Python creating them for you, and it is safe to run those scripts as many times as you like.

> 🛋️ **Aim for one sitting of about an hour.** If you do need to pause, the natural break is after Cluster C (recipe cards), when you have decisions, loops and functions under your belt and the file work is still ahead.

---

## 4. 💾 Saving your work back to GitHub

From inside `Lab02`, when you finish, or any time you pause:

```text
git add .
git commit -m "Finished the loops cluster"
git push
```

The files your scripts generate in `data/` will get committed too — that is fine and harmless.

---

## 5. 🆘 If something goes wrong

| What you see | What it means | What to do |
|---|---|---|
| `FileNotFoundError: … 'data/orders.txt'` | You are running from the wrong folder — Python found no `data` folder in the room it is standing in. | `pwd`. Does it end in `Lab02`? If not, **File → Open Folder** on `Lab02`, then **Terminal → New Terminal**. Confirm with `ls` that you can see `data`. |
| `IndentationError` | The spacing at the start of a line is wrong. | Indent with **4 spaces**, consistently. Never mix tabs and spaces. Cluster A of the lab explains this properly. |
| `'python' is not recognized…` (Windows) | Windows cannot find Python. | Try `py scripts/04_morning_checklist.py`, or reinstall Python with **"Add python.exe to PATH"** ticked. |
| `command not found: python` (Mac) | Mac calls it something else. | Use `python3 scripts/04_morning_checklist.py`. |
| **Output did not change after an edit** | **The file was never saved.** | Look for the ● dot on the file tab. **Ctrl+S** / **Cmd+S**. Rerun. It catches everyone. |

Still stuck after a genuine try? Post in the course channel with **what you ran**, **what you expected**, and **the last line of the error**.

---

*Apeiron AI Training Academy · Module 1, Week 1, Lab 02 · Previous: [Lab01 — Opening Week](https://github.com/ApeironAI-2026/M1-W1-Lab01-B02)*

> 🔗 The links to Lab01's cheat sheet and glossary inside the lab document are **relative** — they work once both repos are cloned side by side as `Week1/Lab01` and `Week1/Lab02`, which is exactly why the folder names above matter.
