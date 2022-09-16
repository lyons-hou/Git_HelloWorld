from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from SW_Inventory.models import SW_InventoryData 
# Create your views here.

class SWReportUploadForm(forms.Form):
   UserName = forms.CharField()
   ReportFile = forms.FileField()

def SWReportUpload(request):
   if request.method == 'POST':
      form = SWReportUploadForm(request.POST, request.FILES)
      if form.is_valid():
         UserName = form.cleaned_data['UserName']
         ReportFile = form.cleaned_data['ReportFile']

         BiosReport = SW_InventoryData()
         BiosReport.UserName = UserName
         BiosReport.ReportFile = ReportFile 
         BiosReport.save()
         return HttpResponse('System Inventory Report upload !!!')
   else: 
      form = SWReportUploadForm()
   return render_to_response('SWReportUpload.html',{'form': form})
