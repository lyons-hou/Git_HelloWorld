from django.contrib import admin
from .models import BIOS_Package
from ProductInfo.models import ProductInfo
from ReportUpload.models import Test_Report
from django.utils.html import format_html
from blog.settings import MEDIA_URL,BASE_DIR
import os
import shutil

# Remove files when delete records
def delete_files(modeladmin, request, queryset):
  ServerFileBase = os.path.join( BASE_DIR, 'upload/')
  BackupFolderBase = os.path.join( BASE_DIR, 'upload/', 'Jenkins_Release/')
  BackupTPDCFolderBase = os.path.join( BASE_DIR, 'upload/', 'Jenkins_Release_TPDC/')
  try:
    for obj in queryset:
      ServerFileName = os.path.join(ServerFileBase,obj.FileName.name)
      BackupServerFileName = os.path.join(BackupFolderBase,obj.ProductName,obj.CustomerName,obj.Version,obj.FileName.name.split('/')[-1])
      BackupTPDCServerFileName = os.path.join(BackupTPDCFolderBase,obj.ProductName,"BIOS",obj.CustomerName,obj.Version,obj.FileName.name.split('/')[-1])
      print(BackupServerFileName)
      if (os.path.isfile(BackupServerFileName)):         
        os.remove(BackupServerFileName)
        if not os.listdir(os.path.join(BackupFolderBase,obj.ProductName,obj.CustomerName,obj.Version)):
           os.rmdir(os.path.join(BackupFolderBase,obj.ProductName,obj.CustomerName,obj.Version))
        if not os.listdir(os.path.join(BackupFolderBase,obj.ProductName,obj.CustomerName)):
           os.rmdir(os.path.join(BackupFolderBase,obj.ProductName,obj.CustomerName)) 
        if not os.listdir(os.path.join(BackupFolderBase,obj.ProductName)):
           os.rmdir(os.path.join(BackupFolderBase,obj.ProductName))
      if (os.path.isfile(BackupTPDCServerFileName)):         
        os.remove(BackupTPDCServerFileName)
        if not os.listdir(os.path.join(BackupTPDCFolderBase,obj.ProductName,"BIOS",obj.CustomerName,obj.Version)):
           os.rmdir(os.path.join(BackupTPDCFolderBase,obj.ProductName,"BIOS",obj.CustomerName,obj.Version))
        if not os.listdir(os.path.join(BackupTPDCFolderBase,obj.ProductName,"BIOS",obj.CustomerName)):
           os.rmdir(os.path.join(BackupTPDCFolderBase,obj.ProductName,"BIOS",obj.CustomerName))
        if not os.listdir(os.path.join(BackupTPDCFolderBase,obj.ProductName,"BIOS")):
           os.rmdir(os.path.join(BackupTPDCFolderBase,obj.ProductName,"BIOS"))
        if not os.listdir(os.path.join(BackupTPDCFolderBase,obj.ProductName)):
           os.rmdir(os.path.join(BackupTPDCFolderBase,obj.ProductName))
      if (os.path.isfile(ServerFileName)):
        os.remove(ServerFileName)
      obj.delete()
  except:
    print("error!!") 

delete_files.short_description = "Delete records and files which were selected"

# Register your models here.
class BiosPackageAdmin(admin.ModelAdmin):
   list_display=('id','BU', 'Family', 'ProductName','Owner','CustomerName','Version','PackageType','ReleaseTime','URL_FileName','QA')

   def Owner(self,obj):
      try:
          Data = obj.OwnerName.split("@")[0] 
      except:
          Data = ""
      return Data

   def BU(self, obj):
      try:
          Data = ProductInfo.objects.filter(ProductName=obj.ProductName)[0].Business_Group
      except:
          Data = ""
      return Data
   def Family(self, obj):
      try:
          Data = ProductInfo.objects.filter(ProductName=obj.ProductName)[0].Product_Family
      except:
          Data = ""
      return Data

   def URL_FileName(self, obj):
      if obj.FileName:
          if (obj.PackageType in ("BIN","MFG")) and (obj.FileNameRef !=""):
            return format_html(u"<a href='../../../BiosDownload/?ProductName=%s&Version=%s&PackageType=%s&FileNameRef=%s' download>Download</a>" % (obj.ProductName, obj.Version,obj.PackageType,obj.FileNameRef))
          else:
            return format_html(u"<a href='../../../BiosDownload/?ProductName=%s&Version=%s&PackageType=%s' download>Download</a>" % (obj.ProductName, obj.Version,obj.PackageType))
      else:
          return "No attachment"

   def QA(self, obj):
      try:
         Data = Test_Report.objects.filter(ProductName=obj.ProductName,Version=obj.Version)[0].ReportFile
      except:
         Data = ""

      if Data:
         return format_html(u"<a href='../../../ReportDownload/?ProductName=%s&Version=%s' download>Done</a>" % (obj.ProductName, obj.Version))
      else:
         return ""

   list_filter=('CustomerName','ProductName',)
   search_fields=('ProductName',)
   ordering=('ReleaseTime',) 
   actions=[delete_files]


admin.site.register(BIOS_Package,BiosPackageAdmin)
admin.site.disable_action('delete_selected')
