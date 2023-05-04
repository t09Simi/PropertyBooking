import csv
import os
import random
from pathlib import Path
from django.db import models
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from property.models import Customer, Property, Room, Booking, Payment, PropertyEval

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table
        Property.objects.all().delete()
        Room.objects.all().delete()
        Booking.objects.all().delete()
        Payment.objects.all().delete()
        PropertyEval.objects.all().delete()
        Customer.objects.all().delete()
        User.objects.all().delete()
        print("table dropped successfully")

        fake = Faker()

        #Create customers using faker
        for i in range(10):
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            username = first_name + last_name,
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=fake.ascii_free_email(),
                password='p@ssw0rd')
            customer = Customer.objects.get(user=user)
            customer.save()


        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/property/NYC_PropertyData/AB_NYC_2019 - AB_NYC_2019.csv', encoding='utf-8', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line
            for row in reader:
                # Creating room object
                room = Room.objects.create(
                    room_type=(row[6]),
                    price=(row[7]),
                )
                room.save()

                # Creating property object
                property = Property.objects.create(
                    name=(row[0]),
                    neighbourhood_group=(row[2]),
                    neighbourhood=(row[3]),
                    number_of_reviews=(row[9]),
                    latitude=(row[4]),
                    longitude=(row[5]),
                    room=room,
                )
                property.save()


                # Creating Booking object
                booking = Booking.objects.create(
                    property=property,
                )
                booking.save()

                #Creating Payment object
                payment = Payment.objects.create(
                    booking=booking,
                )
                payment.save()

                # Creating PropertyEval object
                propertyeval = PropertyEval.objects.create(
                    name=(row[0]),
                    room_type=(row[6]),
                    price=(row[7]),
                    neighbourhood=(row[3]),
                    number_of_reviews=(row[9]),
                    available=(row[13]),
                    host_name=(row[1]),
                    neighbourhood_group=(row[2]),
                    minimum_nights=(row[8]),
                )
                propertyeval.save()

        print("data parsed successfully")
