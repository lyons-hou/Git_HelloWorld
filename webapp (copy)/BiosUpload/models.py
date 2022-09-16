from django.db import models
from blog.settings import MEDIA_URL

class BIOS_Package(models.Model):
   ProductName = models.CharField(max_length = 30)
   Version = models.CharField(max_length = 20)
   BiosType = models.CharField(max_length=5, default = 'STD')
   PackageType = models.CharField(max_length = 10, default = 'PKG') 
   ReleaseTime = models.DateTimeField(auto_now_add=True) 
   FileName = models.FileField(upload_to = MEDIA_URL) 
   FileNameRef = models.CharField(max_length = 100 , blank=True)
   CustomerName = models.CharField(max_length = 30, default = 'ADLINK')
   OwnerName = models.CharField(max_length = 50, blank=True)
   SenderInfo = models.CharField(max_length = 50, blank=True)

   def __unicode(self):
      return self.ProductName

   def __str__(self):
      return self.ProductName

class BIOS_Package_Me(models.Model):
   ProductName = models.CharField(max_length = 30)
   Version = models.CharField(max_length = 20)
   MeVersion = models.CharField(max_length = 50)

   def __unicode(self):
      return self.ProductName

   def __str__(self):
      return self.ProductName

class BIOS_Package_Ucode(models.Model):
   ProductName = models.CharField(max_length = 30)
   Version = models.CharField(max_length = 20)
   UcodeVersion = models.TextField(blank=False)

   def __unicode(self):
      return self.ProductName

   def __str__(self):
      return self.ProductName
