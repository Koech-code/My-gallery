from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Category(models.Model):
    Categories=models.TextField(max_length=25)
    

class Location(models.Model):
    place= models.CharField(max_length=30)


class Image(models.Model):
    image= models.ImageField(upload_to='images/')
    name= models.CharField(max_length=20)
    description=models.TextField(max_length=200)
    image_category=models.ForeignKey(Category, on_delete=CASCADE)
    image_location=models.ForeignKey(Location, on_delete=CASCADE)

    