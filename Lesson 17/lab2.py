class User:
    __slots__ = ("__name", "__password", "__age")

    def __init__(self, name, password, age):
        self.__name = name
        self.__password = password
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            print("Error is in type 'name'")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if isinstance(value, str):
            self.__password = value
        else:
            print("Error is in type 'password'")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self.__age = value
        else:
            print("Error is in type 'age'")


us = User("Tom", "qwerty", 34)
us.name = "Tim"
# us.name=23
# us.password=34
# us.age="asdas"
# us.lastname="Smith"
print(us.__slots__)
print(f"{us.name=}, {us.password=}, {us.age=}")
