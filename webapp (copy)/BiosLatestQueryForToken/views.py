from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from BiosUpload.models import BIOS_Package
from blog.settings import BASE_DIR
import os 
# Create your views here.

def BiosLatestQueryForToken(request):
   ProductName_URL  = request.GET.get('ProductName')
   PackageType_URL  = request.GET.get('PackageType')
   TokenName_URL    = request.GET.get('Token')

   try:
     if PackageType_URL is None:
       bios_data = BIOS_Package.objects.filter(ProductName=ProductName_URL,PackageType="PKG",BiosType="STD").order_by('-Version')[0] 
     else:
       bios_data = BIOS_Package.objects.filter(ProductName=ProductName_URL,PackageType=PackageType_URL,BiosType="STD").order_by('-Version')[0]

     #InputfileFolder= "/home/bios-download/webapp/BIOS-Release/blog/upload/Jenkins_Release/"+bios_data.ProductName+"/ADLINK/"+bios_data.Version+"/"
     InputfileFolder = os.path.join( BASE_DIR, "upload", "Jenkins_Release", bios_data.ProductName, "ADLINK", bios_data.Version)
     FilePath1=InputfileFolder+"/"+"token.mak"
     FilePath2=InputfileFolder+"/"+"token.h"
     if (os.path.isfile(FilePath1) and os.path.isfile(FilePath2)):
        TokenData = os.popen("python "+BASE_DIR+"/BiosLatestQueryForToken/CheckBiosToken.py " + FilePath1 + " " + FilePath2 + " " + TokenName_URL).readlines() 
     else:
        TokenData = "NULL"

   except:
     errormessage = "NULL"
     return HttpResponse(errormessage) 

   TokenValue = HttpResponse(TokenData)
   return TokenValue 
