from django.http import HttpResponse
from django.db.models import Q
from json import dumps, loads
from idb.models import MVP, Franchise, SuperBowl

def merge(*dicts):
    """
    This is a helper function to merge multiple dictionaries and return
    a new merged dictionary.
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result

def make_successful_response_object(body):
    return {
        "success": True,
        "data": body
    }

def make_failure_response_object(error_type, error_message):
    return {
        "success": False,
        "error": {
            "type": str(error_type),
            "message": str(error_msg)
        }
    }

def make_path(_type = "", _id = None):
    p = "/api/v2/" + str(_type)
    if _id is not None:
        p += "/" + str(_id)
    return p

def make_ref(model):
    _type = str(type(model).__name__).lower() + "s"
    return {
        "id" : model.id,
        "self": make_path(_type, model.id),
        "collection": make_path(_type)
    }

def serialize_superbowl_model(model) :
    return merge(make_ref(model), {
        "winning_franchise": make_ref(model.winning_franchise),
        "losing_franchise": make_ref(model.losing_franchise),
        "mvp": make_ref(model.mvp),
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

def serialize_franchise_model(model) :
    return merge(make_ref(model), {
        "mvps" : [make_ref(m) for m in model.mvps.all()],
        "superbowls_won" : [make_ref(sb) for sb in SuperBowl.objects.filter(Q(winning_franchise = model))],
        "superbowls_lost" : [make_ref(sb) for sb in SuperBowl.objects.filter(Q(losing_franchise = model))],
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

def serialize_mvp_model(model) :
    return merge(make_ref(model), {
        "superbowls" : [make_ref(sb) for sb in SuperBowl.objects.filter(mvp = model)],
        "franchises" : [make_ref(f) for f in Franchise.objects.filter(mvps__in = [model])],
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
