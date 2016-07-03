from __future__ import unicode_literals

from django.db import models

class Site(models.Model):
    url = models.CharField(max_length=50)
    def __unicode__(self):
	    return self.url
	    
# # Create your models here.
class Search(models.Model):
    query = models.CharField(blank=False,max_length=100)
    # url =models.CharField(max_length=100)
    # https://docs.djangoproject.com/en/1.9/ref/contrib/postgres/fields/
    # site = models.CharField(blank=False,max_length=100)
    site = models.ForeignKey(Site)
    def __unicode__(self):
	    return self.query

class Result(models.Model):
    url = models.CharField(blank=False,max_length=100)
    site = models.ForeignKey(Search)
    content = models.TextField(blank=True)
    def __unicode__(self):
	    return self.url


    

