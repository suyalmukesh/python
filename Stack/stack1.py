def push(arr,a):
    arr.append(a)

def pop(arr):
    arr.remove(arr[-1])

if __name__ == '__main__':
    arr = []

value = ''
while(value != 'n'):
      push(arr, value)
      print(arr)
      value = input()




