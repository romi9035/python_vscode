# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total_height = 0
total_count = 0
for heights in student_heights:
  total_height += heights
  total_count += 1
avg_height = round( total_height / total_count)
print(avg_height)