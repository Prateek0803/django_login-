from django.db import models

# Create your models here.

class Customer(models.Model):
     email = models.EmailField(max_length = 254)
     phone = models.IntegerField(max_length=10)
     password = models.CharField(max_length = 30)

     def __str__(self):
         return self.email
