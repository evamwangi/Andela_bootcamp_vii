def arith_geo(A):

    length = len(A)

    if length == 0:
    	return 0


    for i in range(length-1):

        if A[i+1] - A[i] == A[i+2] - A[i+1] == A[i+3] - A[i+2] :

            return "Arithmetic"

        elif A[i+1] / A[i] == A[i+2] / A[i+1] == A[i+3] / A[i+2]:
            return "Geometric"


        else:
            return -1

print arith_geo([2,4,6,8,10])
print arith_geo([3,9,27,81,243])
print arith_geo([0.5, 3.5, 24.5, 171.5])
print arith_geo([])