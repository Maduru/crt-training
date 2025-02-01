c = int(input("enter the count of numbers"))
for i in range(c):
     num =int(input("enter {} number".format(i+1)))
     if num%2==0:
          print("even")
     else:
          print("odd")
          