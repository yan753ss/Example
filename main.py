# Принцип единой ответственности (SRP)
# Класс Invoice отвечает только за расчёт счета.
class Invoice:
    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self):
        return self.amount + self.calculate_tax()

    def calculate_tax(self):
        return self.amount * 0.1  # 10% налог

# Класс InvoicePrinter отвечает только за печать счета.
class InvoicePrinter:
    def print_invoice(self, invoice):
        print(f"Invoice total: {invoice.calculate_total()}")

# Принцип открытости/закрытости (OCP)
# Базовый класс Shape - открытый для расширения, но закрыт для модификации.
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Принцип подстановки Лисков (LSP)
# Базовый класс и подклассы должны быть взаимозаменяемы.
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly")

# Принцип разделения интерфейсов (ISP)
# Множество специализированных интерфейсов лучше, чем один универсальный.
class Printer:
    def print_document(self):
        pass

class Scanner:
    def scan_document(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

# Принцип инверсии зависимостей (DIP)
# Классы высокого уровня (Notification) не должны зависеть от низкоуровневых (EmailService, SMSService).
# Вместо этого они оба должны зависеть от абстракции.
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailService(NotificationService):
    def send(self, message: str):
        print(f"Sending email: {message}")

class SMSService(NotificationService):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

class Notification:
    def __init__(self, service: NotificationService):
        self.service = service

    def send_notification(self, message: str):
        self.service.send(message)

# Использование:
invoice = Invoice(100)
printer = InvoicePrinter()
printer.print_invoice(invoice)

shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print(f"Area of shape: {shape.area()}")

sparrow = Sparrow()
penguin = Penguin()

sparrow.fly()  # работает
# penguin.fly()  # вызывает ошибку, но мы видим нарушение LSP

email_service = EmailService()
sms_service = SMSService()

notification = Notification(email_service)
notification.send_notification("Hello via Email!")

notification = Notification(sms_service)
notification.send_notification("Hello via SMS!")
