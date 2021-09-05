from gallery.models import Category, Image, Location
from django.test import TestCase

# Create your tests here.

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.image_category=Category(Categories='food')
        self.image_category.save_category()

        self.image_location=Location(place='Gelegele')
        self.image_location.save_location()

        self.image=Image(id=1, img_name='hyke1', description='a picture of our first hyke', image_location=self.image_location, image_category=self.image_category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        saved=Image.objects.all()
        self.assertTrue(len(saved) > 0)   

    def test_delete_image(self):
        self.image.delete_image()
        deleted=Image.objects.all()
        self.assertTrue(len(deleted) == 0) 

    def test_search_by_category(self):
        image_category='food'
        result=self.image.search_by_category(image_category)
        self.assertTrue(len(result) >=0)

class TestCategoryClass(TestCase):
    def setUp(self):
        self.image_category=Category(Categories='food')
        self.image_category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_category, Category))

    def test_save_category(self):
        self.image_category.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_category(self):
        self.image_category.delete_category()
        category=Category.objects.all()
        self.assertTrue(len(category) ==0)

class TestLocationClass(TestCase):
    def setUp(self):
        self.image_location=Location(place='Gelegele')
        self.image_location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_location, Location))

    def test_save_location(self):
        self.image_location.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_location(self):
        self.image_location.delete_location()
        location=Location.objects.all()
        self.assertTrue(len(location) ==0)


