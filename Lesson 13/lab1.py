# class Point:
#     xr = 12
#     xm = 10
#
#     def __new__(cls, *args, **kwargs):
#         print("Вызов __new__" + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x, y):
#         print("Вызов __init__")
#         self.x = x
#         self.y = y
#         print(Point.xm)
#         print(f"x = {self.x}, y = {self.y}")
#
#
# # point1 = Point(1, 2)
# # Point.xm = 13
# # point2 = Point(3, 2)
#
# pt1 = Point(1, 2)
# print(pt1)


# class DataBase:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#     def connect(self):
#         print(f"Соединение с БД, {self.user}, {self.psw}, {self.port}")
#
#
# DB1 = DataBase("root", "1234", "80")
# DB1.connect()
# DB2 = DataBase("root2", "123443", "88")
# DB2.connect()
# print(DB1, DB2)


# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validata(x) and self.validata(y):
#             self.x = x
#             self.y = y
#
#     @classmethod
#     def validata(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD
#
#     @staticmethod
#     def get_square(a, b):
#         return a * b
#
#     def get_coord(self):
#         return self.x, self.y
#
#
# v1 = Vector(-10, 100)
# print(Vector.validata(6))
# print(v1.validata(-5))
# print(v1.get_coord())
# print(Vector.get_square(10, 15))


class Review:
    MAX_LEN = 500

    def __init__(self, author, text, phone_num):
        self.author = author
        self.phone_num = phone_num
        if self.validata(text):
            self.text = text
        else:
            self.text = text[:500]

    @classmethod
    def validata(cls, arg):
        return len(arg) <= cls.MAX_LEN

    @staticmethod
    def lower_letters(text):
        return text.lower()


author = "Iam"
text = '''"Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
    'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, '
    "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
    "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "
    "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
    "and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. "
    "Why do we use it? It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. "
    "The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, "
    "as opposed to using 'Content here, content here', making it look like readable English. "
    "Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, "
    "and a search for 'lorem ipsum' will uncover many web sites still in their infancy. "
    "Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
    "Where does it come from? Contrary to popular belief, Lorem Ipsum is not simply random text. "
    "It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. "
    "Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, "
    "consectetur, from a Lorem Ipsum passage, and going through the cites of the word in clas"'''
phone_num = 89232323423
lorem = Review(author,text,phone_num)
print(lorem.validata(text))
print(Review.lower_letters(text))
print(lorem.text)
