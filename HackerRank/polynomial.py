import numpy
A = []
n = input().split()
B = float(input())
for i in n:
    A.append(float(i))


print(numpy.polyval(A,B))


