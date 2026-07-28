# ============================================================
#  The Cozy Bean -- Script 01: Barista Decision Rules
#  Lab STEPs 1-3.
#  Shows: if / else, why indentation IS the grammar, and elif
#         chains where the FIRST True rule wins.
#  Run:   python scripts/01_decision_rules.py (from M1-W1-Lab02/)
# ============================================================

# ---- Section 1  (STEP 1): the first barista rule -----------
# if asks a True/False question. The indented lines below it
# only run when the answer is True. Otherwise else runs.
oat_milk_left = 0

if oat_milk_left == 0:
    print("Sorry, we're out of oat milk today -- almond instead?")
else:
    print("One oat latte coming right up!")

# 📌 You saw this in class:
age = 20

if age < 18:
    print("You are a minor")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")

# ---- Section 2  (STEP 2): indentation IS the grammar -------
# Those 4 spaces are not decoration. Remove them and Python
# stops -- it cannot tell which lines belong to the if. This
# broken version is COMMENTED OUT so the script still runs:
#   if oat_milk_left == 0:
#   print("out of oat milk")
# IndentationError: expected an indented block after 'if' statement on line 1

# ---- Section 3  (STEP 3): a chain of rules -----------------
# elif means "else, if". Python checks top to bottom and stops
# at the FIRST True rule. The rest never get a look in.
cups = 9

if cups >= 10:
    print("Big order -- free cookie!")
elif cups >= 5:
    print("Medium order -- thank you!")
else:
    print("Small order -- enjoy!")

# 📌 You saw this in class. Here ALL THREE conditions are True
# (90 > 50, 90 > 40, 90 > 30) -- but only the first one prints.
x = 90

if x > 50:
    print("Condition 1 is True")
elif x > 40:
    print("Condition 2 is True")
elif x > 30:
    print("Condition 3 is True")
else:
    print("None are True")
