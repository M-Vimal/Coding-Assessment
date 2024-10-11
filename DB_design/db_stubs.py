from datetime import datetime
from enum import Enum
from typing import List

class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.orders = []

    def create_order(self, order_details):
        order = Order(self, order_details)
        self.orders.append(order)

    def view_orders(self):
        return self.orders

class OrderStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    SHIPPED = "Shipped"
    CANCELLED = "Cancelled"

class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity: int):
        self.stock -= quantity

class OrderDetails:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

class Order:
    def __init__(self, user: User, order_details: List[OrderDetails]):
        self.user = user
        self.order_details = order_details
        self.status = OrderStatus.PENDING
        self.date_created = datetime.now()
        self.payment = None

    def calculate_total(self):
        return sum(detail.product.price * detail.quantity for detail in self.order_details)

    def add_payment(self, payment):
        self.payment = payment
        self.status = OrderStatus.COMPLETED

    def update_status(self, new_status: OrderStatus):
        self.status = new_status

    def confirm_order(self):
        for detail in self.order_details:
            detail.product.update_stock(detail.quantity)
        self.status = OrderStatus.COMPLETED

class Payment:
    def __init__(self, order: Order, amount: float, payment_date: datetime = datetime.now()):
        self.order = order
        self.amount = amount
        self.payment_date = payment_date

    def process_payment(self):
        if self.amount == self.order.calculate_total():
            self.order.add_payment(self)
        else:
            raise ValueError("Payment amount does not match the order total.")
