from django.conf.urls import patterns, url
from idb import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name="index"), 
	url(r'^games/(\d*)', views.games, name="games"), 
	url(r'^teams/(\d*)', views.teams, name="teams"), 
	url(r'^players/(\d*)', views.players, name="players"), 
	url(r'^sitemap/', views.sitemap, name="sitemap"), 
	url(r'^contact/', views.contact, name="contact"))