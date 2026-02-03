# Count Words in a File
# Problem Statement : Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input : Demo.txt
# Expected Output : Total number of words in Demo.txt.

import os

def CountWords(FileName):

    Ret = os.path.exists(FileName)
    if(Ret == False):
        print("There is no such file")
        return
    
    fobj = open(FileName,"r")

    Data = fobj.read()

    Count = 0

    for str in Data.split():
        Count = Count + 1

    return Count
def main():
    FName = input("Enter name of the file : ")

    Ret = CountWords(FName)

    print(f"Total number of words in {FName} : ",Ret)

if __name__ == "__main__":
    main()