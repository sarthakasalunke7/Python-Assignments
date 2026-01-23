# Write a lambda function which accepts one number and returns True if divisible by 5.

Divisible = lambda No: No%5 == 0

def main():
    Value = int(input("Enter a number : "))

    print(Divisible(Value))

if __name__ == "__main__":
    main()