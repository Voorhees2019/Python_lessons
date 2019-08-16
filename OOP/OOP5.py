class Shape():

    def __init__(self):  # эти методы наследники обязаны переопределить, а то при вызове их из отцовского класса
        raise NotImplementedError("Can't instantiate an abstract class")  # произойдет ошибка

    def draw(self):
        raise NotImplementedError("Can't instantiate an abstract class")

    def area(self):
        raise NotImplementedError("Can't instantiate an abstract class")

    def perimeter(self):
        raise NotImplementedError("Can't instantiate an abstract class")


class Rectangle(Shape):

    def __init__(self, width, height):
        #Shape.__init__(self)

        self.width = width
        self.height = height
        print('Rectangle created')
        #Shape.area(self)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)

    def draw(self):
        print(f'Drawing rectangle with width {self.width} and height {self.height}')


rect = Rectangle(10, 15)
print(rect.area())


class Triangle(Shape):

    def __init__(self, a, b, c):
        #Shape.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        print('Triangle created')

    def draw(self):
        print(f'Drawing triangle with sides: {self.a}, {self.b}, {self.c}')

    def area(self):
        s = (self.a + self.b + self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**(1/2)

    def perimeter(self):
        return self.a + self.b + self.c


triangle = Triangle(10, 10, 10)
print(triangle.perimeter())
print(triangle.area())
print('--------------------------------------')
for shape in [triangle, rect]:
    shape.draw()


