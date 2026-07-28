# ============================================================
#  PRACTICE p05 -- The End-of-Day Report
#  The Cozy Bean  |  M1-W1 Lab02
#
#  YOUR TASK:
#    Write the shop's end-of-day report to data/my_report.txt,
#    three lines, each one ending in \n so they do not all
#    smoosh onto one line. Then read the file back and print
#    what it says, to prove it worked.
#    The three lines are:
#      THE COZY BEAN -- END OF DAY
#      Cups sold: 63
#      Muffins sold: 24
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Report saved to data/my_report.txt
#    Here is what the file says:
#    THE COZY BEAN -- END OF DAY
#    Cups sold: 63
#    Muffins sold: 24
#
#  HINT: without \n on the end of each write, all three lines
#        land on top of each other -- the bug from STEP 13.
#
#  How to run it: python practice/p05_end_of_day_report.py
#                 (run it from inside the M1-W1-Lab02 folder)
#
#  NOTE: this file CREATES data/my_report.txt for you. You never
#  have to make a file by hand. It is safe to run many times.
#
#  Stuck? See solutions/p05_end_of_day_report.py -- but give it
#  a real try first. The struggle makes it stick.
# ============================================================


# "w" means "fresh page" -- it wipes the file and starts again.
with open("data/my_report.txt", "w") as report:

    # TODO 1: write the three report lines. Do not forget the \n
    #         on the end of each one!
    report.write("THE COZY BEAN -- END OF DAY")

print("Report saved to data/my_report.txt")
print("Here is what the file says:")

# TODO 2: read the file back and print each line. Use .strip()
#         so you do not get extra blank lines.
report = open("data/my_report.txt", "r")

report.close()
