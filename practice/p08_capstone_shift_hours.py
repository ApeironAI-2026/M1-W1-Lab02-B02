# ============================================================
#  PRACTICE p08 -- CAPSTONE B -- Barista Shift Hours
#  The Cozy Bean  |  M1-W1 Lab02
#
#  This is a CAPSTONE: the hours.txt exercise from class,
#  rebuilt with your own baristas.
#
#  YOUR TASK:
#    data/shift_hours.txt already exists. Every line looks like:
#       <id> <name> <five daily hour figures>
#    for example:
#       101 Sara 6.5 7.0 8.0 5.5 6.0
#    For each barista, work out the TOTAL hours and the average
#    per day (everyone works exactly 5 days), and print one line
#    each in the shape the class slide used.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Sara ID 101 worked 33.0 hours: 6.6 / day
#    Ben ID 102 worked 37.0 hours: 7.4 / day
#    Aisha ID 103 worked 34.0 hours: 6.8 / day
#
#  HINT: after  pieces = line.split()  you get a list where
#        pieces[0] is the id, pieces[1] is the name, and
#        pieces[2] onward are the hours -- still as TEXT.
#
#  How to run it: python practice/p08_capstone_shift_hours.py
#                 (run it from inside the M1-W1-Lab02 folder)
#
#  Stuck? See solutions/p08_capstone_shift_hours.py -- but give
#  it a real try first. This one is worth the struggle.
# ============================================================


timesheet = open("data/shift_hours.txt", "r")

for line in timesheet:

    # TODO 1: tear the line into its pieces with .split()
    pieces = []

    # TODO 2: pull out the id and the name
    worker_id = "?"
    name = "?"

    # TODO 3: add up the five hour figures. They are TEXT, so
    #         each one needs float() before it can be added.
    total = 0.0

    # TODO 4: work out the average per day (5 days)
    average = 0.0

    print(name, "ID", worker_id, "worked", total, "hours:", average, "/ day")

timesheet.close()
