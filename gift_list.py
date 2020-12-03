import json
from recipient import Recipient
class GiftList:
	'''class that contains list of recipient objects, loads from json file, 
	takes one argument, name'''

	def __init__(self, name):
		self.name=name
		self.recipients=[]
		self.load()

	def save(self):
		jsondict={}
		filename=f'{self.name}.json'
		for rec in self.recipients:
			jsondict[f'{rec.name}']=f'{rec.gift_list}'
		with open(filename, 'w') as f:
			json.dump(jsondict, f, indent=2)
		
	def load(self):
		filename=f'{self.name}.json'
		with open(filename) as f:
			data=json.load(f)
			for person in data:
				person=Recipient(person)
				self.recipients.append(person)

	def add_recipient(self, recipient):
		self.recipients.append(recipient)

	def total(self):
		pass
	
	def show(self):
		for person in self.recipients:
			person.show()


class Interface:
	pass	


#Lauren=Recipient('Lauren')
#Dad=Recipient('Dad')
#Dad.add_gift('whisky','?')
#Dad.save()
#Lauren.load()
#Lauren.add_gift('necklace', 63)
#Lauren.save()
#Lauren.show()
#Lauren.total()
xmas = GiftList('xmas')
#xmas.add_recipient(Lauren)
#xmas.add_recipient(Dad)
#xmas.show()
#xmas.save()
#xmas.load()
