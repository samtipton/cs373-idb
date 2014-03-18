from django.test import TestCase
from urllib.request import urlopen, Request
from json import dumps

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

	def test_API_get_game_response(self) :
		request = Request("http://idb.apiary.io/api/games")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)
		
	def test_API_get_game_content(self) :
		response = urlopen("http://idb.apiary.io/api/games")
		response_content_list =[]
		actual_response_list = ['[', '        {',
						 '            \"home_team\" : [1],',
						  '            \"away_team\" : [1],',
						  '            \"home_score\" : 48,',
						  '            \"away_score\" : 3,',
						  '            \"venue\" : [0],',
						  '            \"game_day\" : \"2014-2-14\",',
						  '            \"game_number\" : \"XLVIII\"',
						  '        }', ']']
		
		for line in response:
			#formatting each line in response
			strip_string = str(line.rstrip())
			format_string = strip_string[2 : len(strip_string) - 1]
			response_content_list.append(format_string)

		self.assertTrue(actual_response_list == response_content_list)


	def test_API_get_teams_response(self) :
		request =  Request("http://idb.apiary.io/api/teams")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

	def test_API_get_teams_content(self) :
		response = urlopen("http://idb.apiary.io/api/teams")
		response_content_list =[]
		actual_response_list = ['[', '        {',
						 '            \"team_name\" : \"Seahawks\",',
						  '            \"team_city\" : \"Seattle\",',
						  '            \"owner\" : \"Paul Allen\"',
						  '        }', ']']
		
		for line in response:
			#formatting each line in response
			strip_string = str(line.rstrip())
			format_string = strip_string[2 : len(strip_string) - 1]
			response_content_list.append(format_string)

		self.assertTrue(actual_response_list == response_content_list)

	def test_API_get_players_response(self) :
		request =  Request("http://idb.apiary.io/api/players")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

	def test_API_get_players_content(self) :
		response = urlopen("http://idb.apiary.io/api/players")
		response_content_list =[]
		actual_response_list = ['[', '        {',
						 '            \"first_name\" : \"Peyton\",',
						  '            \"last_name\" : \"Manning\",',
						  '            \"birth_date\" : \"1976-03-24\",',
						  '            \"birth_town\" : \"New Orleans, LA\",',
						  '            \"high_school\" : \"New Orleans Newman\",',
						  '            \"college\" : \"University of Tennessee\"',
						  '        }', ']']
		
		
		for line in response:
			#formatting each line in response
			strip_string = str(line.rstrip())
			format_string = strip_string[2 : len(strip_string) - 1]
			response_content_list.append(format_string)

		self.assertTrue(actual_response_list == response_content_list)

	def test_API_get_single_game_response(self) :
		request =  Request("http://idb.apiary.io/api/games/{id}")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

	def test_API_get_single_game_content(self) :
		response = urlopen("http://idb.apiary.io/api/games/{id}")
		response_content_list =[]
		actual_response_list = ['{',
						 '    \"home_team\" : [1],',
						  '    \"away_team\" : [1],',
						  '    \"home_score\" : 48,',
						  '    \"away_score\" : 3,',
						  '    \"venue\" : [0],',
						  '    \"game_day\" : \"2014-2-14\",',
						  '    \"game_number\" : \"XLVIII\"',
						  '}']


		for line in response:
			#formatting each line in response
			strip_string = str(line.rstrip())
			format_string = strip_string[2 : len(strip_string) - 1]
			response_content_list.append(format_string)

		self.assertTrue(actual_response_list == response_content_list)

	def test_API_get_single_team_response(self) :
		request =  Request("http://idb.apiary.io/api/teams/{id}")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)

	def test_API_get_single_team_content(self) :
		response = urlopen("http://idb.apiary.io/api/teams/{id}")
		response_content_list =[]
		
		actual_response_list = ['{',
						 '    \"team_name\" : \"Seahawks\",',
						  '    \"team_city\" : \"Seattle\",',
						  '    \"owner\" : \"Paul Allen\"',
						  '}']
		
		for line in response:
			#formatting each line in response
			strip_string = str(line.rstrip())
			format_string = strip_string[2 : len(strip_string) - 1]
			response_content_list.append(format_string)

		self.assertTrue(actual_response_list == response_content_list)

	def test_API_get_single_player_response(self) :
		request =  Request("http://idb.apiary.io/api/players/{id}")
		response = urlopen(request)
		self.assertEqual(response.getcode(), 200)
	
	def test_API_get_single_player_content(self) :
		response = urlopen("http://idb.apiary.io/api/players/{id}")
		response_content_list =[]
		actual_response_list = ['{',
						 '    \"first_name\" : \"Peyton\",',
						  '    \"last_name\" : \"Manning\",',
						  '    \"birth_date\" : \"1976-03-24\",',
						  '    \"birth_town\" : \"New Orleans, LA\",',
						  '    \"high_school\" : \"New Orleans Newman\",',
						  '    \"college\" : \"University of Tennessee\"',
						  '}']
		
		
		for line in response:
			#formatting each line in response
			strip_string = str(line.rstrip())
			format_string = strip_string[2 : len(strip_string) - 1]
			response_content_list.append(format_string)

		self.assertTrue(actual_response_list == response_content_list)

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

	# -----------------------------------------
	# post
	# -----------------------------------------
	# check status codes and content is correct
	# ----------------------------------------- 

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
		
		#formatting response
		response = str(urlopen(request).read())
		response = response[2: len(response) - 1]

		actual_response = "{\"id\" : 1}"
		self.assertEqual(response, actual_response)


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
		values = dumps({
		    "team_name" : "Seahawks",
		    "team_city" : "Seatle",
		    "owner" : "Paul Allen"
		})
		headers = {"Content-Type": "application/json"}
		vbin = values.encode("utf-8")
		request = Request("http://idb.apiary.io/api/teams", data=vbin, headers=headers)		
		
		#formatting response
		response = str(urlopen(request).read())
		response = response[2: len(response) - 1]

		actual_response = "{\"id\" : 1}"
		self.assertEqual(response, actual_response)
	

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
		
		#formatting response
		response = str(urlopen(request).read())
		response = response[2: len(response) - 1]

		actual_response = "{\"id\" : 1}"
		self.assertEqual(response, actual_response)


	# -----------------------
	# put
	# -----------------------
	# check status codes only
	# -----------------------


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