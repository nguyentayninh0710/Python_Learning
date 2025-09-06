'''
Context
A government tax system must calculate the tax payable for different types of businesses.
Each business type shares a common method calculate_tax(), but the implementation differs. This demonstrates polymorphism.

Your Task
1) Define an abstract base class Business:
    +) Has an attribute revenue.
    +) Defines an abstract method calculate_tax().
2) Implement three subclasses:
    +) SoleProprietorship: Tax = 10% of revenue.
    +) Corporation: Tax = 20% of revenue − 5,000 allowance.
    +) Startup: Tax = 5% of revenue, but if revenue < 50,000 then Tax = 0.
3) Write a function total_tax(businesses)
    +) Accepts a list of businesses.
    +) Calls calculate_tax() on each business (without checking type).
    +) Returns the sum of all taxes.

4) Test your code with the following data:
    +) SoleProprietorship with revenue = 80,000
    +) Corporation with revenue = 100,000
    +) Startup with revenue = 40,000

Expected output:
Sole Proprietorship: Tax = 8000.00
Corporation: Tax = 15000.00
Startup: Tax = 0.00
Total tax collected: 23000.00
'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Business (ABC):
    def __init__(self, revenue:float):
        self.revenue = revenue

    def calculate_tax(self) -> float:
        pass

class SoleProprietorship(Business):
    def calculate_tax(self) -> float:
        return self.revenue * 0.10
    
class Corporation(Business):
    def calculate_tax(self) -> float:
        return max(0, (self.revenue * 0.20)-5000)
    
class Startup(Business):
    def calculate_tax(self) -> float:
        if self.revenue * 0.1 < 50000:
            return 0
        return self.revenue * 0.05
    
def total_tax(businesses: List[Business]) -> float:
    total = 0
    for b in businesses:
        total += b.calculate_tax()
    return total

def demo_polymorphism_business() -> None:
    businesses: List[Business] = [
        SoleProprietorship(80000),
        Corporation(100000),
        Startup(4000)
    ]
    for b in businesses:
        print(f"{b.__class__.__name__}: Tax = {b.calculate_tax():.2f}")
    print("Total tax collected:", f"{total_tax(businesses):.2f}")