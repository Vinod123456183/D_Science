class Person:
    def __init__(self):
        self.name="vinod"
        self.age=10
    
Person()


class Person2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
# Outside class
def greet(p):
    print(id(p))
    print("name",p.name , "age",p.age)
    return p

p = Person2("Vin" , 10)
print(id(p))
p1 = greet(p)
greet(p)
print(id(p))
