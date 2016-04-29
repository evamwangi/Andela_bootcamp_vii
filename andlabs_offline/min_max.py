def min_max(A):

	"""
	return an array containing the min and max number from a list
	"""

	max_, min_ = A[0], A[0]

	for i in A:
		if i > max_:
			max_ = i

		if i < min_:
			min_ = i

	if max_ != min_:
		b = []
		b.append(max_)
		b.append(min_)
		return "{} for {}".format(b,A)

	else:
		a = []
		a.append(len(A))
		return a
		
print min_max([10,20,746,908,543])
print min_max([4,4,4,4,4])




