# Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def CheckFrequency(Arr, FChk):
    Freq = 0
    
    for i in range(len(Arr)):
        if(Arr[i] == FChk):
            Freq = Freq + 1

    return Freq

def main():
    Value = 0
    data = []

    Size = int(input("Enter number of elements : "))

    print("Enter the elements : ")

    for Value in range(Size):
        Value = int(input())
        data.append(Value)

    Chk = int(input("Enter the element to search : "))

    Ret = CheckFrequency(data, Chk)

    print(Ret)

if __name__ == "__main__":
    main()