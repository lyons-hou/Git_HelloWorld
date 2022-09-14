from django.db import models
from blog.settings import MEDIA_URL

# Create your models here.

class Test_Report(models.Model):
   ProductName = models.CharField(max_length = 30)
   Version = models.CharField(max_length = 20)
   TestTime = models.DateTimeField(auto_now_add=True) 
   ReportFile = models.FileField(upload_to = MEDIA_URL) 

   def __unicode(self):
      return self.ProductName
   def __str__(self):
      return self.ProductName
