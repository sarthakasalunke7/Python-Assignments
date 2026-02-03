# Search a Word in File
# Problem Statement :
# Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
# Input : Demo.txt Marvellous
# Expected Output : Display whether the word Marvellous is found in Demo.txt or not.

import os

def SearchWord(FileName, StringChk):
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print("There is no such file")
        return

    fobj1 = open(FileName,"r")
    Data = fobj1.read()

    Count = 0

    for str in Data.split():
        if(str == StringChk):
            return True

def main():
    FName = input("Enter file name : ")
    String = input("Enter the word to search : ")

    Ret = SearchWord(FName,String)

    if(Ret == True):
        print(f"The word {String} is in {FName}")
    else:
        print(f"The word {String} is not in {FName}")


if __name__ == "__main__":
    main()