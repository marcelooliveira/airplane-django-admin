from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
class Product(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Products"

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)