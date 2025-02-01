# l=[1,2,34,5,4,2,6,72,2,2]
# # l.sort(reverse=True)
# # print(l)
# # a=l.copy()
# # l[2]=56
# # print(id(l[2]))
# # print(id(a[2]))
# # print(l)
# # print(a) 
# print(l.index(2,4))


# l=[1,2,3,4,5]
# sum=0
# for i in l:
#     sum+=i
# print(sum)

# a=[]
# n= int(input("enter list length:"))
# for i in range(n):
#     e= int(input())
#     a.append(e)
# min=a[0]
# max=a[0]
# for i in a:
#     if min>i :
#         min=i
#     if max<i :
#         max=i
# print( "min is",min)
# print("max is",max)


# l=[1,2,2,3,4,4,5]
# a=[]
# for i in l:
#     if i not in a:
#         a.append(i)
# print(a)


# l=[1,1,2,2,3,4,5,5]
# a=[]
# for i in l:   
#    c= l.count(i)
#     if c==1:
#         a.append(i)
# print(a)


# l= [1,2,3,4,6,7,8,9,10]
# for i in range(1,11):
#     if i not in l:
#         print(i)


# l= [1,2,3,4,6,5,8,9,10]
# sum =0
# for i in l:
#     sum+=i
# print("missing number:{}".format(55-sum))

# a=[8,9,5]
# b=[2,4,6,8,10]
# c=[]
# m= min(len(a),len(b))
# for i in range(m):
#     c.append(a[i])
#     c.append(b[i])
# if len(a)>m:
#     c.extend(a[m:])
# elif len(b)>m:
#     c.extend(b[m:])
# print(c)
    

b=(2,4,6,8,10) 
print(b[::-1])   
