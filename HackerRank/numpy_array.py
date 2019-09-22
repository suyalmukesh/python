import numpy

n = input()
my_input = []
for i in n.split():
    my_input.append(i)

print( numpy.array(my_input[::-1],float))


