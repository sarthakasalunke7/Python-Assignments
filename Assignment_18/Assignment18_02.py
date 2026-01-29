# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

def Max(Arr):
    MaxValue = Arr[0]

    for i in range(1, len(Arr)):
        if(Arr[i] > MaxValue):
            MaxValue = Arr[i]

    return MaxValue

def main():
    Size = 0
    Value = 0
    data = []

    Size = int(input("Enter number of elements : "))

    print("Enter the elements : ")

    for Value in range(Size):
        Value = int(input())
        data.append(Value)

    Ret = Max(data)

    print("Maximum number from list is : ",Ret)

if __name__ == "__main__":
    main()