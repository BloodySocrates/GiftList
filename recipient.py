import json

class Recipient:
	'''class for single gift recipient.'''
	def __init__(self, name):
		self.name=name
		self.wish_list={}
		self.gift_list={}
		self.load()
		self.total=self.total()

#	def show_total(self):
#		costs=[]
#		for value in self.gift_list.values():
#			costs.append(int(value))
#		return f'You have spent ${sum(costs)} on {self.name} so far.'

	def total(self):
		costs=0
		for value in self.gift_list.values():
			costs+=(int(value))
		return costs

	def add_gift(self, item, amount):
		self.gift_list[item]=amount

	def add_wish(self, item):
		self.wish_list.append(item)

	def save(self):
		data={
		'gift_list': self.gift_list,
		'wish_list': self.wish_list
		}
		filename=f'{self.name}.json'
		with open(filename, 'w') as f:
			json.dump(data, f, indent=2)

	def load(self):
		filename=f'{self.name}.json'
		try: #if recipient has no prior data, breaks from load function
			with open(filename) as f:
				data=json.load(f)
				self.gift_list=data['gift_list']
				self.wish_list=data['wish_list']
		except:FileNotFoundError
		else:
			print('New recipient created')

	def show(self):
		print(f'Name: {self.name} \n Items bought: {self.gift_list} \n Total spent: {self.total} \n  wish list: {self.wish_list}')
	
	def __str__(self):
		return f'Name:{self.name}, Total: {self.total}'


