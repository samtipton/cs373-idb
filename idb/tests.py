from django.test import TestCase, Client
from urllib.request import urlopen, Request
from json import dumps, loads
from idb.models import MVP, Franchise, SuperBowl
import types
from django.db.models import Q

# ----------------------
# RESTful API Unit Tests
# Inglorious Bashers
# ----------------------

def merge(*dicts):
	"""
	This is a helper function to merge multiple dictionaries and return
	a new merged dictionary.
	"""
	result = {}
	for d in dicts:
		result.update(d)
	return result

class test_API(TestCase) :

	def assert_successful_response(self, api_response):
		"""
		This is a helper function to assert a successful response from the
		API. Additionally, it returns the payload of the API operation.
		"""
		self.assertTrue(type(api_response) is dict)
		self.assertTrue("success" in api_response)
		self.assertTrue(api_response["success"])
		self.assertTrue("data" in api_response)
		return api_response["data"]

	def assert_failure_response(self, api_response, error_type, error_message):
		"""
		This is a helper function to asser that an API operation failed and
		that it failed with the expected error response.
		"""
		self.assertTrue(type(api_response) is dict)
		self.assertTrue("success" in api_response)
		self.assertFalse(api_response["success"])
		self.assertTrue("error" in api_response)
		self.assertTrue(type(api_response["error"] is dict))
		self.assertTrue("type" in api_response["error"])
		self.assertEqual(api_response["error"]["type"], error_type)
		self.assertTrue("message" in api_response["error"])
		self.assertEqual(api_response["error"]["message"], error_message)

	def path(self, _type = "", id = None):
		"""
		This is a helper function to compute the url to an API operation.
		"""
		p = "/api/v2/" + str(_type)
		if id is not None:
			p += "/" + str(id)
		return p

	def ref(self, model):
		"""
		This is a helper function to generate the API urls for a specific
		model instance.
		"""
		_type = str(type(model).__name__).lower() + "s"
		return {
			"id": model.id,
			"self": self.path(_type, model.id),
			"collection": self.path(_type)
		}
	
	def serialize_superbowl_model(self, model):
		return merge(self.ref(model), {
		    "winning_franchise": self.ref(model.winning_franchise),
		    "losing_franchise": self.ref(model.winning_franchise),
		    "mvp": self.ref(model.winning_franchise),
		    "mvp_stats": model.mvp_stats,
		    "mvp_blurb": model.mvp_blurb,
		    "winning_score": model.winning_score,
		    "losing_score": model.losing_score,
		    "venue_name": model.venue_name,
		    "venue_city": model.venue_city,
		    "venue_state": model.venue_state,
		    "game_day": str(model.game_day),
		    "attendance": model.attendance,
		    "game_number": model.game_number,
		    "halftime_performer": model.halftime_performer,
		    "twitter_id": model.twitter_id,
		    "youtube_id": model.youtube_id,
		    "latitude": model.latitude,
		    "longitude": model.longitude
		})
	
	def serialize_franchise_model(self, model):
		return merge(self.ref(model), {
		    "mvps": [self.ref(m) for m in model.mvps.all()],
			"superbowls": [self.ref(m) for m in ...],
		    "team_name": ,
			"team_city": "Seattle",
			"team_state": "WA",
			"current_owner": "Paul Allen",
			"current_gm": "John Schneider",
			"current_head_coach": "Pete Carroll",
			"year_founded": 1974,
			"active": true,
			"home_stadium": "CenturyLink Field",
			"division": "NFC West",
			"facebook_id": "seahawks",
			"twitter_id": "GoHawks",
			"youtube_id": "vh500h",
			"latitude": 334.6,
			"longitude": 44.1
		})
	
	
	
	# ----------------------------------------------------
	# Helper functions to make REST calls against the API.
	# ----------------------------------------------------
	
	def get(self, _type = "", id = None):
		url = path(_type, id)
		response = self.client.get(url)
		api_response = loads(response.content)
		return (response.status_code, api_response)

	def post(self, _type, request):
		url = path(_type)
		response = self.client.post(url, request, 'application/json');
		api_response = loads(response.content)
		return (response.status_code, api_response)

	def put(self, _type, id, request):
		url = path(_type, id)
		response = self.client.put(url, request, 'application/json');
		api_response = loads(response.content)
		return (response.status_code, api_response)

	def delete(self, _type):
		url = path(_type, id)
		response = self.client.get(url)
		api_response = loads(response.content)
		return (response.status_code, api_response)
	
	# ----------
	# Unit Tests
	# ----------
	
	def setUp(self) :
		# Initialize the database for testing.
		self.malcolm_smith = MVP.objects.create(first_name='Malcolm', last_name='Smith', position='OLB', birth_date='1989-07-05', birth_town='Woodland Hills, CA', high_school='Woodland Hills (CA) Taft', college='Southern California', draft_year=2011, active=True, salary=465000, facebook_id='MalcSmitty', twitter_id='MalcSmitty', youtube_id='zfB8hCsHwLE', latitude=34.1683, longitude=-118.6050)
		self.seahawks = Franchise.objects.create(team_name='Seahawks', team_city='Seattle', team_state='WA', current_owner='Paul Allen', current_gm='John Schneider', current_head_coach='Pete Carroll', year_founded=1974, active=True, home_stadium='CenturyLink Field', division='NFC West', facebook_id='Seahawks', twitter_id='Seahawks', youtube_id='l9-NicPH-58', latitude=47.5953, longitude=-122.3317)
		self.broncos = Franchise.objects.create(team_name='Broncos', team_city='Denver', team_state='CO', current_owner='Pat Bowlen', current_gm='John Elway', current_head_coach='John Fox', year_founded=1960, active=True, home_stadium='Sports Authority Field', division='AFC West', facebook_id='DenverBroncos', twitter_id='Broncos', youtube_id='HGMbmbnu2Oc', latitude=39.7439, longitude=-105.0200)
		self.seahawks.mvps.add(self.malcolm_smith)
		self.sb_48 = SuperBowl.objects.create(winning_franchise=self.seahawks, losing_franchise=self.broncos, mvp=self.malcolm_smith, mvp_stats='1 INT 1 FR 1 TD 9 T', mvp_blurb='Malcolm Smith was the de-facto SB MVP for a legendary Seattle defense.\n\nWhile he was a relative unknown at the start of the season, a game-sealing interception in the NFC Championship as well as two takeaways in the Super Bowl served as a coming out party for the young linebacker.', winning_score=43, losing_score=8, venue_name='MetLife Stadium', venue_city='East Rutherford', venue_state='NJ', game_day='2014-02-02', attendance=82529, game_number='XLVIII', halftime_performer='Bruno Mars', twitter_id='SuperBowlXLVIII', youtube_id='NbcA1UISfG0', latitude=40.8136, longitude=-74.0744)
		self.client = Client()


























	def test_get_superbowls(self) :
		response = self.client.get('/api/v2/superbowls')
		self.assertEqual(response.status_code, 200)
		api_response = loads(response.content)

		expected_response = [
			merge(ref(self.sb_48),
			{
				"winning_franchise": ref(self.seahawks),
		        "losing_franchise": ref(self.broncos),
		        "mvp": ref(self.malcolm_smith),
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
		]

		self.assert_successful_response(api_response, expected_response)

	def test_post_superbowls(self) :

		response = self.client.post('/api/v2/superbowls',content_type='application/json', data=dumps(request));
		self.assertEqual(response.status_code, 201)
		api_response = loads(response.content)

		expected_response = ref(self.sb_48)

		self.assert_successful_response(api_response, expected_response)




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
