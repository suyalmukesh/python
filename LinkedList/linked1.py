class Node:
    def __init__(self,val):
        self.val = val
        self.next = None  # the pointer initially points to nothing

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3






