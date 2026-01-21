# Write a program which accepts one number and prints its factors.
# Input: 12
# Output: 1 2 3 4 6 12

def Factors(No):
    data = []

    for i in range(1,No+1):
        if(No%i == 0):
            data.append(i)
    
    return data

def main():
    Ret = []

    Value = int(input("Enter a number : "))

    Ret = Factors(Value)

    print(*Ret)

if __name__ == "__main__":
    main()