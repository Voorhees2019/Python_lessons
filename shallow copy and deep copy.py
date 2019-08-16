import copy
list1 = [1, 2, 3, [4, 5, 6]]
copied_list = list1.copy()  # copy the object address
copied_list[3].append(7)
print(list1)        # the same!
print(copied_list)  # the same!
list1.append(8)
print(list1)        # [1, 2, 3, [4, 5, 6, 7], 8]
print(copied_list)  # [1, 2, 3, [4, 5, 6, 7]]

shallow_copy = copy.copy(list1)
deep_copy = copy.deepcopy(list1)
deep_copy[3].append(9)
print(list1)
print(deep_copy)


class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


a = Point(1, 2)
b = copy.copy(a)
a.x = 3
print(a)  # Point(3, 2). Integer is not changeable type
print(b)  # Point(1, 2)
print('-------------')


class Line():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __copy__(self):
        cls = self.__class__  # get class data
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memodict={}):
        cls = self.__class__
        result = cls.__new__(cls)
        memodict[id(self)] = result  # to avoid problems with infinitely copying
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memodict))
        return result


print('==copy.copy==')
l1 = Line(a, b)
l2 = copy.copy(l1)
print(l1.p1)
print(l2.p1)
l1.p1.x = 4
print('l1.p1.x = 4')
print(l1.p1)
print(l2.p1)

print('==copy.deep_copy==')
l1 = Line(a, b)
l2 = copy.deepcopy(l1)
print(l1.p1)
print(l2.p1)
l1.p1.x = 5
print('l1.p1.x = 5')
print(l1.p1)
print(l2.p1)
