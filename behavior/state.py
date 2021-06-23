from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, document):
        self.document = document

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def publish(self):
        pass


class Draft(State):
    def render(self):
        print("You can change your document")

    def publish(self):
        self.document.state = Moderation(self.document)


class Moderation(State):
    def render(self):
        pass

    def publish(self):
        user = input("User: ")
        if user == "admin":
            self.document.state = Published(self.document)
        else:
            print("You can't publish documents")


class Published(State):
    def render(self):
        pass

    def publish(self):
        pass


class Document:

    def __init__(self):
        self.state: State = Draft(self)

    def moderate(self):
        self.state.publish()

    def publish(self):
        self.state.publish()

    def show_state(self):
        print(f"{self.state}")


if __name__ == "__main__":
    doc = Document()
    doc.show_state()
    doc.moderate()
    doc.show_state()
    doc.publish()
    doc.show_state()
