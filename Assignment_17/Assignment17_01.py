# Create an module named as Arithmetic which contains 4 functions as Add() for addition,
# Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write an python program which call all the
# functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    print("Addition is : ",Arithmetic.Add(Value1,Value2))
    print("Substraction is : ",Arithmetic.Sub(Value1,Value2))
    print("Multiplication is : ",Arithmetic.Mult(Value1,Value2))
    print("Division is : ",Arithmetic.Div(Value1,Value2))

if __name__ == "__main__":
    main()