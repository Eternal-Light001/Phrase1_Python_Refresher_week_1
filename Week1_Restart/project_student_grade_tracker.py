# STEP (PROCEDURE)
# A CLI app that takes a nested dict of students → subjects → scores, computes each student's average and grade band, identifies top/bottom performers, and prints a formatted report card for each student with a final class summary.


# TEST TABLE (EXPECTATION):- 
# SCENARIO 1 — the default students dict above:
#   Ada:   avg (90+85+88)/3 = 87.67 → Grade B
#   Bob:   avg (72+68+75)/3 = 71.67 → Grade C
#   Cleo:  avg (95+92+98)/3 = 95.00 → Grade A
#   Dee:   avg (55+62+48)/3 = 55.00 → Grade F
#   Eve:   avg (78+88+82)/3 = 82.67 → Grade B
#   Summary: 5 students | A: 1 | B: 2 | C: 1 | D: 0 | F: 1
#   Top: Cleo | Bottom: Dee
#   Class avg: (87.67+71.67+95+55+82.67)/5 = 78.40

# SCENARIO 2 — change Dee's math from 55 → 90 (edge: grade boundary):
#   Dee: avg (90+62+48)/3 = 66.67 → Grade D
#   Summary: A: 1 | B: 2 | C: 1 | D: 1 | F: 0
#   Class avg changes accordingly

# SCENARIO 3 — change Bob's math from 72 → 70 (edge: exact boundary):
#   Bob: avg (70+68+75)/3 = 71.00 → still Grade C (70 is C, not B)
#   Only the "at or above 70" rule is tested
#   Summary unchanged — Bob stays C


# Script
students = {
    "Ada":    {"math": 90, "english": 85, "science": 88},
    "Bob":    {"math": 72, "english": 68, "science": 75},
    "Cleo":   {"math": 95, "english": 92, "science": 98},
    "Dee":    {"math": 55, "english": 62, "science": 48},
    "Eve":    {"math": 78, "english": 88, "science": 82},
}

# Function & Logic
def calculate_average(scores_dict):
    """Computes the mean score from a student's sub-dictionary."""
    total = sum(scores_dict.values())
    count = len(scores_dict)
    return round(total / count, 2)

def classify_grades(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def find_top_student(students_dict):
    top_student_name = ""
    highest_average = 0

    for name, scores in students_dict.items():
        total = sum(scores.values())
        count = len(scores)              
        average = round(total / count, 2)

        if average > highest_average:     
            highest_average = average     
            top_student_name = name      
    return top_student_name

def find_bottom_student(students_dict):
    bottom_student_name = ""
    lowest_average = float('inf')

    for name, scores in students_dict.items():
        total = sum(scores.values())
        count = len(scores)              
        average = round(total / count, 2)

        if average < lowest_average:     
            lowest_average = average     
            bottom_student_name = name      
    return bottom_student_name


def main():
    all_averages = []
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for name, score in students.items():
        average = calculate_average(score)
        grade = classify_grades(average)

        all_averages.append(average)
        grade_counts[grade] += 1

        print("="*30)
        SRC = "STUDENTS REPORT CARD"
        print(f"{SRC:^30}")
        print("="*30)

        print(f"\nName:    {name}")
        print(f"Math:    {score['math']}")
        print(f"English: {score['english']}")
        print(f"Science: {score['science']}")

        print("-"*30)
        print(f"Average: {average:.2f}%")
        print(f"Grade:   {grade}")
        print("="*30)
        print("\n")

    print("="*30)
    CS = "CLASS SUMMARY"
    print(f"{CS:^30}")
    print("="*30)

    print(f"Total Students: {len(students)}")
    print(f"\nClass Average: {round(sum(all_averages) / len(all_averages), 2)}%")
    print(f"Top Performer: {find_top_student(students)}")
    print(f"Bottom Performer: {find_bottom_student(students)}")

    print("-"*30)
    print("Grade Distribution: ")
    for grade, count in grade_counts.items():
        print(f"  {grade}: {count}")
        
if __name__ == "__main__":
    main()