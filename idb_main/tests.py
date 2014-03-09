from django.test import TestCase
from urllib2 import urlopen



class test_API(TestCase) :

	def test_API_game(self) :
		
		response = urlopen("http://idb.apiary.io/games")
		self.assertEquals(response.getcode(), 200)


