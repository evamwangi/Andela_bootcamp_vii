"""
global variables are not a good idea
"""
people = [

	('joe', 78),
	('janet', 90),
	('Brian', 67)
]


def super_sum(*args):
	return sum(args)


def hello_again(name,age):
	return "i am {} and {} years old".format(name,age)

def max_min(A):
	"""
	takes the maximum and substract the minimum

	"""
	#return (max(A)-min(A)) its built in

	max_, min_ = A[0], A[0]

	for i in A:
		if i > max_:
			max_ = i
		if i < min_:
			min_ = i

	return max_ - min_


print max_min([1,4,7,5,4,9])
