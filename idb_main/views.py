from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

# Create your views here.
def index(request) :
	context = RequestContext(request)
	t = loader.get_template('idb_main/design.html')

	return HttpResponse(t.render(context))