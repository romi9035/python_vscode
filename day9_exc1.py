student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for student_name in student_scores:
    score = student_scores[student_name]
    if score <= 100 and score >= 91:
        student_grades[student_name] = "Outstanding"
    elif score <= 90 and score >= 81:
        student_grades[student_name] = "Exceeds Expectations"
    elif score <= 80 and score >= 71:
        student_grades[student_name] = "Acceptable"
    else:
        student_grades[student_name] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
