# Design automation script which accept two directory names. Copy all files from first directory into second directory. Second directory should be created at run time.
# Usage : DirectoryCopy.py “Demo” “Temp”
# Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files from Demo to Temp.
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.

import sys
from Module31_03 import DirectoryCopy, WriteLog

def GetInputFromFile(FileName):
    try:
        fobj = open(FileName,"r")
        Data = fobj.read().split()
        if(len(Data) >= 2):
            return Data[0], Data[1]
        
    except Exception as eobj:
        print(f"Error reading input file: {str(eobj)}")

    return None, None

def main():
    try:
        if(len(sys.argv) == 3):
            Dir1 = sys.argv[1]
            Dir2 = sys.argv[2]

        elif(len(sys.argv) == 2):
            Dir1, Dir2 = GetInputFromFile(sys.argv[1])

        else:
            print("Error : Invalid number of arguments")
            return
        
        DirectoryCopy(Dir1,Dir2)
        
    except Exception as eobj:
        print(f"Unexpected Error : {str(eobj)}")

    finally:
        WriteLog("End of application")

if __name__ == "__main__":
    main()