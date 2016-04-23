#unpacking
def hallo(name, age, class_=""):
	"""
	explanation on what it does
	"""
	if class_ != "":
		return "i am {}, and i am {}, and {} class".format(name, age, class_)
	return "i am {}, and i am {}".format(name,age)

people = [
			("jane",23,'high'),
			("joe" , 25,'low'),
			("brian", 60),
			("betty", 45)
		]
'''
for name, age, class_ in people:
	print hallo(name,age, class_)
'''
	#use of unpacking
for person in people:
	print hallo(*person)


def super_sum(*args):
	"""
	takes in variable number of items
	and returns the sum.
	e.g. super_sum(10,20)=30
	super_sum(10,20,30)=70
	"""

	total = 0
	for i in args:
		total += i

	return total

print super_sum(10, 20)
print super_sum(1,4,5,7)
a = [10,40,60]
print super_sum(*a)
b = {1:"hallo",2:"me"}
print super_sum(*b)

def hello_again(**kwargs):
	return "i am {}, and i am {}".format(kwargs['name'],kwargs['age'])

print hello_again(name='Joe', age=20)
print hello_again(age=20, name='jane')



joe={'name': 'joe', 'age':98}

print hello_again(**joe) 
print hello_again(name='joe',age=98)






