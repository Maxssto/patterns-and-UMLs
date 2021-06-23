from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice

class Subject(ABC):
    """Интферфейс издателя объявляет набор методов для управлениями подписчиками."""

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Присоединяет наблюдателя к издателю."""
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Отсоединяет наблюдателя от издателя."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Уведомляет всех наблюдателей о событии."""
        pass


class ConcreteSubject(Subject):
    """Издатель владеет некоторым важным состоянием и оповещает наблюдателей о его изменениях."""

    _state = None
    """Для удобства в этой переменной хранится состояние Издателя, необходимое всем подписчикам."""

    _observers = []
    """Список подписчиков."""

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print("\nUser was removed")
        self._observers.remove(observer)

    """Методы управления подпиской."""

    def notify(self) -> None:
        """Запуск обновления в каждом подписчике."""

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def change_state(self) -> None:

        print("\nSubject: I'm doing something important.")
        self._state = choice(["User1", "User2"])

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """Интерфейс Наблюдателя объявляет метод уведомления, который издатели используют для оповещения своих
    подписчиков. """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """Получить обновление от субъекта."""
        pass


"""
Конкретные Наблюдатели реагируют на обновления, выпущенные Издателем, к которому
они прикреплены.
"""


class User1(Observer):
    def update(self, subject: Subject) -> None:
        if "User1" in subject._state:
            print("Notification for User1")


class User2(Observer):
    def update(self, subject: Subject) -> None:
        if "User2" in subject._state:
            print("Notification for User2")


if __name__ == "__main__":
    subject = ConcreteSubject()
    user1 = User1()
    user2 = User2()
    subject.attach(user1)
    subject.attach(user2)
    subject.change_state()
    subject.change_state()
    subject.detach(user1)
    subject.change_state()
