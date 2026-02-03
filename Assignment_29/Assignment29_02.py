# Display File Contents
# Problem Statement : Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
# Input : Demo.txt
# Expected Output : Display contents of Demo.txt on console.

import os

def ReadFile(FileName):
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print("There is no such file")
        return

    fobj = open(FileName,"r")

    Data = fobj.read()

    print("Contents of file : ", Data)

def main():
    FName = input("Enter name of the file : ")

    ReadFile(FName)

if __name__ == "__main__":
    main()