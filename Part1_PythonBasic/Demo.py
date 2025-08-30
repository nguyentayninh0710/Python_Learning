# 1 Variable and Datatype
# String 
name = "Alice"
# Integer
age = 18
# Float
height = 1.65
# Boolean 
is_student = True

print("Name:", name, type(name), "Age:", age, type(age), )

# 2 Selection IF
x = 100
y = 20
if x < y:
    print("x less than y")
else: 
    print("x greater than y")

# if - elis -else 
score = 85
if score > 90: 
    print("every good")
    # if score <= 90 and score >=70
elif score >= 70: 
    print("good")
    # if score < 70
else:
    print("normal")

# < > <= >= == !=

#Arithmetic operators
# + - * / // % **
a = 10 
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#Logic operators
a = True # 1
b = False # 0

#AND
# A | B | A AND B
# 0 | 0 |    0
# 1 | 0 |    0
# 0 | 1 |    0
# 1 | 1 |    1

#OR
# A | B | A OR B
# 0 | 0 |    0
# 1 | 0 |    1
# 0 | 1 |    1
# 1 | 1 |    1

#NOT
# A | NOT A 
# 0 | 1
# 1 | 0

print(a and b) # False
print(a or b) # True
print(not a) # False

#Practice Exercise 1:
#Create variables: name, age, math score, student (True/False).
#Print all of them on the screen with their data types.
#An review and do again 


#Practice Exercise 2:
#Calculate the area of the rectangle (a=5, b=7).
#Compare the two numbers x=15, y=20 and print the result (x < y).

#INPUT from keyboard 
# myName = input("input your name: ")
# print("Hello ", myName)

# myAge = int(input("input your age: "))
# demo = myAge + 3
# print("Your age ", myAge)

# myHeight = float(input("input your height: "))

#Practice Exercise 3:
#Write a program to input an integer from the keyboard and print out whether the number is even or odd.

# LOOP
# FOR LOOP
# range(start, stop)
for index in range(1,6):
    print(index)
# range(start, stop, step)
for index in range(1,6,2):
    print(index)
# While LOOP
print("_______________________WHILE LOOP______________________")
count = 0
while count < 5:
    print(count)
    #count = count + 1
    count += 1

List = ["Audi", "Bmw", "Toyota"]
for car in List:
    print("Brand:", car)


# Practice Exercise 4:

# Print the 5 multiplication table using a for loop.
print("5 Times Table")
for i in range(1, 11): 
    print("5 x", i, "=", 5 * i)

# Print the numbers from 1 to 20, but only print even numbers.
print("Even numbers from 1 to 20")
for i in range(1, 21):   
    if i % 2 == 0:   
        print(i, end = " ")
        
#Function
def greet(name):
    return f"Hello {name}"

print(greet("Alice"))
print(greet("Vu"))

def add(a,b):
    return a + b

print("4 + 3 =", add(4,3))
print("2 + 1 =", add(2,1))

# Practice Exercise 5:

# Write a function to calculate the area of ​​a circle (parameter: radius r).
import math
math.pi

# Write a function to check if the input number is prime.
math.sqrt
# 0 1 not prime
# 2 
# N sqrt = [(√N) + 1] ~ , check 2 to √N | N can % any number on range(1,√N) => yes => not prime 
# end range => dont have any number can % for N => prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(4))

# Problem Statement

# A school wants to keep track of students’ average marks and classification. Each student has:

# a name (string)

# a set of subject marks (real numbers)

# You need to write a program that:

# Reads the number of students n.

# For each student:

# Reads the name.

# Reads the number of subjects.

# Reads all subject marks.

# Calculates the average mark.

# Determines the grade category:

# >= 8.0: Excellent

# >= 6.5: Good

# >= 5.0: Pass

# < 5.0: Fail

# Outputs the result for each student in the form: Name – Average – Category

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


