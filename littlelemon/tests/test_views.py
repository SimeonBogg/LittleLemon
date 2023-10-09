from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu, Booking

class MenuItemsViewTestCase(TestCase):
    def setUp(self):
        
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_menu_items_view(self):
        
        menu_item1 = Menu.objects.create(name='Item 1', price=10.0)
        menu_item2 = Menu.objects.create(name='Item 2', price=15.0)

        response = self.client.get(reverse('menu-items-list'))

        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

       
        self.assertContains(response, 'Item 1')
        self.assertContains(response, 'Item 2')

class BookingViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_booking(self):
        
        data = {
            'name': 'Test Booking',
            'no_of_guests': 4,
            'booking_date': '2023-10-31T19:30:00Z'
        }
        response = self.client.post(reverse('booking-list'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_bookings(self):

        booking1 = Booking.objects.create(name='Booking 1', no_of_guests=2)
        booking2 = Booking.objects.create(name='Booking 2', no_of_guests=3)

        response = self.client.get(reverse('booking-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, 'Booking 1')
        self.assertContains(response, 'Booking 2')
