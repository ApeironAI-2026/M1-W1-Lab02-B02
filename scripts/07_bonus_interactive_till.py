# ============================================================
#  The Cozy Bean  --  Script 07: 🚀 BONUS -- The Interactive Till
#
#  🚀 Bonus -- beyond class. Nothing else in this lab needs it.
#
#  What this shows : input() from Lab01's bonus, combined with
#                    this lab's if/elif rules, makes a till that
#                    really takes an order and prices it.
#  How to run it   : python scripts/07_bonus_interactive_till.py
#                    (run it from inside the M1-W1-Lab02 folder)
#
#  NOTE: the program STOPS and waits for you to type. That
#  blinking cursor is your turn, not a freeze.
# ============================================================


def price_for(size):
    """Hand back the price for a size. (A recipe card!)"""
    if size == "small":
        return 3.00
    elif size == "medium":
        return 3.50
    elif size == "large":
        return 4.00
    else:
        return 3.50   # anything else, charge the medium price


name = input("Customer name? ")
drink = input("Which drink? ")
size = input("Size (small / medium / large)? ")

price = price_for(size.lower())

print("--- THE COZY BEAN ---")
print(f"{name}: one {size.lower()} {drink.lower()}")
print(f"Total: ${price:.2f}")
print("Thank you, see you tomorrow!")
