from django.contrib import admin
from BiosUpload.models import BIOS_Package_Me 

# Register your models here.
class BiosLatestQueryForMeAdmin(admin.ModelAdmin):
   pass

admin.site.register(BIOS_Package_Me,BiosLatestQueryForMeAdmin)
