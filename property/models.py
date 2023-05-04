from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username},{self.user.email}'

    class Meta:
        db_table = 'customer'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.customer.save()

class Property(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    neighbourhood_group = models.CharField(max_length=30, null=True, blank=True)
    neighbourhood = models.CharField(max_length=15, null=True, blank=True)
    number_of_reviews = models.IntegerField()
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name},{self.neighbourhood_group},{self.neighbourhood},{self.number_of_reviews},{self.latitude},{self.longitude}'

class Room(models.Model):
    room_type = models.CharField(max_length=30, null=True, blank=True)
    property = models.ForeignKey(Property, related_name="property_name", on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(default=80)
    number_of_beds = models.IntegerField(default=1)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.room_type},{self.property},{self.availability},{self.price},{self.number_of_beds}'
class Booking(models.Model):
    user = models.ForeignKey(Customer, related_name="booking_user", on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, related_name="room_booking", on_delete=models.CASCADE, null=True, blank=True)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user},{self.room},{self.check_in},{self.check_out}'

class Payment(models.Model):
    booking = models.ForeignKey(Booking, related_name="booking_details", on_delete=models.CASCADE, null=True, blank=True)
    transaction_id = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'{self.booking},{self.transaction_id}'

class PropertyEval(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    host_name = models.CharField(max_length=20, null=True, blank=True)
    neighbourhood_group = models.CharField(max_length=30, null=True, blank=True)
    neighbourhood = models.CharField(max_length=20, null=True, blank=True)
    room_type = models.CharField(max_length=30, null=True, blank=True)
    price = models.IntegerField(default=80)
    number_of_reviews = models.IntegerField(null=True, blank=True)
    minimum_nights = models.IntegerField(null=True, blank=True)
    available = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name},{self.host_name},{self.neighbourhood_group},{self.room_type},{self.price},{self.neighbourhood},{self.number_of_reviews},{self.minimum_nights},{self.available}'



