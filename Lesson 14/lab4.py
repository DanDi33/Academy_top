class Clock:
    def __init__(self, seconds: int):
        if isinstance(seconds, int):
            self.seconds = seconds
        else:
            raise TypeError("Секунды должны быть INT")

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"

    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("С Int складываем только Int и Clock")
        sc = other if(isinstance(other, int)) else other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other


c1 = Clock(1021)
print(c1.__dict__)
print(c1.get_time())
c2 = c1 + 60
print(c2.get_time())
c3 = c1 + c2
print(c3.get_time())
