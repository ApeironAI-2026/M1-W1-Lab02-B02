# ============================================================
#  The Cozy Bean  --  Script 02: Serving the Line
#
#  What this shows : for loops (serve everyone), range (counting),
#                    while loops (keep going until...), and break.
#  Lab STEPs       : STEP 4, 5, 6 and 7
#  How to run it   : python scripts/02_serving_the_line.py
#                    (run it from inside the M1-W1-Lab02 folder)
# ============================================================


# ---- Section 1  (STEP 4): serve everyone in the queue ------
# A for loop takes each item in turn and runs the indented
# block once per item. Four customers, one greeting each.
queue = ["Sara", "Ben", "Aisha", "Marcus"]

for customer in queue:
    print("Now serving:", customer)

# 📌 You saw this in class, with fruit:
fruits = ["apple", "banana", "orange", "mango"]

for fruit in fruits:
    print(fruit)


# ---- Section 2  (STEP 5): counting with range --------------
# 📌 From class: range(5) counts 0, 1, 2, 3, 4 -- five numbers,
# starting at 0, stopping BEFORE 5. Five loyalty stamps.
for i in range(5):
    print("Stamp number:", i)


# ---- Section 3  (STEP 6): restocking with while ------------
# A for loop needs to know how many times up front. A while
# loop just keeps going until its question turns False --
# perfect for "keep restocking until the shelf is full".
# 📌 The class counter pattern, in shop clothes:
cups_on_shelf = 0

while cups_on_shelf < 5:
    print("Restocking... cups on shelf:", cups_on_shelf)
    cups_on_shelf += 1   # += 1 means "add one to this jar"

print("Shelf is full!")


# ---- Section 4  (STEP 7): the fire alarm (break) -----------
# break leaves the loop immediately, no matter how many items
# are left. Usually an if decides when.
for customer in queue:
    if customer == "Aisha":
        print("FIRE ALARM -- everybody out!")
        break
    print("Served:", customer)
