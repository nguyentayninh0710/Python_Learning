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



