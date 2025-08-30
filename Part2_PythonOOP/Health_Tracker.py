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

18.5-24.9: “Normal”

25-29.9: “Overweight”

>=30: “Obese”

Override __repr__ so that printing the object shows something like:

HealthProfile(name='Alice', weight=55kg, height=1.65m, BMI=20.2 Normal)
'''

class HealthProfile:
    def __init__(self, name: str, weight: float, height: float):
        self.name = name
        self.__weight = None
        self.__height = None
        self.set_weight(weight)
        self.set_height(height)

    def set_weight(self, new_weight: float) -> None:
        if new_weight > 0:
            self.__weight = new_weight
        else:
            raise ValueError("Weight must be greater than 0")

    def set_height(self, new_height: float) -> None:
        if new_height > 0:
            self.__height = new_height
        else:
            raise ValueError("Height must be greater than 0")

    def get_weight(self) -> float:
        return self.__weight

    def get_height(self) -> float:
        return self.__height

    def calculate_bmi(self) -> tuple[float, str]:
        bmi = self.__weight / (self.__height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        return round(bmi, 1), category

    def __repr__(self) -> str:
        bmi, category = self.calculate_bmi()
        return (f"HealthProfile(name='{self.name}', "f"weight={self.__weight}kg,"f"height={self.__height}m,"f"BMI={bmi} {category})")
    
def demo_health():
    profile = HealthProfile("Alice", 55, 1.65)
    print(profile)

    profile.set_weight(70)
    print("After weight update:", profile)

    profile.set_height(1.70)
    print("After height update:", profile)