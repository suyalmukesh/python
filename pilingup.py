import time
import sys

def pileup(sample1):
  n = len(sample1)
  i,j = 0,n-1
  while i<j:
      if sample1[i] >= sample1[j]:
         i += 1;j -= 1
      else:
          return 1
  return 0

if __name__=='__main__':
    no_of_tests = int(input())

    for i in range(no_of_tests):
        ar = []
        j = int(input())
        str = input().split(' ')
        for k,m in range(j),str:
            ar.append(int(str))

        print(ar)
        ind = pileup(ar)
        print("Yes" if ind == 0 else "No")