import json
from recipient import Recipient
class GiftList:
	'''class that contains list of recipient objects, loads from json file, 
	takes one argument, name'''

	def __init__(self, name):
		self.name=name
		self.recipients=[]
		self.options=['[1]Add Recipient','[2]Add Gift','[3]Add Wish', '[4]Get total','[5]Display','[6]Total','[7]Quit']
		self.load()
		self.run()

	def run(self):
		run=True
		while run==True:
			print(self.options)
			choice=int((input("What would you like to do?")))
			if choice==1:
				self.add_recipient()
			elif choice==2:
				self.add_gift()
			elif choice==3:
				self.add_wish()
			elif choice==4:
				self.total()
			elif choice==5:
				self.display()
			elif choice==6:
				self.total()
			elif choice==7:
				run=False
			else:
				print("Invalid input")

	def save(self):
		jsonlist=[]
		for person in self.recipients:
			jsonlist.append(person.name)
		try:
			filename=f'{self.name}.json'	
			with open(filename, 'w') as f:
				json.dump(jsonlist, f)
		except: FileNotFoundError
		else: print('New gift list started.')

	def load(self):
		try:
			filename=f'{self.name}.json'
			with open(filename) as f:
				data=json.load(f)
				for rec in data:
					person=Recipient(rec)
					self.recipients.append(person)
		except:FileNotFoundError
		else:
			print('New gift list started')	

	def add_recipient(self):
		name=input('New recipient name?')
		recipient=Recipient(f'{name}')
		self.recipients.append(recipient)
		self.save()

	def add_gift(self):
		gift=input('What did you buy?')
		amount=input('How much did it cost?')
		for i in range(len(self.recipients)):
			print(i, end=' ')
			print(self.recipients[i].name)
		recipient=int(input('Who did you buy it for? (choose a number)'))
		self.recipients[recipient].add_gift(gift, amount)
		self.recipients[recipient].save()
		self.save()

	def add_wish(self):
		wish=input('What were you thinking of buying?')
		amount=input('How much did it cost?')
		for i in range(len(self.recipients)):
			print(i, end=' ')
			print(self.recipients[i].name)
		recipient=int(input('Who would you buy it for? (choose a number)'))
		self.recipients[recipient].add_wish(gift, amount)
		self.recipients[recipient].save()
		self.save()


	def total(self):
		totals=[]
		for recipient in self.recipients:
			total=(recipient.total)
			totals.append(total)
		return sum(totals)
	
	def display(self):
		for person in self.recipients:
			person.show()

	def __str__(self):
		people=[i.name for i in self.recipients]
		return ' '.join(people)


xmas = GiftList('xmas')
