def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
v=sum(1,2,3,4,4,7)
print(v)
 

class product:
    def user(self):
        self.name= input("enter product name:")
        self.price =int(input("product price:"))
    def display(self):
        print("product name:",self.name)
        print("product price:",self.price)
a= product()
b=product()
a.user()
b.user()
print("----------------")
print("product 1")
a.display()
print("----------------")
print("product 2")
b.display()


from abc import ABC,abstractmethod
class Bsec(ABC):
    @abstractmethod
    def hyd(self):
        pass
class durga(Bsec):
    def hyd(self):
        print("navya--go or not go! tell me durga fastly")
o=durga()
o.hyd()
class navya(Bsec):
    def hyd(self):
        print("makante pandaga ledhu prends ! miraina pandaga cheskondi prends")
o=navya()
o.hyd()






