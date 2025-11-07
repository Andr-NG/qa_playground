# Создай базовый класс Notification и подклассы EmailNotification, SMSNotification.

# Требования:
# У каждого класса есть метод send() (у базового — абстрактный).
# Класс EmailNotification принимает email, subject, body.
# Класс SMSNotification принимает phone, message.
# При вызове send() выводит сообщение в консоль:
# "Sending email to user@example.com: Subject: Hello"
# "Sending SMS to +123456789: Your code is 1234"


# Нельзя создать объект класса, пока не будут реализованы все методы родительского класса
from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotification(Notification):

    def __init__(self, email: str, subject: str, body: str):
        self.email = email
        self.subject = subject
        self.body = body

    def send(self):
        print(f"Sending email to {self.email}: {self.subject}: {self.body}")


email = EmailNotification("mailer@mail.com", "WARNING", "GO TO HELLL!!")
email.send()
