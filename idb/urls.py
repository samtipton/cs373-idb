from django.conf.urls import patterns, url
from idb import views, api

urlpatterns = patterns('', 
	url(r'^api/v2/superbowls/(\d+)', api.api_superbowls_id),
	url(r'^api/v2/superbowls', api.api_superbowls),
	url(r'^api/v2/franchises/(\d+)', api.api_franchises_id),
	url(r'^api/v2/franchises', api.api_franchises),
	url(r'^$', views.splash, name="splash"), 
	url(r'^superbowls/(\d*)', views.superbowls, name="superbowls"), 
	url(r'^franchises/(\d*)', views.franchises, name="franchises"), 
	url(r'^mvps/(\d*)', views.mvps, name="mvps"), 
	url(r'^sitemap/', views.sitemap, name="sitemap"), 
	url(r'^contact/', views.contact, name="contact"))