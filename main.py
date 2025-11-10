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

# Import necessary modules
# Using tkinter for GUI and random for simulating scans
import random
import tkinter as tk        # GUI library
from tkinter import ttk     # For themed buttons, labels, etc.

# Create a few products in the database
Product.objects.update_or_create(upc_code=12345, name='Coffee', price=8.32)
Product.objects.update_or_create(upc_code=67890, name='Muffin', price=2.50)
Product.objects.update_or_create(upc_code=54321, name='Sandwich', price=5.75)
Product.objects.update_or_create(upc_code=98765, name='Juice', price=3.20)
Product.objects.update_or_create(upc_code=13579, name='Donut', price=1.99)

# Cash Register Application
class CashRegisterApp:
    def __init__(self, root):

        # Set up main window
        self.root = root
        self.root.title("Cash Register Scanner")    # Window title

        # Store scanned items
        self.scanned_items = []
        self.products = list(Product.objects.all())

        # Header for the application window
        ttk.Label(root, text="Cash Register", font=("Arial", 16, "bold")).pack(pady=10)

        # List of scanned products
        self.items_box = tk.Text(root, width=40, height=10, state='disabled', wrap='none')
        self.items_box.pack(pady=10)

        # UPC input field
        ttk.Label(root, text="Enter UPC Code:").pack()
        self.upc_entry = ttk.Entry(root, width=20)
        self.upc_entry.pack(pady=5)

        # Subtotal display at the bottom of window
        self.subtotal_var = tk.StringVar(value="Subtotal: $0.00")
        ttk.Label(root, textvariable=self.subtotal_var, font=("Arial", 12, "bold")).pack(pady=10)

        # Scan button
        ttk.Button(root, text="Scan Item", command=self.scan_item).pack(pady=5)

    def scan_item(self):

        upc_code = self.upc_entry.get().strip()

        try:
            # Try to get product from DB
            product = Product.objects.get(upc_code=upc_code)
            self.scanned_items.append(product)

            # Update subtotal
            subtotal = sum(p.price for p in self.scanned_items)

            # Update scanned list
            self.items_box.config(state='normal')
            self.items_box.insert('end', f"{product.name}\t${product.price:.2f}\n")
            self.items_box.config(state='disabled')

            # Update subtotal label
            self.subtotal_var.set(f"Subtotal: ${subtotal:.2f}")

            # Clear entry box
            self.upc_entry.delete(0, 'end')

        except Product.DoesNotExist:
            # If UPC not found in DB
            self.items_box.config(state='normal')
            self.items_box.insert('end', f"UPC {upc_code} not found.\n")
            self.items_box.config(state='disabled')
            self.upc_entry.delete(0, 'end')

        except ValueError:
            # If the UPC is not a number
            self.items_box.config(state='normal')
            self.items_box.insert('end', f"Invalid UPC: '{upc_code}' (must be numeric)\n")
            self.items_box.config(state='disabled')

        finally:
            # Always clear entry box after scanning
            self.upc_entry.delete(0, 'end')

if __name__ == "__main__":
    root = tk.Tk()
    app = CashRegisterApp(root) # Create cash register instance
    root.mainloop()
