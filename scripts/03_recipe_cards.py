# ============================================================
#  The Cozy Bean  --  Script 03: Laminated Recipe Cards
#
#  What this shows : writing a function once and using it
#                    forever, return values, and the built-in
#                    tools that came free with Python.
#  Lab STEPs       : STEP 8, 9 and 10
#  How to run it   : python scripts/03_recipe_cards.py
#                    (run it from inside the M1-W1-Lab02 folder)
# ============================================================


# ---- Section 1  (STEP 8): write the card once --------------
# def writes the recipe card. The word in brackets is the
# PARAMETER -- the ingredient that changes each time you use it.
def greet_customer(name):
    print("Good morning,", name + "! What can I get you?")

# Now use the same card twice, with different ingredients.
greet_customer("Sara")
greet_customer("Ben")

# 📌 You saw this in class:
def greet(name):
    print("Hello", name)

greet("Debela")
greet("Memar")


# ---- Section 2  (STEP 9): a card that hands something back -
# return hands a value BACK to whoever called the card, instead
# of printing it. That lets you store it and use it later.
def latte_price(cups):
    return cups * 3.50

# Catch what comes back in a jar:
two_lattes = latte_price(2)
print("Two lattes cost:", two_lattes)
print("Five lattes cost:", latte_price(5))

# 📌 You saw this in class:
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print("Result:", result)


# ---- Section 3  (STEP 10): the appliances that came free ---
# You have been using built-in functions since your first day.
# They come with Python -- nothing to install, nothing to write.
todays_orders = ["latte", "espresso", "muffin"]

print(len(todays_orders))         # how many?
print(type(todays_orders))        # what kind of thing is it?
print(max(3.50, 2.75, 4.25))      # the biggest of these
print(list(range(3)))             # a run of numbers
