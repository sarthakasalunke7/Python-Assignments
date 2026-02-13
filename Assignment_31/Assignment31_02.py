# Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.
# Usage : DirectoryRename.py “Demo” “.txt” “.doc”
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
# After execution this script each .txt file gets renamed as .doc.
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.

from Module31_02 import RenameFile, WriteLog
import sys

def GetInputFromFile(FileName):
    try:
        with open(FileName, "r") as fobj:
            data = fobj.read().split()

        if len(data) >= 3:
            return data[0], data[1], data[2]

    except Exception as eobj:
        print(f"Error reading input file: {str(eobj)}")

    return None, None, None

def main():
    try:
        if(len(sys.argv) == 4):
            DirectoryName = sys.argv[1]
            Extension1 = sys.argv[2]
            Extension2 = sys.argv[3]

        elif(len(sys.argv) == 2):
            DirectoryName, Extension1, Extension2 = GetInputFromFile(sys.argv[1])
            if DirectoryName is None:
                print("Error : Invalid input file format")
                return

        else:
            print("Error : Invalid number of arguments")
            return

        RenameFile(DirectoryName, Extension1, Extension2)

    except Exception as eobj:
        print(f"Unexpected Error : {str(eobj)}")

    finally:
        WriteLog("End of application")

if __name__ == "__main__":
    main()