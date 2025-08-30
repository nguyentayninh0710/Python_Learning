#Encapsulation
class BankAccount:
    """
    Encapsulation: protect the balance and access via methods.
    In Python, name-mangling using __balance helps discourage direct access.
    """
    def __init__(self, owner: str, opening_balance: float = 0.0): 
        self.owner = owner # public variable
        self.__balance = float(opening_balance) # private 
    
    def get_balance(self) -> float:
        return self.__balance
    
    def deposit(self, amount: float) -> None:
        if amount <= 0: 
            raise ValueError("Amount must be positive")
        else:
            self.__balance += amount
    def withdraw(self, amount: float) -> None:
        if amount <= 0: 
            raise ValueError("Amount must be positive")
        elif amount > self.__balance:
            raise ValueError("Insufficient funds")
        else: 
            self.__balance -= amount
    
    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner}, balance={self.__balance})"

def demo_encapsulation() -> None:
    acc = BankAccount("ALice", 100.0)
    print("Initial: ", acc)

    acc.deposit(50)
    print("After deposit 50$:", acc)

    acc.__balance = 100000 

    print("Hacked:", acc)

    acc.withdraw(90)
    print("After withdraw 90$:", acc)


