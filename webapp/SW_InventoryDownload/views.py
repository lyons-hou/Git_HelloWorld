from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from SW_Inventory.models import SW_InventoryData 
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

def SWReportDownload(request):
   UserName_URL = request.GET.get('UserName')
   ReportFile_URL = request.GET.get('ReportFile')
   try:
     if ReportFile_URL is None:
       bios_data = SW_InventoryData.objects.filter(UserName=UserName_URL).order_by('-CollectTime')[0] 
     else:
       bios_data = SW_InventoryData.objects.filter(UserName=UserName_URL,ReportFile=ReportFile_URL)[0]
   except:
     errormessage = "Data Error!!"
     return HttpResponse(errormessage)
   DownloadFile = StreamingHttpResponse(bios_data.ReportFile)
   DownloadFile['Content-Type'] = 'application/octet-stream'
   DownloadFile['Content-Disposition'] = 'attachment;filename="{0}"'.format(bios_data.ReportFile.name[7:])
   return DownloadFile 
