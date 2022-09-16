from django.contrib import admin
from .models import EngineerInfo 
from .models import Managers 

# Register your models here.

class EngineerInfoAdmin(admin.ModelAdmin):
   list_display=('EngineerName','EngineerManager',)
   ordering=('EngineerManager',) 

class ManagersInfoAdmin(admin.ModelAdmin):
   pass 


admin.site.register(EngineerInfo,EngineerInfoAdmin)
admin.site.register(Managers,ManagersInfoAdmin)
