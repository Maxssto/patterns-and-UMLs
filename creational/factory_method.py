from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self):
        pass


class WindowsButton(Button):
    def __init__(self):
        self.name = "Windows button"

    def render(self):
        print("Windows button created")

    def onClick(self):
        print("You've clicked on Windows button")


class IOSButton(Button):
    def __init__(self):
        self.name = "IOS button"

    def render(self):
        print("IOS button created")

    def onClick(self):
        print("You've clicked on IOS button")


class ButtonFactory:

    @staticmethod
    def build_button(oc):
        if oc == "Windows":
            return WindowsButton()
        if oc == "IOS":
            return IOSButton()
        else:
            print("Incorrect System!")


choice = input("What is your system: ")
button = ButtonFactory.build_button(choice)
button.render()
button.onClick()