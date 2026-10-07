class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Double_LL:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        return self.head

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return self.head
        
        curr = self.head
        while curr.next:
            curr = curr.next 
        curr.next = new_node
        new_node.prev = curr
        return self.head
    def delete_begin(self):
        if not self.head:
            print("List is empty")
            return None
        self.head = self.head.next
        if self.head:
            self.head.prev = None   
    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

dll = Double_LL()
dll.insert_at_begin(10)
dll.insert_at_begin(20)
dll.insert_at_begin(30)
dll.traverse()
dll.insert_at_end(40)
dll.insert_at_end(50)
dll.traverse()
dll.delete_begin()
dll.traverse()