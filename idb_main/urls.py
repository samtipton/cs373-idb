from django.conf.urls import patterns, url
from idb_main import views


urlpatterns = patterns('',
	url(r'^$', views.index, name = "index.html"))