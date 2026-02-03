# Copy File Contents into a New File (Command Line)
# Problem Statement:
#   Write a program which accepts an existing file name through command line arguments, creates a new file
#   named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input (Command Line) : ABC.txt
# Expected Output : Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import os
import sys

def CopyFile(FileName):
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print("There is no such file")
        return

    fobj1 = open(FileName,"r")
    Data = fobj1.read()

    fobj2 = open("Demo.txt","w")

    fobj2.write(Data)

def main():
    FName = sys.argv[1]

    CopyFile(FName)

if __name__ == "__main__":
    main()