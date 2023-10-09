from django.test import TestCase
from restaurant.models import Booking, Menu

class BookingModelTestCase(TestCase):
    def test_booking_creation(self):
        booking = Booking.objects.create(
            name="Test Booking",
            no_of_guests=4,
            booking_date="2023-10-31T19:30:00Z"
        )
        self.assertEqual(booking.name, "Test Booking")
        self.assertEqual(booking.no_of_guests, 4)

class MenuModelTestCase(TestCase):
    def test_menu_creation(self):
        menu_item = Menu.objects.create(
            title="Test Menu Item",
            price=9.99,
            inventory=10
        )
        self.assertEqual(menu_item.title, "Test Menu Item")
        self.assertEqual(menu_item.price, 9.99)