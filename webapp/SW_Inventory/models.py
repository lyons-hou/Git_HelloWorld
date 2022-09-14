from django.db import models
from blog.settings import MEDIA_URL

# Create your models here.

class SW_InventoryData(models.Model):
   UserName = models.CharField(max_length = 30)
   CollectTime = models.DateTimeField(auto_now_add=True) 
   ReportFile = models.FileField(upload_to = MEDIA_URL) 

   def __unicode(self):
      return self.UserName
   def __str__(self):
      return self.UserName
