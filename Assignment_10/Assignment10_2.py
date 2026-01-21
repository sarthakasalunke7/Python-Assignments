# Write a program which accepts one number and prints sum of first N natural numbers.
# Input: 5
# Output: 15

def Sum(Value):
    sum = 0
    
    for i in range(1,Value+1):
        sum = sum + i
        i = i + 1

    return sum

def main():
    print("Enter a number : ")
    No = int(input())
    
    Ret = Sum(No)

    print("Sum is : ",Ret)


if __name__ == "__main__":
    main()