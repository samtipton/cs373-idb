from django.test import TestCase, Client
from urllib.request import urlopen, Request
from json import dumps, loads
from idb.models import MVP, Franchise, SuperBowl
import types
from django.db.models import Q
from idb.helpers import *

# ----------------------
# RESTful API Unit Tests
# Inglorious Bashers
# ----------------------

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
	
	# ----------------------------------------------------
	# Helper functions to make REST calls against the API.
	# ----------------------------------------------------
	
	def get(self, _type = "", id = None):
		url = make_path(_type, id)
		response = self.client.get(url)
		api_response = loads(response.content.decode('utf-8'))
		return (response.status_code, api_response)

	def post(self, _type, body):
		url = make_path(_type)
		response = self.client.post(url, dumps(body), 'application/json');
		api_response = loads(response.content.decode('utf-8'))
		return (response.status_code, api_response)

	def put(self, _type, id, body):
		url = make_path(_type, id)
		response = self.client.put(url, dumps(body), 'application/json');
		api_response = loads(response.content.decode('utf-8'))
		return (response.status_code, api_response)

	def delete(self, _type, id):
		url = make_path(_type, id)
		response = self.client.delete(url)
		api_response = loads(response.content.decode('utf-8'))
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
		self.sb_to_delete = SuperBowl.objects.create(winning_franchise=self.seahawks, losing_franchise=self.broncos, mvp=self.malcolm_smith, mvp_stats='1 INT 3 FR 1 TD 9 T', mvp_blurb='Malcolm Smith was the de-facto SB MVP for a legendary Seattle defense.\n\nWhile he was a relative unknown at the start of the season, a game-sealing interception in the NFC Championship as well as two takeaways in the Super Bowl served as a coming out party for the young linebacker.', winning_score=43, losing_score=8, venue_name='MetLife Stadium', venue_city='East Rutherford', venue_state='NJ', game_day='2014-02-02', attendance=82529, game_number='XLVIII', halftime_performer='Bruno Mars', twitter_id='SuperBowlXLVIII', youtube_id='NbcA1UISfG0', latitude=40.8136, longitude=-74.0744)
		self.sb_49 = SuperBowl.objects.create(winning_franchise=self.broncos, losing_franchise=self.seahawks, mvp=self.malcolm_smith, mvp_stats='1 INT 1 FR 1 TD 9 T', mvp_blurb='Malcolm Smith was the de-facto SB MVP for a legendary Seattle defense.\n\nWhile he was a relative unknown at the start of the season, a game-sealing interception in the NFC Championship as well as two takeaways in the Super Bowl served as a coming out party for the young linebacker.', winning_score=43, losing_score=8, venue_name='MetLife Stadium', venue_city='East Rutherford', venue_state='NJ', game_day='2014-02-02', attendance=82529, game_number='XLVIII', halftime_performer='Bruno Mars', twitter_id='SuperBowlXLVIII', youtube_id='NbcA1UISfG0', latitude=40.8136, longitude=-74.0744)
		self.client = Client()

	# --------------------
	# API SUPERBOWLS TESTS
	# --------------------

	def test_API_get_superbowls(self) :
		(code, response) = self.get("superbowls")
		self.assertEqual(code, 200)
		body = [serialize_superbowl_model(self.sb_48), serialize_superbowl_model(self.sb_to_delete), serialize_superbowl_model(self.sb_49)]
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)

	def test_API_get_superbowls_id(self):
		sb_id = self.sb_48.id
		(code, response) = self.get("superbowls", sb_id)
		self.assertEqual(code, 200)
		body = serialize_superbowl_model(self.sb_48)
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)

	def test_API_post_superbowls(self):
		request = {
		 "winning_franchise": {
			"id": self.broncos.id 
		  },
		  "losing_franchise": {
			"id" : self.seahawks.id
		  },
		  "mvp": {
		    "id": self.malcolm_smith.id
		  },
		  "mvp_stats":'1 INT 1 FR 1 TD 9 T', 
		  "mvp_blurb":'Malcolm Smith was the de-facto SB MVP for a legendary Seattle defense.\n\nWhile he was a relative unknown at the start of the season, a game-sealing interception in the NFC Championship as well as two takeaways in the Super Bowl served as a coming out party for the young linebacker.', 
		  "winning_score":43, 
		  "losing_score":8, 
		  "venue_name":'MetLife Stadium', 
		  "venue_city":'East Rutherford', 
		  "venue_state":'NJ', 
		  "game_day":'2014-02-02', 
		  "attendance":82529, 
		  "game_number":'XLVIII', 
		  "halftime_performer":'Bruno Mars', 
		  "twitter_id":'SuperBowlXLVIII', 
		  "youtube_id":'NbcA1UISfG0', 
		  "latitude":40.8136, 
		  "longitude":-74.0744
		}
		(code, response) = self.post("superbowls", request)
		self.assertEqual(code, 201)
		body = {
        "id" : 4,
        "self": make_path("superbowls", 4),
        "collection": make_path("superbowls")
        }
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)
		sb_id = response['data']['id']
		sb = SuperBowl.objects.get(pk=sb_id)
		self.assertEqual(sb.winning_franchise.id, self.broncos.id)
		self.assertEqual(sb.losing_franchise.id, self.seahawks.id)
		self.assertEqual(sb.mvp.id, self.malcolm_smith.id)
		self.assertEqual(sb.mvp_stats, '1 INT 1 FR 1 TD 9 T')

	def test_API_put_superbowls(self):
		request = {
		 "winning_franchise": {
			"id": self.broncos.id 
		  },
		  "losing_franchise": {
			"id" : self.seahawks.id
		  },
		  "mvp": {
		    "id": self.malcolm_smith.id
		  },
		  "mvp_stats":'1 INT 1 FR 4 TD 9 T', 
		  "mvp_blurb":'Malcolm Smith was the de-facto SB MVP for a legendary Seattle defense.\n\nWhile he was a relative unknown at the start of the season, a game-sealing interception in the NFC Championship as well as two takeaways in the Super Bowl served as a coming out party for the young linebacker.', 
		  "winning_score":43, 
		  "losing_score":8, 
		  "venue_name":'MetLife Stadium', 
		  "venue_city":'East Rutherford', 
		  "venue_state":'NJ', 
		  "game_day":'2014-02-02', 
		  "attendance":82529, 
		  "game_number":'XLVIII', 
		  "halftime_performer":'Bruno Mars', 
		  "twitter_id":'SuperBowlXLVIII', 
		  "youtube_id":'NbcA1UISfG0', 
		  "latitude":40.8136, 
		  "longitude":-74.0744
		}
		(code, response) = self.put("superbowls", 1, request)
		self.assertEqual(code, 200)
		body = {
        "id": 1,
        "self": "/api/v2/superbowls/1",
        "collection": "/api/v2/superbowls",
        "winning_franchise":
        {
            "id": self.broncos.id,
            "self": "/api/v2/franchises/2",
            "collection": "/api/v2/franchises"
        },
        "losing_franchise":
        {
            "id": self.seahawks.id,
            "self": "/api/v2/franchises/1",
            "collection": "/api/v2/franchises"
        },
        "mvp":
        {
            "id": self.malcolm_smith.id,
            "self": "/api/v2/mvps/1",
            "collection": "/api/v2/mvps"
        },
        "mvp_stats":'1 INT 1 FR 4 TD 9 T', 
		  "mvp_blurb":'Malcolm Smith was the de-facto SB MVP for a legendary Seattle defense.\n\nWhile he was a relative unknown at the start of the season, a game-sealing interception in the NFC Championship as well as two takeaways in the Super Bowl served as a coming out party for the young linebacker.', 
		  "winning_score":43, 
		  "losing_score":8, 
		  "venue_name":'MetLife Stadium', 
		  "venue_city":'East Rutherford', 
		  "venue_state":'NJ', 
		  "game_day":'2014-02-02', 
		  "attendance":82529, 
		  "game_number":'XLVIII', 
		  "halftime_performer":'Bruno Mars', 
		  "twitter_id":'SuperBowlXLVIII', 
		  "youtube_id":'NbcA1UISfG0', 
		  "latitude":40.8136, 
		  "longitude":-74.0744
		}
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)

		sb_id = response['data']['id']
		sb = SuperBowl.objects.get(pk=sb_id)
		self.assertEqual(sb.mvp_stats, '1 INT 1 FR 4 TD 9 T')

	def test_API_superbowls_delete(self):
		sb_id = self.sb_to_delete.id
		(code, response) = self.delete("superbowls", sb_id)
		self.assertEqual(code, 200)
		body = None
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)

	# --------------------
	# API FRANCHISES TESTS
	# --------------------

	def test_API_get_franchises(self) :
		(code, response) = self.get("franchises")
		self.assertEqual(code, 200)
		body = [serialize_franchise_model(self.seahawks), serialize_franchise_model(self.broncos)]
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)

	def test_API_get_franchises_id(self):
		f_id = self.seahawks.id
		(code, response) = self.get("franchises", f_id)
		self.assertEqual(code, 200)
		body = serialize_franchise_model(self.seahawks)
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)

	def test_API_post_franchises(self):
		request = {
		  "mvps": [{
		    "id": self.malcolm_smith.id,
		  }],
		  "superbowls_won" : [{
		  	"id": self.sb_48.id,
          }],
		  "superbowls_lost" : [{
            "id": self.sb_49.id,
		  }],
		  "team_name": "Seahawks",
	      "team_city": "Oklahoma",
	      "team_state": "WA",
	      "current_owner": "Paul Allen",
	      "current_gm": "John Schneider",
	      "current_head_coach": "Pete Carroll",
	      "year_founded": 1974,
	      "active": True,
	      "home_stadium": "CenturyLink Field",
	      "division": "NFC West",
	      "facebook_id": "seahawks",
	      "twitter_id": "GoHawks",
	      "youtube_id": "vh500h",
	      "latitude": 334.6,
	      "longitude": 44.1
		}
		(code, response) = self.post("franchises", request)
		self.assertEqual(code, 201)
		body = {
        "id" : 3,
        "self": make_path("franchises", 3),
        "collection": make_path("franchises")
        }
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)
		f_id = response['data']['id']
		f = Franchise.objects.get(pk=f_id)
		
		self.assertEqual(f.team_city, 'Oklahoma')

	def test_API_put_franchises(self):
		f_id = self.seahawks.id
		request = {
		  "mvps":
		  [{
		      "id": self.malcolm_smith.id,
		  }],
		  "superbowls_won":
		  [{
		      "id": self.sb_48.id,
		  }],
		  "superbowls_lost":
		  [{
		      "id": self.sb_49.id,
		  }],
		  "team_name": "Seahawks",
		  "team_city": "Seattle",
		  "team_state": "WA",
		  "current_owner": "George Allen",
	      "current_gm": "John Schneider",
		  "current_head_coach": "Pete Carroll",
		  "year_founded": 1974,
		  "active": True,
		  "home_stadium": "CenturyLink Field",
		  "division": "NFC West",
		  "facebook_id": "seahawks",
		  "twitter_id": "GoHawks",
		  "youtube_id": "vh500h",
		  "latitude": 334.6,
		  "longitude": 44.1
		}
		(code, response) = self.put("franchises", f_id, request)
		self.assertEqual(code, 200)
		body = {
        "id": f_id,
        "self": "/api/v2/franchises/1",
        "collection": "/api/v2/franchises",
        "mvps":
        [{
            "id": self.malcolm_smith.id,
            "self": "/api/v2/mvps/1",
            "collection": "/api/v2/mvps"
        }],
        "superbowls_won":
        [{
            "id": self.sb_48.id,
            "self": "/api/v2/superbowls/1",
            "collection": "/api/v2/superbowls"
        }, {
			"id" : self.sb_to_delete.id,
			"self": "/api/v2/superbowls/2",
            "collection": "/api/v2/superbowls"       
        }],
        "superbowls_lost":
        [{
            "id": self.sb_49.id,
            "self": "/api/v2/superbowls/3",
            "collection": "/api/v2/superbowls"
        }],
        "team_name": "Seahawks",
        "team_city": "Seattle",
        "team_state": "WA",
        "current_owner": "George Allen",
        "current_gm": "John Schneider",
        "current_head_coach": "Pete Carroll",
        "year_founded": 1974,
        "active": True,
        "home_stadium": "CenturyLink Field",
        "division": "NFC West",
        "facebook_id": "seahawks",
        "twitter_id": "GoHawks",
        "youtube_id": "vh500h",
        "latitude": 334.6,
        "longitude": 44.1
		}
		expected_response = make_successful_response_object(body)
		
		self.assertEqual(response, expected_response)

		f_id = response['data']['id']
		f = Franchise.objects.get(pk=f_id)
		self.assertEqual(f.current_owner, 'George Allen')

	def test_API_delete_franchises(self):
		f_id = self.broncos.id
		(code, response) = self.delete("franchises", f_id)
		self.assertEqual(code, 200)
		body = None
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)


	# --------------------
	# API FRANCHISES TESTS
	# --------------------

	def test_API_get_mvps(self) :
		(code, response) = self.get("mvps")
		self.assertEqual(code, 200)
		body = [serialize_mvp_model(self.malcolm_smith)]
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)
	
	def test_API_get_mvps_id(self) :
		p_id = self.malcolm_smith.id
		(code, response) = self.get("mvps", p_id)
		self.assertEqual(code, 200)
		body = serialize_mvp_model(self.malcolm_smith)
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)

	def test_API_post_mvps(self) :
		request = {
		  "superbowls": [{
		  	"id" : self.sb_48.id
		  }, {
		  	"id" : self.sb_49.id
		  }],
		  "franchises" :
		  [{
		  	"id" : self.seahawks.id
		  }],
		  "first_name": "Malcolm",
	    "last_name": "Jones",
	    "position": "LB",
	    "birth_date": "1989-07-05",
	    "birth_town": "Woodland Hills, CA",
	    "high_school": "Woodland Hills (CA) Taft",
	    "college": "Southern California",
	    "draft_year": 2011,
	    "active": True,
	    "salary": 465000,
	    "facebook_id": "MalcomFanPage",
	    "twitter_id": "MalcomTweets",
	    "youtube_id": "ghwhh09",
	    "latitude": 100.5,
	    "longitude": 37.6
		}
		(code, response) = self.post("mvps", request)
		self.assertEqual(code, 201)
		body = {
		"id" : 2,
		"self" : make_path("mvps", 2),
		"collection" : make_path("mvps")
		}
		expected_response = make_successful_response_object(body)
		self.assertEqual(response, expected_response)
		p_id = response['data']['id']
		p = MVP.objects.get(pk=p_id)

		self.assertEqual(p.last_name, 'Jones')
		self.assertNotEqual(p.last_name, 'Smith')

	def test_API_put_mvps(self) :
		pass
	def test_API_delete_mvps(self) :
		pass

print("IngloriousBashers-tests.py")

print("Done.")
