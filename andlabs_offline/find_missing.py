def find_missing(A, B):

	"""
	returns the missing number in a list
	[1,2,3] and [1,2,3,4] should return 4
	[4,66,7] and [66,77,7,4] should return 77

	"""
	if A != B:
		first_set = set(A)
		second_set = set(B)
		if first_set != second_set:
			b = list(second_set - first_set)

			return b[0]
	else:
		return 0

list1 = find_missing([1, 2], [1, 2, 5])
list2 = find_missing([4, 6, 8], [4, 6, 8, 10])
list3 = find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])
print [list1, list2, list3]