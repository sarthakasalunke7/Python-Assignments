# Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input : 4 Output : 16
# Input : 6 Output : 36

Power = lambda No : No**2

def main():
    Value = int(input("Enter a number : "))

    print(Power(Value))

if __name__ == "__main__":
    main()