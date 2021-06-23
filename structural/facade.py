class Paper:
    """Paper"""
    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def draw(self, text):
        if self._count > 0:
            self._count -= 1
            print(text)


class Printer:
    """Printer"""

    def print(self, paper, text):
        if paper.get_count() > 0:
            paper.draw(text)
        else:
            print(f"Paper finished")


class Facade:
    def __init__(self):
        self._printer = Printer()
        self._paper = Paper(3)

    def write(self, text):
        self._printer.print(self._paper, text)


if __name__ == "__main__":
    f = Facade()
    f.write("Hello world!")
    f.write("Hello world!")
    f.write("Hello world!")
    f.write("Hello world!")
