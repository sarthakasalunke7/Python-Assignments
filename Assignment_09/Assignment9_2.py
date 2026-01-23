# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number
# Input: 10 20
# Output: 20 is greater

def ChkGreater(No1, No2):
    if(No1 > No2):
        return True
    
def main():

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = False

    Ret = ChkGreater(Value1,Value2)

    if(Ret == True):
        print(Value1,"is greater")

    else:
        print(Value2,"is greater")

if __name__ == "__main__":
    main()


    
