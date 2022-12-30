from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField (max_length=900)
    price = models.IntegerField()
    text = models.TextField(max_length=1993)
    image = models.ImageField(blank=True,null=True)
    def  __str__(self):
        return self.title
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product

class Category(models.Model):
    product = models .ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
