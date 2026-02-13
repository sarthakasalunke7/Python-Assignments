import os
import shutil
import time

def isExists(DirName):
    return os.path.exists(DirName)

def isDir(DirName):
    return os.path.isdir(DirName)

def WriteLog(Message ,LogFile= "DirectoryCopy.log"):
    try:
        fobj = open(LogFile,"a")
        fobj.write(time.ctime()+" : "+Message+"\n")
        fobj.close()

    except Exception:
        pass

def DirectoryCopy(Source, Destination):
    try:
        Ret = isExists(Source)
        if(Ret == False):
            WriteLog("No such directory exists")
            return
        
        Ret = isDir(Source)
        if(Ret == False):
            WriteLog("There is no such directory")
            return
        
        WriteLog(f"Copying files from '{Source}' to '{Destination}'")

        os.makedirs(Destination, exist_ok=True)

        for FolderName, SubFolderName, FileNames in os.walk(Source):

            relative_folder = os.path.relpath(FolderName, Source)
            dest_folder = os.path.join(Destination, relative_folder)

            os.makedirs(dest_folder, exist_ok=True)

            for file in FileNames:
                src_path = os.path.join(FolderName, file)
                dest_path = os.path.join(dest_folder, file)

                shutil.copy2(src_path, dest_path)

                WriteLog(f"COPIED : {src_path} -> {dest_path}")

        WriteLog("Directory copied successfully")

    except Exception as eobj:
        WriteLog(f"Error : {str(eobj)}")