def fizz_buzz(number):

	"""
	return 'Fizzbuzz' if number is divisible by 3 and 5
	return 'Fizz' if number is divisible by 3
	return 'Buzz' if number is divisible by 5
	return the number if it is not divisible by 3 and 5

	"""

	if number % 3 == 0 and number % 5 == 0:
		return 'Fizzbuzz'

	elif number % 3 == 0:
		return 'fizz'

	elif number % 5 == 0:
		return 'buzz'

	else:
		return number
		
print fizz_buzz(10)

