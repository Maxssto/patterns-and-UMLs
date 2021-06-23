from __future__ import annotations
from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ComponentA(Component):

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_component_a(self)

    def exclusive_method_of_component_a(self) -> str:
        return "A"


class ComponentB(Component):

    def accept(self, visitor: Visitor):
        visitor.visit_component_b(self)

    def special_method_of_component_b(self) -> str:
        return "B"


class Visitor(ABC):
    """
    Интерфейс Посетителя объявляет набор методов посещения, соответствующих
    классам компонентов. Сигнатура метода посещения позволяет посетителю
    определить конкретный класс компонента, с которым он имеет дело.
    """

    @abstractmethod
    def visit_component_a(self, element: ComponentA) -> None:
        pass

    @abstractmethod
    def visit_component_b(self, element: ComponentB) -> None:
        pass


class Visitor1(Visitor):
    def visit_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_component_a()} + Visitor1")

    def visit_component_b(self, element) -> None:
        print(f"{element.special_method_of_component_b()} + Visitor1")


class Visitor2(Visitor):
    def visit_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_component_a()} + Visitor2")

    def visit_component_b(self, element) -> None:
        print(f"{element.special_method_of_component_b()} + Visitor2")


if __name__ == "__main__":

    def client_code(components, visitor: Visitor) -> None:
        for component in components:
            component.accept(visitor)

    components = [ComponentA(), ComponentB()]

    visitor1 = Visitor1()
    client_code(components, visitor1)

    print("It allows the same client code to work with different types of visitors:")
    visitor2 = Visitor2()
    client_code(components, visitor2)