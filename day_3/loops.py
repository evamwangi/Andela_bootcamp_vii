a = [10, 20, -9, 45, 60, 80]

for  i in  a:
	#print i
	
	# print in reverse

i = len(a)

while i > 0:
	print a[i - 1]
	i -= 1

for index in range(len(a)-1, -1, -1):
	print a[index]

b = [(2,4),(5,10),(6,20),(50,50)]

for k in b:
	for n in k:
		print n