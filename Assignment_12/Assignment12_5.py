# Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 5 4 3 2 1

def RevDisplay(No):
    data = []

    for i in range(No,0,-1):
        data.append(i)

    return data

def main():
    Ret = []

    Value = int(input("Enter a number : "))

    Ret = RevDisplay(Value)

    print(*Ret)

if __name__ == "__main__":
    main()