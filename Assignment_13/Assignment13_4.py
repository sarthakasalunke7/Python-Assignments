# Write a program which accepts one number and prints binary equivalent.

def DisplayBinary(No):
    Digit = 0
    data = []

    while(No != 0):
        Digit = No % 2
        data.append(Digit)
        No = int(No / 2)

    data.reverse()

    return data

def main():
    Ret = []

    Value = int(input("Enter a number : "))

    Ret = DisplayBinary(Value)

    print("Binary Equivalent is : ",*Ret)

if __name__ == "__main__":
    main()


