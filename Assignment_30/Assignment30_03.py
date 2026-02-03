# Display File Line by Line
# Problem Statement : Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
# Input: Demo.txt
# Expected Output: Display each line of Demo.txt one by one.

import os

def Display(FileName):

    Ret = os.path.exists(FileName)
    if(Ret == False):
        print("There is no such file")
        return
    
    fobj = open(FileName,"r")

    Data = fobj.read()

    print(Data)

def main():
    FName = input("Enter name of the file : ")

    Display(FName)

if __name__ == "__main__":
    main()