from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField (max_length=900)
    price = models.IntegerField()
    text = models.TextField(max_length=1993)

    def  __str__(self):
        return self.title
class Review(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product
