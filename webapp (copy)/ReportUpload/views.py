from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from ReportUpload.models import Test_Report
# Create your views here.

class ReportUploadForm(forms.Form):
   ProductName = forms.CharField()
   Version = forms.CharField() 
   ReportFile = forms.FileField()

def ReportUpload(request):
   if request.method == 'POST':
      form = ReportUploadForm(request.POST, request.FILES)
      if form.is_valid():
         ProductName = form.cleaned_data['ProductName']
         Version = form.cleaned_data['Version']
         ReportFile = form.cleaned_data['ReportFile']

         BiosReport = Test_Report()
         BiosReport.ProductName = ProductName
         BiosReport.Version = Version
         BiosReport.ReportFile = ReportFile 
         BiosReport.save()
         return HttpResponse('BIOS Report upload !!!')
   else: 
      form = ReportUploadForm()
   return render_to_response('ReportUpload.html',{'form': form})
