# Write a program which accepts one number and checks whether it is divisible by 3 and 5
# Input: 15
# Output: Divisible by 3 and 5

def Divisible(Value):
    if ((Value%3 == 0) and (Value%5 == 0)):
        return True

def main():
    No = int(input("Enter a number : "))

    Ret = Divisible(No)

    if (Ret == True):
        print(No,"is Divisible by 3 and 5")

    else:
        print(No,"is not Divisible by 3 and 5")

if __name__ == "__main__":
    main()