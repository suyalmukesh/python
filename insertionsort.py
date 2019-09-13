""" Time Complexity O(n**2) (Avg and worst )
    Space O(1)
    Good if number of elements are small , or when array is almost sorted
"""
import sys

def insertsort(a):
    n = len(a)
    for i in range(1, n):
        x = a[i]
        j = i-1
        print("i loop* i:j", i, j)
        while j >= 0 and a[j] > x:
            print("i+j loop+ i:j", i, j)
            a[j+1], a[j] = a[j], a[j+1]
            j = j-1
            print(a)

    return a
# Note when list is already sorted the inner while loop will not get triggered
# So best case = O(n) when list is already sorted


if __name__ == '__main__':
    #ar = [12, 11, 13, 5, 6]
    ar = []
    for i in range(int(input())):
        ar.append(int(input()))

    #ar = [1, 2, 3, 4, 5, 6, 7, 8]
    print("After Insert Sorting : ",insertsort(ar))
