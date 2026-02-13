# Design automation script which accept directory name and file extension from user. Display all files with that extension.
# Usage : DirectoryFileSearch.py “Demo” “.txt”
# Demo is name of directory and .txt is the extension that we want to search.
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.

from Module31_01 import DisplayFiles, WriteLog
import sys

def GetInputFromFile(FileName):
    try:
        fobj =  open(FileName, "r")
        data = fobj.read().split()

        if(len(data) >= 2):
            return data[0], data[1]
        
    except Exception as eobj:
        WriteLog(f"Error reading input file: {str(eobj)}")
    return None, None

def main():
    try:
        if(len(sys.argv) == 3):
            DirectoryName = sys.argv[1]
            Extension = sys.argv[2]

        elif(len(sys.argv) == 2):
            DirectoryName, Extension = GetInputFromFile(sys.argv[1])
            if DirectoryName is None:
                print("Error : Invalid input file format")
                return

        else:
            print("Error : Invalid number of arguments")
            return
        
        DisplayFiles(DirectoryName, Extension)
        
    except Exception as eobj:
        print(f"Unexpected Error : {str(eobj)}")

    finally:
        WriteLog("End of application")

if __name__ == "__main__":
    main()