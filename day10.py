# #double linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insert_begin(self,data):
#         new= Node(data)
#         if self.head is None:
#             self.head=self.tail=new
#         else:
#             new.next=self.head
#             self.head.prev=new
#             self.head=new
#     def insert_end(self,data):
#         new= Node(data)
#         if self.head is None:
#             self.head= self.tail=new
#         else:
#             new.prev=self.tail
#             self.tail.next=new
#             self.tail=new
    
#     def delete_begin(self):
#         if self.head is None:
#             print("dll is empty")
#         else:
#             current= self.head
#             self.head= self.head.next
#             self.head.prev=None
#             current.next=None
#             del current

#     def delete_end(self):
#         if self.head is None:
#             print("dll is empty")
#         else:
#             current= self.tail
#             self.tail=self.tail.prev
#             self.tail.next=None
#             current.prev=None
#             del current
#     def serach(self,ele):
#         if self.head is None:
#             print("dll is empty")
#         else:
#             current= self.head
#             while current:
#                 if current.data==ele:
#                     print("found")
#                     break
#                 else:
#                     current= current.next



#     def find_len(self):
#         c=0
#         if self.head is None:
#             print("dll is empty")
#         else:
#             current= self.head
#             while current:
#                 current= current.next
#                 c+=1
#             print("no.of nodes",c)

    
#     def display_f(self):
#         if self.head is None:
#             print("dll is empty")
#         else:
#             current= self.head
#             while current:
#                 print(current.data,end=" ")
#                 current= current.next
#             print()

#     def display_b(self):
#         if self.head is None:
#             print("dll is empty")
#         else:
#             current= self.tail
#             while current:
#                 print(current.data,end=" ")
#                 current= current.prev
#             print()


# ll= LinkedList()
# f=Node(100)
# s= Node(200)
# t=Node(300)
# ll.head=f
# f.next= s
# s.next=t
# ll.tail=t
# t.prev=s
# s.prev=f
# print(f.data)
# print(f.next.next.data)
# print("insert at begin")
# ll.insert_begin(780)
# print("display forward")
# ll.display_f()
# print("display forward")
# ll.display_b()
# print("insert at end")
# ll.insert_end(890)
# ll.display_f()
# print("delete at begin")
# ll.delete_begin()
# ll.display_f()
# print("delete at end")      \
     

# ll.delete_end()
# ll.display_f()
# ll.find_len()
# print("search")
# ll.serach(300)








#stack
class stack:
    def __init__(self):
        self.st=[]
    def isEmpty(self):
        return self.st==[]
    def push(self,ele):
        return self.st.insert(0,ele)
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.st.pop(0)
    def peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.st[0]
    def search(self,ele):
        if self.isEmpty():
            return -1
        if ele in self.st:
            return self.st.index(ele)
        else:
            return -2
    def display(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            for i in self.st:
                print(i)
                print("---")
        
        

    