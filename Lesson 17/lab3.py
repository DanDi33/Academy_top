class Point2D:
    __slots__ = ("_x", "_y", "_length")

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._length = (self._x * self._x + self._y * self._y) * 0.5

    def calc_length(self):
        self._length = (self._x * self._x + self._y * self._y) * 0.5

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            self._x = value
            self.calc_length()

        else:
            print("Error")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            self._y = value
            self.calc_length()
        else:
            print("Error")

    @property
    def length(self):
        return self._length


# pt = Point2D(1, 2)
# print(pt.x)
# pt.x = 8
# print(pt.length)


class Point3D(Point2D):
    __slots__ = "__z"

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z
        self._length = (self._x * self._x + self._y * self._y + self.__z * self.__z) * 0.5

    def calc_length(self):
        self._length = (self._x * self._x + self._y * self._y + self.__z * self.__z) * 0.5

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        if isinstance(value, int):
            self.__z = value
            self.calc_length()
        else:
            print("Error")


pt3 = Point3D(1, 2, 3)
# pt3.z = 2
# pt3.j = 1
# print(pt3.__dict__)
# print(pt3.__slots__)
print(pt3.length)
pt3.z = 4
print(pt3.length)
