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
