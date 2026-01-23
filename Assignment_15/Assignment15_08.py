# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

def main():
    Size = 0
    Value = 0
    data = []

    Size = int(input("Enter the number of elements : "))

    print("Enter the elements : ")

    for Value in range(Size):
        Value = int(input())
        data.append(Value)

    FData = list(filter(lambda No : No%3 == 0 and No%5 == 0, data))

    print("Elements after filtering is : ",FData)

if __name__ == "__main__" : 
    main()