import csv
import json

USD_TO_INR = 83

clean_data = []
seen = set()

with open("sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        pid, product, price, country = row

        # Remove quotes from product
        product = product.replace('"', '').strip()

        # Remove $ from price and convert to float
        price = price.replace("$", "").strip()
        price = float(price)

        # Remove duplicates (same product + price)
        key = (product, price)
        if key in seen:
            continue
        seen.add(key)

        # Convert USD to INR
        price_inr = price * USD_TO_INR

        clean_data.append({
            "id": int(pid),
            "product": product,
            "price_inr": price_inr,
            "country": country.strip()
        })

# Save into JSON file
with open("clean_sales.json", "w") as jf:
    json.dump(clean_data, jf, indent=4)

print("clean_sales.json created successfully!")
