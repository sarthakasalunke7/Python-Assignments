# Write a program which accepts one number and prints all even numbers till that number.
# Input: 10
# Output: 2 4 6 8 10

def DisplayEven(Value):
    data = []

    for i in range(1,Value+1):
        if(i % 2 == 0):
            data.append(i)
        i = i + 1

    return data

def main():
    Ret = []    # list()
    print("Enter a number : ")
    No = int(input())
    
    Ret = DisplayEven(No)

    print(*Ret)     # * unpacking operator


if __name__ == "__main__":
    main()