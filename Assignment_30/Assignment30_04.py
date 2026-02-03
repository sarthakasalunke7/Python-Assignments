# Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
# • First file is an existing file
# • Second file is a new file
# Copy all contents from the first file into the second file.
# Input : ABC.txt Demo.txt
# Expected Output : Contents of ABC.txt copied into Demo.txt.

import os

def CopyFile(FileName1,FileName2):
    Ret = os.path.exists(FileName1)
    if(Ret == False):
        print("There is no such file")
        return

    fobj1 = open(FileName1,"r")
    Data = fobj1.read()

    fobj2 = open(FileName2,"w")

    fobj2.write(Data)

def main():
    FName1 = input("File1 name : ")
    FName2 = input("File2 name : ")

    CopyFile(FName1,FName2)

if __name__ == "__main__":
    main()