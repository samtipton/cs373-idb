from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from idb.models import MVP, Franchise, SuperBowl
from django.db.models import Q
from json import dumps, loads
from idb.helpers import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection

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
    return make_response(405, obj)

def respond_with_bad_request_error(request):
    error_type = 'HTTP_BAD_REQUEST'
    message = "This request has violated the API contract. To help you, this is the input you provided. HTTP method '{0}'. Endpoint url '{1}'. Request content '{2}'."
    error_message = message.format(request.method, request.path, request.body.decode('utf-8'))
    obj = make_failure_response_object(error_type, error_message)
    return make_response(400, obj)

def respond_with_not_found_error(request):
    error_type = 'HTTP_NOT_FOUND'
    message = "The resource '{0}' does not exist."
    error_message = message.format(request.path)
    obj = make_failure_response_object(error_type, error_message)
    return make_response(404, obj)

# custom internal API to reset the database
def api_reset_database(request):
    cursor = connection.cursor()
    cursor.execute("SELECT reset_db()")
    return make_response(200, str(cursor.fetchone()[0]))

# -------------------
# API SuperBowl Calls
# -------------------
def api_superbowls(request) :
    try:
        # check context to determine what kind of req
        if (request.method == 'GET'):
            return superbowls_get()
        elif (request.method == 'POST'):
            return superbowls_post(request)
        else:
            return respond_with_method_not_allowed_error(request)
    except Exception:
        return respond_with_bad_request_error(request)

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

    return make_response(201, make_successful_response_object(make_ref(sb)))


def api_superbowls_id(request, _id):
    try:
        if (request.method == 'GET'):
            return superbowls_id_get(_id)
        elif (request.method == 'PUT'):
            return superbowls_id_put(_id, request)
        elif (request.method == 'DELETE'):
            return superbowls_id_delete(_id)
        else:
            return respond_with_method_not_allowed_error(request)
    except ObjectDoesNotExist:
        return respond_with_not_found_error(request)

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
    try:
        # check context to determine what kind of req
        if (request.method == 'GET'):
            return franchises_get()
        elif (request.method == 'POST'):
            return franchises_post(request)
        else:
            return respond_with_method_not_allowed_error(request)
    except Exception:
            return respond_with_bad_request_error(request)

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

    sbw_id_list = json_content["superbowls_won"]

    sbw_list = [SuperBowl.objects.get(pk=entry['id']) for entry in sbw_id_list]

    sbl_id_list = json_content["superbowls_lost"]

    sbl_list = [SuperBowl.objects.get(pk=entry['id']) for entry in sbl_id_list]

    franchise = Franchise(
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

    for m in mvp_list :
        franchise.mvps.add(m)

    for sb in sbw_list:
        sb.winning_franchise = franchise
        sb.save()

    for sb in sbl_list:
        sb.losing_franchise = franchise
        sb.save()

    return make_response(201, make_successful_response_object(make_ref(franchise)))


def api_franchises_id(request, _id) :
    try:
        try:
            if (request.method == 'GET'):
                return franchises_id_get(_id)
            elif (request.method == 'PUT'):
                return franchises_id_put(_id, request)
            elif (request.method == 'DELETE'):
                return franchises_id_delete(_id)
            else:
                return respond_with_method_not_allowed_error(request)
        except ObjectDoesNotExist:
            return respond_with_not_found_error(request)
    except Exception:
        return respond_with_bad_request_error(request)

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

    sbw_id_list = json_content["superbowls_won"]

    sbw_list = [SuperBowl.objects.get(pk=entry['id']) for entry in sbw_id_list]

    sbl_id_list = json_content["superbowls_lost"]

    sbl_list = [SuperBowl.objects.get(pk=entry['id']) for entry in sbl_id_list]

    f.mvps = mvp_list
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

    for sb in sbw_list:
        sb.winning_franchise = f
        sb.save()

    for sb in sbl_list:
        sb.losing_franchise = f
        sb.save()

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
    try:
        # check context to determine what kind of req
        if (request.method == 'GET'):
            return mvps_get()
        elif (request.method == 'POST'):
            return mvps_post(request)
        else:
            return respond_with_method_not_allowed_error(request)
    except Exception:
        return respond_with_bad_request_error(request)

def mvps_get() :
    mvps = MVP.objects.all()
    body = []

    for p in mvps:
        body.append(serialize_mvp_model(p))

    return make_response(200, make_successful_response_object(body))

def mvps_post(request):
    json_content = loads(request.body.decode('utf-8'))

    # get specific model content
    superbowl_id_list = json_content["superbowls"]

    sb_list = [SuperBowl.objects.get(pk=entry['id']) for entry in superbowl_id_list]

    f_id_list = json_content["franchises"]

    f_list = [Franchise.objects.get(pk=entry['id']) for entry in f_id_list]

    mvp = MVP(
        first_name =  json_content["first_name"],
        last_name =  json_content["last_name"],
        position =  json_content["position"],
        birth_date =  json_content["birth_date"],
        birth_town =  json_content["birth_town"],
        high_school =  json_content["high_school"],
        college =  json_content["college"],
        draft_year =  json_content["draft_year"],
        active =  json_content["active"],
        salary =  json_content["salary"],
        facebook_id =  json_content["facebook_id"],
        twitter_id =  json_content["twitter_id"],
        youtube_id =  json_content["youtube_id"],
        latitude =  json_content["latitude"],
        longitude =  json_content["longitude"])
    mvp.save()

    for sb in sb_list:
        sb.mvp = mvp
        sb.save()

    for franchise in f_list:
        franchise.mvps.add(mvp)
        franchise.save()

    return make_response(201, make_successful_response_object(make_ref(mvp)))


def api_mvps_id(request, _id) :
    try:
        try:
            if (request.method == 'GET'):
                return mvps_id_get(_id)
            elif (request.method == 'PUT'):
                return mvps_id_put(_id, request)
            elif (request.method == 'DELETE'):
                return mvps_id_delete(_id)
            else:
                return respond_with_method_not_allowed_error(request)
        except ObjectDoesNotExist:
            return respond_with_not_found_error(request)
    except Exception:
            return respond_with_bad_request_error(request)

def mvps_id_get(_id):
    p = MVP.objects.get(pk=_id)
    body = serialize_mvp_model(p)

    return make_response(200, make_successful_response_object(body))

def mvps_id_put(_id, request):
    mvp = MVP.objects.get(pk=_id)
    json_content = loads(request.body.decode('utf-8'))

    # get specific model content
    superbowl_id_list = json_content["superbowls"]

    sb_list = [SuperBowl.objects.get(pk=entry['id']) for entry in superbowl_id_list]

    f_id_list = json_content["franchises"]

    f_list = [Franchise.objects.get(pk=entry['id']) for entry in f_id_list]

    mvp.first_name =  json_content["first_name"]
    mvp.last_name =  json_content["last_name"]
    mvp.position =  json_content["position"]
    mvp.birth_date =  json_content["birth_date"]
    mvp.birth_town =  json_content["birth_town"]
    mvp.high_school =  json_content["high_school"]
    mvp.college =  json_content["college"]
    mvp.draft_year =  json_content["draft_year"]
    mvp.active =  json_content["active"]
    mvp.salary =  json_content["salary"]
    mvp.facebook_id =  json_content["facebook_id"]
    mvp.twitter_id =  json_content["twitter_id"]
    mvp.youtube_id =  json_content["youtube_id"]
    mvp.latitude =  json_content["latitude"]
    mvp.longitude =  json_content["longitude"]
    mvp.save()

    for sb in sb_list:
        sb.mvp = mvp
        sb.save()

    for franchise in f_list:
        franchise.mvps.add(mvp)
        franchise.save()

    body = serialize_mvp_model(mvp)

    return make_response(200, make_successful_response_object(body))


def mvps_id_delete(_id):
    p = MVP.objects.get(pk=_id)
    p.delete()

    return make_response(200, make_successful_response_object(None))
