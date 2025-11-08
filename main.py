############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Create a few products in the database
Product.objects.update_or_create(upc_code=12345, name='Coffee', price=8.32)
Product.objects.update_or_create(upc_code=67890, name='Muffin', price=2.50)
Product.objects.update_or_create(upc_code=54321, name='Sandwich', price=5.75)
Product.objects.update_or_create(upc_code=98765, name='Juice', price=3.20)
Product.objects.update_or_create(upc_code=13579, name='Donut', price=1.99)

# Simulate Scanner
scanning = True

scanned_items = []  # List to hold scanned items

while(scanning):

    user_input = input("Enter UPC code (or 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        scanning = False
    else:
        try:
            upc = int(user_input)
            product = Product.objects.get(upc_code=upc)
            
            # Add item to scanned list and print subtotal
            scanned_items.append(product)
            print(f'Add product to subtotal: {product.name} - Price: ${product.price}')
            print(f'Current subtotal: ${sum(p.price for p in scanned_items)}\n')
        except Product.DoesNotExist:
            print('Product not found. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a valid UPC code.')

# Print receipt
print('\nScanned Items:')

for p in scanned_items:
    print(f'Item: {p.name} \tPrice: ${p.price}')

total = sum(p.price for p in scanned_items)
print(f'\nSubtotal: ${total:.2f}')
