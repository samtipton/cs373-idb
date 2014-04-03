from django.test import TestCase
from urllib.request import urlopen, Request
from json import dumps, loads
import types

# ----------------------
# RESTful API Unit Tests
# Inglorious Bashers
# ----------------------


class test_API(TestCase) :

	def assert_successful_response(self, api_response, expected_response):

		self.assertTrue(type(api_response) is dict)
		self.assertTrue("success" in api_response)
		self.assertTrue(api_response["success"])
		self.assertTrue("data" in api_response)
		self.assertEqual(api_response["data"], expected_response)

	def assert_failure_response(self, api_response, error_type, error_message):

		self.assertTrue(type(api_response) is dict)
		self.assertTrue("success" in api_response)
		self.assertFalse(api_response["success"])
		self.assertTrue("error" in api_response)
		self.assertTrue(type(api_response["error"] is dict))
		self.assertTrue("type" in api_response["error"])
		self.assertEqual(api_response["error"]["type"], error_type)
		self.assertTrue("message" in api_response["error"])
		self.assertEqual(api_response["error"]["message"], error_message)


	# -----------------------------------------
	# get
	# -----------------------------------------
	# check status codes and content is correct
	# ----------------------------------------- 
		
	def test_API_get_superbowls_content(self) :
		response = urlopen("http://idb.apiary-mock.com/api/v2/superbowls")

		self.assertEqual(response.getcode(), 200)

		str_response = response.readall().decode("utf-8")
		
		response_content_list = loads(str_response)
		actual_response_list =     [
			{
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
    		}
    	]	
		self.assert_successful_response(response_content_list, actual_response_list)


	# def test_API_get_teams_content(self) :
	# 	response = urlopen("http://idb.apiary-mock.com/api/v2/teams")
		
	# 	self.assertEqual(response.getcode(), 200)

	# 	str_response = response.readall().decode("utf-8")

	# 	response_content_list = loads(str_response)
	# 	actual_response_list = [
	#         {
	#             "team_name" : "Seahawks",
	#             "team_city" : "Seattle",
	#             "owner" : "Paul Allen",
	#             "sb_appearances" : [40, 48],
	#             "mvp_list" : ["Malcom Smith"]
	#         }
	# 	]
		
	# 	self.assertTrue(actual_response_list == response_content_list)
		

	# def test_API_get_players_content(self) :
	# 	response = urlopen("http://idb.apiary-mock.com/api/v2/players")

	# 	self.assertEqual(response.getcode(), 200)

	# 	str_response = response.readall().decode("utf-8")
		
	# 	response_content_list = loads(str_response)
	# 	actual_response_list = [
	#         {
	#             "first_name" : "Peyton",
	#             "last_name" : "Manning",
	#             "teams" : ["Indianapolis Colts", "Denver Broncos"],
	#             "sb_appearances" : [41, 44, 48],
	#             "birth_date" : "1976-03-24",
	#             "birth_town" : "New Orleans, LA",
	#             "high_school" : "New Orleans Newman",
	#             "college" : "University of Tennessee",
	#             "draft_year" : 1998,
	#             "retired" : false
	#         }
	# 	]
		
	# 	self.assertTrue(actual_response_list == response_content_list)


	# def test_API_get_single_game_content(self) :
	# 	response = urlopen("http://idb.apiary-mock.com/api/v2/games/{id}")
		
	# 	self.assertEqual(response.getcode(), 200)

	# 	str_response = response.readall().decode("utf-8")
		
	# 	response_content_list = loads(str_response)
	# 	actual_response_list = {
	# 	    "winning_team" : "Seattle Seahawks",
	#         "losing_team" : "Denver Broncos",
	#         "mvp" : "Malcom Smith",
	#         "winning_score" : 48,
	#         "losing_score" : 3,
	#         "venue" : "MetLife Stadium",
	#         "game_day" : "2014-02-14",
	#         "game_number" : "XLVIII"
	# 	}

	# 	self.assertTrue(actual_response_list == response_content_list)

	# 	actual_response_list = {
	# 	}

	# 	self.assertFalse(actual_response_list == response_content_list)

		

	# def test_API_get_single_team_content(self) :
	# 	response = urlopen("http://idb.apiary-mock.com/api/v2/teams/{id}")

	# 	self.assertEqual(response.getcode(), 200)

	# 	str_response = response.readall().decode("utf-8")
		
	# 	response_content_list = loads(str_response)
	# 	actual_response_list = {
	# 	    "team_name" : "Seahawks",
	#         "team_city" : "Seattle",
	#         "owner" : "Paul Allen",
	#         "sb_appearances" : [40, 48],
	#         "mvp_list" : ["Malcom Smith"]
	# 	}
		
	# 	self.assertTrue(actual_response_list == response_content_list)

	# 	actual_response_list = {
	# 	    "team_name" : "Seahawks",
	# 	    "team_city" : "Seattle"
	# 	}
		
	# 	self.assertFalse(actual_response_list == response_content_list)

	
	# def test_API_get_single_player_content(self) :
	# 	response = urlopen("http://idb.apiary-mock.com/api/v2/players/{id}")
		
	# 	self.assertEqual(response.getcode(), 200)
	# 	self.assertNotEqual(response.getcode(), 404)

	# 	str_response = response.readall().decode("utf-8")

	# 	response_content_list = loads(str_response)
	# 	actual_response_list = {
	#         "first_name" : "Peyton",
	#         "last_name" : "Manning",
	#         "teams" : ["Indianapolis Colts", "Denver Broncos"],
	#         "sb_appearances" : [41, 44, 48],
	#         "birth_date" : "1976-03-24",
	#         "birth_town" : "New Orleans, LA",
	#         "high_school" : "New Orleans Newman",
	#         "college" : "University of Tennessee",
	#         "draft_year" : 1998,
	#         "retired" : false
	# 	}

	# 	self.assertTrue(actual_response_list == response_content_list)


	# 	actual_response_list = {
	# 	    "first_name" : "Archie",
	# 	    "last_name" : "Manning",
	# 	    "birth_date" : "1949-05-19",
	# 	    "birth_town" : "New Orleans, LA",
	# 	    "high_school" : "New Orleans Newman",
	# 	    "college" : "University of Tennessee",
	# 	    "Totally" : "Not suppose to be here"
	# 	}

	# 	self.assertFalse(actual_response_list == response_content_list)


	# # ----------------------
	# # delete
	# # ----------------------
	# # check status codes only
	# # ----------------------

	# def test_API_remove_games_response(self) :
	# 	request = Request("http://idb.apiary-mock.com/api/v2/games/{id}")
	# 	request.get_method = lambda: 'DELETE'
	# 	response = urlopen(request)
	# 	self.assertEqual(response.getcode(), 204)

	# def test_API_remove_teams_response(self) :
	# 	request = Request("http://idb.apiary-mock.com/api/v2/teams/{id}")
	# 	request.get_method = lambda: 'DELETE'
	# 	response = urlopen(request)
	# 	self.assertEqual(response.getcode(), 204)

	# def test_API_remove_players_response(self) :
	# 	request = Request("http://idb.apiary-mock.com/api/v2/players/{id}")
	# 	request.get_method = lambda: 'DELETE'
	# 	response = urlopen(request)
	# 	self.assertEqual(response.getcode(), 204)
	# 	request.get_method = lambda: 'GET'
	# 	response = urlopen(request)
	# 	self.assertNotEqual(response.getcode(), 204)
	# # -----------------------------------------
	# # post
	# # -----------------------------------------
	# # check status codes and content is correct
	# # ----------------------------------------- 

	# def test_API_post_games_content(self) :
	# 	values = dumps({
	# 	    "winning_team" : "Seattle Seahawks",
	#         "losing_team" : "Denver Broncos",
	#         "mvp" : "Malcom Smith",
	#         "winning_score" : 48,
	#         "losing_score" : 3,
	#         "venue" : "MetLife Stadium",
	#         "game_day" : "2014-02-14",
	#         "game_number" : "XLVIII"
	# 	})
	# 	headers = {"Content-Type": "application/json"}
	# 	vbin = values.encode("utf-8")
	# 	request = Request("http://idb.apiary-mock.com/api/v2/games", data=vbin, headers=headers)
		
	# 	response = urlopen(request)
	# 	self.assertEqual(response.getcode(), 201)
	# 	#formatting response
	# 	str_response = response.readall().decode("utf-8")
	# 	obj_response = loads(str_response)

	# 	actual_response = {'id' : 48}
	# 	self.assertEqual(obj_response, actual_response)

	# def test_API_post_teams_content(self) :
	# 	values = dumps({
	# 	    "team_name" : "Seahawks",
	#         "team_city" : "Seattle",
	#         "owner" : "Paul Allen",
	#         "sb_appearances" : [40, 48],
	#         "mvp_list" : ["Malcom Smith"]
	# 	})
	# 	headers = {"Content-Type": "application/json"}
	# 	vbin = values.encode("utf-8")
	# 	request = Request("http://idb.apiary-mock.com/api/v2/teams", data=vbin, headers=headers)		
		
	# 	response = urlopen(request)
	# 	self.assertEqual(response.getcode(), 201)
	# 	self.assertNotEqual(response.getcode(), 204)
	# 	#formatting response
	# 	str_response = response.readall().decode("utf-8")
	# 	obj_response = loads(str_response)

	# 	actual_response = {'id' : 1}
	# 	self.assertEqual(obj_response, actual_response)
	

	# def test_API_post_players_content(self) :
	# 	values = dumps({
	# 	   	"first_name" : "Peyton",
	#         "last_name" : "Manning",
	#         "teams" : ["Indianapolis Colts", "Denver Broncos"],
	#         "sb_appearances" : [41, 44, 48],
	#         "birth_date" : "1976-03-24",
	#         "birth_town" : "New Orleans, LA",
	#         "high_school" : "New Orleans Newman",
	#         "college" : "University of Tennessee",
	#         "draft_year" : 1998,
	#         "retired" : false
	# 	})
	# 	headers = {"Content-Type": "application/json"}	
	# 	vbin = values.encode("utf-8")
	# 	request = Request("http://idb.apiary-mock.com/api/v2/players", data=vbin, headers=headers)		
		
	# 	response = urlopen(request)
	# 	self.assertEqual(response.getcode(), 201)
	# 	#formatting response
	# 	str_response = response.readall().decode("utf-8")
	# 	obj_response = loads(str_response)

	# 	actual_response = {'id' : 1}
	# 	self.assertEqual(obj_response, actual_response)

	# 	actual_response = {'id' : 2}
	# 	self.assertNotEqual(obj_response, actual_response)


	# # -----------------------
	# # put
	# # -----------------------
	# # check status codes only
	# # -----------------------


	# def test_API_put_game_response(self) :
	# 	values = dumps({
	# 	    "winning_team" : "Seattle Seahawks",
	#         "losing_team" : "Denver Broncos",
	#         "mvp" : "Malcom Smith",
	#         "winning_score" : 48,
	#         "losing_score" : 3,
	#         "venue" : "MetLife Stadium",
	#         "game_day" : "2014-02-14",
	#         "game_number" : "XLVIII"
	# 	})

	# 	headers = {"Content-Type": "application/json"}
	# 	vbin = values.encode("utf-8")
	# 	request = Request("http://idb.apiary-mock.com/api/v2/games/{id}", data=vbin, headers=headers)
	# 	request.get_method = lambda: 'PUT'
	# 	response = urlopen(request)
	# 	self.assertEqual(response.getcode(), 204)
	# 	self.assertNotEqual(response.getcode(), 304)

	# def test_API_put_team_response(self) :
	# 	values = dumps({
	# 	    "team_name" : "Seahawks",
	#         "team_city" : "Seattle",
	#         "owner" : "Paul Allen",
	#         "sb_appearances" : [40, 48],
	#         "mvp_list" : ["Malcom Smith"]
	# 	})

	# 	headers = {"Content-Type": "application/json"}
	# 	vbin = values.encode("utf-8")
	# 	request = Request("http://idb.apiary-mock.com/api/v2/teams/{id}", data=vbin, headers=headers)
	# 	request.get_method = lambda: 'PUT'
	# 	response = urlopen(request)
	# 	self.assertEqual(response.getcode(), 204)

	# 	request.get_method = lambda: 'GET'
	# 	response = urlopen(request)
	# 	self.assertNotEqual(response.getcode(), 204)


	# def test_API_put_player_response(self) :
	# 	values = dumps({
	# 	    "first_name" : "Peyton",
	#         "last_name" : "Manning",
	#         "teams" : ["Indianapolis Colts", "Denver Broncos"],
	#         "sb_appearances" : [41, 44, 48],
	#         "birth_date" : "1976-03-24",
	#         "birth_town" : "New Orleans, LA",
	#         "high_school" : "New Orleans Newman",
	#         "college" : "University of Tennessee",
	#         "draft_year" : 1998,
	#    	    "retired" : false
	# 	})

	# 	headers = {"Content-Type": "application/json"}
	# 	vbin = values.encode("utf-8")
	# 	request = Request("http://idb.apiary-mock.com/api/v2/players/{id}", data=vbin, headers=headers)
	# 	request.get_method = lambda: 'PUT'
	# 	response = urlopen(request)
	# 	self.assertEqual(response.getcode(), 204)

print("IngloriousBashers-tests.py")

print("Done.")