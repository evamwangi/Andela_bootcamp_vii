def super_sum(A):
	"""
	takes in a list A, and: 
		half every even number
		doubles every odd number
		and returns the sum of all
		[2,3]
	"""
	total = 0

	for i in A:
		if i % 2 == 0:
			total += (i / 2)

		else:

			total += (i * 2)

	return total




 