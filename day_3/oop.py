from person import Person

p = Person('Joe', 23)

print p

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

