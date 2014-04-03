from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from idb.models import MVP, Franchise, SuperBowl
from django.db.models import Q
from json import dumps, loads
from idb.helpers import *

# ----------------
# helper functions
# ----------------

def make_response(code, body):
    response = HttpResponse(dumps(body), content_type='application/json')
	response.status_code = code
	return response

def respond_with_method_not_allowed_error(request):
    error_type = 'HTTP_METHOD_NOT_ALLOWED'
    message = "The method '{0}' is not allowed on the endpoint '{1}'."
    error_message = message.format(request.method, request.path)
    obj = make_failure_response_object(error_type, error_message)
    return make_response(400, obj)

# -------------------
# API SuperBowl Calls
# -------------------
def api_superbowls(request) :
	# check context to determine what kind of req
	if (request.method == 'GET'):
		return superbowls_get()
	elif (request.method == 'POST'):
		return superbowls_post(request)
	else:
		return respond_with_method_not_allowed_error(request)

def superbowls_get() :
	superbowls = SuperBowl.objects.all()
	body = []

	for sb in superbowls:
		body.append(serialize_superbowl_model(sb))

	return make_response(200, make_successful_response_object(body))

def superbowls_post(request) :
	json_content = loads(request.body.decode('utf-8'))

	# get specific model content
	w_id = json_content["winning_franchise"]["id"]

	winning_franchise = Franchise.objects.get(pk=w_id)

	l_id = json_content["losing_franchise"]["id"]

	losing_franchise = Franchise.objects.get(pk=l_id)

	mvp_id = json_content["mvp"]["id"]

	mvp = MVP.objects.get(pk=mvp_id)

	sb = SuperBowl(winning_franchise = winning_franchise,
	 losing_franchise = losing_franchise,
	 mvp = mvp,
	 mvp_stats = json_content["mvp_stats"],
	 mvp_blurb = json_content["mvp_blurb"],
	 winning_score = json_content["winning_score"],
	 losing_score = json_content["losing_score"],
	 venue_name = json_content["venue_name"],
	 venue_city = json_content["venue_city"],
	 venue_state = json_content["venue_state"],
	 game_day = json_content["game_day"],
	 attendance = json_content["attendance"],
	 game_number = json_content["game_number"],
	 halftime_performer = json_content["halftime_performer"],
	 twitter_id = json_content["twitter_id"],
	 youtube_id = json_content["youtube_id"],
	 latitude = json_content["latitude"],
	 longitude = json_content["longitude"])
	sb.save()

	return make_response(200, make_successful_response_object(make_ref(sb)))


def api_superbowls_id(request, _id) :
	if (request.method == 'GET'):
		return superbowls_id_get(_id)
	elif (request.method == 'PUT'):
		return superbowls_id_put(_id, request)
	elif (request.method == 'DELETE'):
		return superbowls_id_delete(_id)
	else:
		return respond_with_method_not_allowed_error(request)

def superbowls_id_get(_id) :

	sb = SuperBowl.objects.get(pk=_id)
	body = serialize_superbowl_model(sb)

	return make_response(200, make_successful_response_object(body))

def superbowls_id_put(_id, request) :
	sb = SuperBowl.objects.get(pk=_id)
	json_content = loads(request.body.decode('utf-8'))

	# get specific model content
	w_id = json_content["winning_franchise"]["id"]

	winning_franchise = Franchise.objects.get(pk=w_id)

	l_id = json_content["losing_franchise"]["id"]

	losing_franchise = Franchise.objects.get(pk=l_id)

	mvp_id = json_content["mvp"]["id"]

	mvp = MVP.objects.get(pk=mvp_id)

	sb.winning_franchise = winning_franchise
	sb.losing_franchise = losing_franchise
	sb.mvp = mvp
	sb.mvp_stats = json_content["mvp_stats"]
	sb.mvp_blurb = json_content["mvp_blurb"]
	sb.winning_score = json_content["winning_score"]
	sb.losing_score = json_content["losing_score"]
	sb.venue_name = json_content["venue_name"]
	sb.venue_city = json_content["venue_city"]
	sb.venue_state = json_content["venue_state"]
	sb.game_day = json_content["game_day"]
	sb.attendance = json_content["attendance"]
	sb.game_number = json_content["game_number"]
	sb.halftime_performer = json_content["halftime_performer"]
	sb.twitter_id = json_content["twitter_id"]
	sb.youtube_id = json_content["youtube_id"]
	sb.latitude = json_content["latitude"]
	sb.longitude = json_content["longitude"]
	sb.save()

	body = serialize_superbowl_model(sb)


	return make_response(200, make_successful_response_object(body))

def superbowls_id_delete(_id) :
	sb = SuperBowl.objects.get(pk=_id)
	sb.delete()

	return make_response(200, make_successful_response_object(None))

# -------------------
# API Franchise Calls
# -------------------

def api_franchises(request) :

	# check context to determine what kind of req
	if (request.method == 'GET'):
		return franchises_get()
	elif (request.method == 'POST'):
		return franchises_post(request)
	else:
		return respond_with_method_not_allowed_error(request)

def franchises_get() :
	franchises = Franchise.objects.all()
	body = []

	for f in franchises:
		body.append(serialize_franchise_model(f))

	return make_response(200, make_successful_response_object(body))

def franchises_post(request) :
	json_content = loads(request.body.decode('utf-8'))

	# get specific model content
	mvp_id_list = json_content["mvps"]

	mvp_list = [MVP.objects.get(pk=entry['id']) for entry in mvp_id_list]

	sb_id_list = json_content["superbowls"]

	sb_list = [SuperBowl.objects.get(pk=entry['id']) for entry in sb_id_list]

	franchise = Franchise(mvps = mvp_list,
		team_name = json_content["team_name"],
		team_city = json_content["team_city"],
		team_state = json_content["team_state"],
		current_owner = json_content["current_owner"],
		current_gm = json_content["current_gm"],
		current_head_coach = json_content["current_head_coach"],
		year_founded = json_content["year_founded"],
		active = json_content["active"],
		home_stadium = json_content["home_stadium"],
		division = json_content["division"],
		facebook_id = json_content["facebook_id"],
		twitter_id = json_content["twitter_id"],
		youtube_id = json_content["youtube_id"],
		latitude = json_content["latitude"],
		longitude = json_content["longitude"])
	franchise.save()


	return make_response(200, make_successful_response_object(make_ref(franchise)))


def api_franchises_id(request, _id) :
	if (request.method == 'GET'):
		return franchises_id_get(_id)
	elif (request.method == 'PUT'):
		return franchises_id_put(_id, request)
	elif (request.method == 'DELETE'):
		return franchises_id_delete(_id)
	else:
	       return respond_with_method_not_allowed_error(request)

def franchises_id_get(_id) :
	# context = RequestContext(request)

	f = Franchise.objects.get(pk=_id)
	body = serialize_franchise_model(f)

	return make_response(200, make_successful_response_object(body))

def franchises_id_put(_id, request) :
	f = Franchise.objects.get(pk=_id)
	json_content = loads(request.body.decode('utf-8'))

	# get specific model content
	mvp_id_list = json_content["mvps"]

	mvp_list = [MVP.objects.get(pk=entry['id']) for entry in mvp_id_list]

	sb_id_list = json_content["superbowls"]

	sb_list = [SuperBowl.objects.get(pk=entry['id']) for entry in sb_id_list]

	f.mvps = mvp_list
	f.superbowls = sb_list
	f.team_name = json_content["team_name"]
	f.team_city = json_content["team_city"]
	f.team_state = json_content["team_state"]
	f.current_owner = json_content["current_owner"]
	f.current_gm = json_content["current_gm"]
	f.current_head_coach = json_content["current_head_coach"]
	f.year_founded = json_content["year_founded"]
	f.active = json_content["active"]
	f.home_stadium = json_content["home_stadium"]
	f.division = json_content["division"]
	f.facebook_id = json_content["facebook_id"]
	f.twitter_id = json_content["twitter_id"]
	f.youtube_id = json_content["youtube_id"]
	f.latitude = json_content["latitude"]
	f.longitude = json_content["longitude"]
	f.save()

	body = serialize_franchise_model(f)

	return make_response(200, make_successful_response_object(body))

def franchises_id_delete(_id) :
	f = Franchise.objects.get(pk=_id)
	f.delete()

	return make_response(200, make_successful_response_object(None))

# -------------
# MVP API Calls
# -------------

def api_mvps(request) :
	return respond_with_method_not_allowed_error(request)

def api_mvps_id(request) :
	return respond_with_method_not_allowed_error(request)
