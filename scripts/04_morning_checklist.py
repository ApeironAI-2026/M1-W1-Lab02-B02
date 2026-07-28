# ============================================================
#  The Cozy Bean  --  Script 04: The Morning Opening Checklist
#
#  What this shows : this is what a .py SCRIPT is for. A notebook
#                    is for tasting as you go; a script is the
#                    laminated checklist you rerun every morning,
#                    the same way, in one command.
#  Lab STEP        : STEP 11
#  How to run it   : python scripts/04_morning_checklist.py
#                    (run it from inside the M1-W1-Lab02 folder)
#
#  Windows and Mac use the exact same command. If "python" is
#  not recognised on Windows, try:  py scripts/04_morning_checklist.py
# ============================================================


print("=== THE COZY BEAN -- OPENING CHECKLIST ===")

# A list of jobs, and a for loop to walk through them.
opening_jobs = [
    "Unlock the front door",
    "Switch on the coffee machine",
    "Put the OPEN sign up",
    "Count the float in the till",
    "Bake the first tray of muffins",
]

step_number = 1
for job in opening_jobs:
    print(step_number, "-", job)
    step_number += 1

# A decision rule, exactly like the ones from script 01.
muffins_baked = 24

if muffins_baked >= 20:
    print("Muffin tray: full. Good to open!")
else:
    print("Muffin tray: low -- bake another batch.")

print("=== Ready to open. Have a lovely day. ===")
