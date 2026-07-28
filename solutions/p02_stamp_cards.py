# ============================================================
#  SOLUTION p02 -- Loyalty Stamp Cards
#  The Cozy Bean  |  M1-W1 Lab02
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p02_stamp_cards.py
#                 (run it from inside the M1-W1-Lab02 folder)
# ============================================================


for i in range(5):
    # i goes 0, 1, 2, 3, 4 -- so i + 1 gives the human number.
    print("Stamp", i + 1, "of 5")

# Not indented, so it runs ONCE, after the loop has finished.
print("Card full -- next coffee is free!")
