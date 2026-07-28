# ============================================================
#  The Cozy Bean  --  Script 06: Tearing Up Order Slips
#
#  What this shows : split() breaks a line into pieces, float()
#                    turns a price piece into real money, and
#                    join() staples the pieces back together.
#  Lab STEPs       : STEP 16 and 17
#  How to run it   : python scripts/06_order_slips.py
#                    (run it from inside the M1-W1-Lab02 folder)
# ============================================================


# ---- Section 1  (STEP 16): tearing a slip into pieces ------
# .split() with nothing in the brackets breaks text at spaces.
slip = "latte with oat milk"
pieces = slip.split()
print(pieces)
print(len(pieces))

# .split(",") breaks it at commas instead -- perfect for our
# price list, where every line looks like  latte,3.50
line = "latte,3.50"
parts = line.split(",")
print(parts)

# Careful: those pieces are still TEXT. "3.50" cannot do maths
# until float() repackages it (just like Lab01's paper labels).
drink = parts[0]
price = float(parts[1])
print(drink, "costs", price * 2, "for two")

# The whole price list, one line at a time.
total = 0.0
for line in open("data/menu_prices.txt", "r"):
    parts = line.strip().split(",")
    print(parts[0], "->", float(parts[1]))
    total += float(parts[1])

print("One of everything costs:", total)


# ---- Section 2  (STEP 17): stapling pieces back together ---
# join() is the opposite of split. The text in front is the
# glue that gets put BETWEEN the pieces.
order_parts = ["latte", "muffin", "tea"]
print(", ".join(order_parts))
print(" + ".join(order_parts))
