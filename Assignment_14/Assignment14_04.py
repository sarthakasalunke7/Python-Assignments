# Write a lambda function which accepts two numbers and returns minimum number.

Min = lambda No1,No2: No1 < No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Min(Value1,Value2)

    if(Ret == True):
        print("Minimum number is : ",Value1)
    else:
        print("Minimum number is : ",Value2)

if __name__ == "__main__":
    main()