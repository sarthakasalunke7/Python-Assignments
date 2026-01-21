# Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def Reverse(a):
    Rev = 0
    while(a != 0):
        Rev = Rev*10        # Rev = (32 * 10) + 1 = 320 + 1
        Rev = Rev + a%10    # Rev = 321
        a = int(a/10)       # a//10
        
    return Rev

def main():
    Ret = 0
    No = int(input("Enter a number : "))

    Ret = Reverse(No)

    print(Ret)

if __name__ == "__main__":
    main()


#    /	    Exact division (float)
#    // 	Whole number division (integer)