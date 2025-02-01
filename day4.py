# # n = int(input("enter no of subjects you want to store"))
# # l= [int(input("enter sub:{} ".format(i+1))) for i in range(n)]
# # print(l)
# # while True:
# #     print("Enter option for the following operations")
# #     c=int(input("1.Find max\n2.Find min\n3.Find avg\n4.Exit\n"))
# #     if c==1:
# #         print("max is:",max(l))
# #     elif c==2:
# #         print("min is:",min(l))
# #     elif c==3:
# #         print("avg is:",sum(l)/n)
# #     elif c==4:
# #         break
# #     else:
# #         print("enter valid option")

# # s1= set(map(int,input("enter multiple elements with space:").split()))
# # s2= set(map(int,input("enter multiple elements with space:").split()))
# # s3= set(map(int,input("enter multiple elements with space:").split()))
# # o=list(s1.intersection(s2.intersection(s3)))
# # print(o)


# s1= set(map(int,input("enter multiple elements with space:").split()))
# s2= set(map(int,input("enter multiple elements with space:").split()))

# a= list(s1)
# b= list(s2)
# d=[]
# m = max(len(a),len(b))
# for i in range(m):
#     if a[i] in b:
#         d.append(a[i])        
# print(d)

s1= list(input("enter multiple elements with space:").split())
a=set(s1)
e ={}
print(s1)
for k in s1 :
    c=s1.count(k)
    e[k]=c
print(e)


    









