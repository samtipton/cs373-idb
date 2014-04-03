from django.conf.urls import patterns, url
from idb import views, api

urlpatterns = patterns('',
	# API routes
	url(r'^api/v2/superbowls/(\d+)', api.api_superbowls_id),
	url(r'^api/v2/superbowls', api.api_superbowls),
	url(r'^api/v2/franchises/(\d+)', api.api_franchises_id),
	url(r'^api/v2/franchises', api.api_franchises),
	url(r'^api/v2/mvps/(\d+)', api.api_mvps_id),
	url(r'^api/v2/mvps', api.api_mvps),
	
	# Website routes
	url(r'^superbowls/(\d*)', views.superbowls), 
	url(r'^franchises/(\d*)', views.franchises), 
	url(r'^mvps/(\d*)', views.mvps), 
	url(r'^sitemap/', views.sitemap), 
	url(r'^contact/', views.contact),
	url(r'^$', views.splash)
)
