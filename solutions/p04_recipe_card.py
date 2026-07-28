# ============================================================
#  SOLUTION p04 -- Laminated Recipe Cards
#  The Cozy Bean  |  M1-W1 Lab02
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p04_recipe_card.py
#                 (run it from inside the M1-W1-Lab02 folder)
# ============================================================


# Write the recipe once...
def latte_price(cups):
    return cups * 3.50


def muffin_price(muffins):
    return muffins * 2.25


# ...then use it as many times as you like, with different
# ingredients each time.
two_lattes = latte_price(2)      # the answer is stored in a jar
print("Two lattes cost:", two_lattes)

print("Five lattes cost:", latte_price(5))
print("A dozen muffins cost:", muffin_price(12))
print("Two muffins cost:", muffin_price(2))
