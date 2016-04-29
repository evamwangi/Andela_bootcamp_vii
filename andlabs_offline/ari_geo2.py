def arith_geo(A):

    length = len(A)

    for i in range(1, length-1):

        if A[i+1] - A[i] == A[i+2] - A[i+1] == A[i+2] - A[i+1] + A[i+1] - A[i]  :

            return "arithmetic"

        elif A[i+1] / A[i] == A[i+2] / A[i+1] == A[i+2] / A[i+1] *A[i+1] / A[i] :
            return "geometric"

        elif A == []:
            return 0

        else:
            return -1
print arith_geo([15, 10, 5, 0, -5, -10])
