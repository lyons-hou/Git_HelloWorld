from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from BiosUpload.models import BIOS_Package
from blog.settings import MEDIA_URL
# Create your views here.
def file_iterator(file_name, chunk_size=512):
   with open(file_name, "rb") as f:
     while True:
       c = f.read(chunk_size)
       if c:
         yield c
       else:
         break

def BiosDownload(request):
   ProductName_URL = request.GET.get('ProductName')
   Version_URL = request.GET.get('Version')
   PackageType_URL = request.GET.get('PackageType')
   FileNameRef_URL = request.GET.get('FileNameRef')

   try:
     if Version_URL is None:
       bios_data = BIOS_Package.objects.filter(ProductName=ProductName_URL,PackageType="PKG").order_by('-Version')[0] 
     else:
       if FileNameRef_URL is None:
         bios_data = BIOS_Package.objects.filter(ProductName=ProductName_URL,Version=Version_URL,PackageType=PackageType_URL)[0]
       else:
         bios_data = BIOS_Package.objects.filter(ProductName=ProductName_URL,Version=Version_URL,PackageType=PackageType_URL,FileNameRef=FileNameRef_URL)[0]
   except:
     errormessage = "Data Error!!"
     return HttpResponse(errormessage)
   DownloadFile = StreamingHttpResponse(bios_data.FileName)
   DownloadFile['Content-Type'] = 'application/octet-stream'
   if FileNameRef_URL is None:
     DownloadFile['Content-Disposition'] = 'attachment;filename="{0}"'.format(bios_data.ProductName+"_"+bios_data.Version.replace(".","")+"."+bios_data.FileName.name.split(".")[-1])
   else:
     DownloadFile['Content-Disposition'] = 'attachment;filename="{0}"'.format(bios_data.FileNameRef+"."+bios_data.FileName.name.split(".")[-1])
   return DownloadFile 
