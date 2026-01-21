# Write a program which accepts one number and prints factorial of that number.
# Input: 5
# Output: 120

def Factorial(Value):
    fact = 1
    
    for i in range(1,Value+1):
        fact = fact * i
        i = i + 1

    return fact

def main():
    print("Enter a number : ")
    No = int(input())
    
    Ret = Factorial(No)

    print("Factorial is : ",Ret)


if __name__ == "__main__":
    main()