#测试
import unittest
from ch11_test import city_fun

class test_city(unittest.TestCase):
	def test_cities(self):
		rs = city_fun('Santiago', 'Chile')
		self.assertEqual(rs, 'Santiago, Chile')
		
	def test_cities_popu(self):
		rs = city_fun('Santiago', 'Chile', 500000)
		self.assertEqual(rs, 'Santiago, Chile-population 500000')
	

from ch11_test import AnnoySurvey
class TestAnnoySurvey(unittest.TestCase):
	
	def setUp(self):
		"""
		创建一个调查对象和一组答案
		"""
		question = "language? "
		self.mysurvey = AnnoySurvey(question)
		self.responses = ['English','Chinese','Japanese']
		
	def test_single(self):
		self.mysurvey.store_question(self.responses[0])
		self.assertIn(self.responses[0],self.mysurvey.responses)
		
	def test_three(self):
		for r in self.responses:
			self.mysurvey.store_question(r)
			self.assertIn(r,self.mysurvey.responses)
	
unittest.main()
