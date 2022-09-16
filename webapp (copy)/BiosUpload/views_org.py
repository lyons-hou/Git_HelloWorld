from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from BiosUpload.models import BIOS_Package
from EngineerInfo.models import Managers,EngineerInfo 
from ProductInfo.models import ProductInfo
import os
from shutil import copyfile
from blog.settings import BASE_DIR

from django.core.mail import send_mail
from django.template import Context, loader
from django.core.mail import EmailMultiAlternatives,get_connection
from BiosUpload.ShowHistory import ShowHistory

# Create your views here.

class BiosUploadForm(forms.Form):
   ProductName = forms.CharField()
   CustomerName = forms.CharField()
   Version = forms.CharField() 
   FileName = forms.FileField()
   OwnerName = forms.CharField()

def CheckProductNameNotExist(Email_ProductName):
    try:
       Data = ProductInfo.objects.get(ProductName=Email_ProductName)
       return False
    except:
       return True 

def SendUnRegEmailNotification(Email_Owner, Email_ProductName):
    context = {
    'Email_Owner': Email_Owner,
    'Email_ProductName': Email_ProductName,
    }

    TITLE = '['+Email_ProductName+'] Project was not registered'
    EMAIL_HOST_USER = 'samuel.lin@adlinktech.com'
    MAIL_LIST = EMAIL_HOST_USER

    email_template_name = 'email_notification.html'
    kk = loader.get_template(email_template_name)

    subject, from_email, to = TITLE, EMAIL_HOST_USER, MAIL_LIST
    html_content = t.render(context)
    conn = get_connection()
    conn.open()
    msg = EmailMultiAlternatives(subject, html_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    conn.send_messages([msg,])
    conn.close()

def SendEmailNotification(Email_Owner, Email_ProductName, Email_CustomerName, Email_Version, Email_DownloadLink, Email_Type, Email_History):
    context = {
    'Email_Owner': Email_Owner,
    'Email_ProductName': Email_ProductName,
    'Email_CustomerName': Email_CustomerName,
    'Email_Version': Email_Version,
    'Email_Type': Email_Type,
    'Email_DownloadLink': Email_DownloadLink,
    'Email_History': Email_History,
    }

    TITLE = '['+Email_ProductName+'] BIOS Formal release package ('+Email_Version+')'

    EMAIL_HOST_USER = 'samuel.lin@adlinktech.com'
 
    try:
       ManagerList = str(EngineerInfo.objects.select_related().get(EngineerName=Email_Owner).EngineerManager)+'@adlinktech.com'  
    except:
       ManagerList = 'samuel.lin@adlinktech.com'

    MAIL_LIST = [Email_Owner+'@adlinktech.com',ManagerList,]

    email_template_name = 'email_template.html'
    t = loader.get_template(email_template_name)

    subject, from_email, to = TITLE, EMAIL_HOST_USER, MAIL_LIST
    html_content = t.render(context)
    conn = get_connection()
    #conn.username = 'adlink.bios'
    #conn.password = 'T@jhe6Kw'
    #conn.host = 'smtp.adlinktech.com'
    conn.open()
    msg = EmailMultiAlternatives(subject, html_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    conn.send_messages([msg,])
    conn.close()

def BackupFileToFolder(ProjectName, CustomerName, BIOSVersion, SrcFileName, FileName):
   SourceFilePath   = os.path.join( BASE_DIR, "upload")
   BackupFolderPath = os.path.join( BASE_DIR, "upload", "Jenkins_Release")
   print(SrcFileName)
   if (not os.path.isdir(os.path.join( BackupFolderPath, ProjectName))):
     os.mkdir(os.path.join( BackupFolderPath, ProjectName))
   if (not os.path.isdir( os.path.join( BackupFolderPath, ProjectName, CustomerName))):
     os.mkdir( os.path.join( BackupFolderPath, ProjectName, CustomerName))
   if (not os.path.isdir( os.path.join( BackupFolderPath, ProjectName, CustomerName, BIOSVersion))):
     os.mkdir( os.path.join( BackupFolderPath, ProjectName, CustomerName, BIOSVersion)) 
   if (not os.path.isfile(os.path.join( BackupFolderPath, ProjectName, CustomerName, BIOSVersion, FileName))):
     copyfile(os.path.join( SourceFilePath, SrcFileName), os.path.join( BackupFolderPath, ProjectName, CustomerName, BIOSVersion, FileName))

def BackupFileToFolderTPDC(ProjectName, CustomerName, BIOSVersion, SrcFileName, FileName):
   SourceFilePath   = os.path.join( BASE_DIR, "upload")
   BackupFolderPath = os.path.join( BASE_DIR, "upload", "Jenkins_Release_TPDC")
   TPDC_FunctionName = "BIOS"
   print(SrcFileName)
   if (not os.path.isdir(os.path.join( BackupFolderPath, ProjectName))):
     os.mkdir(os.path.join( BackupFolderPath, ProjectName))
   if (not os.path.isdir( os.path.join( BackupFolderPath, ProjectName, TPDC_FunctionName))):
     os.mkdir( os.path.join( BackupFolderPath, ProjectName, TPDC_FunctionName))   
   if (not os.path.isdir( os.path.join( BackupFolderPath, ProjectName, TPDC_FunctionName, CustomerName))):
     os.mkdir( os.path.join( BackupFolderPath, ProjectName, TPDC_FunctionName, CustomerName))
   if (not os.path.isdir( os.path.join( BackupFolderPath, ProjectName, TPDC_FunctionName, CustomerName, BIOSVersion))):
     os.mkdir( os.path.join( BackupFolderPath, ProjectName, TPDC_FunctionName, CustomerName, BIOSVersion)) 
   if (not os.path.isfile(os.path.join( BackupFolderPath, ProjectName, TPDC_FunctionName, CustomerName, BIOSVersion, FileName))):
     copyfile(os.path.join( SourceFilePath, SrcFileName), os.path.join( BackupFolderPath, ProjectName, TPDC_FunctionName, CustomerName, BIOSVersion, FileName))

def GetFilePathFromJenkinsFolder(ProjectName, CustomerName, BIOSVersion, FileName):
    BackupFolderPath = os.path.join( BASE_DIR, "upload", "Jenkins_Release")
    return os.path.join( BackupFolderPath, ProjectName, CustomerName, BIOSVersion, FileName)

def CheckBIOSIfExist( QueryProductName, QueryVersion, QueryCustomerName, QueryPackageType, QueryFileNameRef):
   CheckResult = False
   try:
     if QueryPackageType in ('ROM','PKG','PKG_FULL'):
       Data = BIOS_Package.objects.get(ProductName=QueryProductName,Version=QueryVersion,CustomerName=QueryCustomerName,PackageType=QueryPackageType)
     else:
       Data = BIOS_Package.objects.get(ProductName=QueryProductName,Version=QueryVersion,CustomerName=QueryCustomerName,PackageType=QueryPackageType,FileNameRef=QueryFileNameRef)
     CheckResult = True
   except BIOS_Package.DoesNotExist:
     CheckResult = False 
   return CheckResult

#
# Get sender information from META
#   (1) Via proxy: HTTP_X_FORWARDED_FOR
#   (2) Directly: REMOTE_ADDR
#
def get_client_ip(request):
   x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
   if x_forwarded_for:
      ip = x_forwarded_for.split(',')[0]
   else:
      ip = request.META.get('REMOTE_ADDR')
   return ip

def BiosUpload(request):
   if request.method == 'POST':
      form = BiosUploadForm(request.POST, request.FILES)
      if form.is_valid():
         ProductName = form.cleaned_data['ProductName']
         Version = form.cleaned_data['Version']
         FileName = form.cleaned_data['FileName']
         CustomerName = form.cleaned_data['CustomerName']
         OwnerName = form.cleaned_data['OwnerName']
         TmpFileNameRef = FileName.name.split(".")[0]
         
         if Version in ("VVVVVV"):
            TempVersion = FileName.name.split("_")[1].upper()
            if len(TempVersion) == 5:
               Version = TempVersion[:1]+"."+TempVersion[1:3]+"."+TempVersion[3:5]

         PackageType = FileName.name.split(".")[-1].upper()
         if PackageType in ("ZIP","7Z"):
            if FileName.name.upper().find("FULLIMAGE")>-1:
               PackageType = "PKG_FULL"
            elif FileName.name.upper().find("IMAGE")>-1:
               PackageType = "PKG"
            elif FileName.name.upper().find("CLOSEMNF")>-1:
               PackageType = "MFG"
            elif FileName.name.upper().find("FWCHECK")>-1:
               PackageType = "MFG"
            else:
               PackageType = "OTHER"

         if CheckBIOSIfExist(ProductName, Version, CustomerName, PackageType, TmpFileNameRef):
            return HttpResponse('BIOS Package is duplicated!!!')

         BiosPackage = BIOS_Package()
         BiosPackage.ProductName = ProductName
         BiosPackage.Version = Version
         print(request.FILES['FileName'].name)

         if Version.count(".")==2:
            BiosPackage.BiosType = "STD"
         else:
            BiosPackage.BiosType = "CST"

         BiosPackage.CustomerName = CustomerName 
         BiosPackage.PackageType = PackageType
         BiosPackage.FileName = FileName
         BiosPackage.Version = Version
         if PackageType in ("BIN"):
            BiosPackage.FileNameRef = FileName.name.split(".")[0]
         if PackageType in ("MFG","OTHER"):
            BiosPackage.FileNameRef = ProductName+"_"+Version+"_"+FileName.name.split(".")[0]
            request.FILES['FileName'].name = ProductName+"_"+Version+"_"+FileName.name
         BiosPackage.OwnerName = OwnerName

         BiosPackage.SenderInfo = get_client_ip(request)

         BiosPackage.save()
         BackupFileToFolder(ProductName, CustomerName, Version, BiosPackage.FileName.name, FileName.name)
         
         #if CheckProductNameNotExist(ProductName):
         #   SendUnRegEmailNotification(OwnerName.split("@")[0], ProductName);
            
         if PackageType in ("PKG","PKG_FULL"):
            Email_Owner = OwnerName.split("@")[0]
            Email_ProductName = ProductName
            Email_CustomerName = CustomerName
            Email_Version = Version
            Email_DownloadLink = request.get_host()+'/BiosDownload/?ProductName='+Email_ProductName+'&Version='+Email_Version+'&PackageType='+PackageType
            Email_Type = PackageType
            Email_History = ShowHistory(GetFilePathFromJenkinsFolder( ProductName, CustomerName, Version, FileName.name))
            BackupFileToFolderTPDC(ProductName, CustomerName, Version, BiosPackage.FileName.name, FileName.name)
            SendEmailNotification( Email_Owner, Email_ProductName, Email_CustomerName, Email_Version, Email_DownloadLink, Email_Type, Email_History)
            
         return HttpResponse('BIOS package upload !!!')
   else: 
      form = BiosUploadForm()
   return render_to_response('BiosUpload_2.html',{'form': form})
