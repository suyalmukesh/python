"""
This program adds 2 very-very long numbers

"""

def add(a,b):
      ans = ''
      left, right = len(a)-1, len(b)-1
      sum, carry = 0, 0
      while left >= 0 or right >= 0:
             if left < 0:
                i = 0
             else: i = int(a[left])
             if right < 0:
                 j = 0
             else: j = int(b[right])

             sum = carry + (i + j)%10
             carry = int((i+j)/10)

             ans = ans + str(sum)
             left -= 1
             right -= 1
      return ans[::-1]

if __name__ == '__main__':
 a = '111111111111111111111111111111111111111111111111111111111111111111'
 b = '1111111111111111111111111111111111111111111111111111111111111111111'

 a = input("Enter first number")
 b = input("Enter second number")

 sum = []
 sum = add(a,b)
 print(sum)






