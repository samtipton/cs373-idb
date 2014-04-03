from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from idb.models import MVP, Franchise, SuperBowl

from json import dumps, loads


def create_successful_response(code, body):

	body = {
		"success": True,
		"data": body
	}

	response = HttpResponse(dumps(body), content_type='application/json')
	response.status_code = code

	return response

def create_failure_response(code, error_type, error_message) :
	body = {
		"success": False,
		"error": {
			"type": error_type,
			"message": error_message
		}
	}
	response = HttpResponse(dumps(body), content_type='application/json')
	response.status_code = code
	
	return response


def path(self, _type = "", id = None):
	p = "/api/v2/" + str(_type)
	if id is not None:
		p += "/" + str(id)
	return p

def ref(model, body = {}):
	_type = str(model.__name__).lower() + "s"
	temp = {
		"id" = model.id,
		"self": self.path(_type, model.id),
		"collection": self.path(_type)
	}
	temp.update(body)
	return temp



def api_superbowl_id(request, id) :
	context = RequestContext(request)

	sb = SuperBowl.objects.get(pk=id)

	body = ref(sb, {
        
        "winning_franchise": ref(sb.winning_franchise),
        "losing_franchise": ref(sb.losing_franchise),
        "mvp": ref(sb.mvp),
        "winning_score": 43,
        "losing_score": 8,
        "venue_name": "MetLife Stadium",
        "venue_city": "East Rutherford",
        "venue_state": "NJ",
        "game_day": "2014-02-02",
        "attendance": 82529,
        "game_number": "XLVIII",
        "halftime_performer": "Bruno Mars"
    })

	return create_successful_response(200, body)

def api_superbowls(request) :
	context = RequestContext(request)

	body = [{
        "id": 0,
        "self": "http://blooming-shelf-7492.herokuapp.com/api/v2/superbowls/0",
        "collection": "http://blooming-shelf-7492.herokuapp.com/api/v2/superbowls",
        "winning_franchise":
        {
            "id": 0,
            "self": "http://blooming-shelf-7492.herokuapp.com/api/v2/franchises/0",
            "collection": "http://blooming-shelf-7492.herokuapp.com/api/v2/franchises"
        },
        "losing_franchise":
        {
            "id": 1,
            "self": "http://blooming-shelf-7492.herokuapp.com/api/v2/franchises/1",
            "collection": "http://blooming-shelf-7492.herokuapp.com/api/v2/franchises"
        },
        "mvp":
        {
            "id": 0,
            "self": "http://blooming-shelf-7492.herokuapp.com/api/v2/mvps/0",
            "collection": "http://blooming-shelf-7492.herokuapp.com/api/v2/mvps"
        },
        "winning_score": 43,
        "losing_score": 8,
        "venue_name": "MetLife Stadium",
        "venue_city": "East Rutherford",
        "venue_state": "NJ",
        "game_day": "2014-02-02",
        "attendance": 82529,
        "game_number": "XLVIII",
        "halftime_performer": "Bruno Mars"
    }]

	return create_successful_response(200, body)

