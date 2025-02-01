def fun1(l):
    def fun2(l):
        return len(l)
    return fun2(l)

if __name__=='__main__':
    l=[1,2,3,4,5,6,7]
    print(fun1(l))
                                                                                  














 