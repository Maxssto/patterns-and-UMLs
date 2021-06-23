from abc import ABC, abstractmethod


class IUser(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def login(self):
        pass


class User(IUser):

    def login(self):
        print(f"You are in system {self._name}!")


class ProxyUser(IUser):
    def __init__(self, name):
        super().__init__(name)
        self._user = User(self._name)

    def login(self):
        if self._user._name == "admin":
            print("Welcome admin")
        else:
            self._user.login()


if __name__ == "__main__":
    user1 = User("Max")
    user1.login()
    user2 = ProxyUser("admin")
    user2.login()
    