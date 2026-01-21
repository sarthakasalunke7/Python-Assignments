# Write a program which accepts one number and prints that many numbers starting from 1
# Input: 5
# Output: 1 2 3 4 5

def Display(No):
    data = []

    for i in range(1,No+1):
        data.append(i)

    return data

def main():
    Ret = []

    Value = int(input("Enter a number : "))

    Ret = Display(Value)

    print(*Ret)

if __name__ == "__main__":
    main()