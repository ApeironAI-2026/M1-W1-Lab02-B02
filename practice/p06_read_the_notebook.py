# ============================================================
#  PRACTICE p06 -- Reading the Order Notebook
#  The Cozy Bean  |  M1-W1 Lab02
#
#  YOUR TASK:
#    Read yesterday's order notebook, data/orders.txt, and print
#    every order as a numbered line. Trim the invisible newline
#    off each one. Finish by printing how many orders there were.
#    (The file already exists -- you do not create anything.)
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    1. latte with oat milk
#    2. espresso
#    3. large hot chocolate with extra marshmallows and cream
#    4. cappuccino and a blueberry muffin
#    5. tea
#    Total orders: 5
#
#  HINT: keep a counter jar that goes up by 1 each time round
#        the loop, and use it for the number at the front.
#
#  How to run it: python practice/p06_read_the_notebook.py
#                 (run it from inside the M1-W1-Lab02 folder)
#
#  Stuck? See solutions/p06_read_the_notebook.py -- but give it
#  a real try first. The struggle makes it stick.
# ============================================================


notebook = open("data/orders.txt", "r")

order_number = 0

for line in notebook:

    # TODO 1: add 1 to the order number

    # TODO 2: print the number, a dot, and the tidied-up order.
    #         Use .strip() to trim the invisible newline.
    print(line)

notebook.close()

# TODO 3: print how many orders there were in total
print("Total orders:", 0)
