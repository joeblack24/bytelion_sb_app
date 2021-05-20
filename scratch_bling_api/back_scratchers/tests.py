from django.test import TestCase
from .models import BackScratchers, Size
# Create your tests here.

class BackScratcherTestCase(TestCase):
    def test_back_scratcher(self):
        self.back_scratcher = BackScratchers(name='Test Scratcher', description='Testing')
        self.assertEqual(self.back_scratcher.name, 'Test Scratcher')
        self.assertEqual(self.back_scratcher.description, 'Testing')

    def test_size(self):
        self.test_size = Size()
        self.test_size.size = 'S'
        self.assertEqual(self.test_size.size, 'S')