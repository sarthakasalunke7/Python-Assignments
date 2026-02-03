# Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of both files.
# • If both files contain the same contents, display Success
# • Otherwise display Failure
# Input (Command Line) : Demo.txt Hello.txt
# Expected Output : Success OR Failure

import sys

def CompareFiles(FileName1,FileName2):

    fobj1 = open(FileName1,"r")
    Data1 = fobj1.read()

    fobj2 = open(FileName2,"r")
    Data2 = fobj2.read()

    if(Data1 == Data2):
        print("Success")
    else:
        print("Failure")

def main():
    FName1 = sys.argv[1]
    FName2 = sys.argv[2]

    CompareFiles(FName1,FName2)

if __name__ == "__main__":
    main()