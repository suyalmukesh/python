""" Analysis : Selection sort
Best  : O(n**2)
Worst : O(n**2)
Avg   : O(n**2)
Space : O(1)
-----------------------------------------------"""
import sys
import time
def selectsort(a):
    start_time = time.time()
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            #print("i:j", i, ":", j)
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                #print(a)
    print("The program took ", time.time() - start_time, "seconds to run")
    return a

if __name__ == '__main__':
    ar = []
    a1 = [1, 2, 3, 4, 5, 67, 8, 9, 10]
    a2 = [i for i in range(100, -100)]
    a3 = [i for i in range(0, 1000)]
    a32 = [i for i in range(0, 2000)]
    a34 = [i for i in range(0, 4000)]
    a38 = [i for i in range(0, 8000)]
    a4 = [i for i in range(0, 10000)]

    ar = [a1, a2, a3, a32,a34,a38,a4]
    for i in ar:
        selectsort(i)
        # examining running time for the algo by doubling the sizes

