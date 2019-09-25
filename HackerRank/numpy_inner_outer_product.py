import numpy


A = numpy.array([input().split()],int)
B = numpy.array([input().split()],int)

a = numpy.inner(A, B)
print(a[0][0])
print(numpy.outer(A, B))
