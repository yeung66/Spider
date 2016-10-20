#coding:utf-8
from django.db import models

# Create your models here.
class Duanzi(models.Model):
    content = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.content