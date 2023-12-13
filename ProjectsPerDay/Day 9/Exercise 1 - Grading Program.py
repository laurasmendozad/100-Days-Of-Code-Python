student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for name,score in student_scores.items():
    if score in range(91,101):
        grade = 'Outstanding'
    elif score in range(81,91):
        grade = 'Exceeds Expectations'
    elif score in range(71,81):
        grade = 'Acceptable'
    elif score <= 70:
        grade = 'Fail'

    student_grades[name] = grade

# 🚨 Don't change the code below 👇
print(student_grades)