from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self):
        pass


class TextBox(ABC):

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def edit(self):
        pass


class WindowsTextBox(TextBox):
    def __init__(self):
        self.name = "Windows TextBox"

    def render(self):
        print("Windows TextBox created")

    def edit(self):
        print("You've edited Windows TextBox")


class IOSTextBox(TextBox):
    def __init__(self):
        self.name = "IOS TextBox"

    def render(self):
        print("IOS TextBox created")

    def edit(self):
        print("You've edited IOS TextBox")


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


class GUIFactory(ABC):

    @abstractmethod
    def build_button(self):
        pass

    @abstractmethod
    def build_textbox(self):
        pass


class IOSFactory(GUIFactory):

    def build_button(self):
        return IOSButton()

    def build_textbox(self):
        return IOSTextBox()


class WindowsFactory(GUIFactory):
    def build_button(self):
        return WindowsButton()

    def build_textbox(self):
        return WindowsTextBox()


class App:

    @staticmethod
    def os(os):
        if os == "Windows":
            return WindowsFactory()
        if os == "IOS":
            return IOSFactory()
        else:
            print("Incorrect System!")


choice = input("What is your system: ")
button = App().os(choice)
button.build_button().onClick()
textbox = App().os(choice)
textbox.build_textbox().edit()
