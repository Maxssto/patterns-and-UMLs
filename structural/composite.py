from abc import ABC, abstractmethod


class Purchases(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Item(Purchases):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def name(self):
        return self._name

    def price(self):
        return self._price


class Box(Purchases):
    def __init__(self, name):
        self._name = name
        self._purchases = []

    def name(self):
        return self._name

    def add_purchase(self, item):
        self._purchases.append(item)

    def remove_item(self, item):
        self._purchases.remove(item)

    def price(self):
        price = 0
        for item in self._purchases:
            price += item.price()
        return price


if __name__ == "__main__":
    shirt = Item("shirt", 300)
    fruit_basket = Box("fruit basket")
    fruit_basket.add_purchase(Item("apple", 25))
    fruit_basket.add_purchase(Item("orange", 40))
    cart = Box("cart")
    cart.add_purchase(shirt)
    cart.add_purchase(fruit_basket)
    print("total price:", cart.price())