import numpy

A = numpy.array([input().split() for _ in range(int(input()))], float)

print(round(numpy.linalg.det(A),2))