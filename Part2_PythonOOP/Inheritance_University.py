from __future__ import annotations
from typing import List, Optional
#superclass
class Person:
    def __init__(self, createName: str, createAge: int):
        self.name = createName
        self.age = createAge
    
    def introduce(self) -> str:
        return f"I am {self.name}, {self.age} years old."
#subclass
class Student(Person):
    def __init__(self, createName, createAge, student_id: str):
        super().__init__(createName, createAge)
        self.student_id = student_id
    def introduce(self) -> str:
        return f"Student {self.name} (ID: {self.student_id}, age: {self.age})"

def find_student_by_id(students: List[Student], student_id: str) -> Optional[Student]:
    for st in students:
        if st.student_id == student_id:
            return st
    return None

def demo_inheritance() -> None: 
    studentList: List[Student]= [
        Student("An", "17", "std_123"),
        Student("Vu", "17", "std_456"),
        Student("Khoa", "17", "std_789")
    ]

    for st in studentList:
        print(st.introduce())
    
    print("Search student std_456", find_student_by_id(studentList, "std_456").introduce())