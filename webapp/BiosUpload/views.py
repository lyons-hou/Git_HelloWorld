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

UploadListTPDC = ["207GIECF", "207GIEWIBU", "ABX-1401", "ABX-2300", "ABX-5600", "ADi-BSEC", "ADi-SA1X-KB", "ADi-SA1Z-CFZitro", "ADi-SA2X-RZ", "ADi-SA3X-CL", "ADi-SA3X-CL-EAAF", "ADi-SC1X", "ADi-SC1X-AR", "ADi-SC1X-CF", "ADi-SC1X-TL", "ADi-SC2X", "ADi-SC2X-SL-EAAF", "ADi-sCOT2", "ADi-SIOG-LEC1", "ADi-SMXE-211", "ADiSW", "ADLINKVisionSoftwareSDK", "AETO", "AM300", "AmITX-AD-G", "AmITX-AL-I", "AmITX-BE", "AmITX-BT-I", "Amitx-BW", "AmITX-CF-G", "AmITX-CF-G-ADi-Ax", "AmITX-HL", "AmITX-KB-G-ADi-Ax", "AmITX-RZ-G", "AmITX-RZ-G-ADi-Ax", "AMITX-SL-EOS-1300", "AmITX-SL-G", "AmITX-SL-GOMA", "AMP-500", "AmSTX-CF", "ANISE", "APS SDK-MotionSoftware", "aTCA-9710", "AUO - ComQi Media Player", "AVA-3510", "AVA-3510-Gen1", "AVA-5500", "AVA-AP1", "AVA-RAGX", "AVA-RAGX (PoC)", "AVA-XV-V1", "AVBX-6000", "Back-Tray-PC", "Bayer-AL", "C4CST", "C-9288", "CAP-CA03AI", "cExpress-AL", "cExpress-AR", "cExpress-BL", "cExpress-BT2", "cExpress-BW", "cExpress-EL", "cExpress-HL", "cExpress-KL", "cExpress-SL", "cExpress-TL", "cExpress-WL", "Clr-86dx", "CM1-86DX2", "CM1-86DX3", "CM3-mHL", "CMx-BT", "CMx-SL", "COM-HPC-ALT", "COM-HPC-cADP", "COM-HPC-EP", "COM-HPC-Server-Carrier", "COMHPC-sIDH", "common utility", "cPCI-3510", "cPCI-3510BL", "cPCI-3520", "cPCI-3620", "cPCI-3630", "cPCI-6540", "cPCI-6630", "cPCI-6636KL", "cPCI-6636SL", "cPCI-6640", "cPCI-6940", "cPCI-A3515", "cPCI-A3525", "cPCI-A3TP", "cPCI-A3W10", "CSA7210", "CSA-7210", "CSA7600", "CSRD_Edge_DAQ", "DCS-210", "DCS-211", "DCS-RAPL", "DELLOEM", "DELL-OEM", "DEX-100", "DIO2.0", "DLAP-201", "DLAP-211", "DLAP3000", "DLAP-301", "DLAP-401", "DMI-1040", "DMI-1210", "DW-ARM2", "ECAR-B-TKN", "Edge Vision Analytic SREP", "EE-2106AD", "EGW-3100", "EGW3200", "EGW5200", "EMP-200", "EMP-500", "EOS-JNX", "ETX-BT", "EVE-CF", "Express-ADP", "Express-ADP-R3.1", "Express-BD7", "Express-BD74", "Express-BE", "Express-BL", "Express-CF", "Express-CFR", "Express-CVC", "Express-DN7", "Express-HL", "Express-HL2", "Express-HLE", "Express-IBE2", "Express-ID7", "Express-KL", "Express-KL2", "Express-SL", "Express-SL2", "Express-TL", "GE TAI X AIOC", "GEHC-HAWAII", "GE-TAI-X", "GU-V2.0", "Hitachi-EP6200_EP6185", "HPERC-KBL", "HPERC-KBLMH-RAFA", "Hydrogen", "IMB-M43", "IMB-M43H", "IMB-M45", "IMB-M45_M45H", "IMB-M45H", "IMB-M47_M47H", "IMB-T10", "IntelHighWay", "iw.brain(BMW)", "JC-S400", "KOJAK", "LDC", "Lec-AL", "LEC-AL-AI", "LEC-AL-AI-EMMC", "LEC-AL-AI-IPI", "LEC-AL-AI-IPI-SMARC-PLUS", "Lec-AL-IPI-SMARC-PLUS", "LEC-BT", "LEC-BW", "LEC-EL", "LEC-iMX6", "LEC-iMX6R2", "LEC-iMX8", "LEC-iMX8MM", "LEC-iMX8MP", "LEC-KMB", "LEC-Q1000", "LED-TKN", "M45_M45H", "M45_M45H_1v1", "M9024A", "M9025A", "M9035A", "M9037A", "M9038A", "M-910", "M9506A", "MANTA", "MAPS Core", "MCM-100", "MCM-200", "MCM-204", "MCN2610T", "MCT-116", "MECS-6120", "MECS7210", "Merlion-AL", "Minnetronix", "MLC-150", "MLC8", "MNET-4XMO-C", "MOTS-MB", "mPPC-15", "MPU-C3000", "MT-300", "MT-400", "MVP-6100", "MVP-6100-MG2", "MVP-6200", "MXC6400", "MXE110i", "MXE1500", "MXE-210", "MXE-5401", "MXE5500", "MXE5600", "NanoX-AL", "NanoX-EL", "NanoX-EL-TCC", "NDCS18", "NEON-1000-MDX", "NEON-1021C", "NEON-2000-JNO", "NEON-2000-JNX", "NEON-2000-JT2", "NEON-2000-JTN", "NEON-ATS200", "NEON-i2000", "Nuctech", "NuPRO-A40H", "NuPRO-E43", "Orion", "PCI-8134A", "PCIe-10GPoE", "PCIe-8364RS", "PCIe-U312", "PIS-5500", "projectlist.txt", "PX-30", "PXES-2785", "PXES-2788", "PXI-3982", "PXIe-3937", "PXIe-3977", "PXIe-3987", "PXIe-3988", "PXIe-Gie74", "Q7-AL", "Q7-BT", "Q7-BW", "R4600-3A1", "R4600-GEN2", "SA_CPU_BOARD", "SB-MLC-master", "SEMA EC Spec", "Serverlist.txt", "SP-AL", "SP-KL", "SP-TGL", "STC-AL", "Supra", "Tesgine3", "Tianfu1.0", "Titan-AL", "TrainingMaterials", "Triton", "Trixell", "TSPI7_070D", "UE-M15", "VPX3010", "VPX3020", "VPX3-MXM-STD", "VPX3-TL", "VPX6011", "VPX6100", "VPX-TL"]

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
            if ProductName in UploadListTPDC:
                BackupFileToFolderTPDC(ProductName, CustomerName, Version, BiosPackage.FileName.name, FileName.name)
            SendEmailNotification( Email_Owner, Email_ProductName, Email_CustomerName, Email_Version, Email_DownloadLink, Email_Type, Email_History)
            
         return HttpResponse('BIOS package upload !!!')
   else: 
      form = BiosUploadForm()
   return render_to_response('BiosUpload.html',{'form': form})
