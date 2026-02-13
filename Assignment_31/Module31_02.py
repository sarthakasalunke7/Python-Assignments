import os
import time

def isDirectory(DirName):
    return os.path.isdir(DirName)

def isExtension(Extension):
    return Extension.startswith(".")

def WriteLog(Message ,LogFile= "DirectoryRename.log"):
    try:
        fobj = open(LogFile,"a")
        fobj.write(time.ctime()+" : "+Message+"\n")
        fobj.close()

    except Exception:
        pass

def RenameFile(DirName,Extension1, Extension2):
    Ret = isDirectory(DirName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret1 = isExtension(Extension1)
    Ret2 = isExtension(Extension2)
    if(Ret1 == False or Ret2 == False):
        print("Invalid Extension")
        return

    try:
        WriteLog(f"Renaming files from '{Extension1}' to '{Extension2}' in '{DirName}'")      
        for FolderName, SubFilderName, FileName in os.walk(DirName):
            for fname in FileName:
                if(fname.lower().endswith(Extension1.lower())):

                    oldPath = os.path.join(FolderName, fname)        # It creates the full absolute/relative path of the existing file
                    # oldpath = "Demo/SubFolder/A.txt"

                    name, ext = os.path.splitext(fname)
                    newName = name + Extension2

                    newPath = os.path.join(FolderName, newName)      # create the full path for the new filename.
                    # newpath = "Demo/SubFolder/A.doc"

                    os.rename(oldPath,newPath)      # Go to this file on disk (oldpath) and rename it to (newpath)
                    # Demo/SubFolder/report.doc

                    WriteLog(f"RENAMED : {oldPath}  ->  {newPath}")

    except Exception as eobj:
        print("Error : ",eobj)