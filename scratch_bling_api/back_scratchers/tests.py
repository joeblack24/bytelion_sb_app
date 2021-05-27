from django.test import TestCase
from .models import BackScratchers, Size
# Create your tests here.

class BackScratcherTestCase(TestCase):
    def test_back_scratcher(self):
        self.back_scratcher = BackScratchers(name='Test Scratcher', description='Testing')
        self.test_size = Size()
        self.test_size.size = 'S'
        self.test_size.save()
        self.back_scratcher.save()
        self.back_scratcher.size.set([self.test_size])
        self.assertEqual(self.back_scratcher.name, 'Test Scratcher')
        self.assertEqual(self.back_scratcher.description, 'Testing')
        self.assertIsNotNone(self.back_scratcher.size)

    def test_size(self):
        self.test_size = Size()
        self.test_size.size = 'S'
        self.assertEqual(self.test_size.size, 'S')