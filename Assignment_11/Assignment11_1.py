# Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

def PrimeCheck(No):
    for i in range(2, (int(No/2)+1)):       # need to iterate till half of the value
        if(No % i == 0):
            return True

    return False

def main():
    Ret = False

    value = int(input("Enter a number : "))

    Ret = PrimeCheck(value)

    if (Ret == True):
        print("Not prime")

    else:
        print("Prime")


if __name__ == "__main__":
    main()