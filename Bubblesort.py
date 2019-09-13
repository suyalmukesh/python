"""------------------------------------------------------------------------------------------------------------
Bubble Sort : Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted
--------------------------------------------------------------------------------------------------------------"""
import sys

def bubble(arr):
    for j in range(len(arr)):
       print("\nIteration : ", j)
       for i in range(0, len(arr)-1):
           swap = 0
           if arr[i] > arr[i+1]:
             arr[i],arr[i+1] = arr[i+1],arr[i]
             swap = 1

             print("arr",arr)
             i += 1


    return arr

if __name__ == '__main__':
    n = int(input("Enter number of elements i array"))
    ar = []
    for i in range(n):
        ar.append(int(input()))
    print(ar,len(ar))
    print(bubble(ar))
