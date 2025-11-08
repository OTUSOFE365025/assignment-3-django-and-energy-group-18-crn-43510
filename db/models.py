import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()

# Product model
class Product(models.Model):
    upc_code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        return f'{self.name} (${self.price})'