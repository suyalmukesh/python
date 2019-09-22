#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n,m = input().split()
    n,m = int(n),int(m)
    matrix = [[0]*m]*n
    print(matrix)

    for i in range(n):
          j_list = []
          str = input()
          for j in range(m):
             j_list.append(str[j])
          matrix[i]=(j_list)

    strr = ''
    for i in range(m):
        for j in range(n):
            strr = strr+matrix[j][i]

    pattern = '[a-zA-Z][^a-zA-Z0-9]+[a-zA-Z]'
    print(strr)
    new = re.sub(pattern,' ',strr)
    print("new",new)









