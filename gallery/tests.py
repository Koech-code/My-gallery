from gallery.models import Category, Image, Location
from django.test import TestCase

# Create your tests here.

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category=Category()
        self.category.save_category()

        self.location=Location()
        self.location.save_location()

        self.image=Image(id=1, img_name='hyke1', description='a picture of our first hyke', location=self.location, category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        saved=Image.objects.all()
        self.assertTrue(len(saved) > 0)   

    def test_delete_image(self):
        self.image.delete_image()
        deleted=Image.objects.all()
        self.assertTrue(len(deleted) > 0) 

    