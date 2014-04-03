from django.conf.urls import patterns, url
from idb import views

urlpatterns = patterns('', 
	url(r'^$', views.splash, name="splash"), 
	url(r'^superbowls/(\d*)', views.superbowls, name="superbowls"), 
	url(r'^franchises/(\d*)', views.franchises, name="franchises"), 
	url(r'^mvps/(\d*)', views.mvps, name="mvps"), 
	url(r'^sitemap/', views.sitemap, name="sitemap"), 
	url(r'^contact/', views.contact, name="contact"))