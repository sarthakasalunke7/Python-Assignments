# Write a program which accept one number form user and return addition of its factors.
# Input : 12    Output : 16     (1+2+3+4+6)

def FactorSum(No):
    Sum = 0
    for i in range(1,No):
        if(No%i == 0):
            Sum = Sum + i
    
    return Sum

def main():
    Ret = 0
    Value = int(input("Enter a number : "))

    Ret = FactorSum(Value)

    print(Ret)

if __name__ == "__main__":
    main()