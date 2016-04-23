def funky(a, b):

	"""takes two arguments dictionaries,lists, ints, float and ints,strings and returns (arg1+arg2) """
	if type(a)==type(b) and type(a) != dict and type(b) != dict :
		return (a + b)

	if type(a)==float and type(b)==int or type(a)==int and type(b)==float:
		return (a + b)

	if type(a)==dict and type(b)==dict:
		 a.update(b)
		 return a


	else:
		return ("invalid inputs")
		

	


print(funky(2,5))
print(funky("eva","mwangi"))
print(funky(4.87,89.9))
print(funky(['abcd', 786, 2.23],['john', 70.2]))
print(funky("foll",9))
print(funky({1:"hello",2:"listen"},{3:"i am",4:"here"}))
print(funky(2,3.6))
