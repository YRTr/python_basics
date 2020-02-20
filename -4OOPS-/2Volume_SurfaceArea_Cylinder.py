#Calculate the Volume and SurfaceArea of a cylinder
class Cylinder():
    pi=3.14
    def __init__(self,radius=1,height=1):
        self.radius=radius
        self.height=height

    def Volume(self):
        return Cylinder.pi * (self.radius)**2 * self.height

    def SurfaceArea(self):
        top = self.pi * (self.radius)**2
        return (2*top) + (2 * self.pi * self.radius * self.height)

r = float(input("Enter the radius of surfaces: "))
h = float(input("Enter the height of surfaces: "))
cy=Cylinder(r,h)
print("The Volume of the Cylinder: {}".format(cy.Volume()))
print("The SurfaceArea of the Cylinder: {}".format(cy.SurfaceArea()))
