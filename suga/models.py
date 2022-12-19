from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField (max_length=900)
    price = models.IntegerField()
    text = models.TextField(max_length=1993)

    def  __str__(self):
        return self.title

