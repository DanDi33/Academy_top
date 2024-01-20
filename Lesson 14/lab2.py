class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть Int")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f"__set__: {self.name} = {value} , {instance}")
        instance.__dict__[self.name] = value

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        # self.verify_coord(x)
        # self.verify_coord(y)
        # self.verify_coord(z)

        # self._x = x
        # self._y = y
        # self._z = z
        self.x = x
        self.y = y
        self.z = z

    # @property
    # def x(self):
    #     print("Произошёл вызов Х")
    #     return self._x
    #
    # @x.setter
    # def x(self, coord):
    #     print("Установка значения для Х")
    #     self.verify_coord(coord)
    #     self._x = coord

    # @classmethod
    # def verify_coord(cls, coord):
    #     if type(coord) != int:
    #         raise TypeError("Координата должна быть Int")


pt1 = Point3D(1, 2, 3)
# print(Point3D.__dict__)
print(pt1.__dict__)
print(pt1.x)

