import sys
class node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def traverse(self,a):
        while(a != None):
            print(a.val)
            a = a.next

    def add_to_last(self,node):
        while(self != None):
            self = self.next
        self.next = node

    def delete_last(self):
        while(self.next.next != None):
            self.next = None

    def print_backward(self,list):
        if list is None: return
        head = list
        tail = list.next
        list.print_backward(tail)
        print(head, end=" ")

if __name__ == '__main__':
    a = node(5)
    b = node(5)
    c = node(6)

    a.next = b
    b.next = c

    a.traverse(a)
    c.print_backward(c)
