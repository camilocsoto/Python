import json
new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accessories",
    "entry_date": "2024-07-01"
}

with open("products.json", "r") as file:
    products = json.load(file)
    for product in products:
        print(product)