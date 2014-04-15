from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from django.db.models import Q
from idb.models import MVP, Franchise, SuperBowl
from django.views.generic.list import BaseListView #search 

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
		if int(id) <= len(SuperBowl.objects.all()) :
			url = 'idb/superbowl-template.html'
			game_id = int(id)
			game = SuperBowl.objects.get(id = game_id)
			mvp = MVP.objects.get(id = game.mvp.id)
			context = RequestContext(request, {'game':game, 'mvp':mvp})
		else :
			url = 'idb/404.html'
			context = RequestContext(request)

	else :
		url = 'idb/superbowls-template.html'
		game_list = SuperBowl.objects.order_by('-game_day')
		context = RequestContext(request, {'game_list':game_list})
	
	t = loader.get_template(url)

	return HttpResponse(t.render(context))

def franchises(request, id = None) :

	if id.isdigit():
		if int(id) <= len(Franchise.objects.all()) :
			url = 'idb/franchise-template.html'
			team_id = int(id)
			team = Franchise.objects.get(id = team_id)
			game_history = SuperBowl.objects.filter(Q(winning_franchise=team) | Q(losing_franchise=team)).all()
			mvp_history = team.mvps.all()
			context = RequestContext(request, {'team':team, 'game_history':game_history
				,'mvp_history':mvp_history})
		else :
			url = 'idb/404.html'
			context = RequestContext(request)
	else :
		url = 'idb/franchises-template.html'
		team_list = Franchise.objects.order_by('-year_founded')
		context = RequestContext(request, {'team_list':team_list})

	
	t = loader.get_template(url)

	return HttpResponse(t.render(context))

def mvps(request, id = None) :

	if id.isdigit():
		if int(id) <= len(MVP.objects.all()) :
			url = 'idb/mvp-template.html'
			mvp_id = int(id)
			mvp = MVP.objects.get(id=mvp_id)
			game_history = SuperBowl.objects.filter(mvp=mvp).all()
			teams = Franchise.objects.filter(mvps__in=[mvp]).all()
			context = RequestContext(request, {'mvp':mvp, 'game_history':game_history, 'teams':teams})
		else :
			url = 'idb/404.html'
			context = RequestContext(request)

	else :
		url = 'idb/mvps-template.html'
		mvp_list = MVP.objects.order_by('-draft_year')
		context = RequestContext(request, {'mvp_list':mvp_list})


	t = loader.get_template(url)

	return HttpResponse(t.render(context))

def contact(request) :
	context = RequestContext(request)
	t = loader.get_template('idb/contact.html')

	return HttpResponse(t.render(context))





class SearchMixin(object):
    
    """Base mixin for search views."""
    
    context_object_name = "search_results"
    
    query_param = "q"
    
    def get_query_param(self):
        """Returns the query parameter to use in the request GET dictionary."""
        return self.query_param
    
    models = ()
    
    def get_models(self):
        """Returns the models to use in the query."""
        return self.models 
    
    exclude = ()
    
    def get_exclude(self):
        """Returns the models to exclude from the query."""
        return self.exclude
    
    def get_queryset(self):
        """Returns the initial queryset."""
        return watson.search(self.query, models=self.get_models(), exclude=self.get_exclude())
    
    def get_query(self, request):
        """Parses the query from the request."""
        return request.GET.get(self.get_query_param(), "").strip()
    
    empty_query_redirect = None
    
    def get_empty_query_redirect(self):
        """Returns the URL to redirect an empty query to, or None."""
        return self.empty_query_redirect
    
    extra_context = {}
    
    def get_extra_context(self):
        """
        Returns any extra context variables.
        
        Required for backwards compatibility with old function-based views.
        """
        return self.extra_context
    
    def get_context_data(self, **kwargs):
        """Generates context variables."""
        context = super(SearchMixin, self).get_context_data(**kwargs)
        context["query"] = self.query
        # Process extra context.
        for key, value in six.iteritems(self.get_extra_context()):
            if callable(value):
                value = value()
            context[key] = value
        return context
    
    def get(self, request):
        """Performs a GET request."""
        self.query = self.get_query(request)
        if not self.query:
            empty_query_redirect = self.get_empty_query_redirect()
            if empty_query_redirect:
                return redirect(empty_query_redirect)
        return super(SearchMixin, self).get(request)


"""SEARCH"""
class SearchView_IDB(SearchMixin, generic.ListView):
	"""View that performs a search and returns the search results."""
	template_name = "watson/search.html"


def search_idb(request,**kwargs):
	return SearchView_IDB.as_view(**kwargs)(request)



