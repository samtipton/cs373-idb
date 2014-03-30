from django.test import TestCase
from urllib.request import urlopen, Request
from json import dumps, loads

# ----------------------
# RESTful API Unit Tests
# Inglorious Bashers
# ----------------------


class test_API(TestCase) :

	# -----------------------------------------
	# get
	# -----------------------------------------
	# check status codes and content is correct
	# ----------------------------------------- 
		
	def test_API_get_game_content(self) :
		response = urlopen("http://idb.apiary.io/api/games")

		self.assertEqual(response.getcode(), 200)

		str_response = response.readall().decode("utf-8")
		
		response_content_list = loads(str_response)
		actual_response_list = [
	        {
	            "winning_team" : "Seattle Seahawks",
	            "losing_team" : "Denver Broncos",
	            "mvp" : "Malcom Smith",
	            "winning_score" : 48,
	            "losing_score" : 3,
	            "venue" : "MetLife Stadium",
	            "game_day" : "2014-02-14",
	            "game_number" : "XLVIII"
        	}
		]	

		self.assertTrue(actual_response_list == response_content_list)


	def test_API_get_teams_content(self) :
		response = urlopen("http://idb.apiary.io/api/teams")
		
		self.assertEqual(response.getcode(), 200)

		str_response = response.readall().decode("utf-8")

		response_content_list = loads(str_response)
		actual_response_list = [
	        {
	            "team_name" : "Seahawks",
	            "team_city" : "Seattle",
	            "owner" : "Paul Allen",
	            "sb_appearances" : [40, 48],
	            "mvp_list" : ["Malcom Smith"]
	        }
		]
		
		self.assertTrue(actual_response_list == response_content_list)
		

	def test_API_get_players_content(self) :
		response = urlopen("http://idb.apiary.io/api/players")

		self.assertEqual(response.getcode(), 200)

		str_response = response.readall().decode("utf-8")
		
		response_content_list = loads(str_response)
		actual_response_list = [
	        {
	            "first_name" : "Peyton",
	            "last_name" : "Manning",
	            "teams" : ["Indianapolis Colts", "Denver Broncos"],
	            "sb_appearances" : [41, 44, 48],
	            "birth_date" : "1976-03-24",
	            "birth_town" : "New Orleans, LA",
	            "high_school" : "New Orleans Newman",
	            "college" : "University of Tennessee",
	            "draft_year" : 1998,
	            "retired" : false
	        }
		]
		
		self.assertTrue(actual_response_list == response_content_list)


	def test_API_get_single_game_content(self) :
		response = urlopen("http://idb.apiary.io/api/games/{id}")
		
		self.assertEqual(response.getcode(), 200)

		str_response = response.readall().decode("utf-8")
		
		response_content_list = loads(str_response)
		actual_response_list = {
		    "winning_team" : "Seattle Seahawks",
	        "losing_team" : "Denver Broncos",
	        "mvp" : "Malcom Smith",
	        "winning_score" : 48,
	        "losing_score" : 3,
	        "venue" : "MetLife Stadium",
	        "game_day" : "2014-02-14",
	        "game_number" : "XLVIII"
		}

		self.assertTrue(actual_response_list == response_content_list)

		actual_response_list = {
		}

		self.assertFalse(actual_response_list == response_content_list)

		

	def test_API_get_single_team_content(self) :
		response = urlopen("http://idb.apiary.io/api/teams/{id}")

		self.assertEqual(response.getcode(), 200)

		str_response = response.readall().decode("utf-8")
		
		response_content_list = loads(str_response)
		actual_response_list = {
		    "team_name" : "Seahawks",
	        "team_city" : "Seattle",
	        "owner" : "Paul Allen",
	        "sb_appearances" : [40, 48],
	        "mvp_list" : ["Malcom Smith"]
		}
		
		self.assertTrue(actual_response_list == response_content_list)

		actual_response_list = {
		    "team_name" : "Seahawks",
		    "team_city" : "Seattle"
		}
		
		self.assertFalse(actual_response_list == response_content_list)

	
	def test_API_get_single_player_content(self) :
		response = urlopen("http://idb.apiary.io/api/players/{id}")
		
		self.assertEqual(response.getcode(), 200)
		self.assertNotEqual(response.getcode(), 404)

		str_response = response.readall().decode("utf-8")

		response_content_list = loads(str_response)
		actual_response_list = {
	        "first_name" : "Peyton",
	        "last_name" : "Manning",
	        "teams" : ["Indianapolis Colts", "Denver Broncos"],
	        "sb_appearances" : [41, 44, 48],
	        "birth_date" : "1976-03-24",
	        "birth_town" : "New Orleans, LA",
	        "high_school" : "New Orleans Newman",
	        "college" : "University of Tennessee",
	        "draft_year" : 1998,
	        "retired" : false
		}

		self.assertTrue(actual_response_list == response_content_list)


		actual_response_list = {
		    "first_name" : "Archie",
		    "last_name" : "Manning",
		    "birth_date" : "1949-05-19",
		    "birth_town" : "New Orleans, LA",
		    "high_school" : "New Orleans Newman",
		    "college" : "University of Tennessee",
		    "Totally" : "Not suppose to be here"
		}

		self.assertFalse(actual_response_list == response_content_list)


	# ----------------------
	# delete
	# ----------------------
	# check status codes only
	# ----------------------

	def test_API_remove_games_response(self) :
		request = Request("http://idb.apiary.io/api/games/{id}")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)
		self.assertEqual(response.getcode(), 204)

	def test_API_remove_teams_response(self) :
		request = Request("http://idb.apiary.io/api/teams/{id}")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)
		self.assertEqual(response.getcode(), 204)

	def test_API_remove_players_response(self) :
		request = Request("http://idb.apiary.io/api/players/{id}")
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)
		self.assertEqual(response.getcode(), 204)
		request.get_method = lambda: 'GET'
		response = urlopen(request)
		self.assertNotEqual(response.getcode(), 204)
	# -----------------------------------------
	# post
	# -----------------------------------------
	# check status codes and content is correct
	# ----------------------------------------- 

	def test_API_post_games_content(self) :
		values = dumps({
		    "winning_team" : "Seattle Seahawks",
	        "losing_team" : "Denver Broncos",
	        "mvp" : "Malcom Smith",
	        "winning_score" : 48,
	        "losing_score" : 3,
	        "venue" : "MetLife Stadium",
	        "game_day" : "2014-02-14",
	        "game_number" : "XLVIII"
		})
		headers = {"Content-Type": "application/json"}
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/games", data=vbin, headers=headers)
		
		response = urlopen(request)
		self.assertEqual(response.getcode(), 201)
		#formatting response
		str_response = response.readall().decode("utf-8")
		obj_response = loads(str_response)

		actual_response = {'id' : 48}
		self.assertEqual(obj_response, actual_response)

	def test_API_post_teams_content(self) :
		values = dumps({
		    "team_name" : "Seahawks",
	        "team_city" : "Seattle",
	        "owner" : "Paul Allen",
	        "sb_appearances" : [40, 48],
	        "mvp_list" : ["Malcom Smith"]
		})
		headers = {"Content-Type": "application/json"}
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/teams", data=vbin, headers=headers)		
		
		response = urlopen(request)
		self.assertEqual(response.getcode(), 201)
		self.assertNotEqual(response.getcode(), 204)
		#formatting response
		str_response = response.readall().decode("utf-8")
		obj_response = loads(str_response)

		actual_response = {'id' : 1}
		self.assertEqual(obj_response, actual_response)
	

	def test_API_post_players_content(self) :
		values = dumps({
		   	"first_name" : "Peyton",
	        "last_name" : "Manning",
	        "teams" : ["Indianapolis Colts", "Denver Broncos"],
	        "sb_appearances" : [41, 44, 48],
	        "birth_date" : "1976-03-24",
	        "birth_town" : "New Orleans, LA",
	        "high_school" : "New Orleans Newman",
	        "college" : "University of Tennessee",
	        "draft_year" : 1998,
	        "retired" : false
		})
		headers = {"Content-Type": "application/json"}	
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/players", data=vbin, headers=headers)		
		
		response = urlopen(request)
		self.assertEqual(response.getcode(), 201)
		#formatting response
		str_response = response.readall().decode("utf-8")
		obj_response = loads(str_response)

		actual_response = {'id' : 1}
		self.assertEqual(obj_response, actual_response)

		actual_response = {'id' : 2}
		self.assertNotEqual(obj_response, actual_response)


	# -----------------------
	# put
	# -----------------------
	# check status codes only
	# -----------------------


	def test_API_put_game_response(self) :
		values = dumps({
		    "winning_team" : "Seattle Seahawks",
	        "losing_team" : "Denver Broncos",
	        "mvp" : "Malcom Smith",
	        "winning_score" : 48,
	        "losing_score" : 3,
	        "venue" : "MetLife Stadium",
	        "game_day" : "2014-02-14",
	        "game_number" : "XLVIII"
		})

		headers = {"Content-Type": "application/json"}
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/games/{id}", data=vbin, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		self.assertEqual(response.getcode(), 204)
		self.assertNotEqual(response.getcode(), 304)

	def test_API_put_team_response(self) :
		values = dumps({
		    "team_name" : "Seahawks",
	        "team_city" : "Seattle",
	        "owner" : "Paul Allen",
	        "sb_appearances" : [40, 48],
	        "mvp_list" : ["Malcom Smith"]
		})

		headers = {"Content-Type": "application/json"}
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/teams/{id}", data=vbin, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		self.assertEqual(response.getcode(), 204)

		request.get_method = lambda: 'GET'
		response = urlopen(request)
		self.assertNotEqual(response.getcode(), 204)


	def test_API_put_player_response(self) :
		values = dumps({
		    "first_name" : "Peyton",
	        "last_name" : "Manning",
	        "teams" : ["Indianapolis Colts", "Denver Broncos"],
	        "sb_appearances" : [41, 44, 48],
	        "birth_date" : "1976-03-24",
	        "birth_town" : "New Orleans, LA",
	        "high_school" : "New Orleans Newman",
	        "college" : "University of Tennessee",
	        "draft_year" : 1998,
	   	    "retired" : false
		})

		headers = {"Content-Type": "application/json"}
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/players/{id}", data=vbin, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		self.assertEqual(response.getcode(), 204)

print("IngloriousBashers-tests.py")

print("Done.")