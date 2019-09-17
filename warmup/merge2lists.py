import sys
import time
# merge 2 lists
lst1 = [1, 2, 4]
lst2 = [3, 5, 6]
# Result = [1,2,3,4,5,6]
n = len(lst1)
m = len(lst2)
i, j, k = 0, 0, 0
temp = [0]*(n+m)
print(temp)

while i < n and j < m:
    print("i,j", i, ":", j)
    if lst1[i] < lst2[j]:
        temp[k] = lst1[i]
        k += 1
        i += 1
    else:
        temp[k] = lst2[j]
        k += 1
        j += 1

while(i<n):
    temp[k] = lst1[i]
    i += 1
    k += 1
while(j<m):
    temp[k] = lst2[j]
    j += 1
    k += 1



print("Final i,j,k", i, ":", j, ":",k)
print(temp)



