'''Write the abstract class PaymentMethod , the concrete classes CreditCardPayment
and PayPalPayment , and the code to demonstrate polymorphism.'''
from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self):
        pass
class CreditCardPayment(PaymentMethod):
    def processPayment(self):
        print("Credit Card payment method being processed")
class PayPalPayment(PaymentMethod):
    def processPayment(self):
        print("PayPalPayment method being processed")
payments = [CreditCardPayment(), PayPalPayment()]

for payment in payments:
    payment.processPayment()
    