from django.db import models

# Create your models here.
class File(models.Model):

    date_add = models.DateTimeField(auto_now_add=True)
    name     = models.CharField(max_length=255)
    link    = models.CharField(max_length=255)
    

    def __unicode__(self):
        return "{0}".format(self.code, )

class User(models.Model):

    username = models.CharField(max_length=255)
    password    = models.CharField(max_length=255)
  

    def __unicode__(self):
        return "{0}".format(self.code, )