# ============================================================
#  PRACTICE p04 -- Laminated Recipe Cards
#  The Cozy Bean  |  M1-W1 Lab02
#
#  YOUR TASK:
#    Write two recipe cards (functions).
#      latte_price(cups)     -> the cost of that many lattes
#                               at 3.50 each
#      muffin_price(muffins) -> the cost at 2.25 each
#    Then use each card twice with different numbers. Store at
#    least one answer in a jar before printing it.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Two lattes cost: 7.0
#    Five lattes cost: 17.5
#    A dozen muffins cost: 27.0
#    Two muffins cost: 4.5
#
#  HINT: return hands the answer back so you can store it;
#        print only shows it on the screen.
#
#  How to run it: python practice/p04_recipe_card.py
#                 (run it from inside the M1-W1-Lab02 folder)
#
#  Stuck? The answer is in solutions/p04_recipe_card.py -- but
#  give it a real try first. The struggle makes it stick.
# ============================================================


# TODO 1: finish this card so it hands back the cost of the
#         lattes instead of always handing back 0
def latte_price(cups):
    return 0


# TODO 2: write a second card called muffin_price, the same
#         shape as the one above, at 2.25 per muffin
def muffin_price(muffins):
    return 0


# TODO 3: use the cards. Store the first answer in a jar.
two_lattes = latte_price(0)
print("Two lattes cost:", two_lattes)

print("Five lattes cost:", latte_price(0))
print("A dozen muffins cost:", muffin_price(0))
print("Two muffins cost:", muffin_price(0))
