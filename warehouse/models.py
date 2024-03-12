from django.db import models
from decimal import Decimal


class Material(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return self.name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self) -> str:
        return f"{self.product.name} {self.material.name}"


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    reminder = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.material}"
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.product}"    

