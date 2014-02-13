#!coding:utf8
from django.db import models

class Device(models.Model):
    nip = models.CharField(max_length=30)
    wip = models.CharField(max_length=50, null=True, blank=True)
    hostname = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=1, choices=(('y','是'),('n','否')))
    rack = models.CharField(max_length=10)

    def __unicode__(self):
        return self.hostname
