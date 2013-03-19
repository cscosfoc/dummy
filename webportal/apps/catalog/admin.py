from django.contrib import admin
from webportal.apps.catalog.models import Catalog

class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']

admin.site.register(Catalog, CatalogAdmin)


