from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from shop.models import Product
from warehouse.models import Warehouse

CITY_CHOICES = (
    ('Bhim Colony', 'Bhim Colony'),
    ('Basai Enclave-2', 'Basai Enclave-2'),
    ('Chandan Vihar', 'Chandan Vihar'),
    ('Ganga Vihar', 'Ganga Vihar'),
    ('Sai Kunj', 'Sai Kunj'),
    ('Shri Ram Colony', 'Shri Ram Colony'),
    ('Amanpura Colony', 'Amanpura Colony'),
    ('Patel Nagar Ext', 'Patel Nagar Ext'),
    ('Shiv Nagar', 'Shiv Nagar'),
    ('Vikas Nagar', 'Vikas Nagar'),
    ('Basai Enclave Ext', 'Basai Enclave Ext'),
    ('Krishna Nagar', 'Krishna Nagar'),
    ('Surya Vihar', 'Surya Vihar'),
    ('Ashok Vihar', 'Ashok Vihar'),
    ('Rajeev colony', 'Rajeev colony'),
    ('Nihal Vihar', 'Nihal Vihar'),
    ('Mayur Kunj', 'Mayur Kunj'),
    ('Ryan Enclave', 'Ryan Enclave'),
    ('Shyam Kunj', 'Shyam Kunj'),
    ('Shanti Kunj', 'Shanti Kunj'),
    ('Mohan Nagar', 'Mohan Nagar'),
    ('Vatika Kunj', 'Vatika Kunj'),
    ('Defense Enclave', 'Defense Enclave'),
    # ('Agra', 'Agra'),
    # ('Meerut', 'Meerut'),
    # ('Madurai', 'Madurai'),
    # ('Guwahati', 'Guwahati'),
    # ('Thiruvananthapuram', 'Thiruvananthapuram'),
    # ('Tiruchchirappalli', 'Tiruchchirappalli'),
    # ('Kota', 'Kota'),
    # ('Jammu', 'Jammu'),
    # ('Mangalore', 'Mangalore'),
    # ('Ajmer', 'Ajmer'),
    # ('Shillong', 'Shillong'),
    # ('New Delhi', 'New Delhi')
)

SLOT_CHOICES = (
    ('Morning Slot', 'Morning  {8 am - 12 pm}'),
    ('Noon Slot', 'Noon {12 pm - 7 pm}'),
    ('Night Slot', 'Night {7 pm - 11 pm}'),
)


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user', null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100, choices=CITY_CHOICES, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    time_slot = models.CharField(
        max_length=100, choices=SLOT_CHOICES, null=False)

    class Meta:
        ordering = ('-created',)

    def _str_(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.item.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    selected_shop = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
