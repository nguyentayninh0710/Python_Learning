'''
scenario

A transportation company manages different types of vehicles:

Vehicle (parent class): has plateNumber, capacity.

Car (subclass): inherits from Vehicle, adds fuelType.

Bus (subclass): inherits from Vehicle, adds routeNumber.

The system must:

Create a list of Car and Bus objects.

Write a linear search to find a Bus by its routeNumber.

Write a selection sort to sort the list of Car by capacity.

Write a filtering function to return all Car objects with fuelType = "Electric".

Expected Output

cars = [
    Car("51A-12345", 4, "Petrol"),
    Car("51B-22222", 4, "Electric"),
    Car("51C-33333", 7, "Diesel"),
    Car("51D-44444", 5, "Electric")
]

buses = [
    Bus("79A-11111", 30, "R01"),
    Bus("79B-22222", 45, "R02"),
    Bus("79C-33333", 40, "R03")
]

== Linear Search Bus ==
Bus 79B-22222, capacity 45, route R02

== Selection Sort Cars by Capacity ==
Car 51A-12345, capacity 4, fuel: Petrol
Car 51B-22222, capacity 4, fuel: Electric
Car 51D-44444, capacity 5, fuel: Electric
Car 51C-33333, capacity 7, fuel: Diesel

== Filter Electric Cars ==
Car 51B-22222, capacity 4, fuel: Electric
Car 51D-44444, capacity 5, fuel: Electric
'''

from typing import List, Optional

class Vehicle:
    def __init__(self, plateNumber: str, capcity: int):
        self.plateNumber = plateNumber
        self.capacity = capcity

class Car(Vehicle):
    def __init__(self, plateNumber: str, capacity: int, fuelType: str):
        super().__init__(plateNumber, capacity)
        self.fuelType = fuelType

    def __repr__(self) -> str:
        return f"Car {self.plateNumber}, capacity {self.capacity}, fuel: {self.fuelType}"
        
class Bus(Vehicle):
    def __init__(self, plateNumber: str, capacity: int, routeNumber: str):
        super().__init__(plateNumber, capacity)
        self.routeNumber = routeNumber

    def __repr__(self) -> str:
        return f"Bus {self.plateNumber}, capacity {self.capacity}, route{self.routeNumber}"
    
def find_bus_by_route(buses: List[Bus], route:str) -> Optional[Bus]:
    for bus in buses:
        if bus.routeNumber == route:
            return bus
    return None

def selection_sort_cars(cars: List[Car]) -> None:
    n = len(cars)
    for i in range(n):
        min_index = i
        for j in range (i+1, n):
            if cars[j].capacity < cars[min_index].capacity:
                min_index = j

def filter_electric_cars(cars):
    return [car for car in cars if car.fuelType == "Electric"]

def demo_transportation() -> None:
    cars = [
        Car("51A-12345", 4, "Petrol"),
        Car("51B-22222", 4, "Electric"),
        Car("51C-33333", 7, "Diesel"),
        Car("51D-44444", 5, "Electric")
    ]
    buses = [
        Bus("79A-11111", 30, "R01"),
        Bus("79B-22222", 45, "R02"),
        Bus("79C-33333", 40, "R03")
    ]

    print("== Linear Search Bus ==")
    found = find_bus_by_route(buses, "R02")
    if found:
        print(found)

    print("== Selection Sort Cars by Capacity ==")
    selection_sort_cars(cars)
    for car in cars:
        print(car)

    print("== Filter Electric Cars ==")
    electric_cars = filter_electric_cars(cars)
    for car in electric_cars:
        print(car)
    