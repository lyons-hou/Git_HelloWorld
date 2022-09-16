from django.contrib import admin
from BiosUpload.models import BIOS_Package_Ucode 

# Register your models here.
class BiosLatestQueryForUcAdmin(admin.ModelAdmin):
   pass

admin.site.register(BIOS_Package_Ucode,BiosLatestQueryForUcAdmin)
