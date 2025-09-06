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