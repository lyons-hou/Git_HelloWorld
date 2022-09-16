from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from BiosUpload.models import BIOS_Package
# Create your views here.

def BiosLatestQuery(request):
   ProductName_URL = request.GET.get('ProductName')
   PackageType_URL = request.GET.get('PackageType')

   try:
     if PackageType_URL is None:
       bios_data = BIOS_Package.objects.filter(ProductName=ProductName_URL,PackageType="PKG",BiosType="STD").order_by('-Version')[0] 
     else:
       bios_data = BIOS_Package.objects.filter(ProductName=ProductName_URL,PackageType=PackageType_URL,BiosType="STD").order_by('-Version')[0]
   except:
     errormessage = "NULL"
     return HttpResponse(errormessage) 
   BiosVersion = HttpResponse(bios_data.Version)
   return BiosVersion 
