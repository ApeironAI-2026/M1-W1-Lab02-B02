# ============================================================
#  PRACTICE p09 -- 🚀 BONUS -- The Order Taker
#  The Cozy Bean  |  M1-W1 Lab02
#
#  🚀 Bonus -- beyond class. This one uses input(), which was
#  not in your session. Nothing else in this lab depends on it.
#  Skip it with a clear conscience, or enjoy it -- it is fun.
#
#  YOUR TASK:
#    Build a till that really takes an order. Ask for a name, a
#    drink and a size. Use a recipe card with if/elif/else to
#    price the size (small 3.00, medium 3.50, large 4.00, and
#    anything else charges the medium price). Print a tidy
#    receipt with the price to two decimal places.
#
#  AN EXAMPLE RUN (yours will say whatever you type):
#    Customer name? Ben
#    Which drink? Cappuccino
#    Size (small / medium / large)? large
#    --- THE COZY BEAN ---
#    Ben: one large cappuccino
#    Total: $4.00
#    Thank you, see you tomorrow!
#
#  NOTE: when you run this, the program STOPS and waits for
#  you. That blinking cursor is your turn, not a freeze.
#
#  HINT: .lower() on what they typed means "Large", "large"
#        and "LARGE" all work the same way.
#
#  How to run it: python practice/p09_bonus_order_taker.py
#                 (run it from inside the M1-W1-Lab02 folder)
#
#  Stuck? See solutions/p09_bonus_order_taker.py.
# ============================================================


# TODO 1: finish this recipe card so each size returns its
#         own price, and anything unexpected returns 3.50
def price_for(size):
    return 0.00


# TODO 2: ask the three questions with input()
name = "Ben"
drink = "Cappuccino"
size = "large"

price = price_for(size.lower())

print("--- THE COZY BEAN ---")

# TODO 3: print the order line and the total. Use an f-string,
#         and show the price with 2 decimals using {price:.2f}
print("...: one ... ...")
print("Total: $...")
print("Thank you, see you tomorrow!")
