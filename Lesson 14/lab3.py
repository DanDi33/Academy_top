from pprint import pprint


class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Кошка - имя {self.name}"

    # def info(self):
    #     print("Кошка - имя ", self.name)


# cat = Cat("Мурка")
# # cat.info()
# # print(cat.__dict__)
# print(cat)

class Market:
    def __init__(self):
        self.gods = []

    def append(self, dict):
        self.gods.append(dict)

    def show(self):
        pprint(self.gods)

    def __len__(self):
        return len(self.gods)


shop = Market()
shop.append({"Товар1": 1})
shop.append({"Товар2": 3})
shop.append({"Товар3": 7})
shop.append({"Товар4": 9})
shop.show()
print(len(shop))
