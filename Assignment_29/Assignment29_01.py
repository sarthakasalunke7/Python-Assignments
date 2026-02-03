# Check File Exists in Current Directory
# Problem Statement : Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
# Input : Demo.txt
# Expected Output : Display whether Demo.txt exists or not.

import os

def FileExists(FileName):
    Ret = os.path.exists(FileName)

    if(Ret == True):
        print(f"{FileName} exists in the current directory")
    else:
        print(f"{FileName} do not exists in the current directory")

def main():
    FName = input("Enter name of the file : ")

    FileExists(FName)

if __name__ == "__main__":
    main()