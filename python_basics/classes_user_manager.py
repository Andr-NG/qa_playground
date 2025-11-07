# Создай два класса:

# User — у пользователя есть id, name, email, is_active.
# UserManager — управляет списком пользователей.
# Методы UserManager:
# add_user(user) — добавить пользователя.
# deactivate_user(user_id) — отключить пользователя.
# get_active_users() — вернуть всех активных.
# find_by_email(email) — найти пользователя по email.
# Нужно продумать, как проверять уникальность email при добавлении.


class User:

    def __init__(self, id: str, name: str, email: str, is_active: bool = True):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_active

    def __repr__(self):
        return f"User {self.name}"


class UserManager:

    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        if not isinstance(user, User):
            raise TypeError("Wrong user type")

        if all(user.email != u.email and user.id != u.id for u in self.users):
            self.users.append(user)
            print(f"{user} added")
        else:
            raise ValueError("Something went wrong while adding a user")

    def deactivate_user(self, user_id):
        for user in self.users:
            if user_id == user.id:
                user.is_active = False
                print(f"User {user.name} deactivated")
                break
        else:
            print(f"No such User {user_id} found")

    def get_active_users(self):

        active_users = [user.__str__() for user in self.users if user.is_active is True]

        if not active_users:
            return "No active users"

        return active_users

    def find_by_email(self, email):

        for user in self.users:
            if email == user.email:
                return user
        return None


user_1 = User(1, "Andrey", "andrey@mail.com")
user_2 = User(2, "Jenna", "jenna@mail.com")
user_3 = User(3, "Jenna", "jenna@mail.com")

user_list = UserManager()

user_list.add_user(user_1)
user_list.add_user(user_2)
user_list.deactivate_user(user_id=1)
print(user_list.get_active_users())
print(user_list.find_by_email("andrey@mail.com"))
