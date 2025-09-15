class Geometry:

    def __init__(self , x , y):
        self.x=x
        self.y=y

    def __str__(self):
        return "<{},{}>".format(self.x,self.y)

    def euclidenDistance(self,other):
        return ((other.x-self.x)**2 + (other.x-self.y)**2)**0.5


    def distanceFromOrigin(self):
        return self.euclidenDistance(Geometry(0,0))

class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C


    def __str__(self):
        return "{}x+{}y+{}=0".format(self.A,self.B,self.C)


    def checkPointLieOnLine(self,point):
        if self.A*point.x + self.B*point.y + self.C == 0:
            return "1"
        else:
            return "No"


    def shortestDistance(line,point):
        return abs(  (line.A*point.x + line.B*point.y + line.C ) / (line.A**2 + line.B ** 2))   



c1 = Geometry(0,0)
c2 = Geometry(20,20)

l1 = Line(10,20,30)
print(l1 , c2)

print("sd is" ,l1.shortestDistance(c1))

print(l1.checkPointLieOnLine(c2))

# print(c1.euclidenDistance(c2))
# print(c1.distanceFromOrigin())




