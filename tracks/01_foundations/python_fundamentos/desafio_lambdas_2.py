products = [
    {"name": "Keyboard", "price": 150.0},
    {"name": "Mouse", "price": 80.0},
    {"name": "Monitor", "price": 900.0},
    {"name": "Headset", "price": 250.0},
]

def apply_discount(products, percentage):
    new_products = []
    for product in products:
        discount_amount = product['price'] * (percentage / 100)
        new_price = product['price'] - discount_amount

        new_product = {
            "name": product["name"],
            "price": new_price,
        }
        new_products.append(new_product)
    return new_products

def sort_by_price(products):
    return sorted(products, key=lambda p: p['price'])
