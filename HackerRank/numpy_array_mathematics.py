"""
1 4
1 2 3 4
5 6 7 8  """

import numpy
task = []
n,m = map(int,input().split())
arr1,arr2 = [],[]
for i in range(n):
    a =  map(int,input().split())
    for j in a:
        arr1.append(j)
for i in range(n):
    a =  map(int,input().split())
    for j in a:
        arr2.append(j)

arr1 = numpy.array(arr1)
arr1 = arr1.reshape((n,m))
arr2 = numpy.array(arr2)
arr2 = arr2.reshape((n,m))



print(numpy.array(arr1+arr2))
print(arr1-arr2)
print(arr1*arr2)
print(arr1//arr2)
print(arr1%arr2)
print(arr1**arr2)
