# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

CheckOdd = lambda No: No%2 == 1     # No%2 != 0

def main():
    Value = int(input("Enter a number : "))

    print(CheckOdd(Value))

if __name__ == "__main__":
    main()