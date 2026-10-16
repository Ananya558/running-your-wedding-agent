import csv

VENDOR_FILE = "data/vendors.csv"

# Columns that hold numbers (everything else stays as text)
NUMBER_COLUMNS = [
    "price_min", "price_max", "starting_price",
    "capacity_min", "capacity_max",
]


def load_vendors():
    """Read vendors.csv and return a list of vendors (one dictionary each)."""
    vendors = []

    with open(VENDOR_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            for column in NUMBER_COLUMNS:
                if row[column] == "NA":
                    row[column] = None
                else:
                    row[column] = int(row[column])
            vendors.append(row)

    return vendors


# This part only runs when you run this file directly (for testing)
if __name__ == "__main__":
    vendors = load_vendors()
    print(f"Loaded {len(vendors)} vendors")

    first = vendors[0]
    print("\nFirst vendor:")
    print("  Name:", first["vendor_name"])
    print("  City:", first["city"])
    print("  Price per plate:", first["price_min"], "to", first["price_max"])
    print("  Capacity:", first["capacity_min"], "to", first["capacity_max"])
    print("  Price as a number? ", type(first["price_min"]))