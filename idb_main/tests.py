from django.test import TestCase
from urllib.request import urlopen, Request
from json import dumps



class test_API(TestCase) :

	# ---
	# get
	# ---
	def test_API_get_game_response(self) :
		request = Request("http://idb.apiary.io/api/games")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)
		
	def test_API_get_game_content(self) :
		pass
	# 	request = Request("http://idb.apiary.io/api/games")
	# 	response_body = urlopen(request).read()
	# 	s = "[\n\t{\n\t    \"home_team\" : [1],\n\t    \"away_team\" : [1],\n\t    \"home_score\" : 48,\n\t    \"away_score\" : 3,\n\t    \"venue\" : [0],\n\t    \"game_day\" : \"2014-2-14\",\n\t    \"game_number\" : \"XLVIII\"\n\t}\n]"
	# 	print (s)
	# 	print(response_body)
	# 	self.assertTrue(s == response_body)

	def test_API_get_teams_response(self) :
		request =  Request("http://idb.apiary.io/api/teams")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

	def test_API_get_teams_content(self) :
		pass

	def test_API_get_players_response(self) :
		request =  Request("http://idb.apiary.io/api/players")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

	def test_API_get_players_content(self) :
		pass

	def test_API_get_single_game_response(self) :
		request =  Request("http://idb.apiary.io/api/games/{id}")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

	def test_API_get_single_game_content(self) :
		pass

	def test_API_get_single_team_response(self) :
		request =  Request("http://idb.apiary.io/api/teams/{id}")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

	def test_API_get_single_team_content(self) :
		pass

	def test_API_get_single_player_response(self) :
		request =  Request("http://idb.apiary.io/api/players/{id}")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)
	
	def test_API_get_single_player_content(self) :
		pass

	# ------
	# delete
	# ------
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

	# ----
	# post
	# ----

	def test_API_post_games_response(self) :
		values = dumps({
		    "home_team" : [1],
		    "away_team" : [1],
		    "home_score" : 48,
		    "away_score" : 3,
		    "venue" : [0],
		    "game_day" : "2014-2-14",
		    "game_number" : "XLVIII"
		})
		headers = {"Content-Type": "application/json"}

		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/games", data=vbin, headers=headers)
		response = urlopen(request)
		self.assertEqual(response.getcode(), 201)

	def test_API_post_games_content(self) :
		pass

	def test_API_post_teams_response(self) :
		values = dumps({
		    "team_name" : "Seahawks",
		    "team_city" : "Seatle",
		    "owner" : "Paul Allen"
		})
		headers = {"Content-Type": "application/json"}
		
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/teams", data=vbin, headers=headers)		
		response = urlopen(request)
		self.assertEqual(response.getcode(), 201)

	def test_API_post_teams_content(self) :
		pass

	def test_API_post_players_response(self) :
		values = dumps({
		    "first_name" : "Peyton",
		    "last_name" : "Manning",
		    "birth_date" : "1976-03-24",
		    "birth_town" : "New Orleans, LA",
		    "high_school" : "New Orleans Newman",
		    "college" : "University of Tennessee"
		})
		headers = {"Content-Type": "application/json"}
		
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/players", data=vbin, headers=headers)		
		response = urlopen(request)
		self.assertEqual(response.getcode(), 201)

	def test_API_post_players_content(self) :
		pass

	# --- 
	# put
	# ---

	def test_API_put_game_response(self) :
		values = dumps({
		    "home_team" : [1],
		    "away_team" : [1],
		    "home_score" : 48,
		    "away_score" : 3,
		    "venue" : [0],
		    "game_day" : "2014-2-14",
		    "game_number" : "XLX"
		})
		headers = {"Content-Type": "application/json"}
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/games/{id}", data=vbin, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		self.assertEqual(response.getcode(), 204)

	def test_API_put_team_response(self) :
		values = dumps({
		    "team_name" : "Seahawks",
		    "team_city" : "Seatle",
		    "owner" : "Paul Allen"
		})
		headers = {"Content-Type": "application/json"}
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/teams/{id}", data=vbin, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		self.assertEqual(response.getcode(), 204)


	def test_API_put_player_response(self) :
		values = dumps({
		    "first_name" : "Peyton",
		    "last_name" : "Manning",
		    "birth_date" : "1976-03-24",
		    "birth_town" : "New Orleans, LA",
		    "high_school" : "New Orleans Newman",
		    "college" : "The University of Tennessee"
		})
		headers = {"Content-Type": "application/json"}
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/players/{id}", data=vbin, headers=headers)
		request.get_method = lambda: 'PUT'
		response = urlopen(request)
		self.assertEqual(response.getcode(), 204)