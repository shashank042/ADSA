'''
Double Linked List:
Data store Nodes
Nodes 3 parts
1. data
2. prev
3. next

Algorithm:
1. create nodes
2. insert data
3. connection b/e nodes
4. traverse nodes

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

def traverse():
    curr = node1
    while curr:
        print(curr.data, end = "<->")
        curr = curr.next
    print("None")
traverse()