# Create variables
name = "Alice"          # string
age = 20                # integer
math_score = 88.5       # float
student = True          # boolean

# Print values and their data types
print(name, type(name))
print(age, type(age))
print(math_score, type(math_score))
print(student, type(student))

# Calculate the area of the rectangle
a = 5
b = 7
area = a * b
print("Area of rectangle:", area)

# Compare two numbers
x = 15
y = 20
print("Is x < y?", x < y)

# Input an integer from the keyboard
num = int(input("Enter an integer: "))

# Check the number is even or odd
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Practice Exercise 4:

# Print the 5 multiplication table using a for loop.
print("5 Times Table:")
for i in range(1, 11): 
    print("5 x", i, "=", 5 * i)

# Print the numbers from 1 to 20, but only even numbers.
print("Even numbers from 1 to 20:")
for i in range(1, 21):   
    if i % 2 == 0:   
        print(i, end = " ")

import math

def circle_area(r):
    return math.pi * r * r 


print(circle_area(5)) 

# Function to check if the input number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Read number of students
n = int(input("Enter number of students: "))

for _ in range(n):
    # Read student name
    name = input("\nEnter student name: ")

    # Read number of subjects
    subjects = int(input("Enter number of subjects: "))

    # Read subject marks
    marks = []
    for i in range(subjects):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)

    # Calculate average
    average = sum(marks) / subjects

    # Determine category
    if average >= 8.0:
        category = "Excellent"
    elif average >= 6.5:
        category = "Good"
    elif average >= 5.0:
        category = "Pass"
    else:
        category = "Fail"

    # Print result
    print(f"{name} – {average:.2f} – {category}")