from django.contrib import admin
from .models import ProductInfo 
from .models import ProductFamily

# Register your models here.

class ProductInfoAdmin(admin.ModelAdmin):
   #pass
   list_display=('id', 'Business_Group','Product_Family', 'ProductName',)

class ProductFamilyInfoAdmin(admin.ModelAdmin):
   pass
   #list_display=('Business_Group','Product_Family')


admin.site.register(ProductInfo,ProductInfoAdmin)
admin.site.register(ProductFamily,ProductFamilyInfoAdmin)
