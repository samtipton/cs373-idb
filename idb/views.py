from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from idb.models import MVP, Franchise, SuperBowl

# Create your views here.
def index(request) :
	context = RequestContext(request)
	t = loader.get_template('idb/splash.html')

	return HttpResponse(t.render(context))

def games(request, id = None) :

	if id.isdigit():
		url = 'idb/superbowl.html'
	else :
		url = 'idb/superbowls.html'

	if id.isdigit():
		game_id = id
	else :
		game_list = SuperBowl.objects.order_by('game_number')

	context = RequestContext(request)
	t = loader.get_template(url)

	return HttpResponse(t.render(context))

def teams(request, id = None) :

	if id.isdigit():
		url = 'idb/franchise.html'
	else :
		url = 'idb/franchises.html'

	context = RequestContext(request)
	t = loader.get_template(url)

	return HttpResponse(t.render(context))

def players(request, id = None) :

	if id.isdigit():
		url = 'idb/player' + str(id) + '.html'
	else :
		url = 'idb/players.html'

	context = RequestContext(request)
	t = loader.get_template(url)

	return HttpResponse(t.render(context))

def sitemap(request) :
	context = RequestContext(request)
	t = loader.get_template('idb/sitemap.html')

	return HttpResponse(t.render(context))

def contact(request) :
	context = RequestContext(request)
	t = loader.get_template('idb/contact.html')

	return HttpResponse(t.render(context))
	
# Example of a view to inflate with a Django template in an .html file
# Possible implementation from tutorial example shown in index.html comment

# from idb_main.models import Game
# 
# class IndexView(generic.ListView):
#     template_name = 'index.html'
#     context_object_name = 'latest_game_list'
# 
#     def get_queryset(self):
# 	"""Return the last five published games."""
# 
# 	return Game.objects.order_by('-game_day')[:3]