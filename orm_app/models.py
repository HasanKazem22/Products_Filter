from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Brands(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Warranty(models.Model):
    Warranty = (
        ('1 Year', '1 Year'),
        ('2 Years', '2 Years'),
    )

    year = models.CharField(max_length=200, choices=Warranty)

    def __str__(self):
        return self.year

class Filter_Price(models.Model):
    Filter_Price = (
        ('1000 To 10000', '1000 To 10000'),
        ('10000 To 20000', '10000 To 20000'),
        ('20000 To 30000', '20000 To 30000'),
        ('30000 To 40000', '30000 To 40000')
    )

    price = models.CharField(max_length=200, choices=Filter_Price)

    def __str__(self):
        return self.price


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    date = models.DateTimeField(auto_created=True)

    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE)
    warranty = models.ForeignKey(Warranty, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)

    def __str__(self):
        return self.name