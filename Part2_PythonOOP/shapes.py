from __future__ import annotations
from abc import ABC, abstractmethod
from math import pi
from typing import Iterable, List

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, create_radius: float):
        self.radius = create_radius
    def area(self) -> float:
        return pi * (self.radius ** 2)
    def __repr__(self) -> str:
        return f"Circle(r={self.radius})"

class Retanggle(Shape):
    def __init__(self, create_width: float, create_height: float):
        self.width = create_width
        self.height = create_height
    def area(self):
        return self.width * self.height
    def __repr__(self) -> str:
        return f"Retanggle(w={self.width}, h={self.height})"

def demo_polymorphism() -> None:
    shapes: List[Shape] = [Circle(3), Retanggle(4, 5)]
    for s in shapes:
        print(f"{s}: area = {s.area():.2f}")

