# #queue
# class Queue:
#     def __init__(self):
#         self.q=[]
#     def isEmpty(self):
#         return self.q==[]
#     def enqueue(self,ele):
#         return self.q.append(ele)
#     def dequeue(self):
#         if self.isEmpty():
#             return -1
#         else:
#             return self.q.pop(0)
#     def peek(self):
#         if self.isEmpty():
#             return -1
#         else:
#             return self.q[0]
#     def search(self,ele):
#         if self.isEmpty():
#             return -1
#         elif ele in self.q:
#             n= self.q.index(ele)                  
#             return n
#         else:
#             return -2
#     def display(self):
#         if self.isEmpty():
#             print("queue is empty")
#         else:
#             for i in self.q:
#                 print(i,end=" ")
#             print()       

import sys
from collections import deque
q=deque()
while True:
    print("----DeQue Operations----")
    print("\t\t\t1.Enqueue:")
    print("\t\t\t2.Dequeue:")
    print("\t\t\t3.Peek:")
    print("\t\t\t4.search:")
    print("\t\t\t5.Display:")
    print("\t\t\t6.Exit")
    option=int(input("Enter your Choice:"))
    if option==1:
        e=int(input("Enter the element to insert:"))
        q.appendleft(e)
    elif option==2:
       if len(q)==0:
           print("deque is empty")
       else:
           
           print(f"popped element is: {q.pop()}")
    elif option==3:
        if len(q)==0:
            print("queue is empty")
        else:
            print("peek ele is",q[len(q)-1])
    elif option==4:
        e=int(input("enter a number to search"))
        flag=False
        for i in q:
            if i==e:
                print(f"eelment found at:{q.index(e)+1}")
                falg=True
                break
            if flag==False:
                print("element not found")
    


    elif option==5:
        if len(q)==0:
            print(" queue is empty")
        else:
            for i in q:
                print(i,end=" | ")
        print()
    elif option==6:
        sys.exit()
    else:
        print("enter valid option")
        



