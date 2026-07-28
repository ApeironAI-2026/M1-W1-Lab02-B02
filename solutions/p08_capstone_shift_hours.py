# ============================================================
#  SOLUTION p08 -- CAPSTONE B -- Barista Shift Hours
#  The Cozy Bean  |  M1-W1 Lab02
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p08_capstone_shift_hours.py
#                 (run it from inside the M1-W1-Lab02 folder)
# ============================================================


timesheet = open("data/shift_hours.txt", "r")

for line in timesheet:

    # "101 Sara 6.5 7.0 8.0 5.5 6.0"
    #   -> ['101', 'Sara', '6.5', '7.0', '8.0', '5.5', '6.0']
    pieces = line.split()

    worker_id = pieces[0]
    name = pieces[1]

    # Add the five hour figures one at a time. Each is still
    # text, so float() repackages it into a real number first.
    total = 0.0
    for hours in pieces[2:]:
        total += float(hours)

    average = total / 5

    print(name, "ID", worker_id, "worked", total, "hours:", average, "/ day")

timesheet.close()

# 📌 In class this was Suzy, Brad and Jenn on an office timesheet.
# Same recipe, new aprons.
