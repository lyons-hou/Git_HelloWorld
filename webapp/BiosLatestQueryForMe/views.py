from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from BiosUpload.models import BIOS_Package
from BiosUpload.models import BIOS_Package_Me
from blog.settings import BASE_DIR
import os 
# Create your views here.

def CheckDataBaseForMeVersion(sProductName, sBiosVersion):
   Result = "NULL"
   try:
     CollectData = BIOS_Package_Me.objects.filter(ProductName=sProductName,Version=sBiosVersion).order_by('-Version')[0]
     Result = CollectData.MeVersion
   except:
     Result = "N/A"
   return Result
   
def InsertDataBaseForMeVersion(sProductName, sBiosVersion, sMeVersion):
   Database = BIOS_Package_Me(ProductName=sProductName, Version=sBiosVersion, MeVersion=sMeVersion)
   Database.save()

def BiosLatestQueryForMe(request):
   ProductName_URL = request.GET.get('ProductName')
   PackageType_URL = request.GET.get('PackageType')

   try:
     if PackageType_URL is None:
       bios_data = BIOS_Package.objects.filter(ProductName=ProductName_URL,PackageType="PKG",BiosType="STD").order_by('-Version')[0] 
     else:
       bios_data = BIOS_Package.objects.filter(ProductName=ProductName_URL,PackageType=PackageType_URL,BiosType="STD").order_by('-Version')[0]

     ME_TXE_VersionData = CheckDataBaseForMeVersion(ProductName_URL, bios_data.Version)
     if ME_TXE_VersionData in ('N/A'):
       #InputfileFolder= "/home/bios-download/webapp/BIOS-Release/blog/upload/Jenkins_Release/"+bios_data.ProductName+"/ADLINK/"+bios_data.Version+"/"
       InputfileFolder = os.path.join( BASE_DIR, "upload", "Jenkins_Release", bios_data.ProductName, "ADLINK", bios_data.Version)
       items = os.listdir(InputfileFolder)
       newlist = []
       for names in items:
            if names.upper().endswith(".BIN"):
                newlist.append(names)
       FilePath=InputfileFolder+"/"+newlist[0]
       ME_TXE_VersionData = os.popen("python "+BASE_DIR+"/BiosLatestQueryForMe/ReadBinaryMe.py " + FilePath).readline() 
       InsertDataBaseForMeVersion(ProductName_URL, bios_data.Version, ME_TXE_VersionData)

   except:
     errormessage = "NULL"
     return HttpResponse(errormessage) 

   BiosVersion = HttpResponse(ME_TXE_VersionData)
   return BiosVersion 
