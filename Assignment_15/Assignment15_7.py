# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

CheckStrLength = lambda Str : len(Str) > 5

def main():
    Size = 0
    Value = 0
    data = []

    Size = int(input("Enter the number of elements : "))

    print("Enter the elements : ")

    for Value in range(Size):
        Value = input()
        data.append(Value)

    FData = list(filter(CheckStrLength, data))

    print("Elements after filtering is : ",FData)

if __name__ == "__main__" : 
    main()