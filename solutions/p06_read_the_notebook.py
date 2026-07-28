# ============================================================
#  SOLUTION p06 -- Reading the Order Notebook
#  The Cozy Bean  |  M1-W1 Lab02
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p06_read_the_notebook.py
#                 (run it from inside the M1-W1-Lab02 folder)
# ============================================================


notebook = open("data/orders.txt", "r")

order_number = 0

for line in notebook:
    order_number += 1
    # The dot is glued straight onto the number, so we build
    # that piece as text first, then let print add the space.
    print(str(order_number) + ".", line.strip())

notebook.close()

print("Total orders:", order_number)
