# # # import array
# # # def lsearch(a,e):
# # #     c=0
# # #     for i in range(len(a)):
# # #         if a[i]==e:
# # #             p=i
# # #             print("found")
# # #             c+=1
# # #             break
# # #         else:
# # #             print("not found")
# # #             p=-1
# # #             c+=1
# # #     print("no. of comparisions made:",c)
# # #     return p

# # # a= array.array('i',[1,4,5,7,8,2,8,98,6,7,45,34,2,3,34,56,56,40,89,87,78,67])
# # # e = int(input("enter element to be searched:"))
# # # pos=lsearch(a,e)
# # # if pos==-1:
# # #     print("element not found")
# # # else:
# # #     print("the element found at {} position".format(pos))



# # def bsearch(l,n):
# #     lb=0
# #     ub=len(l)-1 
# #     mid = 0
# #     while lb<=ub:
# #         mid = (lb+ub)//2
# #         if n<l[mid]:
# #             ub= mid-1
# #         elif n>l[mid]:
# #             lb= mid+1
# #         else:
# #             return mid
# #     return -1
# # l= list(map(int,input().split()))
# # l.sort()
# # print("the original list is",l)
# # n= int(input("enter the element to search:"))
# # ret=bsearch(l,n)
# # if ret==-1:
# #     print(" element not found")
# # else:
# #     print("element found at:",ret)



# def bubble(l):
#     for i in range(len(l)-1):
#         for i in range(len(l)-i-1):
#             if l[i]>l[i+1]:
#                 temp = l[i]
#                 l[i]=l[i+1]
#                 l[i+1]=temp
#     return l
# l=list(map(int,input().split()))
# print(" before sort",l)
# r= bubble(l)
# print(r)
    


def sele(l):
    for i in range(len(l)):
        min=i
        for j in range(i+1,len(l)):
            if l[j]<l[min]:
                min=j

        temp=l[i]
        l[i]=l[min]
        l[min]= temp
        print(l)
    print()
    return l
l=list(map(int,input().split()))
print(sele(l))

