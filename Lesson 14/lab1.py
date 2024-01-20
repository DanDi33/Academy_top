class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.z = 0

    def __getattribute__(self, item):
        if item == "_Point__x":
            raise ValueError("Private attribute")
        print("__getattribute__", item)
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z" and value<0:
            raise ValueError("число должно быть больше 0")
        print("__setattr__", key, value)
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        if item == "c":
            raise AttributeError("Метод изменился,  смотри документацию")
        print("__getattr__")
        raise AttributeError("Такого метода нет")
    def set_coord(self, x, y):
        self.x = x
        self.y = y


pt1 = Point(1, 2)
# print(pt1.__dict__)
# print(pt1._Point__x)
pt1.z = 343
print(pt1.c)
print(pt1.z)
