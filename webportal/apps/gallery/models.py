from django.db import models
from string import join

# Create your models here.

class Album(models.Model):
    name 	= models.CharField(max_length=60)
    hall_id = models.ForeignKey('hall.Hall', blank=True, null=True)

    def __unicode__(self):
        return self.name

class Image(models.Model):
    name 	= models.CharField(max_length=60, blank=True, null=True)
    image 	= models.FileField(upload_to="images/")
    albums 	= models.ManyToManyField(Album, blank=True)

    def albums_(self):
    	lst = [x[1] for x in self.albums.values_list()]
    	return str(join(lst, ', '))

    def __unicode__(self):
        return self.image.name