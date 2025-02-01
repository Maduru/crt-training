n = int(input("enter no. of products: "))
d={}
for i in range(n):
    p=input("enter product's name:")
    v=int(input("enter product's value:"))
    d[p]= v
val = list(d.values())
key = list(d.keys())
print(val)
print(key)
print("the max cost product")
print(key[val.index(max(val))])
print(val[val.index(max(val))]) 


n = int(input("enter no. of players: "))
d={}
for i in range(n):
    p=input("enter player's name:")
    s=int(input("enter score:"))
    d[p]= s
    print("players in the match:")
pnames=list(d.keys())
for i in pnames:
    print(i)
pl = input("enter player name to find score:")
na= d.get(pl)
print(na)


s = input()
print(s[0::2])

n = int(input())
sum=0
for i in range(1,n+1):
    sum+=i
    if i%2==0:
        print(i*i,end="-")
    elif i==n:
        print(i*i,end=" ")
    else:
        print(i*i,end="+")
print()
print(sum)



def add(n):
    d1=(n//1000)
    d2=(n//100)%10
    d3=(n//10)%10
    d4=n%10
    print(d1+d2+d3+d4)

if __name__=='__main__':      
    n = int(input(" enetr four digit number:"))
    if n>999 and n<=9999:
        add(n)
    else:
        print("enter four digit number only")


