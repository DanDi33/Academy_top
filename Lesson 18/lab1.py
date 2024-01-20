class Anton:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        if name != "Антон":
            print(f"Я не {name}. Я - Антон")
            self.name = "Антон"
        else:
            self.name = name
        self.age = age

    def __str__(self):
        return f"Я - {self.name}. Мне {self.age}"


an = Anton("Fedya", 33)
print(an)
