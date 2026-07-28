# ============================================================
#  SOLUTION p07 -- CAPSTONE A -- The Biggest Order of the Day
#  The Cozy Bean  |  M1-W1 Lab02
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p07_capstone_biggest_order.py
#                 (run it from inside the M1-W1-Lab02 folder)
# ============================================================


def biggest_order(filename):

    orders = open(filename, "r")

    # "Longest so far" starts empty, so the very first real
    # line is bound to beat it.
    longest = ""

    for line in orders:
        order = line.strip()

        if len(order) > len(longest):
            longest = order

    orders.close()

    print("The biggest order of the day was", len(longest), "characters long:")
    print(longest)


biggest_order("data/orders.txt")

# 📌 In class this was written as longest_line(filename), reading
# a poem instead of an order book. Same recipe card, new shop.
