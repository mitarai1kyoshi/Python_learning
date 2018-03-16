#类
class Restaurant():
	
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.price = 30
		
	def describe(self):
		print(self.name + " is " + self.type)
		
	def open(self):
		print(self.name + " is opening.")
		
	def update_price(self, price):
		if(price > 0):
			self.price = price
		else:
			print("you cannot change price to a negative value")
res = Restaurant('sjdk','chinese food')
res.open()
print(str(res.price))
res.update_price(-5)
print(str(res.price))


class Food():
	def __init__(self, foodname="sushi"):
		self.foodname = foodname
	def p(self):
		print(self.foodname)
		
		
class NewRestaurant(Restaurant):
	def __init__(self, name, type, year):
		super().__init__(name, type)
		self.year = year
		self.food = Food("dfh")
new = NewRestaurant('sjdk','chinese food',2016)
new.food.p()


from random import randint

class Die():
	def __init__(self, sides = 6):
		self.sides = sides
	
	def roll_die(self):
		print(randint(1,self.sides))
mydie = Die(10)
for i in range(1,10):
	mydie.roll_die()
