import numpy

i,j = input().split()
i,j = int(i),int(j)
my_array = []

for ii in range(i):
    a = input().split()
    for k in a:
        my_array.append(int(k))

num_array = numpy.array(my_array)
_array = numpy.reshape(num_array,(i,j))
print(numpy.transpose(_array))
print(num_array.flatten())


