# Beginner Inventory & Sales Tracking System
import json
import os
inventory = {}

sales = []

def add_product(name, stock, price, threshold):
    inventory[name] = {'stock': stock, 'price': price, 'threshold': threshold}
    print(f"Added {name} to inventory.")

def record_sale(product, quantity):
    if product not in inventory:
        print("Product not found.")
        return
    if inventory[product]['stock'] < quantity:
        print("Not enough stock for this sale.")
        return
    inventory[product]['stock'] -= quantity
    total = quantity * inventory[product]['price']
    sales.append({'product': product, 'quantity': quantity, 'total': total})
    print(f"Sale recorded: {quantity} x {product}")
    check_stock_alert(product)

def check_stock_alert(product):
    if inventory[product]['stock'] <= inventory[product]['threshold']:
        print(f"Alert: {product} stock is low ({inventory[product]['stock']} left).")

def print_sales_report():
    print("\nSales Report")
    for sale in sales:
        print(f"{sale['quantity']} x {sale['product']} = ₹{sale['total']:.2f}")

# Example usage
add_product('Shirt', 10, 499.0, 2)
add_product('Trousers', 5, 799.0, 1)
record_sale('Shirt', 10)
record_sale('Trousers', 5)
print_sales_report()