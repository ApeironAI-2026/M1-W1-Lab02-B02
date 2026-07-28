# ============================================================
#  SOLUTION p03 -- Restocking the Shelf
#  The Cozy Bean  |  M1-W1 Lab02
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p03_restock_counter.py
#                 (run it from inside the M1-W1-Lab02 folder)
# ============================================================


cups_on_shelf = 0
trays_used = 0
trays_in_delivery = 3

# The while loop's question is "is the shelf still not full?"
while cups_on_shelf < 10:

    cups_on_shelf += 3   # one tray holds 3 cups
    trays_used += 1

    print("Tray", trays_used, "-- shelf now has", cups_on_shelf, "cups")

    # Without this break the loop would keep asking for trays
    # that do not exist. break leaves the loop immediately.
    if trays_used == trays_in_delivery:
        break

print("Delivery ran out after", trays_used, "trays -- shelf has", cups_on_shelf, "cups")
