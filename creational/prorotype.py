from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Person(Prototype):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} {self.age}")

    def clone(self):
        return type(self)(self.name, self.age)


if __name__ == "__main__":
    p1 = Person("Max", 20)
    p2 = copy.deepcopy(p1)
    p3 = p1.clone()
    p2.age = 26
    p3.name = "Bob"
    p1.info()
    p2.info()
    p3.info()
