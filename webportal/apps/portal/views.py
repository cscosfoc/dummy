from django.shortcuts import render
from webportal.apps.portal.models import Location, Building
from random import sample

def Index(request):
	locations = Location.objects.all()
	r_id = sample(xrange(1, 7), 3)
	b_fil = Building.objects.filter(id__in=r_id)
	context = {	'locations': locations,
				'b_fil': b_fil,
	}
	return render(request, 'portal/index.html', context)