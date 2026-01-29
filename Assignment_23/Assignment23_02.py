# Write a Python program to implement a class named BankAccount with the following requirements:
# • The class should contain two instance variables:
#   ◦ Name (Account holder name)
#   ◦ Amount (Account balance)
# • The class should contain one class variable:
#   ◦ ROI (Rate of Interest), initialized to 10.5
# • Define a constructor (__init__) that accepts Name and initial Amount.
# • Implement the following instance methods:
#   ◦ Display() – displays account holder name and current balance
#   ◦ Deposit() – accepts an amount from the user and adds it to balance
#   ◦ Withdraw() – accepts an amount from the user and subtracts it from balance
#       (Ensure withdrawal is allowed only if sufficient balance exists)
#   ◦ CalculateInterest() – calculates and returns interest using formula:
#     Interest = (Amount * ROI) / 100
# • Create multiple objects and demonstrate all methods.

class BankAccount:
    ROI = 10.5

    def __init__(self, AccHolder, AccBalance):
        self.Name = AccHolder
        self.Amount = AccBalance

    def Display(self):
        print("Acount Holder Name : ",self.Name)
        print("Account Balance : ",self.Amount)

    def Deposit(self):
        self.DAmt = int(input("Enter Deposit Amount : "))
        
        if (self.DAmt > 0):
            self.Amount = self.Amount + self.DAmt
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def Withdraw(self):
        self.WAmt = int(input("Enter Withdrawal Amount : "))

        if(self.WAmt <= self.Amount):
            self.Amount = self.Amount - self.WAmt
            print("Amount withdrawn successfully.")

        else:
            print("Insufficient balance.")

    def CalculateInterest(self):
        self.Interest = (self.Amount * BankAccount.ROI) / 100
        return self.Interest

def main():
    obj1 = BankAccount("Name1",50000)
    obj2 = BankAccount("Name2",500)

    print("-"*25)
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    print("Interest is : ",obj1.CalculateInterest())

    print("-"*25)
    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    print("Interest is : ",obj2.CalculateInterest())

    print("-"*25)

if __name__ == "__main__":
    main()