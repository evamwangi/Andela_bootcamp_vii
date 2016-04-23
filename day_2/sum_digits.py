def sum_digits(A):
	"""
	takes a list A and returns the sum of all the digits in the list
	e.g.[10,30,45] should return 1+0+3+0+4+5

	"""
	

	b=list("".join(str(i) for i in A))
	return sum(int(i) for i in b)

print sum_digits([10,30,45])
	


	

