from django.conf.urls import patterns, url
from webportal.apps.portal import views

urlpatterns = patterns('',
	url(r'^$', views.Index)

	)