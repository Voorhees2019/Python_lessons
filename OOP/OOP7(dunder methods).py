class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point x={self.x}, y={self.y}'


p = Point(4, 5)
print(p)
print('----------------------------------')


class Road():

    def __init__(self, length):
        self.length = length

    def __len__(self):
        return self.length

    def __str__(self):
        return f'A road of length:{self.length}'

    def __del__(self):
        return f'The road has been destroyed'


r = Road(1000)
print(len(r))
print(r)
del r
print(r)  # NameError: name 'r' is not defined

