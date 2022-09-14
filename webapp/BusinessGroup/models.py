from django.db import models

class BusinessGroup_Info (models.Model):
   Business_Group = models.CharField(max_length = 20)

   def __unicode__(self):
      return self.Business_Group
   def __str__(self):
      return self.Business_Group
