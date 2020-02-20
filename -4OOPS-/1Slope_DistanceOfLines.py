# Slope of the line and the distance between two points on a line

class Line():

    def __init__(self,coord1,coord2):
        self.coord1=coord1
        self.coord2=coord2

    def slope(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return ((y2-y1)/(x2-x1))

    def distance(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return (((x2-x1)**2)+((y2-y1)**2))**0.5
x1=int(input("Enter the x1-coordinate: "))
y1=int(input("Enter the y1-coordinate: "))
x2=int(input("Enter the x2-coordinate: "))
y2=int(input("Enter the y2-coordinate: "))
c1=(x1,y1)
c2=(x2,y2)
ln=Line(c1,c2)
print('The slope of the given line: {}'.format(ln.slope()))
print('The distance of the points on the line: {}'.format(ln.distance()))
