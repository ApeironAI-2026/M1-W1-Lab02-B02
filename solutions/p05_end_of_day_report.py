# ============================================================
#  SOLUTION p05 -- The End-of-Day Report
#  The Cozy Bean  |  M1-W1 Lab02
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p05_end_of_day_report.py
#                 (run it from inside the M1-W1-Lab02 folder)
# ============================================================


# "w" means "fresh page" -- it wipes the file and starts again.
with open("data/my_report.txt", "w") as report:
    report.write("THE COZY BEAN -- END OF DAY\n")
    report.write("Cups sold: 63\n")
    report.write("Muffins sold: 24\n")

print("Report saved to data/my_report.txt")
print("Here is what the file says:")

# Read it back one line at a time. .strip() trims the invisible
# newline off the end, so print does not add a second one.
report = open("data/my_report.txt", "r")

for line in report:
    print(line.strip())

report.close()
