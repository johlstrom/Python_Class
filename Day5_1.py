# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

number_heights = 0
for i in student_heights:
  number_heights += 1

total_heights = 0
for heights in student_heights:
  total_heights += heights


avg_height = round(total_heights / number_heights)

print(avg_height)