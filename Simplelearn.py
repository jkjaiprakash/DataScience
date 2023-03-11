##class gun:
##    def fun(a,b):
##        print(a,"scores",b,"runs")
##gun.fun("dhoni",100)

##class new:
##    var=10
##print(new.var)

#Class is an way or a procedure or a blue print to create a object because python is an object oriented programming language
#Class is an group of related statement that can perform any specific task
#It can be only executed only when we call by its name 

#Bounded and Unbounded

#Adavntage
#Code reusability
#Compact
#Secure
#Better undersatndabilty

##class fun:
##    def add(a,b):
##        print(a+b)
##fun.add(10,20)        

##class fun:
##    def add(a,b):
##        print(a+b)
##    def add():
##        print("Success")
##fun.add(10,20)

##class fun:
##    def add(a,b):
##        print(a+b)
##    def __add():
##        print("Success")
##fun.add(10,20)

##new=10
##class nxt:
##    global new
##    new=20
##    def fun(a,b):
##        print("Success")
##        print(a+b)
##nxt.fun(100,200)
##print(new)
##print(nxt.new)

##class calc:
##    def add(a,b):
##        print(a+b)
##    def sub(a,b):
##        print(a-b)
##    def div(a,b):
##        print(a/b)
##    def mul(a,b):
##        print(a*b)
##calc.add(10,20)
##calc.sub(10,20)
##calc.mul(10,20)
##calc.div(10,20)

##class old:
##    def fun(a,b):
##        print(a+b)
##class new(old):
##    def fun1():
##        print("Success")
##new.fun(10,20)

##class a:
##    def fun():
##        print('a')
##class b(a):
##    def fun():
##        print('b')
##class c(b,a):
##    def fun():
##        print('c')
##class d(c,b):
##    def fun():
##        print('d')
##d.fun()

##class a:
##    def fun():
##        print('a')
##class b(a):
##    def fun():
##        print('b')
##class c(b,a):
##    def fun():
##        print('c')
##class d(c,b):
##    def fun():
##        pass
##d.fun()

##class a:
##    def fun():
##        print('a')
##class b(a):
##    def fun():
##        print('b')
##class c(b,a):
##    def fun():
##        print('c')
##class d(c,b):
##    def fun1():
##        print("d")
##d.fun()

##class a:
##    def fun():
##        print('a')
##class b(a):
##    def fun():
##        print('b')
##class c(b,a):
##    def fun():
##        print('c')
##class d(b,a):
##    def fun():
##        pass
##d.fun()

##class New:
##    def fun(ip,pwd):
##        print(ip,pwd)
##    def fun1(ip,pwd,code):
##        print(ip,pwd,code)
##New.fun("127.0.0.0","@124")
##New.fun1("127.0.0.0","@124","ipconfiq")
##
##class New:
##    def __init__(self,ip,pwd):
##        self.a=ip
##        self.b=pwd
##    def fun(self):
##        print(self.a,self.b)
##    def fun1(self,code):
##        print(self.a,self.b,code)
##c=New("127.0.0.0","@124")
##c.fun()
##c.fun1("ipconfiq")


##class old:
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun(self):
##        print(self.a,self.b)
##class new(old):
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun1(self):
##        print(self.a,self.b)
##c=new("dhoni","40")
##c.fun()
##c.fun1()

##class old:
##    def __init__(self,name,age):
##        self.a1=name
##        self.b2=age
##    def fun(self):
##        print(self.a1,self.b2)
##class new(old):
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun1(self):
##        print(self.a,self.b)
##c=new("dhoni","40")
##c.fun()
##c.fun1()

##class old:
##    def __init__(self,name,age):
##        self.a1=name
##        self.b2=age
##    def fun(self):
##        print(self.a1,self.b2)
##class new(old):
##    def __init__(self,name,age):
##        old.__init__(self,name,age)
##        self.a=name
##        self.b=age
##    def fun1(self):
##        print(self.a,self.b)
##c=new("dhoni","40")
##c.fun()
##c.fun1()

##class fun():
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def add(self):
##        print(self.a+self.b)
##    @staticmethod 
##    def mul(a,b):
##        print(a*b)
##    @classmethod
##    def sub(cls,a,b):
##        a-b
##        return cls(a,b)
##c=fun(10,20)
##c.mul(10,20)
##c.add()
##print(d=fun.sub(20,10))

##class new:
##    def __init__(self,name,age):
##        self.name=name
##        self.__age=age
##    def fun(self):
##        print(self.name,self.age)
##c=new("dhoni",40)
##c.fun()
##print(c.name)
##print(c.age)
##c.age=40
##c.fun()

##class old:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def fun(self):
##        print(self.name,self.__age)
##    def upd(self,age):
##        self.__age=age
##    def get(self,age):
##        print(self.__age)
##c=old("dhoni",40)
##c.fun()
##c.upd(100)
##c.get()

class apple:
    def type(self):
        print("fruits")
    def color(self):
        print("red")
class tomato:
    def type(self):
        print("Veg")
    def color(self):
        print("red")
def fun(obj):
    obj.type()
    obj.color()
c=apple()
d=tomato()
fun(c)
fun(d)


    
