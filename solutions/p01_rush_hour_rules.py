# ============================================================
#  SOLUTION p01 -- Rush Hour Rules
#  The Cozy Bean  |  M1-W1 Lab02
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p01_rush_hour_rules.py
#                 (run it from inside the M1-W1-Lab02 folder)
# ============================================================


orders = [12, 6, 2]

for cups in orders:

    # The FIRST rule that is True wins, so the biggest test
    # has to come first. Swap them round and 12 cups would
    # match "5 or more" and never reach the big-order line.
    if cups >= 10:
        print(cups, "cups: Big order -- free cookie!")
    elif cups >= 5:
        print(cups, "cups: Medium order -- thank you!")
    else:
        print(cups, "cups: Small order -- enjoy!")
