import sys
from day10 import*
s=stack()
while True:
    print(" select the following option")
    print("\t\t1.push")
    print("\t\t2.pop")
    print("\t\t3.peek")
    print("\t\t4.search")     
    print("\t\t5.display")
    print("\t\t6.Exit")
    o= int(input("enter option:"))
    if o==1:
        ele= int(input(" enter data :"))
        s.push(ele)
    elif o==2:
        ret=s.pop()
        if ret==-1:
            print("stack is empty")
        else:
            print("popped element",ret)
        
    elif o==3:
        ret=s.peek()
        if ret==-1:
            print("stack is empty")
        else:
            print("peek element",ret)

    elif o==4:
        ele= int(input(" enter element to search"))
        ret=s.search(ele)
        if ret==-1:
            print("stack is empty")
        elif ret==-2:
            print("not found")
        else:
            print("found at index:",ret)
    elif o==5:
        s.display()
    elif o==6:
        sys.exit()
    else:
        print("enter valid option")
  
