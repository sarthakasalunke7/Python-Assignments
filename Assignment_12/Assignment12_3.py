# Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def Calculation(Value1, Value2):
    return Value1+Value2, Value1-Value2, Value1*Value2, Value1/Value2

def main():
    Result1 = None
    Result2 = None
    Result3 = None
    Result4 = None

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Result1,Result2,Result3,Result4 = Calculation(No1,No2)

    print("Addition is : ",Result1)
    print("subtraction is : ",Result2)
    print("Multiplication is : ",Result3)
    print("Division is : ",Result4)

if __name__ == "__main__":
    main()