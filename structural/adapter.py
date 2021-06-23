class OldApp:

    def get(self, m):
        return f"{m} m"


class NewApp:

    def get(self, cm):
        return f"{cm} cm"


class Adapter(NewApp):

    def get_m(self, cm):
        return f"{cm*100} m"


if __name__ == "__main__":
    obj1 = OldApp()
    print(obj1.get(25))

    obj2 = NewApp()
    print(obj2.get(250))

    obj3 = Adapter()
    print(obj3.get(25))
