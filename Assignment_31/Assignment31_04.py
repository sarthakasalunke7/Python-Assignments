# Design automation script which accept two directory names and one file extension. Copy all
# files with the specified extension from first directory into second directory. Second directory should be created at run time.
# Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files with extension .exe from Demo to Temp.
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.

import sys
from Module31_04 import DirectoryFileCopy, WriteLog

def GetInputFromFile(FileName):
    try:
        fobj = open(FileName,"r")
        Data = fobj.read().split()
        if(len(Data) >= 3):
            return Data[0], Data[1], Data[2]
        
    except Exception as eobj:
        print(f"Error reading input file: {str(eobj)}")

    return None, None, None

def main():
    try:
        if(len(sys.argv) == 4):
            Dir1 = sys.argv[1]
            Dir2 = sys.argv[2]
            extension = sys.argv[3]

        elif(len(sys.argv) == 2):
            Dir1, Dir2, extension = GetInputFromFile(sys.argv[1])

        else:
            print("Error : Invalid number of arguments")
            return
        
        DirectoryFileCopy(Dir1,Dir2,extension)
        
    except Exception as eobj:
        print(f"Unexpected Error : {str(eobj)}")

    finally:
        WriteLog("End of application")

if __name__ == "__main__":
    main()