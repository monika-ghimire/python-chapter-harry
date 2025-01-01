# write  a program to calculate the grade of a student from marks from the following scheme

# 90 - 100 - Ex
# 80 - 90 -- A 
# 70 - 80 -- B 
# 60 - 70 -- C
# 50 - 60 -- D
# <50     -- F

def calculate_grade(marks):
    if 90 <= marks <= 100:
        grade = 'Ex'
    elif 80 <= marks < 90:
        grade = 'A'
    elif 70 <= marks < 80:
        grade = 'B'
    elif 60 <= marks < 70:
        grade = 'C'
    elif 50 <= marks < 60:
        grade = 'D'
    elif 0 <= marks < 50:
        grade = 'F'
    else:
        grade = 'Invalid marks'
    return grade

# Input from user
try:
    marks = float(input("Enter marks (0-100): "))
    grade = calculate_grade(marks)
    print(f"The grade is: {grade}")
except ValueError:
    print("Please enter a valid number.")
