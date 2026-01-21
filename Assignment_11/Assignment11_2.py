# Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def CountDigit(a):
    i = 0
    while(a != 0):
        a = int(a/10)
        i = i+1
        
    return i

def main():
    Ret = 0
    No = int(input("Enter a number : "))

    Ret = CountDigit(No)

    print("Count of digit is : ",Ret)

if __name__ == "__main__":
    main()





