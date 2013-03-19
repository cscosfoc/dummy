from django.db import models

# Create your models here.
class Catalog(models.Model):
	name	= models.CharField(max_length=50)
	slug	= models.SlugField(max_length=50, unique=True)
	parent	= models.ForeignKey('self', null=True, blank=True, related_name='children')

	def __unicode__(self):
		return self.name
