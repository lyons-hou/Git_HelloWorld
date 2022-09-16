from django.contrib import admin
from .models import Test_Report
from django.utils.html import format_html
from blog.settings import MEDIA_URL

# Register your models here.
class TestReportAdmin(admin.ModelAdmin):
   list_display=('id','ProductName','Version','TestTime','URL_FileName',)
   def URL_FileName(self, obj):
      if obj.ReportFile:
          return format_html(u"<a href='../../../ReportDownload/?ProductName=%s&Version=%s' download>Download</a>" % (obj.ProductName, obj.Version))
      else:
          return "No attachment"
   list_filter=('ProductName','Version')
   search_fields=('ProductName',)
   ordering=('TestTime',) 

admin.site.register(Test_Report,TestReportAdmin)
