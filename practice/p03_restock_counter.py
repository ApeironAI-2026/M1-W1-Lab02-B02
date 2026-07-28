# ============================================================
#  PRACTICE p03 -- Restocking the Shelf
#  The Cozy Bean  |  M1-W1 Lab02
#
#  YOUR TASK:
#    The shelf needs 10 cups. Each tray from the delivery adds
#    3 cups. Use a WHILE loop to keep unloading trays until the
#    shelf has at least 10 -- but today's delivery only has 3
#    trays in it, so use break to stop when the trays run out.
#    Print the shelf count after each tray, then the closing
#    message.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Tray 1 -- shelf now has 3 cups
#    Tray 2 -- shelf now has 6 cups
#    Tray 3 -- shelf now has 9 cups
#    Delivery ran out after 3 trays -- shelf has 9 cups
#
#  HINT: keep a trays_used counter going up by 1 each time, and
#        break out of the loop the moment it reaches 3.
#
#  How to run it: python practice/p03_restock_counter.py
#                 (run it from inside the M1-W1-Lab02 folder)
#
#  Stuck? The answer is in solutions/p03_restock_counter.py --
#  but give it a real try first. The struggle makes it stick.
# ============================================================


cups_on_shelf = 0
trays_used = 0
trays_in_delivery = 3

# TODO 1: keep going WHILE the shelf has fewer than 10 cups
while False:

    # TODO 2: unload one tray: 3 more cups, and one more tray used
    cups_on_shelf = cups_on_shelf
    trays_used = trays_used

    print("Tray", trays_used, "-- shelf now has", cups_on_shelf, "cups")

    # TODO 3: if the delivery has run out of trays, break out
    #         of the loop (otherwise this would run forever!)

print("Delivery ran out after", trays_used, "trays -- shelf has", cups_on_shelf, "cups")
