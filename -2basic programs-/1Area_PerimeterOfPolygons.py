P = input("What's the polygon you want to measure: ")
print('1 is Area')
print('2 is Perimeter/Circumference')
if P=='square' or P=='Square':
    S = float(input("Area or Perimeter : "))
    if S == 1:
        side = float(input("side of the square: "))
        area = side*side
        area_of_square = float(area)
        print("The area of the Square -> {}".format(area_of_square))
    elif S == 2:
        side = float(input("side of the square: "))
        perimeter = 4*side
        perimeter_of_square = float(perimeter)
        print("The perimeter of the Square -> {}".format(perimeter_of_square))
    else:
        print("Choose the appropriate option")
elif P=='triangle' or P=='Triangle':
    T = float(input("Area or Perimeter : "))
    if T == 1:
        base = float(input("Base of the triangle: "))
        height = float(input("Height of the triangle: "))
        area = (1/2)*base*height
        area_of_triangle = float(area)
        print("The area of the triange -> {}".format(area_of_triangle))
    elif T == 2:
        a = float(input("base of the triangle: "))
        b = float(input("one side of the triangle: "))
        c = float(input("other side of the triangle: "))
        perimeter = a+b+c
        perimeter_of_square = float(perimeter)
        print("The perimeter of the triangle -> {}".format(perimeter_of_square))
    else:
        print("Choose the appropriate option")
elif P=='Circle' or P=='circle':
    C = float(input("Area or Circumference : "))
    if C == 1:
        radius = float(input("Enter the radius of circle: "))
        area = 3.14*radius*radius
        area_of_circle = float(area)
        print("The area of the Cirlce -> {}".format(area_of_circle))
    elif C == 2:
        radius = float(input("Enter the radius of circle: "))
        c = 2*3.14*radius
        circumference_of_circle = float(c)
        print("The circumference of the Circle -> {}".format(circumference_of_circle))
    else:
        print("Choose the appropriate option")
else:
    print("ONLY AVAILABLE OPTIONS TO BE ENTERED")
