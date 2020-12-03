class Interface:
	def __init__:(self)
		self.gift_list=GiftList('xmas')
		self.show()

		def show(self):
			for recipient in self.gift_list:
				recipient.show()
			choice=input('1. Add gift 2. Add wish 3. Add recipient')
			if choice not in ['1','2','3']:
				print('Invalid choice')
			else:
				if choice=='1':
					gift=input('What did you buy?')
					price=int(input('How much did it cost?'))
					giftlist.recipients.show()
					recipient=input('Who did you buy it for?')
				elif choice=='2':
					gift=input('What were you thinking of buying?')
					giftlist.recipients.show()
					recipient=input('For who?')
				elif choice=='3':
					recipient=input('Who else do you need to buy for?')

	#TODO break if loop into class methods
