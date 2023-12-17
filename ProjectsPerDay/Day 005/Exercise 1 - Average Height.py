# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
s = 0
n = 0
for items in student_heights:
    s += items
    n += 1
a = round(s/n)
print(f"total height = {s}")
print(f"number of students = {n}")
print(f"average height = {a}")
