"""Given a list of rational numbers,find their product.
Concept
The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.
    reduce(lambda x, y : x + y,[1,2,3])
6
"""
import sys

from fractions import Fraction
from functools import reduce

def product(fracs):
    a = fracs[0]
    b = fracs[1]
    print(a.numerator)
    print(b.numerator)

    #t = reduce(lambda a, b : a.numerator*b.numerator,a.denominator*b.denominator)
    t = reduce(lambda x, y: x*y, fracs) # Very Complicated


    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
        print(type(fracs))
    result = product(fracs)
    print(*result)