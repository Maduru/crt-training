# tress using Linked List-->Double Linked List:
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def Inorder(Node):
#     if Node is None:
#         return
#     Inorder(Node.left)
#     print(Node.data,end=" ")
#     Inorder(Node.right)
# def preorder(Node):
#     if Node is None:
#         return
#     print(Node.data,end=" ")
#     preorder(Node.left)
#     preorder(Node.right)
# def postorder(Node):
#     if Node is None:
#         return
#     postorder(Node.left)
#     postorder(Node.right)
#     print(Node.data,end=" ")
# root=Node('A')
# root.left=Node('B')
# root.left.left=Node('D')
# root.left.left.right=Node('H')
# root.left.right=Node('E')
# root.right=Node('C')
# root.right.left=Node('F')
# root.right.right=Node('G')
# root.right.right.left=Node('I')
# print("Inorder traversal:")
# Inorder(root)
# print("----------------")
# print("preorder Traversal:")
# preorder(root)
# print("---------------")
# print("postorder Traversal:")
# postorder(root)
# print("---------------")

               
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None 
# def Inorder(Node):
#     if Node is None:
#         return
#     Inorder(Node.left)
#     print(Node.data,end=" ")
#     Inorder(Node.right)    
# def insert(root,ele):
#     if root is None:
#         return Node(ele)
#     else:
#         if root.data==ele:
#             return root
#         elif root.data<ele:
#             root.right= insert(root.right,ele)
#         else:
#             root.left= insert (root.left,ele)
#     return root
# obj=Node(56)
# obj=insert(obj,45)
# obj=insert(obj,35)
# obj=insert(obj,95)
# obj=insert(obj,75)
# obj=insert(obj,23)
# obj=insert(obj,411)
# obj=insert(obj,35)
#Inorder(obj)



n=5
for i in range(0,n):
    for j in range(0,n-i-1):
        print("",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(n):
    print("*"+" "*7+"*")
for i in range(1):
    print("* "*5)
for i in range(2):
    print("* "*2+" "*2+ "* "*2)



