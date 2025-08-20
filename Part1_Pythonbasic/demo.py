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