def data_type(x):
	"""
	takes in an argument, x:
	-for a integer, return x**2
	-for a float, return x/2
	-for a string, returns "Hello" + x
	-for a boolean, return "Boolean"
	-for a long , returns "Long"
	"""
	if type(x) == int:
		return x ** 2

	elif type(x) == float:
		return x / 2

	elif type(x) == str:
		return "Hello " + x

	elif type(x) == bool:
		return "Boolean"

	elif type(x) == long:
		return "Long"

	else:
		return "Not in the requirements"

print data_type("mum")
print data_type([1,2,3])
print data_type(False)
print data_type(10)
print data_type(1.675)
print data_type(50**50)


