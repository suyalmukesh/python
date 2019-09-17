import sys

# ------------------------------------------------------------------
def partition(ar, low, high):
     print(ar)
     pivot = ar[high]  # making last element as pivot

     i = low-1   # index of smaller element

     print("Pivot: ", pivot," i", i, "low:high ", low, high)

     for j in range(low, high):
         if ar[j] <= pivot:
             i += 1
             ar[j], ar[i] = ar[i], ar[j]

     ar[i+1],ar[high] = ar[high],ar[i+1]
     print("i+1",i+1)
     return (i+1)
# -------------------------------------------------------------------

def quicksort(ar, low, high):
    if low < high:
        pi = partition(ar, low, high)
        quicksort(ar, low, pi-1)   # before pi
        quicksort(ar, pi+1, high)  # After pi
    return ar
# -------------------------------------------------------------------

if __name__ == '__main__':

    ar = [1, 2, 9, 8, 7, 6, 5, 4, 3]
    n = len(ar)
    quicksort(ar, 0, n-1)
    for i in range(n):
      print("%d" %ar[i],end = '  ')

"""
Analysis of QuickSort
Time taken by QuickSort in general can be written as following.

 T(n) = T(k) + T(n-k-1) + \theta(n)
The first two terms are for two recursive calls, the last term is for the partition process. k is the number of elements which are smaller than pivot.
The time taken by QuickSort depends upon the input array and partition strategy. 

"""




