from django.conf.urls import patterns, url
from webportal.apps.catalog import views

urlpatterns = patterns('',
	url(r'^$', views.CatalogsAll)

	)