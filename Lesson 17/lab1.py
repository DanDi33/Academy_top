import timeit


class Point2D:
    __slots__ = ("__x", "y")  # Ограничение атрибутов класса

    def __init__(self, x, y):
        self.__x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    def input_data(self):
        self.__x = input()
        self.y = input()

    def __str__(self):  # С помощью str можем принтовать объект просто по названию
        return f"{self.x=}, {self.y=}"

    def calc(self):
        self.__x += 1
        del self.y
        self.y = 0


class Point2_copy:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def append_z(self, value):
        self.z = value

    def input_data(self):
        self.x = input()
        self.y = input()

    def __str__(self):  # С помощью str можем принтовать объект просто по названию
        return f"{self.x=}, {self.y=}"

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


pt = Point2D(1, 2)
pt2 = Point2_copy(13, 42)
# pt.z = 4
del pt.y
pt.y = 3
print(pt.y)
print(pt.__slots__)
print(pt)
pt.calc()
print(pt)
print(pt, pt2)

t1 = timeit.timeit(pt.calc)
t2 = timeit.timeit(pt2.calc)

print(t1, "()", t2)
pt2.append_z(123)
print(pt2.__dict__)
