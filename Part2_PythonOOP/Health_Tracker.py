'''
Exercise: Health Tracker (Encapsulation Practice)
🎯 Objective

You will build a class to manage personal health information.

Some data must be protected (not directly accessible).

Users should only interact with the object through public methods.

This demonstrates the concept of Encapsulation: hiding details and providing controlled access.

🚀 Requirements

Create a class HealthProfile with:

__weight (in kg) → private

__height (in meters) → private

name → public

Add safe setter/getter methods:

set_weight(new_weight) → only allow values > 0

set_height(new_height) → only allow values > 0

get_weight(), get_height()

Add a method calculate_bmi()

Formula: BMI = weight / (height ** 2)

Return a string category:

<18.5: “Underweight”

18.5–24.9: “Normal”

25–29.9: “Overweight”

>=30: “Obese”

Override __repr__ so that printing the object shows something like:

HealthProfile(name='Alice', weight=55kg, height=1.65m, BMI=20.2 Normal)
'''

#Health_Tracker 
class Tracker:
    def __init__(self, name: str, weight: float, height: float):
        self.name = name # public variable
        self.__weight = None
         self.__height = None
        
        def weight(self, new_weight: float) -> None:
           if new_weight <= 0:
              raise ValueError( "Weight must be positive" )
           self.__weight = float(new_weight)

        def height(self, new_height: float) -> None:
           if new_height <= 0:
              raise ValueError( "Weight must be positive" )
           self.__weight = float(new_height)

def calculate_bmi(self) -> str: 
   bmi = self.__weight / (self.__height ** 2)

   if bmi < 18.5:
      category = "Underweight"
   elif bmi < 25:
      category = "Normal"
   elif bmi < 30:
      category = "Overweight"
   else:
      category = "Obese"

def demo_HealthTracker() -> None:
   person = HealthTracker( "Alice", 55, 1.65 )
   print("Initial:", person)

   person.set_weight(70)
   print("After weight update:", person)

   person.set_height(1.70)
   print("After height update:", person)
   
