# Write a lambda function which accepts two numbers and returns multiplication.

Multi = lambda No1,No2: No1 * No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    print("Multiplication is : ",Multi(Value1,Value2))

if __name__ == "__main__":
    main()