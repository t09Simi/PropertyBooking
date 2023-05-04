from django.test import TestCase

from datetime import datetime
from property.models import Customer, Property, Room, Booking


class ModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(username='John Doe', email='johndoe@example.com')
        self.property = Property.objects.create(name='Cozy Apartment', neighbourhood='Brooklyn',
                                                number_of_reviews=20, latitude=40.775807, longitude=-73.955752)
        self.room = Room.objects.create(room_type='Private room', property=self.property, price=500, number_of_beds=1, availability='True', )
        self.booking = Booking.objects.create(customer=self.customer, property=self.property, room=self.room,
                                              check_in='2023-05-10', check_out='2023-05-15',
                                              )

    def test_booking_customer(self):
        self.assertEqual(str(self.booking.customer), 'John Doe')

    def test_booking_property(self):
        self.assertEqual(str(self.booking.property), 'Cozy Apartment')

    def test_booking_room(self):
        self.assertEqual(str(self.booking.room), 'Private room')

    def test_booking_check_in_date(self):
        self.assertEqual(str(self.booking.check_in), '2023-05-10')

    def test_booking_check_out_date(self):
        self.assertEqual(str(self.booking.check_out), '2023-05-15')

    def test_booking_total_price(self):
        self.assertEqual(self.booking.price, 500)

