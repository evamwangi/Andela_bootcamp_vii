from person import Person

class Kenyan(Person):
	corrupt = False

	def probe(self,corrupt):
		self.corrupt = corrupt

	def is_corrupt(self):
		if self.corrupt:
			return "yes"
		return "no"


#for now

