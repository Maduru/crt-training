# n = int(input("enter the range:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum) 

# while True :
#     print("1.Add\n2.Subtract\nMultiply\n4.Exit")
#     c= int(input("enter your choice:"))
#     if c==1:
#         a = int(input("enter a value :"))
#         b = int(input("enter b value :"))
#         print("sum is",a+b)
#     elif c==2:
#         a = int(input("enter a value :"))
#         b = int(input("enter b value :"))
#         print("subtraction is",a-b)
#     elif c==3:
#         a = int(input("enter a value :"))
#         b = int(input("enter b value :"))
#         print("multiply is",a*b)
#     elif c==4:
#         break
#     else:
#         print("enter valid option")
        


# p = input("enter password:") 
# r=input("enter password in reverse:")
# rev = p[::-1]
# if r==rev:
#     print("valid")
# else:
#     print("invalid")


s = input("enter string:")
print("original string :",s)
print("after elimination:",s[:len(s):2])
