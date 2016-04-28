def min_max(A):

	min_, max_ = A[0], A[0]

	b = []

	for i in A:

		if i > max_:
			max_ = i  

		if i < min_:
			min_ = i

	if max_ != min_:

		b.append(max_)
		b.append(min_)

	else:
		b.append(A[i])

	


	return b




	#return max_ - min_


print min_max([12,4,57,3,7])

print min_max([7,7,7,7])


		


	