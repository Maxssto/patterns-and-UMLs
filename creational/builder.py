from abc import ABC, abstractmethod


class Product(ABC):
    @property
    @abstractmethod
    def name(self):
        pass


class Sushi(Product):
    @property
    def name(self):
        return "Sushi"


class Burger(Product):
    @property
    def name(self):
        return "Burger"


class OrderBuilder(ABC):
    @abstractmethod
    def pack(self):
        pass

    @abstractmethod
    def add_gloves(self):
        pass

    @abstractmethod
    def get_ready_order(self):
        pass


class SushiOrderBuilder(OrderBuilder):
    def pack(self):
        print("Packing sushi")

    def add_gloves(self):
        pass

    def get_ready_order(self):
        return Sushi()


class BurgerOrderBuilder(OrderBuilder):
    def pack(self):
        print("Packing burger")

    def add_gloves(self):
        print("Gloves added")

    def get_ready_order(self):
        return Sushi()


class Director:
    def __init__(self, order_builder):
        self.order_builder = order_builder

    def pack_sushi(self):
        self.order_builder.pack()
        self.order_builder.get_ready_order()
        return self.order_builder.get_ready_order()

    def pack_burger(self):
        self.order_builder.pack()
        self.order_builder.add_gloves()
        self.order_builder.get_ready_order()
        return self.order_builder.get_ready_order()


if __name__ == "__main__":
    print("Client ordered sushi")
    packer = Director(SushiOrderBuilder())
    order = packer.pack_sushi()
    print(f"{order.name} is ready!\n")

    print("Client ordered burger")
    packer = Director(BurgerOrderBuilder())
    order = packer.pack_burger()
    print(f"{order.name} is ready!")