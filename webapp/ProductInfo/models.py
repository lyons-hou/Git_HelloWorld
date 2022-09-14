from django.db import models
from BusinessGroup.models import BusinessGroup_Info 

class ProductFamily(models.Model):
   Product_Family = models.CharField(max_length = 20, null =True)
   
   def __str__(self):
      return self.Product_Family
 
class ProductInfo(models.Model):
   ProductName = models.CharField(max_length = 30, null =True)
   Product_Family = models.ForeignKey(ProductFamily,null=True, related_name='ids',on_delete=models.DO_NOTHING) 
   Business_Group = models.ForeignKey(BusinessGroup_Info,null=True, related_name = 'ids',on_delete=models.DO_NOTHING) 

   def __unicode__(self):
      return self.ProductName
   def __str__(self):
      return self.ProductName
