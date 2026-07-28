# ============================================================
#  PRACTICE p01 -- Rush Hour Rules
#  The Cozy Bean  |  M1-W1 Lab02
#
#  YOUR TASK:
#    Write the barista's rule for order size:
#      10 cups or more -> a big order, free cookie
#      5 to 9 cups     -> a medium order, say thank you
#      anything less   -> a small order, say enjoy
#    Test it on three orders -- 12, 6 and 2 cups -- by looping
#    over the list and running the rule for each one.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    12 cups: Big order -- free cookie!
#    6 cups: Medium order -- thank you!
#    2 cups: Small order -- enjoy!
#
#  HINT: Python checks the rules top to bottom and stops at the
#        FIRST one that is True -- so put the biggest test first.
#
#  How to run it: python practice/p01_rush_hour_rules.py
#                 (run it from inside the M1-W1-Lab02 folder)
#
#  Stuck? The answer is in solutions/p01_rush_hour_rules.py --
#  but give it a real try first. The struggle makes it stick.
# ============================================================


orders = [12, 6, 2]

for cups in orders:

    # TODO 1: if the order is 10 cups or more, it is a big order
    #         (replace the False below with the real question)
    if False:
        print(cups, "cups: Big order -- free cookie!")

    # TODO 2: add an elif for 5 cups or more (medium order)

    # TODO 3: add an else for everything smaller (small order)

    else:
        print(cups, "cups: (rule not written yet)")
