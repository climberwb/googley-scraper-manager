from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Search(models.Model):
    query = models.CharField(blank=False,max_length=100)
    # https://docs.djangoproject.com/en/1.9/ref/contrib/postgres/fields/
    url = ArrayField(models.CharField( blank=True,max_length=100))
    def __unicode__(self):
	    return self.query


    

