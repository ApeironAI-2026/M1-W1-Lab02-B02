# ============================================================
#  SOLUTION p09 -- 🚀 BONUS -- The Order Taker
#  The Cozy Bean  |  M1-W1 Lab02
#
#  🚀 Bonus -- beyond class.
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
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
#  How to run it: python solutions/p09_bonus_order_taker.py
#                 (run it from inside the M1-W1-Lab02 folder)
# ============================================================


def price_for(size):
    if size == "small":
        return 3.00
    elif size == "medium":
        return 3.50
    elif size == "large":
        return 4.00
    else:
        return 3.50   # anything unexpected pays the medium price


name = input("Customer name? ")
drink = input("Which drink? ")
size = input("Size (small / medium / large)? ")

# .lower() means "Large", "large" and "LARGE" all work.
price = price_for(size.lower())

print("--- THE COZY BEAN ---")
print(f"{name}: one {size.lower()} {drink.lower()}")
print(f"Total: ${price:.2f}")
print("Thank you, see you tomorrow!")
