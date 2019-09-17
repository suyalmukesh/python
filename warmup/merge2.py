import sys

ar = [1, 2, 3, 7, 5, 90, 67, 4, 8]
m = len(ar)
left, right = 0, len(ar)-1
mid = int((left+right)/2)

len1 = mid-left+1
len2 = right-mid
L = [0]*len1
R = [0]*len2
i,j,k = 0,0,0

merge = [0]*(len1+len2)

for i in range(len1):
    L[i] = ar[left+i]
    i += 1
for j in range(len2):
    R[j] = ar[mid+1+j]
    j += 1
# merge







print(len1,len2)
print(L)
print(R)






