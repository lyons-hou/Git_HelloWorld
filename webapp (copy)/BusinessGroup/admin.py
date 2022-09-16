from django.contrib import admin
from .models import BusinessGroup_Info 

# Register your models here.
class BusinessGroupAdmin(admin.ModelAdmin):
   list_display=('id','Business_Group',)
   ordering=('id',) 

admin.site.register(BusinessGroup_Info,BusinessGroupAdmin)
