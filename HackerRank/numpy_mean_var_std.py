import numpy

n, m = map(int,input().split())

A = numpy.array([input().split() for _ in range(n)],int )
numpy.set_printoptions(sign=' ')
print(numpy.mean(A,axis = 1))
print(numpy.var(A,axis = 0))
print(numpy.around(numpy.std(A),12))