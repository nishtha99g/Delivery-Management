from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from warehouse.models import Warehouse

class Profile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)
    date_birth = models.DateField(default=datetime.date.today, blank=True)
    shopkeeper = models.BooleanField(default=False)
    warehouse=models.ForeignKey(Warehouse,on_delete=models.CASCADE,null=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
