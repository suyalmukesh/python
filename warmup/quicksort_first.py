# keeping first element as PIVOT
def partition(arr, low, high):
    pivot = arr[low]
    i = high + 1

    for j in range(low, high):
        if arr[j] >= pivot:
            i -= 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i - 1], arr[high] = arr[high], arr[i - 1]
    print("i+1", i + 1)
    return (i+1)
# -------------------------------------------------------------------------
def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)
    return arr
# ------------------------------------------------------------------------
if __name__ == '__main__':
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    n = len(arr)
    print(quicksort(arr,0,n-1))

