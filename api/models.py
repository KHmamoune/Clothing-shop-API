from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    product_type = models.CharField(max_length=255)
    date_of_addition = models.DateField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=255)
    quantity = models.IntegerField()
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.size


class Promotion(models.Model):
    sale = models.FloatField()
