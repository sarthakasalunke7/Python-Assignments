# Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
# Input : Demo.txt Marvellous
# Expected Output : Count how many times "Marvellous" appears in Demo.txt.

import os
import sys

def StrFreq(FileName, StringChk):
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print("There is no such file")
        return

    fobj1 = open(FileName,"r")
    Data = fobj1.read()

    Count = 0

    for str in Data.split():
        if(str == StringChk):
            Count = Count + 1

    return Count

def main():
    FName = sys.argv[1]
    String = sys.argv[2]

    Ret = StrFreq(FName,String)

    print("Count is : ",Ret)

if __name__ == "__main__":
    main()