from django.db import models

class Managers(models.Model):
   TeamManager = models.CharField(max_length = 20, null =True)
   
   def __str__(self):
      return self.TeamManager
 
class EngineerInfo(models.Model):
   EngineerName = models.CharField(max_length = 30, null =True)
   EngineerManager = models.ForeignKey(Managers,null=True, related_name='ids',on_delete=models.DO_NOTHING) 

   def __unicode__(self):
      return self.EngineerName
   def __str__(self):
      return self.EngineerName
