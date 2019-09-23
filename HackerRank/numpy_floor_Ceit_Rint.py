import numpy

a = map(float, input().split())
aa = []
for i in a:
    aa.append(i)

my_array = numpy.array(aa)
numpy.set_printoptions(sign=' ')
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))


