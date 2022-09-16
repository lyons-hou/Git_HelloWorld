from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from ReportUpload.models import Test_Report
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

def ReportDownload(request):
   ProductName_URL = request.GET.get('ProductName')
   Version_URL = request.GET.get('Version')
   try:
     if Version_URL is None:
       bios_data = Test_Report.objects.filter(ProductName=ProductName_URL).order_by('-Version')[0] 
     else:
       bios_data = Test_Report.objects.filter(ProductName=ProductName_URL,Version=Version_URL)[0]
   except:
     errormessage = "Data Error!!"
     return HttpResponse(errormessage)
   DownloadFile = StreamingHttpResponse(bios_data.ReportFile)
   DownloadFile['Content-Type'] = 'application/octet-stream'
   DownloadFile['Content-Disposition'] = 'attachment;filename="{0}"'.format(bios_data.ReportFile.name[7:])
   return DownloadFile 
