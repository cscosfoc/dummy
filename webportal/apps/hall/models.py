from django.db import models
from string import join
# Create your models here.
class Hall(models.Model):
	name		= models.CharField(max_length=50)
	slug		= models.SlugField(unique=True)
	location 	= models.ForeignKey('catalog.Catalog')
	address		= models.CharField(max_length=100)
	description	= models.TextField(blank=True)

	def __unicode__(self):
		return self.name

class Hall_image(models.Model):
	name		= models.CharField(max_length=50)
	photo		= models.FileField(upload_to="images/", blank=True)
	Hall 		= models.ForeignKey('Hall', null=True, blank=True)

	def __unicode__(self):
		return self.name
