import numpy

n, m, p = input().split()
n, m, p = int(n), int(m), int(p)
array1, array2 = [],[]
for i in range(n):
    a = input().split()
    for i in a:
        array1.append(int(i))
for i in range(m):
    a = input().split()
    for i in a:
        array2.append(int(i))

a = numpy.reshape(array1, (n, p))
b = numpy.reshape(array2, (m, p))
print(numpy.concatenate((a,b), axis = 0))