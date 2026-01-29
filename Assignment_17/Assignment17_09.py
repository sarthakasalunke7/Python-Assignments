# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934        Output : 7

def Digit(No):
    Count = 0

    while(No != 0):
        No = int(No / 10)
        Count = Count + 1

    return Count

def main():
    Ret = 0
    Value = int(input("Enter a number : "))

    Ret = Digit(Value)

    print(Ret)

if __name__ == "__main__":
    main()