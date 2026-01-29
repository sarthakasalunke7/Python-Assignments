# Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934        Output : 37

def DigitSum(No):
    Sum = 0

    while(No != 0):
        Sum = Sum + (No % 10)
        No = int(No / 10)

    return Sum

def main():
    Ret = 0
    Value = int(input("Enter a number : "))

    Ret = DigitSum(Value)

    print(Ret)

if __name__ == "__main__":
    main()