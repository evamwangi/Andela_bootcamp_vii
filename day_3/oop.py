class Person:

	people_count = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age
		Person.people_count += 1

	def __repr__(self):
		return "<object: {}, {}>".format(self.name,self.age)

	def say_hello(self):
		return "hello, i am {} and {} y/o".format(self.name,self.age)

p = Person('Joe', 23)
p2 = Person('jane',23)
p3 = Person('george',40)


print p.say_hello()


a = [('jane' , 23), ('jackie', 34), ('jacob', 23), ('jee', 18), ('josh',60)]
b = []
for name, age in a:
	person = Person(name, age)
	b.append(person)

for i in b:
	print i.say_hello()



#print Person.people_count
#print p2.people_count  # chain look_up

print b

