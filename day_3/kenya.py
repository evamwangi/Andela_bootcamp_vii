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

k = Kenyan('miguna', 20)

k.probe(True)

print "is {} corrupt? {}".format(k.name, k.is_corrupt())

print k.say_hello()

l= Kenyan('kamau', 30)
print "is {} corrupt? {}".format(l.name, l.is_corrupt())
print l.say_hello()


