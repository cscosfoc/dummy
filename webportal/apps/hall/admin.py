from django.contrib import admin
from webportal.apps.hall.models import Hall, Hall_image

class ImageInLine(admin.StackedInline):
	model = Hall_image

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    list_display = ('name', 'location')
    inlines = [
    	ImageInLine
    ]

class ImageAdmin(admin.ModelAdmin):
	list_display = ('name', 'Hall')

admin.site.register(Hall, PostAdmin)
admin.site.register(Hall_image, ImageAdmin)