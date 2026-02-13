import os
import time

def isDirectory(DirName):
    return os.path.isdir(DirName)

def isExtension(Extension):
    return Extension.startswith(".")

def WriteLog(Message ,LogFile= "DirectoryFileSearch.log"):
    try:
        fobj = open(LogFile,"a")
        fobj.write(time.ctime()+" : "+Message+"\n")
        fobj.close()

    except Exception as eobj:
        print("Error : ",eobj)

def DisplayFiles(DirName,Extension):
    Ret = isDirectory(DirName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = isExtension(Extension)
    if(Ret == False):
        print("Invalid Extension")
        return

    try:
        WriteLog(f"Files in directory '{DirName}' with extension '{Extension}' : ")       
        for FolderName, SubFilderName, FileName in os.walk(DirName):
            for fname in FileName:
                if(fname.endswith(Extension)):
                    WriteLog(os.path.join(FolderName, fname) + "\n")

    except PermissionError:
        WriteLog("Error : Permission denied while accessing directory")
    
    except Exception as eobj:
        print("Error : ",eobj)