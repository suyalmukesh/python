import numpy

n = input()
inp = []

a=  n.split()
for i in a:
 inp.append(int(i))

lst = numpy.array(inp)
print(numpy.reshape(lst,(3,3)))


