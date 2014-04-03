from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from idb.models import MVP, Franchise, SuperBowl
from django.db.models import Q

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

# ----------------
# helper functions
# ----------------

def path(_type = "", _id = None):
	p = "/api/v2/" + str(_type)
	if _id is not None:
		p += "/" + str(_id)
	return p

def ref(model, body = {}):
	_type = str(type(model).__name__).lower() + "s"
	temp = {
		"id" : model.id,
		"self": path(_type, model.id),
		"collection": path(_type)
	}
	temp.update(body)
	return temp


def create_sb_response_object(model) :
	return ref(model, {
		"winning_franchise": ref(model.winning_franchise),
		"losing_franchise": ref(model.losing_franchise),
		"mvp": ref(model.mvp),
		"mvp_stats" : model.mvp_stats,
		"mvp_blurb" : model.mvp_blurb,
		"winning_score": model.winning_score,
		"losing_score": model.losing_score,
		"venue_name": model.venue_name,
		"venue_city": model.venue_city,
		"venue_state": model.venue_state,
		"game_day": str(model.game_day),
		"attendance": model.attendance,
		"game_number": model.game_number,
		"halftime_performer": model.halftime_performer, 
		"twitter_id" : model.twitter_id,
		"youtube_id" : model.youtube_id,
		"latitude" : model.latitude,
		"longitude" : model.longitude
	})

def create_franchise_response_object(model) :
	return ref(model, {
		"mvps" : [ref(m) for m in model.mvps.all()],
		"superbowls" : [ref(sb) for sb in SuperBowl.objects.filter(Q(winning_franchise = model) | Q(losing_franchise = model))],
		"team_name" : model.team_name,
		"team_city" : model.team_city,
		"team_state" : model.team_state,
		"current_owner" : model.current_owner,
		"current_gm" : model.current_gm,
		"current_head_coach" : model.current_head_coach,
		"year_founded" : model.year_founded,
		"active" : model.active,
		"home_stadium" : model.home_stadium,
		"division" : model.division,
		"facebook_id" : model.facebook_id,
		"twitter_id" : model.twitter_id,
		"youtube_id" : model.youtube_id,
		"latitude" : model.latitude,
		"longitude" : model.longitude
		})

def create_mvp_response_object(model) :
	return ref(model, {
		"superbowls" : [ref(sb) for sb in SuperBowl.objects.filter(mvp = model)],
		"franchises" : [ref(f) for f in Franchise.objects.filter(mvps__in = [model])],
		"first_name" : model.first_name,
		"last_name" : model.last_name,
		"position" : model.position,
		"birth_date" : model.birth_date,
		"birth_town" : model.birth_town,
		"high_school" : model.high_school,
		"college" : model.college,
		"draft_year" : model.draft_year,
		"active" : model.active,
		"salary" : model.salary,
		"facebook_id" : model.facebook_id,
		"twitter_id" : model.twitter_id,
		"youtube_id" : model.youtube_id,
		"latitude" : model.latitude,
		"longitude" : model.longitude
		})

# -------------------
# API SuperBowl Calls
# -------------------
def api_superbowls(request) :
	# context = RequestContext(request)

	# check context to determine what kind of req
	if (request.method == 'GET'):
		return superbowls_get()
	elif (request.method == 'POST'):
		return superbowls_post(request)
	else:
		pass

def superbowls_get() :
	superbowls = SuperBowl.objects.all()
	body = []

	for sb in superbowls:
		body.append(create_sb_response_object(sb))

	return create_successful_response(200, body)

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

	return create_successful_response(201, ref(sb))


def api_superbowls_id(request, _id) :
	if (request.method == 'GET'):
		return superbowls_id_get(_id)
	elif (request.method == 'PUT'):
		return superbowls_id_put(_id, request)
	elif (request.method == 'DELETE'):
		return superbowls_id_delete(_id)
	else:
		pass

def superbowls_id_get(_id) :
	# context = RequestContext(request)

	sb = SuperBowl.objects.get(pk=_id)
	body = create_sb_response_object(sb)

	return create_successful_response(200, body)

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

	body = create_sb_response_object(sb)


	return create_successful_response(200, body)

def superbowls_id_delete(_id) :
	sb = SuperBowl.objects.get(pk=_id)
	sb.delete()

	return create_successful_response(200, None)


# -------------------
# API Franchise Calls
# -------------------

def api_franchises(request) :
	# context = RequestContext(request)

	# check context to determine what kind of req
	if (request.method == 'GET'):
		return franchises_get()
	elif (request.method == 'POST'):
		return franchises_post(request)
	else:
		pass

def franchises_get() :
	franchises = Franchise.objects.all()
	body = []

	for f in franchises:
		body.append(create_franchise_response_object(f))

	return create_successful_response(200, body)

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
	

	return create_successful_response(201, ref(franchise))


def api_franchises_id(request, _id) :
	if (request.method == 'GET'):
		return franchises_id_get(_id)
	elif (request.method == 'PUT'):
		return franchises_id_put(_id, request)
	elif (request.method == 'DELETE'):
		return franchises_id_delete(_id)
	else:
		pass

def franchises_id_get(_id) :
	# context = RequestContext(request)

	f = Franchise.objects.get(pk=_id)
	body = create_franchise_response_object(f)

	return create_successful_response(200, body)

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

	body = create_franchise_response_object(f)


	return create_successful_response(200, body)

def franchises_id_delete(_id) :
	f = Franchise.objects.get(pk=_id)
	f.delete()

	return create_successful_response(200, None)

# -------------
# MVP API Calls
# -------------

def api_mvps(request) :
	pass