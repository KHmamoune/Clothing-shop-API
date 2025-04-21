from django.db import models
from django.contrib.auth.models import User as AuthUser

class User(AuthUser):
    phone_number = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    product_type = models.CharField(max_length=255)
    date_of_addition = models.DateField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Size(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=255)
    quantity = models.IntegerField()
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.size


class Promotion(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.FloatField()

