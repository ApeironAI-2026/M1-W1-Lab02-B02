# ============================================================
#  PRACTICE p07 -- CAPSTONE A -- The Biggest Order of the Day
#  The Cozy Bean  |  M1-W1 Lab02
#
#  This is a CAPSTONE: the exercise from class (a function that
#  finds the longest line in a file), rebuilt in the coffee shop.
#
#  YOUR TASK:
#    At closing time you give a small prize for the biggest
#    order of the day. Write a recipe card (function) called
#    biggest_order(filename) that:
#      - opens the file
#      - walks through every line
#      - remembers the longest one it has seen so far
#      - prints how many characters long it was, and what it said
#    Then call it on "data/orders.txt".
#    Use .strip() on each line so the invisible newline does not
#    get counted.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    The biggest order of the day was 53 characters long:
#    large hot chocolate with extra marshmallows and cream
#
#  HINT: start with a jar called longest holding "" (empty
#        text), and replace it whenever a longer line turns up.
#
#  How to run it: python practice/p07_capstone_biggest_order.py
#                 (run it from inside the M1-W1-Lab02 folder)
#
#  Stuck? See solutions/p07_capstone_biggest_order.py -- but
#  give it a real try first. This one is worth the struggle.
# ============================================================


def biggest_order(filename):

    orders = open(filename, "r")

    # TODO 1: start with an empty "longest so far"
    longest = ""

    for line in orders:

        # TODO 2: tidy the line with .strip()

        # TODO 3: if this line is longer than the longest so
        #         far, it becomes the new longest
        pass

    orders.close()

    # TODO 4: print the two result lines
    print("The biggest order of the day was", 0, "characters long:")
    print(longest)


biggest_order("data/orders.txt")
