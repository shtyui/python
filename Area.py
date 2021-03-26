import math
class G():
    def __init__(self):
        self.color=" "
        self.shape=" "
    def getColor(self):
        if self.shape=="circle":
            self.color="Green"
        if self.shape=="square":
            self.color="Red"
        return self.color
class Circle(G):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
        self.shape="circle"
    def getRadius(self):
        return self.radius
    def setRadius(self,radius):
        self.radius=radius
    def getDiameter(self):
        return self.radius*2
    def getPerimeter(self):
        return self.radius*2*math.pi
    def getArea(self):
        return (self.radius**2)*math.pi
class Square(G):
    def __init__(self,lenght):
        super().__init__()
        self.shape="square"
        self.lenght=lenght
    def getLenght(self):
        return self.lenght
    def getBoundary(self):
        return self.lenght*4
    def getDiagonal(self):
        return self.lenght*1.414
    def getArea(self):
        return self.lenght*self.lenght
A=Circle(5)
print("圓形的顏色 : ",A.getColor())
print("圓形的半徑 : ",A.getRadius())
print("圓形的直徑 : ",A.getDiameter())
print("圓形的圓周 : ",A.getPerimeter())
print("圓形的面積 : ",A.getArea())
B=Square(10)
print("正方形的顏色 : ",B.getColor())
print("正方形的邊長 : ",B.getLenght())
print("正方形的對角線長 : ",B.getDiagonal())
print("正方形的周長 : ",B.getBoundary())
print("正方形的面積 : ",B.getArea())

            