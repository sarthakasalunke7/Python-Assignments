# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

Square = lambda No: No*No

def main():
    Size = 0
    Value = 0
    data = []

    Size = int(input("Enter the number of elements : "))

    print("Enter the elements : ")

    for Value in range(Size):
        Value = int(input())
        data.append(Value)

    MData = list(map(Square , data))

    print("Elements after mapping : ",MData)

if __name__ == "__main__":
    main()