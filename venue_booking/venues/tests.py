# venues/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Venue, Category
from venues.models import CustomUser

class VenueCreationTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')

    def test_venue_creation(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('create_venue'), {
            'name': 'Test Venue',
            'description': 'A test venue',
            'category': self.category.id,
            'capacity': 100,
            'price_per_hour': 50.00,
            'address': '123 Test St',
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertTrue(Venue.objects.filter(name='Test Venue').exists())