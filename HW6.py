class shapes:
    def _init_(self, s):
        self.sides = s

    def area(self):
        if self.sides == triangle:
            print(self.sides, "1/2 * b * h")
        elif self.sides == square:
            print(self.sides, "a ^ 2")
        elif self.sides == rectangle:
            print(self.sides, "w * l")
        elif self.sides == circle:
            print(self.sides, "3.14 * r ^ 2")

    def perimeter(self):
        if self.sides == triangle:
            print(self.sides, "a + b + c")
        elif self.sides == square:
            print(self.sides, "4 * a")
        elif self.sides == rectangle:
            print(self.sides, "2(l + w)")
        elif self.sides == circle:
            print(self.sides, "2 * 3.14 * r")

square = shapes("squares")
square.area()
square.perimeter()

triangle = shapes("triangles")
triangle.area()
triangle.perimeter()

rectangle = shapes("rectangles")
rectangle.area()
rectangle.perimeter()

circle = shapes("circles")
circle.area()
circle.perimeter()
