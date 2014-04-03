from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from idb.models import MVP, Franchise, SuperBowl

# Create your views here.
def splash(request) :
	context = RequestContext(request)
	t = loader.get_template('idb/splash.html')

	game_list = SuperBowl.objects.order_by('-game_day')
	team_list = Franchise.objects.order_by('-year_founded')
	mvp_list = MVP.objects.order_by('-draft_year')

	context = RequestContext(request, {'game_list':game_list, 
		'team_list':team_list, 'mvp_list':mvp_list})

	return HttpResponse(t.render(context))

def superbowls(request, id = None) :

	if id.isdigit():
		url = 'idb/superbowl-template.html'
		game_id = int(id)
		game = SuperBowl.objects.get(id = game_id)
		mvp = MVP.objects.get(id = game.mvp.id)
		context = RequestContext(request, {'game':game, 'mvp':mvp})
	else :
		url = 'idb/superbowls-template.html'
		game_list = SuperBowl.objects.order_by('-game_day')
		context = RequestContext(request, {'game_list':game_list})
	
	t = loader.get_template(url)

	return HttpResponse(t.render(context))

def franchises(request, id = None) :

	if id.isdigit():
		url = 'idb/franchise-template.html'
		team_id = int(id)
		team = Franchise.objects.get(id = team_id)
		context = RequestContext(request, {'team':team})
	else :
		url = 'idb/franchises-template.html'
		team_list = Franchise.objects.order_by('-year_founded')
		context = RequestContext(request, {'team_list':team_list})

	
	t = loader.get_template(url)

	return HttpResponse(t.render(context))

def mvps(request, id = None) :

	if id.isdigit():
		url = 'idb/mvp-template.html'
		mvp_id = int(id)
		mvp = MVP.objects.get(id=mvp_id)
		context = RequestContext(request, {'mvp':mvp})
	else :
		url = 'idb/mvps-template.html'
		mvp_list = MVP.objects.order_by('-draft_year')
		context = RequestContext(request, {'mvp_list':mvp_list})


	t = loader.get_template(url)

	return HttpResponse(t.render(context))

def sitemap(request) :
	context = RequestContext(request)
	t = loader.get_template('idb/sitemap.html')

	return HttpResponse(t.render(context))

def contact(request) :
	context = RequestContext(request)
	t = loader.get_template('idb/template.html')

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