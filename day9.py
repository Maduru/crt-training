#single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
ll=LinkedList()
f= Node(100)
s= Node(300)
t= Node(400)
ll.head=f
f.next=s
s.next=t
print(f.data)
print(s.data)
print(t.data)
print(id(f))
print(id(f.next))
print(id(s))

insert at begin 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
        else:
            new.next=self.head
            self.head=new
    def delete_begin(self):
        if self.head is None:
            print(' linked list is empty')
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            del temp



    def insert_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
        else:
            c= self.head
            while(c.next):
                c= c.next
            c.next= new

    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while(temp.next.next):
                temp=temp.next
            delnode=temp.next
            temp.next=None
            del delnode

    def find_len(self):
        c=0
        if self.head:
            current= self.head
            while current:
                c+=1
                current=current.next
            return c

    def search(self,data):
        c_p=1
        if self.head is None:
            print("linked list is empty")
        else:
            current= self.head
            while current:            
                if current.data==data:
                    print("ele is found at {} position".format(c_p))
                    break
                else:
                    current= current.next
                    c_p+=1               
            else:
                print("not present")


    def insert_at_pos(self,pos,data):
        if self.head is None:
            print("linked list is empty")
        else:
            l= self.find_len()
            if pos<=0:
                print("should be >0")
            elif pos==1:
                self.insert_begin(data)
            elif pos==l+1:
                self.insert_end(data)
            elif pos>l:
                print("position doesn't exist")
            else:
                new=Node(data)
                temp=self.head
                c_p=1
                while temp:
                    if c_p==pos-1:
                        new.next=temp.next
                        temp.next=new
                        return
                    else:
                        c_p+=1
                        temp=temp.next


    def display(self):
        if self.head:
            current=self.head
            while current:
                print(current.data,end=" ")
                current=current.next
            print()
        else:
            print("ll is empty")
ll= LinkedList()
ll.insert_begin(100)
ll.display()
ll.insert_begin(800)
ll.display()
ll.insert_end(900)
ll.display()
ll.delete_begin()
ll.display()
ll.delete_end()
ll.display()
print(ll.find_len())
ll.search(100)
ll.insert_begin(800)
ll.insert_begin(700)
ll.insert_begin(300)
ll.display()
ll.insert_at_pos(2,500)
ll.display()


#  #double linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
ll= LinkedList()
f=Node(100)
s= Node(200)
t=Node(300)
ll.head=f
f.next= s
s.next=t
ll.tail=t
t.prev=s
s.prev=f
print(f.data)
print(f.next.next.data)
