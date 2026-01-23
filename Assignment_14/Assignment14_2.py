# Write a lambda function which accepts one number and returns cube of that number.

Cube = lambda No1: No1 ** 3

def main():
    Value = int(input("Enter a number : "))

    print("Cube is : ",Cube(Value))

if __name__ == "__main__":
    main()