class User:
    def __init__(self, name):
        self.name = name  # public attribute


u = User("Иван")
print(u.name)  # public attribute


class UserProtected:
    def __init__(self, name):
        self._name = name  # agreed on to be protected


u = UserProtected("Иван")
print(u._name)  # technically accessable, but not advised


class UserPrivate:
    def __init__(self, name):
        self.__name = name  # private


u = UserPrivate("Иван")
# print(u.__name)  # AttributeError
print(u._UserPrivate__name)  # accessing attribute via name mangling


class UserProperty:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):  # getter
        return self.__name

    @name.setter
    def name(self, value):  # setter
        if not value:
            raise ValueError("Имя не может быть пустым")
        self.__name = value


user = UserProperty("Ivan")
user.name("Jack")
print(user.name)
