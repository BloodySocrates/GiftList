import json

class Recipient:
	def __init__(self, name):
		self.name=name
		self.gift_list={}
		self.load()

	def total(self):
		costs=[]
		for value in self.gift_list.values():
			costs.append(value)
		print(f'You have spent ${sum(costs)} on {self.name} so far.')

	def add_gift(self, item, amount):
		self.gift_list[item]=amount

	def save(self):
		filename=f'{self.name}.json'
		with open(filename, 'w') as f:
			json.dump(self.gift_list, f, indent=1)

	def load(self):
		filename=f'{self.name}.json'
		try: #if recipient has no prior data, breaks from load function
			with open(filename) as f:
				self.gift_list=json.load(f)
		except:FileNotFoundError
		else:
			print('New recipient created')

	def show(self):
		print(f'You have purchased {self.gift_list} for {self.name}.')
	
	def __str__(self):
		pass


