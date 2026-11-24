# STEPS:-

# Section 1 — pass demo (tiny)
# Write a for loop over range(3) with pass inside.
# Print after the loop: "pass demo: loop completed without errors"
# Purpose: prove pass runs clean

# Section 2 — else-on-loop demo (both patterns)
# Part A — the else-on-loop pattern:
# List: [10, 20, 30, 40]
# Loop through it, check if 30 is in the list
# If found → print, break
# Add else: → print "30 not found"
# Expected: else does not run (found at 30, broke out)

# Part B — same logic with a flag variable:
# Same list, same search
# Use a found = False flag instead of else-on-loop
# Expected: same output
# Comment: "Both patterns do the same thing. else-on-loop is fewer lines but less obvious. Flag pattern is more readable."

# Part C — a break-less loop:-
# Search for 99 in [10, 20, 30]
# Loop finishes without break → else fires → print "99 not found"
# This is where the else-on-loop magic shows.

# Section 3 — Nested iteration — list of dicts
# Loop through the list
# Print each student's name and score
# Bonus: also print each student's grade band using match-case (A ≥ 85, B ≥ 70, C ≥ 50, else F) — this shows Day 5 skills applied to nested data

# Section 4 — Nested iteration — dict of dicts
# Loop through the outer dict
# For each student, loop through their subjects
# Print "Ada — math: 85"
# Bonus: compute each student's average and print it


# TEST TABLE (EXPECTATION):-
# Loop over [10,20,30,40] searching 30  --> else does NOT fire (broke at 30)
# Loop over [10,20,30] searching 99     --> else DOES fire ("99 not found")
# students[0]["name"]                   --> "Ada"
# student_grades["Ada"] -- ["math"]     -->85
# Ada's average (85+90)/2               --> 87.5

# Section 1 — pass demo (tiny)
for i in range(3):
    pass
print("pass demo: loop completed without errors")

# Section 2 — else-on-loop demo (both patterns)
# Part A — the else-on-loop pattern:
lists = [10, 20, 30, 40]
for element in lists:
    if element == 30:
        print("found")
        break
else:
    print("not found")

# Part B — same logic with a flag variable:
found = False
for item in lists:
    if item == 30:         
        found = True
        break

if found:
    print("found")
else:
    print("not found")

# Part C — a break-less loop:-
values = [10, 20, 30]
for n in values:
    if n == 99:
        print("99 Found.")
else:
    print("99 not found")

# Section 3 — Nested iteration — list of dicts
students = [
    {"name": "Ada", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Cleo", "score": 91},
]

for student in students:
    each_student = f"{student['name']} -- {student['score']}"

    match student["score"]:
        case score if score >= 85:
            print(f"{each_student} --- Grade A")
        case score if score >= 70:
            print(f"{each_student} --- Grade B")
        case score if score >= 50:
            print(f"{each_student} --- Grade C")
        case _:
            print(f"{each_student} --- Grade F")

print()  # blank line for readability

# Section 4 — Nested iteration — dict of dicts
student_grades = {
    "Ada": {"math": 85, "english": 90},
    "Bob": {"math": 72, "english": 68},
    "Cleo": {"math": 91, "english": 88},
}

for name, scores in student_grades.items():
    for subject, score in scores.items():
        print(f"{name} — {subject}: {score}")
    
    print()
    average = sum(scores.values()) / len(scores)
    print(f"{name}'s average: {average:.2f}")
    print() # blank line for readability
    

