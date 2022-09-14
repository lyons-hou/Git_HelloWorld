from django.contrib import admin
from .models import SW_InventoryData 
from django.utils.html import format_html
from blog.settings import MEDIA_URL

# Register your models here.
class SWReportAdmin(admin.ModelAdmin):
   list_display=('id','UserName','CollectTime','URL_FileName',)
   def URL_FileName(self, obj):
      if obj.ReportFile:
          return format_html(u"<a href='../../../SW_InventoryDownload/?UserName=%s&ReportFile=%s' download>Download</a>" % (obj.UserName, obj.ReportFile))
      else:
          return "No attachment"

   list_filter=('UserName',)
   search_fields=('UserName',)
   ordering=('CollectTime',) 

admin.site.register(SW_InventoryData,SWReportAdmin)
