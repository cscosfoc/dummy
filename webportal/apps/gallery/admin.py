from django.contrib import admin
from webportal.apps.gallery.models import Album, Image


class ImageAdmin(admin.ModelAdmin):
	list_display = ('name', 'albums_')

admin.site.register(Album)
admin.site.register(Image, ImageAdmin)

