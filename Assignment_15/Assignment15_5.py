# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

Max = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    Size = 0
    Value = 0
    data = []

    Size = int(input("Enter the number of elements : "))

    print("Enter the elements : ")

    for Value in range(Size):
        Value = int(input())
        data.append(Value)

    RData = reduce(Max, data)

    print("Elements after reducing is : ",RData)

if __name__ == "__main__" : 
    main()