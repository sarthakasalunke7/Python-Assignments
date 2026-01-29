# Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

def Min(Arr):
    MinValue = Arr[0]

    for i in range(1, len(Arr)):
        if(Arr[i] < MinValue):
            MinValue = Arr[i]

    return MinValue

def main():
    Size = 0
    Value = 0
    data = []

    Size = int(input("Enter number of elements : "))

    print("Enter the elements : ")

    for Value in range(Size):
        Value = int(input())
        data.append(Value)

    Ret = Min(data)

    print("Minimum number from list is : ",Ret)

if __name__ == "__main__":
    main()