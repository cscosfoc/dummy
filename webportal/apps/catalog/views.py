# Create your views here.

from django.shortcuts import render
from webportal.apps.catalog.models import Catalog
from webportal.apps.hall.models import Hall

def CatalogsAll(request):
	catalogs = Catalog.objects.all()
	halls = Hall.objects.all()
	h1 = halls[0]
	h2 = halls[1]
	ima1 = h1.hall_image_set.get(id=1).photo.url
	ima2 = h2.hall_image_set.get(id=2).photo.url
	context = {'catalogs': catalogs,
			'h1': h1,
			'h2': h2,
			'ima1': ima1,
			'ima2': ima2,
			}
	return render(request, 'catalog/catalog.html', context)