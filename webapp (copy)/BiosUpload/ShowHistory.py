import sys 
import os
import zipfile
import shutil
from glob import glob
from zipfile import ZIP_DEFLATED


# Reture History from File
def ReturnHistoryfromFile(HistoryName):
    f = open(HistoryName, "rb")
    try:
        HistoryData = f.readlines()
        ResultData = "".join('%s' %id.decode().replace("\r\n","<br>") for id in HistoryData) 
    except: 
        ResultData = "History Content: Parsing Error"
    finally:
        f.close()
    return ResultData 
           
#
# Unzip file for history only
#             
def UnzipPackageForHistory(Zip_File, targetFolder, ReleaseHistoryFile):
    zip_ref = zipfile.ZipFile(Zip_File, 'r')
    zip_ref.setpassword(b'adlinkadlink')
    filelist = zip_ref.namelist()
    for eachfile in filelist: 
        if (eachfile.split("/")[-1].upper() == ReleaseHistoryFile):
            zip_ref.extract(eachfile,targetFolder)
    zip_ref.close()  

#
# Return True if request file in zip file
#             
def IsFileExist(Zip_File, ReqFile):
    zip_ref = zipfile.ZipFile(Zip_File, 'r')
    filelist = zip_ref.namelist()
    zip_ref.close() 
    for eachfile in filelist: 
        if (eachfile.split("/")[-1].upper() == ReqFile.upper()):
            return True
    return False
   
#
# Remove Folder
#    
def RemoveFolder(targetFolder):
        shutil.rmtree(targetFolder, ignore_errors=True)

def ShowHistory(FileName):
    import textwrap
    temp_folder = "temp123"
    ReleaseHistoryFile = "HISTORY.TXT"
    CurrentWorkingPath = os.path.abspath(os.path.dirname(__file__))
    ResultData = "N/A"

    temp_folder = FileName.split(".zip")[0] 
    UnzipPackageForHistory( FileName, temp_folder, ReleaseHistoryFile)

    if (not IsFileExist(FileName, ReleaseHistoryFile)):
        print ("===============================================================================")
        print ("           Resule : Skip (Doesn't exist file History.txt) \n")
        return ResultData
        
    ResultData = ReturnHistoryfromFile( temp_folder + "/" + ReleaseHistoryFile)
            
    RemoveFolder( temp_folder)
    return ResultData
    
def main(args = None):
    import textwrap
    temp_folder = "temp123"
    ExitValue = 0
    ReleaseHistoryFile = "HISTORY.TXT"
    USAGE=textwrap.dedent("""\
    
        Description: 
            Check ADLINK History and Binary checksum.
            If compare result is different, it will return errorlevel -3,
            else return 0.
        
        Usage:
            CheckCompileTool BIOSPackage
        """)
    if args is None:
        args = sys.argv[1:]
    else:
        sys.exit(-1)  
    
    if len(args) != 1:
        print(USAGE)
        sys.exit(0)
    temp_folder = args[0].split(".zip")[0]
    UnzipPackageForHistory( args[0], temp_folder, ReleaseHistoryFile)

    if (not IsFileExist(args[0], ReleaseHistoryFile)):
        print ("===============================================================================")
        print ("           Resule : Skip (Doesn't exist file History.txt) \n")
        sys.exit(0)
        
    print(ReturnHistoryfromFile(temp_folder +"/"+  ReleaseHistoryFile))
            
    RemoveFolder( temp_folder)
    sys.exit(ExitValue)
    
if __name__ == '__main__':
    main()
    
    
