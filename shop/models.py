from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os 
from django.core.files.storage import FileSystemStorage





class Product(models.Model):
    name = models.TextField(max_length=128)
    description = models.TextField(max_length=10000)
    price = models.FloatField()
    amount = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='img/')
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tovars = models.ManyToManyField(Product)
    date = models.DateTimeField(default=datetime.now, blank=True)
    pay = models.BooleanField(default=False)





    






