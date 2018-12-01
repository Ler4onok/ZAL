class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            state = False
            while state is not True:
                if value > current.value:
                    if current.right is None:
                        current.right = Node(value)
                        state = True
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = Node(value)
                        state = True
                    else:
                        current = current.left


bst = BinarySearchTree()
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(3)
bst.insert(1)
bst.insert(10)





































# class Node:
#         def __init__(self, value):
#             self.value = value
#             self.left = None
#             self.right = None
#
#
# class BinarySearchTree:
#         def __init__(self):
#             self.root = None
#
#         def insert(self, value):
#             new_node = Node( value )
#             if self.root == None:
#                 self.root = new_node  # 4, has .value, .right, .left
#             elif (self.root != None):
#                 root = self.root
#                 state = False
#                 while state != True:
#                     if root.value < value:
#                         if root.right == None:
#                             root.right = new_node
#                             state = True
#                         elif (root.right != None):
#                             root = root.right  # recursion, right node becomes a root
#                     elif (root.value > value):
#                         if root.left == None:
#                             root.left = new_node
#                             state = True
#                         elif (root.left != None):
#                             root = root.left
#
#         def fromArray(self, array):
#             for i in range (len(array)):
#                 if i == 0:
#                     self.root = Node(array[i])
#                 else:
#                     root = self.root
#                     state = False
#                     while state != True:
#                         if root.value < array[i]:
#                             if root.right == None:
#                                 root.right = Node(array[i])
#                                 state = True
#                             else:
#                                 root = root.right
#                         elif root.value >array[i]:
#                             if root.left == None:
#                                 root.left = Node(array[i])
#                                 state = True
#                             else:
#                                 root = root.left
#
#         def search(self, value):
#             self.visited = 0
#             root = self.root
#             while root != None:
#                 if root.value == value:
#                     self.visited+=1
#                     return True
#                 else:
#
#                     if value > root.value:
#                         root = root.right
#
#                     elif value < root.value:
#                         root = root.left
#                     self.visited+=1
#
#
#             return False
#
#
#         def min(self):
#             self.visited = 1
#             root = self.root
#             if root is not None:
#                 while root.left is not None:
#                     root = root.left
#                     self.visited += 1
#                 return root.value
#             else:
#                 return None
#
#
#
#
#         def max(self):
#             self.visited = 1
#             root = self.root
#             if root is not None:
#                 while root.right is not None:
#                     root = root.right
#                     self.visited += 1
#                 return root.value
#             else:
#                 return None
#
#         def visitedNodes(self):
#             return self.visited
#
