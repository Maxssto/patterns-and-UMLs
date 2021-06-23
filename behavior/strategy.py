from abc import ABC, abstractmethod


class Strategy(ABC):
    """Интерфейс стратегии"""

    @abstractmethod
    def make_search(self, data):
        pass


class Linear(Strategy):

    def make_search(self, data) -> str:
        return "Linear search is completed"


class Binary(Strategy):

    def make_search(self, data) -> str:
        return "Binary search is completed"


class User:
    def __init__(self, algorithm):
        self._algorithm = Strategy()
        print(f" Your algorithm is {algorithm}")

    def start_search(self, data):
        print(f"looking for {data}")
        self._algorithm.check_algorithm(self._algorithm):



if __name__ == "__main__":
    ex = [1, 2, 3]
    obj = User(),
    obj.start

    barista.take_order(20)
    barista.take_order(50)
    barista.set_strategy(BadStrategy())
    barista.take_order(40)
    barista.take_order(200)
    barista.set_strategy(GoodStrategy())
    barista.take_order(40)
    barista.set_chief_mood(ChiefMood.GOOD)
    barista.take_order(0)