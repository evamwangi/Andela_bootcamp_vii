b = [(2,4),(5,10),(6,20),(50,50)]

"""
x:2, y:4
x:5, y:10
"""

for x, y in b:
	print "x: {}, y: {}".format(x, y)

"""its too much work. hold that thought"""
for h in b:
	for l in h:
		print l

"""another way"""

for d in b:
	print "x: {}, y: {}".format(d[0], d[1])


	"""
	assignment2
	have an array f=[(10,20,40),(10,20),(4,5,50)]
	"""





	

