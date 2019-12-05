class Fish:
	def __init__(self, name='Fish',hunger=0,happiness = 10):
		self.name = name
		self.hunger = hunger
		self.happiness = happiness
		# add 4 other data fields 

		self.hunger = self.hunger - 1
		self.happiness = self.happiness + 1 
		print(self.name + "has eaten, you hunger has decreased!")
		# what happens hunger and happiness when the fish eats?

	def swim(self):
		# what happens to hunger and happiness when the fist swims?
		self.hunger = self.hunger + 1 
		self.happiness = self.happiness + 1

	#what other things does the fish do besides eat and swim?
	fish = Fish("Love")
