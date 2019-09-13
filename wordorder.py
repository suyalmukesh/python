import sys

def no_of_distinct_words(a):

     cnt = []
     count = 0
     newlist = []
     for i in a:
         if i not in newlist:
            count = a.count(i)
            cnt.append(count)
            newlist.append(i)
     return(cnt)

if __name__ == '__main__':
  a=[]
  n = int(input())
  for i in range(n):

      a.append(input())
  c= no_of_distinct_words(a)
  print(len(c))
  for i in c:
      print(i,end = ' ')





