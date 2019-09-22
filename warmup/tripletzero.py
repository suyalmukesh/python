# Easy !  Given N distinct integers , how many triplets sum to exactly Zero ?
import time
import sys
lst = []
#for i in range(int(input())):
 #   lst.append(int(input()))

lst = [i for i in range(-98, 500)]
start_time = time.time()
count = 0
n = len(lst)

# brute force algorithm
for i in range(0, n):

    for j in range(i+1, n):

        for k in range(j+1, n):

            if lst[i] + lst[j] + lst[k] == 0:

                print(lst[i], lst[j], lst[k])
                count += 1
                print(count)
print("The program took ", time.time() - start_time, "seconds to run")



