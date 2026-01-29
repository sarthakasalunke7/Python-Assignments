# 5.Write a program which accept one number for user and check whether number is prime or not.
# Input : 5      Output : It is Prime Number

def CheckPrime(No):
    for i in range(2,No):
        if(No%i == 0):
            return False
        else:
            return True

def main():
    Ret = False
    Value = int(input("Enter a number : "))

    Ret = CheckPrime(Value)

    if(Ret == True):
        print("It is Prime Number")

    else:
        print("It is not Prime Number")

if __name__ == "__main__":
    main()