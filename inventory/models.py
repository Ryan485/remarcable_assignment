# Author : Ryan Song

from django.db import models


class Category(models.Model):
    """
    Represents a product category in the inventory
    """
    
    name = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    Represents a tag used to label products in the inventory
    """
    name = models.CharField(max_length = 100)


    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Represents a Product in the inventory
    """
    name = models.CharField(max_length = 100)
    description = models.TextField()

    # used PROTECT to avoid deleting categories that still have products in them
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name
