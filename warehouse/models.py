from django.db import models
from shop.models import Product

ZONE_CHOICES = (
    ('RED ZONE', 'R'),
    ('ORANGE ZONE', 'O'),
    ('GREEN ZONE', 'G')
)

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
)

SLOT_CHOICES = (
    ('Morning Slot', 'Morning  {8 am - 12 pm}'),
    ('Noon Slot', 'Noon {12 pm - 7 pm}'),
    ('Night Slot', 'Night {7 pm - 11 pm}'),
)


class Warehouse(models.Model):
    location = models.CharField(
        max_length=100, choices=CITY_CHOICES, null=True)
    zone = models.CharField(max_length=30, choices=ZONE_CHOICES, null=True)
    loc_x = models.DecimalField(max_digits=10, decimal_places=6)
    loc_y = models.DecimalField(max_digits=10, decimal_places=6)
    time_slot = models.CharField(
        max_length=100, choices=SLOT_CHOICES, null=False, default='Noon {12 pm - 7 pm}')


class KeyVal(models.Model):
    locname = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
