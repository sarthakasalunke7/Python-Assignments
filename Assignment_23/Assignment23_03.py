# Write a Python program to implement a class named Numbers with the following specifications:
# • The class should contain one instance variable:
#   ◦ Value
# • Define a constructor (__init__) that accepts a number from the user and initializes Value.
# • Implement the following instance methods:
#   ◦ ChkPrime() – returns True if the number is prime, otherwise returns False
#   ◦ ChkPerfect() – returns True if the number is perfect, otherwise returns False
#   ◦ Factors() – displays all factors of the number
#   ◦ SumFactors() – returns the sum of all factors
#       (You may use this method as a helper in ChkPerfect() if required)
# • Create multiple objects and call all methods.

class Numbers:
    def __init__(self,No):
        self.Value = No

    def ChkPrime(self):
        if(self.Value <= 1):
            return False
        
        for i in range(2, int(self.Value / 2)+1):
            if(self.Value % i == 0):
                return False
        
        return True

    def ChkPerfect(self):
        if(self.Value == self.SumFactors()):
            return True
        
        else:
            return False

    def Factors(self):
        print("Factors are : ")

        for i in range(1, self.Value + 1):
            if(self.Value % i == 0):
                print(i, end=" ")
        print()

    def SumFactors(self):
        self.Sum = 0

        for i in range(1, self.Value):
            if(self.Value % i == 0):
                self.Sum = self.Sum + i
        
        return self.Sum

def main():
    obj1 = Numbers(11)
    obj2 = Numbers(6)

    print("-"*25)
    print("Prime Number : ",obj1.ChkPrime())
    print("Perfect Number : ",obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of all factors : ",obj1.SumFactors())

    print("-"*25)
    print("Prime Number : ",obj2.ChkPrime())
    print("Perfect Number : ",obj2.ChkPerfect())
    obj2.Factors()
    print("Sum of all factors : ",obj2.SumFactors())

    print("-"*25)

if __name__ == "__main__":
    main()