from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from BiosUpload.models import BIOS_Package
from BiosUpload.models import BIOS_Package_Ucode
from blog.settings import BASE_DIR
import os 
# Create your views here.

def CheckDataBaseForUcodeVersion(sProductName, sBiosVersion):
   Result = "N/A"
   try:
     CollectData = BIOS_Package_Ucode.objects.filter(ProductName=sProductName,Version=sBiosVersion).order_by('-Version')[0]
     Result = CollectData.UcodeVersion
   except:
     Result = "N/A"
   return Result
   
def InsertDataBaseForUcodeVersion(sProductName, sBiosVersion, sUcodeVersion):
   Database = BIOS_Package_Ucode(ProductName=sProductName, Version=sBiosVersion, UcodeVersion=sUcodeVersion)
   Database.save()

def BiosLatestQueryForUc(request):
   ProductName_URL = request.GET.get('ProductName')
   PackageType_URL = request.GET.get('PackageType')

   try:
     if PackageType_URL is None:
       bios_data = BIOS_Package.objects.filter(ProductName=ProductName_URL,PackageType="PKG",BiosType="STD").order_by('-Version')[0] 
     else:
       bios_data = BIOS_Package.objects.filter(ProductName=ProductName_URL,PackageType=PackageType_URL,BiosType="STD").order_by('-Version')[0]

     UCODE_Version = CheckDataBaseForUcodeVersion(ProductName_URL, bios_data.Version)
     if UCODE_Version in ('N/A'):
        #InputfileFolder= "/home/bios-download/webapp/BIOS-Release/blog/upload/Jenkins_Release/"+bios_data.ProductName+"/ADLINK/"+bios_data.Version+"/"
        InputfileFolder = os.path.join( BASE_DIR, "upload", "Jenkins_Release", bios_data.ProductName, "ADLINK", bios_data.Version)
        items = os.listdir(InputfileFolder)
        newlist = []
        for names in items:
            if names.upper().endswith(".ROM"):
                newlist.append(names)
        FilePath=InputfileFolder+"/"+newlist[0]
        AmiToolOutput = os.popen(BASE_DIR + "/BiosLatestQueryForUc/" + "MMToolLnx64 " + FilePath + " /p").readlines()
        Index = len(AmiToolOutput)-4
        UCODE_VersionData = []

        while True:
            Index = Index - 2
            if AmiToolOutput[Index].split("|")[1].strip().upper()== "VOL":
                break;
            UCODE_VersionData.append(AmiToolOutput[Index].split("|")[4].strip()+"("+AmiToolOutput[Index].split("|")[8].strip()+")"+"\n")                
        LastItem = UCODE_VersionData.pop()
        LastItem.replace("\n", "")
        UCODE_VersionData.append(LastItem)
        InsertDataBaseForUcodeVersion(ProductName_URL, bios_data.Version, "".join(UCODE_VersionData))
        return HttpResponse("".join(UCODE_VersionData))

   except:
     errormessage = "NULL"
     return HttpResponse(errormessage) 

   BiosVersion = HttpResponse(UCODE_Version)
   return BiosVersion 
