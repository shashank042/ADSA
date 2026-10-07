class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# Tree structure
root = Node(1)
root.right = Node(2)
root.left = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Tree Traversal techinques
'''
1. DFS
    1. pre-order(Root - left - Right)
    2. in-order(Left - Root - Right)
    3. post-order(Left - Right - Root)
2. BFS(Level order)


'''
def Pre_Order(root):
    if root:
        print(root.data,end= " -> ")
        Pre_Order(root.left)
        Pre_Order(root.right)
print("\n Pre_Order Traversal")
Pre_Order(root)

def In_Order(root):
    if root:
        In_Order(root.left)
        print(root.data,end = " -> ")
        In_Order(root.right)
print("\n In_Order Traversal")

def Post_Order(root):
    if root:
        Post_Order(root.left)
        Post_Order(root.right)
        print(root.data,end = " -> ")
print("\n Post_Order Traversal")
Post_Order(root)
