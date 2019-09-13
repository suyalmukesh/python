import sys

def merge(arr, start, mid, end):
    # create a temp array
    temp = [0]*int(end-start+1)

    i, j, k = start, mid+1, 0
    # traverse both the lists and add smaller of both elements in temp
    if((i<= mid ) and (j <= end)):
           if(arr[i] <= arr[j]):
               temp[k] = arr[i]
               k += 1;i += 1
           else:
               temp[k] = arr[j]
               k += 1;j += 1
    # add element left in the first interval
    while(i<mid):
        temp[k]=arr[i]
        k += 1;i += 1
    # add element left in the second inteval
    while(j < end):
        temp[k]=arr[j]
        k += 1;j += 1
    # copy temp to original interval
    for i in range(start,end):
        arr[i] = temp[i-start]
        i += 1

def mergesort(arr,start,end):

    if start < end:
        mid = int((start+end-1)/2)
        mergesort(arr, start, mid)
        mergesort(arr, mid+1, end)
        merge(arr, start, mid, end)

if __name__ == '__main__':
    # print(sys.getrecursionlimit())
    # sys.setrecursionlimit(1500)
    ar = [2,3,8,1,4,3,9,10]
    print(ar)
    mergesort(ar,0,7)
    print(ar)