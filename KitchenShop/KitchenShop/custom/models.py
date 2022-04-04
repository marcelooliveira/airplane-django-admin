from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.description}"

class Product(models.Model):
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.description}"

class Inventory(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )    
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(1000000)])

    class Meta:
        verbose_name_plural = "Inventories"

    def __str__(self):
        product_description = Product.objects.filter(id=self.product.id)[0].description
        return f"{product_description}, qty: {self.quantity}, unit price: ${self.unit_price:2}"

