"""  0 1 2 3 4 5 6 7 8 9   """
import sys
def get_input():
      res = []
      num = []
      n = int(input("Enter the number of elements : \n"))
      for i in range(n):
          a = int(input("Enter the element of array: "))
          num.append(a)
      m = int(input("\nEnter number of connected nodes :"))
      for i in range(m):
         temp = [0]*2
         x,y = input("Enter connected nodes").split()
         temp[0]=x
         temp[1]=y
         res.append(temp)
      return num,res

def find_no_of_connected_nodes():
         a = []
         b = []

if __name__ == '__main__':
    allnodes,connections  = get_input()
    print(allnodes)
    print("\n")
    print(connections)





