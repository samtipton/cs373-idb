from django.conf.urls import patterns, include, url

from django.contrib import admin
from idb_main import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('idb_main.urls')),
    url(r'^games/(\d*)', views.games, name="games"),
    url(r'^teams/(\d*)', views.teams, name="teams"),
    url(r'^players/(\d*)', views.players, name="players"),
    url(r'^sitemap/', views.sitemap, name="sitemap"),
 	url(r'^contact/', views.contact, name="contact")
)
