from abc import ABC, abstractmethod


class IAlgorithm(ABC):
    def template_method(self):
        self.step1()
        self.step2()
        self.step3()

    def step1(self):
        print("First step is the same for everybody")

    @abstractmethod
    def step2(self):
        pass

    def step3(self):
        print("Algorithm is finished")


class Algorithm1(IAlgorithm):

    def step2(self):
        print("Second step is special for Algorithm1")


class Algorithm2(IAlgorithm):

    def step2(self):
        print("Second step is special for Algorithm2")


if __name__ == "__main__":
    a1 = Algorithm1()
    a2 = Algorithm2()
    a1.template_method()
    print("---------------------------------")
    a2.template_method()