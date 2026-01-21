# Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

def SumDigit(a):
    Sum = 0
    while(a != 0):
        Sum = Sum + (a%10)
        a = int(a/10)
        
    return Sum

def main():
    Ret = 0
    No = int(input("Enter a number : "))

    Ret = SumDigit(No)

    print("Sum of digit is : ",Ret)

if __name__ == "__main__":
    main()





