import json
from recipient import Recipient
class GiftList:
	def __init__(self, name):
		self.name=name
		self.recipients=[]

	def save(self):
		pass #TODO format str function of recipient class to json serializable string
	#	filename=f'{self.name}.json'
	#	with open(filename, 'w') as f:
	#		json.dump(self.recipients, f)
		
	def load(self):
		filename=f'{self.name}.json'
		with open(filename) as f:
			self.recipients=json.load(f)

	def add_recipient(self, recipient):
		self.recipients.append(recipient)

	def total(self):
		pass
	
	def show(self):
		print(self.recipients)

	def __str__(self):
		pass

Lauren=Recipient('Lauren')
Dad=Recipient('Dad')
Dad.add_gift('whisky','?')
Dad.save()
#Lauren.load()
#Lauren.add_gift('necklace', 63)
#Lauren.save()
#Lauren.show()
#Lauren.total()
xmas = GiftList('xmas')
xmas.add_recipient(Lauren)
xmas.show()
#xmas.save()

