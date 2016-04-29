def factorial(number):

	"""
	returns the factorial of a number
	
	"""

	 if number == 0:
	 	return 1

	 else:
	 	return number * factorial(number-1)

print factorial(3)