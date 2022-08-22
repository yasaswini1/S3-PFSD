import math
class Perimeter_area:

    def perimeterofrectangle(self, a, b):
        d = 2 * (a + b)
        e = a * b
        print("perimeter of rectangle is", d)
        print("area of rectangle is", e)

    def perimeterofcircle(self, a):
        f = 2 * 3.17 * a
        g = 3.17 * a * a
        print("perimeter of circle is", f)
        print("area of circle is", g)

    def perimeteroftriangle(self, a, b, c):
        h = a + b + c
        s=a+b+c/2
        k = math.sqrt( s*(s-a)*(s-b)*(s-c)*0.5)
        print("perimeter of triangle", h)
        print("area of triangle", k)



obj = Perimeter_area()
obj.perimeterofrectangle(5, 10)
obj.perimeterofcircle(5)
obj.perimeteroftriangle(5, 10, 15)