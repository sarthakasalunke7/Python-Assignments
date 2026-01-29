# Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input : 11      Output : Positive Number
# Input : -8      Output : Negative Number
# Input : 0       Output : Zero

def NumCheck(No):
    if(No > 0):
        return 1
    elif(No < 0):
        return 2
    else:
        return 0

def main():
    Ret = 0

    Value = int(input("Enter a number : "))

    Ret = NumCheck(Value)

    if(Ret == 1):
        print("Positive Number")

    elif(Ret == 2):
        print("Negative Number")

    else:
        print("Zero")
    
if __name__ == "__main__":
    main() 