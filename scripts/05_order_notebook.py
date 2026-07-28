# ============================================================
#  The Cozy Bean -- Script 05: The Order Notebook
#  Lab STEPs 12-15.
#  Shows: writing to a file, the famous missing-\n bug, reading
#         a file back, and the r / w / a modes.
#  Run:   python scripts/05_order_notebook.py (from M1-W1-Lab02/)
#  Note:  this CREATES files in data/. Safe to rerun any time.
# ============================================================

# ---- Section 1  (STEP 12): writing the notebook ------------
# open(name, "w") opens a page for writing. "with" closes it
# for you when the block ends -- the tidy way.
with open("data/end_of_day.txt", "w") as report:
    report.write("THE COZY BEAN -- END OF DAY\n")
    report.write("Cups sold: 63\n")
    report.write("Muffins sold: 24\n")

print("Report written to data/end_of_day.txt")

# ---- Section 2  (STEP 13): the missing \n bug --------------
# 📌 From class. Three writes, no \n anywhere...
with open("data/sample.txt", "w") as f:
    f.write("Python")
    f.write("Machine Learning")
    f.write("AI Fundamentals")

file = open("data/sample.txt", "r")
print(file.read())   # ...and they all smoosh into ONE line
file.close()

# \n means "start a new line here". With it, they behave:
with open("data/sample_fixed.txt", "w") as f:
    f.write("Python\n")
    f.write("Machine Learning\n")
    f.write("AI Fundamentals\n")

print(open("data/sample_fixed.txt", "r").read())

# ---- Section 3  (STEP 14): reading yesterday's notebook ----
# The template from class: open it, then loop over its lines.
# .strip() trims the invisible newline off each end.
file = open("data/orders.txt", "r")
for line in file:
    print("Order:", line.strip())
file.close()   # always close what you open by hand

# ---- Section 4  (STEP 15): three ways to read --------------
file = open("data/orders.txt", "r")
print(file.readline().strip())   # just the next single line
file.close()

file = open("data/orders.txt", "r")
print(len(file.readlines()))     # every line, as a list
file.close()

# Modes: "r" read | "w" write (fresh page, ERASES!) | "a" append
with open("data/end_of_day.txt", "a") as report:
    report.write("Signed: Sara\n")

print(open("data/end_of_day.txt", "r").read())
