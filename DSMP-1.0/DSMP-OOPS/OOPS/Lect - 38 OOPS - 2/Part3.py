class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    
p1 = Person("Vinod" , "Male")
p2 = Person("Barr" , "Male")

l=[p1,p2]
s={p1,p2}
for i in l:
    print (i.name , i.gender)

print("\n")

for i in s:
    print (i.name , i.gender)