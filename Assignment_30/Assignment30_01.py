# Count Lines in a File
# Problem Statement : Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input : Demo.txt
# Expected Output : Total number of lines in Demo.txt.

import os

def CountLines(FileName):

    Ret = os.path.exists(FileName)
    if(Ret == False):
        print("There is no such file")
        return
    
    fobj = open(FileName,"r")

    Data = fobj.read()

    Count = 0

    for str in Data.split("\n"):
        Count = Count + 1

    return Count
def main():
    FName = input("Enter name of the file : ")

    Ret = CountLines(FName)

    print(f"Total number of lines in {FName} : ",Ret)

if __name__ == "__main__":
    main()