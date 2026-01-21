# Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

def CheckPalindrome(Value):
    Temp = Value
    Rev = 0

    while(Temp != 0):
        Rev = (Rev * 10) + (Temp % 10)
        Temp = Temp // 10   # int(Temp/10)

    if (Rev == Value):
        return True

def main():
    Ret = False

    No = int(input("Enter a number : "))

    Ret = CheckPalindrome(No)

    if (Ret == True):
        print("Palindrome")

    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()


#    /	    Exact division (float)
#    // 	Whole number division (integer)