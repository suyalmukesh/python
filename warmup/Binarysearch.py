"""
Time Complexity :  T(n) = T(n/2) + c  =  O(log(n))

"""

import sys
def bsearch(arr,a,left,right):
    l, r = left, right
    mid = int((l + r)/2)

    if arr[mid] == a:
        print("Element found at position ",mid)
        return mid

    elif a < arr[mid]:
        l = mid
        return bsearch(arr, a, l, r)

    elif a > arr[mid]:
        l = mid+1
        return bsearch(arr, a, l, r)
    else:
        return -1

""" ----------------------------------------------------------------------- """
if __name__ == '__main__':
   sys.setrecursionlimit(15000)
   ar = []
   for i in range(int(input())):
      ar.append(int(input()))  # time being insert sorted list

   element = 5
   print(bsearch(ar,element,0,len(ar)-1))


