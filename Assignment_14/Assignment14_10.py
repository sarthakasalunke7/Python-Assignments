# Write a lambda function which accepts three numbers and returns largest number.

Max = lambda No1,No2,No3: No1 if(No1 > No2 and No1 > No3) else (No2 if(No2 > No1 and No2 > No3)   else No3)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    Value3 = int(input("Enter third number : "))


    print("Largest number is : ",Max(Value1,Value2,Value3))

if __name__ == "__main__":
    main()


# In Python, lambda functions do not support the elif keyword directly. Instead, you must nest if-else statements to achieve the same multi-condition logic
# lambda arguments: value1 if condition1 else (value2 if condition2 else default_value)
# Cannot use colon in lambda functtion for if-else statements