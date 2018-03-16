#ch11测试
def city_fun(city, country, population = 0):
	if population > 0:
		rs = city+", "+country+"-population "+str(population)
	else:
		rs=city+", "+country
	return rs
	
class AnnoySurvey():
	"""匿名调查问卷"""
	def __init__(self, question):
		self.question = question
		self.responses = []
		
	def show_question(self):
		print(slef.question)
		
	def store_question(self, new_response):
		self.responses.append(new_response)
		
	def shwo_re(self):
		for i in self.responses:
			print('--'+i)