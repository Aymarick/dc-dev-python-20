class Point:
    pointCount = 0
    def __init__(self):
        self.x = 0
        self.y = 0
        Point.pointCount = Point.pointCount + 1

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY

    def print(self):
        print("x="+ str(self.x)+",y="+ str(self.y))

class Point3D(Point):
    def __init__(self):
        Point.__init__(self)
        self.z = 0
        
    def move(self, deltaX, deltaY, deltaZ):
        Point.move(self, deltaX, deltaY)
        self.z = self.z + deltaZ

    def print(self):
        print("x="+ str(self.x)+",y="+ str(self.y) + ",z="+str(self.z))


pointA = Point()
pointB = Point3D()
pointA.move(2, 3)
pointB.move(-4, 10, 5)
pointA.print()
pointB.print()

print("Nombre de points : "+str(Point.pointCount))
