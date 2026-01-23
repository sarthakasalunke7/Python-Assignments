# Write a lambda function which accepts one number and returns True if number is even otherwise False.

CheckEven = lambda No: No%2 == 0

def main():
    Value = int(input("Enter a number : "))

    print(CheckEven(Value))

if __name__ == "__main__":
    main()