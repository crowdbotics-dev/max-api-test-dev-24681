from django.conf import settings
from django.db import models


class Product(models.Model):
    "Generated Model"
    product_name = models.CharField(
        max_length=10,
    )
    price = models.FloatField()
